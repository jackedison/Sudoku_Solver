# Advanced Sudoku Solver Algorithm & Sudoku Puzzle Game (Pygame)

This package is a work in progress to experiment with:
1. Sudoku solving algorithms (including advanced variations with more complex rulesets, i.e. anti-chess)
2. Pygame implementation of a playable sudoku game

This package is work in progress.

### TODO:
* Allow user to input their own in pygame (parameter input when calling func)
* Check if unique solution
* Add magic square as constraint to advanced solver
* Consider complexity, worse case O(n) and document
* Make more efficient



# Extras
* Draw rects (blit, display) one at a time rather than recalc and image flip to make it faster: https://stackoverflow.com/questions/34683930/pygame-program-is-running-slow-why
* Allow pencil marks
* ALlow colouring
* Allow user to input custom sudoku (create menu at start?)
* Add graphics for magic square, diagonals, thermo, etc.
* Add timer strikes and notification if user gets square wrong. +15s and highlight in red




# EXTENSIONS OVER A BASIC SUDUKO SOLVER
 1. This code will find **all** possible solutions of the puzzle. It will not stop after finding the first solution.
 2. Allows for solution to more complex sudokus (anti chess constraints, diagonal constraints, etc.)


# Suggested future extensions
1. Additional constraints. Due to OOP nature of this code these can be easily added with a new method to the Advanced_Sudoku_Solver() class.
