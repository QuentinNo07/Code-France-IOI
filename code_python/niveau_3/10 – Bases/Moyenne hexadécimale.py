def hexadecimal(hex_str, liste):

    nombre_entier = 0
    longueur = len(hex_str)
    for i, valeur in enumerate(hex_str):
        nb = liste.index(valeur)
        nombre_entier += nb * (16 ** (longueur - i - 1))
    return nombre_entier

liste = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


entre = input().strip()
repetition = hexadecimal(entre, liste)

somme = 0
for _ in range(repetition):
    entre = input().strip()
    valeur = hexadecimal(entre, liste)
    somme += valeur


moyenne = somme // repetition
resultat = format(moyenne, 'X')


print(resultat)