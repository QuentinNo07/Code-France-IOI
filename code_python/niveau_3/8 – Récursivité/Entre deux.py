def suite(mini,maxi):
   if maxi==mini:
      print(maxi)
   else:
      print(mini,end=" ")
      suite(mini+1,maxi)

mini,maxi=map(int,input().split())

suite(mini,maxi)