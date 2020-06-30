import pyautogui
from PIL import Image, ImageGrab
import time
#from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)

def takeScreenshot():
    image = ImageGrab.grab().convert('L')
    #image.show()
    return image

def isCollide(data):
    for i in range(350,420):
        for j in range(420,450):
            if data[i,j]<100:
                return True
    return False

if __name__ == "__main__":
    print('Dino Game will start in 3 sec.....')
    time.sleep(3)

    # image = takeScreenshot()
    # data = image.load()
    # for i in range(350,420):
    #     for j in range(420,450):
    #         data[i,j]=0
    
    # image.show()

    hit('up')
    hit('up')
    while(True):
        image = takeScreenshot()
        data = image.load()

        if isCollide(data):
            hit('up')