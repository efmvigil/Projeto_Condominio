from Torre import Torre
from Apartamento import Apartamento
from Condominio import Condominio

def menu():
    condominio = Condominio()

    while True:
        print("\nMenu:")
        print("1. Cadastrar apartamento")
        print("2. Liberar vaga")
        print("3. Imprimir lista de apartamentos com vaga")
        print("4. Imprimir fila de espera por vaga")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            id = input("ID do apartamento: ")
            numero = input("Número do apartamento: ")
            idTorre = input("ID da torre: ")
            nomeTorre = input("Nome da torre: ")
            enderecoTorre = input("Endereço da torre: ")
            torre = Torre(idTorre, nomeTorre, enderecoTorre)
            apto = Apartamento(id, numero, 0, torre)
            condominio.cadastrarApartamento(apto)

        elif opcao == '2':
            numeroVaga = int(input("Número da vaga a ser liberada: "))
            condominio.liberarVaga(numeroVaga)

        elif opcao == '3':
            condominio.imprimirApartamentosComVaga()

        elif opcao == '4':
            condominio.imprimirFilaEspera()

        elif opcao == '5':
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
