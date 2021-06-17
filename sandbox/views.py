from django.http.response import HttpResponse
from typing import Any
from django.http.request import HttpRequest
from sandbox.models import Sandbox
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SandboxForm
from .models import Sandbox

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name='sandbox/index.html'
    context_object_name = 'sandboxlist'
    
    def get_queryset(self):
        return Sandbox.objects.filter()[:]

class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Sandbox
    form_class = SandboxForm
    template_name = 'sandbox/detail.html'
    success_url = '/sandbox'


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Sandbox
    form_class = SandboxForm
    template_name = 'sandbox/detail.html'
    success_url = '/sandbox'
