from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from webapp.views import FoodDetailView, OrderDetailView, \
                            FoodCreateView, FoodDeleteView, FoodUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('food/<int:pk>', FoodDetailView.as_view(), name='food_detail'),
    path('food/create', FoodCreateView.as_view(), name='food_create'),
    path('food/<int:pk>/update', FoodUpdateView.as_view(), name='food_update'),
    path('food/<int:pk>/delete', FoodDeleteView.as_view(), name='food_delete'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
