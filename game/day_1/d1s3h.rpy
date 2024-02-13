default hair_checked = False
default card_checked = False
default necklace_checked = False

# The First Clues
label d1s3h:
    scene black
    scene bg rons_office with fade

    show marley confused at right
    show ron confused at center
    show danny smile at left

    b "Home sweet home!"
    r "Wh- what the hell?"
    b "Surprise!"
    r "Wh- why does your spare room look like my office?"
    b "I redecorated it to look like your place back in the city, to make you feel more at home!"
    r "I- I don't remember you ever having been to our office."
    b "No, haha. You never invited me. I had to do a bit of snooping on your social media!"
    m "That's not creepy at all. Is that a papier-mâché bust of Ron?"
    r "Well, uh... it's nice of you to go to all this trouble, Danny."
    b "Any time! I just really want you to be comfortable here."
    r "But didn't you get in trouble with your landlord? This must have required some serious renovations!"
    b "I had to have the back wall completely redone. But mom smoothed it over with the landlord for me."
    m "Uh-huh... um, anyway, why don't you tell us what's going on?"
    b "If you need anything, you just let me know! I'm always happy to help in any way I can!"
    m "Well, we 'need' you to tell us what's going on so we can solve the case, so—"
    b "Anything at all, Ron. Anything you want. Don't hesitate to ask. No holds barred."

    show marley frustrated with dissolve

    m "So what's happening—"
    b "I can get you a TV in here, a coffee machine—you can even use my computer for any research! Try it! Click on the search box and type in a question. What about 'The History of Kingston'?"
    r "If I do, will you just tell us what's going on, Danny?"
    b "Of course, Ron."

    call screen wikipedia() with fade

screen wikipedia():
    imagemap:
        ground "bg wikipedia"
        hotspot (1125, 560, 50, 40) action Show("history_of_kingston", transition = dissolve)

    text "History of Kingston":
        xpos 735
        ypos 560
        slow_cps 10

screen history_of_kingston():
    image ("bg museum_display"):
        matrixcolor TintMatrix("#424242")

    side "c r":
        area (100, 100, 1360, 700)
        xalign 0.5

        viewport id "vp":
            draggable True

            text "{b}{u}Kingston, TX{/b}{/u}\n\n          A small town in eastern Texas, USA, Kingston is one of the oldest in the area. Kingston was founded in 1673 by Terence Maddux. He and his fellow settlers came over from England on a ship called 'The Conquest.' Maddux had been tasked, by England's Grand Wizard Nathan Pulsifer, to settle in that territory specifically. Pulsifer foresaw that an English settlement in the area would have great importance in any battle over the land.\n           To protect the settlers from hostile Indigenous Peoples and Spaniards, Pulsifer gave Maddux five special pillars, named 'The Protective Pillars of Kingston', which Pulsifer carved from sacred stones and inscribed with protective runes. Once Maddux and his people made their way to the specified area, they planted the five posts around the perimeter of the settlement. Maddux anointed the tops with his own blood. The pillars remained in place for 321 years. They prevented any who wished harm on the people that resided within those pillars from passing through the town's perimeter. Thus, Kingston soon began a healthy trade with the Indigenous Peoples in the area while the Spanish settlers remained entirely unaware of the town's existence. When they finally noticed the town in 1820, their hold over the area was slipping too much for them to strike.\n\n         Kingston has a colorful set of local legends, including stories of a chaotic Witch who wanted to bring the people of Kingston to their knees. This legend has been added to by the fact that Kingston has been the site of many interesting crimes, and...":
                xalign 0.5
                yalign 0.3
                maximum (1350, 760)
                color "#ffffff"
                outlines [(2, "#000000", 0, 0)]

        vbar value YScrollValue("vp")

    imagebutton idle "images/ui/next_button.png" action Jump("after_reading_article"):
        xalign 0.5
        yalign 0.9

label after_reading_article:
    hide screen history_of_kingston with fade

    show ron neutral at center with dissolve

    r "So what's been going on, Danny?"

    show marley neutral with dissolve
    show danny neutral with dissolve

    b "Well, long story short, three places in town have been attacked over the last week: the mayor-my mom's-office, the library, and the sheriff's office."
    b "I can't remember in what order. Anyway, luckily no one's been killed yet; the bastards only appear at night when there's not many people around."
    r "Yeah, ghouls de-animate when the sun comes up."
    b "Ahh. Well, they've caused quite a lot of damage."
    r "Right. I'll need to have a look at the scenes."
    b "Maybe you should also talk to Seb. You know, interrogate the prime suspect?"

    show ron nervous with dissolve

    r "Uh, no. Not just yet. It's too soon."
    b "If you're sure."

    show ron neutral with dissolve

    m "Why do you think this Seb guy is behind it?"

    show danny moody with dissolve

    b "Your secretary sure asks a lot of questions, don't she?"

    show marley angry with dissolve

    m "Hey, what the hell?"

    show ron angry with dissolve

    r "Knock it off, Danny. She's my assistant, a Witch, and a doggone good friend. So answer her question."
    b "Fine. Well, Marie—"
    m "Marley!"
    b "I've checked out all the scenes-they've been left as they were after the attack for you to examine. And I've found things belonging to Seb at each place. Look—"

    show marley neutral with dissolve
    show ron neutral with dissolve
    show danny neutral with dissolve

    "He pulls out a plastic zipper bag from one of the desk's drawers and holds it out to me."
    "There are three objects in it."

    call screen dannys_evidence with fade

screen dannys_evidence():
    image ("bg ziplock")

    # if hair_checked:
    #     return True

    imagebutton idle "hair_lock" action [Show("evidence_description", description = "A lock of purple hair tied up with a red bow. Seb's hair changed that color a few years back thanks to his elf's blood according to his Instachat... that I absolutely didn't stalk."), SetVariable("hair_checked", True)]:
        xpos 490
        ypos 45

    imagebutton idle "card" action [Show("evidence_description", description = "An old Pikiman card-a fancy Balaturtle. Seb got one back when he was collecting them in school."), SetVariable("card_checked", True)]:
        xpos 910
        ypos 65

    imagebutton idle "necklace" action [Show("evidence_description", description = "A heart-shaped locket... My breath catches in my throat-this was his mother's locket. Or it had been hers, many, many years ago. I've never seen Seb take it off, not since the day she pressed it into his hand as he cried over her hospital bed."), SetVariable("necklace_checked", True)]:
        xpos 630
        ypos 765

screen evidence_description(description):
    image ("bg ziplock"):
        matrixcolor TintMatrix("#424242")

    text [description]:
        xalign 0.5
        yalign 0.3
        maximum (700, 500)
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]

    imagebutton idle "images/ui/previous_button.png" action Function(check_evidences):
        xalign 0.5
        yalign 0.9

label after_evidence:
    show marley neutral at right
    show ron thoughtful at center
    show danny neutral at left
    with dissolve

    r "Um. You found these all at the locations that were attacked?"
    b "Uh-huh."
    m "How did you get these?"
    b "Stopped by after the police were through checking the scenes."
    r "It's strange that they were all left at the scenes."

    show danny confused with dissolve

    b "How so?"
    r "Seb's a smart guy. You'd think he wouldn't leave such easily identifiable things at a crime scene. Part of the process to summon a ghoul is to give it an item that's important to you... an anchor—but surely he would have found a way to grab them back afterwards."

    show danny neutral with dissolve

    b "I don't know. Anyway, we should start checking out the scenes before it gets too late—"

    show marley serious with dissolve

    m "Not yet."

    show danny moody with dissolve

    b "What? Why not, what's wrong?"
    m "I need to meditate."
    b "WHAT? There is a criminal on the loose and you want to practise deep breathing?"
    m "Again... I. Am. A. Witch. All my power relies on nature. And I don't know the nature here. I'm not in tune with it. To use my magic, I have to get in touch with nature each and every day."
    m "I need access to my magic at all times during an investigation. So, before we do anything, I need to find somewhere to meditate."
    b "Jesus. Not that amazing of a power set you got there if you have to meditate every day."

    "Marley looks Danny up and down, judgment in her eyes."

    m "Maybe you should try it, Danny. Think it would really... {i}benefit{/i} you. Fix your whole vibe."

    "I fight off a laugh as Marley turns and leaves before Danny can muster a comeback."

    show marley serious at offscreenright with move
    
    show ron thoughtful at dialogright
    show danny angry at dialogleft 
    with move

    b "SON OF A-!"
    r "You deserved that."

    show danny smile with dissolve

    b "Listen, Ron—you know, we could just go without her. We've got lots to do that we don't need her weird magic for, like interrogating suspects—"

    show danny curious with dissolve

    b "You got a strategy in mind for the questioning?"

    show ron neutral with dissolve

    r "Same one I always do."
    b "Yeah?"
    r "Well, there are a few possible ways you may want a suspect to feel about you."
    r "First, you can try and get them to trust and respect you as a professional. Be a peacemaker, seem smart and 'adult.' Be bold. Be honest. Straightforward."
    r "Make them trust in your competence; if they're innocent, they'll help you and feel safe around you. But, if they're guilty, seeming smart and competent will usually make them up their game... They might try and get rid of you."
    r "Next, you can try to be their friend. You get on their good side, get them to want to help you. If they're innocent, they might go out of their way to lend a hand in the investigation-but, of course, the flip side is that this puts them in danger."
    r "If they're guilty, sometimes it makes them drop their defenses, makes 'em slip up. But it can be dangerous-you think you're getting under their defenses, but really, they're getting under {i}yours{/i}."
    r "Then, finally, you can try and make 'em angry. That's the {i}most{/i} dangerous one; even if they're innocent, the suspect might try and screw you up out of spite. They stonewall you. Although, I have known people who responded well when I tried to make them mad—liked the brutal honesty of it, I guess."
    r "But in a case like this, ego is always involved, so if you make the guilty suspect angry, they'll take it to heart. They'll probably try to screw you over, but they'll also probably make mistakes—ones big enough to show themselves."

    show danny thoughtful with dissolve

    b "I see. So ya' assess each suspect and pick the best technique?"

    show ron smile with dissolve

    r "Exactly. None of the methods are wrong, but some are better than others depending on the situation. They'll each get different results. Every decision I make when talking to a suspect aims to make them feel a certain way about me. Everything I do is trying to get them to feel one of those ways."
    b "That's very clever, Ron."
    r "Thank you."

    show danny neutral with dissolve

    b "Should we go?"

    show ron serious with dissolve

    r "Nope. No, we wait for Marley."

    "I wonder how her meditation is going."

    scene black with fade

    jump d1s4

init python:
    def check_evidences():
        global hair_checked
        global card_checked
        global necklace_checked

        if hair_checked and card_checked and necklace_checked:
            renpy.hide_screen("dannys_evidence")
            renpy.hide_screen("evidence_description")
            renpy.jump("after_evidence")
        else:
            renpy.hide_screen("evidence_description")