from django.urls import path
from ismutant import views

urlpatterns = [
    path('', views.isMutant, name='mutants algorithm')
]