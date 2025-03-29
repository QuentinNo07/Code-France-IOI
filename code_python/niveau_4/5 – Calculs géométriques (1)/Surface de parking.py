from math import sqrt

def calc_height(xa, ya, xb, yb, xc, yc):
    # Vecteur AB
    vect_ab_x = xb - xa
    vect_ab_y = yb - ya
    
    # Vecteur AC
    vect_ac_x = xc - xa
    vect_ac_y = yc - ya
    
    # Norme de AB
    norme_ab = sqrt(vect_ab_x ** 2 + vect_ab_y ** 2)
    
    # Produit scalaire AC . AB
    produit_scalaire = vect_ac_x * vect_ab_x + vect_ac_y * vect_ab_y
    
    # Calcul de la hauteur (AH)
    hauteur = abs(produit_scalaire) / norme_ab
    
    return hauteur

def main():
    # Lecture des coordonnées des sommets
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xc, yc = map(int, input().split())
    
    # Calcul de la hauteur
    height = calc_height(xa, ya, xb, yb, xc, yc)
    
    # Calcul de la base
    base = sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
    
    # Calcul du double de la surface
    double_area = base * height
    
    # Affichage du résultat
    print(int(double_area))  # Conversion en entier si nécessaire

main()