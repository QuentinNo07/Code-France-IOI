import sys
def main():
    n = int(sys.stdin.readline().strip()) 
    resultat = 1
    for _ in range(n):
        nb = int(sys.stdin.readline().strip()) 
        resultat *= nb
        resultat %= 10000
    print("{:04d}".format(resultat)) 
main()