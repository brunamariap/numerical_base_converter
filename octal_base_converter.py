def octal_to_binary(numero: str):
    ''' Conversões de octal para binário'''
    num_octal = ''
    valores_binarios = {'0': '000', '1': '001', '2': '010', '3': '011',
                        '4': '100', '5': '101', '6': '110', '7': '111'}

    for digito in numero:
        num_octal += valores_binarios[digito]
    
    if num_octal[0] and num_octal[1] == '0': # se tiver 0 nas 2 primeiras posições da string eles vão ser "cortados" para que não fiquem 0s a mais no número
        num_octal = num_octal[2:] # pega o caractere da segunda posiçã até o último
    elif num_octal[0]: # se tiver 0 apenas na primeira posição da string ele vai ser "cortado"
        num_octal = num_octal[1:]

    return num_octal