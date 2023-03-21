from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # SALVAR OS DADOS DA TELA NO BANCO DE DADOS
    novo_usuarios = Usuario()
    novo_usuarios.nome = request.POST.get('nome')
    novo_usuarios.idade = request.POST.get('idade')
    novo_usuarios.save()
    #EXIBIR TODOS OS USUARIOS CADASTRADOS
    usuarios = {
        'usuarios': Usuario.objects.all(    )
    }
    # RETORNAR OS DADOS A PAGINA
    return render(request, 'usuarios/usuarios.html', usuarios)