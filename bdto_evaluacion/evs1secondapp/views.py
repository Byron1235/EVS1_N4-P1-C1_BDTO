from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def displayhugemessage(request):
    return HttpResponse("<h1>Hola soy parte de la evs1secondapp :D</h1> <a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'>Sorpresa sorpresa</a> <h2>Literalmente, nunca falla</h2> <small>Lo siento profe D;</small> <main>Lorem evs1secondapp</main>")

def displayfinal(request):
    return HttpResponse("<h1>Siempre se parte con un h1</h1> <a href='https://www.youtube.com/watch?v=F4aZAVgwOvY&ab_channel=dudewhereismyspoon'>Canción genial!</a> <p>Muy buena, digna del videojuego del año</p> <blockquote>Con esta evaluación me hice un experto tipeando etiquetas html</blockquote> <main>Etiqueta final :D</main>")