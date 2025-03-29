def main():
    nb_spectacles = int(input())
    spectacles = []
    for _ in range(nb_spectacles):
        duree, frequentation = map(int, input().split())
        spectacles.append((duree, frequentation))
    spectacles.sort()  
    
    somme_cumulee = 0
    meilleure_moyenne = 0
    meilleure_limite = 0
    
    for i in range(nb_spectacles):
        duree, frequentation = spectacles[i]
        somme_cumulee += frequentation 
        moyenne = somme_cumulee / (i + 1)  
        
        if moyenne > meilleure_moyenne or (moyenne == meilleure_moyenne and duree > meilleure_limite):
            meilleure_moyenne = moyenne
            meilleure_limite = duree
    
    print(meilleure_limite)

main()