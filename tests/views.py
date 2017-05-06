from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Test
from django.views.decorators.csrf import csrf_exempt

import random

# Create your views here.
# @csrf_exempt
def index(request):
    response = render(request, "index.html")

    return response

def testStarter(request):

    return render(request, 'testsPage.html')

@csrf_exempt
def qstGen(request):
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

    random.shuffle(questions)
    return JsonResponse(questions)
