from collections import deque
def main():
   nbCol,nbLig = map(int,input().split())
   # Lecture de la grille avec sentinelles en passant de 2D à 1D
   BORD = "-"
   ligneVierge = BORD*(nbCol+1)
   grille = BORD.join([input() for _ in range(nbLig)])
   grille = "".join([ligneVierge,grille,ligneVierge])
   tailleGrille = (nbLig + 1)*(nbCol + 1)
   atteints = [[False]*tailleGrille for _ in range(tailleGrille)]
   mouvements = [-nbCol-1,nbCol+1,-1,1]
   posBlancInit = nbCol + 1
   posNoirInit = nbLig*(nbCol + 1) + nbCol - 1
   enAttente = deque()
   
   def empiler(posBlanc,posNoir):
      nonlocal atteints,enAttente
      if posBlanc == posNoirInit and posNoir == posBlancInit:
         print(1)
         exit(0)
      if not atteints[posBlanc][posNoir]:
         atteints[posBlanc][posNoir] = True
         enAttente.append((posBlanc,posNoir))
   
   empiler(posBlancInit,posNoirInit)
   while len(enAttente) > 0:
      blanc,noir = enAttente.pop()
      for mvtBlanc in mouvements:
         posBlanc = blanc + mvtBlanc
         couleur = grille[posBlanc]
         if couleur != BORD:
            for mvtNoir in mouvements:
               posNoir = noir + mvtNoir
               if grille[posNoir] == couleur:
                  empiler(posBlanc,posNoir)
   print(0)
main()
