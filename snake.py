import pygame


class Snake():
    '''The snake object that the player controls.'''

    def __init__(self, settings, screen, grid_rect):
        '''Initialise the snake object.'''
        # Store settings, screen and grid_rect objects
        self.settings = settings
        self.screen = screen
        self.grid_rect = grid_rect

    def reset(self):
        '''Reset the the snake to its starting position.'''
        # Positions for each block in the snake
        # Creates a list with 3 tuples of positions for the initial 3 blocks
        # This positions the snake facing to the right in the top left corner
        # (with a one block size margin from the edge)
        self.block_positions = [
            (i * self.settings.block_size + self.grid_rect.x,
             self.settings.block_size + self.grid_rect.x)
            for i in range(3, 0, -1)
        ]

        # The direction the snake is moving
        self.direction = 'NONE'

        # Flag for whether the snake has just eaten the fruit or not
        self.eaten_fruit = False

        # Flag for whether the snake is changing direction or not
        self.changing_direction = False

    def update(self):
        '''Move the snake according to the current direction by adding a new block for
        the head in the new position, and removing the last block (the tail) to simulate
        movement.'''
        # At the start of the game, we don't move the snake
        if self.direction != 'NONE':
            # Start with the current head position
            x = self.block_positions[0][0]
            y = self.block_positions[0][1]
            # Add/subtract the block size to/from x or y depending on direction
            if self.direction == 'UP':
                y -= self.settings.block_size
            if self.direction == 'DOWN':
                y += self.settings.block_size
            if self.direction == 'LEFT':
                x -= self.settings.block_size
            if self.direction == 'RIGHT':
                x += self.settings.block_size
            # Add the new block to the head of the list
            self.block_positions.insert(0, (x, y))

            # Delete the last block in the list unless the fruit has just been eaten
            if not self.eaten_fruit:
                self.block_positions.pop()

            # Reset the flags
            self.eaten_fruit = False
            self.changing_direction = False

    def draw_snake(self):
        '''Draw each block of the snake to the screen.'''
        for index, pos in enumerate(self.block_positions):
            rect = pygame.Rect(pos[0], pos[1],
                               self.settings.block_size,
                               self.settings.block_size)
            # Head is a different colour to the rest of the snake
            if index == 0:
                color = self.settings.snake_head_color
            else:
                color = self.settings.snake_body_color
            # Draw to screen
            pygame.draw.rect(self.screen, color, rect)
