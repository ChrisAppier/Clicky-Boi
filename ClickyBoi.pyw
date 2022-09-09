"""
Clicks both mouse buttons for 1 ms +/1 0.1ms every 5 min +/- 3 min

Author: Chris Appier
Created: 09/09/2022
"""
#%% Imports
import time
import random
import mouse
import tkinter as tk
from tkinter import tix

#%% Functions
def start():

    while loop == 0:
        wait = random.randrange(180,480,1)
        sleep = random.randrange(1,10,1)/100

        time.sleep(wait)
        mouse.press(button = 'left')
        mouse.press(button = 'right')
        time.sleep(sleep)
        mouse.press(button = 'left')
        mouse.press(button = 'right')

def stop():
    loop = 0

#%% Variables
loop = 1

#%% Populating Window
window = tix.Tk()
window.title('Clicky Boi')
window.geometry('100x300+50+50')
window.resizable(False, False)

start_button = tk.Button(window, text = 'Start', width = 10, command=start)
start_button.pack()
stop_button = tk.Button(window, text = 'Stop', width = 10, command=stop)
stop_button.pack()
