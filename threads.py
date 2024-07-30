import threading
import time

def desayuno():
    time.sleep(2)
    print('Leche')

def deporte():
    time.sleep(5)
    print('Espalda')


def estudiar():
    time.sleep(4)
    print('Python')


hilo1 = threading.Thread(target=desayuno, args=())
hilo2 = threading.Thread(target=deporte, args=())
hilo3 = threading.Thread(target=estudiar, args=())

hilo1.start()
hilo2.start()
hilo3.start()


print(threading.active_count())

print(threading.enumerate())