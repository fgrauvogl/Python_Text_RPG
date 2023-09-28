import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random
import Monsters

# Random number generator
level_1num = random.randint(1, 8)
level_2num = random.randint(8, 16)
level_3num = random.randint(16, 24)

# Initialize the game window
game_window = tk.Tk()
game_window.title('Turnika')
game_window.geometry('1024x768')

# Create tabs for different sections of the game
tabs = ttk.Notebook(game_window)
tabs.pack(pady=5)

# Load images
sword = ImageTk.PhotoImage(Image.open('Sword1.png'))
map_img = ImageTk.PhotoImage(Image.open('Map.png'))
warrior_img = ImageTk.PhotoImage(Image.open('Warrior.png'))
archer_img = ImageTk.PhotoImage(Image.open('Archer.png'))
wizard_img = ImageTk.PhotoImage(Image.open('Wizard.png'))

# Create frames for different tabs
main_frame = Frame(tabs, width=800, height=540)
inventory_frame = Frame(tabs, width=800, height=540)
map_frame = Frame(tabs, width=800, height=540)
journal_frame = Frame(tabs, width=800, height=540)

# Create a label to display the map image
map_label = Label(map_frame, image=map_img)
map_label.pack(pady=0)

# Define functions for health management
def lose_health1():
    global level_1num
    if level_1num > 8:
        level_1num = 6
    elif level_1num < 1:
        level_1num = 0
        print('Miss!1')
    else:
        pass

# Similar functions for lose_health2, lose_health3, gain_health1, gain_health2, gain_health3

# Start Screen

# Function to clear the start screen and show the main frame
def clear_start():
    tabs.add(main_frame, text='Main')
    welcome_label.forget()
    start_label.forget()
    start_button.forget()

# Labels and buttons for the start screen
welcome_label = Label(game_window, text="Welcome to Turnika", font='Courier 18 bold')
welcome_label.pack(pady=10)

start_label = Label(game_window, text='Start', font='Courier 18 bold', justify='center')
start_label.pack(side=BOTTOM, pady=25)

start_button = Button(game_window, image=sword, justify='center', command=clear_start, cursor='hand2')
start_button.pack(side=BOTTOM, pady=50)

# Main Tab First Story Lines

# Labels for the main story
first_story = Label(main_frame, text='Long ago when swords and magic existed, three legendary leaders existed.\n\n\n'
                                     'The honorable Nephetus from Drumilin.\n\n\n'
                                     'The barbaric Thesius from Northgaul.\n\n\n'
                                     'The princess Lorica from Ancora.', pady=40, font='Courier 13')
first_story.pack(pady=10)

# Similar labels for second_story, third_story, and fourth_story

# Buttons to continue the story
next_button1 = Button(main_frame, text='Continue', command=move_screens1, cursor='hand2')
next_button2 = Button(main_frame, text='Continue', command=move_screens2, cursor='hand2')
next_button3 = Button(main_frame, text='Continue', command=move_screens3, cursor='hand2')
next_button4 = Button(main_frame, text='Continue', command=move_screen4, cursor='hand2')

# Intro to your character

# Function to explore the character's background
def explore():
    choose_label.destroy()
    warrior_button.destroy()
    archer_button.destroy()
    wizard_button.destroy()
    warrior_header.destroy()
    display_warrior.destroy()
    archer_header.destroy()
    display_archer.destroy()
    wizard_header.destroy()
    display_wizard.destroy()
    classY_button.destroy()
    classN_button.destroy()

# Labels for character introductions
a_intro = Label(journal_frame,
                 text="In order to survive the harsh wilds of your homeland you learned archery.\n"
                      "Your eyesight is keen and you wit sharp.\n"
                      "You've gained a sense of distance from the world.\n"
                      "Woken up by the sound of screams nearby, \n"
                      "you stretch out of the position you held at a tree.\n"
                      "They seem to be coming from the nearby town.\n"
                      "What do you do?", font='Courier 13', pady=20)
war_intro = Label(journal_frame,
                  text="You're strong, stronger than the rest. Brawn was always a feature you've envied.\n"
                       "Your swing is enough to take down an orc.\n"
                       "There are many who look up to strength.\n"
                       "In the distance there are screams coming from center square.\n"
                       "What do you do?", font='Courier 13', pady=20)
wiz_intro = Label(journal_frame, text="e", font='Courier 13', pady=20)

# Buttons to choose character class
classY_button = Button(main_frame, text='Yes', font='Courier 11 bold', cursor='hand2', padx=60, command=explore)
classN_button = Button(main_frame, text=' No ', font='Courier 11 bold', cursor='hand2', padx=20, command=return_screen)

# Functions to choose character class
def choose_warrior():
    choose_label.forget()
    warrior_button.forget()
    archer_button.forget()
    wizard_button.forget()
    warrior_header.pack()
    display_warrior.pack()
    classY_button.pack()
    classN_button.pack()

def choose_archer():
    Archer()
    choose_label.forget()
    warrior_button.forget()
    archer_button.forget()
    wizard_button.forget()
    archer_header.pack()
    display_archer.pack()
    classY_button.pack()
    classN_button.pack()

def choose_wizard():
    Wizard()
    choose_label.forget()
    warrior_button.forget()
    archer_button.forget()
    wizard_button.forget()
    wizard_header.pack()
    display_wizard.pack()
    classY_button.pack()
    classN_button.pack()

# Character classes
class Warrior:
    health = 200
    is_warrior = True
    print(health)
    lose_health1()
    print(health)

class Archer:
    is_archer = True
    max_health = 120

class Wizard:
    is_wizard = True
    max_health = 100

# Labels and buttons for choosing character
choose_label = Label(main_frame, text='Choose Your Character!', justify='center', font='Courier 18 bold')
warrior_button = Button(main_frame, pady=10, text='Warrior', command=choose_warrior,
                        cursor='hand2', font='Courier 18 bold')
archer_button = Button(main_frame, pady=10, text='Archer', command=choose_archer,
                       cursor='hand2', font='Courier 18 bold')
wizard_button = Button(main_frame, pady=10, text='Wizard', command=choose_wizard,
                       cursor='hand2', font='Courier 18 bold')

# Start the game window
game_window.mainloop()

