base,nb_chiffre=map(int, input().split())
liste_chiffre=list(map(int,input().split()))
liste_chiffre.reverse()
compteur=0
for i in range(nb_chiffre):
   compteur+= liste_chiffre[i]*(base**i)
print(compteur)