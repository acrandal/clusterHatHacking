#!/usr/bin/env python

from random import randint
import time
from time import sleep
from time import time, gmtime, strftime
import datetime

import unicornhat as unicorn

print("""Snow

Draws random white pixels to look like a snowstorm.

If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.3)
width,height=unicorn.get_shape()


rows = []
screen_choice = 1

WHITE = (150,150,150)
RED = (200,0,0)
OFF = (0,0,0)


def init():

    # create a buffer of <height> blank rows
    for i in range(height):
        rows.append(get_blank_row())

'''
 Make a screen for the clock
'''
def get_clock_screen():
    scr = []
    for i in range(height):
        scr.append(get_blank_row())

    #print strftime("%H:%M:%S %Z", gmtime())
    #print(datetime.datetime.now())
    print(datetime.datetime.now().strftime('%H:%M:%S'))
    timestr = datetime.datetime.now().strftime('%H6%M6%S')

    timeNums = list(timestr)
    timeNums = map(int, timeNums)

    binNums = []
    for num in timeNums:
        binNum = bin(num)[2:].zfill(4)
        binNums.append(list(binNum))
        print binNum

    print binNums
    for num in range( len(binNums) ):
        #print binNums[num]
        binNum = binNums[num]
        for idx in range( len( binNum ) ):
            #print idx
            scr[idx][num] = binNum[idx]

    for h in range(height):
        for w in range(width):
            # val is between 50 and 255
            val = scr[h][w]

            color = RED
            if w == 2 or w == 5:
                color = WHITE

            if val == '1':
                scr[h][w] = color
            else:
                scr[h][w] = OFF
    return(scr)


def get_blank_row():

    # generate a blank row
    return [OFF] * width


def update_display():
    global rows
    # keep track of the row we are updating
    for h in range(height):
        for w in range(width):
            # val is between 50 and 255
            val = rows[h][w]
            #print(rows)
            print str(h) + "  " + str(w) + "  " + str(val)

            # invert coordinates
            #unicorn.set_pixel((width - 1) - w, (height - 1) - h, val, val, val)
            #unicorn.set_pixel(w, h, val, val, val)
            (r,g,b) = val
            unicorn.set_pixel(w, h, r, g, b)
    print ""
    unicorn.show()


def step():
    global rows
    global screen_choice
    scr = get_clock_screen()
    rows = scr
    update_display()

#** Begin code here **#
init()
while True:
    step()
    sleep(1.0)
