from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Test
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    response = render(request, "index.html")

    return response

def testStarter(request):

    return render(request, 'testsPage.html')

@csrf_exempt
def qstGen(request):
    questions = {}
    counter = 0
    for test in Test.objects.all():
        questions[counter] = {"qst": test.condition,
                              0: test.first,
                              1: test.second,
                              2: test.third,
                              3: test.fourth,
                               }
        counter += 1

    return JsonResponse(questions)
