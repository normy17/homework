from django.urls import path

from homework.views import *

urlpatterns = [
    path("", eng_view, name="eng"),
    path("fr/", fr_view, name="fr"),
    path("de/", de_view, name="de"),
    path("es/", es_view, name="es"),
    path("toyota/", toyota_view, name="toyota"),
    path("honda/", honda_view, name="honda"),
    path("renault/", renault_view, name="renault"),
    path('today/', today_day, name="today")
]