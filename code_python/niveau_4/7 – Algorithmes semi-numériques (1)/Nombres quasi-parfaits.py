import sys
def main():
    limite = int(sys.stdin.readline().strip())
    dif = int(sys.stdin.readline().strip())
    
    # Initialiser un tableau pour la somme des diviseurs
    somme_diviseurs = [0] * (limite + 1)
    
    # Calculer la somme des diviseurs pour chaque nombre
    for i in range(1, limite + 1):
        for j in range(2 * i, limite + 1, i):
            somme_diviseurs[j] += i
            
    compteur = 0
    for i in range(1, limite + 1):
        if abs(somme_diviseurs[i] - i) <= dif:
            compteur += 1
            
    print(compteur)
main()