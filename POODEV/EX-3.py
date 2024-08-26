class Produto():
    def __init__(self, nome, valor, quantidade):
        self.nome = nome
        self.valor = valor
        self.num = quantidade
    
    def registro(self):
        print(f'Nome do produto: {self.nome}\n Preço do produto: R${self.valor}\n Quantidade disponível: {self.num}')

produto1 = Produto('Laptop muito brabo', 2500, 7)
produto2 = Produto('Televisão pica', 4600, 4)
produto3 = Produto('Banana', 999999, 1)

print()
produto1.registro()
print()
produto2.registro()
print()
produto3.registro()
print()