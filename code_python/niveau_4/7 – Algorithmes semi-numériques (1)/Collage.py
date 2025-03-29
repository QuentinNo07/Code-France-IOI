def ppcm(l,L):
   def pgcd(a,b):
      while b!=0:
         a, b=b, a%b
      return a
      
   return abs(l*L)//pgcd(l,L)
def main():
   l,L=map(int, input().split())
   print(ppcm(l, L))
   
main()