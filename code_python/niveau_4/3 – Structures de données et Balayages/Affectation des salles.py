def disponibilite(nb_salle, representations):
    # Trie les représentations par date de début
    representations.sort(key=lambda x: x[1][0])
    
    # Liste pour suivre la fin de la dernière représentation de chaque salle
    fins_salles = [0] * nb_salle
    affectation = [-1] * len(representations)
    
    for index, (i, (debut, fin)) in enumerate(representations):
        # Trouver la première salle disponible
        for j in range(nb_salle):
            if debut >= fins_salles[j]:
                fins_salles[j] = fin
                affectation[i] = j + 1
                break
        else:
            # Aucune salle disponible pour cette représentation
            return "NON", []
    
    return "OUI", affectation

def main():
    nb_salle, nb_representation = map(int, input().split())
    representations = []