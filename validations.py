import re

def validate_number(number, base): 
    ''' Função para checar se o número é aceitável de acordo com as condições'''
    if base == 2:
        binary_regex = re.search(r'[^0-1]', number)
        if binary_regex:
            return False
    elif base == 8:
        octal_regex = re.search(r'[^0-7]',number)
        if octal_regex:
            return False
    elif base == 10:
        decimal_regex = re.search(r'[^0-9]', number)
        if decimal_regex:
            return False
    elif base == 16:
        hexadecimal_regex = re.search(r'[^0-9A-F]', number) # checando se na palavra existe algum caractere que está fora desses 2 intervalos de caracteres
        if hexadecimal_regex: # se caso existir algum caractere que não se encaixe no padrão indicado
            return False

def new_number(base): # Pede que o usuário digite um novo número
    print("\nInvalid number!")
    number = input(f"Digite um número de base {base} para converter: ").upper()
    return number