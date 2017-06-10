from random import shuffle
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from .models import Test


# Generate list with all test questions
class QuestionList(ListView):
    model = Test
    context_object_name = 'test_list'
    template_name = 'question-list.html'


def index(request):
    return render(request, "index.html")


def qstGen(request):
    """
    Return mixed questions dictionary in Json format.

    Get questions from Test model, puts them in questions dictionary
    and mixing. Questions number gets from request and save in qstCount.
    """
    qstCount = int(request.GET['qstCount'])
    questions = {}
    counter = 0

    for test in Test.objects.all()[:qstCount]:
        questions[counter] = {"qst": test.condition,
                              0: test.first,
                              1: test.second,
                              2: test.third,
                              3: test.fourth,
                              'answ': test.correctChoice,
                               }
        counter += 1

    # Mix questions, using random.shuffle()
    shuffle(questions)
    return JsonResponse(questions)
