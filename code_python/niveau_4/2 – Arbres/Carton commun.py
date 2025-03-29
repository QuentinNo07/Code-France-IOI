def recherche(liste, valeur):
    liste_position = []
    position = valeur
    while position != 0:
        liste_position.append(position)
        position = liste[position - 1]
    return liste_position

def check_box(liste1, liste2):
    for element in liste1:
        if element in liste2:
            return element
    return 0

nb = int(input())
liste = list(map(int, input().split()))

nb_question = int(input())
for _ in range(nb_question):
    valeur1, valeur2 = map(int, input().split())
    valeur1_liste = recherche(liste, valeur1)
    valeur2_liste = recherche(liste, valeur2)
    print(check_box(valeur1_liste, valeur2_liste))