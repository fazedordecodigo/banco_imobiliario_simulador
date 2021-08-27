from random import random
from config import Configuracao
from models import Dado, Impulsivo, Exigente, Cauteloso, Aleatorio


def handler():
    for simulacao in range(1, 301):
        configuracao = Configuracao()
        tabuleiro = configuracao.montarTabuleiro()
        dado = Dado()

        jogadores = [
            Impulsivo(), Exigente(), Cauteloso(), Aleatorio()
        ]

        for rodada in range(1, 1001):
            for jogador in jogadores:
                casa = jogador.avancarCasas(dado.sortear(), tabuleiro.quantidadeDeCasas())
                propriedade = tabuleiro.retornarPropriedade(casa)
                jogador.analisar(propriedade)

                print(f"Rodada: {rodada}, {str(jogador)}")

    

if __name__=='__main__':
    handler()
