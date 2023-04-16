import pygame

from settings import Settings
from fruit import Fruit
from snake import Snake
from game_text import GameText


class SimpleSnake:
    '''A simple Snake style game.'''

    def __init__(self):
        '''Initialise the game and settings.'''
        # Initialise PyGame and the clock
        pygame.init()
        self.clock = pygame.time.Clock()

        # Get settings
        self.settings = Settings()

        # Display (square)
        # Multiply the block size by grid size to get playable grid dimensions
        self.grid_size = self.settings.block_size * self.settings.grid_blocks
        # Set the border size
        border_size = self.settings.block_size * self.settings.border_blocks
        # Add a border around the edge for the full game screen (double to allow for a
        # border each side)
        screen_size = self.grid_size + (2 * border_size)
        # Set the screen
        self.screen = pygame.display.set_mode((screen_size, screen_size))
        # Create a rect for the playable grid and position within the border
        self.grid_rect = pygame.Rect(border_size, border_size, self.grid_size,
                                     self.grid_size)

        # Set title
        pygame.display.set_caption(self.settings.title)

        # Create the fruit, snake and game text objects
        self.fruit = Fruit(self.settings, self.screen, self.grid_rect)
        self.snake = Snake(self.settings, self.screen, self.grid_rect)
        self.game_text = GameText(self.settings, self.screen)

        # Load the sounds
        self.eat_sound = pygame.mixer.Sound('sounds/eat.wav')
        self.game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')

        # Set objects to starting states
        self.reset_game()

        # Flag for whether the game is running
        self.running = True

    def reset_game(self):
        '''Reset the objects to their starting states.'''
        # Start with a score of 0
        self.score = 0
        # Set up initial score and guide text
        self.game_text.update_score_text(self.score)
        self.game_text.update_guide_text('Use  the  arrow  keys  to  move  snake')

        # Set snake and fruit to starting positions
        self.snake.reset()
        self.fruit.reset()

        # Set the flag
        self.game_active = True

    def main_loop(self):
        '''The main loop for the game.'''
        while self.running:
            # Listen for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Exit the main game loop
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event.key)

            # Update snake and screen
            if self.game_active:
                self.snake.update()
                self._check_collisions()
                self._check_game_over()

            self._update_screen()

        # When while loop ends
        pygame.quit()

    def _check_keydown_events(self, pressed_key):
        '''Responds to keyboard presses when the game is active and inactive.
        Only respond to arrow keys if not already performing a direction change.
        This stops the snake from being able to very quickly illegally change
        direction.'''
        # If the game is inactive, any key resets the game
        if not self.game_active:
            self.reset_game()
        # If the game is active, handle snake direction changing
        else:
            if not self.snake.changing_direction:
                if pressed_key == pygame.K_UP and self.snake.direction != 'DOWN':
                    self.snake.changing_direction = True
                    self.snake.direction = 'UP'
                if pressed_key == pygame.K_DOWN and self.snake.direction != 'UP':
                    self.snake.changing_direction = True
                    self.snake.direction = 'DOWN'
                if pressed_key == pygame.K_LEFT and self.snake.direction != 'RIGHT':
                    self.snake.changing_direction = True
                    self.snake.direction = 'LEFT'
                if pressed_key == pygame.K_RIGHT and self.snake.direction != 'LEFT':
                    self.snake.changing_direction = True
                    self.snake.direction = 'RIGHT'

    def _check_collisions(self):
        '''Handle collisions between the snake and the fruit.'''
        if self.snake.block_positions[0] == self.fruit.pos:
            # Set the flag so that the next time the snake updates, it doesn't
            # remove the tail. This increases the snake length by 1
            self.snake.eaten_fruit = True
            # Play sound
            pygame.mixer.Sound.play(self.eat_sound)
            # Increase score
            self.score += self.settings.points_per_fruit
            # Update score text
            self.game_text.update_score_text(self.score)
            # Move the fruit to a new position
            _old_pos = self.fruit.pos
            self.fruit.set_random_pos()
            # If the new random position is the same as the old position,
            # generate a new position
            while _old_pos == self.fruit.pos:
                self.fruit.set_random_pos()

    def _check_game_over(self):
        '''Check for game over triggers and set flag is met.'''
        # Out of bounds
        # The x and y positions for the snake head to be considered out of bounds
        out_x = self.grid_rect.width + \
            ((self.settings.border_blocks - 1) * self.settings.block_size)
        out_y = self.grid_rect.height + \
            ((self.settings.border_blocks - 1) * self.settings.block_size)

        if self.snake.block_positions[0][0] < self.grid_rect.x:
            self.game_active = False
        elif self.snake.block_positions[0][0] > out_x:
            self.game_active = False
        elif self.snake.block_positions[0][1] < self.grid_rect.y:
            self.game_active = False
        elif self.snake.block_positions[0][1] > out_y:
            self.game_active = False

        # Snake eating itself
        if self.snake.block_positions[0] in self.snake.block_positions[1:]:
            self.game_active = False

        # If anything triggered game over
        if not self.game_active:
            # Play sound
            pygame.mixer.Sound.play(self.game_over_sound)
            # Update text and set flag
            self.game_text.update_guide_text('Press  any  key  to  play  again')
            self.game_active = False

    def _update_screen(self):
        '''Draw what is displayed on the screen and flip to the new screen.'''
        # Set background color
        self.screen.fill(self.settings.bg_color)

        # Draw the grid rect
        pygame.draw.rect(self.screen, self.settings.grid_color, self.grid_rect)

        # Draw the snake and the fruit (fruit on top of snake)
        self.snake.draw_snake()
        self.fruit.draw_fruit()

        # Draw the game text
        self.game_text.draw_text()
        if not self.game_active:
            self.game_text.draw_game_over_text()

        # Show the screen
        pygame.display.flip()

        # Set max fps
        self.clock.tick(self.settings.speed)


if __name__ == '__main__':
    # Make a game instance and run the game
    snake_game = SimpleSnake()
    snake_game.main_loop()
