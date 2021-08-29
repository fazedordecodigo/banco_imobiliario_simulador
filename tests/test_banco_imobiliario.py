import unittest
from unittest import TestCase
from banco_imobiliario.config import Configuracao


class TestBancoImobiliario(TestCase):

    def test_tabuleiro_deve_ter_20_casas(self):
        configuracao = Configuracao()
        tabuleiro = configuracao.montar_tabuleiro()
        self.assertEqual(tabuleiro.quantidade_de_casas(), 20)


if __name__ == "__main__":
    unittest.main()
