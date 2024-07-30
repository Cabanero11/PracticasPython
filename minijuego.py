import random

choices = ['piedra', 'papel', 'tijera']


ha_ganado = False

while not ha_ganado:

    computer_choice = random.choice(choices)

    jugador_choice = input("¿piedra, papel, o tijeras?: ").lower()

    if computer_choice == 'piedra' and jugador_choice == 'papel':
        print('Ganaste')
        break
    elif computer_choice == 'pale' and jugador_choice == 'tijeras':
        print('Ganaste')
        break
    elif computer_choice == 'tijeras' and jugador_choice == 'piedra':
        print('Ganaste')
        break
    elif jugador_choice == 'piedra' and computer_choice == 'papel':
        print('Perdiste')
        break
    elif jugador_choice == 'pale' and computer_choice == 'tijeras':
        print('Perdiste')
        break
    elif jugador_choice == 'tijeras' and computer_choice == 'piedra':
        print('Perdiste')
        break
    elif jugador_choice == computer_choice:
        print(f'Maquina: {computer_choice}')
        print(f'Jugador: {jugador_choice}\n-------\n')
    

print('Acabo el juego :D')