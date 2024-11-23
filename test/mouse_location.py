from time import sleep
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        r,g,b = pyautogui.pixel(x, y)
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + '   R: ' + str(r).rjust(3) + ' G: ' + str(g).rjust(3) + ' B: ' + str(b).rjust(3)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        sleep(.1)
except KeyboardInterrupt:
    print('\n')
