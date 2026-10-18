from empolyeeGAIA import Empolyee

class Manager(Empolyee):
    def __init__(self, name, wage, managedUnit):
#prima istruzione del costruttore di una classe figlia è l'invocazione del costruttore della classe padre
        super().__init__(name, wage)
        self.__managedUnit = managedUnit

#con la OOP posso ridefinire i medoti che non mi oiacciono della classe padre, andando a specificare
#comportamenti specializzati nel figlio
    def __str__(self):
        return f"{super().__str__()} {self.__managedUnit}" #prima chiamo la parte interna da stampare
        #con super, poi aggiungo la parte specifica della classe figlia Manager da stampare

    def increment_wage(self):
        self.wage += 10000   #i metodi ridefiniti nella classi figie con lo stesso noke si dicono
        #in OVERRIDING
