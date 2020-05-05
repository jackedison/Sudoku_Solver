# Implement a sudoku UI using pygame

import pygame  # wrapper for the SDL library
import time


class Grid():
    def __init__(self, window, rows=9, columns=9):
        assert rows == columns  # For now game requires but could adapt
        self.rows = rows
        self.columns = columns
        self.window = window

        self.width, self.height = pygame.display.get_surface().get_size()

        self.box_width = self.width // self.columns
        self.box_height = self.height // self.rows

        pygame.font.init()
        self.font = pygame.font.Font('freesansbold.ttf', 90)


    def draw(self):
        # Draw rows
        for row_num in range(self.rows+1):  # +1 to draw line at bottom
            pygame.draw.line(self.window,  # Window
                             (0, 0, 0),  # Line colour
                             (0, self.box_height*row_num),  # Start coords
                             (self.width, self.box_height*row_num))  # End

        for col_num in range(self.columns+1):
            pygame.draw.line(self.window,
                             (0, 0, 0),
                             (self.box_width*col_num, 0),
                             (self.box_width*col_num, self.height))

    def get_box_coords(self, row, col):
        assert row >= 0 and row < self.rows and col >= 0 and col < self.columns
        '''Return top left and bottom right coords of box_num, 0-8'''
        top_left = (self.box_width * col, self.box_height * row)
        bot_right = (self.box_width * (col + 1), self.box_height * (row + 1))
        return (top_left, bot_right)

    def test_draw_in_box(self, row, col):
        for r in range(row):
            for c in range(col):
                coords = self.get_box_coords(r, c)
                center = ((coords[0][0] + coords[1][0]) // 2,
                          (coords[0][1] + coords[1][1]) // 2)

                # Temp draw circle test
                # pygame.draw.circle(self.window,
                #                   (0, 0, 255),
                #                   center,
                #                   30)

                # TODO seems to be uncentered slightly?
                self.draw_num(str(r+1), center)

    def draw_num(self, num, center):
        textsurf = self.font.render(num, True, (0, 0, 0))

        textrect = textsurf.get_rect()

        textrect.center = (center)

        self.window.blit(textsurf, textrect)





if __name__ == "__main__":
    screen = pygame.display.set_mode(size=(900, 900))

    grid = Grid(screen)

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    grid.draw()
    grid.test_draw_in_box(9, 9)

    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        # Flip the display
        pygame.display.flip()


    pygame.quit()
