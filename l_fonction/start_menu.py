import pygame
from l_fonction.constants import *

class StartMenu:
    def __init__(self):
        self.font = pygame.font.Font("Font/airstrikebold.ttf", 36)
        self.title_font = pygame.font.Font("Font/Dune_Rise.otf", 200)
        self.menu_surface = pygame.Surface((WIDTH, HEIGHT))
        self.background_image = pygame.image.load("texture/Fond.png").convert()
        self.menu_surface.blit(self.background_image, (0, 0))
        self.menu_rect = self.menu_surface.get_rect(topleft=(0, 0))
        self.title_text = self.title_font.render("Starcol", True, WHITE)
        self.title_rect = self.title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        self.play_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 200, 200, 50)
        self.quit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 270, 200, 50)

    def draw(self, screen):
        screen.blit(self.menu_surface, self.menu_rect)

        screen.blit(self.title_text, self.title_rect)

        pygame.draw.rect(screen, GREEN, self.play_button_rect)
        play_text = self.font.render("Jouer", True, WHITE)
        play_text_rect = play_text.get_rect(center=self.play_button_rect.center)
        screen.blit(play_text, play_text_rect)

        pygame.draw.rect(screen, RED, self.quit_button_rect)
        quit_text = self.font.render("Quitter", True, WHITE)
        quit_text_rect = quit_text.get_rect(center=self.quit_button_rect.center)
        screen.blit(quit_text, quit_text_rect)

    def handle_click(self, pos):
        if self.play_button_rect.collidepoint(pos):
            return "PLAY"
        elif self.quit_button_rect.collidepoint(pos):
            return "QUIT"
        else:
            return None