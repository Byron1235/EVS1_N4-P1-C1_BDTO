from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def displayapp1re1(request):
    return HttpResponse("<h1>Hola Mundo!</h1> <p>Lorem evaluación sumativa 1</p> <a href='https://www.youtube.com/watch?v=L6sbfskaTDQ&ab_channel=FIFA'>Clickeame!</a> <h2>Cristiano Ronaldo</h2> <blockquote>Probando probando</blockquote>")

def displayapp1re2(request):
    return HttpResponse("<h1>Nuevamente nos encontramos</h1> <p>Aquí abajo dejaré un link</p> <a href='https://www.youtube.com/watch?v=6R3ouGNcACQ'>Click me!</a> <h3>¿Que tal la canción?</h3> <main>Espero que este correcto como he tipeado el codigo en la rama1</main>")

    
