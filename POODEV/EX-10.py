import math
from abc import ABC, abstractmethod

class FormaGeomatrica(ABC):
    def calcularArea(self):
        pass

class Quadrado(FormaGeomatrica):
    def __init__(self, lado):
        self.lado = lado
    
    def calcularArea(self):
        print(f'A área de um quadrado com lados de {self.lado}m é {self.lado * self.lado}m²')

class Circulo(FormaGeomatrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcularArea(self):
        print(f'A área de um círculo com raio de {self.raio} é {(self.raio**2)*math.pi}') 

quadrado = Quadrado(4)
circulo = Circulo(3)

quadrado.calcularArea()
circulo.calcularArea()