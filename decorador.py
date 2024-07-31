# Decorador permite, modificar 
# el comportamiento de una funcion

def decorador(func):
    def wrapper():
        print('Antes de funcion')
        func()
        print('Despois de funcion')
    return wrapper()

# no funciona xd, pero deberia ser que deja 
# hacer el f = decorador(funcion) 
# con el @ pero weno

# @decorador
def funcion():
    print('He')

f = decorador(funcion)

# GENERADOR

def generador():
    yield 1
    yield 2
    yield 'Hola'

for i in generador():
    print(f'i: {i}')