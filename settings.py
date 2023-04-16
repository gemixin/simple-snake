import pygame.font


class Settings:
    '''A class to store all settings for Simple Snake.'''

    def __init__(self):
        '''Initialise the game's settings.'''
        # Game speed (fps)
        self.speed = 8

        # Screen setting
        self.bg_color = (0, 171, 169)  # Teal
        self.grid_color = (226, 254, 254)  # Pale Teal
        self.title = 'Simple Snake'

        # Text settings
        self.text_color = (226, 254, 254)  # Pale Teal
        self.score_font = pygame.font.Font('font/handdrawn.ttf', 60)
        self.guide_font = pygame.font.Font('font/handdrawn.ttf', 30)
        self.game_over_font = pygame.font.Font('font/handdrawn.ttf', 72)
        self.button_font = pygame.font.Font('font/handdrawn.ttf', 80)

        # Block size in pixels
        self.block_size = 32

        # Size in blocks of the grid (multiplied by block size to get grid dimensions)
        self.grid_blocks = 12

        # Size in blocks of the border around the grid
        self.border_blocks = 3

        # Snake colors
        self.snake_body_color = (220, 165, 255)  # Green
        self.snake_head_color = (120, 0, 200)  # Dark Green

        # Fruit color
        self.fruit_color = (220, 20, 60)  # Crimson

        # Score
        self.points_per_fruit = 10
