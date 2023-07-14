a = 1
while a != 3:
    print("ELEGIR LA OPCION")
    print("1: convertir de sol a dolar")
    print("2: convertir de dolar a soles")
    print("3: salir")
    a = int(input())

    if a == 3:
        break

    if a == 1:
        m = float(input("ingrese el monto en soles para convertir a dolares: \n"))
        r = m / 3.5
        print("El resultado es :" , r , " dolares")
    else:
        if a == 2:
            m = float(input("ingrese el monto en dolares para convertir a soles\n"))
            r = m * 3.5
            print("El resultado es :" , r , " soles")
        else:
            print("ingresaste una opcion incorrect")
