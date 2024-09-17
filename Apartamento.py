from Torre import Torre

class Apartamento:
    def __init__(self, id, numero, numeroVaga, torre):
        self.id = id
        self.numero = numero
        self.numeroVaga = numeroVaga
        self.torre = torre

    def __str__(self):
        return f"Apartamento {self.numero}, Vaga: {self.numeroVaga}, Torre: {self.torre.nome}"
