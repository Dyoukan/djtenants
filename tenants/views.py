from django.contrib.auth import login
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import views

class IndexView(generic.TemplateView):
    template_name = 'tenant/index.html'


class LoginView(views.LoginView):
    template_name = 'registration/login.html'
    def get_success_url(self):
        return super().get_success_url()