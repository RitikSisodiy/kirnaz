from django.urls import path
from . import views


urlpatterns = [
    
    # path('<slug:slug>', views.regis, name = 'registration'),
    path('<slug:slug1>/<slug:slug2>/', views.regis, name = 'registration'),
   

]