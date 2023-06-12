from django.shortcuts import render

def listafilmes(request):
        return render(request, 'filme/listafilmes.html', {}     )
