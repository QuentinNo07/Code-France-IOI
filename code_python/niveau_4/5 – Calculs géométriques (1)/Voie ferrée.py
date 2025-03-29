import math
def main():
    # Lecture des coordonnées des points de la voie ferrée
    x1, y1, x2, y2 = map(int, input().split())
    
    # Lecture du nombre de positions proposées
    N = int(input())
    
    # Variables pour suivre la position la plus éloignée
    max_distance = -1
    farthest_position = (0, 0)
    
    # Calcul de la distance pour chaque position proposée
    for _ in range(N):
        xi, yi = map(int, input().split())
        
        # Calcul de la distance du point (xi, yi) à la ligne
        numerator = abs((y2 - y1) * xi - (x2 - x1) * yi + x2 * y1 - y2 * x1)
        denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        distance = numerator / denominator
        
        # Vérification si cette position est la plus éloignée
        if distance > max_distance:
            max_distance = distance
            farthest_position = (xi, yi)
    
    # Affichage des coordonnées de la position la plus éloignée
    print(farthest_position[0], farthest_position[1])
# Appel de la fonction principale
main()