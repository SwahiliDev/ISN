#Mastermind Project by Hypnotiquee and Swahili
import random
from random import randint


#How many colors (Issues fixed : final code)
x=0
color=[]
lor=input("Nombre de couleurs")
nbrcolor=int(lor)
while nbrcolor!=0 :
    x+=1
    color.append(x)
    nbrcolor=nbrcolor-1
print(color)


#Other(Incomplete)
colonnes=input("Nombre de colonnes")
tentatives=input("Nombre de tentatives")




#Initial Combination (Issues fixed : final code)
comb=[]
boule_ini=int(colonnes)
for i in range (0,boule_ini,1):
    y=randint(1, len(color))
    comb.append(y)
print(comb)






 
"""
for i in range (0,(tentatives+1),1):
"""
