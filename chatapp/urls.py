
from django.contrib import admin
from django.urls import path, include

from users import views as user_views

urlpatterns = [
    path('', include('chatroom.urls')), 
    path('admin/', admin.site.urls),

    path('register/', user_views.registerUser, name="register"),
    path('login/', user_views.loginUser, name="login"),
    path('logout/', user_views.logoutUser, name="logout"),
]
