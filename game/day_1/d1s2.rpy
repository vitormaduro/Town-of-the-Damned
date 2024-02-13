# Welcome to Kingston
label d1s2:
    scene bg kingston_streets with fade

    show marley smile at dialogright
    show ron anxious at dialogleft

    # TODO: SFX Town noises, crows cawing

    m "So {i}this{/i} is the place that raised you."
    r "Shut it, Mar."
    m "Jeez, you look as if someone just stole all your candy!"
    r "I don't like this town, Mar..."

    show marley smile at right
    show ron awkward at center 
    with move

    show danny smile at offscreenleft
    show danny smile at left with move

    b "Ron! Hiya buddy! It's great to see you again!"

    show ron neutral with dissolve

    r "Hey Danny. It's great to see you too. You remember my friend, Marley Shipway, don't you?"
    m "Hiya!"

    show danny neutral with dissolve

    b "Uh... sure, yeah. Hi Marry."

    show marley moody with dissolve

    m "Um, actually, it's—"

    show danny smile with dissolve

    b "I've missed you so much, Ron!"
    r "Yeah. Missed you too."
    b "Why don't I take your bags? You must be exhausted after all that travel."

    show ron smile with dissolve

    r "Oh that's kind of you!"

    "I pass him my suitcase. And he immediately presses it into Mar's hands."

    show marley angry with dissolve

    m "Hey!"

    show danny serious with dissolve

    b "Well, you {i}are{/i} his assistant, aren't you? Assist!"

    "Same old Danny."

    m "Why you little—"

    show danny smile with dissolve

    b "Why don't I give you a tour around town, Ron? Help you re-familiarize yourself."

    show ron awkward with dissolve

    r "Uh... good idea."

    "Before Marley teleports him into a river."

    b "Where shall we head to first?"

    call screen d1s2_map
    
screen d1s2_map():
    image("images/city_map/city_map.jpg")

    if not visited_library:
        imagebutton:
            idle "images/city_map/book.png"
            hover "images/city_map/book_hover.png"
            xpos 785
            ypos 90
            action [SetVariable("visited_library", True), Jump("d1s3b")]

    if not visited_museum:
        imagebutton:
            idle "images/city_map/museum.png"
            hover "images/city_map/museum_hover.png"
            xpos 1465
            ypos 385
            action [SetVariable("visited_museum", True), Jump("d1s3f")]

    if visited_library and visited_museum:
        imagebutton:
            idle "images/city_map/house.png"
            hover "images/city_map/house_hover.png"
            xpos 240
            ypos 515
            action Jump("d1s3h")