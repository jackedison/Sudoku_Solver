# Advanced Sudoku Solver Algorithm & Sudoku Puzzle Game (Pygame)

This package is a work in progress to experiment with:
1. Pygame implementation of a playable sudoku game
2. Various sudoku solving algorithms and analysis of their efficiency/complexity. This includes solvers to advanced variants of sudoku (i.e. anti-chess)

## Setup

In terminal (mac) or command prompt (windows) clone the repository with:
* `git clone https://github.com/jackedison/Sudoku_Solver`

Then change directory to the cloned repository:
* `cd Sudoku_Solver`

### To run

Once cloned to a local repository, simply run `python UI.py` to play the sudoku in a pygame interface.

The sudoku in play can be changed by editing it in the sudoku.json file.

Solutions will be savedto a generated solutions.json file.

## Controls
* Click on boxes or use arrow keys <kbd>↑</kbd>
<kbd>↓</kbd>
<kbd>→</kbd>
<kbd>←</kbd> to move between cells
* Input numbers with <kbd>1</kbd><kbd>2</kbd><kbd>3</kbd><kbd>4</kbd><kbd>5</kbd><kbd>6</kbd><kbd>7</kbd><kbd>8</kbd><kbd>9</kbd>
* <kbd>DEL</kbd> or <kbd>delete</kbd> to clear cells

* Hold down <kbd>CTRL</kbd> or <kbd>command</kbd> to select multiple cells
* Press <kbd>spacebar</kbd> for the computer to solve the sudoku


## Functionalities
* Will read in a customisable sudoku from the sudoku.json file. This file can be edited by the user.

* Will solve the sudoku finding **all** possible solutions. Solutions will be saved to a solutions.json file.
* The user may attempt to solve the sudoku themselves through a pygame UI.
* A timer will run allowing the user to speedrun their attempts.
* Incorrect entries will add 15s to the time and highlight the error.
* Advanced sudoku variants can be played and solved for by adjusting paremeters in the sudoku.json file. These include various forms of chess sudoku, magic squares, and diagonals.

## Solving algorithms

The second purpose of this software is to enable a real world use case to apply machine learning algorithms to. Using the UI we can visualise how an algorithm would solve a sudoku.

**TODO** Show solving thought process by pressing enter

### Basic solver
The basic solving algorithm will run through each empty cell. For each cell it will check which numbers could be valid inputs to the cell. Using recursion it will try each number and continue through the board. If it reaches a cell with no valid inputs it will work backwards to the last cell with another valid entry.

This algorithm will solve most puzzles instantly, however, its easy to see that for all solutions in worst case (an empty board) it would have time complexity of O(n^n^2) where n is the row/column length. For a 9x9 board this is a rather huge number of 9^81 which would cover all 6.6 sextillion possible solutions to a standard sudoku board.

### Improvements to the basic solver
To improve the efficiency of the basic solver we can adjust the order it moves across the board. Instead of moving in a uniform sequence we could select the cells we have most information about first.


#### (Consider time complexity in more detail)
#### (More solving algorithms, implement some novel ML)


## Suggested future extensions
1. Additional constraints. Due to OOP nature of this code these can be easily added with a new method to the Advanced_Sudoku_Solver() class in the solver.py module. Suggestions: tower sudoku, thermometer, quadrant maths.

2. Draw rects (blit, display) one at a time rather than recalculating and image flipping to improve UI snappiness: https://stackoverflow.com/questions/34683930/pygame-program-is-running-slow-why

3. Improveplayable UI by adding:
    
    a. Pencil marks (top corner & centre box)
    b. Cell colouring
    c. Graphics for any new constraints.
    d. Interactive, customisable ruleset (e.g. adjust penalties in game)
