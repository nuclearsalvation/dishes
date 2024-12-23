from django.urls import path
from .views import login_view, AboutMeView, RegisterView, logout_view
from django.contrib.auth.views import LoginView

app_name = 'myauth'

urlpatterns = [
    #path('login/', LoginView.as_view(template_name='my_auth/login.html'), name='login'),
    path('login/', login_view, name='login'),
    path('about_me/', AboutMeView.as_view(), name='about_me'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout')
]