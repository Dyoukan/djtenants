from django.urls import path
from django.contrib.auth import views as auth_view

from . import views

app_name = "tenants"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]
