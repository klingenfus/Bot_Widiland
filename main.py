from code import InteractiveConsole
from turtle import position
import cv2 as cv
from time import time
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
from paths import Products
from time import sleep
from functions import click
from threading import Thread

###
#Configurations definition
pyautogui.FAILSAFE= True
loop_time = time()
bot_running = False
#Bot Status:
# None = Só tira print
# Trigo = Colhe, Planta, Faz missao só de Trigo
# Milho = Colhe, Planta, Faz missao só de Milho
# Mix = Colhe, Planta, Faz missao de Trigo e Milho
bot_status = None
###

###
#Caputar todas as janelas abertas
WindowCapture.list_window_names()
###

###
#Usar para detectar um programa especifico
#Quando Google Chrome é selecionado, o resultado será um tela preta, devido ao problema de compatibilidade de imagem entre Chorme e win32api.
# wincap = WindowCapture('League of Legends')
#Usar para detectar a tela principal(Desktop)
wincap = WindowCapture(None)
###

###
vision_Trigo = Vision(Products['milho'])
###

def bot_actions(positions_trigo):
    if len(positions_trigo)>0:
        for cord in positions_trigo:
            print(cord)
            offset_x = -20
            offset_y = 10
            cord_x = cord[0] + offset_x
            cord_y = cord[1] + offset_y
            print(f' cord: {cord}, cord_x: {cord_x}, cord_y: {cord_y}')
            click(cord_x , cord_y)
        sleep(5)
    global bot_running
    bot_running = False

while(True):
    screenshot = wincap.get_screenshot() #PyAutoGui Tira o ScreenShot
    
    # cv.imshow('Computer Vision', screenshot) #Open CV Mostra a imagem crua 
    positions_trigo = vision_Trigo.find(screenshot, 0.6, 'rectangles') #Mostra a imagem com os objetos encontrados
    
    ###
    #Bot Commands Call
    if not bot_running:
        bot_running = True
        t = Thread(target=bot_actions, args=(positions_trigo,))
        t.start()
    ###
    
    #Print FPS
    print('FPS: {}'.format(1/(time()-loop_time)))
    loop_time = time()
    
    #Wait Key Q
    if cv.waitKey(1) == ord('q'): #Espera a tecla Q ser apertada para sair
        cv.destroyAllWindows()
        break
    
print('Programa Finalizado')

def do_Reconnect():
    pass
def do_login():
    pass
def do_Mission():
    pass
def do_MissionCheck():
    pass
def do_Collect():
    pass
def do_Plant():
    pass