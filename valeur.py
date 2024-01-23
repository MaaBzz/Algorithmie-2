# Une voiture coûte 56 000 e et perd 7% de sa valeur chaque année.
# Rédiger le programme qui calcule et affiche la valeur de cette voiture au bout de 18 ans.

prix = 56000
perte = 0.93

# On boucle le nombre d'année (la c est 18 de base mais on peut changer)
for i in range(0,18):
    prix = prix * perte
print(f"La valeur de votre voiture dans 18 ans sera de {prix}€")