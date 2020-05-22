from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class cordinates():
    replaybtn=(480,400)
    dinasaur=(246,405)
#x= 320 cordinate to check for tree
#y= 415 cordinate for half tree 

def restartgame():
    pyautogui.click(cordinates.replaybtn)


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
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

main()



