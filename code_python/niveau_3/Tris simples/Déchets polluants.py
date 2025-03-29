nb_boite,nb_repetition=map(int,input().split())
boite=list(map(int, input().split()))
boite.sort(reverse=True)

for i in range(nb_repetition):
   print(boite[i], end=" ")