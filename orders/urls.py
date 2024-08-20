from django.urls import path

from .views import MyOrderView, CreateOrderProductView, DeleteProductView

urlpatterns = [
    path("mi-orden", MyOrderView.as_view(), name="my_order"),
    path("agregar-producto", CreateOrderProductView.as_view(), name="add_product"),
    path("eliminar-producto/<int:pk>", DeleteProductView.as_view(), name="delete_product"),
]