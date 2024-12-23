from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class AboutMeView(TemplateView):
    template_name='my_auth/about_me.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'my_auth/register.html'
    success_url = reverse_lazy('myapp:index')

def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse_lazy('myapp:index'))



def login_view(request: HttpRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse_lazy('myapp:index'))
        return render(request, 'my_auth/login2.html')
    
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse_lazy('myapp:index'))
    return render(request, 'my_auth/login2.html')