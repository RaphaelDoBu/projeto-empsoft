
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^estudantes/(?P<estudante_id>[0-9]+)$', views.detail, name='detail')
]
