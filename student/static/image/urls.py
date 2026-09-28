from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.Home,name='home'),
    path('Gadgets',views.Gadgets,name='Gadgets'),
    path('Search_Table',views. Search_Table,name=' Search_Table'),

    
    path('register',views.Register,name='register'),
    path('log',views.Login1,name='log'),
    path('logout',views.Logout,name='logout'),
    path('order',views.Order_Form1,name='order'),
    path("del/<int:id>/",views.Delete , name="delete"),

]
