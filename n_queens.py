
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True
    
    def solve(board, col):
        if col >= n:
            return True
        
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve(board, col + 1):
                    return True
                board[i][col] = 0
        
        return False
    
    board = [[0] * n for _ in range(n)]
    if solve(board, 0):
        return board
    return None


def main():
    for n in [4, 8]:
        solution = solve_n_queens(n)
        if solution:
            print(f"N-Queens solution for n={n}:")
            for row in solution:
                print(row)
        else:
            print(f"No solution for n={n}")


if __name__ == "__main__":
    main()
