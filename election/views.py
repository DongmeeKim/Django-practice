from django.shortcuts import render
from django.http import HttpResponse

from .models import Character
# Create your views here.

def index(request):
    characters = Character.objects.all()
    context = {'characters' : characters}
    return render(request, 'election/index.html', context)
