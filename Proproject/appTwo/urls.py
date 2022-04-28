from django.urls import path,include
from appTwo import views


urlpatterns = [
    path('help/', views.help, name='help'),
    path('register/',views.register, name='register'),
    path('login/',views.user_login,name='login'),
]
