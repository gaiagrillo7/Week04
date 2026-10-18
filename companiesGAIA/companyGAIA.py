from empolyeeGAIA import Empolyee
from managerGAIA import Manager

e1 = Empolyee("Mr: Bean", 15000)

print(e1)

m = Manager("B.Boss", 40000, "HR")

print(m)  #se faccio print m senza aver definito un metodo di stampa della classe figlia manager mi stampa come
#stampa la classe padre, per questo in managerGAIA.py ridefinisco def __str__

print("----Incremento della paga----")
e1.increment_wage()
print(e1)

m.increment_wage()
print(m)

print("**** Struttura dati ****")
users = []
users.append(e1)
users.append(m)
#DUCK TTPING  cioè la stringa abcdefg e l'intero 35 vengono stampati lo stesso, perche sono degli oggetti
users.append("abcdefg")    #che hanno gli stessi metordi degli altri oggetti
users.append(35)

for user in users:
    print(f"{str(user)} {type(user)}")   #type ci stampa le info relative all'oggetto della lista
             #str lo metto perche 'abcdefg' è una sringa che altrikenti non verebbe stampata

if isinstance(e1, Empolyee) is True:   #uso isnstance per verificare l'appartrnza di un oggetto (e1)
    print("e1 è un Employee")          #ad una classe (Employee)
else:
    print("e1 non è un Employee")