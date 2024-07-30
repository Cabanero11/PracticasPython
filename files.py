import os
import shutil

path = 'C:\\Users\\Antonio\\Downloads\\DESCARGAS\\PYTHON COURSE\\texto.txt'



def foo():
    if os.path.exists(path) and os.path.isfile(path):
        print('Archivo leido OK\n') 
    else:
        print('El path ta mal')

    try:
        with open('test.txt', 'a') as file:
            file.write('Elden\nRing')
    except FileNotFoundError as e:
        print(f'{e}')

#shutil.copyfile('test.txt', 'text.txt')
os.remove('test.txt')

