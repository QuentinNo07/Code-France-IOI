import math
def main():
   N=int(input())
   P=int(input())
   resultat=math.factorial(N)//math.factorial(N-P)
   print(resultat)
   
main()