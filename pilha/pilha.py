from .pilha_no import No

class Pilha:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def empilhar(self, elemento):
        """Insere um elemento na pilha"""
        novo_no = No(elemento)
        novo_no.proximo = self.__topo
        self.__topo = novo_no
        self.__tamanho += 1

    def desempilhar(self):
        """Remove último elemento da pilha"""

        if self.__tamanho > 0:
            no_atual = self.__topo
            self.__topo = self.__topo.proximo
            self.__tamanho -= 1
            return no_atual.data
        raise IndexError("A pilha está vazia")

    def ver_topo(self):
        """retorna o valor do topo sem remover"""
        if self.__tamanho > 0:
            return self.__topo.data
        raise IndexError("A pilha está vazia")

    def listar(self):
        """Retorna todos os elementos da pilha em uma lista, desempilhando"""
        lista = []
        while self.__topo:
            lista.append(self.desempilhar())
        return lista

    @property
    def tamanho(self):
        """Retorna o tamanho da lista"""
        return self.__tamanho


if __name__ == '__main__':
    pilha = Pilha()
    
    pilha.empilhar(1)
    pilha.empilhar(2)
    pilha.empilhar(3)
    pilha.empilhar(4)
    
    pilha.desempilhar()

    print(pilha.ver_topo())