from django.urls import path
from . import views


urlpatterns = [
    
    # path('<slug:slug>', views.regis, name = 'registration'),
    path('<slug:slug1>/', views.taxfiling, name = 'taxfiling'),
   

]