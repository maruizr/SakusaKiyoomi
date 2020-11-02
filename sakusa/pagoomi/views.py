from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse 
from django.core.mail import send_mail
from django.views import generic
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from pagoomi.models import Curiosidad

# Create your views here.

def index(request):    
    return render(
        request,
        'index.html'
    )
