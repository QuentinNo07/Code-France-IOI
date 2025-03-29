def main():
   taille_liste=int(input())
   liste=list(map(int,input().split()))
   longeur_max=0
   somme=0
   for i in range(taille_liste):
      somme+=liste[i]
      somme=max(somme,0)
      longeur_max=max(somme,longeur_max)
      
   print(longeur_max)

main()