from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = "dangun_app"
urlpatterns = [

    path('', views.main,name='main'),
    path('trade/', views.trade, name='trade'),
    path('trade/<int:post_id>',views.trade_post, name='trade_post'),
    path("location", views.location, name="location"),
    path("set_region/", views.set_region, name="set_region"),
    path("set_region_certification/", views.set_region_certification, name="set_region_certification"),
  
    path('chat/', views.chatroom_list, name='chatroom'),
    path('ws/chat/<str:chatroom_id>/', views.chatroom, name='chat_room'),

    path('search/', views.search, name='search')
]