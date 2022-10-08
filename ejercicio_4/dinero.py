cheque=int(input("digita el valor del cheque: "))
Tbi10k=0
Tbi2k=0
Tmon=0
bi10k=0
bi2k=0
mon1=0
while cheque<0: 
    print("¡ingresaste una cifra negativa!")
    cheque=int(input("digita el valor del cheque: "))
    Tbi10k=0
    Tbi2k=0
    Tmon=0
    bi10k=0
    bi2k=0
    mon1=0
   
while cheque!=0:
   bi10k=cheque//10000
   bi2k=((cheque-(bi10k*10000)))//2000
   mon1=((cheque-(bi10k*10000))-(bi2k*2000))//100
   Tbi10k=Tbi10k+bi10k
   Tbi2k=Tbi2k+bi2k 
   Tmon=Tmon+mon1

   cheque=int(input("digita el valor del cheque: "))

print(cheque)
print("billetes de 10000: " + str(Tbi10k))
print("billetes de 2000: "+str(Tbi2k))
print("monedas de 100: "+str(Tmon))

    

