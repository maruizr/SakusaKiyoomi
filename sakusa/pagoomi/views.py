from django.shortcuts import render
from django.http import HttpResponse 
from django.core.mail import send_mail
from django.views import generic
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from pagoomi.models import Curiosidad, Formulario

# Create your views here.

def index(request):    
    return render(
        request,
        'index.html'
    )

def galeria(request):    
    return render(
        request,
        'galeria.html'
    )

def formulario(request):

    if request.method=="POST": # Cuando se presiona el boton enviar formulario
    
        # carga las variables con los campos del formulario 
        nombre   = request.POST["nombre"]
        email    = request.POST["email"]
        comment  = request.POST["comentario"]

        formulario = Formulario(nombre=nombre, 
                            email=email,
                            comentario=comment)
        formulario.save() # Guarda en BD

        mostrar_popup = '1'
        
        return render (
            request,
            'formulario.html',
            context={'mostrar_popup':mostrar_popup}
        )

    else:

        return render (
            request,
            'formulario.html'
        )

class CuriosidadListView(generic.ListView):
    model = Curiosidad
    paginate_by = 30

class CuriosidadCreate(CreateView):
    model = Curiosidad
    fields = ['name','description']

class CuriosidadUpdate(UpdateView):
    model = Curiosidad
    fields = ['name','description']

class CuriosidadDelete(DeleteView):
    model = Curiosidad
    success_url = reverse_lazy('curiosidad')

class CuriosidadDetailView(generic.DetailView):
    model = Curiosidad
