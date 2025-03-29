nb_variable=int(input())

for i in range(nb_variable):
   nom=input()
   taille=len(nom)
   correct=True
   if not(nom[0].isalpha() or nom[0]=="_"):
      print("NO")
      correct=False
      continue
      
      
   for i in range(1,taille):
      if not (nom[i].isalpha() or nom[i].isdigit() or nom[i]=="_"):
         print("NO")
         correct=False
         break
   if correct:
      print("YES")
