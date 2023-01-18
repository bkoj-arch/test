import random
import time


def dessiner(nv_eau):
    nb_diese=nv_eau//10
    nb_espace=10-nb_diese
    print(" _ ")
    for i in range(nb_espace):
        print("| |")
    for i in range(nb_diese):
        print("|\033[5;34m#\033[0m|")

lim=70
nb=random.randint(0,100)
print("Le niveau actuel est de ",nb)

dessiner(nb)

if nb < lim:
    choix=input("Voulez-vous remplir la cuve? (O/n): ")
    
    if choix == "O" or choix == "":
        print("On remplit la cuve")

        while nb < lim+10:
            dessiner(nb)
            time.sleep(1)
            print("\n"*50)
            nb=nb+10
    else:
        print("On remplit pas la cuve...")
else:
        print("On remplit pas la cuve...")

dessiner(nb)
