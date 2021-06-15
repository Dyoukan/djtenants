from django.urls import path

from . import views

app_name = "sandbox"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.UpdateView.as_view(), name="update"),    
    path('create/', views.CreateView.as_view(), name="create"),
]
