def main():
   m=100000
   nb_jour, nb_groupe=map(int,input().split())
   groupes=list(map(int, input().split()))
   deja_vue=[0 for i in range(nb_groupe +1)]
   compteur=0
   debut=0
   for fin in range(nb_jour):
      currentGroupe=groupes[fin]
      
      if deja_vue[currentGroupe]==0:
         compteur+=1
      deja_vue[currentGroupe]+=1
      
      while compteur==nb_groupe:
         m=min(m, fin-debut)
         deja_vue[groupes[debut]] -=1
         if deja_vue[groupes[debut]]==0:
            compteur-=1
            
         debut+=1

   print(m+1)

main()