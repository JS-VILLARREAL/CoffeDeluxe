from django import forms
from coffe_app.models import Product

class ProductForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=255)
    description = forms.CharField(label="Descripcion", max_length=355)
    price = forms.DecimalField(label="Precio", max_digits=10, decimal_places=2)
    available = forms.BooleanField(label="Disponible", required=False)
    photo = forms.ImageField(label="Foto", required=False)
    
    def save(self):
        data = self.cleaned_data
        product = Product.objects.create(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            available=data.get("available"),
            photo=data.get("photo")
        )
        return product