def total_utilisation(interval):
   interval.sort()
   temps_total=0
   debut, fin=interval[0]
   
   for i in range(1,len(interval)):
      d, f=interval[i]
      if d<=fin:
         fin=max(f,fin)
      else:
         temps_total+=fin-debut
         debut,fin= d, f
   temps_total+=fin-debut
   return   temps_total 
   
N = int(input())
intervalles = []
for _ in range(N):
    D, F = map(int, input().split())
    intervalles.append((D, F))

resultat = total_utilisation(intervalles)
print(resultat)
