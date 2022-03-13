from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Dna
from django.http import HttpResponse, HttpResponseForbidden

__sequences = ['AAAA', 'TTTT', 'CCCC', 'GGGG']

@api_view(['POST'])
def isMutant(request):
    dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    data = JSONParser().parse(request)
    dna = data['dna']
    ocurrences = 0
    for i in range(len(dna)):
        for j in range(len(dna[i])):
            ocurrences += searchHorizontal(dna, i, j)
            ocurrences += searchVertical(dna, i, j)
            ocurrences += searchDiagonal(dna, i, j)
            ocurrences += searchDiagonalInv(dna, i, j)
    mutant = ocurrences > 1
    test = Dna(dna_chain=dna, mutant=mutant, analysis_date=timezone.now())
    test.save()
    if ocurrences > 1:
        return HttpResponse()
    else:
        return HttpResponseForbidden()

def searchHorizontal(dna, i, j):
    matches = 0
    if j < len(dna[i]) - 3:
        data = dna[i][j]+dna[i][j+1]+dna[i][j+2]+dna[i][j+3]
        for seq in __sequences:
            if seq == data:
                matches += 1
    return matches

def searchVertical(dna, i, j):
    matches = 0
    if i < len(dna) - 3:
        data = dna[i][j]+dna[i+1][j]+dna[i+2][j]+dna[i+3][j]
        for seq in __sequences:
            if seq == data:
                matches += 1
    return matches

def searchDiagonal(dna, i, j):
    matches = 0
    if i < len(dna) - 3 and j < len(dna[i]) - 3:
        data = dna[i][j]+dna[i+1][j+1]+dna[i+2][j+2]+dna[i+3][j+3]
        for seq in __sequences:
            if seq == data:
                matches += 1
    return matches
       

def searchDiagonalInv(dna, i, j):
    matches = 0
    if i >= 3 and j < len(dna[i]) - 3:
        data = dna[i][j]+dna[i-1][j+1]+dna[i-2][j+2]+dna[i-3][j+3]
        for seq in __sequences:
            if seq == data:
                matches += 1
    return matches

class DnaView(viewsets.ModelViewSet):
    queryset = Dna.objects.all()
