import math

class MatematicaUtil:
    
    def quadrado(numero):
        return numero**2
    
    def cubo(numero):
       return numero**3
    
    def raiz(numero):
        return math.sqrt(numero)

numero = 9

quadrado = MatematicaUtil.quadrado(numero)
cubo = MatematicaUtil.cubo(numero)
raiz = MatematicaUtil.raiz(numero)

print(f'Quadrado de {numero}: {quadrado}')
print(f'Cubo de {numero}: {cubo}')
print(f'Raiz de {numero}: {raiz}')
