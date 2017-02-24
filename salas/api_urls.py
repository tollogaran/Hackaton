from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Salas API')

urlpatterns = [
    url(r'^reservas/', include('modules.Reservas.urls_api')),
    # Se agrega para Swagger
    url(r'^documentation/', schema_view),
    #TODO agregar Publicaciones
]