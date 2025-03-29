decriptage=input()
alphabet="abcdefghijklmnopqrstuvwxyz"


dico_decryptage={alphabet[i] : decriptage[i] for i in range(26)}
dico_decryptage.update({alphabet[i].upper() : decriptage[i].upper() for i in range(26)})

texte_a_decripte=input()
texte_decrypte=[]

for character in texte_a_decripte:
   if character in dico_decryptage:
      texte_decrypte.append(dico_decryptage[character])
   else:
      texte_decrypte.append(character)
      

   
print(''.join(texte_decrypte))