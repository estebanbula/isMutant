from django.test import TestCase
from django.http import HttpResponse, HttpResponseForbidden
import unittest
from views import mutant

# Create your tests here.
class TestingFunctions(TestCase):
    def test_mutant(self):
        self.assertEqual(mutant(["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]), HttpResponse)
        self.assertEqual(mutant(["ATGCGA","CAGTGC","TTATGT","AGAAGG","CTTCTA","TCACTG"]), HttpResponse)
        self.assertEqual(mutant(["CTGCGA","CAGTGC","TTATGT","AGAATG","CCCCTA","TCACCG"]), HttpResponseForbidden)
        self.assertEqual(mutant(["TTGCGT","CAGAGC","AAATGT","AGAAAG","CGCGTA","TCACTG"]), HttpResponseForbidden)
