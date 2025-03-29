nb_bacs=int(input())

bacs_non_trie=list(map(int,input().split()))

for i in range(nb_bacs):
   for y in range(nb_bacs-1-i):
      if bacs_non_trie[y]>bacs_non_trie[y+1]:
         bacs_non_trie[y],bacs_non_trie[y+1]=bacs_non_trie[y+1],bacs_non_trie[y]
         
for nombre in bacs_non_trie:
   print(nombre,end=" ")