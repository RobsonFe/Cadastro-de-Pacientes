from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.profissao = request.POST.get('profissao')
    novo_usuario.nascimento = request.POST.get('nascimento')
    novo_usuario.plano_saude = request.POST.get('plano_saude')
    novo_usuario.diagnostico = request.POST.get('diagnostico')
    novo_usuario.save()
    
    #Exibir todos os usuarios já cadastrados em uma pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a pagina de usuarios.
    return render(request,'usuarios/usuarios.html',usuarios)