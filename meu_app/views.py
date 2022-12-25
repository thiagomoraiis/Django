from django.template import loader
from .models import Aluno
from django.http import HttpResponse

# def meu_app(request):
#   alunos = Aluno.objects.all().values()
#   template = loader.get_template('template.html')
#   context = {
#     'alunos': alunos,
#   }
#   return HttpResponse(template.render(context, request))

# Create your views here.

def meu_app(request):
    alunos = Aluno.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'alunos': alunos,
    }
    return HttpResponse(template.render(context, request))

def detalhe(request, id):
    dAluno = Aluno.objects.get(id=id)
    template = loader.get_template('detalhe.html')
    context = {
        'dAluno':dAluno,
    }
    return HttpResponse(template.render(context, request))




