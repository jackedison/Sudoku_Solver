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

The sudoku in play can be changed by editing it in the **sudoku.json** file.

Solutions will be saved to a generated solutions.json file.

## Controls
* Click on boxes or use arrow keys <kbd>↑</kbd>
<kbd>↓</kbd>
<kbd>→</kbd>
<kbd>←</kbd> to move between cells
* Input numbers with <kbd>1</kbd><kbd>2</kbd><kbd>3</kbd><kbd>4</kbd><kbd>5</kbd><kbd>6</kbd><kbd>7</kbd><kbd>8</kbd><kbd>9</kbd>
* <kbd>DEL</kbd> or <kbd>delete</kbd> to clear cells

* Hold down <kbd>CTRL</kbd> or <kbd>command</kbd> to select multiple cells
* Press <kbd>spacebar</kbd> to see the computer derived solution to the puzzle
* Press <kbd>return</kbd> to run through the algorithm's solution (press again to pause)


## Functionalities
* Will read in a customisable sudoku from the sudoku.json file. This file can be edited by the user.

* Will solve the sudoku. By default when run through the UI the algorithm(s) will stop after the first solution is found. However, if running through terminal simply set `all_solutions=True` to find all solutions, if there are multiple. Solutions will be saved to a solutions.json file.
* Solution can be seen in the UI as well as how the algorithm solved it with keypresses.
* The user may attempt to solve the sudoku themselves through a pygame UI.
* A timer will run allowing the user to speedrun their attempts.
* Incorrect entries will add 15s to the time and highlight the error.
* Advanced sudoku variants can be played and solved for by adjusting paremeters in the sudoku.json file. These include various forms of chess sudoku, magic squares, and diagonals.

## Solving algorithms

The second purpose of this code is to experiment with solving algorithms. Thanks to the UI we can visualise how an algorithm solves a sudoku. This can be enabled by pressing <kbd>return</kbd>.

The original implementation displaying the solving steps in the UI ran the solver as a generator and updated new puzzle yields to the UI. However, this required running the solver twice, once to confirm there is a solution and then a second time to generate the steps. To improve efficiency I have alterred the solving algorithm to store each row/column/element edit for later reference. This has minimal space complexity implications.

### Basic solver
The first implementation is of a basic solving algorithm which will run through each empty cell, checking which numbers could be valid inputs. On finding a valid input it will update the puzzle and move to the next empty cell. Using recursion, if the algorithm reaches a dead-end it will backtrack to the next valid input in its backlog.

<!--Default image size is 900 814-->
<p align="center">
<img src="Graphics/basic_solver.gif" width="450" height="407" />
</p>

This basic algorithm will solve puzzles with a single solution very quickly. **TODO** TO what O(n)? 16 cells required.

, however, its easy to see that for all solutions in worst case (an empty board) it would have time complexity of O(n^n^2) where n is the row/column length. For a 9x9 board this is a rather huge number of 9^81 which would cover all 6.6 sextillion possible solutions to a standard sudoku board.

#### Improvements to the solver: Efficient cell selection
To improve the efficiency of the basic solver we can adjust the order it moves through cells. Instead of moving in a uniform sequence we could check which cells we have the most information for and loop through all their valid entries first.

To implement this its as simple as refactoring the next_empty() method. I created a new class inheriting from the Advanced_Sudoku_Solver() class. This allows us to inherit logic for anti-chess constraints amongst other things.

<!--Default image size is 900 814-->
<p align="center">
<img src="Graphics/basic_solver_improved.gif" width="450" height="407" />
</p>

On most sudokus this will solve without a single penalty - a much more human like approach to solution as well as far more efficient.

This implementation brings down the time it takes to solve the most complex test puzzle (multi constraint with multiple solutions) from 5.424s to 2.177s.

However, for finding just the first solution to the same puzzle the algorithm adjustment actually increases the time from 0.05s to a staggering 1.744s! Although we are now moving through the board much more efficiently, the computation it is taking to figure out efficient movement can drastically exceed the computation required to just move in a more basic path for simple solutions.

Quick test of current test cases shows puzzle layouts of 8 to 11,000. 11,000 9x9 lists in memory is quite a lot (100k), but manageable. Would take a very long time to loop through though for a demonstration so?

#### Improvements to the solver: Dynamic programming using hash tables for valid entries
To reduce the overhead of computing efficient movement we can implement dynamic programming and store valid cell calculations to a hash table. We can now directly update this hash table when checking a new valid number. (Each cell has a set of valid numbers which are updated directly when row, col, or box is updated. This saves full computation of every cell each move. Each recursive function call would have to keep a copy of their hash table.)
**TODO** implement as new class all this stuff probably. Would only work for basic sudoku unless you code in all constraints again to check which cell valids need to be updated..

### **TODO** Write up extra extension to this algorithm - assessing what each cell can and cant be in sets and exploring row and column combinations with that. As an advanced player would do.

### **TODO** any more advanced solving algos computers can do?

### Challenge: can I develop an ML/AI algorithm that can beat my efficient cell selection with dynamic programming solver implementation?

#### (Consider time complexity in more detail)
#### (More solving algorithms, implement some novel ML)
#### Review writing of complexities etc.


## Suggested future extensions
1. Additional constraints. Due to OOP nature of this code these can be easily added with a new method to the Advanced_Sudoku_Solver() class in the solver.py module. Suggestions: tower sudoku, thermometer, quadrant maths.

2. Draw rects (blit, display) one at a time rather than recalculating and image flipping to improve UI snappiness for a human player: https://stackoverflow.com/questions/34683930/pygame-program-is-running-slow-why

3. Improve the UI for human playing with functionality for:
    
    a. Pencil marks (top corner & centre box)

    b. Cell colouring
    
    c. Graphics for any new constraints.

    d. Interactive, customisable ruleset (e.g. adjust penalties in game)

