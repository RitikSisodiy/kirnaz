from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('convologin/', views.Login,name='convologin'),
    path('logout', views.Logout,name='logout'),
    path('message/', views.message,name='sendmsg'),
    path('getmsg/>', views.getmsg,name='getmsg'),
]