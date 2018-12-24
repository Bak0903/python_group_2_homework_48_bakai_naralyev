from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from webapp.views import FoodDetailView, OrderDetailView,\
                            FoodListView, OrderListView,\
                            FoodCreateView, FoodDeleteView, FoodUpdateView,\
                            OrderCreateView, OrderfoodCreateView, OrderUpdateView, OrderfoodDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('food_list/', FoodListView.as_view(), name='food_list'),
    path('', OrderListView.as_view(), name='order_list'),

    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('food/<int:pk>', FoodDetailView.as_view(), name='food_detail'),

    path('food/create', FoodCreateView.as_view(), name='food_create'),
    path('food/<int:pk>/update', FoodUpdateView.as_view(), name='food_update'),
    path('food/<int:pk>/delete', FoodDeleteView.as_view(), name='food_delete'),

    path('order/create', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/order_food', OrderfoodCreateView.as_view(), name='orderfood'),
    path('order_food/<int:pk>/delete_food', OrderfoodDeleteView.as_view(), name='food_delete'),
    path('order/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
