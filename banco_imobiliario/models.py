from abc import abstractmethod
from enum import Enum
import random


class Vencedor:
    def __init__(self, rodada, jogador) -> None:
        self._rodada = rodada
        self._jogador = jogador


class Resultado:
    def __init__(self) -> None:
        self._vencedores = []

    def adicionar_vencedor(self, vencedor: Vencedor):
        self._vencedores.append(vencedor)


class Propriedade:
    def __init__(self, custo_venda, valor_aluguel) -> None:
        self._custo_venda = custo_venda
        self._valor_aluguel = valor_aluguel
        self._proprietario = None

    def disponivel(self) -> bool:
        if self._proprietario is None:
            return True
        return False

    def retornar_valor_aluguel(self) -> int:
        return self._valor_aluguel

    def retornar_custo_venda(self) -> int:
        return self._custo_venda

    def retornar_proprietario(self) -> object:
        return self._proprietario

    def definir_novo_proprietario(self, proprietario) -> bool:
        if self.disponivel:
            self._proprietario = proprietario
            return True
        return False

    def definir_disponivel_mercado(self):
        self._proprietario = None


class Tabuleiro:
    def __init__(self, propriedades: list) -> None:
        self._propriedades = propriedades
        self._jogadores = []

    def quantidade_de_casas(self) -> int:
        return len(self._propriedades)

    def retornar_propriedade(self, casa: int) -> Propriedade:
        return self._propriedades[casa - 1]

    def retornar_todas_propriedades(self) -> list:
        return self._propriedades

    def adicionar_jogadores(self, jogadores: list):
        self._jogadores = jogadores

    def retorna_qtd_jogadores(self) -> int:
        em_jogo = 0
        for jogador in self._jogadores:
            if jogador.retorna_em_jogo():
                em_jogo += 1

        return em_jogo

    def retornar_vencedor(self) -> object:
        for jogador in self._jogadores:
            if jogador.retorna_em_jogo():
                return jogador


class Dado:
    def __init__(self) -> None:
        self._lado = 0

    def sortear(self) -> int:
        self._lado = random.randint(1, 6)
        return self._lado


class Jogador:
    def __init__(self, tabuleiro: Tabuleiro, tipo: Enum) -> None:
        self._tabuleiro = tabuleiro
        self._propriedades = []
        self._casa = 0
        self._saldo = 300
        self._tipo = tipo
        self._em_jogo = True

    @abstractmethod
    def analisar(self, propriedade: Propriedade):
        pass

    def avancar_casas(self, dado: int) -> int:
        _resultado = self._casa + dado

        if _resultado > self._tabuleiro.quantidade_de_casas():
            self._casa = _resultado - self._tabuleiro.quantidade_de_casas()
            self.adciona_saldo(100)
        else:
            self._casa = _resultado
        return self._casa

    def retorna_em_jogo(self):
        return self._em_jogo


    def desclassificar(self) -> bool:
        if self._saldo < 0:
            self._em_jogo = False
            return True
        return False
    
    def retornar_saldo(self) -> int:
        return self._saldo

    def adciona_saldo(self, valor: int):
        self._saldo += valor

    def adicionar_propriedade(self, propriedade: Propriedade):
        self._propriedades.append(propriedade)

    def _comprar(self, propriedade: Propriedade):
        if self._saldo >= propriedade.retornar_custo_venda():
            self._saldo -= propriedade.retornar_custo_venda()
            self.adicionar_propriedade(propriedade)
            propriedade.definir_novo_proprietario(self)
    
    def _pagar(self, propriedade: Propriedade):
        self._saldo -= propriedade.retornar_valor_aluguel()
        proprietario = propriedade.retornar_proprietario()
        proprietario._receber(propriedade.retornar_valor_aluguel())
    
    def _receber(self, valor: int):
        self._saldo += valor

    def devolver_propriedades(self):
        propriedades = list(filter(lambda x : x in self._propriedades, self._tabuleiro.retornar_todas_propriedades()))

        for propriedade in propriedades:
            propriedade.definir_disponivel_mercado()

        self._propriedades = []
    
    def __str__(self):
        return f'Jogador( Tipo: {self._tipo.name}, Saldo: {self._saldo}, Em fogo? {self._em_jogo} )'
        

class Impulsivo(Jogador):
    def __init__(self, tabuleiro) -> None:
        super().__init__(tabuleiro, ETipoJogador.Impulsivo)
    
    def analisar(self, propriedade: Propriedade):
        if propriedade.disponivel():
            self._comprar(propriedade)
        else:
            self._pagar(propriedade)

        if self.desclassificar():
            self.devolver_propriedades()



class Exigente(Jogador):
    def __init__(self, tabuleiro) -> None:
        super().__init__(tabuleiro, ETipoJogador.Exigente)

    def analisar(self, propriedade: Propriedade):
        if propriedade.disponivel():
            if propriedade.retornar_valor_aluguel() > 50:
                self._comprar(propriedade)
        else:
            self._pagar(propriedade)

        if self.desclassificar():
            self.devolver_propriedades()


class Cauteloso(Jogador):
    def __init__(self, tabuleiro) -> None:
        super().__init__(tabuleiro, ETipoJogador.Cauteloso)

    def analisar(self, propriedade: Propriedade):
        if propriedade.disponivel():
            if self.retornar_saldo() - propriedade.retornar_custo_venda() >= 80:
                self._comprar(propriedade)
        else:
            self._pagar(propriedade)

        if self.desclassificar():
            self.devolver_propriedades()


class Aleatorio(Jogador):
    def __init__(self, tabuleiro) -> None:
        super().__init__(tabuleiro, ETipoJogador.Aleatorio)

    def analisar(self, propriedade: Propriedade):
        if propriedade.disponivel():
            if random.randint(1, 2) == 1:
                self._comprar(propriedade)
        else:
            self._pagar(propriedade)

        if self.desclassificar():
            self.devolver_propriedades()


class ETipoJogador(Enum):
    Impulsivo = 1,
    Exigente = 2,
    Cauteloso = 3,
    Aleatorio = 4
