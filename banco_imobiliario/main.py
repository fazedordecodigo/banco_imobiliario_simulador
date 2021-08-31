from config import Configuracao
from entidades import Vencedor, Resultado


def handler():
    resultado = Resultado()

    for simulacao in range(1, 301):
        configuracao = Configuracao()
        tabuleiro = configuracao.montar_tabuleiro()
        dado = configuracao.retorna_dado()
        jogadores = configuracao.retorna_jogadores()
        
        for rodada in range(1, 1001):
            if tabuleiro.retorna_qtd_jogadores() <= 1:
                break

            for jogador in jogadores:
                if jogador.retorna_em_jogo():
                    casa = jogador.avancar_casas(dado.sortear())
                    propriedade = tabuleiro.retornar_propriedade(casa)
                    jogador.analisar(propriedade)

        resultado.adicionar_vencedor(
            Vencedor(rodada, tabuleiro.retornar_vencedor())
        )
            
    resultado.exibir()


if __name__ == '__main__':
    handler()
