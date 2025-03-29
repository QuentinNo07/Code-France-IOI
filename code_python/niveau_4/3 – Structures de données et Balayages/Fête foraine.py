def main():
   nb_cible=int(input())
   cibles=list(map(int,input().split()))
   
   nb_lots=int(input())
   lots=list(map(int,input().split()))
   
   for cible in cibles:
      for i in range(nb_lots):
         if cible<lots[i]:
            print(lots[i-1], end=" ")
            break
main()