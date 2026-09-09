# Turnika
 
A text-driven fantasy RPG built with Python and Tkinter. Choose your class, follow the opening story, and explore the world of Veyra as the blight spreads.
 
## Story
 
Three sovereigns once held the realm in balance — Aldric of Velmora, Kaelen of Duskreach, and Seraphine of Aurelia — until a creeping blight corrupted the land and its creatures. Kaelen fell fighting it; Aldric founded an order of hunters to purge it; Seraphine opened her council to the common people. Years later, the blight still spreads, and few are willing to walk into its shadow.
 
You are the next to try.
 
## Features
 
- **Opening story sequence** — a multi-screen narrative intro leading into character creation
- **Three playable classes** — Warrior, Archer, and Wizard, each with a distinct max health pool and journal introduction
- **Tabbed interface** — Main, Inventory, Map, and Journal tabs unlock as you progress
- **Back/Continue navigation** — move forward and backward through the story and character selection without losing your place
- **Level-based encounter system** — health tracking with per-level thresholds for taking and recovering damage
## Requirements
 
- Python 3
- [Pillow](https://pypi.org/project/Pillow/) (`pip install Pillow`) — used for loading image assets
## Running the game
 
```bash
git clone https://github.com/<your-username>/Python_Text_RPG.git
cd Python_Text_RPG
pip install Pillow
python Main.py
```
 
Make sure `Sword.png`, `Map.png`, `Warrior.png`, `Archer.png`, and `Wizard.png` are in the same directory as `Main.py` — the game loads them on startup.
 
## Project structure
 
```
Python_Text_RPG/
├── Main.py         # Game entry point — window, screens, and navigation
├── Warrior.png
├── Archer.png
├── Wizard.png
├── Sword.png
├── Map.png
└── README.md
```
 
## How it's built
 
The game is structured around a small screen-navigation system: every screen (story panels, class selection, class confirmation, journal intros) is a named group of widgets, and a history stack tracks which screens have been visited so the Back button can retrace the player's actual path — including through branching choices like which class was picked.
 
Character stats are modeled with a `Character` class (name, max health, current health) rather than one-off variables per class, and per-level health thresholds are defined in a single rules table instead of duplicated functions.
 
## Status
 
Early development — core navigation, story intro, and class selection are in place. Combat, inventory, and map interactivity are still to come.
