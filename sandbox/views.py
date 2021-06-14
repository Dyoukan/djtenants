from django.shortcuts import render
from django.views import generic

from .forms import SandboxForm

# Create your views here.
class IndexView(generic.FormView):
    template_name = "sandbox/index.html"
    form_class = SandboxForm