from django.shortcuts import render
from .models import CafeList
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

# Create your views here.

class IndexClassView(ListView):
    model = CafeList
    template_name = 'cafe/index.html'
    context_object_name = 'cafe_list'

class AddCafe(CreateView):
    model = CafeList;  
    fields = ['cafe_name','cafe_wifi','cafe_address','cafe_rating']
    template_name = 'cafe/add-cafe.html'
    

