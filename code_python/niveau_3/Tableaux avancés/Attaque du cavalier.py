def knight_can_capture(board):
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    # Find all white knights positions
    white_knights = [(i, j) for i in range(8) for j in range(8) if board[i][j] == 'C']
    
    # Check each white knight's possible moves
    for x, y in white_knights:
        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny].islower():
                return "yes"
    
    return "no"

# Reading the chessboard from input
board = []
for _ in range(8):
    board.append(input().strip())

print(knight_can_capture(board))