from django.urls import path
from django.contrib import admin

from . import views

#app_web ="user"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),

]
# from django.contrib import admin
# from django.urls import path
# from . import views
#
# app_name = "user"
#
# urlpatterns = [
#     path('register/',views.register,name = "register"),
#     path('login/',views.loginUser,name = "login"),
#     path('logout/',views.logoutUser,name = "logout"),
#
# ]
