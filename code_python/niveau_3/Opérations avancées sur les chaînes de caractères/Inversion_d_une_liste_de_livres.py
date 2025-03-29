nb_livre=int(input())
livres=[" "]*nb_livre
for i in range(nb_livre):
   livres.append(input())

livres=livres[::-1]

for livre in livres:
   print(livre)