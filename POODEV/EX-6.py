class Animal():
    def emitirSom(self):
        raise

class Cachorro(Animal):
    def emitirSom(self):
        return 'Woof Woof'
    
class Gato(Animal):
    def emitirSom(self):
        return 'Miau'
    
def faz_som(animal):
    print(animal.emitirSom())

dog = Cachorro()
cat = Gato()

print()
faz_som(dog)
faz_som(cat)
print()