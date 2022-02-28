from chat.models import Status, user,conversation,convofiles
from django.contrib import admin
# Register your models here.
admin.site.register(user)
admin.site.register(conversation)
admin.site.register(Status)
admin.site.register(convofiles)