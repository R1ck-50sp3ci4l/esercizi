"""
scrivere una funzione che data una lista ,stampi a video
il numero degli elementi pari
"""
def numeri_pari (lista):
    contatore=0
    for elements in lista:
        if elements%2==0:
            contatore=contatore+1
    print(contatore)

lista=[]
for i in range(10):
    elements = input("Inserisci un elemento: ")
    lista.append(int(elements))

numeri_pari(lista)
print("i numeri pari sono:")
