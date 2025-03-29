nb_carton = int(input())
liste = [0] * (nb_carton + 1)
cartons = list(map(int, input().split()))
for carton in cartons:
    liste[carton] += 1
maxi = max(liste)
print(maxi)