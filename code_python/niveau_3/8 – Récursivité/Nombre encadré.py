def debutfin(valeur,nb_crochet):
   if nb_crochet>0:
      print('[',end="")
      debutfin(valeur, nb_crochet-1)
      print(']',end="")
   else:
      print(valeur,end="")
      
valeur, nb_crochet = input().split()
valeur = int(valeur)
nb_crochet = int(nb_crochet)

debutfin(valeur, nb_crochet)
