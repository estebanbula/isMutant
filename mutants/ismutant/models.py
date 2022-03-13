from django.db import models

class Dna(models.Model):
    dna_chain = models.CharField(max_length=200, null=False)
    mutant = models.BooleanField(default=0, null=False)
    analysis_date = models.DateTimeField()

    def __str__(self):
        return self.dna

    def analysis_day(self):
        return self.analysis_date