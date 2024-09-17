class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return f"Torre {self.nome}, Endereço: {self.endereco}"
