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
import keyboard
import numpy as np
import PIL, PIL.Image, PIL.ImageOps, PIL.ImageEnhance
import time


#TODO# Obtencion de imagenes#####
def ImagenDerecha():
    pathImage = filedialog.askopenfilename(filetypes = [("image", ".jpg")])

    if len(pathImage) > 0:
        global ImDerecha, wid, hgt, ImDerechaCV
        ImDerecha = PIL.Image.open(pathImage, mode = 'r').convert('L')
        ImDerechaCV = cv2.imread(pathImage)
        wid, hgt = ImDerecha.size

def ImagenIzquierda():
    pathImage = filedialog.askopenfilename(filetypes = [("image", ".jpg")])

    if len(pathImage) > 0:
        global ImIzquierda, ImIzquierdaCV
        ImIzquierda = PIL.Image.open(pathImage, mode = 'r').convert('L')
        ImIzquierdaCV = cv2.imread(pathImage)
        

#?#################################
#?#### Funciones de vision 3d #####
#?#################################

def Anaglifo():
    global ImIzquierda, ImDerecha , wid, hgt
    ImRoja = PIL.ImageOps.colorize(ImIzquierda,(0,0,0),(255,0,0))#Las iamgenes estan en BGR
    ImCyan = PIL.ImageOps.colorize(ImDerecha,(0,0,0),(0,255,255))#Limita los espacios de color desde 0 hasta el valor deseado 255 en el canal


    mezcla = PIL.Image.blend(ImRoja, ImCyan, 0.5)#Alpha 0.5 para que se puperpongan las dos imagenes sin predominancias en ninguna
    npMezcla = np.array(mezcla)

    ImCombinada = imutils.resize(npMezcla, height=hgt)
    ImCombinada = cv2.cvtColor(ImCombinada, cv2.COLOR_BGR2RGB)#Al pasar de BGR a RGB solo cambia el formato de la imagen, pero la informacion de los pixeles queda igual en el mismo orden

    os.chdir("Resultados")
    cv2.imwrite("Anaglifo.jpg",ImCombinada)#Guardar la imagen en el computador
    os.startfile("Anaglifo.jpg")#Abrir la imagen con el gestor de imagenes del computador
    os.chdir("..")

    time.sleep(0.2)##Esperar y maximizar imagen 
    keyboard.press('F11')

def Paralela():
    global ImIzquierdaCV, ImDerechaCV

    os.chdir("Resultados")
    cv2.imwrite("VisionParalela.jpg", np.hstack([ImIzquierdaCV,ImDerechaCV]))
    os.startfile("VisionParalela.jpg")#Abrir la imagen con el gestor de imagenes del computador
    os.chdir("..")

    time.sleep(0.2)
    keyboard.press('F11')

def Cruzada():
    global ImIzquierdaCV, ImDerechaCV

    os.chdir("Resultados")
    cv2.imwrite("VisionCruzada.jpg", np.hstack([ImDerechaCV,ImIzquierdaCV]))
    os.startfile("VisionCruzada.jpg")#Abrir la imagen con el gestor de imagenes del computador
    os.chdir("..")

    time.sleep(0.2)
    keyboard.press('F11')

def TopDown():
    global ImIzquierdaCV, ImDerechaCV

    os.chdir("Resultados")
    cv2.imwrite("TopDown.jpg", np.concatenate((ImIzquierdaCV,ImDerechaCV),0))
    os.startfile("TopDown.jpg")#Abrir la imagen con el gestor de imagenes del computador
    os.chdir("..")

    time.sleep(0.2)
    keyboard.press('F11')


def PruebaAnaglifos():#
    global ImIzquierda, ImDerecha , wid, hgt
    ImRoja = PIL.ImageOps.colorize(ImIzquierda,(0,0,0),(255,0,0))#Las iamgenes estan en BGR
    ImCyan = PIL.ImageOps.colorize(ImDerecha,(0,0,0),(0,255,255))#Limita los espacios de color desde 0 hasta el valor deseado 255 en el canal
    npImRoja = np.array(ImRoja)
    npImCyan = np.array(ImCyan)
    
    npImRoja = imutils.resize(npImRoja, height=hgt)
    npImCyan = imutils.resize(npImCyan, height=hgt)
    npImRoja1 = cv2.cvtColor(npImRoja, cv2.COLOR_BGR2RGB)
    npImCyan1 = cv2.cvtColor(npImCyan, cv2.COLOR_BGR2RGB)
    cv2.imwrite("Canalesseparados.jpg", np.hstack([npImRoja,npImCyan,npImRoja1,npImCyan1]))
    os.startfile("Canalesseparados.jpg")#Abrir la imagen con el gestor de imagenes del computador
    time.sleep(0.1)
    keyboard.press('F11')


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

btnCruzada = Button(root, text = "Vision cruzada", width = 18, font=("Palatino Linotype",13),command=Cruzada)
btnCruzada.grid(column=0, row=3, padx=5, pady = 5)

btnTD = Button(root, text = "Top & Down", width = 18, font=("Palatino Linotype",13), command=TopDown)
btnTD.grid(column=1, row=3, padx=5, pady = 5)

root.mainloop()