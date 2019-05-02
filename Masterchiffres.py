import random
from random import randint

#Nombre de couleurs
x=0
couleur_liste=[]
couleur=input("Nombre de couleurs")
nombre_couleur=int(couleur)
while nombre_couleur!=0 :
    x+=1
    couleur_liste.append(x)
    nombre_couleur=nombre_couleur-1

#Autres
colonnes=input("Nombre de colonnes")
nombre_colonnes=int(colonnes)
tentatives=input("Nombre de tentatives")
nombre_tentatives=int(tentatives)
compteur=0
gameover=1

#Combinaison de l'Ordinateur
ordi_combinaison=[]
for i in range (0,nombre_colonnes,1):
    y=randint(1,len(couleur_liste))
    ordi_combinaison.append(y)
print ("Solution secrete", ordi_combinaison)

#Combinaison du Joueur
def CombinaisonJoueur():
    combinaison_joueur = []
    selection_couleurs=input("Choisissez une couleur (ex 1224)")
    if (len(selection_couleurs) == nombre_colonnes) :
        for i in range(nombre_colonnes):
            combinaison_joueur.append(int(selection_couleurs[i]))
    return combinaison_joueur #liste vide à tester si erreur d'entrée

#Formules des pions bien placés
def PionsBienPlacés(ordi_combinaison,joueur_combinaison):
    bien_placés=0
    for i in range(len(ordi_combinaison)):
        if joueur_combinaison[i]==ordi_combinaison[i]:
            bien_placés+=1
    return bien_placés

#Formules des pions mal placés (prof)
def PionsMalPlacés(ordi_combinaison,joueur_combinaison):
    ordi_combinaison_copie=[couleur for couleur in ordi_combinaison]
    présentes=0
    for i in range(len(joueur_combinaison)):
        compare=joueur_combinaison[i]
        for i in range(len(ordi_combinaison_copie)):
            if compare==ordi_combinaison_copie[i]:
                présentes+=1
                ordi_combinaison_copie[i]=0
                break
            else:
                présentes+=0
    malplacés=présentes-PionsBienPlacés(ordi_combinaison,joueur_combinaison)
    return malplacés

#Boucle principale
while nombre_tentatives!=0 and gameover != 0:
    #Affichage de l'historique des combinaisons
    joueur_combinaison=CombinaisonJoueur()
    if len(joueur_combinaison) == 0 :
        print("Attention à introduire le bon nombre de couleurs !")
    else :
        print("Votre proposition n° ", compteur+1, " est : ", joueur_combinaison)
        nombre_tentatives-=1
        compteur+=1
        #Boucle de comparaison
        if joueur_combinaison!=ordi_combinaison:
            print(PionsBienPlacés(ordi_combinaison,joueur_combinaison))
            print(PionsMalPlacés(ordi_combinaison,joueur_combinaison))
        #Message de victoire
        else :
            print("Vous avez gagné en ",compteur,"tentative(s)")
            gameover=0
#Message de défaite
if gameover==1:
    print("Perdu, vous avez utilisé vos",compteur,"tentative(s)")
