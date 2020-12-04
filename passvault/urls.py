from django.urls import path
from . import views

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
]