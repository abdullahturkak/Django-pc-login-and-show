from django.forms import ModelForm
from giris.models import Satıs
from django import forms
from .models import Satıs

class PcEkleme(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Satıs
        fields = [
            'id', 'marka', 'model', 'fiyat',
            'tel', 'adres'
        ]