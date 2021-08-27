from estrutura import Propriedade, Tabuleiro
from abc import abstractmethod
from enum import Enum
import random


class Jogador:
    def __init__(self, tabuleiro: Tabuleiro, tipo: Enum) -> None:
        self._tabuleiro = tabuleiro
        self._casa = 0
        self._saldo = 300
        self._tipo = tipo

    def avancar_casas(self, dado: int) -> int:
        _resultado = self._casa + dado

        if _resultado > self._tabuleiro.quantidade_de_casas():
            self._casa = _resultado - self._tabuleiro.quantidade_de_casas()
        else:
            self._casa = _resultado
        return self._casa
    
    def retornar_saldo(self) -> int:
        return self._saldo

    @abstractmethod
    def analisar(self, propriedade: Propriedade):
        pass

    def _comprar(self, propriedade: Propriedade):
        self._saldo -= propriedade.retornar_custo_venda()
        propriedade.definir_novo_proprietario(self)
    
    def _pagar(self, propriedade: Propriedade):
        self._saldo -= propriedade.retornar_valor_aluguel()
        proprietario = propriedade.retornar_proprietario()
        proprietario.receber(propriedade.retornar_valor_aluguel())
    
    def receber(self, valor: int):
        self._saldo += valor
    
    def __str__(self):
        return f'Jogador( Tipo: {self._tipo.name}, Saldo: {self._saldo} )'
        

class Impulsivo(Jogador):
    def __init__(self, tabuleiro) -> None:
        super().__init__(tabuleiro, ETipoJogador.Impulsivo)
    
    def analisar(self, propriedade: Propriedade):
        if propriedade.disponivel():
            self._comprar(propriedade)
        else:
            self._pagar(propriedade)


class Exigente(Jogador):
    def __init__(self, tabuleiro) -> None:
        super().__init__(tabuleiro, ETipoJogador.Exigente)

    def analisar(self, propriedade: Propriedade):
        if propriedade.disponivel():
            if propriedade.retornar_valor_aluguel() > 50:
                self._comprar(propriedade)
        else:
            self._pagar(propriedade)


class Cauteloso(Jogador):
    def __init__(self, tabuleiro) -> None:
        super().__init__(tabuleiro, ETipoJogador.Cauteloso)

    def analisar(self, propriedade: Propriedade):
        if propriedade.disponivel():
            if self.retornar_saldo() - propriedade.retornar_custo_venda() >= 80:
                self._comprar(propriedade)
        else:
            self._pagar(propriedade)


class Aleatorio(Jogador):
    def __init__(self, tabuleiro) -> None:
        super().__init__(tabuleiro, ETipoJogador.Aleatorio)

    def analisar(self, propriedade: Propriedade):
        if propriedade.disponivel():
            if random.randint(1, 2) == 1:
                self._comprar(propriedade)
        else:
            self._pagar(propriedade)


class ETipoJogador(Enum):
    Impulsivo = 1,
    Exigente = 2,
    Cauteloso = 3,
    Aleatorio = 4
