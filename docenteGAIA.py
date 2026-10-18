#per dire che la classe Docente eredita da Persona: devo inserire il nome della classe tra parentesi
from personaGAIA import Persona #dal file prsonaGAIA import la classe Persona

class Docente(Persona):      #DOCENTE è UNA CLASSE FIGLIA DI PERSONA
    def __init__(self, nome, cognome):   #qua NON devo ripetere gli attributi del padre!!!
        super().__init__(nome, cognome)   #cosi costruisco la parte Persona della classe figlia Docente

        self.dipartimento = dipartimento  #ora posso inizializzare gli attributi specifici della
                                          #classe Docente

