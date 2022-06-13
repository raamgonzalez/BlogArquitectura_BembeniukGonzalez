from django.urls import path
from app_blog.views import obras_arq_view, inst_edu_view, bibliografia_view, cargar_obra, cargar_Instedu, cargar_bibliografia,search_obra,detail_obrasarq,detail_instedu,detail_biblio

urlpatterns = [
    path('obras_arq_view/', obras_arq_view,name = 'obras_arq_view'),
    path('inst_edu_view/', inst_edu_view,name = 'inst_edu_view'),
    path('bibliografia_view/', bibliografia_view,name = 'bibliografia_view'),
    path('obras_arq_view/cargar_obra/', cargar_obra,name = 'cargar_obra'),
    path('inst_edu_view/cargar_Instedu/', cargar_Instedu ,name= 'cargar_Instedu'),
    path('bibliografia_view/cargar_bibliografia/', cargar_bibliografia ,name= 'cargar_bibliografia'),
    path('search_obra/', search_obra ,name = 'search_obra'),
    path('detail_obrasarq/<int:pk>/',detail_obrasarq,name ='detail_obrasarq'),
    path('detail_instedu/<int:pk>/', detail_instedu,name ='detail_instedu'),
    path('detail_biblio/<int:pk>/', detail_biblio,name = 'detail_biblio'),
]