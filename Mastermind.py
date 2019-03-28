#Mastermind Project by Hypnotiquee and Swahili
import random
from random import randint


#Nombre de couleurs (Code Final)
x=0
CouleurListe=[]
Couleur=input("Nombre de couleurs")
NbrCouleur=int(Couleur)
while NbrCouleur!=0 :
    x+=1
    CouleurListe.append(x)
    NbrCouleur=NbrCouleur-1
print(CouleurListe)


#Autres(Incomplet)
Colonnes=input("Nombre de colonnes")
Tentatives=input("Nombre de tentatives")


#Combinaison de l'Ordinateur (Code Final)
OrdiCombinaison=[]
NbrColonnes=int(Colonnes)
for i in range (0,NbrColonnes,1):
    y=randint(1,len(Couleur))
    OrdiCombinaison.append(y)
print(OrdiCombinaison)


#Pions Bien Placés (Code Final)
def PionsBienPlacés (OrdiCombinaison,JoueurCombinaison):
    BienPlacés=0
    for i in range(len(OrdiCombinaison)):
        if JoueurCombinaison[i]==OrdiCombinaison[i]:
            BienPlacés+=1
    return BienPlacés
print(PionsBienPlacés(OrdiCombinaison,JoueurCombinaison))


#Pions Mal Placés (ça marche moyen)
def CouleursPrésentes (OrdiCombinaison,JoueurCombinaison):
    Présentes=0
    for i in range(len(JoueurCombinaison)):
        Compare=JoueurCombinaison[i]
        for i in range(len(OrdiCombinaison)):
            if Compare==OrdiCombinaison[i]:
                Présentes+=1
            else:
                Présentes+=0
    MalPlacés=Présentes-PionsBienPlacés(OrdiCombinaison,JoueurCombinaison)
    return MalPlacés
print(CouleursPrésentes(OrdiCombinaison,JoueurCombinaison))
