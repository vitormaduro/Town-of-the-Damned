# Checking out Danny's job
label d1s3f:
    scene black
    scene bg museum_open with fade

    show marley neutral at right
    show ron neutral at center
    show danny smile at left

    b "This is the museum; it's where I work. I'll have to be here for shifts during some of your visits, but if you need me, Ron, I'll always be here."
    m "Thanks—"
    b "I was talking to Ron, Maisy."

    show marley moody with dissolve

    m "Marley."
    b "We're currently showing a display on how the town has changed over the years. I doubt it'll be much help, but it's kinda interesting."

    call screen maps(0) with fade

# Map screen with buttons to go back and forth between them
screen maps(index):
    image("images/bgs/kingston_map.jpg")

    text "Map " + str(index + 1):
        xalign 0.5
        yalign 0.4
        size 100
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]

    hbox:
        if index > 0:
            imagebutton idle "images/ui/previous_button.png":
                action Function(change_map, index - 1)

        imagebutton idle "images/ui/next_button.png":
            action Function(change_map, index + 1)

        xalign 0.5
        yalign 0.8
        spacing 30

# After checking the maps of the city
label after_maps:
    show marley curious

    m "What happened to that lake there?"
    r "They built a dam and turned it into a reservoir which they still call Mallory Lake. It's just further to the west."

    show danny neutral with dissolve

    b "You'll also see here there's a display on the Madduxes up at the moment. You remember them, don't you?"

    show ron moody with dissolve

    r "Unfortunately."
    m "Not a fan of the family?"
    r "Terry Maddux—the youngest in the family—he went to school with us. He was a bully, but the teachers let him get away with it because his family was such a big deal."
    b "Oh come on, Terry wasn't that bad. Anyway, since the family founded the town, they put up displays about them a bunch."
    r "My family also founded the town and we don't get displays."
    m "I'm curious what it's got to say."

    call screen display with fade

# Display with Maddux's information
screen display():
    imagemap:
        ground "bg museum_display"
        hotspot (150, 290, 1350, 575) action Show("display_text", transition = fade)

# Screen with the text of the display
screen display_text():
    image ("bg museum_display"):
        matrixcolor TintMatrix("#424242")

    text "Maddux's information will go here":
        xalign 0.5
        yalign 0.4
        size 100
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]

    imagebutton idle "images/ui/next_button.png" action Jump("after_reading_display"):
        xalign 0.5
        yalign 0.9

# After reading the display
label after_reading_display:
    hide screen display_text with fade

    r "Come on. I have no interest in staring at this shrine to my old bully's great-great-grandpa. Or staying in this godforsaken place any longer."
    b "It's gotten a lot better here recently. Mom got some interesting projects funded—"

    show ron moody with dissolve

    r "Yes, yes, we get it, your mum is amazing. Now come on, let's get out of here."
    b "Come on, we don't have all day."

    call screen d1s2_map with fade

init python:
    def change_map(index):
        if index == 1:
            renpy.jump("after_maps")
        else:
            renpy.show_screen("maps", index)