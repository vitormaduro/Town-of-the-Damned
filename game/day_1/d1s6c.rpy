# Terry Maddux
label d1s6c:
    scene bg sheriffs_office with fade

    # SFX- soft office noises- talking, phone ringing, and occasional radio beep and crackle.

    show danny nervous at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    "As Marley, Danny, and I head into the office, I look around. I've never seen this place properly before—don't think I ever went here as a kid. It's small. Quaint."

    mystery "Hmm. It seems another player has entered the game."

    show ron confused at center with dissolve

    r "Sorry?"
    m "Huh?"
    r "Who said that?"
    m "Said what?"
    b "Hey Ron, there's something I should probably tell you, before the sheriff comes over here."
    r "Did you guys not hear—"
    b "Come on Ron, this is important! It's about the sheriff."

    show ron curious at center with dissolve

    r "Oh yeah? What about them?"
    b "You... you know him."
    r "Huh?"
    b "We went to school with him."

    show ron worried at center with dissolve

    r "Who is it?"
    b "Uh..."
    r "Danny, who is it?"

    show terry smile at left with dissolve

    t "Ron, you old dog, is that you?"

    "Oh crap oh crap oh crap oh crap oh crap."

    show ron fake_smile at center with dissolve

    r "Terry Maddux—how nice to see you again after all these years."

    "I have literally had a vampire pin me down and try to tear out my throat. Not the sexy type either. The face-melty, ugly ones that smell like rats. I've had evil priests try to rip out my heart. I've had an infernal possess me."
    "I'd rather go through {i}any{/i} of those again than be here, with {i}him{/i}."

    t "Gosh, it's been so long!"
    r "Yes, the last time we saw each other was when you broke into the principal's office and announced I was 'one of them queers' over the loudspeakers."
    t "Haha, oh yeah! Sorry about that, I always took those little pranks a smidge too far."

    show ron neutral at center with dissolve

    r "Yeah. A smidge."
    t "My bad, haha. Hey Danny, go grab me a coffee, will you? Black. Machine's over there."

    show danny neutral at right with dissolve

    b "Uh... sure. Be right back."

    show marley neutral at right with dissolve

    r "This definitely isn't where I figured you'd end up. Didn't you get a scholarship somewhere?"

    show terry awkward at left with dissolve

    t "No, no, there was a change of plans. But I love my job! All my old friends are still in town—Zack works at the timber mill; Steve helps out at my pa's farm. Oh, and my old friend Brent is a doc up at the hospital. We still meet every month and go hunting."

    show terry smile at left with dissolve

    t "Ooh, and, who's this fine lady?"

    show marley confused at right with dissolve

    r "This is Marley, my assistant."
    t "Oh, thank the Lord. I was worried you'd turned straight and this was your missus."
    r "Uh... no. No, still gay."
    t "So, uh, are you single then, ma'am?"

    show marley moody at right with dissolve

    m "Why do you ask?"
    t "'Cos you've dang near taken my breath away."
    m "I wish that was literal. Your halitosis is a serious problem."

    show terry confused at left with dissolve

    t "Well, uh... that's mighty kind of you to say, ma'am."

    show terry neutral at left with dissolve

    "From the look on Marley's face, I think I'd better step in before she gives the idiot a black eye."

    r "So, uh, this place was attacked? As was the mayor's office and the library? What happened?"
    t "Well, this was attacked on Saturday—after the attack on the library, two days after the mayor's office. In the dead of night, one of the bastards came in and attacked my poor Chief Deputy, Derek Prikus, who was working late. Wrecked his desk."
    t "He's fine. Physically. It seems to have given his nerves a bit of a crack. He's been committed to the psych ward at a nearby hospital, ranting and raving like a loon. Luckily for the guy, I was there and managed to beat the little wretch back."
    r "So you were here when the attack happened?"
    t "No, I just got back to catch the end of it. I was out with your Danny, trying to teach him how to hunt."

    show terry moody at left with dissolve

    t "Difficult to do when that weasel of a mayor has got the land 'round here designated as no hunting. Typical woman, always ruining people's fun."

    "Ugh—why would Danny want to spend time with this idiot?"

    r "Why don't you show us where the attack happened?"

    show terry neutral at left with dissolve

    t "Right there, over by the chief deputy's desk."

    call screen search_sheriff_office_minigame

screen search_sheriff_office_minigame():
    image "black"

    text "This minigame is not available yet":
        xpos 0.5
        ypos 0.3

    imagebutton idle "images/ui/next_button.png" action Jump("after_search_sheriff_office_minigame"):
        xpos 0.5
        ypos 0.9

label after_search_sheriff_office_minigame:
    t "That's a pretty accent ya got there, Miss Marley. Where ya from?"
    m "England."
    t "Oh awesome, whereabouts? Maine? You look like a Maine girl."
    m "...{i}Old{/i} England. Not {i}New{/i}."

    "I snatch up the hidden flash drive and tuck the yearbook under my coat while Terry's distracted making goo-goo eyes at a very irritated Marley."

    r "Whoever was controlling them ghouls really wanted that computer destroyed."
    m "You think the chief deputy might have been investigating the summoner and this was to cover it up?"
    r "The idea has crossed my mind."
    t "Oh, I think you big city detectives are jumping to conclusions. I reckon the perp just wants to cause a ruckus."

    "That's a mighty strange motive, to 'cause a ruckus'. A ghoul summoning spell— well, that's restricted magic. The kinda spell that ain't readily available. Too much effort for just 'causing a ruckus.'"

    "Terry's a fool, always has been, but he can't be that stupid. Maybe he's trying to brush it under the rug? This is his turf, maybe he's embarrassed that it's all going to hell under his watch."

    "Or maybe he just doesn't like his old high school nemesis doing his job? If I'm careful, I think I can get his real opinions on the case."

    "Or maybe he just doesn't like his old high school nemesis doing his job? If I'm careful, I think I can get his real opinions on the case."

    menu:
        "You're really dumb enough to think this is just some bored kid looking to cause trouble on a Friday night? 'Cos if you do, you're as stupid as you were when we were kids.":
            jump d1s6co1

        "You're probably right, Terry. After all, you've been here longer than I have. You've certainly got a better sense of the town. But it seems like an awful lot of fuss to go through just to 'cause a ruckus.' Ghoul summoning spells are forbidden magic after all— mighty hard to get a hold of. Are teens these days particularly troublesome? The type to go too far to get some fun?":
            jump d1s6co2

        "And that's your professional opinion, is it? Do you have any suspects? Any one in town with a record who you think would go this far to 'cause a ruckus'? 'Cos ghoul summoning spells, they're forbidden by all the magic councils. Mighty tricky to get a hold of one.":
            jump d1s6co3

label d1s6co1:
    show terry neutral at left with dissolve
    show marley neutral at right with dissolve
    show ron angry at center with dissolve

    r "You're really dumb enough to think this is just some bored kid looking to cause trouble on a Friday night? 'Cos if you do, you're as stupid as you were when we were kids."

    show terry angry at left with dissolve

    t "How dare you! Here I am, extending the hand of friendship after all our years of difficulties, and you spit in my face!"

    show ron laughing at center with dissolve

    r "Ha!"

    show ron moody at center with dissolve

    r "That's a damn joke. You 'extending a hand of friendship' is a load of crock, and you know it. You're just puffing up your chest like a darn rooster. Trying to prove you're some big bad alpha craphead like you did when we were kids."
    r "And you're as stupid as you always were then. So, I ask you again: do you really think someone went to all the trouble of summoning ghouls just to cause a darn 'ruckus'?"
    t "I don't think it's just dumb kids, I ain't never said that! It's clearly someone who wants to screw up the town! Someone who hates Kingston."
    t "I ain't a fool, Ron. I'm the sheriff, not a darned kid anymore. There are people who have {i}vendettas{/i} against the town."

    show ron confused at center with dissolve

    r "What? Why would someone hate the town?"

    show terry moody at left with dissolve

    t "Oh I don't know, 'cos they've got a damn chip on their shoulder about how they didn't fit in or whatever, or they're hungry for power or some bullcrap."

    "The unvoiced accusation hangs in the air. I can practically hear it."

    "'People like {i}you{/i}, Ron.'"

    show terry sad at left with dissolve

    t "{i}*Sigh*{/i} Look, Ron, I get it. Our time here when we were kids weren't... great. But we're adults now. We need to be better than we were. So... so I understand why you don't trust me. But... we gotta work together on this."

    show terry serious at left with dissolve

    t "So, for the sake of this investigation, I'll be a bigger man than I was when I was a boy. And say that I'm sorry. About the way I treated you, back then."

    "..."
    "..."
    "BULLCRAP."
    "I ain't never heard such bullcrap before."
    "Terry's full of crap."
    "But... but if I call him on it, I'll look like a petulant child."
    "So, I smile."

    show ron smile at center with dissolve

    r "Well, that's mighty good of you to say, Terry."
    r "I ain't here to get revenge or nothing. I'm here to solve the case. And we have to work together on that. I'll do what I can to make that goal come true."

    show terry smile at left with dissolve

    t "Good. I know that we can put our differences aside and crack this puzzle together."

    "Bull."
    "Crap."
    "He looks like some darn kids' TV character, talking about peace and working together."
    "I can smell the lies on his stinkin' breath."

    jump d1s6cc1

label d1s6co2:
    show terry neutral at left with dissolve
    show marley neutral at right with dissolve
    show ron smile at center with dissolve

    r "You're probably right, Terry. After all, you've been here longer than I have. You've certainly got a better sense of the town. But it seems like an awful lot of fuss to go through just to 'cause a ruckus.' Ghoul summoning spells are forbidden magic after all— mighty hard to get a hold of. Are teens these days particularly troublesome? The type to go too far to get some fun?"

    show terry thoughtful at left with dissolve

    t "Oh, I don't mean kids, more people who want to cause a ruckus {i}out of spite{/i}."

    show ron confused at center with dissolve

    r "Huh? Why?"

    show terry neutral at left with dissolve

    t "Oh, people have reasons. There are folks ‘round here that sure seem to hate Kingston."

    show terry smile at left with dissolve

    t "But I bet together, the two of us can work this out! We'll be a great team. I just know it!"

    "Slime bag."

    show ron forced_smile at center with dissolve

    r "Oh definitely. I'm sure we'll work excellently together."

    jump d1s6cc1

label d1s6co3:
    show terry neutral at left with dissolve
    show marley neutral at right with dissolve
    show ron serious at center with dissolve

    r "And that's your professional opinion, is it? Do you have any suspects? Any one in town with a record who you think would go this far, to 'cause a ruckus'? ‘Cos ghoul summoning spells, they're forbidden by all the magic councils. Mighty tricky to get a hold of one."

    show terry confused at left with dissolve

    t "Huh? 'The magic councils'? What are they?"
    m "The thirteen councils that govern all branches of magic. They monitor what magic their members have access to. And ghoul summoning isn't really openly available. It's dangerous stuff."

    show terry smile at left with dissolve

    t "Beauty {i}and{/i} brains, huh? Ain't you just the full package?"

    show marley sarcastic at right with dissolve

    m "And you're not even half an envelope."

    show terry thoughtful at left with dissolve

    t "Well, I have a few guesses in mind. But no one with a record or nothing."

    show terry neutral at left with dissolve

    t "But there are people 'round here who've got problems with the town. Who'd pull something like that just as an eff-you to Kingston."

    show ron confused at center with dissolve

    r "Huh? Why would anyone hate Kingston?"
    t "Beats me. I love this town."

    "Of course he does. This damn place worships him."

    jump d1s6cc1

label d1s6cc1:
    show terry neutral at left with dissolve
    show marley neutral at right with dissolve
    show ron neutral at center with dissolve

    t "Anywho, where's that dang Danny with my cup o' joe?"

    show terry neutral at offscreenleft with move
    show ron neutral at left with move

    r "You know something, Mar?"
    m "What, Ron?"
    r "I got a hunch there's more to this whole mess than meets the eye."
    m "You don't say. Let me just put up some protection charms, then we can go. Looks like I'll need four—those windows there, there, the front door and the back."
    r "Get Danny to help you if you don't mind. It'll give him an excuse not to deal with Terry."

    scene black with fade

    jump d1s5_map