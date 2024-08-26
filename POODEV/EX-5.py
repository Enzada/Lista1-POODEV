class Veiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Carro(Veiculo):
    def __init__(self, marca, modelo, nome, lealdade):
        super().__init__(marca, modelo)
        self.nome = nome
        self.lealdade = lealdade
    
    def registro(self):
        print(f'Marca: {self.marca}\n Modelo: {self.modelo}\n Nome: {self.nome}\n Lealdade: {self.lealdade}')

print()
carro1 = Carro('Chevrolet', 'Camaro', 'Bumblebee', 'Autobot')
carro2 = Carro('Toyota', 'Chevet', 'Jazz', 'Autobot')

carro1.registro()
print()
carro2.registro()
print()
