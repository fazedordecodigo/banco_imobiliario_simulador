from banco_imobiliario.models import Tabuleiro
from config import Configuracao

def handler():
    config = Configuracao()
    tabuleiro = config.montarTabuleiro()
    
    tabuleiro.avancarCasas()

    

if __name__=='__main__':
    pass