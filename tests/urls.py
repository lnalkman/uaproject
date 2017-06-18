from django.conf.urls import url, include
from .views import index, QuestionList, qstGen, login_view, logout_view, UserRegistration


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^question-list/$', QuestionList.as_view(), name='question-list'),
    url(r'^questions-generator/$', qstGen),
    url(r'^auth/$', login_view, name='authenticate'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^registration/$', UserRegistration.as_view(), name='registration'),
]
