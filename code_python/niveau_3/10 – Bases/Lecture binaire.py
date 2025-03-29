nb=input()
chaine_inverse=nb[::-1]
compteur=0
for i in range(len(chaine_inverse)):
   if chaine_inverse[i]=="1":
      compteur+=2**(i)
     
print(compteur)