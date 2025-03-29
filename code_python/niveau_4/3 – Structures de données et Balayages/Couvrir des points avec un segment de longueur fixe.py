def recherche(liste, surface, nb_point):
    compteur_max = 0
    compteur = 0
    j = 0
    liste.sort()
    
    for i in range(nb_point):
        while j < nb_point and liste[j] <= liste[i] + surface:
            j += 1
        compteur = j - i
        compteur_max = max(compteur, compteur_max)
    return compteur_max

def main():
    surface, nb_point = map(int, input().split())
    liste = list(map(int, input().split()))
    print(recherche(liste, surface, nb_point))

main()
