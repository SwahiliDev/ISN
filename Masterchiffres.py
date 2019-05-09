import random
from random import randint

#Nombre de chiffres
x=0
chiffres_liste=[]
chiffres=input("Combien de chiffres différents (entre 1 et 9)")
nombre_chiffres=int(chiffres)
while nombre_chiffres>=0:
    if nombre_chiffres<=9:
        x+=1
        chiffres_liste.append(x)
        nombre_chiffres=nombre_chiffres-1
    else:
        print("Votre nombre de chiffres doit être compris entre 1 et 9")
        chiffres=input("Combien de chiffres DIFFÉRENTS (entre 1 et 9)")
        nombre_chiffres=int(chiffres)

#Autres
colonnes=input("Nombre de colonnes")
nombre_colonnes=int(colonnes)
tentatives=input("Nombre de chances")
nombre_tentatives=int(tentatives)
compteur=0
gameover=1

#Combinaison de l'Ordinateur
ordi_combinaison=[]
for i in range (0,nombre_colonnes,1):
    y=randint(1,len(chiffres_liste))
    ordi_combinaison.append(y)
print ("Combinaison à trouver", ordi_combinaison)

#Combinaison du Joueur
def CombinaisonJoueur():
    combinaison_joueur=[]
    selection_chiffres=input("Choisissez une combinaison (Exemple : 1234)")
    if (len(selection_chiffres)==nombre_colonnes) :
        for i in range(nombre_colonnes):
            combinaison_joueur.append(int(selection_chiffres[i]))
    return combinaison_joueur #liste vide à tester si erreur d'entrée

#Nombre de chiffres bien placés
def ChiffresBienPlacés(ordi_combinaison,joueur_combinaison):
    bien_placés=0
    for i in range(len(ordi_combinaison)):
        if joueur_combinaison[i]==ordi_combinaison[i]:
            bien_placés+=1
    return bien_placés

#Nombre de chiffres mal placés (prof)
def ChiffresMalPlacés(ordi_combinaison,joueur_combinaison):
    ordi_combinaison_copie=[chiffres for chiffres in ordi_combinaison]
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
    malplacés=présentes-ChiffresBienPlacés(ordi_combinaison,joueur_combinaison)
    return malplacés

#Boucle principale
while nombre_tentatives!=0 and gameover != 0:
    #Affichage de l'historique des combinaisons
    joueur_combinaison=CombinaisonJoueur()
    if len(joueur_combinaison) == 0 :
        print("Attention, il faut que vous entriez:",nombre_colonnes,"chiffres !")
    else :
        print("Votre proposition n°", compteur+1, "est : ", joueur_combinaison)
        nombre_tentatives-=1
        compteur+=1
        #Boucle de comparaison
        if joueur_combinaison!=ordi_combinaison:
            print("Vous avez:",ChiffresBienPlacés(ordi_combinaison,joueur_combinaison),"chiffres de bien placés")
            print("Vous avez:",ChiffresMalPlacés(ordi_combinaison,joueur_combinaison),"chiffres de mal placés")
        #Message de victoire
        else :
            print("Vous avez gagné en ",compteur,"tentative(s)")
            gameover=0
#Message de défaite
if gameover==1:
    print("Perdu, vous avez utilisé vos",compteur,"tentative(s)")
