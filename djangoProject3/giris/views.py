from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import PcEkleme
from .models import Satıs


def ilksayfa(request):
    return render(request, 'giris/ilksayfa.html')

def ekle(request):
    submitted=False
    if request.method=='POST':
        form=PcEkleme(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            k=Satıs()
            k.marka=cd["marka"];
            k.model = cd["model"];
            k.fiyat = cd["fiyat"];
            k.tel = cd["tel"];
            k.adres = cd["adres"];
            k.save();
            cd=form.cleaned_data
            return HttpResponseRedirect('/ekle?submitted=True')

    else:
        form = PcEkleme()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'giris/ekle.html',{'form':form,'submitted':submitted})

def index(request):
    form=PcEkleme()
    if request.method=='POST':
        form=PcEkleme(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"giris/ekle.html",context)



def index(request):
    pcler=Satıs.objects.all()

    context={
        'pcler':pcler
    }

    return render(request, 'giris/getir.html',context)