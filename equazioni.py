 #realizza un programma che attraverso le funzioni risolva
#qualsiasi equazione di secondo grado
import math

def calcolo_determinante (a,b,c):
    det=(b*b)-4*a*c
    return det
    
def calcolo_soluzioni(determinante,b,a):
    if det<0:
        print("non ammette soluzioni reali")
    else:
        x1=(-b+ math.sqrt(determinante))/(2*a)
        x2=(-b2 +math.sqrt(determinante))/(2*a)
    print("x1=",x1, "x2=", x2)

def risolvi_equazione(b,c,x1):
    if((b==0) and (c==0)):
        print("equazione indeterminata")
    else:
        if(b==0):
            print("equazione impossibile")
        else:
            x1=float(-c)/float(b)
            print("x=", x1)

a=float(input("inserisci il valore di a"))
b=float(input("inserisci il valore di b"))
c=float(input("inserisci il valore di c"))

if(a!=0):
    determminante=calcolo_determinante(a,b,c)
    print(determinante)
    calcolo_soluzioni(determinante,b,a)
else:
    risolvi_equazione(b,c,x1)



