import sys
import bisect

def find_closest_density(densities, query):
    pos = bisect.bisect_left(densities, query)
    
    closest = None
    
    if pos < len(densities):
        closest = densities[pos]
    
    if pos > 0:
        prev_density = densities[pos - 1]
        if closest is None or abs(prev_density - query) < abs(closest - query) or \
           (abs(prev_density - query) == abs(closest - query) and prev_density < closest):
            closest = prev_density
            
    return closest

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    
    # Lire le nombre de blocs de plastique
    N = int(data[index])
    index += 1
    
    # Lire les densités des blocs de plastique
    densities = list(map(int, data[index:index + N]))
    index += N
    
    # Trier les densités pour permettre une recherche binaire
    densities.sort()
    
    # Lire le nombre de questions
    Q = int(data[index])
    index += 1
    
    results = []
    
    # Lire les questions et déterminer la densité la plus proche pour chaque question
    for _ in range(Q):
        query = int(data[index])
        index += 1
        closest_density = find_closest_density(densities, query)
        results.append(str(closest_density))
    
    # Afficher les résultats
    print("\n".join(results))

if __name__ == "__main__":
    main()
