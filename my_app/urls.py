from django.urls import path
from .views import site_index, site_time, DishListView, DishCreateView, DishDeleteView, DishUpdateView, DishOneView, DishIndexView

app_name = 'myapp'

urlpatterns = [
    path('', DishIndexView.as_view(template_name='my_app/template_zero.html'), name='index'),
    path('time', site_time, name='time'),
    path('dishes/', DishListView.as_view(template_name='my_app/dish_list.html')),
    path('dishes/create', DishCreateView.as_view(template_name='my_app/send_dish.html'), name='create'),
    path('dishes/delete/<pk>', DishDeleteView.as_view(template_name='my_app/dish_delete_confirm.html'), name='delete'),
    path('dishes/update/<pk>', DishUpdateView.as_view(template_name='my_app/update_dish.html'), name='update'),
    path('dishes/<pk>', DishOneView.as_view(), name='dish'),
]