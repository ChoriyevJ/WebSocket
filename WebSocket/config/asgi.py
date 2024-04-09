from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from django.core.asgi import get_asgi_application
from django.urls import path, re_path
from chat.consumers import ChatConsumer

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourproject.settings')


asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': asgi_application,
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/chat/room/(?P<course_id>\d+)/$', ChatConsumer.as_asgi())
        ])
    )
})
