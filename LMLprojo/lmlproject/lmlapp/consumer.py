# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from lmlappadmin.models import *

class ChatConsumer(WebsocketConsumer):
    def fetch_messges(self, data):
        messages = Message.objects.all()
        content={
            'messages':self.messages_to_json(messages)
        }
        return self.send_message(content)

    def new_message(self, data):
        sender = data['sender']
        reciever = data['reciever']

        sender_user = User.objects.filter(id=sender).first()
        reciever_user = User.objects.filter(id=reciever).first()
        message = Message.objects.create(
            sender=sender_user,
            reciever=reciever_user,
            msg_content=data['message']
        )
        content={
            'command':'new_message',
            'message':self.messages_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result =[]
        for message in messages:
            result.append(self.message_to_json(message))
        return result
    def message_to_json(self, message):
        return {
            'sender': message.sender.first_name,
            'reciever': message.reciever.first_name,
            'message':message.msg_content,
            'date_created': str(message.created_at)
        }

    commands = {
        'fetch_messages': fetch_messges,
        'new_messages':new_message,
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps(message))