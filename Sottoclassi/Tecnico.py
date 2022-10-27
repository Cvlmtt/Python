from Impiegato import Impiegato

class Tecnico(Impiegato):
    numImpiegati = 0

    def __init__(self, nome, cognome):
        super().__init__(nome, cognome)
        Impiegato.aggiungi()