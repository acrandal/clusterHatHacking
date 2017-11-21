#!/usr/bin/env python

import time
import subprocess
import datetime
import sys
from subprocess import Popen, PIPE

PAUSETIME = 0.2
DEBUG = False

def bong():
    subprocess.check_output(["mpg123", "cuckoo_clock.mp3"], stderr=subprocess.STDOUT)

def tick_clock( force_bong ):
    if DEBUG: print(" [x] Current time: " + str(time.asctime()))
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute

    minute = int(minute)
    hour = int(hour) % 12   # don't need a 24 hour clock. :-)

    if minute == 30:
        if DEBUG: print(" [x] It's half past, so sing once")
        bong()
    elif minute == 0 or force_bong:
        if DEBUG: print(" [x] It's on the hour, so bong the hour")
        for i in range(hour):
            bong()
            time.sleep(PAUSETIME)
    else:
        if DEBUG: print(" [x] Not time to cuckoo")

if __name__ == "__main__":

    force_hour_bong = False
    if( len(sys.argv) > 1 ):
        for i in range(1,len(sys.argv)):
            if( sys.argv[i] == "-f" ):
                force_hour_bong = True
            if( sys.argv[i] == "-d" or sys.argv[i] == "--debug" ):
                DEBUG = True


    if DEBUG: print("[x] Starting Clock")
    tick_clock( force_hour_bong )
    if DEBUG: print("[x] Out of time!")
