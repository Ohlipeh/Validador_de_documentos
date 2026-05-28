# Definição NF-e
def validar_nota_fiscal(chave):
    # removendo.
    chave = chave.replace(" ", " ").replace("-", "")

    # Checa se tem 44 digitos.
    if len(chave) != 44:
        return "Nota fiscal Inválida, Tem que ter 44 digitos."
    # Verifica se todos são num.
    if not chave.isdigit():
        return "Nota fiscal inválida,Tem que ter apenas números."

    # separando.
    digitos = chave[:43]

    # calculo.
    peso = [
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        2,
        3,
        4,
    ]
    soma = 0

    # multiplica.
    for i in range(43):
        soma += int(digitos[i]) * peso[i]

    # resto divisao.
    resto = soma % 11

    # aplicação da regra.
    if resto < 2:
        dv_calculado = 0
    else:
        dv_calculado = 11 - resto

    dv_real = int(chave[43])  # último dígito dacgave

    if dv_calculado == dv_real:
        return "Nota Fiscal VÁLIDA!"
    else:
        return "Nota Fiscal INVÁLIDA!"


# teste
chave = input("Digite a chave da Nota Fiscal (44 dígitos): ")
print(validar_nota_fiscal(chave))
