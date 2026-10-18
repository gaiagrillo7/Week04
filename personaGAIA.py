class Persona:
    #variabile di classe sevono per avere informazioni che siano uguali per tutti gli oggetti della classe
    #numero_di_teste = 1

    def __init__(self, nome, cognome):
        self.__nome = nome          #attributi o variabili d'istanza
        self.__cognome = cognome

    def __str__(self):
        return f"{self.__nome} {self.__cognome}"
