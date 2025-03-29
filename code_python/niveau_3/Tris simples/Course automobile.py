nb_voiture=int(input())

ligne_actuel=list(map(int,input().split()))
depassement=[]
compteur=0
          
for i in range(nb_voiture):
    for j in range(nb_voiture - 1 - i):  # Réduire la plage de la boucle interne après chaque passe
        if ligne_actuel[j] > ligne_actuel[j + 1]:
            depassement.append((ligne_actuel[j], ligne_actuel[j + 1]))
            ligne_actuel[j], ligne_actuel[j + 1] = ligne_actuel[j + 1], ligne_actuel[j]
            compteur += 1

print(compteur)
for ligne in depassement:
    print("{} {}".format(ligne[0], ligne[1]))