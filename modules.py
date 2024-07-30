#help('modules')
from coche import Coche

def pizza():
    print('PIZZA')

def foo():
    print('FSU')


coche1 = Coche('Mercedes', 'Negro')
coche2 = Coche('Megane', 'Rojo')

print(coche1.marca)

# Variable que afecta a todos
Coche.ruedas = 2

print(Coche.ruedas)

#coche1.conducir()

print(coche1.ruedas, coche2.ruedas)

# Walrus := asignar y crear :O
print(happy := True)

def hi():
    print('hi')

print(hi) # direccion memoria
e = hi
e()
