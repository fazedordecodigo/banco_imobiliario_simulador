from models import Propriedade, Tabuleiro


class Configuracao:
    def __init__(self) -> None:
        self._propriedades = [
            Propriedade(100, 50), Propriedade(80, 20), Propriedade(10, 5), Propriedade(200, 100),
            Propriedade(95, 40), Propriedade(120, 90), Propriedade(15, 2), Propriedade(35, 6),
            Propriedade(160, 100), Propriedade(500, 350), Propriedade(70, 30), Propriedade(55, 25),
            Propriedade(12, 1), Propriedade(28, 10), Propriedade(900, 600), Propriedade(10, 9),
            Propriedade(68, 47), Propriedade(8, 3), Propriedade(5, 1), Propriedade(190, 100)
        ]
    
    def montar_tabuleiro(self):
        return Tabuleiro(self._propriedades)
