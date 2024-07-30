from coche import Coche, abstractmethod

class Animal:

    alive = True

    def __init__(self, velocidad, nombre) -> None:
        self.velocidad = velocidad
        self.nombre = nombre

    def poo(self):
        print('Prfpfrf...')

    def eat(self):
        print('Ñom ñom Ñom...')

class Conejo(Animal):
    def hop(self):
        print('Hop hop...')
    
    def __init__(self, velocidad, nombre) -> None:
        super().__init__(velocidad, nombre)

class Pez(Animal):
    def swim(self):
        print('Mamahuevo, digo glu glu glu...')

class Vehiculo(Coche):

    @abstractmethod
    def parar(self):
        pass

conejo = Conejo(200, 'Manolo')
pez = Pez(100, 'Pepo')

conejo.hop()
pez.swim()