import math
def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def distance_point_to_segment(px, py, x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    if dx == 0 and dy == 0:
        return distance_between_points(px, py, x1, y1)
    t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)
    if t < 0:
        return distance_between_points(px, py, x1, y1)
    elif t > 1:
        return distance_between_points(px, py, x2, y2)
    else:
        proj_x = x1 + t * dx
        proj_y = y1 + t * dy
        return distance_between_points(px, py, proj_x, proj_y)

x_tower, y_tower = map(int, input().split())
n = int(input())
min_distance = float('inf')
closest_runway = None

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    dist = distance_point_to_segment(x_tower, y_tower, x1, y1, x2, y2)
    
    if dist < min_distance:
        min_distance = dist
        closest_runway = (x1, y1, x2, y2)
print(*closest_runway)