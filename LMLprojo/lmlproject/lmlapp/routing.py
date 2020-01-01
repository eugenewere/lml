# chat/routing.py
from django.urls import re_path, path
from .consumer import ChatConsumer, ChatConsumerCustomer

websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer),
    re_path(r"^employerdash_message/(?P<room_name>[\w.@+-]+)/$", ChatConsumer),
    re_path(r"^employeedash/(?P<room_name>[\w.@+-]+)/$", ChatConsumerCustomer),
]