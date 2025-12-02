#scrivere una funzione che dati due numeri interi crea la funzione

def maggiore (numero1,numero2):
    if numero1>numero2:
        return numero1
    else:
        return numero2

numero1=input("inserire il primo numero")
numero1=int(numero1)
numero2=input("inserire il secondo numero")
numero2=int(numero2)

maggiore(numero1,numero2)
risultato=maggiore(numero1,numero2)
print ("il numero piu grande è",risultato)

def pari_dispari (numero):
    if numero%2==0:
        print("il numero è pari")
    else:
        print("il numero è dispari")

n= risultato
risultato=pari_dispari(n)
