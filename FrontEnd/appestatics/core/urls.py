#from django.contrib import admin
from django.urls import path

from django.conf import settings

from django.conf.urls.static import static

from .views import carga,home,rxml,prepararxml

urlpatterns = [
    path('',home,name="home"),
    path('carga/',carga,name="carga"),
    path('rxml/',rxml,name="rxmlfront"),
    path('preparado/',prepararxml,name="prepararxml")
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)