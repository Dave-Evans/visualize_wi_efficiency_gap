# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone

# Create your models here.
class AsmDistricts(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    asm = models.IntegerField()
    asmdem16 = models.FloatField()
    asmrep16 = models.FloatField()
    asmdemwasted16 = models.FloatField()
    asmrepwasted16 = models.FloatField()
    asmtot16 = models.FloatField()

    asmdem14 = models.FloatField()
    asmrep14 = models.FloatField()
    asmdemwasted14 = models.FloatField()
    asmrepwasted14 = models.FloatField()
    asmtot14 = models.FloatField()    

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return str(self.asm)