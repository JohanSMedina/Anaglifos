from tkinter import *
from tkinter import filedialog
import numpy as np
import cv2
import os

import ctypes#Para el tamaño de la pantalla



global ancho
global alto

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(ancho, alto)

#TODO# Obtencion de imagenes#####
def ImagenDerecha():
    pathImage = filedialog.askopenfilename(filetypes = [("image", ".jpg")])

    if len(pathImage) > 0:
        global ImDerecha
        ImDerecha = cv2.imread(pathImage)

def ImagenIzquierda():
    pathImage = filedialog.askopenfilename(filetypes = [("image", ".jpg")])

    if len(pathImage) > 0:
        global ImIzquierda
        ImIzquierda = cv2.imread(pathImage)

ImagenDerecha()
rgbImDerecha = cv2.cvtColor(ImDerecha,cv2.COLOR_BGR2RGB)


cv2.imwrite("prueba.jpg",rgbImDerecha)




"""#?##################
#?#### Interfaz#####
#?##################

root = Tk()
root.title("Vision-3D")

btn1 = Button(root, text = "Elegir imagen Izquierda", width = 20,height=2, font=("Palatino Linotype",20),command=ImagenIzquierda)
btn1.grid(column=0, row=0, padx=5, pady = 20)

btn2 = Button(root, text = "Elegir imagen Derecha", width = 20,height=2, font=("Palatino Linotype",20),command=ImagenDerecha)
btn2.grid(column=1, row=0, padx=5, pady = 20)


btnAnaglifo = Button(root, text = "Anaglifo", width = 18, font=("Palatino Linotype",13), command=Anaglifo)
btnAnaglifo.grid(column=0, row=2, padx=5, pady = 5)

btnParalela = Button(root, text = "Vision paralela", width = 18, font=("Palatino Linotype",13), command=Paralela)
btnParalela.grid(column=1, row=2, padx=5, pady = 5)

btnCruzada = Button(root, text = "Vision cruzada", width = 18, font=("Palatino Linotype",13))
btnCruzada.grid(column=0, row=3, padx=5, pady = 5)

btnTD = Button(root, text = "Top & Down", width = 18, font=("Palatino Linotype",13))
btnTD.grid(column=1, row=3, padx=5, pady = 5)

root.mainloop()"""