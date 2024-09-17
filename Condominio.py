from Lista import ListaEncadeada
from Apartamento import Apartamento

class Condominio:
    def __init__(self):
        self.vagasDisponiveis = 10
        self.apartamentosComVaga = ListaEncadeada()
        self.filaEspera = []
        self.proximaVaga = 1

    def cadastrarApartamento(self, apartamento):
        atual = self.apartamentosComVaga.cabeca
        while atual != None:
            if atual.apartamento.id == apartamento.id or atual.apartamento.numero == apartamento.numero:
                print("Este apartamento já foi cadastrado!")
                return
            atual = atual.proximo

        for apto in self.filaEspera:
            if apto.id == apartamento.id or apto.numero == apartamento.numero:
                print("Este apartamento já foi cadastrado!")
                return

        if self.vagasDisponiveis > 0:
            apartamento.numeroVaga = self.proximaVaga
            self.apartamentosComVaga.adicionarOrdenado(apartamento)
            self.vagasDisponiveis -= 1
            self.proximaVaga += 1
        else:
            self.filaEspera.append(apartamento)
            print(f"Apartamento {apartamento.numero} foi adicionado à fila de espera.")

    def liberarVaga(self, numeroVaga):
        apto = self.apartamentosComVaga.removerPorVaga(numeroVaga)
        if apto != None:
            apto.numeroVaga = 0  
            self.filaEspera.append(apto)
            self.vagasDisponiveis += 1
        if self.filaEspera:
            aptoFila = self.filaEspera.pop(0)
            aptoFila.numeroVaga = numeroVaga
            self.apartamentosComVaga.adicionarOrdenado(aptoFila)
            self.vagasDisponiveis -= 1

    def imprimirApartamentosComVaga(self):
        print("Apartamentos com vaga:")
        self.apartamentosComVaga.imprimir()


    def imprimirFilaEspera(self):
        print("Lista de espera por vaga:")
        for apto in self.filaEspera:
            print(apto)
