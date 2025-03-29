nb_matiere=int(input())
liste=[]
for i in range(nb_matiere):
   liste.append(input())
   
liste.sort()
for matiere in liste:
   print(matiere)