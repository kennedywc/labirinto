class Labirinto:
    def __init__(self, caminho_arquivo='labirintos/labirinto.txt'):
        self.__caminho_arquivo = caminho_arquivo

        self.__labirinto = []
        self.__tamanho = {'linhas': 0, 'colunas': 0}

    def carregar_labirinto(self):
        try:
            with open(self.__caminho_arquivo, 'r') as arquivo:
                # a primeira linha é sempre no formato NxN
                dimensoes_matriz = arquivo.readline()

                linhas, colunas = map(int, dimensoes_matriz.split('x'))
                self.__tamanho['linhas'] = linhas
                self.__tamanho['colunas'] = colunas

                for posicao_coluna, linha in enumerate(arquivo):
                    # Remove espaços e transforma em lista.
                    lista_caracteres = list(linha.strip())

                    self.__labirinto.append(lista_caracteres)
        except FileNotFoundError:
            print('O arquivo não existe')
        except Exception as error:
            print(f'Exceção encontrada: {error}')

    def exibir(self):
        print(self.__tamanho)
        for linha in self.__labirinto:
            print("".join(linha))


if __name__ == '__main__':
    labirinto = Labirinto()
    labirinto.carregar_labirinto()
    labirinto.exibir()
