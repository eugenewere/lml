# import asyncio
# import json
# from django.contrib.auth import get_user_model
# from channels.consumer import AsyncConsumer
# from channels.db import database_sync_to_async
# from lmlappadmin.models import *
#


# class ChatConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("connected", event)
#         await self.send({"type": "websocket.accept", })
#         other_user = self.scope['url_route']['kwargs']['username']
#         me = self.scope['user']
#         user1 =  User.objects.filter(username=other_user).first()
#         user2 =  User.objects.filter(username=me).first()
#         # print(user, user2)
#         thread_obj = await self.get_thread(user1.username, user2.username)
#         chat_room = "thread_".format(thread_obj)
#         self.chat_room = chat_room
#         await  self.channel_layer.group_add(
#             chat_room,
#             self.channel_name
#         )
#
#         # await asyncio.sleep(10)
#         # await self.send({"type":"websocket.close",})
#
#
#     @database_sync_to_async
#     def get_thread(self, user, other_username):
#         return Thread.objects.get_or_new(reciever__username=user, sender__username=other_username)
#
#     async def websocket_receive(self, event):
#         print('receive', event)
#         front_text = event.get('text', None)
#
#         if front_text is not None:
#             loaded_dict_data = json.loads(front_text)
#             msg = loaded_dict_data.get('message')
#             customer = loaded_dict_data.get('customer')
#             cust = Customer.objects.filter(id=customer).first()
#             customer_img = cust.profile_image.url
#
#
#             my_Response = {
#                 "message":msg,
#                 "customer":customer,
#                 "image":customer_img,
#
#             }
#             new_event={
#                 "type": "websocket.send",
#                 "text": json.dumps(my_Response),
#             }
#             await self.channel_layer.group_send(
#                 self.chat_room,
#                 {
#                     'type':'chat_message',
#                     'messsage':'helloworld',
#                 }
#             )
#             # await self.send({})
#         async def chat_message(self, event):
#             print('message', event)
#     async def websocket_disconnect(self, event):
#         print('disconnected', event)

















from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from lmlappadmin.models import *
class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        messages= Message.objects.all()
        content={
            'messages':self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_messages(self, data):

        s1 = json.dumps(data)
        data = json.loads(s1)
        d = data['text']
        e = json.loads(d)

        sender = e['sender']
        receiver = e['receiver']
        message_content = e['message']

        sender_user = User.objects.filter(id=sender).first()
        receiver_user = User.objects.filter(id=receiver).first()
        message = Message.objects.create(
            sender=sender_user,
            msg_content=message_content,
            reciever=receiver_user,
        )
        content ={
            'command':'new_messages',
            'message' :self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        results=[]
        for message in messages:
            results.append(self.message_to_json(message))
        return results
    def message_to_json(self, message):
        comany = Company.objects.filter(user_ptr_id= message.sender.id).first()
        customer = Customer.objects.filter(user_ptr_id= message.reciever.id).first()
        return {
            'sender':message.sender.username,
            'reciever':message.reciever.username,
            'message':message.msg_content,
            'created_at':str(message.created_at),
            'sImage': comany.logo.url,
            'rImage': customer.profile_image.url
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_messages': new_messages,
    }


    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['username']
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
    def websocket_receive(self, text_data):
        s1 = json.dumps(text_data)
        data = json.loads(s1)
        d = data['text']
        e =json.loads(d)
        # print(e['command'])
        self.commands[e['command']](self, data)



        # print(data['command'])
    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'fetch_messages',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    # def chat_message(self, event):
    #     message = event['message']
    #     # Send message to WebSocket
    #     self.send(text_data=json.dumps(message))