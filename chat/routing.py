from django.urls import re_path
from .consumers import RoomConsumer
from .middleware import WebSocketLogMiddleware

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", WebSocketLogMiddleware(RoomConsumer.as_asgi())),
]