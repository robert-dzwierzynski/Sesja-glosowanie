

from django.conf.urls import url
from . import views
app_name = 'glosowanie'


urlpatterns = [
    url(r'^$', views.lista_uchwal, name='uchwaly'),
    url(r'^wszystkie$', views.wszystkie_uchwaly, name='wszystkie_uchwaly'),
    url(r'^(?P<id_uchwaly>\d+)/$', views.pojedyncza_uchwala, name='detale_uchwaly'),

]