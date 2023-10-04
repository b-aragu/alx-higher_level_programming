#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    # Check the column for conflicts with previously placed queens
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check the upper-left diagonal for conflicts
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check the upper-right diagonal for conflicts
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(["".join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)

    if not solutions:
        print("No solutions found.")
        sys.exit(1)

    for solution in solutions:
        print([[row.index('Q'), row.index('Q')] for row in solution])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
