# Rédiger l’algorithme permettant de compter le nombre de noms saisis avant l’interruption de la
# saisie (lorsque l’on saisit « fin »)

# On stock la variable de fin et on initialise la valeur de nom
i = "fin"
Nom = ""
NbNom = 0

# On boucle jusqu'à que l utilisateur rentre fin et on augmente le compteur a chaque tour
while Nom != i:
    Nom = input("Saisir un nom : ")
    NbNom += 1

# On enlève 1 pour supprimer le mot fin du compteur
NbNom -= 1
print(f"Vous avez rentré {NbNom} noms.")