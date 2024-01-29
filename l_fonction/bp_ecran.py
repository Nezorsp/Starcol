import pygame

from l_fonction.fullscreen import largeur, hauteur

largeur_bouton, hauteur_bouton = 150, 50
x_bouton, y_bouton = (largeur - largeur_bouton) // 2, (hauteur - hauteur_bouton) // 1.4
bouton_rect = pygame.Rect(x_bouton, y_bouton, largeur_bouton, hauteur_bouton)