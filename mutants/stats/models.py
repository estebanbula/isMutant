from django.db import models

class Stats(models.Model):
    count_mutant_dna = models.IntegerField(default=0, null=False)
    count_human_dna = models.IntegerField(default=0, null=False)
    ratio = models.FloatField(default=0.0, null=False)
