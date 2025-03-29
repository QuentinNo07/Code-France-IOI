def hanoi(nb_disque,depart,arrive,intermediaire):
   if nb_disque>0:
      hanoi(nb_disque-1,depart,intermediaire,arrive)
      print(depart,"->",arrive)
      hanoi(nb_disque-1,intermediaire,arrive,depart)

nb_disque=int(input())
hanoi(nb_disque,1,3,2)