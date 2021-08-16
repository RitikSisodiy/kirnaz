from django.contrib import admin
from . models import *

# Register your models here
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display=('objective','obj_details','img')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display= ('news',)

@admin.register(DueDateReminder)
class DueDateReminderAdmin(admin.ModelAdmin):
    list_display= ('date','details')

@admin.register(BlogNews)
class BlogNewsAdmin(admin.ModelAdmin):
    list_display= ('news',)

@admin.register(Offrings)
class OffringsAdmin(admin.ModelAdmin):
    list_display= ('title','details','img')
@admin.register(headbanner)
class OffringsAdmin(admin.ModelAdmin):
    list_display= ('banner_title','banner_content',)


