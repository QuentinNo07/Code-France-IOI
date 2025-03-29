def check_winner(board, N):
    # Vérifier les lignes horizontales et verticales
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                # Check horizontal
                if j <= N - 5 and all(board[i][j + k] == board[i][j] for k in range(5)):
                    return board[i][j]
                # Check vertical
                if i <= N - 5 and all(board[i + k][j] == board[i][j] for k in range(5)):
                    return board[i][j]
                # Check diagonal (top-left to bottom-right)
                if i <= N - 5 and j <= N - 5 and all(board[i + k][j + k] == board[i][j] for k in range(5)):
                    return board[i][j]
                # Check diagonal (top-right to bottom-left)
                if i <= N - 5 and j >= 4 and all(board[i + k][j - k] == board[i][j] for k in range(5)):
                    return board[i][j]
    return 0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    board = []
    index = 1
    for i in range(N):
        row = [int(data[index + j]) for j in range(N)]
        board.append(row)
        index += N
    
    winner = check_winner(board, N)
    print(winner)


main()
