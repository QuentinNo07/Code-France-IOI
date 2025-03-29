import math
def nb_paquet(n, p):
   resultat = math.factorial(n) // (math.factorial(p) * math.factorial(n - p))
   return resultat
def main():
   nbCardes = int(input())
   nb_in_box = int(input())
   print(nb_paquet(nbCardes, nb_in_box))
main()