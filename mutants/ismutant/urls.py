from django.urls import path, include
from ismutant import views

urlpatterns = [
    path('', views.isMutant, name='mutants algorithm')
]