from time import time

start_time = time()
def isSafe(i, j, board):
    for c in range(len(board)):
        for r in range(len(board)):
            if board[c][r] == 'q' and i == c and j != r:
                return False
            elif board[c][r] == 'q' and j == r and i != c:
                return False
            elif (i + j == c + r or i - j == c - r) and board[c][r] == 'q':
                return False
    return True

def nQueens(r, n, board):
    if r == n:
        return True, board

    for i in range(len(board)):
        if isSafe(r, i, board):
            board[r][i] = 'q'

            okay, new_board = nQueens(r + 1, n, board)
            if okay:
                return True, new_board
             
            board[r][i] = '-'
    return False, board

    
def placeNQueens(n, board):
    return nQueens(0, n, board)[1]

def main():
    n = 12
    board = [['-' for _ in range(n)] for _ in range(n)]
    qboard = placeNQueens(n, board)
    qboard = '\n'.join([''.join(x) for x in qboard])
    print(qboard)

main()
end_time = time()
elapsed = end_time - start_time

print(elapsed)
