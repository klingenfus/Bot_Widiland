from turtle import position
import cv2 as cv
from time import time
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
from paths import Products, paths

###
WindowCapture.list_window_names()
###

###
#Usar para detectar um programa especifico
# wincap = WindowCapture('League of Legends')
#Usar para detectar a tela principal(Desktop)
wincap = WindowCapture(None)
###

###
vision_Trigo = Vision(Products['trigo'])
###

loop_time = time()
while(True):
    screenshot = wincap.get_screenshot() #PyAutoGui Tira o ScreenShot
    # screenshot = wincap.get_screenshot() #PyAutoGui Tira o ScreenShot
    
    # cv.imshow('Computer Vision', screenshot) #Open CV Mostra a imagem crua 
    positions_trigo = vision_Trigo.find(screenshot, 0.6, 'rectangles') #Mostra a imagem com os objetos encontrados
    
    if positions_trigo:
        for cord in positions_trigo:
            print(cord)
    #Print FPS
    
    def do_logar():
        pass
    def do_Mission():
        pass
    def do_Reconnect():
        pass
    
        
    
    print('FPS: {}'.format(1/(time()-loop_time)))
    loop_time = time()
    
    #Wait Key Q
    if cv.waitKey(1) == ord('q'): #Espera a tecla Q ser apertada para sair
        cv.destroyAllWindows()
        break
    
print('Programa Finalizado')