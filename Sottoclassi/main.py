from Impiegato import Impiegato
from Tecnico import Tecnico
from Amministrativo import Amministrativo
import random

numI = random.randint(1, 10)
numT = random.randint(1, 10)
numA = random.randint(1, 10)

print('numI=', numI, ', numT=', numT, ', numA=', numA)

listImpiegati = list()
listTecnici = list()
listAmministrativi = list()

for i in range(numI):
    nome = "nome" + str(i)
    cognome = "cognome" + str(i)
    listImpiegati.append(Impiegato(nome, cognome))

for j in range(numT):
    nome = "nome" + str(j)
    cognome = "cognome" + str(j)
    listTecnici.append(Tecnico(nome, cognome))

for k in range(numA):
    nome = "nome" + str(k)
    cognome = "cognome" + str(k)
    listAmministrativi.append(Amministrativo(nome, cognome))

print('num Impiegati=', Impiegato.numImpiegati, 'num Tecnici=', Tecnico.numImpiegati, ', num Amministrativi=', Amministrativo.numImpiegati)
print('sum Tecnici Amministrativi')
