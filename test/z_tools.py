#collection of tools used across my variousscripts
import time
from time import sleep, gmtime, strftime
import pyautogui
from playsound import playsound

#play a sound
def alert():
    playsound("media/drip.ogg")
    sleep(5)
    return None

#repeated calls to finding an object on the screen and clicking the center of it
#resetting the k loop if it found something
def LocateCenterClickWait(png_filename,click,wait,k):
    found = False
    try:
        top_left_sizeX_sizeY = pyautogui.locateOnScreen(png_filename + '.png', confidence = 0.8, region=(0,0,1280,720))
        if click:
            x,y = pyautogui.center(top_left_sizeX_sizeY)
            pyautogui.click(x, y)
        sleep(wait)
        k = 0
        found = True
    except:
        k+=1
    return k,found


if __name__ == '__main__':
    #example call to locate center click wait on an object it finds
    k,found = LocateCenterClickWait('media/inventory_open',True,2,k)

    #example call to play a sound
    alert()
