def main():
   nb_quantite, qRecherche= map(int,input().split())
   quantites=list(map(int,input().split()))
   vues=set()
   for quantite in quantites:
      if quantite*2 == qRecherche:
         return True
      if qRecherche-quantite in vues:
         return True
      vues.add(quantite)
   return False

print("OUI" if main() else "NON")