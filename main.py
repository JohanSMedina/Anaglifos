########################
#! Inicio del proyecto #
########################

#####Librerias#####
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np
import PIL, PIL.Image, PIL.ImageOps, PIL.ImageEnhance


#TODO# Obtencion de imagenes#####
def ImagenDerecha():
    pathImage = filedialog.askopenfilename(filetypes = [("image", ".jpg")])

    if len(pathImage) > 0:
        global ImDerecha
        ImDerecha = PIL.Image.open(pathImage, mode = 'r').convert('L')

def ImagenIzquierda():
    pathImage = filedialog.askopenfilename(filetypes = [("image", ".jpg")])

    if len(pathImage) > 0:
        global ImIzquierda
        ImIzquierda = PIL.Image.open(pathImage, mode = 'r').convert('L')

#?###################
#?#### Filtrados#####
#?###################

###Anaglifo###
def Anaglifo():
    global ImIzquierda, ImDerecha
    if selected.get() == 1:
        ImRoja = PIL.ImageOps.colorize(ImIzquierda,(0,0,0),(255,0,0))
        ImCyan = PIL.ImageOps.colorize(ImDerecha,(0,0,0),(0,255,255))

        mezcla = PIL.Image.blend(ImRoja, ImCyan, 0.5)
        npMezcla = np.array(mezcla)
        ImCombinada = imutils.resize(npMezcla, height=800)
        ImCombinada = cv2.cvtColor(ImCombinada, cv2.COLOR_BGR2RGB)

        cv2.imshow('Anaglifo', ImCombinada)
        cv2.waitKey(0)


#?##################
#?#### Interfaz#####
#?##################

root = Tk()

selected = IntVar()
rad1 = Radiobutton(root, text="Anaglifo", width=50, value = 1, variable=selected, command = Anaglifo)
rad1.grid(column=0, row=4)

btn1 = Button(root, text = "Elegir imagen Izquierda", width=50,command=ImagenIzquierda)
btn1.grid(column=0, row=0, padx=5, pady = 5)

btn2 = Button(root, text = "Elegir imagen Derecha", width=50,command=ImagenDerecha)
btn2.grid(column=0, row=1, padx=5, pady = 5)
root.mainloop()