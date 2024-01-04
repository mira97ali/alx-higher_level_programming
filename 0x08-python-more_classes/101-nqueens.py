#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


class NQueens:
    def __init__(self, n):
        """Initialize an `N x N` chessboard"""
        self.board = [[' ' for _ in range(n)] for _ in range(n)]

    def temporary_board(self, original_board):
        """
        Create a temporary chessboard.

        Args:
            original_board (list): The original chessboard to be copied.

        Returns:
            list: A deep copy of the provided chessboard.
        """
        if isinstance(original_board, list):
            return list(map(self.temporary_board, original_board))
        return original_board

    def find_queen_positions(self, chessboard):
        """
        Find and return the positions of queens on a chessboard.

        Parameters:
        - chessboard (list): The list of lists representation of a chessboard.

        Returns:
        - list: List of lists of positions of queens format [row, column].
        """
        queen_positions = []
        for row in range(len(chessboard)):
            for col in range(len(chessboard)):
                if chessboard[row][col] == "Q":
                    queen_positions.append([row, col])
                    break
        return queen_positions

    def mark_attacked_positions(self, chessboard, row, column):
        """
        Mark all spots on a chessboard where
        non-attacking queens can no longer be played.

        Args:
            chessboard (list): The current working chessboard.
            row (int): The row where a queen was last played.
            column (int): The column where a queen was last played.
        """
        for c in range(column + 1, len(chessboard)):
            chessboard[row][c] = "x"

        for c in range(column - 1, -1, -1):
            chessboard[row][c] = "x"

        for r in range(row + 1, len(chessboard)):
            chessboard[r][column] = "x"

        for r in range(row - 1, -1, -1):
            chessboard[r][column] = "x"

        c = column + 1
        for r in range(row + 1, len(chessboard)):
            if c >= len(chessboard):
                break
            chessboard[r][c] = "x"
            c += 1

        c = column - 1
        for r in range(row - 1, -1, -1):
            if c < 0:
                break
            chessboard[r][c]
            c -= 1

        c = column + 1
        for r in range(row - 1, -1, -1):
            if c >= len(chessboard):
                break
            chessboard[r][c] = "x"
            c += 1

        c = column - 1
        for r in range(row + 1, len(chessboard)):
            if c < 0:
                break
            chessboard[r][c] = "x"
            c -= 1

    def solve_n_queens_recursive(
        self,
        chessboard,
        current_row,
        placed_queens,
        solution_list
    ):
        """
        Recursively solve an N-queens puzzle.

        Args:
        - chessboard (list): The current working chessboard.
        - current_row (int): The current working row.
        - placed_queens (int): The current number of placed queens.
        - solution_list (list): A list of lists representing solutions.

        Returns:
        - list: The updated list of solutions.
        """
        if placed_queens == len(chessboard):
            solution_list.append(self.find_queen_positions(chessboard))
            return solution_list

        for col in range(len(chessboard)):
            if chessboard[current_row][col] == " ":
                temp_board = self.temporary_board(chessboard)
                temp_board[current_row][col] = "Q"
                self.mark_attacked_positions(temp_board, current_row, col)
                solution_list = self.solve_n_queens_recursive(
                    temp_board,
                    current_row + 1,
                    placed_queens + 1,
                    solution_list
                )

        return solution_list


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens = NQueens(n=int(sys.argv[1]))
    solutions = nqueens.solve_n_queens_recursive(nqueens.board, 0, 0, [])
    for sol in solutions:
        print(sol)
