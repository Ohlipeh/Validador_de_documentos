# Validador de Documentos
# Autor: André Felipe
from rg import validar_rg
from cnpj import validar_cnpj
from titulo import validar_titulo
from nota_fiscal import validar_nota_fiscal
from isbn import validar_isbn

# Menu de opções
while True:
    print("\n=== VALIDADOR DE DOCUMENTOS ===")
    print("1 - Validar RG")
    print("2 - Validar CNPJ")
    print("3 - Validar Título de Eleitor")
    print("4 - Validar Nota Fiscal")
    print("5 - Validar ISBN")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # Processar a opção escolhida
    if opcao == "1":
        rg = input("Digite o RG: ")

        if validar_rg(rg):
            print("RG válido")
        else:
            print("RG inválido")

    elif opcao == "2":
        cnpj = input("Digite o CNPJ: ")

        if validar_cnpj(cnpj):
            print("CNPJ válido")
        else:
            print("CNPJ inválido")

    elif opcao == "3":
        titulo = input("Digite o Título: ")

        if validar_titulo(titulo):
            print("Título válido")
        else:
            print("Título inválido")

    elif opcao == "4":
        nota = input("Digite a chave da Nota Fiscal: ")

        if validar_nota_fiscal(nota):
            print("Nota Fiscal válida")
        else:
            print("Nota Fiscal inválida")

    elif opcao == "5":
        isbn = input("Digite o ISBN: ")

        if validar_isbn(isbn):
            print("ISBN válido")
        else:
            print("ISBN inválido")

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")
