import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random
import pygame
#import Monsters

# ---------------------------------------------------------------------------
# Level "progress" numbers
# ---------------------------------------------------------------------------

level_1num = random.randint(1, 8)
level_2num = random.randint(8, 16)
level_3num = random.randint(16, 24)

level_nums = {
    1: random.randint(1, 8),
    2: random.randint(8, 16),
    3: random.randint(16, 24),
}

# high        -> value that counts as "too high", gets reset to high_reset
# equal       -> a specific value that snaps to equal_reset (None if unused)
# low         -> value below which it's treated as a miss and zeroed
# gain_low    -> value below which gaining resets to gain_low_reset

LEVEL_RULES = {
    1: {"high": 8, "high_reset": 6, "equal": 0, "equal_reset": 0,
        "low": 1, "gain_low": 3, "gain_low_reset": 4},
    2: {"high": 16, "high_reset": 14, "equal": 6, "equal_reset": 8,
        "low": 5, "gain_low": 6, "gain_low_reset": 8},
    3: {"high": 28, "high_reset": 26, "equal": 8, "equal_reset": 12,
        "low": 7, "gain_low": 10, "gain_low_reset": 12},
}


def lose_health(level):
    rules = LEVEL_RULES[level]
    value = level_nums[level]
    if value > rules["high"]:
        value = rules["high_reset"]
    elif rules["equal"] is not None and value == rules["equal"]:
        value = rules["equal_reset"]
    elif value < rules["low"]:
        value = 0
        print(f"Miss!{level}")
    level_nums[level] = value


def gain_health(level):
    rules = LEVEL_RULES[level]
    value = level_nums[level]
    if value > rules["high"]:
        value = rules["high_reset"]
    elif value < rules["gain_low"]:
        value = rules["gain_low_reset"]
    level_nums[level] = value

# ---------------------------------------------------------------------------
# Character model
# ---------------------------------------------------------------------------

class Character:
    def __init__(self, name: str, max_health: int):
        self.name = name
        self.max_health = max_health
        self.health = max_health

    def lose_health(self, amount):
        self.health = max(0, self.health - amount)

    def gain_health(self, amount):
        self.health = min(self.max_health, self.health + amount)

    def __repr__(self):
        return f"Character({self.name}, {self.health}/{self.max_health})"

CLASS_MAX_HEALTH = {
    "warrior": 200,
    "archer": 120,
    "wizard": 100,
}


def get_screen_dimensions():
    return {'width': int(pygame.display.Info().current_w), 'height': int(pygame.display.Info().current_h)}

# ---------------------------------------------------------------------------
# Window / tabs / images
# ---------------------------------------------------------------------------
screen_dimensions = get_screen_dimensions()
width = screen_dimensions['width']
height = screen_dimensions['height']

game_window = tk.Tk()
game_window.title('Turnika')
game_window.geometry("2560x1440")

def main():
    print(f"Screen Resolution: {width} x {height}")

if __name__ == "__main__":
    pygame.init()

tabs = ttk.Notebook(game_window)
tabs.pack(pady=5)

sword = ImageTk.PhotoImage(Image.open('Sword_New.png'))
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

# ---------------------------------------------------------------------------
# Start screen
# ---------------------------------------------------------------------------

def clear_start():
    tabs.add(main_frame, text='Main')
    welcome_label.forget()
    start_label.forget()
    start_button.forget()


welcome_label = tk.Label(game_window, text="Welcome to Turnika", font='Courier 18 bold')
welcome_label.pack(pady=10)

start_label = tk.Label(game_window, text='Start', font='Courier 18 bold', justify='center')
start_label.pack(side="bottom", pady=25)

start_button = tk.Button(game_window, image=sword, justify='center', command=clear_start, cursor='hand2')
start_button.pack(side="bottom")

# Main Tab First Story Lines
first_story = tk.Label(main_frame, text='In an age when steel sang and sorcery ran deep, three sovereigns held the realm.\n\n\n'
                                     'The steadfast Aldric of Velmora.\n\n\n'
                                     'The untamed Kaelen of Duskreach.\n\n\n'
                                     'The queen Seraphine of Aurelia.', pady=40, padx=50,
                    font='Courier 13')
first_story.pack(pady=40,padx=50)

second_story = tk.Label(main_frame, text='For generations the lands rested in quiet harmony under their watch.\n\n\n'
                                      'Then a creeping blight seeped into the soil and the blood alike.\n\n\n'
                                      'Those it touched swelled beyond all natural measure.\n\n\n'
                                      'Garden hounds turned ravenous, citizens forgot their own names,\n\n\n'
                                      'and field mice grew large enough to drag travelers down.', pady=40, font='Courier 13')

third_story = tk.Label(main_frame, text='The three drew their blades and marched against the corrupted horde.\n\n\n'
                                     'Kaelen fell in the second week, his body consumed by the very rot he fought.\n\n\n'
                                     'Yet from the ashes of that defeat, Aldric forged an order.\n\n\n'
                                     'Sworn hunters bound to purge the blight from every corner of the land.\n\n\n'
                                     'Their expeditions uncovered old wards and forgotten cures.\n\n\n'
                                     'Seraphine, meanwhile, opened the council halls to common folk.\n\n\n'
                                     'Together their efforts gave the kingdoms something they had not felt in years:\n\n\n'
                                     'a reason to hold the line. Still the blight spreads...\n\n\n'
                                     'few remain willing to walk into its shadow.', pady=40, font='Courier 13')

fourth_story = tk.Label(main_frame, text='Now the tale reaches your hands.\n\n\n'
                                      'Choose who you will become and unravel the truth behind Veyra.\n\n\n',
                     pady=40, font='Courier 13')

story_screens = [first_story, second_story, third_story, fourth_story]
story_index = 0

first_story.pack(pady=10)  # starting screen


def advance_story():
    global story_index
    story_screens[story_index].destroy()
    story_index += 1

    if story_index < len(story_screens):
        story_screens[story_index].pack(pady=10)
        update_back_button()
    else:
        continue_button.destroy()
        back_button.destroy()
        finish_intro()


def go_back():
    global story_index
    story_screens[story_index].destroy()
    story_index -= 1
    story_screens[story_index].pack(pady=10)
    update_back_button()


def update_back_button():
    # Disable Back on the very first screen -- nothing earlier to return to.
    back_button.config(state='disabled' if story_index == 0 else 'normal')


def finish_intro():
    tabs.add(inventory_frame, text='Inventory')
    tabs.add(map_frame, text='Map')
    tabs.add(journal_frame, text='Journal')
    choose_label.pack(pady=10)
    warrior_button.pack(pady=20)
    archer_button.pack(pady=30)
    wizard_button.pack(pady=40)


continue_button = tk.Button(main_frame, text='Continue', command=advance_story, cursor='hand2')
continue_button.pack(side="right", padx=15)

back_button = tk.Button(main_frame, text='Back', command=go_back, cursor='hand2', state='disabled')
back_button.pack(side="left", padx=15)


# ---------------------------------------------------------------------------
# Class intro screens (journal tab)
# ---------------------------------------------------------------------------

a_intro = tk.LabelFrame(journal_frame,
                     text="Surviving the harsh wilds of your homeland taught you archery.\n"
                          "Your eyes are keen, your wit sharp.\n"
                          "You've gained a sense of distance from the world.\n"
                          "Screams nearby jolt you awake, and you stretch out\n"
                          "from the spot you'd been holding against a tree.\n"
                          "The sound seems to be coming from the nearby town.\n"
                          "What do you do?",
                     font='Courier 13', pady=20)

war_intro = tk.Label(journal_frame,
                  text="You're strong — stronger than the rest. Brawn was always\n"
                       "the one feature you envied.\n"
                       "Your swing is enough to take down an orc.\n"
                       "Many look up to strength.\n"
                       "In the distance, screams echo from the center square.\n"
                       "What do you do?",
                  font='Courier 13', pady=20)

wiz_intro = tk.Label(journal_frame, text="e", font='Courier 13', pady=20)


def explore():
    # Tear down the class-selection confirmation widgets...
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

    # ...then show the matching journal intro. This is the block that was
    # previously floating outside any function (the IndentationError) and
    # checking is_archer/is_warrior/is_wizard flags that never got set.
    if current_class == "archer":
        a_intro.pack()
    elif current_class == "warrior":
        war_intro.pack()
    elif current_class == "wizard":
        wiz_intro.pack()

# ---------------------------------------------------------------------------
# Choose character
# ---------------------------------------------------------------------------

display_warrior = tk.Label(main_frame, image=warrior_img)
warrior_header = tk.Label(main_frame, text='You have chosen the warrior class?', font='Courier 18 bold', pady=10)
display_archer = tk.Label(main_frame, image=archer_img)
archer_header = tk.Label(main_frame, text='You have chosen the archer class?', font='Courier 18 bold', pady=10)
display_wizard = tk.Label(main_frame, image=wizard_img)
wizard_header = tk.Label(main_frame, text='You have chosen the wizard class?', font='Courier 18 bold', pady=10)

classY_button = tk.Button(main_frame, text='Yes', font='Courier 11 bold', cursor='hand2', padx=60, command=explore)
classN_button = tk.Button(main_frame, text=' No ', font='Courier 11 bold', cursor='hand2', padx=20, command=lambda: return_screen())

choose_label = tk.Label(main_frame, text='Choose Your Character!', justify='center', font='Courier 18 bold')

warrior_button = tk.Button(main_frame, pady=10, text='Warrior', command=lambda: choose_class('warrior'),
                        cursor='hand2', font='Courier 18 bold')
archer_button = tk.Button(main_frame, pady=10, text='Archer', command=lambda: choose_class('archer'),
                       cursor='hand2', font='Courier 18 bold')
wizard_button = tk.Button(main_frame, pady=10, text='Wizard', command=lambda: choose_class('wizard'),
                       cursor='hand2', font='Courier 18 bold')

CLASS_WIDGETS = {
    "warrior": (warrior_header, display_warrior),
    "archer": (archer_header, display_archer),
    "wizard": (wizard_header, display_wizard),
}


def choose_class(class_name):
    global current_class, player
    current_class = class_name
    player = Character(class_name, CLASS_MAX_HEALTH[class_name])

    choose_label.forget()
    warrior_button.forget()
    archer_button.forget()
    wizard_button.forget()

    header, display = CLASS_WIDGETS[class_name]
    header.pack()
    display.pack()
    classY_button.pack()
    classN_button.pack()


def return_screen():
    global current_class, player
    choose_label.pack(pady=10)
    warrior_button.pack(pady=20)
    archer_button.pack(pady=30)
    wizard_button.pack(pady=40)

    for header, display in CLASS_WIDGETS.values():
        header.forget()
        display.forget()
    classY_button.forget()
    classN_button.forget()

    current_class = None
    player = None


game_window.mainloop()
