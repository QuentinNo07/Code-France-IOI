phrase=input().upper()
compteur=[0]*26
taille=len(phrase)
for i in range(taille):
   if phrase[i]!=" ":
      indice=ord(phrase[i])-ord("A")
      compteur[indice]+=1
   
index=compteur.index(max(compteur))
print(chr(index+ord("A")))