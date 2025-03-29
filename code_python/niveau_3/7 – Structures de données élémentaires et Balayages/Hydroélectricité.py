# Lire les entrées
taille_central, distance_riviere = map(int, input().split())
forces_courant = list(map(int, input().split()))

# Initialisation de la somme de la première fenêtre de taille K
somme_max = current_sum = sum(forces_courant[:taille_central])

# Glissement de la fenêtre sur le reste de la rivière
for i in range(taille_central, distance_riviere):
    # Mettre à jour la somme en retirant l'élément qui sort de la fenêtre et en ajoutant l'élément qui entre dans la fenêtre
    current_sum += forces_courant[i] - forces_courant[i - taille_central]
    # Mettre à jour la somme maximale si nécessaire
    somme_max = max(somme_max, current_sum)

# Afficher le résultat
print(somme_max)
