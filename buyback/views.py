from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Companie, Client
from django.contrib import messages


def buybacks(request):
    comps = Companie.objects.all()
    return render(request, 'afbuyback.html',{'comps':comps})

def buybacku(request, comp):
    comp = Companie.objects.get(symbol = comp)
    if request.method == "POST":
        ccode = request.POST['client_code']

        if Client.objects.filter(ccode=ccode, comname = comp, status = False).exists():
            client = Client.objects.get(ccode = ccode, comname = comp)
            return render(request, 'buyback.html',{'client':client, 'comp':comp})
        elif Client.objects.filter(ccode=ccode, comname = comp, status = True).exists():
            messages.success(request, "You Have Already Applied.")
            return redirect('buybacku',comp)
        else:
            messages.error(request, "You Are Not Entitle To Buy Back.")
            return redirect('buybacku',comp)

    return render(request,'buyback.html',{'comp':comp})


def buybacksave(request, comp):
    comp = Companie.objects.get(symbol = comp)
    if request.method == "POST":
        ccode = request.POST['client_code']
        if Client.objects.filter(ccode=ccode, comname = comp, status = False).exists():
            client = Client.objects.get(ccode = ccode, comname = comp)
            client.qty = request.POST['lot_size']
            client.status = True
            client.save()
            messages.success(request, "You Have Applied Successfully.")
            return redirect('buybacku',comp)
        else:
            messages.success(request, "You Are Not Entitle To Buy Back.")
            return redirect('buybacku',comp)