import sys
input = sys.stdin.read

data = input().splitlines()
nb_requetes = int(data[0])
affiches = []
resultats = []

for i in range(1, nb_requetes + 1):
    requete = data[i].split()
    if requete[0] == "C":
        hauteur = int(requete[1])
        # Retirer toutes les affiches recouvertes
        while affiches and affiches[-1] <= hauteur:
            affiches.pop()
        affiches.append(hauteur)
    elif requete[0] == "Q":
        resultats.append(len(affiches))

# Impression des résultats en une seule fois
sys.stdout.write("\n".join(map(str, resultats)) + "\n")