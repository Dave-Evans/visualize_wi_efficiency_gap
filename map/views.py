# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from map.models import AsmDistricts


# Create your views here.

def gap_map(request):
	
	return render(request, 'map/index.html', {})



def get_map_data(request, type='asm'):
	'''For returning the district layer
	for now just asm, but could be sen or con
	'''

	data = serialize('geojson', AsmDistricts.objects.all(), geometry_field='mpoly')#, fields=('asm',)
	return HttpResponse(data, content_type='json')



# def get_map_data(request):
# from vectorformats.Formats import Django, GeoJSON
# 	asm_dists = AsmDistricts.objects.all()

# 	djf = Django.Django(geodjango='mpoly', properties=['asm'])
# 	geojsn = GeoJSON.GeoJSON()
# 	s = geojsn.encode(djf.decode(asm_dists))