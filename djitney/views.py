from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.
def home(request):
    return render(request, 'djitney/home.html')


