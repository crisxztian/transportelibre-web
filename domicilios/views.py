from domicilios.models import domiciliarios,clientes
from domicilios.serializers import domiciliariosSerializer,clientesSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404

class domiciliariosViewSet(ModelViewSet):
    queryset = domiciliarios.objects.all()
    serializer_class = domiciliariosSerializer
    lookup_field = 'id'
    filter_backend = DjangoFilterBackend
    filter_fields = ('email',)

class clientesViewSet(ModelViewSet):
    queryset = clientes.objects.all()
    serializer_class = clientesSerializer
    lookup_field = 'id'
    filter_backend = DjangoFilterBackend
    filter_fields = ('email',)

def listdomiciliarios(request):
    domvalidos = domiciliarios.objects.filter(estado=1)
    dominvalidos = domiciliarios.objects.filter(estado=0)
    return render_to_response("domiciliarios.html", {"domvalidos": domvalidos, "dominvalidos": dominvalidos})

def validardom(request, domid):
    instance = get_object_or_404(domiciliarios, id=domid)
    instance.estado=1
    instance.save()
    return HttpResponseRedirect("/admin/domiciliarios/list")

def vehiculoslist(request, domid):
    instance = get_object_or_404(domiciliarios, id=domid)
    return render_to_response("vehiculos.html", {"domi":instance})
