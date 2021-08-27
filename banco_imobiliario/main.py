from config import Configuracao
from models import Impulsivo, Exigente, Cauteloso, Aleatorio, Dado, Vencedor, Resultado


def handler():
    resultado = Resultado()

    for simulacao in range(1, 301):
        configuracao = Configuracao()
        tabuleiro = configuracao.montar_tabuleiro()
        dado = Dado()

        jogadores = [
            Impulsivo(tabuleiro), Exigente(tabuleiro), Cauteloso(tabuleiro), Aleatorio(tabuleiro)
        ]

        tabuleiro.adicionar_jogadores(jogadores)
        
        for rodada in range(1, 1001):
            if tabuleiro.retorna_qtd_jogadores() > 1:
                for jogador in jogadores:
                    if jogador.retorna_em_jogo():
                        casa = jogador.avancar_casas(dado.sortear())
                        propriedade = tabuleiro.retornar_propriedade(casa)
                        jogador.analisar(propriedade)
                        #print(f"Simulação: {simulacao}, Rodada: {rodada}, {str(jogador)}")
            else:
                break
        resultado.adicionar_vencedor(
            Vencedor(rodada, tabuleiro.retornar_vencedor()))
            
    print(resultado)



if __name__ == '__main__':
    handler()
