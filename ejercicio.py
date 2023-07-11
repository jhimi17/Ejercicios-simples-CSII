while a != 3:
    print("ELEGIR LA OPCION" )
    print("1: convertir de sol a dolar")
    print("2: convertir de dolar a soles")
    print("3: salir")
    a = int(input())
    if a== 1:
        m = float(input("ingrese el monto en soles para convertir a dolar"))
        r = m/3.5
        print("El resultado es :"+r+" dolar")


