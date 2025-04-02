from django.shortcuts import render
from .models import Devices

def device_list(request):
    # Récupérer tous les devices depuis la base de données
    devices = Devices.objects.order_by("-name")
    # Passer les devices au template
    return render(request, 'device_list.html', {'devices': devices})

def device_detail(request, pk):
    # Récupérer le device spécifique depuis la base de données
    device = Devices.objects.get(pk=pk)
    # Passer le device au template
    return render(request, 'device_detail.html', {'device': device})