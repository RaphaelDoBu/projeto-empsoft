
from django.conf.urls import url
from . import views


# app_name = 'projempsoft'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^estudantes/', views.estudante , name='estudante'),

    url(r'^cadastro-estudante/', views.cadastro_estudante, name='cadastro_estudante'),
    url(r'^cadastro-empresa/', views.cadastro_empresa, name='cadastro_empresa'),

    url(r'^estudante/(?P<estudante_id>[0-9]+)$', views.detail, name='detail'),

    url(r'^login/', views.login, name='login'),

    url(r'^post/new-estudante/$', views.post_new_estudante, name='post_new_estudante'),
    url(r'^post/new-empresa/$', views.post_new_empresa, name='post_new_empresa'),

]
