# Norman or Terry?
label d1s11c:
    scene bg sheriffs_office with fade

    show norman moody at dialogright with dissolve
    show terry confused at dialogleft with dissolve

    # TODO: SFX- Low chatter. Office noises.

    "As Marley and I cross the sheriff's office to meet Terry, I can see he's not alone. Sitting at his desk is a familiar figure."

    n "For the last time, arrest her!"
    t "Not... not to be slow here, Mr. Conlee, but I'm gonna need you to run this by me again—why do you want me to arrest her? 'Cos, I do actually need a reason to lock someone up."
    n "Like I keep tellin' you: wrongful termination!"
    t "... Yeah, that ain't really my department, Norman. You'd need to, like... take her to court. An' even if you win, that's a 'give 'em a fine' kinda thing, not prison."

    show norman angry with dissolve

    n "Arg! I'm surrounded by morons!"

    show terry moody with dissolve

    t "Hey! You can't talk to me like that!"
    n "Gah! You Madduxes are all the same!"

    "Either one of them looks like they might blow. I should step in."

    show norman angry at right
    show terry moody at centerright
    with move

    show marley neutral at offscreenleft
    show ron neutral at offscreenleft

    show ron neutral at centerleft with move
    show marley neutral at left with move

    r "Evening, fellas."

    show terry neutral with dissolve

    t "Ron."

    show terry smile with dissolve

    t "An' the charming Miss Marley! Well, ain't you just a breath of fresh air!"

    show marley moody with dissolve

    m "I guess that makes you a stale fart."

    show terry laughing with dissolve
    show norman confused with dissolve

    t "Ha! Oh, you're funny, Miss Marley."
    n "Uh—I'm sorry, what's going on here?"
    r "We're here about the attacks—interviewing suspects. We'd like to speak to..."

    menu:
        "...Norman. You used to work in the mayor's office, right? That's one of the crime scenes.":
            jump d1s11c_norman

        "...Terry. Since this is one of the places that was attacked, I need to check over a few things with you.":
            jump d1s11c_terry