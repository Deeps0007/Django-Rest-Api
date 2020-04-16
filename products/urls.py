from django.urls import path
from . import views
from products.views import Message

urlpatterns = [
    path('products/hello', views.hello),
    path('products/', views.product_list),
    path('products/<int:pk>/', views.single_product_detail),
    path('messages/', Message.as_view(), name='message')
]
