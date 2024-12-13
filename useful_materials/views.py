from django.shortcuts import render
from useful_materials.models import Useful_Materials

def useful_materials_view(request):
    materials = Useful_Materials.objects.all()
    return render(request, 'useful_materials/material.html', {'materials': materials})
