from math import sqrt
from sys import stdin
def distance_ah(xa, ya, xp, yp,norme, vect_ab_x, vect_ab_y):

    vect_ap_x = xp - xa
    vect_ap_y = yp - ya
    
    ah = (vect_ap_x * vect_ab_x + vect_ap_y * vect_ab_y) / norme
    return "{:.6f}".format(ah)

def main():
    # Lecture des coordonnées de la route (A et B)
    xa, ya, xb, yb = map(int, input().split())
    vect_ab_x = xb - xa
    vect_ab_y = yb - ya
    norme= sqrt(vect_ab_x ** 2 + vect_ab_y ** 2)  
    nb = int(input())
    
    for _,description in zip(range(nb),stdin):
       xp, yp = map( int, description.split() )
       print(distance_ah(xa, ya,xp, yp,norme,vect_ab_x ,vect_ab_y))

main()