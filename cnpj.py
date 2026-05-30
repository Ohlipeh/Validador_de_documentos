# Validador de CNPJ
def validar_cnpj(cnpj):
    # removendo.
    cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "").replace(" ", "")

    # xecagem de num.
    if len(cnpj) != 14:
        return False

    # checa se todos carac. sao núm.
    if not cnpj.isdigit():
        return False

    # 1 digito
    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = 0

    # Multiplica
    for i in range(12):
        soma1 += int(cnpj[i]) * peso1[i]
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1

    # 2 digito
    peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = 0

    # Multiplica
    for i in range(13):
        soma2 += int(cnpj[i]) * peso2[i]
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    return int(cnpj[12]) == digito1 and int(cnpj[13]) == digito2
