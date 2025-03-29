nb_operation = int(input())
liste = []

for _ in range(nb_operation):
    operation = list(map(int, input().split()))
    quantite = operation[0]
    if quantite > 0:
        liste.append((quantite, operation[1]))
    else:
        quantite = -quantite  
        while quantite > 0 and liste:
            quantite_top, date_top = liste[-1]
            if quantite_top > quantite:
                liste[-1] = (quantite_top - quantite, date_top)
                quantite = 0
            else:
                quantite -= quantite_top
                liste.pop()
min_date = min(date for _, date in liste)
print(min_date)