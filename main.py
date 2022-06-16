from hexadecimal_base_converter import hexadecimal_to_binary
from converter_to_decimal_base import convert_to_decimal
from decimal_base_converter import decimal_converter
from validations import validate_number, new_number
from octal_base_converter import octal_to_binary
import os

option = 0

while True:
    try:
        if int(option) < 1 or int(option) > 12:
            os.system("cls")
            print("====================================================")
            print("Conversion options:\n"
            "1. Binary to decimal\n"
            "2. Octal to decimal\n"
            "3. Hexadecimal to decimal\n"
            "4. Decimal to binary\n"
            "5. Octal to binary\n"
            "6. Hexadecimal to binary\n"
            "7. Decimal to octal\n"
            "8. Binary to octal\n" 
            "9. Hexadecimal to octal\n" 
            "10. Decimal to hexadecimal\n" 
            "11. Binary to hexadecimal\n" 
            "12. Octal to hexadecimal") 
            print("====================================================")
            option = input("Select: ")
        else:
            break
    except:
        break

number = input("Digite o número: ").upper()

# conversões para decimal
if option == '1':
    while validate_number(number, 2) == False:
        number = new_number(2)
    print(f"\nThe number {number} in binary corresponds to the number", convert_to_decimal(number, 2), "in decimal")

elif option == '2':
    while validate_number(number, 8) == False:
        number = new_number(8)
    print(f"\nThe number {number} in octal corresponds to the number", convert_to_decimal(number, 8), "in decimal")

elif option == '3':
    while validate_number(number, 16) == False:
        number = new_number(16)
    print(f"\nThe number {number} in hexadecimal corresponds to the number", convert_to_decimal(number, 16), "in decimal")

# conversões para binário
elif option == '4':
    while validate_number(number, 10) == False:
        number = new_number(10)
    print(f"\nThe number {number} in decimal corresponds to the number", decimal_converter(int(number), 2), "in binary")

elif option == '5':
    while validate_number(number, 8) == False:
        number = new_number(8)
    print(f"\nO número {number} in octal corresponds to the number", octal_to_binary(number), "in binary")

elif option == '6':
    while validate_number(number, 16) == False:
        number = new_number(16)
    print(f"\nO número {number} in hexadecimal corresponds to the number", hexadecimal_to_binary(number), "in binary")

elif option == '7':
    while validate_number(number, 10) == False:
        number = new_number(10)
    print(f"\nO número {number} in decimal corresponds to the number", decimal_converter(int(number), 8), "in octal")

elif option == '10':
    while validate_number(number, 10) == False:
        number = new_number(10)
    print(f"\nO número {number} in decimal corresponds to the number", decimal_converter(int(number), 16), "in hexadecimal")