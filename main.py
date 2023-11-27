# Local
from constantes import *
from labirinto import Labirinto

# PYGAME
import pygame
from sys import exit
import os


class Game:
    def __init__(self):

        # Inicialize o Pygame
        pygame.init()

        # Crie uma tela Pygame
        self.__tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO_JANELA)
        self.__background = pygame.image.load(BACKGROUND)
        
        self.__clock = pygame.time.Clock()
        
        self.__efeito_sonoro = pygame.mixer.Sound(MUSICA_INICIAR)

        # Fonte
        self.__fonte = pygame.font.Font(FONT1, 36)

    def iniciar(self):
        labirinto = Labirinto()
        labirinto.carregar_labirinto()
        comecar = False

        parar = False


        # Loop principal do jogo
        while True:
            self.__tela.blit(self.__background, (0, 0))

            # self.__tela.fill(COR_AZUL)

            # capturando eventos da janela
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    # Encerra o Pygame
                    pygame.quit()
                    os.system('clear' if os.name == 'posix' else 'cls')
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        comecar = True
                        self.__efeito_sonoro.play()
                        parar = True

                    if evento.key == pygame.K_k:
                        # Encerra o Pygame
                        pygame.quit()
                        os.system('clear' if os.name == 'posix' else 'cls')
                        exit()

            if comecar:
                comecar = labirinto.movimentar_rato()
            else:
                if not parar:
                    texto = self.__fonte.render('Teclar [ E S P A Ç O ] para começar', 
                                                False, # texto suavizado 
                                                COR_BRANCA)
                

                if parar:
                    texto = self.__fonte.render('Teclar [K] para sair', 
                            False, # texto suavizado 
                            COR_AMARELA)
                
                self.__tela.blit(texto, (100 , 100))
                
            labirinto.atualizar(self.__tela)

            # Atualize a tela dentro do loop
            pygame.display.flip()
            
            self.__clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.iniciar()
