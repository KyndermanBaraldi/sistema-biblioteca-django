from django.shortcuts import redirect, render
from django.http import HttpResponse

from usuarios.models import Usuario
# Create your views here.


def cadastrar(request):
    return HttpResponse('cadastrar livro')


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session.get('usuario'))
        return HttpResponse('home livro')
    else:
        return redirect('/auth/login/?status=1&mensagem=Usuário não logado')
