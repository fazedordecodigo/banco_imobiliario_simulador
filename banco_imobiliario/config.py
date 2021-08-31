from banco_imobiliario.entidades import Propriedade, Tabuleiro, Dado, Impulsivo, Exigente, Cauteloso, Aleatorio


class Configuracao:
    def __init__(self) -> None:
        self.__propriedades = [
            Propriedade(100, 50), Propriedade(80, 20), Propriedade(10, 5), Propriedade(200, 100),
            Propriedade(95, 40), Propriedade(120, 90), Propriedade(15, 2), Propriedade(35, 6),
            Propriedade(160, 100), Propriedade(500, 350), Propriedade(70, 30), Propriedade(55, 25),
            Propriedade(12, 1), Propriedade(28, 10), Propriedade(900, 600), Propriedade(10, 9),
            Propriedade(68, 47), Propriedade(8, 3), Propriedade(5, 1), Propriedade(190, 100)
        ]
        self.__tabuleiro = Tabuleiro(self.__propriedades)
        self.__dado = Dado()
        self.__jogadores = [
            Impulsivo(self.__tabuleiro), Exigente(self.__tabuleiro),
            Cauteloso(self.__tabuleiro), Aleatorio(self.__tabuleiro)
        ]
        self.__tabuleiro.adicionar_jogadores(self.__jogadores)
    
    def montar_tabuleiro(self) -> Tabuleiro:
        return self.__tabuleiro

    def retorna_jogadores(self) -> list:
        return self.__jogadores

    def retorna_dado(self) -> Dado:
        return self.__dado
