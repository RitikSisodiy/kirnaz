from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from chat import consumer
from channels.auth import AuthMiddlewareStack    
application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
          path("chat/<str:username>",consumer.ChatClassConsumer.as_asgi()),
          path("chat/",consumer.EchoClassConsumer.as_asgi())
    ])
    )
})
