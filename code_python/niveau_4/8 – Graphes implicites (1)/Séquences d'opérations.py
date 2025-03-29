from collections import deque
def is_possible(A, B, C, D, N, M):
    if N == M:
        return 1
    MAX_LIMIT = 100000
   
    queue = deque([N])
    
    visited = [False] * (MAX_LIMIT + 1)
    visited[N] = True

    while queue:
        current = queue.popleft()
        next_values = [
            current + A,  
            current - B,  
            current * C  
        ]
        
        if D!=0 and current % D == 0:
            next_values.append(current // D)

        for next_value in next_values:
            if next_value == M:
                return 1
            if 0 <= next_value <= MAX_LIMIT and not visited[next_value]:
                visited[next_value] = True
                queue.append(next_value)
    return 0
    
A, B, C, D = map(int, input().split())
N, M = map(int, input().split())
print(is_possible(A, B, C, D, N, M))