nbCours,nbChoix = map( int, input().split() )
choix = [None]*nbChoix
def choisir(premier,compte):
   global choix
   if compte == 0:
      for cours in choix:
         print(cours,end=" ")
      print()
      return
   for cours in range(premier,nbCours-compte+2):
      choix[nbChoix - compte] = cours
      choisir(cours + 1,compte - 1)
   
if nbChoix <= nbCours:
   choisir(1,nbChoix)