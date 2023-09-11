caracter = input("Ingrese un carácter: ")

if caracter.isalpha():
    if caracter.isupper():
        print("Es una letra mayúscula.")
    else:
        print("Es una letra minúscula.")
elif caracter.isdigit():
    print("Es un número.")
else:
    print('No es ni una letra n iun  número.'d)