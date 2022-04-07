from random import choice
import mysql.connector

class Personagem():
    ## V1
    ##__personagensCincoEstrelas: list = ['Diluc-Pyro-5', 'Mona-Hydro-5', 'Xiao-Anemo-5']
    ##__personagensQuatroEstrelas: list = ['Albedo-Pyro-4', 'Barbara-Hydro-4', 'Sucrose-Anemo-4']
    __mydb = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='gashaimpactdb')

    def GetPersonagensCincoEstrelas(self):
        query = "SELECT * FROM PERSONAGEM WHERE ESTRELA = 5 ORDER BY RAND() LIMIT 1"
        mycursor = self.__mydb.cursor()
        mycursor.execute(query)
        removerdalista = mycursor.fetchall()
        return removerdalista[0]

    def GetPersonagensQuatroEstrelas(self):
        query = "SELECT * FROM PERSONAGEM WHERE ESTRELA = 4 ORDER BY RAND() LIMIT 1"
        mycursor = self.__mydb.cursor()
        mycursor.execute(query)
        removerdalista = mycursor.fetchall()
        return removerdalista[0]