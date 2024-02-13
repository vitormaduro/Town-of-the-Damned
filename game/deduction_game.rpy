screen deduction_game_menu():
    image Solid("#000")

    text "Drag and drop the pieces to form a sentence, then click on the Arrow button" size 50 align(0.5, 0.1)

    imagebutton idle "temp/play_button_idle.png" action Function(setup_deduction_game) align(0.5, 0.8)

label puzzle:
    screen deduction_mini_game():
        image Solid("#C6B0B0")

        imagebutton idle "temp/check_solution.png":
            action Function(check_solution)
            align(0.9, 0.35)

        text "(The solution is \"Terry Lied To Danny Because They Were Scared\")":
            align(0.5, 0.05)

        draggroup:
            drag:
                drag_name "terry"
                droppable False
                dragged piece_dragged
                xpos 100 ypos 600

                add "temp/terry.png"

            drag:
                drag_name "norman"
                droppable False
                dragged piece_dragged
                xpos 350 ypos 600

                add "temp/norman.png"

            drag:
                drag_name "danny"
                droppable False
                dragged piece_dragged
                xpos 600 ypos 600

                add "temp/danny.png"

            drag:
                drag_name "lied_to"
                droppable False
                dragged piece_dragged
                xpos 850 ypos 600

                add "temp/lied_to.png"

            drag:
                drag_name "because_power"
                droppable False
                dragged piece_dragged
                xpos 1100 ypos 600

                add "temp/because_power.png"

            drag:
                drag_name "because_scared"
                droppable False
                dragged piece_dragged
                xpos 1350 ypos 600

                add "temp/because_scared.png"

            drag:
                drag_name "because_connected"
                droppable False
                dragged piece_dragged
                xpos 1600 ypos 600

                add "temp/because_connected.png"

            drag:
                drag_name "zone 1"
                draggable False
                pos (300, 300)

                add "temp/deduction_drop_zone.png":
                    zoom 2.0

            drag:
                drag_name "zone 2"
                draggable False
                pos (600, 300)

                add "temp/deduction_drop_zone.png":
                    zoom 2.0

            drag:
                drag_name "zone 3"
                draggable False
                pos (900, 300)

                add "temp/deduction_drop_zone.png":
                    zoom 2.0

            drag:
                drag_name "zone 4"
                draggable False
                pos (1200, 300)

                add "temp/deduction_drop_zone.png":
                    zoom 2.0

init python:
    def setup_deduction_game():
        renpy.hide_screen("deduction_game_menu")
        renpy.show_screen("deduction_mini_game")
        store.sentence = { 
            "zone 1": "",
            "zone 2": "",
            "zone 3": "",
            "zone 4": ""
        }

    def piece_dragged(drags, drop):
        if not drop:
            return
        
        drags[0].snap(drop.x, drop.y)
        store.sentence[drop.drag_name] = drags[0].drag_name

    def check_solution():
        solution = {
            "zone 1": "terry",
            "zone 2": "lied_to",
            "zone 3": "danny",
            "zone 4": "because_scared"
        }

        return sentence == solution
