import pygame


class GameText:
    '''The various game text used in the game.'''

    def __init__(self, settings, screen):
        '''Initialise the game text object.'''
        # Store settings and screen objects
        self.settings = settings
        self.screen = screen

        # Create game over text image and rect
        self.game_over_image = self.settings.game_over_font.render(
            'Game  Over',
            True, self.settings.text_color, self.settings.bg_color)
        self.game_over_rect = self.game_over_image.get_rect()
        # Position on screen
        self.game_over_rect.center = self.screen.get_rect().center
        # Create a background rect for the game over text
        self.game_over_bg = pygame.Rect(0, 0, self.game_over_rect.width + 20,
                                        self.game_over_rect.height + 20)
        # Position on screen
        self.game_over_bg.center = self.screen.get_rect().center

    def update_guide_text(self, text):
        '''Update the guide text in the top left of the screen with relevant text.'''
        # Create guide text image and rect
        self.guide_image = self.settings.guide_font.render(
            text, True, self.settings.text_color, self.settings.bg_color)
        self.guide_rect = self.guide_image.get_rect()
        # Position on screen
        self.guide_rect.top = 10
        self.guide_rect.left = 10

    def update_score_text(self, score):
        '''Update the score text in the top right of the screen with current score.'''
        # Create score text image and rect
        self.score_image = self.settings.score_font.render(
            str(score), True, self.settings.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        # Position on screen
        self.score_rect.top = -20
        self.score_rect.right = self.screen.get_rect().right - 10

    def draw_text(self):
        '''Draw the score and guide text to the screen.'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.guide_image, self.guide_rect)

    def draw_game_over_text(self):
        '''Draw the game over text and background to the screen.'''
        pygame.draw.rect(self.screen, self.settings.bg_color, self.game_over_bg)
        self.screen.blit(self.game_over_image, self.game_over_rect)
