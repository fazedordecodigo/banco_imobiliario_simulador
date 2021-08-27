class Tabuleiro:
    def __init__(self, propriedades: list) -> None:
        self.casa = 0
        self.propriedades = propriedades
    
    def avancarCasas(self):
        pass


class Dado:
    def __init__(self) -> None:
        self.lado = 0
    
    def sortear(self):
        pass


class Jogador:
    def __init__(self, nome, tipo) -> None:
        self.nome = nome
        self.saldo = 300
        self.propriedades = []
        self.tipo = tipo
    
    def comprar(self):
        pass

    def vende(self):
        pass


class Propriedade:
    def __init__(self, custo_venda, valor_aluguel, posicao) -> None:
        self.custo_venda = custo_venda
        self.valor_aluguel = valor_aluguel
        self.proprietario = None
        self.posicao = posicao
