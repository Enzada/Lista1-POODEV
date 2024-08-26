class DividZero(Exception):
    def __init__(self, mensagem='Não é possível dividir por 0.'):
        super().__init__(mensagem)


class Divisao():
    def dividir(numerador, denominador):
        if denominador == 0:
            raise DividZero
        return numerador / denominador
    
try:
    resultado = Divisao.dividir(6,0)
    print(f'Resultado: {resultado}')
except DividZero as e:
    print(f'Erro: {e}')
