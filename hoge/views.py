from django.shortcuts import render
from django.views import generic

from hoge.forms import HogeForm

class IndexView(generic.FormView):
    form_class = HogeForm
    template_name = "hoge/index.html"