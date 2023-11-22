class Ponto:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, novo_x):
        self.__x = novo_x
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, novo_y):
        self.__y = novo_y
    
    def __eq__(self, outro):
        if isinstance(outro, Ponto):
            return (self.x == outro.x) and (self.y == outro.y)
        return False

    def nevativos(self):
        if self.__x > 0 or self.__y > 0:
            return True
        return False


if __name__ == '__main__':
    ponto = Ponto(2, 5)
    ponto2 = Ponto(2, 2)
    
    print(ponto == ponto2)