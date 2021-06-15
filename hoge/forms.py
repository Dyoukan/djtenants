from django import forms

from .models import Hoge

class HogeForm(forms.ModelForm):
    class Meta:
        model = Hoge
        fields = '__all__'