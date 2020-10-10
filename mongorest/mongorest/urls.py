# mongorest admin & api routes
from django.urls import path
from api import views 


urlpatterns = [
    path('orders', views.orders),
    path('cost-centers', views.cost_centers),
    path('customers', views.customers),
    path('products', views.products),
    path('suppliers', views.suppliers),
    path('delivery-locations', views.delivery_locations),
    path('orders', views.orders)
]
