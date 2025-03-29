def recherche(liste, valeur):
    liste_position = []
    position = valeur
    while position != 0:
        liste_position.append(position)
        position = liste[position - 1]
    liste_position.reverse()
    return liste_position

nb = int(input())  
liste = list(map(int, input().split()))  

nb_recherche = int(input())  
valeur_recherche = list(map(int, input().split()))  

for i in range(nb_recherche):
    valeur = valeur_recherche[i]
    etape = recherche(liste, valeur)
    print(' '.join(map(str, etape)))