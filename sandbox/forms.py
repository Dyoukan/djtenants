from django import forms

from .models import Sandbox

class SandboxForm(forms.ModelForm):
    class Meta:
        model = Sandbox
        fields = '__all__'
        exclude = ('id',)