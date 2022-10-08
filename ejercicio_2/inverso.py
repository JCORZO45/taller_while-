n=int(input("Digite el numero entero positivo: "))
reverso=0

while n>0:
        cifra=n%10
        reverso=reverso*10+cifra
        n=n//10

    


print("su numero invertido es : "+ str(reverso))