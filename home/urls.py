from django.urls import path
from . import views


urlpatterns = [

    path('signuppage/',views.signuppage,name = "signuppage"),
    path("",views.homepage,name='homepage'),
    path('welcome/',views.welcome,name = "welcome"),
    path('logout_user/',views.logout_user,name="logout_user"),
    path('adminlogin/',views.admin_login,name = "adminlogin"),
    path('admin_userlist/',views.admin_userlist,name = "admin_userlist"),
    path('add_user/',views.add_user,name ='add_user'),
    path('update_user/',views.update_user,name='update_user'),
    path('delect_user/',views.delect_user,name='delect_user')
   
]


