nb_livres=int(input())
livres=[]

for i in range(nb_livres):
   livres.append(input().strip())

taille=len(livres)

print(livres[0])
livre_precedent=livres[0]

for i in range(1,taille):
   livre_lu=livres[i]
   if livre_lu>livre_precedent:
      print(livre_lu)
   livre_precedent=livre_lu