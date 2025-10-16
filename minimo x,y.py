import random
punti_cartesiano=[]
for i in range(0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)

minimox=punti_cartesiano[0]
for i in range(0,20):
    if punti_cartesiano[i][0]<minimox[0]:
        minimox=punti_cartesiano[i]
print("la dupla con il valore di x piu piccolo è:",minimox)

minimoy=punti_cartesiano[1]
for i in range(0,20):
    if punti_cartesiano[i][1]<minimoy[0]:
        minimoy=punti_cartesiano[i]
print("la dupla con il valore di y piu piccolo è:",minimoy)

"""
abbiamo fatto la stessa cposa dell'esercizio di
prima solo che invece che il massimo abbiamo fatto il minimo
"""