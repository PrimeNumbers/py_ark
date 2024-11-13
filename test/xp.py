import time
from time import sleep, gmtime, strftime
from playsound import playsound #used to play a sound file
import pyautogui

#sometimes reduced for rapid clicks
normal_delay = 0.25
pyautogui.PAUSE = normal_delay #delay between pyautogui calls
pyautogui.FAILSAFE = True #move mouse to corner to disable

#my helper frunctions used across multiple scripts 
from load_vars import load_vars,val
from z_tools import alert , LocateCenterClickWait

k = 0 #track number of times unable to find an image
sleep(3) #alt tab into ark


#while looking at the grinder in the prone position
def xp(k, eat_drink):
    alert()#play a sound before taking control
    keys,vals = load_vars("vars.txt",'1') #passing the version number that you expect it to be

    pyautogui.keyDown('f') #open grinder
    sleep(3)
    pyautogui.keyUp('f')
    found = False
    sleep(1)

    k,found = LocateCenterClickWait('media/inventory_open',False,2,k)
    if found:
        if eat_drink:
            eat_drink = False
            try_consume()

        pyautogui.click(val('search_x',keys,vals), val('search_y',keys,vals)) #move to search field
        pyautogui.write(val('xp_craft',keys,vals), interval=0.05) #filter out paper
        sleep(0.25)
        pyautogui.click(val('transfer_x1',keys,vals), val('transfer_y',keys,vals)) #transfer all into grinder
        sleep(0.5)

        grind = 0
        pyautogui.PAUSE = 0.05
        while grind < 5:
            pyautogui.click(val('grind_x',keys,vals), val('grind_y',keys,vals)) #Grind All
            grind+=1
        pyautogui.PAUSE = normal_delay

        pyautogui.click(val('search_x2',keys,vals), val('search_y',keys,vals)) # Search Bar in Grinder
        pyautogui.write(val('xp_craft2',keys,vals), interval=0.05) #filter out paper
        sleep(0.25)
        pyautogui.click(val('transfer_x2',keys,vals), val('transfer_y',keys,vals)) # transfer all out of grinder
        sleep(0.25)

        pyautogui.click(val('crafting_x',keys,vals), val('crafting_y',keys,vals)) #crafting tab
        sleep(0.5)
        pyautogui.click(val('search_x',keys,vals), val('search_y',keys,vals)) #move to search field
        pyautogui.write(val('xp_craft',keys,vals), interval=0.05) #filter out paper
        sleep(0.5)
        pyautogui.click(val('first_slot_x',keys,vals), val('first_slot_y',keys,vals)) #click on the top left inventory slot

        #try to grind up everything
        pyautogui.PAUSE = 0.05
        for x in range(11):
            pyautogui.keyDown('a') #try to craft 100
            pyautogui.keyUp('a')

#todo: add this when adding coordinate file
##        #if the grinder was off, turn it on
##        pyautogui.click(1282, 1174) #toggle grinder on/off
##
##        #and grind up everything
##        for x in range(11):
##            pyautogui.keyDown('a') #try to craft 100
##            pyautogui.keyUp('a')


        pyautogui.PAUSE = normal_delay
        
        pyautogui.click(val('close_inv_x',keys,vals), val('close_inv_y',keys,vals)) #close inventory
        sleep(0.25)
    else:
        pass #inventory not open return exit script
    return k,found,eat_drink

#while inventory is closed,
#attempt to use a chili that is in the '0' slot
def useChili():
    sleep(2)
    pyautogui.keyDown('0')
    sleep(0.18)
    pyautogui.keyUp('0')
    sleep(.25)

#while inventory is open
#attempt to search for and consume 1 each: custom food/drink
def try_consume():
    #food
    pyautogui.click(val('search_x',keys,vals), val('search_y',keys,vals)) #move to search field
    pyautogui.write(val('food',keys,vals), interval=0.05) #filter out paper
    sleep(0.25)
    pyautogui.click(val('first_slot_x',keys,vals), val('first_slot_y',keys,vals)) #click on the top left inventory slot
    pyautogui.click(button='right') #right click in top left slot
    sleep(1.5)
    pyautogui.click(val('first_slot_x',keys,vals), val('first_slot_consume_one_offset_y',keys,vals)) #move down to the consume 1 of these
    clear_left_search()

    #water
    pyautogui.click(val('search_x',keys,vals), val('search_y',keys,vals)) #move to search field
    pyautogui.write(val('water',keys,vals), interval=0.05) #filter out paper
    sleep(0.25)
    pyautogui.click(val('first_slot_x',keys,vals), val('first_slot_y',keys,vals)) #click on the top left inventory slot
    pyautogui.click(button='right') #right click in top left slot
    sleep(1.5)
    pyautogui.click(val('first_slot_x',keys,vals), val('first_slot_consume_one_offset_y',keys,vals)) #move down to the consume 1 of these
    clear_left_search()


#todo consolidate pyautogui.click and pyautogui.write into smaller statements
#todo that already know what to do w/ the keys and values

def clear_left_search():
    sleep(1)
    pyautogui.click(val('search_x',keys,vals), val('search_y',keys,vals)) #move to search field
    sleep(0.5)
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('del')

def startup(interval, hours, nth_interval):
    script_start = time.time()
    #Start off the script by printing out the settings
    print("Press escape to bring up in game menu.\nIt will soft stop the script at the end of the next iteration.")
    print("\nCurrent Settings:")
    print("Trying to craft every: {}seconds".format(interval))
    print("Run program for a minimum of: {}hours".format(hours))
    print("Try to eat and drink every: ~{}minutes".format(int(interval*nth_interval/60)))
    return script_start

def shutdown(interval, rounds, consumed):
    #readout of how long it worked for
    a = int(rounds*interval/60) #runtime in minutes
    h = int(a/60) #runtime hours portion
    m = a-(h*60) #runtime minutes portion

    print("\n")
    print("Script completed.")
    print("Total Crafting Rounds: {}!".format(rounds))
    print("Ran for at least: {} hours {} minutes".format(h,m))
##    print("Ran for: {}".format(strftime("%Y, %M, %d, %H:%M:%S", gmtime())
##))
    print("Consumed Food/Water: {}".format(consumed))

    #switch back to script
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')



#--------------------------------------------------------------------------------------
#main script that calls the above functions
#--------------------------------------------------------------------------------------
if __name__ == "__main__":
    #load up the user specific key value pairs
    keys,vals = load_vars("vars.txt",'1') #passing the version number that you expect it to be
    print('Current vars file version: {}'.format(val('file_version',keys,vals)))

    interval = val('grind_interval',keys,vals) # seconds
    hours = val('grind_hours',keys,vals) # minimum hours to run the program for (not including time from sleeps while program is running)
    duration = hours*60*60 # hours represented in seconds

    #todo remove these next two and make it based on wall clock runtime
    #vs rounds that may or may not have found the open inventory image
    rounds = 1 # counting how many times crafted
    nth_interval = 12 # (minimum 1) 1 for every interval, 5 for every 5th interval, etc

    eat_drink = False 
    consumed = 0 #attempts at eating food

    #readout of how it should perform
    script_start = startup(interval, hours, nth_interval)

    #todo
    #while runtime < duration:

    x = 0
    y = round(24*60*60/300,0)
    while x < y:
    #for x in range(duration):
        k,found,eat_drink = xp(k, eat_drink)

        if found:
            useChili()

            #todo
            #calculate how long to sleep for
            #where sleep = (interval) - (runtime mod interval)
            sleep(interval)
            rounds+=1

        #for every nth interval try to eat/drink something
        if rounds % nth_interval == 0:
            eat_drink = True
            #todo is there a way to incorporate the toilet buff into crafting
            #try to poop before each time you eat
            pyautogui.keyDown(val('poop',keys,vals))
            pyautogui.keyUp(val('poop',keys,vals))
            consumed+=1


        k+=1    #this value is reset each time an image is found
        if k > 5:    #keeping track of how many times it was not able to find the inventory
            break    #break out if a certain threshold is reached.
        sleep(1) #sleep for at least 1 second per loop
        x+=1

    #readout of how it performed
    shutdown(interval, rounds, consumed)
