from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class cordinates():
    replaybtn=(480,400)
    dinasaur=(246,405)

def restartgame():
    pyautogui.click(cordinates.replaybtn)
    pyautogui.keyDown   ('down')


def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("jump")
    time.sleep(0.18)
    pyautogui.keyUp('space')

def imageGrab():
    box = (cordinates.dinasaur[0]+74,cordinates.dinasaur[1],cordinates.dinasaur[0]+100,cordinates.dinasaur[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return (a.sum())

def main():
    restartgame()
while True:
  if (imageGrab()!=1027):
     pressSpace()
     time.sleep(0.1)

main()



