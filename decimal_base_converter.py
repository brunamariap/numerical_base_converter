def decimal_converter(number: int, base: int):
    ''' Converte números de qualquer base numérica para decimal '''

    converted_number = ''
    hexadecimal_values = {0: 0, 1: 1, 2: 2, 3: 3,
                          4: 4, 5: 5, 6: 6, 7: 7,
                          8: 8, 9: 9, 10: 'A', 11:'B', 
                          12: 'C', 13: 'D', 14: 'E', 15:'F'}

    while number != 0:
        resto = number % base # resto da divisão do número decimal
        number = number // base # guardando sempre o número do quociente da divisão

        if base == 16: 
            converted_number += str(hexadecimal_values[resto]) # busca o valor no dicionário com os valores haxadecimais
        else:
            converted_number += str(resto)

    return ''.join(reversed(converted_number)) # reverte a ordem da string com o número convertido