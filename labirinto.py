from constantes import *
from ponto import Ponto
from pilha.pilha import Pilha

import pygame


class Labirinto:
    def __init__(self):
        # path
        self.__caminho_arquivo = 'labirintos/labirinto4.txt'

        # matriz estatica
        self.__labirinto = []
        self.__tamanho = Ponto()

        self.__posicao_rato = Ponto()

        self.__caminho = Pilha()


        # Exibição
        # self.__tamanho_quadrados = 90
        self.__tamanho_quadrados = 40
        self.__margem_top = 200
        self.__margem_left = 310

        # EFEITOS SONOROS
        self.__efeito_sonoro = pygame.mixer.Sound(MUSICA_ANDAR)
        self.__efeito_sonoro2 = pygame.mixer.Sound(MUSICA_ACHOU_QUEIJO)

        # Movimentar
        self.__movimentacao = [
            (1, 0, 'direita'),
            (-1, 0, 'esquerda'),
            (0, -1, 'cima'),
            (0, 1, 'baixo')
        ]

    def caminho_certo(self):
        caminhos = self.__caminho.listar()
        for caminho in caminhos:
            self.__labirinto[caminho.y][caminho.x] = CAMINHO_CERTO

    def carregar_labirinto(self):
        try:
            with open(self.__caminho_arquivo, 'r') as arquivo:

                # a primeira linha é sempre no formato NxN
                dimensoes_matriz = arquivo.readline()

                linhas, colunas = map(int, dimensoes_matriz.split('x'))
                self.__tamanho.x = linhas
                self.__tamanho.y = colunas

                for indice, linha in enumerate(arquivo):
                    if RATO in linha:
                        self.__posicao_rato.x = linha.find(RATO)
                        self.__posicao_rato.y = indice
                        self.__caminho.empilhar(self.__posicao_rato)

                    # Remove espaços e transforma em lista.
                    lista_caracteres = list(linha.strip())
                    self.__labirinto.append(lista_caracteres)

        except FileNotFoundError:
            print('O arquivo não existe')
        except Exception as error:
            print(f'Exceção encontrada: {error}')

    def atualizar(self, tela):
        """Desenha o labirinto na tela """
        for indice_linha, linha_labirinto in enumerate(self.__labirinto):
            for indice_coluna, valor in enumerate(linha_labirinto):
                pos_x = self.__margem_left + indice_coluna * self.__tamanho_quadrados
                pos_y = self.__margem_top + indice_linha * self.__tamanho_quadrados

                match valor:
                    case '0':
                        imagem = pygame.image.load(IMG_GRAMA)
                    case '1' | '|':
                        imagem = pygame.image.load(IMG_CAIXA)
                    case '.':
                        imagem = pygame.image.load(IMG_LUGAR_VISITADO)
                    case 'c':
                        imagem = pygame.image.load(IMG_CERTO)
                    case 'm':
                        imagem = pygame.image.load(IMG_RATO)
                    case 'e':
                        imagem = pygame.image.load(IMG_QUEIJO)

                # Redimensione a imagem
                imagem = pygame.transform.scale(
                    imagem, (self.__tamanho_quadrados, self.__tamanho_quadrados))

                # desenha imagem na tela
                tela.blit(imagem, (pos_x, pos_y))

    def valida_posicao(self, ponto):

        try:
            if self.__labirinto[ponto.y][ponto.x] not in (CAMINHO, QUEIJO):
                return False
        except IndexError:
            return False

        return True

    def movimentar_rato(self):

        for movimento in self.__movimentacao:
            posicao_x, posicao_y, direcao = movimento

            nova_posicao = Ponto()
            nova_posicao.x = self.__posicao_rato.x + posicao_x
            nova_posicao.y = self.__posicao_rato.y + posicao_y

            # Debug
            print('Rato indo para: ', direcao, nova_posicao.y, nova_posicao.x)

            if self.valida_posicao(nova_posicao):

                self.__caminho.empilhar(nova_posicao)

                if self.__labirinto[nova_posicao.y][nova_posicao.x] == QUEIJO:
                    self.__labirinto[self.__posicao_rato.y][self.__posicao_rato.x] = CAMINHO_VISITADO
                    self.__posicao_rato = nova_posicao
                    self.__labirinto[nova_posicao.y][nova_posicao.x] = RATO

                    self.__efeito_sonoro.play()
                    pygame.time.delay(1000)
                    self.__efeito_sonoro2.play()
                    self.caminho_certo()

                    return False

                self.__labirinto[self.__posicao_rato.y][self.__posicao_rato.x] = CAMINHO_VISITADO
                self.__labirinto[nova_posicao.y][nova_posicao.x] = RATO
                self.__posicao_rato = nova_posicao

                self.__efeito_sonoro.play()
                pygame.time.delay(1000)

                return True

        if self.__caminho.tamanho > 1:

            self.__labirinto[self.__posicao_rato.y][self.__posicao_rato.x] = CAMINHO_VISITADO

            self.__caminho.desempilhar()
            self.__posicao_rato = self.__caminho.ver_topo()

            self.__labirinto[self.__posicao_rato.y][self.__posicao_rato.x] = RATO

            print('Desempilhando o rato: ',
                  self.__posicao_rato.y, self.__posicao_rato.x)

            self.__efeito_sonoro.play()
            pygame.time.delay(1000)

            return True

        # rato preso ou sem quijo
        print('Rato sem saida!')
        return False


if __name__ == '__main__':
    labirinto = Labirinto()
    labirinto.carregar_labirinto()
