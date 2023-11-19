from constantes import *

import pygame

class Labirinto:
    def __init__(self):
        # path
        self.__caminho_arquivo = 'labirintos/labirinto.txt'

        # matriz estatica
        self.__labirinto = []
        self.__tamanho = {'linhas': 0, 'colunas': 0}

        # Exibição
        # self.__tamanho_quadrados = 90
        self.__tamanho_quadrados = 60
        self.__margem_top = 200
        self.__margem_left = 310

    def carregar_labirinto(self):
        try:
            with open(self.__caminho_arquivo, 'r') as arquivo:

                # a primeira linha é sempre no formato NxN
                dimensoes_matriz = arquivo.readline()

                linhas, colunas = map(int, dimensoes_matriz.split('x'))
                self.__tamanho['linhas'] = linhas
                self.__tamanho['colunas'] = colunas

                for linha in arquivo:
                    # Remove espaços e transforma em lista.
                    lista_caracteres = list(linha.strip())
                    self.__labirinto.append(lista_caracteres)

        except FileNotFoundError:
            print('O arquivo não existe')
        except Exception as error:
            print(f'Exceção encontrada: {error}')

    def atualizar(self, tela):
        # Desenha a matriz centralizada
        for indice_linha, linha_labirinto in enumerate(self.__labirinto):
            for indice_coluna, valor in enumerate(linha_labirinto):
                pos_x = self.__margem_left + indice_coluna * self.__tamanho_quadrados
                pos_y = self.__margem_top + indice_linha * self.__tamanho_quadrados

                match valor:
                    case '0':
                        imagem = pygame.image.load('Assets/tile_0000.png')
                    case '1' | '|':
                        imagem = pygame.image.load('Assets/Group13.png')
                    case 'x':
                        imagem = pygame.image.load('Assets/tile_0043.png')
                    case 'm':
                        imagem = pygame.image.load('Assets/rato.png')
                    case 'e':
                        imagem = pygame.image.load('Assets/geo.png')
                
                # Redimensione a imagem
                imagem = pygame.transform.scale(imagem, (self.__tamanho_quadrados, self.__tamanho_quadrados))

                # desenha imagem na tela
                tela.blit(imagem, (pos_x, pos_y))


if __name__ == '__main__':
    labirinto = Labirinto()
    labirinto.carregar_labirinto()
    labirinto.exibir()
