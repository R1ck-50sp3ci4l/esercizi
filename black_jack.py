import random
somma=0
contatore=0
mazzo=[]
mazzo=[1,2,3,4,5,6,7,8,9,10,"j","q","k"]
bj={}
bj={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"j":10,"q":10,"k":10}

while somma<=21:
    i=random.randint(1,13)
    carta=mazzo[i]
    valore=bj[carta]
    somma=somma+valore
    contatore=contatore+1


