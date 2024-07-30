# set - coleccion sin ordenar


utensilios = {'tenedor', 'cuchara', 'cuchillo', 'cuchillo', 'cuchillo'}
platos = {'bol', 'plato', 'copa'}

utensilios.add('plato')

utensilios.remove('tenedor')

utensilios.update(platos)

dinner_table = utensilios.union(platos)

for i in utensilios:
    print(i)

print('--------')

for i in dinner_table:
    print(i)