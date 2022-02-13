import channels
from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import  User
from chat.models import Status
import json
from django.db.models import Count
# def getOrCreateGroup(user1,user2):
#     data = msgGroup.objects.filter(user__in=[user1,user2],type='p').distinct()
#     data = data.annotate(u_count=Count('user')).filter(u_count=2)
#     print(data)
#     if data.exists():
#         return data[0]
#     else:
#         thre = msgGroup.objects.create(type="p")
#         thre.user.add(user1)
#         thre.user.add(user2)
#         thre.save()
#         return thre

class ChatClassConsumer(SyncConsumer):
    def websocket_connect(self,event):
        self.user = self.scope['user']
        statusob,created = Status.objects.get_or_create(user=self.user)
        statusob.status= True
        statusob.save()
        self.sendOnlineuser()
        otherUserName = self.scope['url_route']['kwargs']['username']
        otheruser = User.objects.get(username=otherUserName)
        # self.Group = getOrCreateGroup(self.user,otheruser)
        # Group= self.Group
        if self.user.is_superuser:
            self.room_name = f"personalchat{otheruser.id}"
        else:
            self.room_name = f"personalchat{otheruser.id}"
        self.send({ 
            'type':'websocket.accept',
        })
        async_to_sync(self.channel_layer.group_add)(self.room_name,self.channel_name)
        print(f'[{self.channel_name}] you are connected')
    def websocket_receive(self,event):
        # print(f'[{self.channel_name}] - received - {event.get("text")}')
        msg = json.dumps({
            'message':"sent"
            })
        async_to_sync(self.channel_layer.group_send)(self.room_name,{
            "type":"websocket.message",
            "text":msg
        })
        # self.storeMessage(event.get('text'))
    def websocket_message(self,event):
        print(f'[{self.channel_name}] - message sent - {event.get("text")}')
        self.send({
            'type':'websocket.send',
            'text': event.get('text')
        })
    def websocket_disconnect(self,event):
        print("event is disconnected")
        async_to_sync(self.channel_layer.group_discard)(self.room_name,self.channel_name)
        self.user.status.status= False
        self.user.status.save()
        self.sendOnlineuser()
        print(f'[{self.channel_name}] you are disconnected')
        print(event)
    def storeMessage(self,text):
        Message.objects.create(
            Group=self.Group,
            sender=self.scope['user'],
            Text = text
        )
    def sendOnlineuser(self):
        onlineuser = Status.objects.filter(status=True).count()
        msg = json.dumps({
            "online":onlineuser
        })
        async_to_sync(self.channel_layer.group_add)("globle",self.channel_name)
        async_to_sync(self.channel_layer.group_send)("globle",{
            "type":"websocket.message",
            "text":msg
        })

class EchoClassConsumer(SyncConsumer):
    def websocket_connect(self,event):
        self.room_name = "broadcast"
        self.send({
            'type':'websocket.accept'
        })
        async_to_sync(self.channel_layer.group_add)(self.room_name,self.channel_name)
        print(f'[{self.channel_name}] you are connected')
    def websocket_receive(self,event):
        print(f'[{self.channel_name}] - received - {event.get("text")}')
        async_to_sync(self.channel_layer.group_send)(self.room_name,{
            "type":"websocket.message",
            "text":event.get('text')
        })
    def websocket_message(self,event):
        print(f'[{self.channel_name}] - message sent - {event.get("text")}')
        self.send({
            'type':'websocket.send',
            'text': event.get('text')
        })
    def websocket_disconnect(self,event):
        print("event is disconnected")
        async_to_sync(self.channel_layer.group_discard)(self.room_name,self.channel_name)
        print(f'[{self.channel_name}] you are disconnected')
        print(event)
