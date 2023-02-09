from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import FormularioEstudante
from .models import Estudante

# Create your views here.

def index(request):
    return render(request, 'estudantes/index.html', {
        'estudantes': Estudante.objects.all()
    })

def ver_estudante(request, id):
    estudante = Estudante.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def adicionar(request):
    if request.method == 'POST':
        form = FormularioEstudante(request.POST)
        if form.is_valid():
            novo_numero_estudante = form.cleaned_data['numero_estudante']
            novo_primeiro_nome = form.cleaned_data['primeiro_nome']
            novo_segundo_nome = form.cleaned_data['segundo_nome']
            novo_email = form.cleaned_data['email']
            novo_curso = form.cleaned_data['curso']
            novo_media = form.cleaned_data['media']
        
            novo_estudante = Estudante(
                numero_estudante = novo_numero_estudante,
                primeiro_nome = novo_primeiro_nome,
                segundo_nome = novo_segundo_nome,
                email = novo_email,
                curso = novo_curso,
                media = novo_media
            )
            novo_estudante.save()
            return render(request, 'estudantes/adicionar.html', {
                'form': FormularioEstudante(),
                'sucesso': True
                })
    else:
        form = FormularioEstudante()
    return render(request, 'estudantes/adicionar.html', {
        'form': FormularioEstudante()
    })

def editar(request, id):
    if request.method == 'POST':
        estudante = Estudante.objects.get(pk=id)
        form = FormularioEstudante(request.POST, instance=estudante)
        if form.is_valid():
            form.save()
            return render(request, 'estudantes/editar.html', {
                'form':form,
                'sucesso':True
            })
    else:
        estudante = Estudante.objects.get(pk=id)
        form = FormularioEstudante(instance=estudante)
    return render(request, 'estudantes/editar.html', {
        'form': form
    })

def deletar(request, id):
    if request.method == 'POST':
        estudante = Estudante.objects.get(pk=id)
        estudante.delete()
    return HttpResponseRedirect(reverse('index'))
