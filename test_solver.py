import unittest
import solver


class Test_Sudokus(unittest.TestCase):
    def test_easy(self):
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

        solution = [[[8, 5, 9, 3, 1, 7, 4, 6, 2],
                     [7, 4, 3, 9, 6, 2, 8, 1, 5],
                     [2, 1, 6, 8, 5, 4, 7, 9, 3],
                     [6, 2, 5, 7, 9, 1, 3, 8, 4],
                     [9, 7, 4, 6, 3, 8, 5, 2, 1],
                     [1, 3, 8, 2, 4, 5, 6, 7, 9],
                     [5, 6, 7, 4, 2, 9, 1, 3, 8],
                     [4, 8, 2, 1, 7, 3, 9, 5, 6],
                     [3, 9, 1, 5, 8, 6, 2, 4, 7]]
                    ]

        sudoku_solver = solver.Sudoku_Solver(puzzle)
        self.assertEqual(sudoku_solver.solve(), solution)

    def test_hard(self):
        puzzle = [
                  [None, None, None, 5, 6, 8, 4, None, None],
                  [None, 8, 7, None, None, None, 9, None, 5],
                  [None, 5, None, None, None, None, 6, 8, None],
                  [None, None, None, 9, 2, None, None, 7, None],
                  [None, 2, None, None, None, 1, None, None, 9],
                  [8, None, None, None, 7, None, None, None, None],
                  [4, None, None, None, None, 5, None, None, 2],
                  [None, 3, None, None, None, None, None, 6, 4],
                  [None, None, None, 7, 3, None, None, 9, None],
                 ]

        solution = [[[9, 1, 3, 5, 6, 8, 4, 2, 7],
                     [6, 8, 7, 3, 4, 2, 9, 1, 5],
                     [2, 5, 4, 1, 9, 7, 6, 8, 3],
                     [3, 4, 5, 9, 2, 6, 8, 7, 1],
                     [7, 2, 6, 8, 5, 1, 3, 4, 9],
                     [8, 9, 1, 4, 7, 3, 2, 5, 6],
                     [4, 7, 9, 6, 8, 5, 1, 3, 2],
                     [5, 3, 8, 2, 1, 9, 7, 6, 4],
                     [1, 6, 2, 7, 3, 4, 5, 9, 8]
                     ]]

        sudoku_solver = solver.Sudoku_Solver(puzzle)
        self.assertEqual(sudoku_solver.solve(), solution)

    def test_multi_solution(self):
        puzzle = [
                [2, 9, 5, 7, 4, 3, 8, 6, 1],
                [4, 3, 1, 8, 6, 5, 9, None, None],
                [8, 7, 6, 1, 9, 2, 5, 4, 3],
                [3, 8, 7, 4, 5, 9, 2, 1, 6],
                [6, 1, 2, 3, 8, 7, 4, 9, 5],
                [5, 4, 9, 2, 1, 6, 7, 3, 8],
                [7, 6, 3, 5, 2, 4, 1, 8, 9],
                [9, 2, 8, 6, 7, 1, 3, 5, 4],
                [1, 5, 4, 9, 3, 8, 6, None, None],
                    ]

        solution = [[[2, 9, 5, 7, 4, 3, 8, 6, 1],
                    [4, 3, 1, 8, 6, 5, 9, 2, 7],
                    [8, 7, 6, 1, 9, 2, 5, 4, 3],
                    [3, 8, 7, 4, 5, 9, 2, 1, 6],
                    [6, 1, 2, 3, 8, 7, 4, 9, 5],
                    [5, 4, 9, 2, 1, 6, 7, 3, 8],
                    [7, 6, 3, 5, 2, 4, 1, 8, 9],
                    [9, 2, 8, 6, 7, 1, 3, 5, 4],
                    [1, 5, 4, 9, 3, 8, 6, 7, 2]
                     ],
                    [
                    [2, 9, 5, 7, 4, 3, 8, 6, 1],
                    [4, 3, 1, 8, 6, 5, 9, 7, 2],
                    [8, 7, 6, 1, 9, 2, 5, 4, 3],
                    [3, 8, 7, 4, 5, 9, 2, 1, 6],
                    [6, 1, 2, 3, 8, 7, 4, 9, 5],
                    [5, 4, 9, 2, 1, 6, 7, 3, 8],
                    [7, 6, 3, 5, 2, 4, 1, 8, 9],
                    [9, 2, 8, 6, 7, 1, 3, 5, 4],
                    [1, 5, 4, 9, 3, 8, 6, 2, 7]
                    ]
                    ]

        sudoku_solver = solver.Sudoku_Solver(puzzle)
        self.assertEqual(sudoku_solver.solve(), solution)

    def test_no_solution(self):
        puzzle = [
            [2, 9, 5, 7, 4, 3, 8, 6, 1],
            [4, 3, 1, 8, 6, 5, 9, None, None],
            [8, 7, 6, 1, 9, 2, 5, 4, 3],
            [3, 8, 7, 4, 5, 9, 2, 1, 6],
            [6, 1, 2, 3, 8, 7, 4, 2, 2],
            [5, 4, 9, 2, 1, 6, 7, 3, 8],
            [7, 6, 3, 5, 2, 4, 1, 8, 9],
            [9, 2, 8, 6, 7, 1, 3, 5, 4],
            [1, 5, 4, 9, 3, 8, 6, None, None],
                ]

        solution = []

        sudoku_solver = solver.Sudoku_Solver(puzzle)
        self.assertEqual(sudoku_solver.solve(), solution)

    def test_anti_knight(self):
        puzzle = [
            [6, None, None, None, None, None, None, 8, 9],
            [None, None, None, None, None, None, None, None, None],
            [None, None, 1, 2, 3, None, None, None, None],
            [None, None, 4, 5, 6, None, None, None, None],
            [None, None, 7, 8, 9, None, None, None, None],
            [None, None, None, None, None, None, 4, None, None],
            [None, None, None, None, None, 2, None, None, None],
            [3, None, None, None, None, None, None, 1, 2],
            [7, None, None, None, None, None, None, 4, 5],
                ]

        solution = [[[6, 3, 5, 4, 7, 1, 2, 8, 9],
                    [4, 7, 2, 9, 8, 5, 6, 3, 1],
                    [9, 8, 1, 2, 3, 6, 5, 7, 4],
                    [2, 1, 4, 5, 6, 3, 8, 9, 7],
                    [5, 6, 7, 8, 9, 4, 1, 2, 3],
                    [8, 9, 3, 1, 2, 7, 4, 5, 6],
                    [1, 4, 9, 3, 5, 2, 7, 6, 8],
                    [3, 5, 6, 7, 4, 8, 9, 1, 2],
                    [7, 2, 8, 6, 1, 9, 3, 4, 5]]]

        sudoku_solver = solver.Advanced_Sudoku_Solver(puzzle, anti_knight=True)
        self.assertEqual(sudoku_solver.solve(), solution)

    def test_multi_constraint(self):
        puzzle = [
                [None, None, 4, None, None, None, 9, None, None],
                [None, None, None, None, 3, None, None, None, None],
                [8, None, None, None, None, None, None, None, 5],
                [None, None, None, 8, None, 9, None, None, None],
                [None, 9, None, None, 5, None, None, 1, None],
                [None, None, None, 1, None, 2, None, None, None],
                [5, None, None, None, None, None, None, None, 2],
                [None, None, None, None, 7, None, None, None, None],
                [None, None, 1, None, None, None, 6, None, None],
                    ]

        solution = [[[1, 2, 4, 5, 8, 6, 9, 3, 7],
                    [9, 6, 5, 7, 3, 4, 1, 2, 8],
                    [8, 3, 7, 2, 9, 1, 4, 6, 5],
                    [4, 1, 2, 8, 6, 9, 7, 5, 3],
                    [6, 9, 8, 3, 5, 7, 2, 1, 4],
                    [7, 5, 3, 1, 4, 2, 8, 9, 6],
                    [5, 4, 6, 9, 1, 8, 3, 7, 2],
                    [2, 8, 9, 6, 7, 3, 5, 4, 1],
                    [3, 7, 1, 4, 2, 5, 6, 8, 9]],
                    [[3, 2, 4, 5, 8, 1, 9, 7, 6],
                    [9, 6, 5, 7, 3, 4, 1, 2, 8],
                    [8, 1, 7, 2, 9, 6, 4, 3, 5],
                    [1, 4, 2, 8, 6, 9, 7, 5, 3],
                    [6, 9, 8, 3, 5, 7, 2, 1, 4],
                    [7, 5, 3, 1, 4, 2, 8, 6, 9],
                    [5, 7, 6, 4, 1, 8, 3, 9, 2],
                    [2, 8, 9, 6, 7, 3, 5, 4, 1],
                    [4, 3, 1, 9, 2, 5, 6, 8, 7]]]

        sudoku_solver = solver.Advanced_Sudoku_Solver_Improved(
            puzzle,
            anti_knight=True,
            main_diagonals=True)
        self.assertEqual(sudoku_solver.solve(), solution)

    def test_multi_constraint_one_solution(self):
        puzzle = [
                [None, None, 4, None, None, None, 9, None, None],
                [None, None, None, None, 3, None, None, None, None],
                [8, None, None, None, None, None, None, None, 5],
                [None, None, None, 8, None, 9, None, None, None],
                [None, 9, None, None, 5, None, None, 1, None],
                [None, None, None, 1, None, 2, None, None, None],
                [5, None, None, None, None, None, None, None, 2],
                [None, None, None, None, 7, None, None, None, None],
                [None, None, 1, None, None, None, 6, None, None],
                    ]

        solution = [[[1, 2, 4, 5, 8, 6, 9, 3, 7],
                    [9, 6, 5, 7, 3, 4, 1, 2, 8],
                    [8, 3, 7, 2, 9, 1, 4, 6, 5],
                    [4, 1, 2, 8, 6, 9, 7, 5, 3],
                    [6, 9, 8, 3, 5, 7, 2, 1, 4],
                    [7, 5, 3, 1, 4, 2, 8, 9, 6],
                    [5, 4, 6, 9, 1, 8, 3, 7, 2],
                    [2, 8, 9, 6, 7, 3, 5, 4, 1],
                    [3, 7, 1, 4, 2, 5, 6, 8, 9]]]

        sudoku_solver = solver.Advanced_Sudoku_Solver_Improved(
            puzzle,
            anti_knight=True,
            main_diagonals=True)
        self.assertEqual(sudoku_solver.solve(all_solutions=False), solution)

    def test_worst_case_hard(self):
        puzzle = [
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, 9, 8, None, None, None, None],
                [None, None, None, None, None, None, 9, 8, None],
                [None, 9, None, None, None, None, None, None, None],
                [None, None, None, 8, 9, None, None, None, None],
                [None, None, None, None, None, None, 8, 9, None],
                [None, None, 9, None, None, 8, None, None, 7],
                [None, None, None, None, None, 9, None, None, 8],
                [None, None, 8, None, None, 7, None, None, 9]
              ]

        solution = [[[9, 8, 1, 2, 3, 4, 5, 7, 6],
                    [2, 5, 7, 9, 8, 6, 1, 3, 4],
                    [3, 4, 6, 1, 7, 5, 9, 8, 2],
                    [8, 9, 2, 4, 5, 1, 7, 6, 3],
                    [6, 7, 5, 8, 9, 3, 2, 4, 1],
                    [1, 3, 4, 7, 6, 2, 8, 9, 5],
                    [4, 1, 9, 3, 2, 8, 6, 5, 7],
                    [7, 6, 3, 5, 1, 9, 4, 2, 8],
                    [5, 2, 8, 6, 4, 7, 3, 1, 9]]]

        sudoku_solver = solver.Advanced_Sudoku_Solver(puzzle)
        self.assertEqual(sudoku_solver.solve(all_solutions=False), solution)


if __name__ == '__main__':
    unittest.main()
