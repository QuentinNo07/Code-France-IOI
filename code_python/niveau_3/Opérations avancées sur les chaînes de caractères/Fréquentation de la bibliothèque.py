somme=0

while True:
   try:
      ligne=input()
      nombre=map(int, ligne.split())
      somme+=sum(nombre)
   except:
      break

print(somme)