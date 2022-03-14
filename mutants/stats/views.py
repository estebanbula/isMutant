from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def stats():
    data = {
        "count_mutant_dna": 40, 
        "count_human_dna": 100, 
        "ratio": 0.4
    }
    return JsonResponse(data)
