class Movimentavel:
    def mover(self, direction):
        raise NotImplementedError('O método mover() deve ser implementado')
    
class Desenhavel:
    def desenhar(self):
        raise NotImplementedError('O método desenhar() deve ser implementado')

class Personagem(Movimentavel, Desenhavel):
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def mover(self, direction):
        x, y = self.position
        if direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        elif direction == 'right':
            x += 1
        elif direction == 'left':
            x -= 1
        self.position = (x,y)
        print(f'{self.name} moveu-se para {direction}. Nova posição: {self.position}')
    
    def desenhar(self):
        print(f'Desenhando o personagem {self.name} na posião {self.position}')

hero = Personagem('Jeff', (0,0))

hero.mover('up')
hero.mover('right')
hero.mover('down')
hero.mover('left')

hero.desenhar()