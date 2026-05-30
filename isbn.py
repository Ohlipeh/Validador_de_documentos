# Validador de ISBN
def validar_isbn(isbn):
    isbn = isbn.replace("-", "").replace(" ", "").upper()

    # Verificar se o ISBN tem 10 ou 13 caracteres
    if len(isbn) == 10:
        return validar_isbn10(isbn)
    elif len(isbn) == 13:
        return validar_isbn13(isbn)
    else:
        return False


# Validação para ISBN-10
def validar_isbn10(isbn):
    if not isbn[:-1].isdigit() or (not isbn[-1].isdigit() and isbn[-1] != "X"):
        return False

    soma = 0

    for i in range(9):
        soma += (i + 1) * int(isbn[i])

    if isbn[-1] == "X":
        soma += 10
    else:
        soma += 10 * int(isbn[-1])

    return soma % 11 == 0


# Validação para ISBN-13
def validar_isbn13(isbn):
    if not isbn.isdigit():
        return False

    soma = 0
    # O dígito verificador é calculado usando os primeiros 12 dígitos do ISBN-13
    for i in range(12):
        if i % 2 == 0:
            soma += int(isbn[i])
        else:
            soma += 3 * int(isbn[i])

    digito_verificador = (10 - (soma % 10)) % 10

    return digito_verificador == int(isbn[-1])
