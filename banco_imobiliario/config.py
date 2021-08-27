from models import Tabuleiro, Propriedade


class Configuracao:
    def __init__(self) -> None:
        self.__propriedades= [
            Propriedade(100, 50, 1), Propriedade(80, 20, 2), Propriedade(10, 5, 3), Propriedade(200, 100, 4),
            Propriedade(95, 40, 5), Propriedade(120, 90, 6), Propriedade(15, 2, 7), Propriedade(35, 6, 8),
            Propriedade(160, 100, 9), Propriedade(500, 350, 10), Propriedade(70, 30, 11), Propriedade(55, 25, 12),
            Propriedade(12, 1, 13), Propriedade(28, 10, 14), Propriedade(900, 600, 15), Propriedade(10, 9, 16),
            Propriedade(68, 47, 17), Propriedade(8, 3, 18), Propriedade(5, 1, 19), Propriedade(190, 100, 20)
        ]
    
    def montarTabuleiro(self):
        return Tabuleiro(self.__propriedades)