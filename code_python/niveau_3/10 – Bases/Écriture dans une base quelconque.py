nb,base=map(int,input().split())
liste_chiffre=[]
if nb==0:
   liste_chiffre.append(0)
else:
   while nb>0:
      reste=nb%base
      liste_chiffre.append(reste)
      nb=nb//base
   
liste_chiffre.reverse()
print(len(liste_chiffre))
for element in liste_chiffre:
   print(element, end=" ")