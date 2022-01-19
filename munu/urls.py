from django.contrib import admin
from django.urls import path, URLResolver, URLPattern

from .views import index, products_list, product_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('product-list/<str:slug>/', products_list, name='list'),
    path('product/<int:product_id>/', product_detail, name='detail'),
]