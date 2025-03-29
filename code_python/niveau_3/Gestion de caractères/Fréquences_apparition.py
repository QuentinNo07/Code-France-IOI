phrase=''.join(input().upper())
alphabet=[0]*26
taille=len(phrase)
taille_pour_moyenne=taille

for i in range(taille):
   if not( phrase[i].isalpha()):
      taille_pour_moyenne-=1
   else:
      indice=ord(phrase[i])-ord("A")
      alphabet[indice]+=1
      
for element in alphabet:
   moyenne= float(element/ taille_pour_moyenne)
   print(moyenne)  