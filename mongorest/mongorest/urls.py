# mongorest admin & api routes
from django.urls import path
from api import views 


urlpatterns = [
    path('amounts', views.amounts),
    path('addresses', views.addresses),
    path('orders', views.orders),
    path('customers', views.customers),
    path('products', views.products),
    path('cost-centers', views.cost_centers),
    path('suppliers', views.suppliers),
    path('companies', views.companies)
]