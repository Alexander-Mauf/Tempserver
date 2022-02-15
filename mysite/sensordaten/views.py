from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from . import serializers, models
from django.db.models import Max
from django.db.models import Min
from django.db.models import Avg


anfangsDatenpunkt = 0
endDatenpunkt = 100

def index(request):
    return HttpResponse("""Hier soll man versichiedene Datenstruckturen anwählen können (Index) """)

def infotext(request):
    return HttpResponse("hier soll in zukunft genaue Datenstuckturen abgefragt werden können")

def admin(request):
    return redirect("/admin")

def neuer(request):
    if anfangsDatenpunkt <= 100:
        anfangsDatenpunkt = anfangsDatenpunkt - (anfangsDatenpunkt - 1)
        endDatenpunkt = endDatenpunkt - (anfangsDatenpunkt - 1)
    else:
        anfangsDatenpunkt = anfangsDatenpunkt - 100
        endDatenpunkte = endDatenpunkt - 100

    nix()
    return redirect("/sensordaten")

def älter(request):
    anfangsDatenpunkt = 100
    endDatenpunkt = anfangsDatenpunkt + 100
    nix()
    return redirect("/sensordaten/{}-{}".format(anfangsDatenpunkt,endDatenpunkt))



def nix(request):
    anfangsDatenpunkt = 0
    endDatenpunkt = 100
    print(request.user.username)
    standorte = models.Standort.objects.all()
    maximum   = models.Messwert.objects.aggregate(Höchsttemperatur=Max('wert'))
    minimum   = models.Messwert.objects.aggregate(Niedrigsttemperatur=Min('wert'))
    Average   = models.Messwert.objects.aggregate(DurchschnittlicheTemperatur=Avg('wert'))
    messwerte = models.Messwert.objects.order_by('-created_at')[0:100] #[anfangsDatenpunkt:endDatenpunkt]      #die "[0:100] müssen variablen werden, welche in die UrI kommen, um die derzeitigen werte anzuzeigen
    for messwert in messwerte:
        messwert.wert = round(messwert.wert,2)

    return render(request,"overview.html",{
        "request":request,
        "standorte": standorte,
        "messwerte": messwerte,
        "maximum": maximum.get("Höchsttemperatur"),
        "minimum": minimum.get("Niedrigsttemperatur"),
        "average": round(Average.get("DurchschnittlicheTemperatur"),2)
    })


def neu(request, neustereintrag, ältestereintrag):
    anfangsDatenpunkt = models.Messwert.objects.get(id=neustereintrag)
    endDatenpunkt = models.Messwert.objects.get(id=ältestereintrag)
    print("anfangsid {} endid{}".format(anfangsDatenpunkt, endDatenpunkt))
    print(request.user.username)
    standorte = models.Standort.objects.all()
    maximum   = models.Messwert.objects.aggregate(Höchsttemperatur=Max('wert'))
    minimum   = models.Messwert.objects.aggregate(Niedrigsttemperatur=Min('wert'))
    Average   = models.Messwert.objects.aggregate(DurchschnittlicheTemperatur=Avg('wert'))
    messwerte = models.Messwert.objects.order_by('-created_at')[0:100] #[anfangsDatenpunkt:endDatenpunkt]      #die "[0:100] müssen variablen werden, welche in die UrI kommen, um die derzeitigen werte anzuzeigen
    for messwert in messwerte:
        messwert.wert = round(messwert.wert,2)

    return render(request,"overview.html",{
        "request":request,
        "standorte": standorte,
        "messwerte": messwerte,
        "maximum": maximum.get("Höchsttemperatur"),
        "minimum": minimum.get("Niedrigsttemperatur"),
        "average": round(Average.get("DurchschnittlicheTemperatur"),2)
    })


class MesswertViewSet(viewsets.ModelViewSet):
    queryset = models.Messwert.objects.all()
    serializer_class = serializers.MesswertSerializer

class StandortViewSet(viewsets.ModelViewSet):
    queryset = models.Standort.objects.all()
    serializer_class = serializers.StandortSerializer


def pie_chart(request):
    labels = []
    data = []

    queryset = models.Messwert.objects.order_by('wert')[:5]
    for city in queryset:
        labels.append(MesswertViewSet.name)
        data.append(city.population)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })