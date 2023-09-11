def main():
    peso = float(input("Para conocer tu IMC debes ingresar los siguientes datos:\n"
                       "Peso (kg): "))
    estatura = float(input("Estatura (m): "))

    if estatura != 0 and peso != 0:
        calculo = peso / (estatura ** 2)

        if calculo < 18.5:
            print("Usted tiene bajo peso.")
        elif 18.555 <= calculo <= 24.999:
            print("Usted se encuentra en estado normal.")
        elif 25.000 <= calculo <= 29.999:
            print("Usted tiene sobrepeso, cuídese.")
        elif calculo >= 30.000:
            print("Alerta, actualmente tiene obesidad.")
    else:
        print("Los datos ingresados no son válidos.")

if __name__ == "__main__":
   main()



