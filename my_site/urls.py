"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from my_app.views import site_index, site_time, DishListView, DishCreateView, DishDeleteView, DishUpdateView
from my_auth.views import login_view, AboutMeView, RegisterView, logout_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('my_app.urls')),
    path('myauth/', include('my_auth.urls')),
    path('time/', site_time),
    #path('login/', auth_views.LoginView.as_view(template_name='my_auth/login.html'), name='login'),
    path('login/', login_view, name='login'),
    path('about_me/', AboutMeView.as_view(template_name='my_auth/about_me.html'), name='about_me'),
    path('register/', RegisterView.as_view(template_name='my_auth/register.html'), name='register'),
    path('logout/', logout_view, name='logout'),
    path('dishes/', DishListView.as_view(template_name='my_app/dish_list.html')),
    path('dishes/create', DishCreateView.as_view(template_name='my_app/send_dish.html')),
    path('dishes/delete/<pk>', DishDeleteView.as_view(template_name='my_app/dish_delete_confirm.html')),
    path('dishes/update/<pk>', DishUpdateView.as_view(template_name='my_app/update_dish.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
