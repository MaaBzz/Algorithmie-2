# Rédiger un algorithme qui, à partir d’une année de naissance, calcule l’âge et affiche le résultat à
# l’utilisateur.
# On considère que la fonction ANNEE() nous donne l’année en cours

# On demande l année de naissance
birth_year = int(input("Saisir une année de naissance : "))

# fonction d'ANNEE
def ANNEE(n):
    return n

# Calcul puis affichage
age = ANNEE(2023) - birth_year
print(f"Vous avez {age} ans")
