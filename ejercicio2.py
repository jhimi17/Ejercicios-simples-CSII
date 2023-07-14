#caclular factorial de un numero

n = int(input("ingresa un numero: "))
r = 1
for i in range(n,1,-1):
   
    r = r*i
print("El resultado del factorial de ",n," es: ",r)