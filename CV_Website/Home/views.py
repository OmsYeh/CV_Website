from django.shortcuts import render
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from Home.models import *

# Create your views here.


def home(request):
    return render(request, 'base.html')


