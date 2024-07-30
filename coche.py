
class Coche:
    
    # Afecta a todas 
    ruedas = 4

    def __init__(self, marca, color) -> None:
        self.marca = marca
        self.color = color

    # self = this
    def conducir(self):
        print(f'Conduciendo...{self.color}')

    def parar(self):
        print('Parando...')

