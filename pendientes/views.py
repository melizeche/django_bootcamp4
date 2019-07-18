from django.shortcuts import render
from django.http import HttpResponse

from pendientes.models import Tarea # Importamos la clase Tarea de models.py
from random import randint
# Create your views here.

def index(request):
    listita = Tarea.objects.all() #consultamos la BD y guardamos todos
                                # los registros de la tabla Tarea
    persona = {                 # como objetos y guardamos en listita
        "nombre" : "Marce", 
        "edad":33,
        "hobbies": ["rugby","comer pan","cortar patas de dinos","comer chocolate","jugar pool"],
        "lista_tareas": listita, # agregamos la clave lista_tareas
        }                        # al diccionario de contenido con la
                                # lista de tareas p/ mandar al template
    return render(request, 'inicio.html', persona)

def tarea(request):
    numero =  str(randint(500,999))
    print("Hola!!!!!", numero)
    return  HttpResponse("Hola soy la vista tarea" + numero)

def aleatorio(request):
    numero =  str(randint(1,999))
    respuesta = "El numero ganador es: " + numero
    return HttpResponse(respuesta)

# Crear la vista/funcion tarea y conectar con la direccion
# /tareas en el archivo urls.py
# despues ir al navegador y abrir http:....../tareas

# Crear una vista respuestas que retorne un texto cuando
# en el navegador entremos a http:...../info
# Pista crear la funcion/vista en views.py y conectar en
# urls.py usando path(.....)