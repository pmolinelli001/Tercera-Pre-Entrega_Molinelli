
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('art_list/', art, name="art_list"),
    path('hogar_list/', hogar, name="hogar_list"),
    path('auto_list/', auto, name="auto_list"),
    path('quienes_somos/', Quienes_somos, name="quienes_somos"),
    path('vida_list/', vida, name="vida_list"),
    path('mas_info/', MasInfo, name="mas_info"),
    path('artForm/', artForm, name="artForm"),
    path('buscarArt/',buscarArt, name="buscarArt"),
    path('encontrarArt/',encontrarArt, name="encontrarArt"),
    path('artcob/',artcob, name="artcob"),
    path('autocob/',autocob, name="autocob"),
    path('autoForm/',autoForm, name="autoForm"),
    path('vidaForm/',vidaForm, name="vidaForm"),
    path('hogarcob1/',hogarcob1, name="hogarcob1"),
    path('hogarcob2/',hogarcob2, name="hogarcob2"),
    path('hogarcob3/',hogarcob3, name="hogarcob3"),
    path('hogarcob4/',hogarcob4, name="hogarcob4"),
    path('hogarcob5/',hogarcob5, name="hogarcob5"),
    path('hogarForm/',hogarForm, name="hogarForm"),
     path('consultar_hogar/', consultar_hogar, name="consultar_hogar")
]

