import win32api, win32con
from time import sleep
from functools import reduce

def click(x,y, duration=30, delay=0.3): 
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    sleep(duration / 1000)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    sleep(delay)

