#Mastermind Project by Hypnotiquee and Swahili
import random
from random import randint


#Nombre de couleurs (Code Final)
x=0
color=[]
lor=input("Nombre de couleurs")
nbrcolor=int(lor)
while nbrcolor!=0 :
    x+=1
    color.append(x)
    nbrcolor=nbrcolor-1
print(color)


#Autres(Incomplet)
colonnes=input("Nombre de colonnes")
tentatives=input("Nombre de tentatives")


#Bot Combinaison (Code Final)
comb=[]
boule_ini=int(colonnes)
for i in range (0,boule_ini,1):
    y=randint(1, len(color))
    comb.append(y)
print(comb)

#Pions Bien Placés (Code Final)
def BienPlacé (comb, play):
    bienplacé = 0
    for i in range(len(comb)):
        if play[i]==comb[i]:
            bienplacé+=1
    return bienplacé
print(BienPlacé(comb, play))
