nb_produit=int(input())
liste=[]
produit=list(map(int,input().split()))


nb_operation=int(input())
for _ in range(nb_operation):
   indice,valeur=map(int,input().split())
   produit[indice-1]+=valeur
   
print(' '.join(map(str,produit)))