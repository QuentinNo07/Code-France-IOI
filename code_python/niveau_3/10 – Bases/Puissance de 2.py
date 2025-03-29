nb=int(input())
compteur=1
i=0
while nb>= compteur:
   compteur= 2**i
   i+=1
print(2**(i-1))