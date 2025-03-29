def main():
   L,C = map(int,input().split())
   compteur=0
   for _ in range(L):
      row= input()
      compteur+=row.count("#")
      
   return compteur
   
print(main())
   