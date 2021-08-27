from abc import abstractclassmethod, abstractmethod
from enum import Enum
import random



class Tabuleiro:
    def __init__(self, propriedades: list) -> None:
        self.__propriedades = propriedades
    
    def quantidadeDeCasas(self) -> int:
        return len(self.__propriedades)
    
    def retornarPropriedade(self, casa: int) -> object:
        return self.__propriedades[casa-1]



class Dado:
    def __init__(self) -> None:
        self.__lado = 0
    
    def sortear(self) -> int:
        self.__lado = random.randint(1, 6)

        return self.__lado



class Propriedade:
    def __init__(self, custo_venda, valor_aluguel, posicao) -> None:
        self.__custo_venda = custo_venda
        self.__valor_aluguel = valor_aluguel
        self.__proprietario = None

    def disponivel(self) -> bool:
        if self.__proprietario is None:
            return True

        return False
    
    def retornarValorAluguel(self) -> int:
        return self.__valor_aluguel
    
    def retornarCustoVenda(self) -> int:
        return self.__custo_venda
    
    def retornarProprietario(self) -> object:
        return self.__proprietario

    def definirNovoProprietario(self, proprietario: object) -> bool:
        if self.disponivel:
            self.__proprietario = proprietario
            return True

        return False
        


class Jogador:
    def __init__(self, tipo: Enum = 0) -> None:
        self.__casa = 0
        self.__saldo = 300
        self.__tipo = tipo

    def avancarCasas(self, dado: int, qtd_casas: int) -> int:
        self.__resultado = self.__casa + dado

        if self.__resultado > qtd_casas:
            self.__casa = self.__resultado - qtd_casas
        else:
            self.__casa = self.__resultado

        return self.__casa
    
    def retornarSaldo(self) -> int:
        return self.__saldo

    @abstractmethod
    def analisar(self):
        pass

    def _comprar(self, propriedade: Propriedade):
        self.__saldo -= propriedade.retornarCustoVenda()
        propriedade.definirNovoProprietario(self)
    
    def _pagar(self, propriedade: Propriedade):
        self.__saldo -= propriedade.retornarValorAluguel()
        proprietario = propriedade.retornarProprietario()
        proprietario._receber(propriedade.retornarValorAluguel())
    
    def _receber(self, valor: int):
        self.__saldo += valor
    
    def __str__(self):
        return f'Jogador( Tipo: {self.__tipo.name}, Saldo: {self.__saldo} )'
        


class Impulsivo(Jogador):
    def __init__(self) -> None:
        super().__init__(ETipoJogador.Impulsivo)
    
    def analisar(self, propriedade: Propriedade):
        if propriedade.disponivel():
            self._comprar(propriedade)
        else:
            self._pagar(propriedade)



class Exigente(Jogador):
    def __init__(self) -> None:
        super().__init__(ETipoJogador.Exigente)

    def analisar(self, propriedade: Propriedade):
        if propriedade.disponivel():
            if propriedade.retornarValorAluguel() > 50:
                self._comprar(propriedade)
        else:
            self._pagar(propriedade)



class Cauteloso(Jogador):
    def __init__(self) -> None:
        super().__init__(ETipoJogador.Cauteloso)

    def analisar(self, propriedade: Propriedade):
        if propriedade.disponivel():
            if self.retornarSaldo() - propriedade.retornarCustoVenda() >= 80:
                self._comprar(propriedade)
        else:
            self._pagar(propriedade)



class Aleatorio(Jogador):
    def __init__(self) -> None:
        super().__init__(ETipoJogador.Aleatorio)

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
