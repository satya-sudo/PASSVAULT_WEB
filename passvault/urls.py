from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views


urlpatterns = [
    path("",views.index,name='index'),
    path("TC",views.TC,name='TC'),
    path("login",views.login_view,name='login_view'),
    path("signup",views.register,name='register'),
    path('logout',views.logout_view,name='logout_view'),
    path('mainMenu',views.userMenu,name='userMenu'),
    path('AddCred',views.AddCred,name='AddCred'),
    path('search',views.search,name='search'),
    path('getAllPasswords',views.getallpassword,name='getallpassword'),
    path('editPassword/<int:id>',views.editPassword,name='editPassword'),


    path('reset_password',auth_views.PasswordResetView.as_view(template_name="passvault/reset_1.html"),name="reset_password"),
    path('resent_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="passvault/reset_2.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="passvault/reset_3.html"),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="passvault/reset_4.html"),name="password_reset_complete"),


]