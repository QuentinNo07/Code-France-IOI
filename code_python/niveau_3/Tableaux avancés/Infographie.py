# Lire les dimensions de la grille
nb_lignes, nb_colonnes = map(int, input().split())

# Initialiser la grille avec des points '.'
rectangle = [['.' for _ in range(nb_colonnes)] for _ in range(nb_lignes)]

# Lire le nombre de rectangles
nb_rectangle = int(input())

# Traiter chaque rectangle
for _ in range(nb_rectangle):
    ligne = input().split()
    iLig1, iCol1, iLig2, iCol2, charactere = int(ligne[0]), int(ligne[1]), int(ligne[2]), int(ligne[3]), ligne[4]
    
    # Ajuster les indices pour Python (qui commence à 0)
    for x in range(iLig1, iLig2+1):
        for y in range(iCol1, iCol2+1):
            rectangle[x][y] = charactere

# Afficher la grille
for ligne in rectangle:
    print(''.join(ligne))