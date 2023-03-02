from django.shortcuts import render
from .forms import StateCreateForm, AttractionCreateForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import State, Attraction
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

#@login_required

class ListState(LoginRequiredMixin,ListView):
    model = State
    template_name = 'tourist_attractions/state_list.html'


class StateFormCreate(LoginRequiredMixin,CreateView):
    model = State
    form_class = StateCreateForm
    template_name = 'tourist_attractions/state_create_form.html'


class AttractionFormCreate(LoginRequiredMixin,CreateView):
    model = Attraction
    form_class = AttractionCreateForm
    template = 'tourist_attractions/attraction_create_form.html'
