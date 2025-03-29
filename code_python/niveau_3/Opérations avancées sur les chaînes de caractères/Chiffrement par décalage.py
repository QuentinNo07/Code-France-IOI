def valeur_decalage(numero_page):
   if numero_page %2==0:
      return -3*numero_page 
   else:  
      return 5*numero_page
   
   
def decallage(character,decalage):
   if character.isalpha():
      if character.islower():
         alphabet="abcdefghijklmnopqrstuvwxyz"
      else:
         alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
         
      index_original=alphabet.index(character)
      new_index=(index_original+decalage)%26
      return alphabet[new_index]
      
   else:
      return character
   
nb_page=int(input())

for numero_page in range(2,nb_page+1):
   valeur_de=valeur_decalage(numero_page)
   phrase=input()
   texte_decrypte=[]
   for character in phrase:
      texte_decrypte.append(decallage(character,valeur_de))
   
   print(''.join(texte_decrypte))  
   