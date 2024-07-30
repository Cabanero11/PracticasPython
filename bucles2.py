#while(True):
#    name = input('Nombre: ')
#    if name != '':
#        break
#

num_telefono = '123-456-789'

for i in num_telefono:
    if i == '-':
        continue
    print(i, end='')