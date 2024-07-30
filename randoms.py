import random


d6 = random.randint(1,6)
# Entre 0 y 1
x = random.random()

lista = ('rock', 'paper', 'scissor')

y = random.choice(lista)

cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']

random.shuffle(cards)

print(f'Dado: {d6}')
print(f'Random: {x:.1}')

print(f'Lista: {y}')
print(f'Cartas: {cards}')
