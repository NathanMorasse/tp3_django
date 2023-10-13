from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from .forms import FermierForm

def index_view(request):
    return render(request, 'demo_app/index.html')

def fermiers_view(request):
    fermiers = models.Fermier.objects.all().order_by('prenom')
    context = {
        'fermier_list': fermiers,
    }

    form = FermierForm()
    if request.method == 'POST':
        if 'Ajouter' in request.POST:
            form = FermierForm(request.POST)
            form.save()
        if 'Modifier' in request.POST:
            pk = request.POST.get('Modifier')
            fermier = models.Fermier.objects.get(id=pk)
            form = FermierForm(instance=fermier)
    
    context['form'] = form
    return render(request, 'demo_app/fermiers.html', context)

def jardin_view(request):
    legumes = models.Legume.objects.all().order_by('nom')

    context = {
        'legume_list': legumes,
    }

    return render(request, 'demo_app/jardin.html', context)

def create_edit_fermier_view(request, id):
    context = {}
    form = FermierForm()
    fermier = models.Fermier.objects.get(id)
    form = FermierForm(instance=fermier)
    context['form'] = form
    context['id'] = id
    if id == 0:
        context['action'] = 'Ajouter'
    else:
        context['action'] = 'Modifier'
    return render(request, 'demo_app/create_edit_fermier.html', context)