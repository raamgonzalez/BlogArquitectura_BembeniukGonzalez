from django.urls import path
from index.views import Index_view

urlpatterns = [
    path('', Index_view.as_view(),name = 'index'),
]