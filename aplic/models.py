from django.db import models
from csvImporter.model import CsvDbModel
class Persona(models.Model):
    nombre=models.CharField(max_length=30)
    def __unicode__(self):
        return self.nombre
class MyCsvModel(CsvDbModel):
    nombre = models.CharField()
    class Meta:
        delimiter = ";"
        dbModel = Persona
