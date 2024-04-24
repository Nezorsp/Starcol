import pygame
import sys
from l_fonction.start_menu import StartMenu
from l_fonction.planet import Planet
from l_fonction.menu import Menu
from l_fonction.constants import *

pygame.init()


pygame.mixer.music.load("sound/Musique_fond.mp3")
pygame.mixer.music.play(-1)

def initialize_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Système Solaire")

    background_image = pygame.image.load("texture/fond.png").convert()

    niveaux_requis = {planet_name: unlock_level for planet_name, _, _, _, _, _, _, _, _, _, _, unlock_level in PLANETS}
    resources = {planet_name: specific_resource for planet_name, _, _, _, _, specific_resource, _, _, _, _, _, _ in
                 PLANETS}
    planets = [Planet(name, radius, distance, texture_path, resource_per_click, auto_farm_cost, specific_resource,
                      resource_name, extractor_upgrade_cost, extractor_upgrade_rate, hull_upgrade_cost, unlock_level)
               for
               name, radius, distance, texture_path, resource_per_click, auto_farm_cost, specific_resource, resource_name, extractor_upgrade_cost, extractor_upgrade_rate, hull_upgrade_cost, unlock_level
               in PLANETS]

    return screen, background_image, planets, niveaux_requis, resources
def main():
    screen, background_image, planets, niveaux_requis, resources = initialize_game()

    offset = 0
    min_offset = -WIDTH / 12
    max_offset = max(planet.distance for planet in planets) - WIDTH + planets[-1].radius  # Offset maximal

    current_menu = None

    clock = pygame.time.Clock()
    running = False
    start_menu = StartMenu()
    while True:
        start_menu.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                result = start_menu.handle_click(event.pos)
                if result == "PLAY":
                    running = True
                    break
                elif result == "QUIT":
                    pygame.quit()
                    sys.exit()

        if running:
            break

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    offset += 50
                    offset = min(offset, max_offset)
                elif event.button == 5:
                    offset -= 50
                    offset = max(offset, min_offset)
                elif event.button == 1:
                    if current_menu:
                        result = current_menu.handle_click(event.pos)
                        if result == "CLOSE":
                            current_menu = None
                    else:
                        for planet in planets[1:]:
                            if pygame.Rect(planet.distance - offset - planet.radius, HEIGHT // 2 - planet.radius,
                                           2 * planet.radius, 2 * planet.radius).collidepoint(event.pos):
                                if niveau_vaisseau >= niveaux_requis[planet.name]:
                                    current_menu = Menu(planet, resources, "texture/fondmenu.png")
                                break
                        else:
                            current_menu = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    offset -= 50
                    offset = max(offset, min_offset)
                elif event.key == pygame.K_RIGHT:
                    offset += 50
                    offset = min(offset, max_offset)

        screen.blit(background_image, (0, 0))

        for planet in planets:
            planet.draw(screen, offset)
            planet.draw_name(screen, offset)
            planet.auto_farm()

        if current_menu:
            current_menu.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
