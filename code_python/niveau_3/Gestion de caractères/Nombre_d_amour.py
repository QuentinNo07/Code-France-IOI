def sup_dix(somme):
   while somme>=10:
      taille_somme=len(str(somme))
      new_somme=0
      for i in range(taille_somme):
         indice=str(somme)[i]
         new_somme+=int(indice)
      somme=new_somme
   return somme
   
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
noms=list(input().split(" "))
liste_somme=[]

for element in noms:
   taille=len(element)
   somme=0
   for i in range(taille):
      indice=alphabet.index(element[i])
      somme+=int(indice)
   if somme>=10:
      somme= sup_dix(somme)
   liste_somme.append(somme)  
                  
print("{} {}".format(liste_somme[0],liste_somme[1]))