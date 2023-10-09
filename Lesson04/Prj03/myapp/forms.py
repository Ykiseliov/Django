from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'photo']

class ProductFilterForm(forms.Form):
    # Добавляем поля для фильтрации, если нужно
    name = forms.CharField(max_length=100, required=False)

class ProductPhotoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['photo']