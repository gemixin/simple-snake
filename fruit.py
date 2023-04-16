import pygame
import random


class Fruit:
    '''The fruit object that the snake will eat.'''

    def __init__(self, settings, screen, grid_rect):
        '''Initialise the fruit object.'''
        # Store settings, screen and grid_rect objects
        self.settings = settings
        self.screen = screen
        self.grid_rect = grid_rect

    def reset(self):
        '''Reset the the fruit to its starting position.'''
        # Set position (roughly central)
        start_xy = ((self.settings.block_size * self.settings.grid_blocks // 2)
                    + self.grid_rect.x)
        self.pos = (start_xy, start_xy)

    def set_random_pos(self):
        '''Set a random position for the fruit inside the grid (allowing a one
        block-size gap to the egde). Only use increments equal to the block size.'''
        x = random.randrange(self.grid_rect.x + self.settings.block_size,
                             self.grid_rect.width - self.settings.block_size,
                             self.settings.block_size)
        y = random.randrange(self.grid_rect.y + self.settings.block_size,
                             self.grid_rect.height - self.settings.block_size,
                             self.settings.block_size)
        self.pos = (x, y)

    def draw_fruit(self):
        '''Draw the fruit to the screen.'''
        rect = pygame.Rect(self.pos[0], self.pos[1],
                           self.settings.block_size,
                           self.settings.block_size)
        pygame.draw.rect(self.screen, self.settings.fruit_color, rect)
