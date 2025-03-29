def carre_magique(carre, nb_ligne):
    # La somme magique que nous attendons
    somme_magique = sum(carre[0])
    
    # Vérifier la présence des nombres de 1 à nb_ligne^2
    nombre_attendu = set(range(1, nb_ligne * nb_ligne + 1))
    nombre_utilise = set()

    for ligne in carre:
        for valeur in ligne:
            if valeur in nombre_utilise or valeur not in nombre_attendu:
                return False
            nombre_utilise.add(valeur)
    
    # Vérifier les sommes des lignes
    for ligne in carre:
        if sum(ligne) != somme_magique:
            return False

    # Vérifier les sommes des colonnes
    for y in range(nb_ligne):
        somme_colonne = sum(carre[x][y] for x in range(nb_ligne))
        if somme_colonne != somme_magique:
            return False

    # Vérifier la somme de la diagonale principale
    somme_diag_principale = sum(carre[i][i] for i in range(nb_ligne))
    if somme_diag_principale != somme_magique:
        return False

    # Vérifier la somme de la diagonale secondaire
    somme_diag_secondaire = sum(carre[i][nb_ligne - i - 1] for i in range(nb_ligne))
    if somme_diag_secondaire != somme_magique:
        return False
    
    return True

# Lecture des entrées
nb_ligne = int(input())
carre = []

for _ in range(nb_ligne):
    ligne = list(map(int, input().split()))
    carre.append(ligne)

if carre_magique(carre, nb_ligne):
    print("yes")
else:
    print("no")
