########################
#! Inicio del proyecto #
########################

#####Librerias#####
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import os
import cv2
import imutils
import numpy as np
import PIL, PIL.Image, PIL.ImageOps, PIL.ImageEnhance


#TODO# Obtencion de imagenes#####
def ImagenDerecha():
    pathImage = filedialog.askopenfilename(filetypes = [("image", ".jpg")])

    if len(pathImage) > 0:
        global ImDerecha, wid, hgt
        ImDerecha = PIL.Image.open(pathImage, mode = 'r').convert('L')
        wid, hgt = ImDerecha.size

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
    global ImIzquierda, ImDerecha , wid, hgt
    ImRoja = PIL.ImageOps.colorize(ImIzquierda,(0,0,0),(255,0,0))#Las iamgenes estan en BGR
    ImCyan = PIL.ImageOps.colorize(ImDerecha,(0,0,0),(0,255,255))#Limita los espacios de color desde 0 hasta el valor deseado 255 en el canal

    mezcla = PIL.Image.blend(ImRoja, ImCyan, 0.5)#Alpha 0.5 para que se puperpongan las dos imagenes sin predominancias en ninguna
    npMezcla = np.array(mezcla)
    ImCombinada = imutils.resize(npMezcla, height=hgt)
    ImCombinada = cv2.cvtColor(ImCombinada, cv2.COLOR_BGR2RGB)

    cv2.imwrite("Resultado.jpg",ImCombinada)#Guardar la imagen en el computador
    os.startfile("Resultado.jpg")#Abrir la imagen con el gestor de imagenes del computador

def Paralela():
    global ImIzquierda, ImDerecha
    ImRoja = PIL.ImageOps.colorize(ImIzquierda,(0,0,0),(255,0,0))
    ImCyan = PIL.ImageOps.colorize(ImDerecha,(0,0,0),(0,255,255))
    cv2.imshow('Paralela', ImCyan)



#?##################
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

root.mainloop()