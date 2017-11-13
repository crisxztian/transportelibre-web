"""telotraigo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from domicilios.views import domiciliariosViewSet, clientesViewSet
from domicilios import views
from rest_framework.routers import SimpleRouter
from django.conf.urls import url, include
from django.contrib import admin

router = SimpleRouter()
router.register(r'domiciliarios', domiciliariosViewSet, base_name='domiciliariosViewSet')
router.register(r'clientes', clientesViewSet, base_name= 'clientesViewSet')


#urlpatterns = patterns('',url(r'^admin/', include(admin.site.urls)),url(r'^', include(router.urls)),)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^admin/domiciliarios/list', views.listdomiciliarios, name='list_domi'),
    url(r'^admin/domiciliarios/validar/(?P<domid>\d+)', views.validardom, name='validar_dom'),
    url(r'^admin/domiciliarios/vehiculos/(?P<domid>\d+)', views.vehiculoslist, name='vehiculos_list'),
]
