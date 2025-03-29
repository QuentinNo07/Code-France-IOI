def posibilite(premier, compte):
    global choix
    
    # Si nous avons rempli tous les jours, imprimez le résultat
    if compte == 0:
        print(" ".join(map(str, choix)))
        return
    
    # Générer des combinaisons
    for cours in range(premier, nbChoix + 1):
        choix[nb_jour - compte] = cours  
        posibilite(cours, compte - 1) 
        
nbChoix, nb_jour = map(int, input().split())
choix = [None] * nb_jour

posibilite(1, nb_jour)
