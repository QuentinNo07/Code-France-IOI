def pgdc(a,b):
   while b!=0:
      a, b=b, a%b
   return a
def main():
   l,L=map(int, input().split())
   print(pgdc(l, L))
   
main()