def binaire(valeur, nb):
    nombre = valeur * nb
    binaire = []
    if nombre == 0:  # Gérer le cas où le produit est 0
        return '0'
    while nombre > 0:
        if nombre % 2 == 0:
            binaire.append('0')
        else:
            binaire.append('1')
        nombre = nombre // 2
    binaire.reverse()  # Les chiffres binaires doivent être dans l'ordre inverse
    return ''.join(binaire)

# Lecture de l'entrée
nb = int(input())

# Génération et affichage de la table de multiplication binaire
for i in range(1, nb + 1):
    liste_ligne = []
    for j in range(1, nb + 1):
        valeur = binaire(i, j)
        liste_ligne.append(valeur)
    print("\t".join(liste_ligne))