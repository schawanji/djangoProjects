from django.shortcuts import render
from .models import Renter, Bike, Rentals
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView



# Create your views here.
def home(request):
    return render(request,'djaunty/home.html')

class ListBikes(ListView):
    model = Bike
    template_name ='djaunty/bikes.html'

class ListRenters(ListView):
    model=Renter
    template_name='djaunty/renters.html'

class ListRentals(ListView):
    model=Rentals
    template_name='djaunty/rentals.html'



