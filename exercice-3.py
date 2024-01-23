# Saisissez le rayon R d’un cercle et un angle a (en degré(s)). Calculez et affichez l’aire du secteur circulaire.
# Aire = ∏ * R2 * a / 360

# On demande les infos a l'utilisateur
rayon = float(input("Saisir le rayon du cercle en cm : "))
angle = float(input("Saisir un angle en degrés : "))

# Calcul puis affichage
aire = (3.14 * (rayon * rayon) * angle)/360
print(f"L'aire du secteur circulaire est de {aire}")