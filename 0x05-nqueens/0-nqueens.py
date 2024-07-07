#!/usr/bin/env python3
import sys

def is_safe(board, row, col):
    """ Check if it's safe to place a queen at board[row][col] """

    # Check upper column on the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, col, solutions):
    """ Utility function to solve N queens problem recursively """
    n = len(board)
    if col >= n:
        # Base case: All queens are placed successfully
        solutions.append([[r, c] for r, c in enumerate(board)])
        return True
    
    res = False
    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen
            
            # Recur to place rest of the queens
            res = solve_nqueens_util(board, col + 1, solutions) or res
            
            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0
            
    return res

def solve_nqueens(n):
    """ Main function to solve the N queens problem """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    
    if not solve_nqueens_util(board, 0, solutions):
        return
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    solve_nqueens(N)

