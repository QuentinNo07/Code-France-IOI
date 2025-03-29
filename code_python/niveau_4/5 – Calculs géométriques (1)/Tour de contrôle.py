def main():
    X1, Y1 = map(int, input().split())
    nombre = int(input())
    min_distance = (10000 ** 2) + (10000 ** 2)  
    closest_x, closest_y = 0, 0  
    
    for _ in range(nombre):
        x1, y1 = map(int, input().split())
        distance_curr = (X1 - x1) ** 2 + (Y1 - y1) ** 2

        if distance_curr < min_distance:
            min_distance = distance_curr
            closest_x, closest_y = x1, y1
            
    print(closest_x, closest_y)

main()
