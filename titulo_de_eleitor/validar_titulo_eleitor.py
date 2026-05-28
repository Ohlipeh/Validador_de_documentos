# Definição, limpar o número.
def validar_titulo(titulo):
    # remove espaço e traço.
    titulo = titulo.replace(" ", " ").replace("-", " ")

    # checa se tem 12 digitos.
    if len(titulo) != 12:
        return "Título inválido: Tem que ter 12 digitos."
    # checa se todos carac. sao núm.
    if not titulo.isdigit():
        return "Título inaválido: deve ter apenas números."

    # separando partes.
    sequencial = titulo[:8]  # primeiros 8 digitos
    estado = titulo[8:10]  # 2 digit
    digito1 = int(titulo[10])  # 1 verificador
    digito2 = int(titulo[11])  # 2 verificador

    # peso para 1 digito.
    peso1 = [2, 3, 4, 5, 6, 7, 8, 9]
    soma1 = 0

    # multiplica.
    for i in range(8):
        soma1 += int(sequencial[i]) * peso1[i]

    # resto divisao.
    resto1 = soma1 % 11

    peso2 = [7, 8, 9]
    soma2 = 0
    parte2 = estado + str(resto1)  # junta 1 digito calculado.

    for i in range(3):
        soma2 += int(parte2[i]) * peso2[i]

    resto2 = soma2 % 11

    # Compara od digitos
    if resto1 == digito1 and resto2 == digito2:
        return "Título VÁLIDO!"
    else:
        return "Título INVÁLIDO!"


numero = input("Digite o Título de Eleitor: ")
print(validar_titulo(numero))
