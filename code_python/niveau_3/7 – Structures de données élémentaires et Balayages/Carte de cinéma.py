nb_client = int(input())
clients = list(map(int, input().split()))
cartes_vues = set()
tricheur = -1

for carte in clients:
    if carte in cartes_vues:
        tricheur = carte
        break
    cartes_vues.add(carte)

# Afficher le résultat
print(tricheur)