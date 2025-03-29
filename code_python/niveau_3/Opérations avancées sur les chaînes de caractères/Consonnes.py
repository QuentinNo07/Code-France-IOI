voyelle="aeiouy"

for i in range(ord("a"), ord("z")+1):
   if not chr(i) in voyelle:
      print(chr(i), end=" ")