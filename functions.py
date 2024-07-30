import math

def hello(text):
    if text == 'a':
        print('AAAAA')
    else:
        print('pon a')


#hello('a')

def pito(n1, n2):
    return math.sqrt(n1)

def foo(first, middle):
    print('Nombre:', first, 'Apellido:', middle)

foo(middle='Ruiz', first='Antonio')

name = 'Caba'

def display_name():
    name = 'Bro'
    print(name)

print(name)
display_name()
