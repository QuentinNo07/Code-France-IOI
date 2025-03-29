def inverse(texte,taille):
   if taille==0:
      print(texte[0])
   else:
      print(texte[taille],end="")
      inverse(texte,taille-1)
   

texte=input()
taille=len(texte)-1
inverse(texte,taille)