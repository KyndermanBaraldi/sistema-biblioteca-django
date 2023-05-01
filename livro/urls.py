from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar, name='buscar'),
    path('listar/', views.listar, name='listar'),
    path('emprestimo/', views.emprestimo, name='emprestimo'),
    path('emprestar/', views.emprestar, name='emprestar'),
    path('novo/', views.novo, name='cadastrarLivro'),
    path('cadastro/<int:livro_id>/', views.cadastrar, name='cadastrarLivro'),
    path('livro/<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
    # path('fake/', views.fake, name='fake')
]
