from django import forms
from .models import CafeList

class CafeForm(forms.ModelForm):
    class Meta:
        model = CafeList
        fields = ['cafe_name','cafe_wifi','cafe_address','cafe_rating']
        