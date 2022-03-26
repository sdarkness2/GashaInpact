from Classes.Gacha import Gacha

class Conta():
    __Gacha = Gacha()
    __personagens: list[str] = []
    __personagemDaHora: str
    __tiros: int = 0
    __personagemQuatroPit: int = 0

    #metodo que adiciona os personagens a conta
    def Tiro(self):
        if self.__tiros >= 89:
            self.__personagemDaHora = self.__Gacha.GachaCincoDefinitivo()
        elif self.__personagemQuatroPit == 9 and self.__tiros < 88:
            self.__personagemDaHora = self.__Gacha.GachaDecimoTiro()
        else:
            self.__personagemDaHora = self.__Gacha.GachaPersonagem()
        #teste para ver os tiros
        #print('cinco: ', self.__tiros)
        #print('quatro: ', self.__personagemQuatroPit)
        self.__personagens.append(self.__personagemDaHora)
        self.GerenciarTiro(self.__personagemDaHora)

    #gerencia numero de tiros que você tem
    def GerenciarTiro(self, personagem:str):
        personagemDividido = personagem.split('-')
        if int(personagemDividido[2]) == 5:
            self.__tiros = 0
        elif int(personagemDividido[2]) == 4:
            self.__personagemQuatroPit = 0
        else:
            self.__personagemQuatroPit += 1
            self.__tiros += 1

    #linhas comentadas eram para teste de qualidade para vir sempre 4 estrelas em 10 tiros
    #Ver tiros, e personagens na conta
    def VerConta(self):
        print('Quantidade de tiros: ', str(self.__tiros))
        print('Quantidade de tiros4: ', str(self.__personagemQuatroPit))
        print('Personagens na conta:')
        #quantidadeTresSeguidos = 0
        for personagem in self.__personagens:
            personagemDividido = personagem.split('-')
            print('Nome: {} Elemento: {} Estrelas: {}' .format(personagemDividido[0], personagemDividido[1],
                                                               personagemDividido[2]))
            #if personagemDividido[2] == '3':
            #    quantidadeTresSeguidos += 1
            #    if quantidadeTresSeguidos == 11:
            #        print('erro')
            #        break;
            #else:
            #    quantidadeTresSeguidos = 0