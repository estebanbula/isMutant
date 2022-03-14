from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Dna
import re
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse

__sequences = ['AAAA', 'TTTT', 'CCCC', 'GGGG']

@api_view(['POST'])
def mutant(request):
    data = JSONParser().parse(request)
    dna = data['dna']
    ocurrences = 0
    if not validateDna(dna):
        raise TypeError('Valores incorrectos en cadena de ADN')
    for i in range(len(dna)):
        for j in range(len(dna[i])):
            ocurrences += searchHorizontal(dna, i, j)
            ocurrences += searchVertical(dna, i, j)
            ocurrences += searchDiagonal(dna, i, j)
            ocurrences += searchDiagonalInv(dna, i, j)
    mutant = ocurrences > 1
    test = Dna(dna_chain=dna, mutant=mutant, analysis_date=timezone.now())
    test.save()
    if mutant:
        return HttpResponse()
    else:
        return HttpResponseForbidden()

@api_view(['GET'])
def stats(request):
    mutants_count = len(Dna.objects.filter(mutant=True))
    human_count = len(Dna.objects.filter(mutant=False))
    ratio = mutants_count / human_count
    stat = {
        'count_mutant_dna': mutants_count,
        'count_human_dna': human_count,
        'ratio': ratio
    }
    return JsonResponse(stat)

def validateDna(dna):
    values = []
    for chain in dna:
        exp = re.findall('[BDEFHIJKLMNOPQRSUVXYZ0-9]', chain)
        if exp:
            values.append(exp)
    if values is None:
        return True
    else:
        return False

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