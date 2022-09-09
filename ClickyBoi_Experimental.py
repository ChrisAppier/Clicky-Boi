"""
Clicks both mouse buttons for 1-10 ms every 3-8 min

Author: Chris Appier
Created: 09/09/2022
"""
#%% Imports
import time
import random
import mouse
import keyboard
import tkinter as tk
from tkinter import filedialog as fd
from threading import Thread
import os

#%% Functions
def start():
    '''Starts the program'''
    
    global loop    
    loop = 0 #activating clicking loop
    
    if login.get() == 1: #launch WoW if necessary
        launch()
        time.sleep(30)
        
        keyboard.write(user)
        time.sleep(1)
        keyboard.press_and_release('tab')
        time.sleep(1)
        keyboard.write(passw)
        time.sleep(10)
        keyboard.press_and_release('return')
        
    
    t = Thread(target=clicking) #using a single thread for clicking loop
    t.start() 

def clicking():
    '''Clicks to move character'''
    
    global loop
    
    while loop == 0:
        wait = random.randrange(180,480,1)
        sleep = random.randrange(1,10,1)/100

        time.sleep(wait)
        
        if loop == 1:
            break
        
        mouse.hold(button='left')
        mouse.hold(button='right')
        time.sleep(sleep)
        mouse.release(button='left')
        mouse.release(button='right')

def stop():
    '''Stops the program'''
    
    global loop
    loop = 1

def launch():
    '''Starts the game based on the selected file'''
    
    os.system(file.get())
    
def select_file():
    '''Allows the user to select the game file'''
    
    file.set(fd.askopenfilename(title='Select a game file'))
    
    return str(file)

#%% Variables
window = tk.Tk()
loop = 1
login = tk.IntVar()
file = tk.StringVar()
user = tk.StringVar()
passw = tk.StringVar()

#%% Populating Window
window.title('Clicky Boi')
window.geometry('1000x500')
window.resizable(False, False)

#Game file selection
btn_file = tk.Button(window, text="Game File", command=select_file)

#Login options
cbx_file = tk.Checkbutton(window, text='Log me in', variable=login).pack()
lbl_user = tk.Label(window, text='User Name').pack()
ent_user = tk.Entry(window, textvariable=user).pack()
lbl_pass = tk.Label(window, text='Password').pack()
ent_pass = tk.Entry(window, textvariable=passw).pack()

#Start and stop buttons
start_button = tk.Button(window, text='Start', width=10, command=start).pack()
stop_button = tk.Button(window, text='Stop', width=10, command=stop).pack()

window.mainloop()

#%%To Do List
#TODO Add ability to open WoW Classic
#TODO Add username/password inputs
#TODO Add ability to join queue
#TODO Add ability to choose when to open game
#TODO Add timeout to logoff
#TODO Add switch for logged in vs out
