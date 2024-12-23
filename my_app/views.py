from datetime import datetime
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Dish
from django.contrib.auth.mixins import LoginRequiredMixin
from random import sample

# Create your views here.

def site_index(request: HttpRequest):
    context = {
        'time_running': datetime.now()
    }
    return render(request, 'my_app/template_zero.html', context=context)

def site_time(request: HttpRequest):
    context = {
        'time_running': datetime.now()
    }
    return render(request, 'my_app/template_one.html', context=context)

class DishListView(TemplateView):
    template_name = 'my_app/dish_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dishes'] = Dish.objects.all()
        return context
    
class DishOneView(View):
    def get(self, request: HttpRequest, pk: int):
        dish = get_object_or_404(Dish, pk=pk)
        context = {
            'dish': dish
        }
        return render(request, template_name='my_app/template_dish.html', context=context)

    
class DishCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    fields = 'name', 'time', 'description', 'body', 'img'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('myapp:index')

class DishDeleteView(LoginRequiredMixin, DeleteView):
    model = Dish
    success_url = reverse_lazy('myapp:index')

class DishUpdateView(LoginRequiredMixin, UpdateView):
    model = Dish
    fields = 'name', 'time', 'description', 'body', 'img'
    def form_valid(self, form):
        form.instance.author = str(self.request.user)
        return super().form_valid(form)
    success_url = reverse_lazy('myapp:index')

class DishIndexView(TemplateView):
    template_name = 'my_app/template_zero.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if len(Dish.objects.all()) <= 5:
            context['dishes'] = Dish.objects.all()
        else:
            context['dishes'] = Dish.objects.order_by('?')[:5]
        return context