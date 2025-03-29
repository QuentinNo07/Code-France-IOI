def main():
    nb_maison = int(input())
    rue = list(map(int, input().split()))
    
    rue.sort()
    # Initialiser `m` avec une grande valeur
    m = rue[1] - rue[0]  # Commencez avec la distance entre les deux premières maisons triées
    for i in range(1, nb_maison - 1):  # Commencez à partir du deuxième indice
        distance = rue[i+1] - rue[i]
        m = min(m, distance)
    return m

print(main())