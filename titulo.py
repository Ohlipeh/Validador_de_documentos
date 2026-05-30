# Validação de Título de Eleitor para o Brasil
def validar_titulo(titulo):
    titulo = titulo.replace(" ", "").replace("-", "")
    # O título de eleitor deve conter exatamente 12 dígitos
    if len(titulo) != 12:
        return False

    # Todos os caracteres devem ser dígitos
    if not titulo.isdigit():
        return False
    # O título de eleitor é composto por 8 dígitos sequenciais, 2 dígitos do estado e 2 dígitos verificadores
    sequencial = titulo[:8]
    estado = titulo[8:10]
    digito1 = int(titulo[10])
    digito2 = int(titulo[11])

    # Primeiro dígito
    peso1 = [2, 3, 4, 5, 6, 7, 8, 9]
    soma1 = sum(int(sequencial[i]) * peso1[i] for i in range(8))
    resto1 = soma1 % 11
    if resto1 == 10:
        resto1 = 0

    # Segundo dígito
    parte2 = estado + str(resto1)
    peso2 = [7, 8, 9]

    soma2 = sum(int(parte2[i]) * peso2[i] for i in range(3))
    resto2 = soma2 % 11
    if resto2 == 10:
        resto2 = 0

    return resto1 == digito1 and resto2 == digito2
