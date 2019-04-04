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
    y=randint(1,len(CouleurListe))
    OrdiCombinaison.append(y)
print(OrdiCombinaison)

#Combinaison du Joueur (Code Test)
def CombinaisonJoueur(JoueurCombinaison):
    JoueurCombinaison=[]
    for i in range(NbrColonnes):
        Tentative=input("Choisissez une couleur")
        JoueurCombinaison.append(int(Tentative))
    return JoueurCombinaison
print(CombinaisonJoueur(JoueurCombinaison))

#Boucle principale (Pas Fait)
if xxxxxxxxxx
    #Pions Bien Placés (Code Final)
    def PionsBienPlacés (OrdiCombinaison,JoueurCombinaison):
        BienPlacés=0
        for i in range(len(OrdiCombinaison)):
            if JoueurCombinaison[i]==OrdiCombinaison[i]:
                BienPlacés+=1
        return BienPlacés
    print(PionsBienPlacés(OrdiCombinaison,JoueurCombinaison))
    #Pions Mal Placés (Code opérationnel)
    #Problème de Pions en plusieurs exemplaires comptés trop de fois réglé : Aide du prof
    def PionsMalPlacés (OrdiCombinaison,JoueurCombinaison):
        OrdiCombinaisonCopie=[couleur for couleur in OrdiCombinaison]
        Présentes=0
        for i in range(len(JoueurCombinaison)):
            Compare=JoueurCombinaison[i]
            for i in range(len(OrdiCombinaisonCopie)):
                if Compare==OrdiCombinaisonCopie[i]:
                    Présentes+=1
                    OrdiCombinaisonCopie[i]=0
                    break
                else:
                    Présentes+=0
        MalPlacés=Présentes-PionsBienPlacés(OrdiCombinaison,JoueurCombinaison)
        return MalPlacés
    print(PionsMalPlacés(OrdiCombinaison,JoueurCombinaison))

#Gagné (A Modifier ?)
elif OrdiCombinaison==JoueurCombinaison:
    print ("Vous avez gagné")
