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
            quantite_bas, date_bas = liste[0]
            if quantite_bas > quantite:
                liste[0] = (quantite_bas - quantite, date_bas)
                quantite = 0
            else:
                quantite -= quantite_bas
                liste.pop(0)

min_date = min(date for quantite, date in liste)
print(min_date)
