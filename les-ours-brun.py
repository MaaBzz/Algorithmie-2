# on vous demande d’établir l’algorithme permettant de calculer et
# d’afficher le tarif unitaire du forfait demandé en précisant le statut du bénéficiaire.

# On demande le type de forfait souhaité
TypeForfait = int(input("Saisir 1 pour un forfait 1 journée ou 2 pour un forfait pour la saison : "))

# On demande l'âge
Age = int(input("Saisir votre âge : "))

# On calcul toutes les possibilitées et on affiche le prix
if TypeForfait == 1 and Age < 12:
    print(f"Le prix de votre forfait est de : 18,70€")
elif TypeForfait == 1 and (Age >= 12 and Age <= 60):
    print(f"Le prix de votre forfait est de : 25,80€")
elif TypeForfait == 1 and Age > 60:
    print(f"Le prix de votre forfait est de : 21,40€")
elif TypeForfait == 2 and Age < 12:
    print(f"Le prix de votre forfait est de : 300€")
elif TypeForfait == 2 and (Age >= 12 and Age <= 60):
    print(f"Le prix de votre forfait est de : 510€")
elif TypeForfait == 2 and Age > 60:
    print(f"Le prix de votre forfait est de : 340€")
else:
    print("Problème veuillez recommencer")
