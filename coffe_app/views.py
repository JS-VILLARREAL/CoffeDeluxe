from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from coffe_app.models import Product

from .forms import ProductForm

# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "./product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        import ipdb; ipdb.set_trace()
        form.save()
        return super().form_valid(form)
    
    
class ProductListView(generic.ListView):
    template_name = "./product_list.html"
    model = Product
    context_object_name = "products"
