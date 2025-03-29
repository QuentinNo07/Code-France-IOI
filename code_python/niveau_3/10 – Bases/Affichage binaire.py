# Lire un nombre entier depuis l'entrée
nb = int(input())

# Cas spécial pour le nombre 0
if nb == 0:
    print(0)
else:
    binaire = ""  # Initialiser la chaîne binaire vide
    while nb > 0:
        # Ajouter le bit de poids faible à la chaîne binaire
        binaire = str(nb % 2) + binaire
        # Diviser nb par 2 pour traiter le prochain bit
        nb = nb // 2

    # Afficher la chaîne binaire complète
    print(binaire)
    