from constantes import *
from ponto import Ponto
from pilha.pilha import Pilha

import pygame

class Labirinto:
    def __init__(self):
        # path
        self.__caminho_arquivo = 'labirintos/labirinto.txt'

        # matriz estatica
        self.__labirinto = []
        self.__tamanho = Ponto()

        self.__posicao_rato = Ponto()

        self.__caminho = Pilha()
        
        # Exibição
        # self.__tamanho_quadrados = 90
        self.__tamanho_quadrados = 60
        self.__margem_top = 200
        self.__margem_left = 310

        # som de passo
        self.__efeito_sonoro = pygame.mixer.Sound('music/footstep_carpet_001.ogg')

    def carregar_labirinto(self):
        try:
            with open(self.__caminho_arquivo, 'r') as arquivo:

                # a primeira linha é sempre no formato NxN
                dimensoes_matriz = arquivo.readline()

                linhas, colunas = map(int, dimensoes_matriz.split('x'))
                self.__tamanho.x = linhas
                self.__tamanho.y = colunas
                
                for indice, linha in enumerate(arquivo):
                    if 'm' in linha:
                        self.__posicao_rato.x = linha.find('m')
                        self.__posicao_rato.y = indice
                    
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
                        imagem = pygame.image.load(GRAMA)
                    case '1' | '|':
                        imagem = pygame.image.load(CAIXA)
                    case '.':
                        imagem = pygame.image.load(LUGAR_VISITADO)
                    case 'm':
                        imagem = pygame.image.load(RATO)
                    case 'e':
                        imagem = pygame.image.load(QUEIJO)
                
                # Redimensione a imagem
                imagem = pygame.transform.scale(imagem, (self.__tamanho_quadrados, self.__tamanho_quadrados))

                # desenha imagem na tela
                tela.blit(imagem, (pos_x, pos_y))

    def valida_posicao(self, ponto):
        if 0 <= ponto.x >= self.__tamanho.x and 0 <= ponto.y >= self.__tamanho.y:
            return False

        if self.__labirinto[ponto.y][ponto.x] not in '0e':
            return False
        
        return True


    def movimentar_rato(self):
        nova_posicao = Ponto(self.__posicao_rato.x, self.__posicao_rato.y)
    

        try:
            nova_posicao.x += 1
            if self.valida_posicao(nova_posicao):
                print('direita',nova_posicao.y, nova_posicao.x)
                self.__caminho.empilhar(nova_posicao)
                self.__labirinto[self.__posicao_rato.y][self.__posicao_rato.x] = '.'
                self.__labirinto[nova_posicao.y][nova_posicao.x] = 'm'
                self.__posicao_rato = nova_posicao
                self.__efeito_sonoro.play()
                pygame.time.delay(1000)
                return True



            nova_posicao.x = self.__posicao_rato.x
            nova_posicao.x -= 1
            if self.valida_posicao(nova_posicao):
                print('esquerda',nova_posicao.y, nova_posicao.x)
                self.__caminho.empilhar(nova_posicao)
                self.__labirinto[self.__posicao_rato.y][self.__posicao_rato.x] = '.'
                self.__labirinto[nova_posicao.y][nova_posicao.x] = 'm'
                self.__posicao_rato = nova_posicao
                self.__efeito_sonoro.play()
                pygame.time.delay(1000)
                return True
            

            nova_posicao.x = self.__posicao_rato.x

            nova_posicao.y -= 1
            if self.valida_posicao(nova_posicao):
                print('cima',nova_posicao.y, nova_posicao.x)
                self.__caminho.empilhar(nova_posicao)
                self.__labirinto[self.__posicao_rato.y][self.__posicao_rato.x] = '.'
                self.__labirinto[nova_posicao.y][nova_posicao.x] = 'm'
                self.__posicao_rato = nova_posicao
                self.__efeito_sonoro.play()
                pygame.time.delay(1000)
                return True
            

            nova_posicao.y = self.__posicao_rato.y
            nova_posicao.y += 1
            if self.valida_posicao(nova_posicao):
                print('baixo',nova_posicao.y, nova_posicao.x)
                self.__caminho.empilhar(nova_posicao)
                self.__labirinto[self.__posicao_rato.y][self.__posicao_rato.x] = '.'
                self.__labirinto[nova_posicao.y][nova_posicao.x] = 'm'
                self.__posicao_rato = nova_posicao
                self.__efeito_sonoro.play()
                pygame.time.delay(1000)
                return True
            elif self.__caminho.tamanho > 0:
                self.__labirinto[self.__posicao_rato.y][self.__posicao_rato.x] = '.'
                self.__posicao_rato = self.__caminho.desempilhar()
                self.__labirinto[self.__posicao_rato.y][self.__posicao_rato.x] = 'm'
                print('desempilha rato', self.__posicao_rato.y, self.__posicao_rato.x)
                self.__efeito_sonoro.play()
                pygame.time.delay(1000)
                return True
            
        except IndexError:
            return False
        
        return False




if __name__ == '__main__':
    labirinto = Labirinto()
    labirinto.carregar_labirinto()