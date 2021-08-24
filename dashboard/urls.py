from django.urls import path
from . import views,otherNavViews
urlpatterns = [
    path('', views.index, name="dindex"),
    path('registration/', views.registration, name="dregistration"),
    path('registration/contact', views.contact, name="drcontact"),
    path('registration/contact/delcontacts', views.delcontacts, name="delcontacts"),
    path('registrationdelete/', views.deleteregistration, name="dsdeleteregistration"),
    path('registration/<slug:slug>/', views.registration, name="dsregistration"),
    path('registration/edit/<slug:slug1>/<slug:slug2>/', views.editregistration, name="dseditregistration"),
    # path('othernavs', otherNavViews.othernavs, name="dothernavs"),
    path('othernavsdelete/', otherNavViews.deleteothernavs, name="dsdeleteothernavs"),
    # path('othernavs/<slug:slug>', otherNavViews.othernavs, name="dsothernavs"),
    path('othernavs/contact', otherNavViews.contact, name="orcontact"),
    path('othernavs/contact/delcontacts', otherNavViews.delcontacts, name="odelcontacts"),
    path('othernavs/edit/<slug:slug1>/<slug:slug2>/', otherNavViews.editothernavs, name="dseditothernavs"),
    path('adminchat/', views.adminchat, name="adminchat"),
    path('adminchat/<slug:slug1>/<int:id>/', views.adminchat, name="adminchatuser"),
    path('getmsg/<slug:slug1>/<int:id>/', views.getmsg, name="admingetmsg"),
    path('dashboardlogout/', views.dashboardlogout, name="dashboardlogout"),
    path('edithome/', views.edithome, name="edithome"),
    path('edithome/<slug:slug>/', views.edithome, name="edithomeslug"),
    path('deletehome/<slug:slug>/', views.deletehome, name="deletehomeslug"),
    path('viewicon/', views.viewicon, name="viewiconslug"),
    
]