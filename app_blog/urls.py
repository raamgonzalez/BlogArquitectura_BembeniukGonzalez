from django.urls import path
from app_blog.views import Obras_arq_view, Create_obra,search_obra,Detail_obrasarq,Arquitectos_view,Detail_arquitecto,Create_arqui

urlpatterns = [
    path('obras_arq_view/', Obras_arq_view.as_view(),name = 'obras_arq_view'),
    path('obras_arq_view/cargar_obra/', Create_obra.as_view(),name = 'cargar_obra'),
    path('detail_obrasarq/<int:pk>/',Detail_obrasarq.as_view(),name ='detail_obrasarq'),
    path('arquitectos_view/', Arquitectos_view.as_view(),name = 'arquitectos_view'),
    path('arquitectos_view/cargar_arqui/', Create_arqui.as_view() ,name= 'cargar_arqui'),
    path('detail_arquitecto/<int:pk>/', Detail_arquitecto.as_view(),name ='detail_arquitecto'),
    path('search_obra/', search_obra ,name = 'search_obra'),
]