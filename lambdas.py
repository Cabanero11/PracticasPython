double = lambda x : x * 2

mult = lambda x, y : x * y

vivo = lambda vida : True if vida >= 1 else False

print(double(2), mult(5,3))

print(f'Ta vivo?: {vivo(0)}')


# dar a la var = name el modulo main
if __name__ == '__main__':
    import coche
    print('\n',__name__)  # __main__
    print(coche.__name__) # coche