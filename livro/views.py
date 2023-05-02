from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render
from livro.models import Emprestimo, LivroForm, Livros

from usuarios.models import Usuario
# Create your views here.


def home(request):
    try:
        usuario = Usuario.objects.get(id=request.session.get('usuario'))
    except:
        usuario = None

    return render(request, 'home.html', {'usuario': usuario})


def buscar(request):
    buscar = request.GET.get('buscar', None)

    try:
        usuario = Usuario.objects.get(id=request.session.get('usuario'))

        if buscar is None:
            livros = Livros.objects.all()
        else:
            livros = Livros.objects.filter(titulo__icontains=buscar)

    except:
        usuario = None
        livros = None

    return render(request, 'buscar.html', {'usuario': usuario, 'livros': livros})


def cadastrar(request, livro_id=None):

    livro = None
    try:
        if livro_id:
            livro = get_object_or_404(Livros, pk=livro_id)
        usuario = Usuario.objects.get(id=request.session.get('usuario'))
    except:
        usuario = None

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return render(request, 'livro_sucesso.html', {'usuario': usuario})
    else:
        form = LivroForm(instance=livro)

    return render(request, 'livro_form.html', {'usuario': usuario, 'form': form})


def detalhes_livro(request, livro_id):

    try:
        livro = get_object_or_404(Livros, pk=livro_id)
        livro_anterior = Livros.objects.filter(
            id__lt=livro.id).order_by('-id').first()
        proximo_livro = Livros.objects.filter(
            id__gt=livro.id).order_by('id').first()
        usuario = Usuario.objects.get(id=request.session.get('usuario'))

        context = {
            'usuario': usuario,
            'livro': livro,
            'livro_anterior': livro_anterior,
            'proximo_livro': proximo_livro,
        }

    except:
        context = None

    return render(request, 'detalhes_livro.html', context=context)


def apagar(request, livro_id):

    try:
        livro = get_object_or_404(Livros, pk=livro_id)
        usuario = Usuario.objects.get(id=request.session.get('usuario'))
    except:
        usuario = None

    if request.method == 'POST':
        livro.delete()
        return render(request, 'apagado_sucesso.html', {'usuario': usuario})

    return render(request, 'apagar.html', {'usuario': usuario, 'livro': livro})


def emprestar(request, livro_id):

    try:
        livro = get_object_or_404(Livros, pk=livro_id)

        usuarios = Usuario.objects.all()
        usuario = usuarios.get(id=request.session.get('usuario'))

    except:
        usuario = None

    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        data_emprestimo = datetime.now().date()
        data_devolucao = data_emprestimo + timedelta(days=7)

        emprestimo = Emprestimo(livro=livro, usuario_id=usuario_id,
                                data_emprestimo=data_emprestimo, data_devolucao=data_devolucao)
        emprestimo.save()

        livro.disponivel -= 1
        livro.save()

        return render(request, 'emprestimo_sucesso.html', {'usuario': usuario})

    return render(request, 'emprestimo.html', {'usuario': usuario, 'livro': livro, 'usuarios': usuarios})


def estoque(request):
    try:
        usuario = Usuario.objects.get(id=request.session.get('usuario'))
        livros = Livros.objects.all()

    except:
        usuario = None
        livros = None

    return render(request, 'estoque.html', {'usuario': usuario, 'livros': livros})


def historico(request):

    try:
        usuario = Usuario.objects.get(id=request.session.get('usuario'))
    except:
        usuario = None

    try:
        if usuario.admin:
            emprestimos = Emprestimo.objects.all()
        else:
            emprestimos = Emprestimo.objects.filter(usuario=usuario)

        devolvidos = emprestimos.filter(devolvido=True)
        nao_devolvidos = emprestimos.filter(
            devolvido=False, data_devolucao__gte=datetime.now().date())
        atrasados = emprestimos.filter(
            data_devolucao__lt=datetime.now().date(), devolvido=False)

    except:
        emprestimos = None

    context = {
        'usuario': usuario,
        'devolvidos': devolvidos,
        'nao_devolvidos': nao_devolvidos,
        'atrasados': atrasados,
    }

    return render(request, 'historico.html', context=context)


def novo(request):
    return cadastrar(request)
