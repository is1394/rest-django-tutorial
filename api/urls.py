from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^notes/$', views.NoteList.as_view()),
    url(r'^notes/(?P<pk>[0-9]+)/$', views.NoteDetail.as_view()),
]