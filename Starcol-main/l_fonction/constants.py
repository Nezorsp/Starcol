# Dimensions de la fenêtre
WIDTH, HEIGHT = 1920, 1080

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHT_BLUE = (135, 206, 250)
ORANGE = (255, 165, 0)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)

niveau_vaisseau = 0

# Planètes
PLANETS = [
    # Nom, rayon, distance du soleil, chemin de la texture, ressource par clic, coût de l'auto farm, ressource spécifique, nom de la ressource, coût d'amélioration de l'extracteur, vitesse d'extraction améliorée, coût d'amélioration de la coque, level requis
    ("Soleil", 120, 0, "texture/soleil.png", 0, 0, 0, "", 0, 0, 0, 0),
    ("Mercure", 60, 400, "texture/mercure.png", 1, 300, 50, "Mercurium", 1500, 33, 3000, 3),
    ("Venus", 80, 800, "texture/venus.png", 2, 225, 100, "Venite", 1700, 36, 3400, 2),
    ("Terre", 90, 1200, "texture/terre.png", 3, 300, 150, "Terranium", 1900, 28, 3500, 0),
    ("Mars", 70, 1600, "texture/mars.png", 4, 400, 25, "Marsium", 2000, 30, 3900, 1),
    ("Jupiter", 160, 2000, "texture/jupiter.png", 5, 550, 250, "Jupiton", 2500, 18, 4000, 4),
    ("Saturne", 140, 2400, "texture/saturne.png", 6, 600, 300, "Saturnium", 3000, 30, 4500, 5),
    ("Uranus", 120, 2800, "texture/uranus.png", 7, 725, 350, "Uranium", 3500, 32, 5000, 6),
    ("Neptune", 110, 3100, "texture/neptune.png", 8, 875, 400, "Neptunium", 4000, 22, 5500, 7)
]

niveau_vaisseau = 0
