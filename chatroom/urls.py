from django.urls import path
from . import views
  

app_name = 'chatroom'
urlpatterns = [
    path('', views.index, name="room-home"),
    path('room/<str:id>/', views.roomMessage, name="room-message"),
    path('create-room/<str:id>/', views.createRoom, name="create-room"),
   
]
