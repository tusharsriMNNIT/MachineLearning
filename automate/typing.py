import pyautogui
from PIL import Image, ImageGrab
import time

s = "OTT stands for over the top services If we sum up the definitions present online OTT in general refers to the delivery of media without using traditional cable or satellite for distribution of content OTT Services use the internet for the distribution of content."

print('Typing will start in 2 sec.......')
time.sleep(2)
for c in s:
    if c==' ':
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
    else:
        ch = c.lower()
        pyautogui.keyDown(ch)
        pyautogui.keyUp(ch)
    
    time.sleep(0.2)