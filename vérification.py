# Écrire un algorithme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse
# convienne. En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! », et
# inversement, « Plus grand ! » si le nombre est inférieur à 10.

# On met une variable vide
i = ""

# On boucle a l'infini
while i != 100000000 :
    # L'utilisateur saisi un chiffre jusqu'à qu'il trouve la bonne tranche, avec des indications
    i = int(input("Saisir un chiffre : "))
    if i > 20:
        print("Trop grand")
    elif i < 10:
        print("Trop petit")
    else:
        print("Gagné")
        # on casse pour en finir
        break