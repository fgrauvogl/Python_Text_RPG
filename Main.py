import random

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.uix.tabbedpanel import TabbedPanel

# ---------------------------------------------------------------------------
# Level "progress" numbers
# ---------------------------------------------------------------------------

level_nums = {
    1: random.randint(1, 8),
    2: random.randint(8, 16),
    3: random.randint(16, 24),
}

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

CLASS_INTROS = {
    "archer": ("Surviving the harsh wilds of your homeland taught you archery.\n"
               "Your eyes are keen, your wit sharp.\n"
               "You've gained a sense of distance from the world.\n"
               "Screams nearby jolt you awake, and you stretch out\n"
               "from the spot you'd been holding against a tree.\n"
               "The sound seems to be coming from the nearby town.\n"
               "What do you do?"),
    "warrior": ("You're strong -- stronger than the rest. Brawn was always\n"
                "the one feature you envied.\n"
                "Your swing is enough to take down an orc.\n"
                "Many look up to strength.\n"
                "In the distance, screams echo from the center square.\n"
                "What do you do?"),
    "wizard": "Write the wizard intro here (same length/voice as the others).",
}

STORY_PAGES = [
    "In an age when steel sang and sorcery ran deep, three sovereigns held the realm.\n\n"
    "The steadfast Aldric of Velmora.\n\n"
    "The untamed Kaelen of Duskreach.\n\n"
    "The queen Seraphine of Aurelia.",

    "For generations the lands rested in quiet harmony under their watch.\n\n"
    "Then a creeping blight seeped into the soil and the blood alike.\n\n"
    "Those it touched swelled beyond all natural measure.\n\n"
    "Garden hounds turned ravenous, citizens forgot their own names,\n\n"
    "and field mice grew large enough to drag travelers down.",

    "The three drew their blades and marched against the corrupted horde.\n\n"
    "Kaelen fell in the second week, his body consumed by the very rot he fought.\n\n"
    "Yet from the ashes of that defeat, Aldric forged an order.\n\n"
    "Sworn hunters bound to purge the blight from every corner of the land.\n\n"
    "Their expeditions uncovered old wards and forgotten cures.\n\n"
    "Seraphine, meanwhile, opened the council halls to common folk.\n\n"
    "Together their efforts gave the kingdoms something they had not felt in years:\n\n"
    "a reason to hold the line. Still the blight spreads...\n\n"
    "few remain willing to walk into its shadow.",

    "Now the tale reaches your hands.\n\n"
    "Choose who you will become and unravel the truth behind Veyra.",
]



KV = """
<StartScreen>:
    name: 'start'
    BoxLayout:
        orientation: 'vertical'
        padding: 40
        spacing: 20
        Label:
            text: 'Welcome to Turnika'
            font_size: '28sp'
            bold: True
        Widget:
        Button:
            text: 'Start'
            size_hint: (0.4, 0.15)
            pos_hint: {'center_x': 0.5}
            on_press: root.manager.current = 'story'

<StoryScreen>:
    name: 'story'
    BoxLayout:
        orientation: 'vertical'
        padding: 40
        spacing: 20
        Label:
            id: story_label
            text: root.page_text
            font_size: '18sp'
            halign: 'center'
            valign: 'middle'
            text_size: self.width, None
        BoxLayout:
            size_hint_y: 0.15
            spacing: 20
            Button:
                text: 'Back'
                disabled: root.at_first_page
                on_press: root.go_back()
            Button:
                text: 'Continue'
                on_press: root.advance()

<ClassSelectScreen>:
    name: 'class_select'
    BoxLayout:
        orientation: 'vertical'
        padding: 40
        spacing: 20
        Label:
            text: 'Choose Your Character!'
            font_size: '24sp'
            bold: True
            size_hint_y: 0.2
        Button:
            text: 'Warrior'
            font_size: '20sp'
            on_press: root.choose_class('warrior')
        Button:
            text: 'Archer'
            font_size: '20sp'
            on_press: root.choose_class('archer')
        Button:
            text: 'Wizard'
            font_size: '20sp'
            on_press: root.choose_class('wizard')

<ClassConfirmScreen>:
    name: 'class_confirm'
    BoxLayout:
        orientation: 'vertical'
        padding: 40
        spacing: 20
        Label:
            text: root.confirm_text
            font_size: '22sp'
            bold: True
            size_hint_y: 0.15
        Image:
            id: class_image
            source: root.image_source
        BoxLayout:
            size_hint_y: 0.15
            spacing: 20
            Button:
                text: 'Yes'
                on_press: root.confirm_yes()
            Button:
                text: 'No'
                on_press: root.confirm_no()

<JournalIntroScreen>:
    name: 'journal_intro'
    BoxLayout:
        orientation: 'vertical'
        padding: 40
        spacing: 20
        Label:
            text: root.intro_text
            font_size: '18sp'
            halign: 'center'
            valign: 'middle'
            text_size: self.width, None
        Button:
            text: 'Enter the world'
            size_hint_y: 0.15
            on_press: root.manager.current = 'game'

<GameScreen>:
    name: 'game'
"""

# ---------------------------------------------------------------------------
# Screen classes
# ---------------------------------------------------------------------------


class StartScreen(Screen):
    pass


class StoryScreen(Screen):
    page_text = StringProperty(STORY_PAGES[0])
    at_first_page = BooleanProperty(True)
    _index = 0

    def advance(self):
        if self._index < len(STORY_PAGES) - 1:
            self._index += 1
            self.page_text = STORY_PAGES[self._index]
            self.at_first_page = (self._index == 0)
        else:
            self.manager.current = 'class_select'
            self._index = 0
            self.page_text = STORY_PAGES[0]
            self.at_first_page = True

    def go_back(self):
        if self._index > 0:
            self._index -= 1
            self.page_text = STORY_PAGES[self._index]
            self.at_first_page = (self._index == 0)


class ClassSelectScreen(Screen):
    def choose_class(self, class_name):
        app = App.get_running_app()
        app.current_class = class_name
        app.player = Character(class_name, CLASS_MAX_HEALTH[class_name])
        confirm = self.manager.get_screen('class_confirm')
        confirm.set_class(class_name)
        self.manager.current = 'class_confirm'


class ClassConfirmScreen(Screen):
    confirm_text = StringProperty('')
    image_source = StringProperty('')

    def set_class(self, class_name):
        self.confirm_text = f'You have chosen the {class_name} class?'
        image_files = {
            'warrior': 'Warrior.png',
            'archer': 'Archer.png',
            'wizard': 'Wizard.png',
        }
        self.image_source = image_files[class_name]

    def confirm_yes(self):
        app = App.get_running_app()
        intro_screen = self.manager.get_screen('journal_intro')
        intro_screen.intro_text = CLASS_INTROS[app.current_class]
        self.manager.current = 'journal_intro'

    def confirm_no(self):
        self.manager.current = 'class_select'


class JournalIntroScreen(Screen):
    intro_text = StringProperty('')


class GameScreen(Screen):
    _built = False

    def on_pre_enter(self, *args):
        if self._built:
            return
        self._built = True

        panel = TabbedPanel(do_default_tab=False)

        main_tab = panel.tab_list and None  # placeholder, real tabs below
        from kivy.uix.tabbedpanel import TabbedPanelItem
        from kivy.uix.label import Label
        from kivy.uix.image import Image

        main_item = TabbedPanelItem(text='Main')
        main_item.add_widget(Label(text='Main game area - wire up combat/dialogue here.'))
        panel.add_widget(main_item)

        inventory_item = TabbedPanelItem(text='Inventory')
        inventory_item.add_widget(Label(text='Inventory - empty for now.'))
        panel.add_widget(inventory_item)

        map_item = TabbedPanelItem(text='Map')
        map_item.add_widget(Image(source='Map.png'))
        panel.add_widget(map_item)

        journal_item = TabbedPanelItem(text='Journal')
        journal_item.add_widget(Label(text='Journal - class intro log goes here.'))
        panel.add_widget(journal_item)

        self.add_widget(panel)


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------


class TurnikaApp(App):
    current_class = ObjectProperty(None, allownone=True)
    player = ObjectProperty(None, allownone=True)

    def build(self):
        Builder.load_string(KV)
        manager = ScreenManager(transition=SlideTransition())
        manager.add_widget(StartScreen())
        manager.add_widget(StoryScreen())
        manager.add_widget(ClassSelectScreen())
        manager.add_widget(ClassConfirmScreen())
        manager.add_widget(JournalIntroScreen())
        manager.add_widget(GameScreen())
        return manager


if __name__ == '__main__':
    TurnikaApp().run()
