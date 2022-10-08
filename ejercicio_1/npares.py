n=int(input("\n Digite un nuemro entero positivo: "))
origin=n
suma=0
digito=0

while n!=0:
    digito=n%10
    n=(n//10)
    suma=suma+digito
    


print("la suma de los digitos del numero: "+str(origin) + " Es:" + str(suma))
