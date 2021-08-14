from django.urls import path
from .import views
urlpatterns = [

    path('<slug:slug1>/<slug:slug2>/', views.handlenav , name="handlenav")
]