from django.conf.urls import url, include
from apps.plan.views import index, plan_view, plan_listar, plan_editar, plan_eliminar, quienesSomos, contacto
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^index$', login_required(index), name='index' ),
    url(r'^quienesSomos$', login_required(quienesSomos), name='quienesSomos' ),
    url(r'^contacto$', login_required(contacto), name='contacto' ),
    url(r'^nuevo$', login_required(plan_view), name='plan_crear'),
    url(r'^listar$', (plan_listar), name='plan_listar'),
    url(r'^editar/(?P<id_plan>\d+)/$', login_required(plan_editar), name='plan_editar'),
    url(r'^eliminar/(?P<id_plan>\d+)/$', login_required(plan_eliminar), name='plan_eliminar')
]