nb_bac, nb_bac_insere = map(int, input().split())
bacs = list(map(int, input().split()))
bac_a_insere = list(map(int, input().split()))

positions = []

for bac in bac_a_insere:
    position = 0
    while position < len(bacs) and bacs[position] < bac:
        position += 1

    positions.append(position)  
    bacs.insert(position, bac)
    
print(' '.join(map(str, positions)))
print(' '.join(map(str, bacs)))
