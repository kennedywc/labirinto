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

    def iniciar(self):
        desenhar_labirinto = Labirinto()
        desenhar_labirinto.carregar_labirinto()

        # Loop principal do jogo
        while True:

            # self.__tela.fill(COR_AZUL)

            # capturando eventos da janela
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    # Encerra o Pygame
                    pygame.quit()
                    exit()

            self.__tela.blit(self.__background, (0, 0))

            desenhar_labirinto.atualizar(self.__tela)

            # Atualize a tela dentro do loop
            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.iniciar()