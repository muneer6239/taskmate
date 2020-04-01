from django.urls import path
from users_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.registeration, name='registeration'), 
    path('login', auth_views.LoginView.as_view(template_name="login.html"), name='login'), #here 'template_name="login.html"' can also be (templates folder/registration folder/login.html file)
    path('logout', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'), 
    
]