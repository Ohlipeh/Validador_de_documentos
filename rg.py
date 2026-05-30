# Validação de RG (Registro Geral) para o Brasil
def validar_rg(rg):
    if len(rg) != 9 or not rg.isdigit():
        return False

    soma = sum(int(rg[i]) * (9 - i) for i in range(8))

    resto = soma % 11
    digito = 0 if resto < 2 else 11 - resto

    return digito == int(rg[8])
