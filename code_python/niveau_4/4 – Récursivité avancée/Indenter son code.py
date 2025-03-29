def indentation(chaine, niveau=0):
   if not chaine:
      return ""
      
   resultat=""  
   if chaine[0]=="{":
      resultat+='   '*(niveau)+'{\n'
      resultat+=indentation(chaine[1:],niveau+1)
   elif chaine[0]=="}":
      resultat+='   '*(niveau-1)+'}\n'
      resultat+=indentation(chaine[1:],niveau-1)

   return resultat
   
def main():
   import sys
   sys.setrecursionlimit(1500)
   accolades=input()
   print(indentation(accolades))
   
main()