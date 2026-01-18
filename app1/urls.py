from django.urls import path
from .views import create_order,order_list_create

urlpatterns = [
    path("order/", create_order),
    path('api/orders/', order_list_create),
]
