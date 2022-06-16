from django.urls import path
from app_blog.views import obras_arq_view, cargar_obra,search_obra,detail_obrasarq,arquitectos_view,detail_arquitecto,cargar_arqui

urlpatterns = [
    path('obras_arq_view/', obras_arq_view,name = 'obras_arq_view'),
    path('obras_arq_view/cargar_obra/', cargar_obra,name = 'cargar_obra'),
    path('detail_obrasarq/<int:pk>/',detail_obrasarq,name ='detail_obrasarq'),
    path('arquitectos_view/', arquitectos_view,name = 'arquitectos_view'),
    path('arquitectos_view/cargar_arqui/', cargar_arqui ,name= 'cargar_arqui'),
    path('detail_arquitecto/<int:pk>/', detail_arquitecto,name ='detail_arquitecto'),
    path('search_obra/', search_obra ,name = 'search_obra'),
]