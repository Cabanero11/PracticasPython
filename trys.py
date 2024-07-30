try:
    num = int(input('Numero: '))
    num2 = int(input('Divisor: '))
    print (f'Res: {num / num2}')
except ZeroDivisionError as e:
    print(f'KAJAJA {e}')
except ValueError:
    print('Pon numeros PELOTUDO')
finally:
    print('Acabios')
