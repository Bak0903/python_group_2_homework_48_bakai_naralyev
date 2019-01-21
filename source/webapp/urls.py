from django.urls import path
from webapp.views import FoodDetailView, OrderDetailView,\
                            FoodListView, OrderListView,\
                            FoodCreateView, FoodDeleteView, FoodUpdateView,\
                            OrderCreateView, OrderfoodCreateView, OrderUpdateView, OrderfoodDeleteView,\
                            order_cancel, order_done, order_delivered, courier_select, CourierListView,\
                            OrderFoodAjaxCreateView, OrderFoodAjaxUpdateView, OrderFoodAjaxDeleteView

app_name = 'webapp'

urlpatterns = [
    path('food_list/', FoodListView.as_view(), name='food_list'),
    path('', OrderListView.as_view(), name='order_list'),
    path('courier_list', CourierListView.as_view(), name='courier_list'),

    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('food/<int:pk>', FoodDetailView.as_view(), name='food_detail'),

    path('food/create', FoodCreateView.as_view(), name='food_create'),
    path('food/<int:pk>/update', FoodUpdateView.as_view(), name='food_update'),
    path('food/<int:pk>/delete', FoodDeleteView.as_view(), name='food_delete'),

    path('order/create', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/order_food', OrderfoodCreateView.as_view(), name='orderfood'),
    path('order_food/<int:pk>/delete_food', OrderfoodDeleteView.as_view(), name='food_delete'),
    path('order/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),

    path('order/<int:pk>/food/create', OrderFoodAjaxCreateView.as_view(), name='order_food_create'),
    path('order/food/<int:pk>/update', OrderFoodAjaxUpdateView.as_view(), name='order_food_update'),
    path('order/food/<int:pk>/delete', OrderFoodAjaxDeleteView.as_view(), name='order_food_delete'),

    path('order/<int:order_pk>/cancel', order_cancel, name='order_cancel'),
    path('order/<int:order_pk>/done', order_done, name='order_done'),
    path('order/<int:order_pk>/delivered', order_delivered, name='order_delivered'),
    path('order/<int:order_pk>/courier', courier_select, name='courier'),
]
