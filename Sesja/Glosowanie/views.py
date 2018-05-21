
from django.shortcuts import render
from .models import Uchwala, Glosowanie, User
from .forms import GlosowanieForm, WszystkieUchwalyForm
from django.http import HttpResponseRedirect,HttpResponse



def lista_uchwal(request):
    uchwaly = Uchwala.objects.all()
    context = {'uchwaly': uchwaly}
    return render(request, 'lista_uchwal.html', context)

def wszystkie_uchwaly(request):
    uchwaly = Uchwala.objects.all().order_by('-id')
    form = WszystkieUchwalyForm(request.POST or None)
    context = {
        'uchwaly': uchwaly,
        'form': form,
    }
    return render(request, 'wszystkie_uchwaly.html', context)

def pojedyncza_uchwala(request, id_uchwaly):
    glos = form = ''
    za = przeciw = wstrzymal_sie = 0
    uchwala = Uchwala.objects.get(pk=id_uchwaly)
    glosowanie = Glosowanie.objects.filter(id_uzytkownika = request.user, id_uchwaly = uchwala)
    czy_glosowano = glosowanie.exists()
    if request.user.is_superuser:
        glosowanie = Glosowanie.objects.filter(id_uchwaly = uchwala).order_by('id_uzytkownika__last_name')
        za = przeciw = wstrzymal_sie = 0
        for g in glosowanie:
            user = g.id_uzytkownika
            if g.vote == 1:
                za+=1
            elif g.vote == 0:
                przeciw+=1
            else:
                wstrzymal_sie+=1
    else:
        if not czy_glosowano:
            form = GlosowanieForm(request.POST or None)
            if form.is_valid():
                f = form.save(commit=False)
                f.id_uchwaly = uchwala
                f.id_uzytkownika = request.user
                f.save()
                return HttpResponseRedirect(request.path_info)
        else:
            glos = Glosowanie.objects.get(pk=str(glosowanie.first()))

    context = {
        'uchwala': uchwala,
        'form': form,
        'czy_glosowano':czy_glosowano,
        'glos':glos,
        'glosowanie':glosowanie,
        'za':za,
        'przeciw':przeciw,
        'wstrzymal_sie':wstrzymal_sie
    }

    return render(request, 'uchwala.html', context)
