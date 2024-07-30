a = [20, '10', 3.14]

print(len(a))
b = [10, '20', 1.14]

if(a[0] == int(b[1])):
    print('True bro')

for i in a:
    print(i, end='-')

food = ['pizza', 'rice','burgar','chicken','pasta']
#food.insert(0, 'cake')
food.append('cum')
#food.sort()

print(food)

drinks = ['cola', 'bepsi']
cena = ['leche', 'tortilla']

comida = [drinks, cena]
print(comida[0][1])