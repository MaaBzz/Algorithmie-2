# BONUS : améliorer votre programme en demandant à l’utilisateur le prix d’achat de sa voiture et
# l’année à laquelle il souhaite la vendre. (Faire les vérifications nécessaires)

# On demande le prix du véhicuuuuule et l'année de la vente
prix_achat = int(input("Saisir le prix d'achat de votre voiture en €: "))
annee = int(input("Saisir l'année de la future vente : "))

# Calcul du nombre d'année sans bibliothéque j'ai plus le nom exact)
anne_actuel = 2023
a = annee - anne_actuel

#  Boucle avec la perte par année et affichage
for i in range(0,a):
    prix_achat = prix_achat * 0.93
print(f"La valeur de votre voiture dans {a} ans sera de {prix_achat}€")
