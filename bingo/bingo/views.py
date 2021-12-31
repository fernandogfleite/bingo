from random import choice

from django.shortcuts import redirect, render
from django.views import View


sorteados = list()
numeros_bingo = list(range(1, 91))

def sortear_numero():
    numero_sorteado = choice([i for i in range(1,91) if i not in sorteados])
    
    return numero_sorteado


class BingoView(View):
    template_name = 'bingo.html'
    def get(self, request):
        dados = {
            'sorteados': sorteados,
            'numeros_bingo': numeros_bingo
        }

        return render(request, self.template_name, dados)
    
    def post(self, request):
        numero_sorteado = sortear_numero()
        sorteados.append(numero_sorteado)

        dados = {
            'numero_sorteado': numero_sorteado,
            'sorteados': sorteados,
            'numeros_bingo': numeros_bingo
        }

        return render(request, self.template_name, dados)
    

def reseta_bingo(request):
    sorteados.clear()

    return redirect('bingo')
