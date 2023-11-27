import pygame

# TELA (Display)
pygame.init()

ALTURA = 1920
LARGURA = 1080

TITULO_JANELA = 'MAZE INSLAND'

DELAY = 1000

# SIMBOLOS
QUEIJO = 'e'
BARREIRA1 = '1'
BARREIRA2 = '|'
CAMINHO = '0'
CAMINHO_VISITADO = '.'
CAMINHO_CERTO = 'c'
RATO = 'm'

# EFEITOS SONOROS
MUSICA_INICIAR = 'Assets/music/jingles_PIZZI04.ogg'
MUSICA_ANDAR = 'Assets/music/impactGlass_light_004.ogg'
MUSICA_ACHOU_QUEIJO = 'Assets/music/jingles_PIZZI04.ogg'

# IMAGENS
IMG_GRAMA = 'Assets/img/grama.png'
IMG_CAIXA = 'Assets/img/caixa3.png'
IMG_LUGAR_VISITADO = 'Assets/img/x.png'
IMG_RATO = 'Assets/img/rato.png'
IMG_QUEIJO = 'Assets/img/geo.png'
IMG_CERTO = 'Assets/img/bandeira.png'

# BACKGROUND
BACKGROUND = 'Assets/img/background.png'

# FONTES
FONT1 = 'Assets/fonts/Fonts/Kenney Mini Square.ttf'

# CORES (RGB)
COR_BRANCA = (255, 255, 255)
COR_PRETA = (0, 0, 0)
COR_AZUL = (0, 104, 255)
COR_AMARELA = (251, 255, 0)
COR_VERDE = (0, 255, 0)