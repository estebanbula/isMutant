from django.urls import path, include
from ismutant import views

urlpatterns = [
    path('', views.mutant, name='mutants algorithm'),
    path('stats', views.stats)
]