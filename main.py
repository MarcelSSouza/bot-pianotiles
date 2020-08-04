import random
import time
import keyboard
import win32api, win32con
import pyautogui
from pyautogui import *
pyautogui.displayMousePosition()

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q')==false:
    if pyautogui.pixel(512, 660)[0] == 0:
        click(512, 660)
    if pyautogui.pixel(615, 660)[0] == 0:
        click(615, 660)
    if pyautogui.pixel(712, 660)[0] == 0:
        click(712, 660)
    if pyautogui.pixel(805, 660)[0] == 0:
        click(805, 660)