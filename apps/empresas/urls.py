from django.urls import path

from apps.empresas.views import home

urlpatterns = [
    path('', home)
]