mot=input().lower()
compteur=0
phrase=list(input().lower().split())
for mots in phrase:
   if mots==mot:
      compteur+=1
print(compteur)