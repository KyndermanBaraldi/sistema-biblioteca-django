from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar, name='buscar'),
    path('estoque/', views.estoque, name='estoque'),
    path('historico/', views.historico, name='historico'),
    path('novo/', views.novo, name='novo'),
    path('apagar/<int:livro_id>/', views.apagar, name='apagar'),
    path('emprestar/<int:livro_id>/', views.emprestar, name='emprestar'),
    path('cadastro/<int:livro_id>/', views.cadastrar, name='cadastrarLivro'),
    path('livro/<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
]
