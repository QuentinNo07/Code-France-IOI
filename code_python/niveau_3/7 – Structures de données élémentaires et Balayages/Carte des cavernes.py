nb_caractere=int(input())
grotte=list(input())
pile=[]
for character in grotte:
   if character =='(':
      pile.append(character)
   elif character==')':
      if not pile:
         print(0)
         exit()
      pile.pop()

      
   
if not pile:
   print("1") 
else:
   print("0")