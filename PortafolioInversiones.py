def menu():

    print("Portafolios de Inversión")
    print("1. Portafolio de  alto Riesgo")
    print("2. Bitcoin")
    print("3. Ethereum")
    print("4. Tasa de Interes ")
    print("5. Compra  de activos")
    print("6. Salir")
    op = input("Escriba la opción:")

    op = int(op)
    if op == 1:
        PorafolioRiesgo()
    elif op == 2:
        Bitcoin()
    elif op == 3:
        Ethereum()
    elif op == 4:
        TasaInteres()
    elif op == 5:
        Compra()
    else:
        exit()

def PortafolioAltoR():
    print("")
    print('Union.')
    Potrafolio_A = [AppleInc]
    Portafolio_B = [AppleCo]
    Conjunto_A = set(Price)
    Conjunto_B = set(Price)
    Resultado = Conjunto_B.union(Conjunto_A)
    print("Resultado:", Resultado)

    print("")

    menu()



def interseccion():

    print("")

    print('Intersección.')

    Conjunto_A = [1, 2, 3, 4, 5, 6]

    Conjunto_B = [2, 2, 5, 3, 7, 9]

    Conjunto_A = set(Conjunto_A)

    Conjunto_B = set(Conjunto_B)

    Resultado = Conjunto_B.intersection(Conjunto_A)

    print("Resultado:", Resultado)

    print("")

    menu()



def complemento():

    print("")

    print('Complemento.')

    Conjunto_A = [1, 2, 3, 4, 5, 6]

    Conjunto_B = [2, 2, 5, 3, 7, 9]

    Conjunto_A = set(Conjunto_A)

    Conjunto_B = set(Conjunto_B)

    Resultado = Conjunto_B.difference(Conjunto_A)

    print("Resultado:", Resultado)

    print("")

    menu()



def diferencia():

    print("")

    print('Diferencia.')

    Conjunto_A = [1, 2, 3, 4, 5, 6]

    Conjunto_B = [2, 2, 5, 3, 7, 9]

    Conjunto_A = set(Conjunto_A)

    Conjunto_B = set(Conjunto_B)

    Resultado = Conjunto_B.difference(Conjunto_A)

    print("Resultado:", Resultado)

    print("")

    menu()



def simetrica():

    print("")

    print('Diferencia Simetrica.')

    Conjunto_A = [1, 2, 3, 4, 5, 6]

    Conjunto_B = [2, 2, 5, 3, 7, 9]

    Conjunto_A = set(Conjunto_A)

    Conjunto_B = set(Conjunto_B)

    Resultado = Conjunto_B.symmetric_difference(Conjunto_A)

    print("Resultado:", Resultado)

    print("")

    menu()



menu()
