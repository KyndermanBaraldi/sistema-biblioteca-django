from django.shortcuts import redirect, render
from django.http import HttpResponse

from usuarios.models import Usuario
from hashlib import sha256


def login(request):
    status = request.GET.get('status', None)
    mensagem = request.GET.get('mensagem', None)
    return render(request, 'login.html', {'status': status, 'mensagem': mensagem})


def cadastro(request):
    status = request.GET.get('status', None)
    mensagem = request.GET.get('mensagem', None)
    return render(request, 'cadastro.html', {'status': status, 'mensagem': mensagem})


def cadastrar(request):

    nome, email, senha = request.POST['nome'], request.POST['email'], request.POST['senha']

    if len(nome.strip()) < 3 or len(email.strip()) < 3:
        return redirect('/auth/cadastrar/?status=1&mensagem=Nome ou email inválidos')

    if len(senha.strip()) < 8:
        return redirect('/auth/cadastrar/?status=1&mensagem=Senha inválida')

    usuario = Usuario.objects.filter(email=email).first()

    if usuario:
        return redirect('/auth/cadastrar/?status=1&mensagem=Email já cadastrado')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario.save()
        return redirect('/auth/login/?status=0&mensagem=Usuário cadastrado com sucesso')

    except:
        return redirect('/auth/cadastrar/?status=1&mensagem=Erro ao cadastrar usuário')


def entrar(request):

    email, senha = request.POST['email'], request.POST['senha']

    if len(email.strip()) < 3:
        return redirect('/auth/login/?status=1&mensagem=Email inválido')

    if len(senha.strip()) < 8:
        return redirect('/auth/login/?status=1&mensagem=Senha inválida')

    senha = sha256(senha.encode()).hexdigest()
    usuario = Usuario.objects.filter(email=email, senha=senha).first()

    if usuario:
        request.session['usuario'] = usuario.id
        return redirect('/?status=0&mensagem=Usuário logado com sucesso')

    return redirect('/auth/login/?status=1&mensagem=Email ou senha inválidos')


def sair(request):
    del request.session['usuario']
    return redirect('/?status=0&mensagem=Usuário deslogado com sucesso')
