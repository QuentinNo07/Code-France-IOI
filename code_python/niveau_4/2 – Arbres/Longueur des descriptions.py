from sys import setrecursionlimit
setrecursionlimit(50 * 1000)
def main():
   nbProduits = int(input())
   contenus = [[] for _ in range(nbProduits + 1)]
   for contenu, contenant in enumerate(map(int, input().split()), 1):
      contenus[contenant].append(contenu)
   def hauteur(racine):
      if racine:
         return max([hauteur(contenus[produit]) for produit in racine]) + 1
      return 0
   print(hauteur(contenus[0]))
main()