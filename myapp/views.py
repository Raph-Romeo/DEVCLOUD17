from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Personne

# Create your views here.


def index(request):
    personnes = Personne.objects.all()
    return render(request, 'index.html', {"personnes":personnes})


def name_form(request):
    if request.method == 'POST':
            prenom = request.POST.get('prenom')
            nom = request.POST.get('nom')
            if len(prenom) > 1 and len(nom) > 1:
                person = Personne(nom=nom, prenom=prenom)
                person.save()
                #return render(request, 'success.html', {'person': person})
                return HttpResponseRedirect('/')
            else:
                #form is invalid
                return HttpResponseRedirect('/form')
    else:
        return render(request, 'form.html', {'form': 'create', 'person': None})


def edit(request, id):
    person = Personne.objects.get(pk=id)
    if request.method == 'POST':
            prenom = request.POST.get('prenom')
            nom = request.POST.get('nom')
            if len(prenom) > 1 and len(nom) > 1:
                person.nom = nom
                person.prenom = prenom
                person.save()
                #return render(request, 'success.html', {'person': person})
                return HttpResponseRedirect('/')
            else:
                #form is invalid
                return HttpResponseRedirect('/form')
    else:
        return render(request, 'form.html', {'form': 'edit', 'person': person})


def delete(request, id):
    name = Personne.objects.get(pk=id)
    name.delete()
    return HttpResponseRedirect('/')
