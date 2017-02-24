from django.conf.urls import url
from .api_views import SalaList, SalasDetail



urlpatterns = [
    url(r'^salas/$', SalaList.as_view(),name='api-salas'),
    url(r'^salas/(?P<pk>[0-9]+)/$', SalasDetail.as_view()),
    #url(r'^publicacionesapi/$', PublicacionList.as_view(), name='api-list-publicacion'),
]