from banco_imobiliario.config import Configuracao
from banco_imobiliario.models import Tabuleiro, Dado, Impulsivo, Cauteloso, Exigente, Aleatorio
from unittest import TestCase
import unittest


class TestConfiguracao(TestCase):

    def setUp(self) -> None:
        self.configuracao = Configuracao()
        self.tabuleiro = self.configuracao.montar_tabuleiro()

    def test_configuracao_deve_retornar_tabuleiro(self):

        self.assertIsInstance(
            self.tabuleiro,
            Tabuleiro,
            'montar_tabuleiro não retorna um Tabuleiro'
        )

    def test_tabuleiro_deve_ter_20_casas(self):
        self.assertEqual(self.tabuleiro.quantidade_de_casas(), 20)

    def test_configuracao_deve_retornar_dado(self):
        self.assertIsInstance(
            self.configuracao.retorna_dado(),
            Dado,
            'retornar_dado não retorna um Dado'
        )

    def test_configuracao_deve_retornar_lista_jogadores(self):
        jogadores_esperado = [
            Impulsivo(self.tabuleiro), Exigente(self.tabuleiro),
            Cauteloso(self.tabuleiro), Aleatorio(self.tabuleiro)
        ]
        jogadores = self.configuracao.retorna_jogadores()

        self.assertListEqual(
            list(map(vars, jogadores_esperado)),
            list(map(vars, jogadores))
        )


if __name__ == "__main__":
    unittest.main()
