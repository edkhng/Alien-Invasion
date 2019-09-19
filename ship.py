import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start ach new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's poistion based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        # Stop the ship if it moves to the boundary of the screen
        if self.center >= self.ai_settings.screen_width:
            self.moving_right = False

        if self.center <= 0:
            self.moving_left = False

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
