from Classes.Personagem import Personagem
from random import randint

class Gacha():
    __personagem = Personagem()
    __personagemSelecionado: list

    def GachaPersonagem(self):
        taxa = randint(1, 10000)
        if taxa <= 64:
            self.__personagemSelecionado = self.__personagem.GetPersonagensCincoEstrelas()
        elif taxa > 64 and taxa <= 1264:
            self.__personagemSelecionado = self.__personagem.GetPersonagensQuatroEstrelas()
        else:
            self.__personagemSelecionado = (999, 'flop', 'flop', 3)
        return self.__personagemSelecionado

    def GachaCincoDefinitivo(self):
        return self.__personagem.GetPersonagensCincoEstrelas()

    def GachaDecimoTiro(self):
        taxa = randint(1, 10000)
        if taxa <= 64:
            self.__personagemSelecionado = self.__personagem.GetPersonagensCincoEstrelas()
        else:
            self.__personagemSelecionado = self.__personagem.GetPersonagensQuatroEstrelas()
        return self.__personagemSelecionado