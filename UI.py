# Implement a sudoku UI using pygame

import pygame  # wrapper for the SDL library
import time
import copy
import json  # to read json sudoku from file

import solver


class Grid():
    def __init__(self, window, rows=9, columns=9):
        assert rows == columns  # For now game requires but could adapt

        self.rows = rows
        self.columns = columns
        self.window = window

        self.width, self.height = pygame.display.get_surface().get_size()
        self.height -= (rows*10)

        self.box_width = self.width // self.columns
        self.box_height = self.height // self.rows

        self.selected_boxes = []

        self.wl = 3  # Width of wide line
        self.nl = 1  # Width of narrow line

        # Puzzle (read in from json)
        self.puzzle, self.constraints = read_sudoku_json()

        self.original_puzzle = copy.deepcopy(self.puzzle)

        # Solve and store the solution of the puzzle for future referal
        sudoku_solver = solver.Advanced_Sudoku_Solver(
            self.puzzle,
            anti_king=self.constraints['anti_king'],
            anti_knight=self.constraints['anti_knight'],
            main_diagonals=self.constraints['main_diagonals'],
            magic_square=self.constraints['magic_square']
            )

        self.solutions = sudoku_solver.solve()
        assert len(self.solutions) > 0  # No solutions exist to sudoku in .json
        print('This sudoku has {} solution(s)'.format(len(self.solutions)))
        with open('solutions.json', 'w+') as file:  # Save solutions to JSON
            json.dump({'solutions': self.solutions}, file)
        self.solution = self.solutions[0]  # Assume 1 solution

        # Draw surface:
        # Initialise font
        pygame.font.init()
        self.font = pygame.font.Font(None, 90)
        self.font_time = pygame.font.Font(None, 70)

        # Fill the background with white
        self.window.fill((255, 255, 255))

        # Draw lines & numbers
        self.draw()
        self.draw_all_nums()

        # Set number of mistakes to adjust timer by
        self.mistakes = 0

        # Start timer
        self.start_time = time.time()
        self.update_timer()

    def draw(self):
        # Draw rows
        for row_num in range(self.rows+1):  # +1 to draw line at bottom
            linewidth = self.wl if row_num % 3 == 0 else self.nl
            pygame.draw.line(self.window,  # Window
                             (0, 0, 0),  # Line colour
                             (0, self.box_height*row_num),  # Start coords
                             (self.width, self.box_height*row_num),  # End
                             linewidth)  # Line width

        for col_num in range(self.columns+1):
            linewidth = self.wl if col_num % 3 == 0 else self.nl
            pygame.draw.line(self.window,
                             (0, 0, 0),
                             (self.box_width*col_num, 0),
                             (self.box_width*col_num, self.height),
                             linewidth)

    def get_box_coords(self, row, col):
        '''Return top left and bottom right coords of box_num, 0-8'''
        assert row >= 0 and row < 9 and col >= 0 and col < 9

        top_left = (self.box_width * col, self.box_height * row)
        bot_right = (self.box_width * (col + 1), self.box_height * (row + 1))
        return (top_left, bot_right)

    def draw_all_nums(self, row=9, col=9):
        for r in range(row):
            for c in range(col):
                if self.puzzle[r][c] is not None:
                    self.draw_num(r, c)

    def draw_num(self, row, col):
        '''Row and col as index (i.e. 0-8 not 1-9)'''
        # Get number to write in
        num = str(self.puzzle[row][col])

        # Get coords of box on window to write number in
        coords = self.get_box_coords(row, col)
        center = ((coords[0][0] + coords[1][0]) // 2,
                  (coords[0][1] + coords[1][1]) // 2)

        # Colour dependent on hard coded, right, or wrong
        if self.original_puzzle[row][col] is not None:  # Hard coded
            colour = (0, 0, 0)
        elif self.puzzle[row][col] == self.solution[row][col]:  # Correct
            colour = (0, 0, 255)
        else:  # Incorrect
            colour = (255, 0, 0)

        textsurf = self.font.render(num, True, colour)

        # Text doesn't center on y axis for some reason so slight adjustment
        center = (center[0], center[1]+(self.box_height//15))
        textrect = textsurf.get_rect(center=center)

        self.window.blit(textsurf, textrect)

    def shade_box(self, row, col, colour=(255, 255, 0)):
        coords = self.get_box_coords(row, col)

        # Line width (lw if col is 0, 3, 6)
        lw = self.wl if col % 3 == 0 else self.nl
        tw = self.wl if row % 3 == 0 else self.nl
        rw = lw + (self.wl/2 if (col + 1) % 3 == 0 else self.nl/2)
        bw = tw + (self.wl/2 if (row + 1) % 3 == 0 else self.nl/2)

        rect = pygame.Rect(coords[0][0]+lw, coords[0][1]+tw,  # Left, Top
                           self.box_width-rw, self.box_height-bw)  # W / H

        self.window.fill(colour, rect)

        if self.puzzle[row][col] is not None:
            self.draw_num(row, col)

    def get_rect(self, coords):
        '''Get rectangle the mouse has clicked on'''
        # Will be // divisor of box height and row height
        col = coords[0] // self.box_width
        row = coords[1] // self.box_height
        return row, col

    def select_box_coords(self, coords, unselect):
        if unselect:
            self.unselect_all()

        # If not out of bounds then select
        if coords[0] <= self.width and coords[1] <= self.height:
            row, col = self.get_rect(coords)
            self.select_box(row, col)

    def select_box_arrow(self, direction, unselect):
        last_selected = self.selected_boxes[-1]

        if unselect:
            self.unselect_all()

        row, col = last_selected

        if direction == 'UP':
            row = (row - 1) % 9
        elif direction == 'DOWN':
            row = (row + 1) % 9
        elif direction == 'RIGHT':
            col = (col + 1) % 9
        elif direction == 'LEFT':
            col = (col - 1) % 9
        else:
            raise KeyError('Arrow key error')

        self.select_box(row, col)

    def select_box(self, row, col):
        if [row, col] not in self.selected_boxes:
            self.shade_box(row, col)

            self.selected_boxes.append([row, col])

    def unselect_all(self):
        for row, col in self.selected_boxes:
            self.shade_box(row, col, colour=(255, 255, 255))
        self.selected_boxes = []

    def input_number(self, num):
        for row, col in self.selected_boxes:
            if self.original_puzzle[row][col] is None:  # Don't change original
                if self.puzzle[row][col] is not None:  # If num already clear
                    self.clear_cell(row, col)

                # Set new numbers
                self.puzzle[row][col] = num

                # Check if number is correct, if not colour red and + mistake
                if self.puzzle[row][col] != self.solution[row][col]:
                    self.mistakes += 1

                self.draw_num(row, col)

    def check_complete(self):
        # Check if puzzle complete
        for row in self.puzzle:
            if None in row:
                break
        else:
            # Check if solution is correct
            if self.puzzle in self.solutions:
                self.display_solved(True)
                return True
            else:
                self.display_solved(False)

        return False

    def clear_cell(self, row, col):
        self.puzzle[row][col] = None
        self.shade_box(row, col)

    def clear_cells(self):
        for row, col in self.selected_boxes:
            self.clear_cell(row, col)

    def update_timer(self):
        # Clear old timer
        left, top = 20, 835
        screen.fill((255, 255, 255), (left, top, 450-left, 900-top))

        # Draw timer to bottom of the screen
        new_time = int(time.time() - self.start_time)
        new_time += (15 * self.mistakes)  # Add 15s per mistake

        string = 'Time: {:02.0f}:{:02.0f}'.format(new_time//60, new_time % 60)

        text = self.font_time.render(string, True, (116, 164, 181))
        self.window.blit(text, (left, top))

    def solve(self):
        # Function to solve based on original analysis of solution
        for r, row in enumerate(self.solution):
            for c, ele in enumerate(row):
                if self.puzzle[r][c] is None:
                    self.unselect_all()
                    self.select_box(r, c)
                    self.input_number(ele)

        self.unselect_all()

    def display_solved(self, solved):
        # Clear any old text
        left, top = 450, 835
        screen.fill((255, 255, 255), (left, top, 900-left, 900-top))

        # Draw solved
        if solved:
            string = 'Solved!'
            colour = (52, 199, 71)
        else:
            string = 'Wrong solution'
            colour = (199, 52, 71)

        text = self.font_time.render(string, True, colour)
        self.window.blit(text, (left, top))


def read_sudoku_json():
    with open('sudoku.json') as file:
        sudoku = json.load(file)
    puzzle = sudoku['sudoku']

    constraints = sudoku
    del(constraints['sudoku'])

    # Assert puzzle is valid
    assert len(puzzle) == 9
    for row in puzzle:
        assert len(row) == 9

    return puzzle, constraints


if __name__ == "__main__":
    screen = pygame.display.set_mode(size=(900, 900))

    grid = Grid(screen)

    # Run game and log user actions
    running = True
    solved = False
    while running and not solved:
        keys = pygame.key.get_pressed()  # To check if ctrl is pressed
        clicks = pygame.mouse.get_pressed()  # To check if click held down

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN:
                # Number inputs (more readable like this than dic)
                if event.key == pygame.K_1:
                    grid.input_number(1)
                if event.key == pygame.K_2:
                    grid.input_number(2)
                if event.key == pygame.K_3:
                    grid.input_number(3)
                if event.key == pygame.K_4:
                    grid.input_number(4)
                if event.key == pygame.K_5:
                    grid.input_number(5)
                if event.key == pygame.K_6:
                    grid.input_number(6)
                if event.key == pygame.K_7:
                    grid.input_number(7)
                if event.key == pygame.K_8:
                    grid.input_number(8)
                if event.key == pygame.K_9:
                    grid.input_number(9)

                # Delete key
                if (event.key == pygame.K_BACKSPACE or  # Windows
                      event.key == pygame.K_DELETE):  # Mac
                    grid.clear_cells()

                # Arrow keys
                if event.key == pygame.K_UP:
                    if keys[pygame.K_LCTRL] or keys[pygame.K_LMETA]:
                        grid.select_box_arrow('UP', unselect=False)
                    else:
                        grid.select_box_arrow('UP', unselect=True)
                if event.key == pygame.K_DOWN:
                    if keys[pygame.K_LCTRL] or keys[pygame.K_LMETA]:
                        grid.select_box_arrow('DOWN', unselect=False)
                    else:
                        grid.select_box_arrow('DOWN', unselect=True)
                if event.key == pygame.K_RIGHT:
                    if keys[pygame.K_LCTRL] or keys[pygame.K_LMETA]:
                        grid.select_box_arrow('RIGHT', unselect=False)
                    else:
                        grid.select_box_arrow('RIGHT', unselect=True)
                if event.key == pygame.K_LEFT:
                    if keys[pygame.K_LCTRL] or keys[pygame.K_LMETA]:
                        grid.select_box_arrow('LEFT', unselect=False)
                    else:
                        grid.select_box_arrow('LEFT', unselect=True)

                # Space key
                if (event.key == pygame.K_SPACE):
                    grid.solve()

            if event.type == pygame.MOUSEBUTTONDOWN or clicks[0]:
                coords = pygame.mouse.get_pos()

                if keys[pygame.K_LCTRL] or keys[pygame.K_LMETA] or clicks[0]:
                    grid.select_box_coords(coords, unselect=False)
                else:
                    grid.select_box_coords(coords, unselect=True)

        grid.update_timer()

        # Check if solved
        solved = grid.check_complete()

        # Flip the display (make more responsive by not updating whole screen)
        pygame.display.flip()

    if solved:  # Stops timer, printed complete msg and stop user input
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

    pygame.quit()
    exit()  # To exit python interpreter in vscode
