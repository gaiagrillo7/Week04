from companiesGAIA.managerGAIA import Manager

class MegaManager(Manager):
    def __init__(self, name, wage, managedUnit, megaAttr):
        #prima inizializzo la parte Manager di Emplyee (essendo Manager importata a sua volta da Employee
        super().__init__(name , wage, managedUnit)
        #poi inizializzo la parte specifica
        self.__megaAttr = megaAttr