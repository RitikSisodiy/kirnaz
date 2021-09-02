from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    # path('basic/', views.basic,name='basic'),
    path('another/', views.another,name='another'),
    path('blogpage/', views.blogpage,name='blogpage'),
    path('chatbox/', views.chatbox,name='chatbox'),
    path('companyregistration/', views.companyregistration,name='companyregistration'),
    path('incometaxfilling/', views.incometaxfilling,name='incometaxfilling'),
    path('login/', views.Login,name='login'),
    path('memberlogin/', views.memberlogin,name='memberlogin'),
    path('membersignup/', views.membersignup,name='membersignup'),
    path('newsfeed/', views.newsfeed,name='newsfeed'),
    path('pvtltdreg/', views.pvtltdreg,name='pvtltdreg'),
    # path('privateltdreg/', views.privateltdreg,name='privateltdreg'),
    path('signup/', views.signup,name='signup'),
    path('signup1/', views.signup1,name='signup1'),
    path('signup2/', views.signup2,name='signup2'),
    path('logindashboard', views.logindashboard, name="logindashboard"),
    path('payment/', views.payment, name="payment"),
    path('handlerequest/', views.handelrequest, name="handelrequest"),
    path('services/', views.services, name="services"),
    path('profile/', views.profile, name="profile"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('profile/changepass/', views.changepass, name="changepass"),
    path('profile/documents', views.documents, name="documents"),
    path('profile/bookings', views.bookings, name="bookings"),
    path('getdoclist',views.getdoclist,name='getdoclist'),
    path('blog/<slug:slug>/', views.blog,name='blog'),
    path('blog/<slug:slug>/<int:id>', views.blog,name='singleblog'),

]