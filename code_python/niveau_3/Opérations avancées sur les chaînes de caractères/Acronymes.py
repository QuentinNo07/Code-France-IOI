def mise_en_propre(titre):
   titre_propre=' '.join([mot.capitalize() for mot in titre])
   return titre_propre 


acronyme=input().upper()
nb_livres=int(input())


for i in range(nb_livres):
   titre=input().split()
   initiale=''.join([mot[0].upper() for mot in titre])
   
   if initiale==acronyme:
      print(mise_en_propre(titre))
     