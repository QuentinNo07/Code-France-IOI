def mot(lettre,size,liste):
   if len(liste)==size:
      print(liste)
      return
   
   for l in lettre:
      liste+=l
      mot(lettre,size,liste)
      liste=liste[:-1]

def main():
   nb_lettre=int(input())
   lettre=input()
   size=int(input())
   
   print(nb_lettre**size)
   
   liste=""
   mot(lettre,size,liste)
 
main()
   