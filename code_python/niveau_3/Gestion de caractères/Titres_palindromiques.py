nb_livre=int(input())

for i in range(nb_livre):
   titre=input()
   titre_maj=''.join(titre.upper().split())
   taille=len(titre_maj)
   est_palindrome=True
   for i in range(taille//2):
      if titre_maj[i]!=titre_maj[taille-i-1]:
         est_palindrome=False
         break
   if est_palindrome:
      print(titre)
      