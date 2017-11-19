#!/usr/bin/env python

from random import randint
from time import sleep

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

def get_jo_screen():
    scr = []
    for i in range(height):
        scr.append(get_blank_row())
    scr[2][0] = WHITE
    scr[3][1] = WHITE
    scr[0][1] = WHITE
    scr[0][2] = WHITE
    scr[0][3] = WHITE
    scr[1][2] = WHITE
    scr[2][2] = WHITE

    scr[0][5] = WHITE
    scr[0][6] = WHITE
    scr[1][4] = WHITE
    scr[1][7] = WHITE
    scr[2][4] = WHITE
    scr[2][7] = WHITE
    scr[3][5] = WHITE
    scr[3][6] = WHITE


    return(scr)

'''
 Make a screen for the I + heart
'''
def get_heart_screen():
    scr = []
    for i in range(height):
        scr.append(get_blank_row())

    scr[0][0] = WHITE
    scr[0][1] = WHITE
    scr[0][2] = WHITE
    scr[1][1] = WHITE
    scr[2][1] = WHITE
    scr[3][0] = WHITE
    scr[3][1] = WHITE
    scr[3][2] = WHITE
    scr[0][4] = RED
    scr[0][6] = RED
    scr[1][3] = RED
    scr[1][4] = OFF
    scr[1][5] = RED
    scr[1][6] = OFF
    scr[1][7] = RED
    scr[2][4] = RED
    scr[2][5] = OFF
    scr[2][6] = RED
    scr[3][5] = RED
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
    scr = 1
    if screen_choice == 1:
        scr = get_heart_screen()
        screen_choice = 2
    elif screen_choice == 2:
        scr = get_jo_screen()
        screen_choice = 1

    rows = scr
    update_display()

#** Begin code here **#
init()
while True:
    step()
    sleep(0.9)
