from tkinter import *


def pulsar_boton(numero):
    #print(f"Nº {numero} presionado") 
    
    global ecuacion_texto
    
    ecuacion_texto += str(numero)
    ecuacion_label.set(ecuacion_texto)

def igual_calculo():
    
    global ecuacion_texto

    try:
        # eval calcula lo del texto (op)
        total = str(eval(ecuacion_texto))

        ecuacion_label.set(total)
        ecuacion_texto = total
    except ZeroDivisionError as e:
        ecuacion_label.set('No DIVIDAS POR 0')
        print(f'{e}')
    except SyntaxError as e:
        ecuacion_label.set('aiwjd Escribe bien awdawd')
        print(f'{e}')


def borrar_texto():
    
    global ecuacion_texto

    ecuacion_texto = ''
    ecuacion_label.set(ecuacion_texto)

ventana = Tk()



ventana.title("Calcu")
ventana.resizable(False, False)
ventana.geometry('550x550')


# Ecuacion

ecuacion_texto = ''

ecuacion_label = StringVar()

label = Label(ventana, textvariable=ecuacion_label, font=('consolas', 20), bg='white', width=38, height=2)
label.pack()

frame = Frame(ventana)
frame.pack()

# Crear botones
for i in range(1, 9+1):
    boton = Button(frame, text=str(i), height=4, width=9, font=36,
                   command=lambda i = i : pulsar_boton(i))
    # // es division entera -> 0,0,0, 1,1,1, 2,2,2
    # % es modulo, y quermos que de resto -> 0,1,2, 0,1,2
    boton.grid(row=(i-1) // 3, column=(i-1) % 3)

boton0 = Button(frame, text=0, height=4, width=9, font=36,
                   command=lambda : pulsar_boton(0))
boton0.grid(row=3, column=0)

# BOTONES DE OPERACIONES

sumar = Button(frame, text='+', height=4, width=9, font=40,
               command= lambda : pulsar_boton('+'))
sumar.grid(row=0, column=4)

restar = Button(frame, text='-', height=4, width=9, font=40,
               command= lambda : pulsar_boton('-'))
restar.grid(row=1, column=4)

multiplicar = Button(frame, text='*', height=4, width=9, font=40,
               command= lambda : pulsar_boton('*'))
multiplicar.grid(row=2, column=4)

dividir = Button(frame, text='/', height=4, width=9, font=40,
               command= lambda : pulsar_boton('/'))
dividir.grid(row=3, column=4)

igual = Button(frame, text='=', height=4, width=9, font=40,
               command= igual_calculo)
igual.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=40,
               command= lambda : pulsar_boton('.'))
decimal.grid(row=3, column=1)

borrar = Button(ventana, text='Borrar', height=4, width=19, font=40,
               command= borrar_texto)

borrar.pack()

ventana.mainloop()