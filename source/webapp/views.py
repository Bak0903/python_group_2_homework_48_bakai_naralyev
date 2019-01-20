from django.shortcuts import reverse,redirect, get_object_or_404, render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from webapp.models import Food, OrderFood, Order, Employee
from webapp.form import FoodForm, OrderForm, OrderfoodForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class CourierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Order
    template_name = 'for_courier.html'
    permission_required = 'webapp.view_order'


class OrderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Order
    template_name = 'order_list.html'
    permission_required = 'webapp.view_order'


class OrderDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Order
    template_name = 'order_detail.html'
    permission_required = 'webapp.view_order'


class OrderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Order
    template_name = 'order_create.html'
    form_class = OrderForm
    permission_required = 'webapp.add_order'

    def form_valid(self, form):
        form.instance.operator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})


class FoodListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Food
    template_name = 'food_list.html'
    permission_required = 'webapp.view_food'


class FoodDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Food
    template_name = 'food_detail.html'
    permission_required = 'webapp.view_food'


class FoodCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Food
    template_name = 'food_create.html'
    form_class = FoodForm
    permission_required = 'webapp.add_food'

    def get_success_url(self):
        return reverse('webapp:food_detail', kwargs={'pk': self.object.pk})


class FoodUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Food
    template_name = 'food_update.html'
    form_class = FoodForm
    permission_required = 'webapp.change_food'

    def get_success_url(self):
        return reverse('webapp:food_detail', kwargs={'pk': self.object.pk})


class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'food_delete.html'
    success_url = reverse_lazy('food_list')
    permission_required = 'webapp.delete_food'


class OrderfoodCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = OrderFood
    template_name = 'orderfood_create.html'
    form_class = OrderfoodForm
    permission_required = 'webapp.add_orderfood'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk = self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.kwargs.get('pk')})


class OrderfoodDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = OrderFood
    template_name = 'orderfood_delete.html'
    permission_required = 'webapp.delete_orderfood'

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': get_object_or_404(OrderFood, pk=self.kwargs.get('pk')).order.pk})


class OrderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderForm
    permission_required = 'webapp.change_order'

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})


def order_cancel(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    order.status = 'Отменён'
    order.save()
    return redirect('webapp:order_list')


def order_done(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    order.status = 'Готов'
    order.save()
    return redirect('webapp:order_list')


def order_delivered(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    order.status = 'Доставлен'
    order.save()
    return redirect('webapp:order_list')


def courier_select(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    order.courier = request.user
    order.status = 'В пути'
    order.save()
    return redirect('webapp:courier_list')
