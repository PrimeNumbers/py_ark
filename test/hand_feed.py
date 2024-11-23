from time import sleep
import pyautogui
pyautogui.PAUSE = 0.25 #delay between pyautogui calls
pyautogui.FAILSAFE = True #move mouse to corner to disable

#my helper frunctions used across multiple scripts 
from load_vars import load_vars,val
from z_tools import alert , LocateCenterClickWait

sleep(3) #alt tab into ark

i = 0
i_max = 100 #try feeding a hundred tames

k = 0 # end searching if no matches found in 
k_max = 2 # a specific amount of loops
inv_open = False

alert()#play a sound before taking control
keys,vals = load_vars("vars.txt",'1') #passing the version number that you expect it to be

while i < i_max and k < k_max:
    inv_open = False

    j = 0 
    j_max = 10 #how many seconds to look for the open inventory
    j_sleep = .5 #seconds between looking
    j_max = j_max/j_sleep # adjust j_max based on j_sleep interval
    
    while j<j_max:
        k,inv_open = LocateCenterClickWait('media/inventory_open',False,2,k)
        if inv_open:
            pyautogui.click(val('transfer_x1',keys,vals), val('transfer_y',keys,vals)) #transfer all in
            sleep(0.5)

            pyautogui.click(val('close_inv_x',keys,vals), val('close_inv_y',keys,vals)) # close inventory
            j = j_max
        else:
            #wait until looking again
            sleep(j_sleep)
        j+=1

    sleep(1.0) #wait before starting the next loop
    i+=1
    k+=1

#switch back to script
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')
