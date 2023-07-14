#Ingresar un numero del 1 al 10 y dar su valor en romanos

a = [1,2,3,4,5,6,7,8,9,10]
b = ['I', 'II','III','IV','V','VI','VII','VIII','IX','X']

n  = int(input("Ingresa un numero: "))

for i in a:
    if n == i:
        print("El valor en romano es ",b[i-1])