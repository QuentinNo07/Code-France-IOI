nb_valeur=int(input())
liste_nombre=list(map(int,input().split()))

liste_trie=liste_nombre.sort()

for nombre in liste_trie:
   print(nombre, end=" ")