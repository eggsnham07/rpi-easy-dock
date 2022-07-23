#!/usr/bin/python3

import RPi.GPIO as gpio
from time import sleep
import easygui
import sys
import os

sys.path.append("/var")

"""
########################################
################ README ################
########################################

Pin Layout:

    left-left button: 31
    left-right button: 29
    middle button: 15
    right-left button: 13
    right-right button: 11

    buzzer: 35

    LED: 37
"""

buttons = [
    False,
    False,
    False,
    False,
    False
]

def setup():
    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)
    
    gpio.setup(8, gpio.OUT)
    
    gpio.setup(11, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.setup(13, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.setup(15, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    
    gpio.setup(29, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.setup(31, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.setup(33, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.setup(35, gpio.OUT)
    gpio.setup(37, gpio.OUT)
    
    gpio.output(8, gpio.HIGH)
    

setup()

def beep(pin:int):
    gpio.output(pin, gpio.HIGH)
    sleep(0.1)
    gpio.output(pin, gpio.LOW)
    sleep(0.1)
    
def end():
    gpio.output(8, gpio.LOW)
    i = 0
            
    while i < config["exit-beeps"]:
        beep(35)
        i += 1

    gpio.cleanup()
    
    exit(0)


while True:
    if gpio.input(33) == gpio.HIGH:
        qt = easygui.ynbox("Are you sure you want to quit EasyBoard?", "Confirm", ("Yes", "No"))
        if qt == True:
            end()
            
    # Button 1
    if gpio.input(11) == gpio.HIGH and buttons[0] == False:
        os.system(config["binds"]["right-right"])
        buttons[0] = True
    else:
        buttons[0] = False
        
    # Button 2  
    if gpio.input(13) == gpio.HIGH and buttons[1] == False:
        os.system(config["binds"]["right-left"])
        buttons[1] = True
    else:
        buttons[1] = False
        
    # Button 3    
    if gpio.input(15) == gpio.HIGH and buttons[2] == False:
        os.system(config["binds"]["middle"])
        buttons[2] = True
    else:
        buttons[2] = False
        
    # Button 4 
    if gpio.input(29) == gpio.HIGH and buttons[3] == False:
            os.system(config["binds"]["left-right"])
            buttons[3] = True
    else:
        buttons[3] = False
        
    # Button 5
    if gpio.input(31) == gpio.HIGH and buttons[4] == False:
        os.system(config["binds"]["left-left"])
        buttons[4] = True
    else:
        buttons[4] = False