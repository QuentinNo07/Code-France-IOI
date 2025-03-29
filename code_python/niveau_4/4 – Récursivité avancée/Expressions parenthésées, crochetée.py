def verification(phrase,index=0, liste=None):
   if liste is None:
      liste=[] 
      
   if index>=len(phrase):
      return len(liste)==0

   char=phrase[index]
   if char in "({[<":
      liste.append(char)
   elif char in ")}]>":
      if not liste:
         return False
      dernier_ouvert=liste.pop()
      if (dernier_ouvert == '(' and char != ')') or \
         (dernier_ouvert == '[' and char != ']') or \
         (dernier_ouvert == '{' and char != '}') or \
         (dernier_ouvert == '<' and char != '>'):
            return False
   return verification(phrase, index + 1, liste)
   
def main():
   phrase=input()

   if verification(phrase):
      print("yes")
   else:
      print("no")
      
main()