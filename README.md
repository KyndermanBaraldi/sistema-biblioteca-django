# Projeto Acadêmico de Desenvolvimento de Software Web para Controle de Biblioteca Escolar com Django e SQL

Este é um projeto acadêmico desenvolvido no âmbito da Disciplina de Projeto Integrador, do Curso de Computação 2ºSemestre/2021, da Universidade Virtual do Estado de São Paulo, e visa à criação de uma aplicação usando o framework Django, com banco de dados SQLite, para gerenciar uma biblioteca escolar.

## Membros do Grupo

## Justificativa
O sistema de gerenciamento de biblioteca escolar é uma ferramenta importante para a organização do acervo bibliográfico em uma escola. Com a digitalização das informações, torna-se fundamental a utilização de sistemas informatizados para gerir dados de alunos, professores, empréstimos de livros e consultas ao acervo.

Dessa forma, a criação de um sistema de gerenciamento de biblioteca escolar é uma demanda crescente nas instituições de ensino. A ferramenta tem como objetivo auxiliar a gestão do acervo, permitindo o cadastro e atualização dos livros, empréstimos, devoluções. Além disso, o sistema permite a geração de relatórios, facilitando a análise e tomada de decisão por parte dos gestores da biblioteca.

### Por que usar Python:
A escolha do Python se deve principalmente pela familiaridade do Grupo com a linguagem, que já fora estadada durante o curso. Porém vale destacar que o Python é uma linguagem de fácil assimilação e com sintaxe intuitiva, tem disponível grande acervo de pacotes e bibliotecas para extender suas funcionalidades, além de possuir uma comunidade ativa. Outros dois diferenciais que conferem vantagem ao Python são a gratuidade, pois o sistema Python tem licença de uso público, e a Portabilidade, já que é multiplataforma, podendo rodar em diversos sistemas operacionais.

### Por que fazer com Django:
Django é um framework de desenvolvimento web em Python, que possui diversas vantagens para o desenvolvimento de sistemas web. Algumas das razões para escolher Django para esse projeto incluem:

* Alta produtividade: Django possui um conjunto de ferramentas e bibliotecas que permitem a criação de sistemas web de forma rápida e eficiente, reduzindo o tempo de desenvolvimento.
* Escalabilidade: Django permite que o sistema seja escalável, ou seja, capaz de lidar com um grande número de usuários e dados.
* Segurança: Django é um framework seguro, que utiliza diversas medidas de segurança para proteger o sistema contra ameaças e ataques.
* Flexibilidade: Django é altamente configurável e personalizável, permitindo que o sistema seja adaptado às necessidades específicas da biblioteca escolar.
* Comunidade ativa: Django possui uma grande comunidade de desenvolvedores, que contribuem com bibliotecas, documentação e suporte técnico, facilitando o desenvolvimento do projeto e solução de problemas.

### Por que usar SQLite:
O SQLite é um banco de dados relacional de código aberto, que armazena os dados dentro de sua própira estrutura, sem a necessidade de um servidor para esse fim. O armazenando é feito em um único arquivo conferindo simplicidade ao sistema. Ele é indicado para aplicações web de tráfego médio bem cimo para sistemas mobile.
A escolha do SQLite para este projeto se deve a sua simplicidade de implementação, pela compatibilidade com o Framework Django e também por atender os demais requisitos da aplicação.


## Tecnologias Utilizadas
1. Python
2. Django
3. HTML
4. CSS
5. JavaScript
6. SQL

## Funcionalidades
O software web terá as seguintes funcionalidades:
- [ ] Cadastro de usuários
- [ ] Autenticação de usuários
- [ ] Busca de livros por título, autor, editora, ISBN e categoria
- [ ] Visualização das informações de cada livro
- [ ] Cadastro de novos livros
- [ ] Empréstimo de livros para usuários
- [ ] Devolução de livros por usuários
- [ ] Histórico de empréstimos e devoluções
- [ ] Controle de estoque de livros

Progresso: <progress value="0" max="100"></progress>

## Instalação
Para instalar e executar o software web, siga as seguintes instruções:

Clone o repositório do projeto para sua máquina local:

```console
git clone https://github.com/kynderman/biblioteca-django.git
```

Entre na pasta do projeto:

```console
cd biblioteca-django
```

Crie um ambiente virtual:

```console
python -m venv venv
```

Ative o ambiente virtual:

```console
source venv/bin/activate
```

Instale as dependências do projeto:

```console
pip install -r requirements.txt
```

Execute as migrações do banco de dados:

```console
python manage.py migrate
```

Inicie o servidor de desenvolvimento:

```console
python manage.py runserver
```

Abra o navegador e acesse o endereço http://localhost:8000/