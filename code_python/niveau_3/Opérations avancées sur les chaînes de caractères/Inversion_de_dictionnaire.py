nb_mots=int(input())

couples=[]

for i in range(nb_mots):
   mot2,mot1=input().split()
   
   couples.append((mot1,mot2))

couples.sort(key=lambda x: x[0])

for couple in couples:
   print("{} {}".format(couple[0],couple[1]))