import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)


def collide(data):
    #For Cactus
    for i in range(550, 570):
        for j in range(225, 260):
            if data[i, j] < 100:
                hit('up')
                return True

    #For Bird
    for i in range(530, 550):
        for j in range(200, 225):
            if data[i, j] < 100:
                hit('down')
                return True



if __name__ == "__main__":
    print("game about to start")
    time.sleep(2)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        collide(data)


