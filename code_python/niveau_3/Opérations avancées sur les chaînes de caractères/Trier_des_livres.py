nb_livres=int(input())

livres=[""]

for i in range(nb_livres):
   livres.append(input())
   
livres.sort()
for livre in livres:
   print(livre)