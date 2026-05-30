# Validador de Nota Fiscal Eletrônica (NFe)
def validar_nota_fiscal(chave):
    chave = chave.replace(" ", "").replace("-", "")

    # Verificar se a chave tem 44 caracteres e é composta apenas por dígitos
    if len(chave) != 44:
        return False

    # Verificar se a chave é composta apenas por dígitos
    if not chave.isdigit():
        return False

    # Cálculo do dígito verificador
    digitos = chave[:43]

    # Atribuir pesos para cada posição dos dígitos
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

    # Multiplicar cada dígito pelo seu peso correspondente e somar os resultados
    for i in range(43):
        soma += int(digitos[i]) * peso[i]

    # Calcular o dígito verificador
    resto = soma % 11

    if resto < 2:
        dv_calculado = 0
    else:
        dv_calculado = 11 - resto

    # Comparar o dígito verificador calculado com o dígito verificador real (último dígito da chave)
    dv_real = int(chave[43])

    return dv_calculado == dv_real
