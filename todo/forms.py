from django import forms
from django.forms import fields, widgets
from .models import Ish

class IshForm(forms.ModelForm):
    class Meta:
        model = Ish
        fields = ['nomi','sana','vaqti']

        widgets= {
            "nomi": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "sana": forms.TextInput(attrs={"class": "form-control mt-2","type":"date"}),
            "vaqti": forms.TextInput(attrs={"class": "form-control mt-2","type":"time"}),
        }
        
        labels = {
            "nomi": "",
            "sana": "",
            "vaqti": "",
        }