import pygame
from l_fonction.constants import *

class Planet:
    def __init__(self, name, radius, distance, texture_path, resource_per_click, auto_farm_cost, specific_resource, resource_name, extractor_upgrade_cost, extractor_upgrade_rate, hull_upgrade_cost, unlock_level):
        self.name = name
        self.radius = radius
        self.distance = distance
        original_texture = pygame.image.load(texture_path).convert_alpha()
        texture_scale_factor = (2 * radius) / max(original_texture.get_width(), original_texture.get_height())
        self.texture = pygame.transform.scale(original_texture, (int(original_texture.get_width() * texture_scale_factor), int(original_texture.get_height() * texture_scale_factor)))
        self.resource_per_click = resource_per_click
        self.resource_count = 0
        self.auto_farm_cost = auto_farm_cost
        self.auto_farm_enabled = False
        self.auto_farm_rate = 8
        self.auto_farm_timer = 0
        self.specific_resource = specific_resource
        self.resource_name = resource_name
        self.auto_farm_button_text = f"Acheter extracteur ({self.auto_farm_cost})"
        self.auto_farm_button_rect = pygame.Rect(10, 190, 300, 50)
        self.extractor_upgrade_cost = extractor_upgrade_cost
        self.extractor_upgrade_rate = extractor_upgrade_rate
        self.extractor_upgraded = False
        self.extractor_upgrade_button_text = f"Améliorer extracteur ({self.extractor_upgrade_cost})"
        self.extractor_upgrade_rect = pygame.Rect(10, 250, 320, 50)
        self.hull_upgrade_cost = hull_upgrade_cost
        self.hull_upgraded = False
        self.hull_upgrade_button_text = f"Améliorer la coque ({self.hull_upgrade_cost})"
        self.hull_upgrade_rect = pygame.Rect(10, 310, 300, 50)
        self.unlock_level = unlock_level


    def draw(self, screen, offset):
        x = self.distance - offset - self.radius
        y = HEIGHT // 2 - self.radius
        screen.blit(self.texture, (x, y))

    def draw_name(self, screen, offset):
        x = self.distance - offset
        y = HEIGHT // 2 + self.radius + 10
        font = pygame.font.Font("./Font/airstrikebold.ttf", 24)
        text_surface = font.render(self.name, True, WHITE)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    def farm_resource(self):
        self.resource_count += self.resource_per_click

    def auto_farm(self):
        if self.auto_farm_enabled:
            self.auto_farm_timer += 1
            if self.auto_farm_timer >= 60:
                self.resource_count += self.auto_farm_rate
                self.auto_farm_timer = 0

    def handle_click(self, pos):
        if self.auto_farm_button_rect.collidepoint(pos):
            if not self.auto_farm_enabled and self.resource_count >= self.auto_farm_cost:
                self.resource_count -= self.auto_farm_cost
                self.auto_farm_enabled = True
                self.auto_farm_button_text = "Extracteur (Activé)"
        elif self.extractor_upgrade_rect.collidepoint(pos):
            if not self.extractor_upgraded and self.resource_count >= self.extractor_upgrade_cost:
                self.resource_count -= self.extractor_upgrade_cost
                self.auto_farm_rate = self.extractor_upgrade_rate
                self.extractor_upgraded = True
                self.extractor_upgrade_button_text = "Extracteur Améliorer"
        return None