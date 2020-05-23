# Sudoku taken in as 2d list
import pprint
import copy

import sys


class Sudoku_Solver():
    '''Sudoku solver for basic sudoku iterations. Will return all solutions.'''
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.original_puzzle = copy.deepcopy(self.puzzle)
        self.solutions = []
        self.iterations = []  # Store iterations to solution

    def solve(self, first_run=True, all_solutions=True):
        if first_run:
            self.puzzle = copy.deepcopy(self.original_puzzle)
            self.solutions = []
            self.iterations = []

        if self.solved():
            self.solutions.append(copy.deepcopy(self.puzzle))
            return all_solutions  # To get all solutions or not (could use gen)

        r, c = self.next_empty()

        keep_searching = True  # Set True in case no valids to confirm
        for i in range(1, 10):
            if self.valid(r, c, i):
                # Set equal to i and solve again, return False if no solution
                self.update_puzzle(r, c, i)
                keep_searching = self.solve(first_run=False,
                                            all_solutions=all_solutions)

                if keep_searching is False:  # Don't check rest of loop
                    break

        # Revert the (potentially) changed cell back to None and continue/not
        if keep_searching:
            self.update_puzzle(r, c, None)

        if first_run:
            return self.solutions

        return keep_searching

    def update_puzzle(self, r, c, i):
        self.puzzle[r][c] = i

        self.iterations.append([r, c, i])

    def solved(self):
        for row in self.puzzle:
            if None in row:
                return False
        return True

    def next_empty(self):
        for r, row in enumerate(self.puzzle):
            for c, num in enumerate(row):
                if num is None:
                    return r, c

    def check_row(self, r, i):
        if i in self.puzzle[r]:
            return True
        False

    def check_column(self, c, i):
        for row in self.puzzle:
            if row[c] == i:
                return True
        return False

    def check_box(self, r, c, i):
        # For r and c we have groupings of 012, 345, 678
        # So need to check 3 rows and columns in range
        start_row = r//3*3
        start_col = c//3*3
        for row in self.puzzle[start_row:start_row+3]:
            for ele in row[start_col:start_col+3]:
                if ele == i:
                    return True
        return False

    def valid(self, r, c, i):
        # Check row
        if self.check_row(r, i):
            return False

        # Check column
        if self.check_column(c, i):
            return False

        # Check box
        if self.check_box(r, c, i):
            return False

        # If no issues found return True
        return True


class Advanced_Sudoku_Solver(Sudoku_Solver):
    '''Sudoku solver for more advanced puzzles with extra constraints.'''
    def __init__(self, puzzle, anti_king=False,
                 anti_knight=False, thermometer=False,
                 main_diagonals=False,
                 magic_square=False):
        self.puzzle = puzzle
        self.original_puzzle = copy.deepcopy(self.puzzle)
        self.solutions = []
        self.iterations = []  # Store iterations to solution

        self.anti_king = anti_king
        self.anti_knight = anti_knight
        self.thermometer = thermometer
        self.main_diagonals = main_diagonals
        self.magic_square = magic_square

    def get_cell(self, r, c):
        if r < 0 or r > 8 or c < 0 or c > 8:
            return None
        else:
            return self.puzzle[r][c]

    def check_anti_king(self, r, c, i):
        # Check all squares 1 away from r, c
        king_squares = [self.get_cell(r-1, c-1), self.get_cell(r-1, c),
                        self.get_cell(r-1, c+1), self.get_cell(r, c-1),
                        self.get_cell(r, c+1), self.get_cell(r+1, c-1),
                        self.get_cell(r+1, c), self.get_cell(r+1, c+1)
                        ]
        if i in king_squares:
            return True  # Breaks the constraint

        return False   # Doesn't currently break the constraint

    def check_anti_knight(self, r, c, i):
        # Check all squares knights move away from r, c
        knight_squares = [self.get_cell(r-2, c-1), self.get_cell(r-2, c+1),
                          self.get_cell(r+2, c-1), self.get_cell(r+2, c+1),
                          self.get_cell(r-1, c-2), self.get_cell(r+1, c-2),
                          self.get_cell(r-1, c+2), self.get_cell(r+1, c+2)
                          ]
        if i in knight_squares:
            return True

        return False

    def check_main_diagonals(self, r, c, i):
        # Check top left to bottom right (0, 0 - 1, 1 ... 8, 8)
        if r == c:
            diagonal1 = [self.puzzle[r][c] for i in range(9)]
            if i in diagonal1:
                return False
        # Check bottom left to top right: (0, 8 - 1, 7 - 2, 6 - 3, 5 - 4, 4 ..)
        if r + c == 8:
            diagonal2 = [self.puzzle[i][8-i] for i in range(9)]
            if i in diagonal2:
                return False
        return True

    def check_magic_square(self, r, c, i):
        # Check whether all rows, columns, diagonals of centre square sum to x

        # If middle box not complete then no constraint broken yet so return F
        for row in [3, 4, 5]:  # Middle 3 rows
            if None in self.puzzle[row][3:6]:  # Middle 3 columns
                return False

        # Check 3 rows, 3 columns, 3 diagonals
        s = sum(self.puzzle[3][3:6])
        c1 = c2 = c3 = d1 = d2 = 0
        for row in [3, 4, 5]:  # Check rows and store vals for cols and diags
            if sum(self.puzzle[row][3:6]) != s:
                return True

            c1 += self.puzzle[row][3]
            c2 += self.puzzle[row][4]
            c3 += self.puzzle[row][5]
            d1 += self.puzzle[row][row]
            d2 += self.puzzle[row][8-row]

        if not (s == c1 == c2 == c3 == d1 == d2):
            return True

        return False

    def valid(self, r, c, i):
        # Check all original sudoku constraints with parent method
        if super().valid(r, c, i) is False:
            return False

        # Check kings constraint
        if self.anti_king:
            if self.check_anti_king(r, c, i):
                return False

        # Check knights constraint
        if self.anti_knight:
            if self.check_anti_knight(r, c, i):
                return False

        # Check magic square constraint
        if self.magic_square:
            if self.check_magic_square(r, c, i):
                return False

        # If no issues found return True
        return True


class Advanced_Sudoku_Solver_Improved(Advanced_Sudoku_Solver):
    def next_empty(self):
        # Return the empty cell with the most information (least num valids)
        num_valids = {}
        for r, row in enumerate(self.puzzle):
            for c, num in enumerate(row):
                if num is None:
                    num_valids[(r, c)] = 0
                    for i in range(1, 10):
                        if self.valid(r, c, i):
                            num_valids[(r, c)] += 1

        min_r_c = min(num_valids, key=num_valids.get)
        return min_r_c


if __name__ == "__main__":
    puzzle = [
                  [8, 5, 9, 3, None, 7, 4, 6, 2],
                  [None, 4, None, 9, None, None, 8, None, None],
                  [2, None, None, None, None, 4, None, None, 3],
                  [6, 2, 5, None, None, None, None, 8, 4],
                  [None, None, None, None, 3, 8, None, 2, 1],
                  [None, 3, None, None, None, 5, None, None, None],
                  [None, None, None, 4, None, None, None, None, 8],
                  [None, 8, 2, None, None, None, 9, 5, 6],
                  [None, 9, 1, 5, 8, None, None, None, None],
                 ]

    assert len(puzzle) == 9
    for row in puzzle:
        assert len(row) == 9

    pprint.pprint(puzzle)

    sudoku_solver = Advanced_Sudoku_Solver(puzzle)

    solutions = sudoku_solver.solve()

    pprint.pprint(solutions)

    print('Done!')

    puzzle = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
                ]
