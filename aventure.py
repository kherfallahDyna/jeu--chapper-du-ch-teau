                                                   Introduction:
    - Échappe-toi du Château !
Un faux pas, et c'est la fin.
Plongez dans une aventure textuelle où chaque décision est une question de vie ou de mort. Fouillez votre cellule, affrontez les gardes et gérez votre inventaire pour trouver la sortie.
Saurez-vous débloquer la fin secrète ou resterez-vous prisonnier à jamais ?
                                                    
                                                   Code du jeu:

import random

nom = input("Quel est ton nom, aventurier ? ")
vie = 100
inventaire = []

print("\nBienvenue", nom, "dans le Château Maudit... 🏰")
print("Tu te réveilles dans une cellule sombre...\n")


def cellule():
    print("\n🔒 Tu es dans une cellule.")
    print("1. Chercher dans la cellule")
    print("2. Dormir")

    choix = input("Ton choix : ")

    if choix == "1":
        print("Tu trouves une clé rouillée 🔑 !")
        inventaire.append("clé")
        couloir()
    else:
        print("Tu ne te réveilles jamais... 💀")
        fin_perdu()


def couloir():
    print("\n🚪 Tu arrives dans un couloir sombre.")
    print("1. Aller à gauche")
    print("2. Aller à droite")

    choix = input("Ton choix : ")

    if choix == "1":
        salle_garde()
    else:
        salle_tresor()


def salle_garde():
    global vie
    print("\n👮 Un garde apparaît !")

    print("1. Attaquer")
    print("2. Fuir")

    choix = input("Ton choix : ")

    if choix == "1":
        chance = random.randint(1, 2)

        if chance == 1:
            print("Tu bats le garde ! 💪")
            inventaire.append("épée")
            sortie()
        else:
            print("Le garde te frappe ! 😵 (-50 vie)")
            vie -= 50

            if vie <= 0:
                fin_perdu()
            else:
                sortie()
    else:
        print("Tu t'échappes mais tu es blessé... (-20 vie)")
        vie -= 20
        sortie()


def salle_tresor():
    print("\n💰 Tu trouves une salle avec un coffre !")

    print("1. Ouvrir le coffre")
    print("2. Ignorer")

    choix = input("Ton choix : ")

    if choix == "1":
        print("Tu trouves une potion ❤️ !")
        inventaire.append("potion")
    else:
        print("Tu ignores le coffre...")

    sortie()


def sortie():
    print("\n🚪 Tu arrives devant la grande porte du château.")

    if "clé" in inventaire:
        print("Tu as une clé !")

        print("1. Ouvrir la porte")
        print("2. Attendre")

        choix = input("Ton choix : ")

        if choix == "1":
            if "potion" in inventaire:
                print("\n🏆 FIN SECRÈTE : Tu t'échappes en pleine forme avec des trésors !")
            else:
                print("\n🎉 FIN : Tu t'échappes du château !")
        else:
            print("Un garde arrive...")
            fin_perdu()
    else:
        print("La porte est fermée...")
        fin_perdu()


def fin_perdu():
    print("\n💀 GAME OVER 💀")
    print("Merci d'avoir joué !")
    exit()

cellule() 

                                             L'explication du code

import random
import sert à importer une bibliothèque.
random permet d’utiliser des fonctions aléatoires.
Ici on l’utilise pour choisir au hasard si le joueur gagne ou perd contre le garde.
2) Variables du joueur
Python
nom = input("Quel est ton nom, aventurier ? ")
input() demande une information à l’utilisateur.
Le texte entre " " s’affiche à l’écran.
La réponse est stockée dans la variable nom.
Python
vie = 100
Crée une variable vie.
Le joueur commence avec 100 points de vie.
Python
inventaire = []
Crée une liste vide.
Cette liste contiendra les objets trouvés :
clé
potion
épée
3) Messages de bienvenue
Python
print("\nBienvenue", nom, "dans le Château Maudit... 🏰")
print() affiche un texte.
\n fait un saut de ligne.
nom affiche le nom du joueur.
Python
print("Tu te réveilles dans une cellule sombre...\n")
Affiche l’histoire du début du jeu.
4) Fonction cellule()
Python
def cellule():
def sert à créer une fonction.
cellule est le nom de la fonction.
Python
print("\n🔒 Tu es dans une cellule.")
Affiche la situation du joueur.
Python
print("1. Chercher dans la cellule")
print("2. Dormir")
Affiche les choix possibles.
Python
choix = input("Ton choix : ")
Demande au joueur de choisir.
Python
if choix == "1":
if signifie “si”.
Vérifie si le joueur a choisi "1".
Python
print("Tu trouves une clé rouillée 🔑 !")
Message affiché si le joueur cherche.
Python
inventaire.append("clé")
append() ajoute un élément dans la liste.
Ici on ajoute "clé" à l’inventaire.
Python
couloir()
Appelle la fonction couloir().
Python
else:
else signifie “sinon”.
Python
print("Tu ne te réveilles jamais... 💀")
Message si le joueur dort.
Python
fin_perdu()
Lance la fonction de défaite.
5) Fonction couloir()
Python
def couloir():
Nouvelle fonction du jeu.
Python
print("\n🚪 Tu arrives dans un couloir sombre.")
Affiche le lieu.
Python
print("1. Aller à gauche")
print("2. Aller à droite")
Affiche les directions possibles.
Python
choix = input("Ton choix : ")
Demande un choix.
Python
if choix == "1":
Si le joueur choisit gauche.
Python
salle_garde()
Va dans la salle du garde.
Python
else:
    salle_tresor()
Sinon le joueur va dans la salle du trésor.
6) Fonction salle_garde()
Python
def salle_garde():
Fonction du combat.
Python
global vie
Permet de modifier la variable globale vie.
Python
print("\n👮 Un garde apparaît !")
Affiche l’ennemi.
Python
print("1. Attaquer")
print("2. Fuir")
Affiche les actions possibles.
Python
choix = input("Ton choix : ")
Demande l’action du joueur.
Python
if choix == "1":
Si le joueur attaque.
Python
chance = random.randint(1, 2)
Choisit un nombre aléatoire entre 1 et 2.
Python
if chance == 1:
Si le nombre vaut 1 → victoire.
Python
print("Tu bats le garde ! 💪")
Message de victoire.
Python
inventaire.append("épée")
Ajoute une épée à l’inventaire.
Python
sortie()
Passe à la sortie.
Python
else:
Sinon le joueur perd le combat.
Python
print("Le garde te frappe ! 😵 (-50 vie)")
Message de dégâts.
Python
vie -= 50
Enlève 50 points de vie.
Même chose que :
Python
vie = vie - 50
Python
if vie <= 0:
Vérifie si la vie est inférieure ou égale à 0.
Python
fin_perdu()
Le joueur perd.
Python
else:
    sortie()
Sinon le joueur continue.
Python
else:
    print("Tu t'échappes mais tu es blessé... (-20 vie)")
Cas où le joueur fuit.
Python
vie -= 20
Retire 20 points de vie.
Python
sortie()
Va vers la sortie.
7) Fonction salle_tresor()
Python
def salle_tresor():
Fonction de la salle du trésor.
Python
print("\n💰 Tu trouves une salle avec un coffre !")
Affiche la salle.
Python
print("1. Ouvrir le coffre")
print("2. Ignorer")
Choix possibles.
Python
if choix == "1":
Si le joueur ouvre le coffre.
Python
print("Tu trouves une potion ❤️ !")
Message de découverte.
Python
inventaire.append("potion")
Ajoute une potion.
Python
else:
    print("Tu ignores le coffre...")
Cas où le joueur ignore le coffre.
Python
sortie()
Continue vers la sortie.
8) Fonction sortie()
Python
def sortie():
Fonction finale.
Python
print("\n🚪 Tu arrives devant la grande porte du château.")
Affiche la porte.
Python
if "clé" in inventaire:
Vérifie si "clé" existe dans l’inventaire.
Python
print("Tu as une clé !")
Message affiché si le joueur possède la clé.
Python
print("1. Ouvrir la porte")
print("2. Attendre")
Choix final.
Python
if choix == "1":
Si le joueur ouvre la porte.
Python
if "potion" in inventaire:
Vérifie si le joueur possède une potion.
Python
print("\n🏆 FIN SECRÈTE : Tu t'échappes en pleine forme avec des trésors !")
Fin spéciale du jeu.
Python
else:
    print("\n🎉 FIN : Tu t'échappes du château !")
Fin normale.
Python
else:
    print("Un garde arrive...")
    fin_perdu()
Si le joueur attend → défaite.
Python
else:
    print("La porte est fermée...")
    fin_perdu()
Si le joueur n’a pas la clé.
9) Fonction fin_perdu()
Python
def fin_perdu():
Fonction de Game Over.
Python
print("\n💀 GAME OVER 💀")
Affiche la défaite.
Python
print("Merci d'avoir joué !")
Message final.
Python
exit()
Arrête complètement le programme.
10) Lancement du jeu
Python
cellule()
Démarre le jeu.
La première fonction exécutée est cellule().

                                           Conclusion
Ce projet est un petit jeu d’aventure réalisé en Python.
Il permet de découvrir plusieurs notions importantes de programmation de manière simple et amusante.


