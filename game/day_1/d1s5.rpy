# The Charms
label d1s5:
    scene bg rons_office with fade

    show marley neutral at right with dissolve
    show ron neutral at center with dissolve
    show danny neutral at left with dissolve

    m "I'm back!"

    show danny moody at left with dissolve

    b "Great. Can we go now?"
    m "Nope! Not yet."
    b "Ugh, what now?"
    r "We need to make charms!"

    show danny confused at left with dissolve

    b "Charms?"

    "I watch as Marley grabs her box of beads."

    r "Like I said, Marley's a Witch. Me and her are gonna make these special charms."

    show marley thoughtful at right with dissolve

    m "We'll put one in each crime scene's possible entry points. You can't remove them unless you know this specific spell. Nothing under another's command will be able to pass through. It'll keep any ghouls out or trapped inside. How many should we make, Ron?"

    show ron thoughtful at center with dissolve

    r "Police station, library, mayor's office—let's say fifteen to be sure."
    m "Alright, can you thread the charms while I do the special hand movements?"

    show ron smile at center with dissolve

    r "Sure thing."

    call screen charm_making_minigame

screen charm_making_minigame():
    image "black"
    text "This minigame is not available yet":
        xpos 0.5
        ypos 0.3

    imagebutton idle "images/ui/next_button.png" action Jump("after_charm_making"):
        xpos 0.5
        ypos 0.9

label after_charm_making:
    show marley smile at right with dissolve

    m "Great! Any ghouls that try and pass under these bad boys will get barbecued!"

    show danny curious at left with dissolve

    b "Can't the summoner just pull them down?"
    m "Nope. The magic will keep them up—the only way to take this down is to spin the wooden bead counter-clockwise three times. Then it can be taken down."
    m "Besides that, like I said, if the charm is covered, the eyes on that bead can't see. So, the charm will be useless until it's uncovered."

    show danny thoughtful at left with dissolve

    b "I see."

    show marley smile at right with dissolve

    m "So, Ron—first day of the investigation! What will be the first question?"

    show danny curious at left with dissolve

    b "Huh? What do you mean?"
    m "As part of our method for solving investigations like this, we divide the whole mystery into smaller, simple questions. If we try to answer at least one question each day, hopefully we can get a full picture of what's going on."
    b "I see."

    show ron thoughtful at center with dissolve

    r "Well Danny said that he can't remember the order of the attacks—let's figure those out first. Nice and easy. And let's get some alibis."
    m "Good idea."
    r "Okay, now that that's decided, we should get going."

    show danny smile at left with dissolve

    b "Sure thing. Where shall we head first?"

    jump d1s5_map

label d1s5_map:
    if visited_d1s6a and visited_d1s6c and visited_d1s6e:
        jump d1s7

    menu:
        "Mayor's Office":
            if not visited_d1s6a:
                $ visited_d1s6a = True
                jump d1s6a
            else:
                jump d1s6b

        "Sheriff's Office":
            if not visited_d1s6c:
                $ visited_d1s6c = True
                jump d1s6c
            else:
                jump d1s6d

        "Library":
            if not visited_d1s6e:
                $ visited_d1s6e = True
                jump d1s6e
            else:
                jump d1s6f

        "Ron's Office":
            jump d1s6g