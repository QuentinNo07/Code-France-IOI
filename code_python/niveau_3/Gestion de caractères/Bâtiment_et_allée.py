nomAuteur = input()
ageFils = int(input())
batiment = ord(nomAuteur[0]) - ord("A") + 1
allee = chr(ageFils - 1 + ord("A"))
print("{}{}".format(batiment, allee))