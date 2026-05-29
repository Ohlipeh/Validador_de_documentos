def validador_cnpj(cnpj):
    #removendo.
    cnpj = cnpj.replace("", "").replace(" ", "")

    #xecagem de num.
    if len(cnpj) != 14:
        return "CNPJ inválido, Tem que ter 14 digítos."
    
    # checa se todos carac. sao núm.
    if not titulo.isdigit():
        return "CNPJ inaválido: deve ter apenas números."
    
    digitos 

