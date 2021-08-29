from banco_imobiliario.config import Configuracao
from banco_imobiliario.models import Tabuleiro, Dado, Impulsivo, Cauteloso, Exigente, Aleatorio
from unittest import TestCase
import unittest


class TestConfiguracao(TestCase):

    def test_configuracao_deve_retornar_tabuleiro(self):
        configuracao = Configuracao()
        self.assertIsInstance(
            configuracao.montar_tabuleiro(),
            Tabuleiro,
            'montar_tabuleiro não retorna um Tabuleiro'
        )

    def test_tabuleiro_deve_ter_20_casas(self):
        configuracao = Configuracao()
        tabuleiro = configuracao.montar_tabuleiro()
        self.assertEqual(tabuleiro.quantidade_de_casas(), 20)

    def test_configuracao_deve_retornar_dado(self):
        configuracao = Configuracao()
        self.assertIsInstance(
            configuracao.retorna_dado(),
            Dado,
            'retornar_dado não retorna um Dado'
        )

    def test_configuracao_deve_retornar_lista_jogadores(self):
        configuracao = Configuracao()
        tabuleiro = configuracao.montar_tabuleiro()
        jogadores_esperado = [
            Impulsivo(tabuleiro), Exigente(tabuleiro),
            Cauteloso(tabuleiro), Aleatorio(tabuleiro)
        ]

        jogadores = configuracao.retorna_jogadores()

        self.assertListEqual(
            list(map(vars, jogadores_esperado)),
            list(map(vars, jogadores))
        )


if __name__ == "__main__":
    unittest.main()
