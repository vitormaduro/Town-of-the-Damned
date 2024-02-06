define remaining_items = [ "bag", "books", "computer", "crystal-ball", "photo", "post-it-notes", "prism", "skull", "tape", "tarot", "wand" ]

init:
    image bag_idle:
        "box_packing/bpm-bag_idle.png"

    image bag_hover:
        "box_packing/bpm-bag_hover.png"

    image books_idle:
        "box_packing/bpm-books_idle.png"

    image books_hover:
        "box_packing/bpm-books_hover.png"

    image computer_idle:
        "box_packing/bpm-computer_idle.png"
        zoom 0.5

    image computer_hover:
        "box_packing/bpm-computer_hover.png"
        zoom 0.5

    image crystal-ball_idle:
        "box_packing/bpm-crystal-ball_idle.png"
        zoom 0.5

    image crystal-ball_hover:
        "box_packing/bpm-crystal-ball_hover.png"
        zoom 0.5

    image photo_idle:
        "box_packing/bpm-photo_idle.png"
        zoom 0.5

    image photo_hover:
        "box_packing/bpm-photo_hover.png"
        zoom 0.5

    image post-it-notes_idle:
        "box_packing/bpm-post-it-notes_idle.png"
        zoom 0.5

    image post-it-notes_hover:
        "box_packing/bpm-post-it-notes_hover.png"
        zoom 0.5 

    image prism_idle:
        "box_packing/bpm-prism_idle.png"
        zoom 0.5

    image prism_hover:
        "box_packing/bpm-prism_hover.png"
        zoom 0.5 

    image skull_idle:
        "box_packing/bpm-skull_idle.png"
        zoom 0.5

    image skull_hover:
        "box_packing/bpm-skull_hover.png"
        zoom 0.5 

    image tape_idle:
        "box_packing/bpm-tape_idle.png"
        zoom 0.5

    image tape_hover:
        "box_packing/bpm-tape_hover.png"
        zoom 0.5 

    image tarot_idle:
        "box_packing/bpm-tarot_idle.png"
        zoom 0.5

    image tarot_hover:
        "box_packing/bpm-tarot_hover.png"
        zoom 0.5 

    image wand_idle:
        "box_packing/bpm-wand_idle.png"
        zoom 0.5

    image wand_hover:
        "box_packing/bpm-wand_hover.png"
        zoom 0.5 

screen box_game_menu:
    image Solid("#000000")

    text "Click on an object, then click on the box" size 50 align(0.5, 0.1)

    imagebutton idle "temp/play_button_idle.png" action Function(setup_box_game) align(0.5, 0.8)


init python:
    def setup_box_game():
        renpy.hide_screen("box_game_menu")
        renpy.show_screen("box_mini_game")

    def select_item(item_name):
        if item_name == "skull":
            item_description = "Just normal pens. The skull? Oh, that was from a ceremony where a bunch of idiots tried to summon Satan. Silly coots. Poor Gertrude the goat here was the ceremonial sacrifice."
        elif item_name == "bag":
            item_description = "Description of the bag, which is not present in the script yet."
        elif item_name == "books":
            item_description = "A bunch of books without description."
        elif item_name == "computer":
            item_description = "A computer. I know nothing about it."
        elif item_name == "crystal-ball":
            item_description = "I may have stolen this from a High Witch who was trying to make a love spell to seduce Chris Hemsworth. Can't say I blamed her."
        elif item_name == "photo":
            item_description = "Me, Danny, and Seb from back in our school days."
        elif item_name == "post-it-notes":
            item_description = "A block of post-it notes and some pins... That's it."
        elif item_name == "prism":
            item_description = "A cool looking prism with no apparent use for the story."
        elif item_name == "skull":
            item_description = "Just normal pens. The skull? Oh, that was from a ceremony where a bunch of idiots tried to summon Satan. Silly coots. Poor Gertrude the goat here was the ceremonial sacrifice."
        elif item_name == "tape":
            item_description = "A roll of tape. Useful for doing tape-y things."
        elif item_name == "tarot":
            item_description = "Oh God, the owner of these was one of the first people to hire me. Poor Madam Serpens. May she rest in peace. Or pieces."
        elif item_name == "wand":
            item_description = "Oh, this belonged to a Mage who was trying to assassinate the president. He was a real prick—the mage, not the president. I ain't going to comment on the president. Wand makes for a good backscratcher though."

        remaining_items.remove(item_name)
        say = SayOnScreen("item_closeup", item_description)
        say()

    class SayOnScreen(Action):
        def __init__(self, label, *args, **kwargs):
            self.old_clear_layers = config.context_clear_layers
            self.label = label
            self.args = args
            self.kwargs = kwargs

        def __call__(self):
            renpy.config.context_clear_layers = [ ]
            renpy.call_in_new_context('intermediary_sayonscreen',
                self.label, self.old_clear_layers,
                *self.args, **self.kwargs)


label intermediary_sayonscreen(lbl, original_layers, *args, **kwargs): #Borrowed code to show dialogue OVER other screens
    $ config.context_clear_layers = original_layers
    show screen absorb_input()
    $ renpy.call(lbl, *args, **kwargs)
    hide screen absorb_input
    return


screen absorb_input(): #Borrowed code to block anything below while showing dialogue OVER other screens
    zorder 1000
    key 'dismiss' action Function(renpy.ui.saybehavior, allow_dismiss = renpy.config.say_allow_dismiss)
    button:
        xysize (config.screen_width, config.screen_height)
        action Function(renpy.ui.saybehavior, allow_dismiss = renpy.config.say_allow_dismiss)


screen box_mini_game:
    image ("box_packing/bmp-wall-stuff.png") zoom 0.5

    for i in remaining_items:
        imagebutton auto i + "_%s" action Function(select_item, i) focus_mask True


label item_closeup(item_description):
    "[item_description]"

    if len(remaining_items) == 0:
        $ renpy.hide_screen("box_mini_game")
        jump after_box_minigame
        