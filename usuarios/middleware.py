from django.shortcuts import redirect

from usuarios.models import Usuario

free_routes: set = {
    '/', '/auth/login/', '/auth/cadastro/', '/auth/cadastrar/', '/auth/entrar/'
}


def autenticado(get_response):
    def middleware(request):

        try:
            Usuario.objects.get(id=request.session.get('usuario'))
        except:
            if not request.path in free_routes:
                return redirect('/auth/login/?status=1&mensagem=Usuário não logado')
        else:
            if request.path in (free_routes - {'/', }):
                return redirect('/?status=1&mensagem=Usuário já logado')

        response = get_response(request)

        return response

    return middleware
