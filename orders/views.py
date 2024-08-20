from django.views.generic import DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse

from .models import Order, OrderProduct
from .forms import OrderProductForm


class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy("my_order")

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user=self.request.user,
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
    
class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = OrderProduct
    success_url = reverse_lazy("my_order")
    template_name = "orders/delete_order_product.html"
    context_object_name = "order_product"
    
    def get_queryset(self):
        return OrderProduct.objects.filter(order__user=self.request.user)
    
    def get_success_url(self):
        return reverse("my_order")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = self.get_object().order
        return context