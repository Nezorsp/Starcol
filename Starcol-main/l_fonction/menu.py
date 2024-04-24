import pygame
from l_fonction.constants import *

class Menu:
    def __init__(self, planet, resources, background_image_path):
        self.planet = planet
        self.resources = resources
        self.font = pygame.font.Font(None, 36)
        self.menu_surface = pygame.Surface((WIDTH, HEIGHT))  # Surface du menu de la taille de l'écran
        self.background_image = pygame.image.load(background_image_path).convert()  # Chargement de l'image de fond
        self.menu_surface.blit(self.background_image, (0, 0))  # Appliquer l'image de fond à la surface du menu
        self.menu_rect = self.menu_surface.get_rect(topleft=(0, 0))  # Position du menu en haut à gauche
        self.close_button_rect = pygame.Rect(WIDTH - 50, 10, 40, 40)  # Rectangle du bouton fermer (en haut à droite)
        self.planet_name_rect = pygame.Rect(10, 10, 200, 50)  # Rectangle pour afficher le nom de la planète
        self.resource_rect = pygame.Rect(10, 70, 200, 50)  # Rectangle pour afficher le nom de la ressource
        self.farm_button_rect = pygame.Rect(121, 288, 200, 50)  # Rectangle du bouton "FARM"
        self.auto_farm_button_rect = pygame.Rect(121, 348, 300, 50)  # Rectangle du bouton "Auto Farm"
        self.extractor_upgrade_rect = pygame.Rect(121, 408, 320, 50)  # Rectangle du bouton "Upgrade Extractor"
        self.hull_upgrade_rect = pygame.Rect(121, 800, 300, 50)  # Rectangle du bouton "Upgrade Hull"
        self.planet_rect = pygame.Rect(1250, 125, 500, 500)  # Rectangle pour afficher la planète

    def draw(self, screen):
        screen.blit(self.menu_surface, self.menu_rect)

        planet_image = pygame.transform.scale(self.planet.texture, (900, 900))
        screen.blit(planet_image, self.planet_rect)

        planet_name_text = self.font.render(self.planet.name, True, WHITE)
        planet_name_rect = planet_name_text.get_rect(topleft=(347.6 , 173.1))
        screen.blit(planet_name_text, planet_name_rect)

        resource_text = self.font.render(f"{self.planet.resource_name} : {self.planet.resource_count}", True, WHITE)
        resource_rect = resource_text.get_rect(topleft=(121, 243))
        screen.blit(resource_text, resource_rect)

        pygame.draw.rect(self.menu_surface, GREEN, self.farm_button_rect)
        farm_text = self.font.render("Miner", True, WHITE)
        farm_text_rect = farm_text.get_rect(center=self.farm_button_rect.center)
        self.menu_surface.blit(farm_text, farm_text_rect)

        if not self.planet.auto_farm_enabled:
            pygame.draw.rect(self.menu_surface, GREEN, self.auto_farm_button_rect)
            auto_farm_text = self.font.render(f"Acheter extracteur ({self.planet.auto_farm_cost})", True, WHITE)
            auto_farm_text_rect = auto_farm_text.get_rect(center=self.auto_farm_button_rect.center)
            self.menu_surface.blit(auto_farm_text, auto_farm_text_rect)
        else:
            pygame.draw.rect(self.menu_surface, GRAY, self.auto_farm_button_rect)  # Change la couleur pour indiquer que c'est désactivé
            auto_farm_text = self.font.render("Extracteur (Acheté)", True, BLACK)
            auto_farm_text_rect = auto_farm_text.get_rect(center=self.auto_farm_button_rect.center)
            self.menu_surface.blit(auto_farm_text, auto_farm_text_rect)

        if self.planet.auto_farm_enabled and not self.planet.extractor_upgraded:
            pygame.draw.rect(self.menu_surface, ORANGE, self.extractor_upgrade_rect)
            extractor_upgrade_text = self.font.render(self.planet.extractor_upgrade_button_text, True, BLACK)
            extractor_upgrade_text_rect = extractor_upgrade_text.get_rect(center=self.extractor_upgrade_rect.center)
            self.menu_surface.blit(extractor_upgrade_text, extractor_upgrade_text_rect)
        elif self.planet.extractor_upgraded:
            pygame.draw.rect(self.menu_surface, GRAY, self.extractor_upgrade_rect)
            extractor_upgrade_text = self.font.render("Extractor Upgraded", True, BLACK)
            extractor_upgrade_text_rect = extractor_upgrade_text.get_rect(center=self.extractor_upgrade_rect.center)
            self.menu_surface.blit(extractor_upgrade_text, extractor_upgrade_text_rect)

        pygame.draw.rect(self.menu_surface, RED, self.close_button_rect)
        close_text = self.font.render("X", True, WHITE)
        close_text_rect = close_text.get_rect(center=self.close_button_rect.center)
        self.menu_surface.blit(close_text, close_text_rect)

        if not self.planet.hull_upgraded:
            pygame.draw.rect(self.menu_surface, ORANGE, self.hull_upgrade_rect)
            hull_upgrade_text = self.font.render(self.planet.hull_upgrade_button_text, True, BLACK)
            hull_upgrade_text_rect = hull_upgrade_text.get_rect(center=self.hull_upgrade_rect.center)
            self.menu_surface.blit(hull_upgrade_text, hull_upgrade_text_rect)
        elif self.planet.hull_upgraded:
            pygame.draw.rect(self.menu_surface, GRAY, self.hull_upgrade_rect)
            hull_upgrade_text = self.font.render("Coque Amélioré", True, BLACK)
            hull_upgrade_text_rect = hull_upgrade_text.get_rect(center=self.hull_upgrade_rect.center)
            self.menu_surface.blit(hull_upgrade_text, hull_upgrade_text_rect)

    def handle_click(self, pos):
        global niveau_vaisseau
        if self.close_button_rect.collidepoint(pos):
            return "CLOSE"
        elif self.farm_button_rect.collidepoint(pos):
            self.planet.farm_resource()
        elif self.auto_farm_button_rect.collidepoint(pos):
            if not self.planet.auto_farm_enabled and self.planet.resource_count >= self.planet.auto_farm_cost:
                self.planet.resource_count -= self.planet.auto_farm_cost
                self.planet.auto_farm_enabled = True
                self.planet.auto_farm_button_text = "Auto Farm (Enabled)"
        elif self.extractor_upgrade_rect.collidepoint(pos):
            if not self.planet.extractor_upgraded and self.planet.resource_count >= self.planet.extractor_upgrade_cost:
                self.planet.resource_count -= self.planet.extractor_upgrade_cost
                self.planet.auto_farm_rate = self.planet.extractor_upgrade_rate
                self.planet.extractor_upgraded = True
                self.planet.extractor_upgrade_button_text = "Extractor Upgraded"
        elif self.hull_upgrade_rect.collidepoint(pos):
            if not self.planet.hull_upgraded and self.planet.resource_count >= self.planet.hull_upgrade_cost:
                self.planet.resource_count -= self.planet.hull_upgrade_cost
                self.planet.hull_upgraded = True
                niveau_vaisseau += 1;
                self.planet.hull_upgrade_button_text = "Hull Upgraded"
            return None
