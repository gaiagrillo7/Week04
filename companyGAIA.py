from empolyeeGAIA import Empolyee
from managerGAIA import Manager

e1 = Empolyee("Mr: Bean", 15000)

print(e1)

m = Manager("B.Boss", 40000, "HR")

print(m)  #se faccio print m senza aver definito un metodo di stampa della classe figlia manager mi stampa come
#stampa la classe padre, per questo in managerGAIA.py ridefinisco def __str__

print("----Incremwnto della paga----")
e1.increment_wage()
print(e1)

m.increment_wage()
print(m)

print("**** Struttura dati ****")
users = []
users.append(e1)
users.append(m)
#DUCK TTPING  cioè la stringa abcdefg e l'intero 35 vengono stampati lo stesso
users.append("abcdefg")
users.append(35)

for user in users:
    print(str(user))