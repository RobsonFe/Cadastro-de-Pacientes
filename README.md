# Formulário de Cadastro de Pacientes com Django

![Banner do Projeto](https://live.staticflickr.com/65535/53143951355_a89a8b6f00_b.jpg)

## Introdução

Bem-vindo(a) ao repositório **Formulário de Cadastro em Python com Django**, um espaço onde a magia do Python e a versatilidade do Django se unem para criar uma aplicação web incrível. Se você é apaixonado por desenvolvimento web e está curioso(a) sobre como construir um formulário de cadastro de pacientes, você está no lugar certo!

## Sobre o Projeto

Neste repositório, mergulhamos em uma aventura de desenvolvimento com Python e Django para criar um formulário de cadastro de pacientes. O objetivo era criar uma aplicação simples, mas funcional, que registrasse dados e os armazenasse de forma eficiente.

### O Desafio

A ideia de criar um formulário de cadastro usando Django surgiu como um desafio estimulante. Queria explorar as capacidades do Django em combinação com a praticidade do SQLite, um banco de dados que se encaixa perfeitamente em projetos menores, como este.

### A Jornada

Ao longo dessa jornada, pude aproveitar a maravilhosa ferramenta que é o Django. Sua facilidade de uso permitiu que eu incorporasse não apenas a lógica dos dados, mas também o poder do HTML e CSS para criar uma experiência completa. A criação de rotas também se mostrou intuitiva, permitindo que eu focasse mais no desenvolvimento real e menos na infraestrutura.

## Funcionalidades Principais

- Formulário de cadastro de pacientes.
- Armazenamento eficiente dos registros usando SQLite.
- Utilização de sintaxe amigável do Django para criação de rotas.

## Imagens do Projeto

- Formulário de Cadastro

Ficha de Cadastro de Pacientes com as informações necessárias para o preenchimento.

![Formulário de Cadastro](https://live.staticflickr.com/65535/53144029238_e518b1f028_b.jpg)

- Exibição do Banco
  
Podemos observar nesta imagem a exibição do banco de dados onde estão armazenadas as informações dos pacientes.

![Exibição do Banco](https://live.staticflickr.com/65535/53144029278_c52cfaceef_b.jpg)

## Linhas de Codigos usadas no Projeto. 

- Rota responsavel para a pagina principal. 

- Foi utilizado um link direcionando para a pagina principal toda vez que clicava no nome "Hospital da Saude".

``` from django.urls import path  ```
  
```from app_cadastro import views ```

```
urlpatterns = [
    #rota, view responsável, nome de referência. 
    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]

```

- Link fixo na home sem alterar a estrutura da pagina, deixando a NavBar fixa na tela.
```
<body>
  <nav style="background-color: rgb(13, 146, 102) !important;" class="navbar navbar-light bg-light">
    <div class="container-fluid">
      <span class="navbar-brand mb-0 h1"><a style="text-decoration: none;color: black;" href="{% url 'home' %}">Hospital
          da Saúde</a></span>
    </div>
  </nav>
  {% block conteudo %}
  {% endblock %} 
  ```


- Importação dos dados do usuario para ser exibidos em tela. 

```from django.shortcuts import render```

```from .models import Usuario```

``` def home(request): ```

``` return render(request,'usuarios/home.html') ```

```
def usuarios(request):
    #salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.profissao = request.POST.get('profissao')
    novo_usuario.nascimento = request.POST.get('nascimento')
    novo_usuario.plano_saude = request.POST.get('plano_saude')
    novo_usuario.diagnostico = request.POST.get('diagnostico')
    novo_usuario.save() ```
    ```
    #Exibir todos os usuarios já cadastrados em uma pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a pagina de usuarios.
    return render(request,'usuarios/usuarios.html',usuarios)
```

## Video do Projeto

[Assista ao vídeo do projeto](https://youtu.be/0b5RaGfEbtI)

## Próximos Passos

Este é apenas o começo. Meu desejo é expandir este projeto e desenvolver uma aplicação CRUD completa com Django.

## Como Usar Este Repositório

Sinta-se à vontade para explorar os arquivos e pastas deste repositório para descobrir como criei o formulário de cadastro de pacientes usando Django. Você pode examinar o código, entender a estrutura e até mesmo testar a aplicação por conta própria.

## Contato

Gostaria de trocar ideias, discutir estratégias de desenvolvimento ou compartilhar seus projetos? Vamos nos conectar [aqui](https://www.linkedin.com/in/robson-ferreira-508247134/)!
