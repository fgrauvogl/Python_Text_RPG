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


# Lose Health


def lose_health1():
    global level_1num
    if level_1num > 8:
        level_1num = 6
    elif level_1num < 1:
        level_1num = 0
        print('Miss!1')
    else:
        pass


def lose_health2():
    global level_2num
    if level_2num > 16:
        level_2num = 14
    elif level_2num == 6:
        level_2num = 8
    elif level_2num < 5:
        level_2num = 0
        print('Miss!2')
    else:
        pass


def lose_health3():
    global level_3num
    if level_3num > 28:
        level_3num = 26
    elif level_3num == 8:
        level_3num = 12
    elif level_3num < 7:
        level_3num = 0
        print('Miss!3')
    else:
        pass


# Gain Health


def gain_health1():
    global level_1num
    if level_1num > 8:
        level_1num = 6
    elif level_1num < 3:
        level_1num = 4
    else:
        pass


def gain_health2():
    global level_2num
    if level_2num > 16:
        level_2num = 14
    elif level_2num < 6:
        level_2num = 8
    else:
        pass


def gain_health3():
    global level_3num
    if level_3num > 28:
        level_3num = 26
    elif level_3num < 10:
        level_3num = 12
    else:
        pass


game_window = tk.Tk()
game_window.title('Turnika')
game_window.geometry('1024x768')

tabs = ttk.Notebook(game_window)
tabs.pack(pady=5)

sword = ImageTk.PhotoImage(Image.open('Sword1.png'))
map_img = ImageTk.PhotoImage(Image.open('Map.png'))
warrior_img = ImageTk.PhotoImage(Image.open('Warrior.png'))
archer_img = ImageTk.PhotoImage(Image.open('Archer.png'))
wizard_img = ImageTk.PhotoImage(Image.open('Wizard.png'))

main_frame = Frame(tabs, width=800, height=540)
inventory_frame = Frame(tabs, width=800, height=540)
map_frame = Frame(tabs, width=800, height=540)
journal_frame = Frame(tabs, width=800, height=540)

map_label = Label(map_frame, image=map_img)
map_label.pack(pady=0)


# Start Screen


def clear_start():
    tabs.add(main_frame, text='Main')
    welcome_label.forget()
    start_label.forget()
    start_button.forget()


welcome_label = Label(game_window, text="Welcome to Turnika", font='Courier 18 bold')
welcome_label.pack(pady=10)

start_label = Label(game_window, text='Start', font='Courier 18 bold', justify='center')
start_label.pack(side=BOTTOM, pady=25)

start_button = Button(game_window, image=sword, justify='center', command=clear_start, cursor='hand2')
start_button.pack(side=BOTTOM, pady=50)

# Main Tab First Story Lines
first_story = Label(main_frame, text='Long ago when swords and magic existed, three legendary leaders existed.\n\n\n'
                                     'The honorable Nephetus from Drumilin.\n\n\n'
                                     'The barbaric Thesius from Northgaul.\n\n\n'
                                     'The princess Lorica from Ancora.', pady=40,
                    font='Courier 13')
first_story.pack(pady=10)

second_story = Label(main_frame, text='The three kingdoms were at peace with the land for many years.\n\n\n'
                                      'During the rule of the three there was a sickness that struck the land.\n\n\n'
                                      'Living beings that were affected grew in size and strength.\n\n\n'
                                      'Household felines became predators, humans lost their sense of self,\n\n\n'
                                      'and even common rats became a danger.', pady=40, font='Courier 13')

third_story = Label(main_frame, text='The leaders took up their arms and \n\n'
                                     'went to war with the abominations.\n\n'
                                     'The many deaths that happened after included Thesius.\n\n'
                                     'Although hope may have seemed lost a guild was started by Nephetus.\n\n'
                                     'One that vowed to the eradication of this sickness.\n\n'
                                     'Through the organization of this guild many discoveries were made. \n\n'
                                     'Lorica, on the other hand, introduced democracy to the masses. \n\n'
                                     'With the organization between the two the kingdoms felt they had a chance.\n\n'
                                     'Still the sickness ravages... \n\n'
                                     ' there are few who take a stand to reclaim lost land.\n\n',
                    pady=40, font='Courier 13')

fourth_story = Label(main_frame, text='This is where you come in to our story.\n\n\n'
                                      'Choose who you will become and uncover the mystery of Turnika.\n\n\n',
                     pady=40, font='Courier 13')


def move_screens1():
    first_story.destroy()
    second_story.pack(pady=10)
    next_button1.destroy()
    next_button2.pack(side=RIGHT, padx=15)


next_button1 = Button(main_frame, text='Continue', command=move_screens1, cursor='hand2')
next_button1.pack(side=RIGHT, padx=15)


def move_screens2():
    second_story.destroy()
    third_story.pack(pady=10)
    next_button2.destroy()
    next_button3.pack(side=RIGHT, padx=15)


next_button2 = Button(main_frame, text='Continue', command=move_screens2, cursor='hand2')


def move_screens3():
    third_story.destroy()
    fourth_story.pack(pady=10)
    next_button3.destroy()
    next_button4.pack(side=RIGHT, padx=15)


next_button3 = Button(main_frame, text='Continue', command=move_screens3, cursor='hand2')


def move_screen4():
    tabs.add(inventory_frame, text='Inventory')
    tabs.add(map_frame, text='Map')
    tabs.add(journal_frame, text='Journal')
    fourth_story.destroy()
    next_button4.destroy()
    choose_label.pack(pady=10)
    warrior_button.pack(pady=20)
    archer_button.pack(pady=30)
    wizard_button.pack(pady=40)


next_button4 = Button(main_frame, text='Continue', command=move_screen4, cursor='hand2')


# Intro to your character


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

    a_intro = LabelFrame(journal_frame,
                         text="In order to survive the harsh wilds of your homeland you learned archery.\n"
                              "Your eyesight is keen and you wit sharp.\n"
                              "You've gain a sense of distance from the world.\n"
                              "Woken up by the sound of screams nearby, \n"
                              "you stretch out of the position you held at a tree.\n"
                              "They seem to be coming from the nearby town.\n"
                              "What do you do?", font='Courier 13', pady=20)
    war_intro = Label(journal_frame,
                      text="You're strong, stronger than the rest. Brawn was always a feature you've envied.\n"
                           "You're swing is enough to take down an orc.\n"
                           "There are many who look up to strength.\n"
                           "In the distance there are screams coming from center square.\n"
                           "What do you do?", font='Courier 13', pady=20)
    wiz_intro = Label(journal_frame, text="e", font='Courier 13', pady=20)

    if is_archer:
        a_intro.pack()
    elif is_warrior:
        war_intro.pack()
    elif is_wizard:
        wiz_intro.pack()


# Choose Character


def return_screen():
    choose_label.pack(pady=10)
    warrior_button.pack(pady=20)
    archer_button.pack(pady=30)
    wizard_button.pack(pady=40)
    warrior_header.forget()
    display_warrior.forget()
    archer_header.forget()
    display_archer.forget()
    wizard_header.forget()
    display_wizard.forget()
    classY_button.forget()
    classN_button.forget()


display_warrior = Label(main_frame, image=warrior_img)
warrior_header = Label(main_frame, text='You have chosen the warrior class?', font='Courier 18 bold', pady=10)
display_archer = Label(main_frame, image=archer_img)
archer_header = Label(main_frame, text='You have chosen the archer class?', font='Courier 18 bold', pady=10)
display_wizard = Label(main_frame, image=wizard_img)
wizard_header = Label(main_frame, text='You have chosen the wizard class?', font='Courier 18 bold', pady=10)
classY_button = Button(main_frame, text='Yes', font='Courier 11 bold', cursor='hand2', padx=60, command=explore)
classN_button = Button(main_frame, text=' No ', font='Courier 11 bold', cursor='hand2', padx=20, command=return_screen)


def choose_warrior():
    choose_label.forget()
    warrior_button.forget()
    archer_button.forget()
    wizard_button.forget()
    warrior_header.pack()
    display_warrior.pack()
    classY_button.pack()
    classN_button.pack()


is_warrior = False


class Warrior:
    health = 200
    is_warrior = True
    print(health)
    lose_health1()
    print(health)


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


is_archer = False


class Archer:
    is_archer = True
    max_health = 120


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


is_wizard = False


class Wizard:
    is_wizard = True
    max_health = 100


choose_label = Label(main_frame, text='Choose Your Character!', justify='center', font='Courier 18 bold')

warrior_button = Button(main_frame, pady=10, text='Warrior', command=choose_warrior,
                        cursor='hand2', font='Courier 18 bold')

archer_button = Button(main_frame, pady=10, text='Archer', command=choose_archer,
                       cursor='hand2', font='Courier 18 bold')

wizard_button = Button(main_frame, pady=10, text='Wizard', command=choose_wizard,
                       cursor='hand2', font='Courier 18 bold')


game_window.mainloop()
