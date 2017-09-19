from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^notes/$', views.note_list),
    url(r'^notes/(?P<pk>[0-9]+)$', views.note_detail),
]