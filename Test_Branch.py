import random
import pygame

# ---------------------------------------------------------------------------
# Level "progress" numbers
# ---------------------------------------------------------------------------

level_1num = random.randint(1, 8)
level_2num = random.randint(8, 16)
level_3num = random.randint(16, 24)

LEVEL_RULES = {
    1: {"high": 8, "high_reset": 6},
    2: {"high": 16, "high_reset": 14},
    3: {"high": 28, "high_reset": 26}
}


# ---------------------------------------------------------------------------
# Character model
# ---------------------------------------------------------------------------

class Character:
    def __init__(self, name: str, max_health: int):
        self.name = name
        self.max_health = max_health
        self.health = max_health

    def lose_health(self, amount):
        if (amount > 0) and ((self.health - amount <= 0)):
            self.health -= random.randint(1 + abs(amount), min(abs(amount * .25)), int(self.health))

    # Additional logic can be added here to manage health gains or resets


# ---------------------------------------------------------------------------
# Window / tabs
# ---------------------------------------------------------------------------

screen_dimensions = pygame.display.Info()
width, height = screen_dimensions.current_w, screen_dimensions.current_h

pygame.init()

game_window = pygame.Surface((800, 540))


def main():
    print(f"Screen Resolution: {width} x {height}")


if __name__ == "__main__":
    # Start Screen
    welcome_label_text = "Welcome to Turnika"
    start_label_text = 'Start'

    # Initialize the window and add frames

    pygame.display.set_caption('Turnika')

# ---------------------------------------------------------------------------
# Main Tab First Story Lines
# ---------------------------------------------------------------------------

first_story_text = ('In an age when steel sang and sorcery ran deep, three sovereigns held the realm.\n\n\n'
                    'The steadfast Aldric of Velmora.')
second_story_text = ("For generations the lands rested in quiet harmony under their watch.")
third_story_text = "Now the tale reaches your hands."
fourth_story_text = ""

# ---------------------------------------------------------------------------
# Choose character
# ---------------------------------------------------------------------------

warrior_button_text, warrior_image = pygame.image.load('Warrior.png'), pygame.image.load('Sword_New.png')
archer_button_text, archer_image = pygame.image.load('Archer.png'), pygame.Surface((1024, 536))
wizard_button_text, wizard_image = pygame.image.load('Wizard.png'), pygame.Surface((897.2, 536))


# ---------------------------------------------------------------------------
# Function to handle button press
def choose_class(class_name):
    global current_class

    if class_name == "warrior":
        display_warrior_image()

    elif class_name == "archer":
    # Display archer image and text here

    else:
        wizard_button_text, wizard_image = pygame.image.load('Wizard.png'), pygame.Surface((897.2, 536))


# ---------------------------------------------------------------------------
# Main loop
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and (event.button & pygame.BUTTON_LEFT):
    # Handle button press here

