from django.urls import path
from . import views,otherNavViews
urlpatterns = [
    path('', views.index, name="dindex"),
    path('registration', views.registration, name="dregistration"),
    path('registrationdelete/', views.deleteregistration, name="dsdeleteregistration"),
    path('registration/<slug:slug>', views.registration, name="dsregistration"),
    path('registration/edit/<slug:slug1>/<slug:slug2>', views.editregistration, name="dseditregistration"),
    # path('othernavs', otherNavViews.othernavs, name="dothernavs"),
    path('othernavsdelete/', otherNavViews.deleteothernavs, name="dsdeleteothernavs"),
    # path('othernavs/<slug:slug>', otherNavViews.othernavs, name="dsothernavs"),
    path('othernavs/edit/<slug:slug1>/<slug:slug2>', otherNavViews.editothernavs, name="dseditothernavs"),
    
]