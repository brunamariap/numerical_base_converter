def hexadecimal_to_binary(number: str):
    ''' Conversão de hexadecimal para binário '''
    hexadecimal_number = ''
    binary_values = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                     '4': '0100', '5': '0101', '6': '0110', '7': '0111', 
                     '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 
                     'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    for i in number:
        hexadecimal_number += binary_values[i]
    
    # Checa se existem zeros antes do primeiros 1 aparecer
    if hexadecimal_number[0] and hexadecimal_number[1] and hexadecimal_number[2] == '0':
        hexadecimal_number = hexadecimal_number[3:]
    elif hexadecimal_number[0] and hexadecimal_number[1] == '0':
        hexadecimal_number = hexadecimal_number[2:] # pega o caractere da segunda posiçã até o último
    elif hexadecimal_number[0]:
        hexadecimal_number = hexadecimal_number[1:]

    return hexadecimal_number