from django.shortcuts import render
from enquetes.models import Enquete

from django.db import *

# Create your views here.
def bemvindo(request):
	return render(request, 'bemvindo.html')

def exibir(request, enquete_id):
	enquete = Enquete.objects.get(id=enquete_id)
	return render(request, 'enquete.html', {'enquete' : enquete})