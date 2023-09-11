def main():
    a = (float(input("Ingrese el dividendo: ")))
    b =float(input("Ingrese el divisor: "))
    residuo = 0
    cociente = 0

    if b != 0:
        residuo = a % b
        cociente = a // b

        if residuo == 0:
            print("La división es exacta.")
            print(f"Cociente: {cociente}")
            print(f"Residuo: {residuo}")
        else:
            print("La división no es exacta.")
            print(f"Cociente: {cociente}")
            print(f"Residuo: {residuo}")
    else:
        print("La división es indeterminada")

if __name__ == "__main__":
    main()
