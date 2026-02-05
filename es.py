#data una lista di 10 elementi random interi nell'intervallo -10,+10
#calcolare il numero degli elementi pari da queli dispari
import random

def creaLista(lista):
    for i in range (0,10):
        element=random.randint(-10,+10)
        lista.append(element)
    return lista

def contaLista(lista):
    contatore1=0
    contatore2=0
    for i in range(0,10):
        if lista[i]%2==0:
            contatore1=contatore1+1
        else:
            contatore2=contatore2+1
    print("i numeri pari sono",contatore1)
    print("i numeri dispari sono",contatore2)
        


if __name__=="__main__":
    mylist=[]
    creaLista(mylist)
    
    contaLista(mylist)