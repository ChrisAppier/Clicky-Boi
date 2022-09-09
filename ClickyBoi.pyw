"""
Clicks both mouse buttons for 1-10 ms every 3-8 min

Author: Chris Appier
Created: 09/09/2022
"""
#%% Imports
import time
import random
import mouse
import tkinter as tk
from threading import Thread

#%% Functions
def start_thread():
    global loop
    
    loop.set(0)
    
    start_button.configure(bg='green')
    
    t.start()

def clicking():
    global loop
    
    while loop == 0:
        wait = random.randrange(180,480,1)
        print(wait)
        sleep = random.randrange(1,10,1)/100

        time.sleep(wait)
        
        if loop == 1:
            break
        
        mouse.hold(button = 'left')
        mouse.hold(button = 'right')
        time.sleep(sleep)
        mouse.release(button = 'left')
        mouse.release(button = 'right')

def stop():
    global loop
    loop.set(1)
    
    start_button.configure(bg='SystemButtonFace')

#%% Variables
window = tk.Tk()
loop = tk.IntVar()
loop.set(1)
t = Thread(target=clicking)

#%% Populating Window
window.title('Clicky Boi')
window.geometry('100x50+50+50')
window.resizable(False, False)

start_button = tk.Button(window, text = 'Start', width = 10, command=start_thread)
start_button.pack()
stop_button = tk.Button(window, text = 'Stop', width = 10, command=stop).pack()

window.mainloop()

loop.set(1)

