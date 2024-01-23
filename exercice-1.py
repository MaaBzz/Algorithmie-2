# Rédiger un algorithme en pseudo-code qui demande à l’utilisateur de saisir le montant d’un produit acheté
# ainsi que la quantité acheté et qui affiche le montant totale avec une remise de 5 %.

# On demande les deux variables

prix = float(input("Saisir le prix du produit : "))
quantite = int(input("Saisir la quantité du produit : "))

# On fait le calcul puis affichage
produit = (prix*quantite) * 0.95
print(f"La somme de vos course avec les 5% de remise sera de {produit}€")