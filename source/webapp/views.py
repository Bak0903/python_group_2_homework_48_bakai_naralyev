from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Food, OrderFood, Order, Employee
from webapp.form import FoodForm
from django.urls import reverse_lazy


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'


class FoodCreateView(CreateView):
    model = Food
    template_name = 'food_create.html'
    form_class = FoodForm
    success_url = reverse_lazy('food_detail.html')

class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'food_update.html'
    form_class = FoodForm
    success_url = reverse_lazy('article_list')


class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'food_delete.html'
    success_url = reverse_lazy('article_list')
