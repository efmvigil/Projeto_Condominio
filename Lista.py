from No import No

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionarOrdenado(self, apartamento):
        novoNo = No(apartamento)
        if self.cabeca == None or self.cabeca.apartamento.numeroVaga > apartamento.numeroVaga:
            novoNo.proximo = self.cabeca
            self.cabeca = novoNo
        else:
            atual = self.cabeca
            while atual.proximo != None and atual.proximo.apartamento.numeroVaga < apartamento.numeroVaga:
                atual = atual.proximo
            novoNo.proximo = atual.proximo
            atual.proximo = novoNo

    def removerPorVaga(self, numeroVaga):
        atual = self.cabeca
        anterior = None
        while atual != None and atual.apartamento.numeroVaga != numeroVaga:
            anterior = atual
            atual = atual.proximo
        if atual == None:
            return None
        if anterior == None:
            self.cabeca = atual.proximo
        else:
            anterior.proximo = atual.proximo
        return atual.apartamento

    def imprimir(self):
        atual = self.cabeca
        while atual != None:
            print(atual.apartamento)
            atual = atual.proximo
