from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from livro.models import LivroForm, Livros

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

    if livro_id:
        livro = get_object_or_404(Livros, pk=livro_id)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return render(request, 'livro_sucesso.html')
    else:
        form = LivroForm(instance=livro)

    return render(request, 'livro_form.html', {'form': form})


def detalhes_livro(request, livro_id):

    try:
        livro = get_object_or_404(Livros, pk=livro_id)
        usuario = Usuario.objects.get(id=request.session.get('usuario'))
    except:
        usuario = None

    return render(request, 'detalhes_livro.html', {'usuario': usuario, 'livro': livro})


def emprestimo(request):
    return HttpResponse('emprestimo livro')


def emprestar(request):
    return HttpResponse('emprestar livro')


def listar(request):
    return HttpResponse('listar livro')


def novo(request):
    return cadastrar(request)


def fake(request):

    livros = [
        {'titulo': 'O Labirinto de ossos', 'autor': 'Rick Riordan', 'editora': 'Intrínseca',
            'isbn': '978-85-8057-032-4', 'categoria': 'Ficção infantojuvenil', 'quantidade': 10},
        {'titulo': 'As Crônicas de Nárnia: O Leão, A Feiticeira e o Guarda-Roupa', 'autor': 'C.S. Lewis',
            'editora': 'WMF Martins Fontes', 'isbn': '978-85-7827-271-6', 'categoria': 'Ficção infantojuvenil', 'quantidade': 8},
        {'titulo': 'A Revolução dos Bichos', 'autor': 'George Orwell', 'editora': 'Companhia das Letras',
            'isbn': '978-85-359-3226-0', 'categoria': 'Ficção distópica', 'quantidade': 15},
        {'titulo': 'O Código Da Vinci', 'autor': 'Dan Brown', 'editora': 'Arqueiro',
            'isbn': '978-85-8041-674-9', 'categoria': 'Ficção de suspense', 'quantidade': 20},
        {'titulo': 'A Arte da Guerra', 'autor': 'Sun Tzu', 'editora': 'L&PM Pocket',
            'isbn': '978-85-254-1721-1', 'categoria': 'Filosofia e estratégia militar', 'quantidade': 5},
    ]

    livros = [
        {'titulo': 'O Sol é Para Todos', 'autor': 'Harper Lee', 'editora': 'Editora José Olympio',
            'isbn': '978-85-03-00194-7', 'categoria': 'Ficção', 'quantidade': 12},
        {'titulo': '1984', 'autor': 'George Orwell', 'editora': 'Companhia das Letras',
            'isbn': '978-85-359-0277-6', 'categoria': 'Ficção distópica', 'quantidade': 7},
        {'titulo': 'A Sangue Frio', 'autor': 'Truman Capote', 'editora': 'Companhia das Letras',
            'isbn': '978-85-359-1241-3', 'categoria': 'Não-ficção', 'quantidade': 3},
        {'titulo': 'O Conde de Monte Cristo', 'autor': 'Alexandre Dumas', 'editora': 'Penguin-Companhia',
            'isbn': '978-85-250-0031-7', 'categoria': 'Ficção', 'quantidade': 20},
        {'titulo': 'A Hora da Estrela', 'autor': 'Clarice Lispector', 'editora': 'Rocco',
            'isbn': '978-85-325-0328-0', 'categoria': 'Ficção', 'quantidade': 15}
    ]

    for livro in livros:
        novo_livro = Livros.objects.create(
            titulo=livro['titulo'],
            autor=livro['autor'],
            editora=livro['editora'],
            isbn=livro['isbn'],
            categoria=livro['categoria'],
            quantidade=livro['quantidade']
        )
        novo_livro.save()

    return HttpResponse('Livros cadastrados com sucesso!')
