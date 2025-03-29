nb_bacs = int(input())
liste_bacs = []

# Lecture des données
for _ in range(nb_bacs):
    liste_bacs.append(list(map(int, input().split())))

# Tri de la liste en fonction du niveau de pollution, puis de l'identifiant en cas d'égalité
liste_bacs.sort(key=lambda x: (x[1], x[0]))

# Affichage des résultats triés
for element in liste_bacs:
    print("{} {}".format(element[0], element[1]))