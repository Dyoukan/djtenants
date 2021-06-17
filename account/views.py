from django.shortcuts import render
from django.contrib.auth import views as auth_views

class LoginView(auth_views.LoginView):
    def dispatch(self, request, *args, **kwargs):
        tenant = request.tenant
        
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        request = self.request
        tenant = request.tenant
        #url = 'http://' + tenant.domain_url + ':8000' +  super().get_success_url()
        url = super().get_success_url()
        return  url
    pass

