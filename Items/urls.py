from django.urls import path
from.views import items, productlist, ProductDetail, UpdateProductView, DeleteProductView


APP_NAME = 'item'


urlpatterns = [
    path('', items, name='item'),
    path('products/', productlist, name='product-list'),
    path('<int:pk>/<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    path('edit/<int:pk>/', UpdateProductView.as_view(), name='update-post'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='delete-post'),
]
