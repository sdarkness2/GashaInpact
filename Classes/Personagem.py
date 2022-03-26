from random import choice

class Personagem():
    __personagensCincoEstrelas: list[str] = ['Diluc-Pyro-5', 'Mona-Hydro-5', 'Xiao-Anemo-5']
    __personagensQuatroEstrelas: list[str] = ['Albedo-Pyro-4', 'Barbara-Hydro-4', 'Sucrose-Anemo-4']

    def GetPersonagensCincoEstrelas(self):
        return choice(self.__personagensCincoEstrelas)

    def GetPersonagensQuatroEstrelas(self):
        return choice(self.__personagensQuatroEstrelas)