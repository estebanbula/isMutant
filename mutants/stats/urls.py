from django.urls import path
from stats import views

urlpatterns = [
    path('', views.stats, name='mutants stats')
]