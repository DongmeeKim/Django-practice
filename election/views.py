from django.shortcuts import render
from django.http import HttpResponse

from .models import Character, Poll, Choice
import datetime
# Create your views here.

def index(request):
    characters = Character.objects.all()
    context = {'characters' :characters}
    return render(request, 'election/index.html', context)


def dormitories(request, dormitory):
    today = datetime.datetime.now()
    try:
        poll = Poll.objects.get(dormitory = dormitory, start_date__lte = today, end_date__gte = today)
        characters = Character.objects.filter(dormitory = dormitory)
    except:
        poll = None
        characters = None
    context = {'characters':characters, 'dormitory':dormitory, 'poll':poll}
    return render(request, 'election/dormitory.html', context)

def polls(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    selection = request.POST['choice']
    try:
        choice = Choice.objects.get(poll_id = poll.id, character_id = selection)
        choice.votes += 1
        choice.save()
    except:
        choice = Choice(poll_id = poll_id, character_id = selection, votes =1)
        choice.save()


    return HttpResponse("finish")