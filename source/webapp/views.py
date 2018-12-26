from django.shortcuts import reverse,redirect, get_object_or_404, render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from webapp.models import Food, OrderFood, Order, Employee
from webapp.form import FoodForm, OrderForm, OrderfoodForm, CourierForm
from django.urls import reverse_lazy


def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s' % reverse('webauth:login'))
    return super().dispatch(request, *args, **kwargs)


class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class CourierListView(ListView):
    model = Order
    template_name = 'for_courier.html'


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

    def get_success_url(self):
        return reverse('webapp:food_detail', kwargs={'pk': self.object.pk})


class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'food_update.html'
    form_class = FoodForm

    def get_success_url(self):
        return reverse('webapp:food_detail', kwargs={'pk': self.object.pk})


class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'food_delete.html'
    success_url = reverse_lazy('food_list')


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})


class OrderfoodCreateView(CreateView):
    model = OrderFood
    template_name = 'orderfood_create.html'
    form_class = OrderfoodForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk = self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.kwargs.get('pk')})


class OrderfoodDeleteView(DeleteView):
    model = OrderFood
    template_name = 'orderfood_delete.html'

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': get_object_or_404(OrderFood, pk=self.kwargs.get('pk')).order.pk})


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderForm

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


class CourierUpdateView(UpdateView):
    model = Order
    template_name = 'choose_courier.html'
    form_class = CourierForm

    def get_success_url(self):
        return reverse('webapp:courier_list')