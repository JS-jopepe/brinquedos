from django.shortcuts import render

# Create your views here.

def home(request):
    nome = 'Jovenel'
    idade = '16'
    text = 'Vem conhecer os nossos brinquedos'
    lista_brinquedos = [
        'Banco Imobilário',
        'Lol Surprise',
        'Boneca Reborn',
        'Shopkins',
        'Angie Oral Care',
        'Hatchimals',
        'John Deere Construction',
        'Baby Madeira ',
    ]

    context = {
        'brinquedos' :  lista_brinquedos,
        'nome' : nome
        'idade' : idade
        'text' : text
    }

    return render(request, 'home.html', context)