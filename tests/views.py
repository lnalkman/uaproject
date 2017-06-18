from random import shuffle
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse
# Since django 1.10: from django.core.urlresolver import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Test
from .forms import AuthForm, RegistrationForm


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


class UserRegistration(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = r'/'

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Success Registration')

        return super(CreateView, self).form_valid(form)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        form = AuthForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password')
                                )
            if user:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'success login')
                return HttpResponseRedirect(reverse('index'))
            else:
                form.add_error(None, "Невірне ім'я користувача або пароль.")
                return render(request, 'auth.html', context={'form': form})
    else:
        form = AuthForm()

    return render(request, 'auth.html', context={'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.INFO, 'success exit')
    return HttpResponseRedirect(reverse('index'))
