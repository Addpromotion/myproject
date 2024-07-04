from django.urls import path
from . import views
from .views import home, CustomLoginView

urlpatterns = [
    # URL-ы для входа
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),

    # URL-ы для клиентов
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/delete/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('customers/<int:customer_id>/orders/<str:period>/', views.customer_orders, name='customer_orders'),

    # URL-ы для товаров
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),

    # URL-ы для заказов
    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.add_order, name='add_order'),
    path('orders/delete/<int:order_id>/', views.delete_order, name='delete_order'),
]