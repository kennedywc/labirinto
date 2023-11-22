# Local
from constantes import *
from labirinto import Labirinto

# PYGAME
import pygame
from sys import exit


class Game:
    def __init__(self):

        # Inicialize o Pygame
        pygame.init()

        # Crie uma tela Pygame
        self.__tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO_JANELA)
        self.__background = pygame.image.load('Assets/background.png')
        
        self.__clock = pygame.time.Clock()
        
        self.__efeito_sonoro = pygame.mixer.Sound('music/go.ogg')

    def iniciar(self):
        labirinto = Labirinto()
        labirinto.carregar_labirinto()
        comecar = False

        # Loop principal do jogo
        while True:

            # self.__tela.fill(COR_AZUL)

            # capturando eventos da janela
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    # Encerra o Pygame
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    comecar = True
                    self.__efeito_sonoro.play()

            if comecar:
                comecar = labirinto.movimentar_rato()
                

            self.__tela.blit(self.__background, (0, 0))

            labirinto.atualizar(self.__tela)

            # Atualize a tela dentro do loop
            pygame.display.flip()
            
            self.__clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.iniciar()
