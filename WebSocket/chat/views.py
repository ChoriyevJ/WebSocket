from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from course.models import Course
from .forms import LoginForm


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Successfully logged in')
                    course = Course.objects.all().first()
                    if request.user.courses.filter(id=course.id).exists():
                        pass
                    else:
                        course.users.add(request.user)
                        course.save()
                        request.user.save()
                    return redirect('chat:course_chat_room', 1)
                else:
                    return HttpResponse('User is not active')
            else:
                return HttpResponse('User is invalid')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html',
                  {'form': form})


@login_required
def course_chat_room(request, course_id):
    try:
        course = request.user.courses.get(id=course_id)
    except Exception as e:
        return HttpResponseForbidden("Sizda bunaqa imkoniyat macjud emas!")
    return render(request, 'chat/room.html', {'course': course})
