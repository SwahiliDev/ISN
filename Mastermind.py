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
NbrColonnes=int(Colonnes)
Tentatives=input("Nombre de tentatives")
NbrTentatives=int(Tentatives)


#Combinaison de l'Ordinateur (Code Final)
OrdiCombinaison=[]
for i in range (0,NbrColonnes,1):
    y=randint(1,len(CouleurListe))
    OrdiCombinaison.append(y)
print(OrdiCombinaison)



def CombinaisonJoueur(JoueurCombinaison):
    for i in range(NbrColonnes):
        Tentative=input("Choisissez une couleur")
        JoueurCombinaison.append(int(Tentative))
    return JoueurCombinaison


def PionsBienPlacés (OrdiCombinaison,JoueurCombinaison):
    BienPlacés=0
    for i in range(len(OrdiCombinaison)):
        if JoueurCombinaison[i]==OrdiCombinaison[i]:
            BienPlacés+=1
    return BienPlacés

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

for i in range(0,NbrTentatives,1):
    #Combinaison du Joueur (Code Test)
    JoueurCombinaison=[]
    print(CombinaisonJoueur(JoueurCombinaison))

    #Boucle principale (Pas Fait)
    if JoueurCombinaison!=OrdiCombinaison:
        #Pions Bien Placés (Code Final)
        
        print(PionsBienPlacés(OrdiCombinaison,JoueurCombinaison))
        #Pions Mal Placés (Code opérationnel)
        #Problème de Pions en plusieurs exemplaires comptés trop de fois réglé : Aide du prof
        
        print(PionsMalPlacés(OrdiCombinaison,JoueurCombinaison))

    #Gagné (A Modifier ?)
    else :
        print("marche")
        break
