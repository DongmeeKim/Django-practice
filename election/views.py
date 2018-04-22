from django.shortcuts import render
from django.http import HttpResponse

from .models import Character
# Create your views here.

def index(request):
    characters = Character.objects.all()
    str = "" # 마지막에 return 해줄 문자열

    for character in characters :
        str += "<p>{}는 {}기숙사에 배정 받았다.<br>".format(character.name, character.dormitory)
        str += character.description + "<p>"

    return HttpResponse(str)
