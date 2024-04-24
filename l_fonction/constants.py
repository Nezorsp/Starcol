# Dimensions de la fenêtre
WIDTH, HEIGHT = 1710, 1112

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
    ("Mercure", 60, 400, "texture/mercure.png", 1, 10, 50, "Mercurium", 50, 33, 100, 0),
    ("Venus", 80, 800, "texture/venus.png", 2, 20, 100, "Venite", 100, 36, 150, 0),
    ("Terre", 90, 1200, "texture/terre.png", 3, 30, 150, "Terranium", 150, 28, 800, 0),
    ("Mars", 70, 1600, "texture/mars.png", 4, 40, 200, "Marsium", 200, 30, 250, 0),
    ("Jupiter", 160, 2000, "texture/jupiter.png", 5, 50, 250, "Jupiton", 250, 18, 300, 0),
    ("Saturne", 140, 2400, "texture/saturne.png", 6, 60, 300, "Saturnium", 300, 30, 350, 0),
    ("Uranus", 120, 2800, "texture/uranus.png", 7, 70, 350, "Uranium", 350, 32, 400, 0),
    ("Neptune", 110, 3100, "texture/neptune.png", 8, 80, 400, "Neptunium", 400, 22, 450, 0)
]

niveau_vaisseau = 0
