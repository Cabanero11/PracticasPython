name = "Antonio Ruiz"

first_name = name[:7]
second_name = name[7:]
xd = name[0:7:2]
reves = name[::-1]

print(first_name + second_name)
#print(xd)
print(reves)

web = "https://google.com"

# Obtener el nombre solo, quitamos delante y detras
slice = slice(8, -4)
# Seleccionamos el trozo
print(web[slice].capitalize())