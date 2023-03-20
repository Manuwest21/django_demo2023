from django.shortcuts import render
from .models import Functionality
from django.views.generic import ListView, DetailView
# Create your views here.
class FunctionnalityListView(ListView):
    model = Functionality
    template_name = "funk/func_list.html"
    context_object_name = "func_list"
    
    
class FunctionalityListView(ListView):
    model = Functionality
    template_name = "funk/func_list.html"
    context_object_name = "func_list"
    
class FunctionalityDetailView(DetailView):
    model = Functionality
    template_name = "funk/func_detail.html"
    context_object_name = "func"