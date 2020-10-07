from django.urls import path
from . import views
from blog import views as blog_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register , name ='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile', views.profile , name ='profile'),
    path('', blog_views.home , name ='blog-home'),
   

]
