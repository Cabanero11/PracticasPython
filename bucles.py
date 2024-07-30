
name = None

#while not name :
    #name = input('Introduce tu nombre:') 

#print('Bienvenido', name, '!')

nombre = 'Caba'

#for i in range(0, 10, 3):
#    print('i:',i)
#
#for i in nombre:
#    print(i)

row = int(input('Row: '))
column = int(input('Column: '))

for i in range(row):
    for j in range(column):
        print('#', end='')
    print()
