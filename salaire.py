age = int(input("Quel est votre âge ?"))
salaire_demande = int(input("Quelles sont vos prétentions salariales ?"))
nb_exp = int(input("Combien d'annéees d'experience avez vous ?"))

if age < 30:
    print ("votre age n'est pas valable pour ce poste")       
elif salaire_demande > 40000:
    print("le salaire demandé est élevé pour  ce poste")
elif nb_exp < 3:
    print ("le nombre d'année d'expérience est insuffisant pour ce poste !")
else:
    print ("votre candidature sera prise en compte")



