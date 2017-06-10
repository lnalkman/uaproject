from django.conf.urls import url, include
from .views import index, QuestionList, qstGen, base


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^question-list$', QuestionList.as_view(), name='question-list'),
    url(r'^questions-generator$', qstGen),
]
