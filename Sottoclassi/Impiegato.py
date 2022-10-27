class Impiegato:
    numImpiegati = 0

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.aggiungi()

    @classmethod
    def aggiungi(cls):
        cls.numImpiegati += 1