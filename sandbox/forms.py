from django import forms

from .models import Sandbox

class SandboxForm(forms.Form):
    char = forms.CharField(max_length=20)
    