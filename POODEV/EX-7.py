class Motor():
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
        self.ligado = False
    
    def ligar(self):
        if self.ligado == False:
            self.ligado = True
            print('O motor foi ligado.')
        else:
            print('O motor já está ligado.')
    
    def desligar(self):
        if self.ligado == True:
            self.ligado = False
            print('O motor foi desligado.')
        else:
            print('O motor já está desligado.')

    def mostra_info(self):
        print(f"Tipo: {self.tipo}, Potência: {self.potencia}, Ligado: {self.ligado}")

class Carro():
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def ligar_motor(self):
        return self.motor.ligar()
    
    def desligar_motor(self):
        return self.motor.desligar()
    
    def mostra_info(self):
        motorInfo = self.motor.mostra_info()
        print(f"Marca: {self.marca}, Modelo: {self.modelo}\n")

motorzin = Motor('Gasolina', 200)
carrin = Carro('Toyota', 'Bingus', motorzin)

print()
carrin.ligar_motor()
print()
carrin.ligar_motor()
print()
carrin.desligar_motor()
print()
carrin.desligar_motor()
print()
carrin.mostra_info()
print()
