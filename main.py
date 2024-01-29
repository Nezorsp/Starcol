# Import
import pygame
import sys

# Ajouter le path:
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# Importer les modules externes:
from l_fonction.fullscreen import basculer_plein_ecran
from l_fonction.creationf import fenetre
from l_fonction.bp_ecran import bouton_rect
from couleur.couleur import BLANC, NOIR
from l_fonction.back import background_image

# Initialiser Pygame
pygame.init()

# boucle principale
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if bouton_rect.collidepoint(event.pos):
                basculer_plein_ecran()

# Mettre le fond
    fenetre.blit(background_image, (0, 0))

# Faire le boutton
    pygame.draw.rect(fenetre, BLANC, bouton_rect, 2)

# Mettre à jour la page
    pygame.display.flip()