def convert_to_decimal(number: str, base: int):
    ''' Conversão de qualquer base numérica para decimal'''
    
    decimal_number = 0
    hexadecimal_values = {'0': 0, '1': 1, '2': 2, '3': 3,
                            '4': 4, '5': 5, '6': 6, '7': 7,
                            '8': 8, '9': 9, 'A': 10, 'B': 11,
                            'C': 12, 'D': 13, 'E': 14, 'F': 15}

    inverted_number = number[::-1]

    # método de conversão usando os valores posicionais
    for index, value in enumerate(inverted_number): # percorre toda a string que contém o número
        if base == 16: # se a base for 16 o valor a ser multiplicado vai ser procurado no dicionário
            decimal_number += hexadecimal_values[value] * (base ** index)
        else:
            decimal_number += int(value) * (base ** index)

    return decimal_number

print('mudança')
