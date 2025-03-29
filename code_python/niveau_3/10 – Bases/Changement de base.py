def depart(liste, base_depart, nb_chiffre):
   liste.reverse()
   compteur=0
   for i in range(nb_chiffre):
      compteur+=liste[i] * (base_depart**i)
   return compteur
      
def arrive(nombre, base_arrive):
   if nombre==0:
      return [0]
   liste_chiffre=[]
   while nombre>0:
      reste=nombre % bs_arrive
      liste_chiffre.append(reste)
      nombre=nombre//bs_arrive
   liste_chiffre.reverse()
   return liste_chiffre
   
 
bs_depart, bs_arrive, nb_chiffre=map(int,input().split())
nombre=list(map(int,input().split()))

valeur_decimal = depart(nombre, bs_depart, nb_chiffre)
valeur_base_arrive = arrive(valeur_decimal, bs_arrive)

for element in valeur_base_arrive :
   print(element, end=" ")