from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Character, Poll, Choice
import datetime

from django.db.models import Sum
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
    return HttpResponseRedirect("/dormitories/{}/results".format(poll.dormitory))

def results(request, dormitory):
    characters = Character.objects.filter( dormitory = dormitory )
    polls = Poll.objects.filter( dormitory = dormitory )
    poll_results = []
    for poll in polls:
        result = {}
        result['start_date'] = poll.start_date
        result['end_date'] = poll.end_date
        total_votes = Choice.objects.filter( poll_id = poll.id ).aggregate(Sum('votes'))
        result['total_votes'] = total_votes['votes__sum']
        rates = []
        for character in characters:
            try:
                choice = Choice.objects.get(poll = poll, character = character)
                rates.append(
                    round(choice.votes * 100 / result['total_votes'],1)
                    )
            except:
                rates.append(0)
        result['rates'] = rates
        poll_results.append(result)

    context = {'characters':characters, 'dormitory':dormitory, 'poll_results':poll_results}
    return render(request, 'election/result.html', context)