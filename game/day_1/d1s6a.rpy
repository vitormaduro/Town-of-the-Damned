label d1s6a:
    scene bg mayors_office with fade

    # sfx muffled arguing

    "As I head up to the Mayor's Office, I can hear angry voices coming from inside. One sounds like Emily—Danny's mom. Then someone I don't know, a man."
    "I reach for the door handle and start to pull it open."

    # sfx door opening

    show emily angry at right with dissolve
    show ron confused at center with dissolve
    show norman angry at left with dissolve

    e "Well well well. Hello there. And who might you be?"

    "The voice is quiet, almost drowned out by the yelling. Barley more than a whisper. It sounds like it's simultaneously miles away and right in my ear. And my gut is telling me that whoever said that isn't part of the pair in the room."

    r "Huh?"
    n "You're {i}firing{/i} me, you soul-sucking DEMON?"
    e "Oh, this has been a long time coming, Norman, and you know it!"

    "As I gape at the mayor screaming at the strange man, all other thoughts fly out of my mind."

    n "You're reveling in this, aren't you?"

    "He waves a fistful of crumpled paper at her then throws it dramatically on the floor. It's like a scene from a soap opera come to life—one where I don't know the plot."

    e "Stop whining, you sniveling, little rat. You've lost. End of story."
    r "Eh-hem. Uh, hello?"

    show emily shocked at right with dissolve

    e "Oh!"

    show emily smile at right with dissolve
    show ron neutral at center with dissolve

    e "Oh my, is that Ronald Kitzinger I see?"
    r "Hi Mayor Sawyer."
    e "Please, call me Emily! You're not a little boy anymore! Gosh, you've grown so much! Aww, aren't you handsome!"
    r "It's great to see you again after so long."
    e "Danny has been so excited about you coming!"
    n "Oh yes, as long as the little prince is happy."
    r "Uh..."

    "I stare at the man, confused and watch him pack things from around the wrecked secretary's desk into cardboard boxes."
    "He doesn't look like a secretary, though. I recognize his jacket as an expensive, designer brand, and his watch is a fancy Swiss make."
    "He glowers at Emily as he packs."
    "The computer on the desk, I notice, is broken and destroyed. A casualty of the ghoul attack, I'd guess."

    show emily fake smile at right with dissolve

    e "So, Ron, you're here to investigate the vandal attacks. Is that right?"

    "Oh right, Danny said that they were telling the townsfolk that it was vandals. That must include the secretary."

    show ron awkward at center with dissolve

    r "Uh... yes."

    show ron serious at center with dissolve

    r "Yes, that's right, ma'am."
    n "If you wanna find who smashed up this desk, Emily, might I suggest you look in a darn mirror? That is, if you ain't shattered 'em all already."

    show emily moody at right with dissolve

    e "Why don't you do the whole world a favor, Norman; go take a li'l dip in Sandero Lake, swim down to the very bottom, and stay there until you drown."

    "Jesus Christ! As a kid, I went around to Mayor Emily's house hundreds of times—she never even raised her voice once."
    "But I think she might actually try and kill this Norman guy—I should say something before they actually start fighting."
    "But should I help her or him? He started it, and she's the one who got me this job, but she's being so... vicious. Maybe I should try and stay neutral instead?"

    menu:
        "Hey cowboy, that ain't no way to talk to the mayor!":
            jump d1s6ao1

        "Maybe go easier on him, Mayor Sawyer—that's kinda intense.":
            jump d1s6ao2

        "Okay, okay, why don't you both take a breath and calm down.":
            jump d1s6ao3

label d1s6ao1:
    show emily angry at right with dissolve
    show ron angry at center with dissolve
    show norman angry at left with dissolve

    r "Hey cowboy, that ain't no way to talk to the mayor!"
    n "Oh yeah? What are ya' gonna do about it, ya' li'l punk?"
    r "You need to apologize to her, then you need to get the hell out, 'cos I ain't gonna stand here and listen to you disrespect her."

    show emily smile at right with dissolve

    e "Oh, pay that idiot no mind, Ron. The little rat's just been fired after clinging to this office like feces on a shoe for {i}far{/i} too long."

    jump d1s6ac1

label d1s6ao2:
    show emily angry at right with dissolve
    show ron sympathetic at center with dissolve
    show norman angry at left with dissolve

    r "Maybe go easy on him, Mayor Sawyer—that's kinda intense."

    show emily serious at right with dissolve
    show norman smug at left with dissolve

    e "Ron, I don't—"
    n "Don't worry about it, buddy. She's probably just on the rag or something."

    show emily angry at right with dissolve

    e "Oh shut up, you little turd."

    jump d1s6ac1

label d1s6ao3:
    show emily angry at right with dissolve
    show ron serious at center with dissolve
    show norman angry at left with dissolve

    r "Okay, okay, why don't you both take a breath and calm down."
    n "Stay out of this!"

    show emily neutral at right with dissolve

    e "Thank you for trying to help, Ron, but really, it's not necessary. You won't get through to him. He doesn't speak 'common sense'."

    jump d1s6ac1

label d1s6ac1:
    show emily moody at right with dissolve
    show ron neutral at center with dissolve
    show norman angry at left with dissolve

    e "Norman?"
    n "What?"
    e "Take your stuff and get the hell out of here."
    n "I hope you drive off a cliff."

    show norman angry at offscreenleft with move
    show ron neutral at left with move
    show emily smile at right with dissolve

    e "Ahh. Air feels cleaner already, don't it? Anyway, I've got some questions for you if that's alright?"

    show ron awkward at left with dissolve

    r "Uh... sure, I guess. Shoot"

    show emily neutral at right with dissolve

    e "Let's start with the ghouls. What can you tell me about them?"

    show ron thoughtful at left with dissolve

    r "Well, um, the corpses will be from a local graveyard."
    e "Yes, we found some disturbed graves. I had the sheriff tape up the place and lock it down. Should prevent tampering and such."
    r "That's probably for the best, although it won't much impact the summoner now. They will have already taken earth from the graves for their ritual."
    r "Any ghouls we encounter will obey the summoner's commands until dawn, at which point they'll de-animate."
    e "Ooh, that's so interesting! I don't really know anything about the topic. I'm very interested in magic, but I never investigated the whole 'undead' type of magic."
    e "Could you tell me—what is the difference between ghouls and zombies? ‘Cos that's what we thought the moldy monsters were before my Danny set us straight."
    e "We were ready to call in the Z-squad to lock this place down and declare Kingston an infection site! Good thing we didn't jump the gun."

    show ron awkward at left with dissolve

    r "Uh..."

    "Her sudden tone change catches me off guard."

    r "Eh-hem."

    show ron neutral at left with dissolve

    r "Well, ghouls are corpses that are given life on an individual level by the summoner. Zombies are infected by a disease someone has created that's laced with magic."

    show emily confused at right with dissolve

    e "Huh?"

    show ron thoughtful at left with dissolve

    r "In simple terms, ghouls are given life by someone and will obey that person's orders. They last until sunrise. Zombies are animated by a disease that can be spread. They last until they rot away or are killed."

    show emily curious at right with dissolve

    r "But outside of that, they're pretty similar. They both tear their victims apart. They're both very strong."
    r "But ghouls are faster, and as a part of the spell to revive them, the summoner has to ensure that at least one of the ghouls has either something important to the caster or the caster's DNA on them. It keeps the ghoul tied to them, anchors them."
    r "If the ghouls lose it, they'll just wander around aimlessly until dawn."

    show emily smile at right with dissolve

    e "Ooh, I see! This is all very fascinating!"

    show ron serious at left with dissolve

    r "Would you mind if I asked you some questions?"
    e "Of course not."

    show ron neutral at left with dissolve

    r "Well, was anyone here the night of the attack?"

    show emily neutral at right with dissolve

    e "No, thank God. We had no idea until we came in the next day and found the back door smashed in."
    r "Where were you at the time?"
    e "At a dinner meeting with the head of the town council to discuss some things."
    r "Danny told me that three places were attacked: here, the library, and the sheriff's office. But he couldn't remember what order that was in. Do you know?"
    e "Let me think—so today is Sunday. Yesterday must have been Saturday, so... the attack on the... I think it must have been the library. Then Friday was here. And that means Thursday must have been the sheriff's office."
    r "Great, thank you. Do you have any idea what they were doing in here?"
    e "No, we don't have cameras inside the building—don't have the funding. The police found the bodies in here, by the smashed computer."
    r "Where are the bodies now?"
    e "There's an emergency bunker beneath this building. We've locked them all down there, including the ones from the other scenes."
    r "Good call. They shouldn't be able to re-animate anymore, but I've seen summoners put evil little booby traps in the corpses."
    e "Oh."

    show emily worried at right with dissolve

    e "They're- they're not going to come back, are they? The ghouls?"
    r "Not once Marley's done."

    show emily curious at right with dissolve

    e "Who?"
    r "My assistant, Marley. She's a Witch. She's outside. Putting protections around your office."
    e "Ooh! That sounds very exciting! I wonder how it's going?"
    r "And I wonder if she's met that assistant of yours yet."

    show emily worried at right with dissolve

    e "Oh no! Your poor assistant! Norman isn't the kind of man you want to talk to when he's in a bad mood."
    r "Oh believe me, no matter how bad his mood is, he ain't a threat to Marley. I once saw her get groped on the subway—she turned that swine into a darned frog, right before my eyes!"
    r "But there's no need to fear her, not really. Sure, she's got one hell of a bite, but deep down, she's a sweetheart—but don't go telling her I said that. If Norman wants to start something, then I pity him."

    scene black with fade
    jump d1s6ac2

label d1s6ac2:
    scene bg kingston_streets with fade

    show danny neutral at left with dissolve
    show marley thoughtful at right with dissolve

    # sfx crow caws, small town noises

    "Danny is standing uncomfortably close, watching me like a hawk as I examine the doorway of the mayor's office building. As I take it in, I shake my water bottle, mixing the goat's blood and angelica root together."

    m "So this is where they got in?"
    b "Yes, we think so. We found... bits of the corpses. Caught on the door handle."
    m "But the door... it looks fine. Doesn't look like they broke in. Was the door unlocked?"
    b "I dunno. So, what exactly are you doing?"
    m "Runes."
    b "Runes?"
    m "How many doors does this place have? Including this one."
    b "What? Why do you need to know?"
    m "It's important. How many?"
    b "Two. Front and this one at the back. Why?"
    m "Any big windows? Big enough to climb through?"
    b "I- I don't think so."
    m "Great. Well, this water bottle is full of blood. I'm going to paint runes next to both doors. They'll stop anything dead from entering the building."
    b "Wait, for real? You can do that? You understand runes?"

    show marley neutral at right with dissolve

    m "Not exactly. But it's not about that."

    show danny confused at left with dissolve

    b "Huh?"
    m "Magic is all about intent. To be honest, I could easily write 'protect this place from ghouls plz' on the door and, as long as I have enough intent behind it, it would work. I could even just draw a pretty picture of a ghoul's head exploding."
    m "But in all things magical, the... 'vibe' is incredibly important. Like... think of it as an actor. You give an actor a terrible script, then no matter how good they are, the feeling they put into it isn't going to be the same as if it's a great script."
    m "Runes can channel magic better than normal words because of their perceived mysticism. Also, your average person going by won't have any idea what it's saying. That can be very useful."
    b "But wait, if you're using runes, what was all that time making charms for?"
    m "The magic works better if there's multiple elements working in harmony to achieve the same goal. Also, this way, if one is bypassed for some reason, the other can act as a failsafe."

    show danny thoughtful at left with dissolve

    b "I see."
    m "I'll be honest, studying runes is more a Level Two Witch thing, and I'm just at Level One. I only know a handful of runes. But there are two—technically three—that I need here."

    call screen rune_making_minigame with fade

screen rune_making_minigame():
    image "black"

    text "This minigame is not available yet":
        xpos 0.5
        ypos 0.3

    imagebutton idle "images/ui/next_button.png" action Jump("after_rune_making_minigame"):
        xpos 0.5
        ypos 0.9

label after_rune_making_minigame:
    b "What do they mean?"
    m "The first one—the one that looks like a capital Y with a stick in the middle—that's Algiz. It's a protection rune."
    b "Right."
    m "The other two, they're a bound rune—two runes put together. Originally, there's one that looks like a stickman shrugging. That's Ear. The interpretation on that's a bit vague, but I'm using it to mean 'death.'"
    m "The final rune is Kaunan. Looks like the less-than math symbol. Or crocodile jaws. I'm using it to mean ‘fire.' So, putting them together: burn the dead. The three of them will protect the building and burn anything dead that tries to enter it."
    r "But, uh, won't the rain wash the runes away once you've done them?"

    show marley smile at right with dissolve

    m "Nope! Once the spell is complete, nothing can wash it off. The spell will keep going until either ninety days pass or each rune is struck through—also with blood."
    b "I see."

    "As I pause to examine my handywork, my attention wanders to the crows scattered around the nearby buildings. They're watching me. Carefully. Danny follows my gaze."

    show danny worried at left with dissolve

    b "Those things creep me the hell out."

    show marley thoughtful at right with dissolve

    m "They're just birds. Everwatching."
    b "There never used to be this amount of them before. They've all come over the past week or so."

    show marley curious at right with dissolve

    m "Is that so?"

    "Suddenly the door to the council office flies open, nearly hitting me in my face."

    show marley curious at center with move
    show norman moody at right with move
    show marley moody at center with dissolve
    show danny neutral at left with dissolve

    m "Oi!"
    n "Get lost!"

    "The strange man glances at me out of the corner of his eye, then pauses."

    n "Hey—I don't know you. You're not from here."

    show marley curious at center with dissolve

    m "Uh—no. No, I'm not."
    n "What, are you from the council? Or do you work for that twit, Mayor Sawyer? 'Cos if you is, you can go screw yourself!"

    show marley confused at center with dissolve

    m "What?? No, I'm not! I'm just—"

    "My gut is telling me to lie here. Not to let this angry weirdo know anything about me."

    m "I'm just a friend of—well, a friend of a friend of Danny's. That's all. My friend Ron and I are staying with him."

    show norman angry at right with dissolve

    "The stranger glowers at Danny."

    n "Get lost, Sawyer."

    show danny worried at left with dissolve

    b "I- I'm not scared of you, Norman!"

    "Norman takes a menacing step forward."

    show danny scared at left with dissolve

    b "Uh- but I think I can hear Ron calling... Got to go!"

    show danny scared at offscreenleft with move
    show marley confused at left with move

    "Coward. Norman's eyes turn back to me."

    show norman suspicious at right with dissolve

    n "... You... you don't work for Sawyer?"
    m "You mean Danny's mom, the mayor? No, I haven't met her."
    n "Or the council?"
    m "No!"

    show norman thoughtful at right with dissolve

    n "Oh. I see."
    n "Well, if you're smart, you'll stay the hell away from all of 'em."

    "Ooh, this feels like a clue. I don't exactly want to keep talking to this angry dude, but I guess this is my job."

    show marley curious at right with dissolve

    m "Oh? And why's that?"

    show norman serious at right with dissolve

    n "The council is full of a bunch of old, power-hungry farts, led by that spoiled bastard, Chris Maddux. And the mayor—well, she's a conniving witch."
    m "Really?"
    n "Don't trust her. No matter how much she prattles on about 'helping Kingston,' and 'bringing it into the modern age,' she's just here for the power."
    n "It's all she cares about—she has this whole town wrapped around her damn finger. And has done for... well, for too long."

    "The hell is he talking about?"

    m "Why? What's she done?"
    n "That ain't none of your business. But listen, the long an' the short of it is this: don't trust no one in Kingston. They all got secrets and agendas."
    n "An' we got some real freaks, too, like the half-elf up at the school. Why these fools would ever let someone like that around kids is beyond me."

    "Wow, what a charmer."
    "If we're looking for someone who hates the town and would want to destroy it, I think there's a good candidate here."

    m "Has she done something to you?"

    show norman moody at right with dissolve

    n "That ain't none of your business."
    n "If you're smart, you'll get the hell out of Kingston. As soon as possible."

    "With that, Norman turns and marches off down the street."
    "He doesn't seem like the most stable of men. But in all honesty, I don't disagree with him about leaving this darn place."

    scene black with fade

    jump d1s6ac3

label d1s6ac3:
    scene bg mayors_office with fade

    show emily neutral at right with dissolve
    show ron neutral at left with dissolve

    r "Do you mind if I have a quick look over the desk that was destroyed? In fact, I should have a look ‘round the whole office if this was the ghouls' target."
    e "Go ahead. I need to visit the li'l girls' room anyway, so I'll give you some privacy."
    r "Thank you ma'am."

    show emily neutral at offscreenright with move
    show ron neutral at center with move

    "As the Mayor walks out of her office, I look around her room. The assistant's desk is completely destroyed. A total wreckage. I don't think I'll be able to find much there. But there's a lot of interesting things around the office that catch my eye."

    call screen search_office_minigame with fade

screen search_office_minigame():
    image "black"

    text "This minigame is not available yet":
        xpos 0.5
        ypos 0.3

    imagebutton idle "images/ui/next_button.png" action Jump("after_search_office_minigame"):
        xpos 0.5
        ypos 0.9

label after_search_office_minigame:
    "As I give the room a final once-over, I hear footsteps coming down the hall."

    # sfx - footsteps

    show ron neutral at right with move
    show marley neutral at left with move

    m "Hiya. I'm all done, Ron. Put up the runes and used two charms—front door and back. None of the windows are big enough to need it."
    r "Where's Danny?"
    m "Hiding from some angry weirdo screaming in the car park. Not sure who he is, but he really hates the mayor and town council."
    r "Ah. I think I met the angry, screaming weirdo. He's the mayor's ex-secretary, Norman."

    show ron neutral at right with dissolve

    r "Oh by the way, do you know what that plant is? The one by the door?"

    "She bends down to examine the small stem and yellow flowers."

    show marley curious at left with dissolve

    m "Hypericum perforatum, also known as St John's Wort. It originates from Europe and West Asia. Some came over to America, but I think it's too hot to find many around here."

    show ron thoughtful at right with dissolve

    r "Hm. Maybe someone who gardens accidently got it caught up in their clothes and tracked it in."

    show marley neutral at left with dissolve

    m "It's possible."

    # sfx - footsteps. Door opening

    "The door opens and Emily walks in."

    show ron thoughtful at center with move
    show emily neutral at right with move

    e "I hope that's all the time you need. If not, I can go away and come back in—"

    show emily surprised at right with dissolve

    e "Oh!"

    "She stops in surprise when she sees Marley."

    show emily curious at right with dissolve

    e "Uh... hello."

    show ron neutral at center with dissolve

    r "Mayor Sawyer, I'd like you to meet my assistant, Marley Shipway. Marley, Mayor Sawyer."

    show emily smile at right with dissolve

    e "Please, call me Emily. It's a pleasure to meet you!"

    show marley smile at left with dissolve

    m "The pleasure's mine."
    e "Ooh, I love your accent! You're from England?"
    m "I certainly am, ma'am."
    e "My my, you are a long way from home! Danny didn't tell me Ron had an assistant. Are you new, Marley?"

    show marley neutral at left with dissolve

    m "Oh no, we've worked together for a few years now."

    show emily curious at right with dissolve

    e "Now, I don't mean to pry, but are you the Witch that Ron mentioned?"
    m "Yes, that would be me."
    e "Oh, how fascinating! I haven't met a Witch before!"
    r "She's been putting up special charms at each of the building's entrances. Should give some protection if anything were to happen again."

    show emily smile at right with dissolve

    e "Oh, thank you! That's so kind of you."

    show marley serious at left with dissolve

    m "Just for technical reasons I need to ask—are there any vampires in the area?"

    show emily sad at right with dissolve

    e "No, none live 'round here."
    m "Well, that keeps things uncomplicated. The anti-ghoul charms affect vampires as well. If you learn of an upcoming visit, would you please let me know about it? I'll need to edit the spells a little."

    show emily neutral at right with dissolve

    e "Of course—that's very forward thinking of you, Marley. Thank you."
    e "And—thank you for coming, Ron. Danny told me you're having difficulty being back here. It means a lot that you want to help us. This town is so important—I've lived here most of my life—Kingston means everything to me."

    show ron serious at center with dissolve

    r "Of course, ma'am. We'll do everything we can to protect it."
    e "And I want justice, against whoever has been doing this. Etiam dii et reges ad Dominae Iustitiae potestatem flectere debent."

    show ron confused at center with dissolve

    r "Huh?"

    show marley thoughtful at left with dissolve

    m "It's Latin. Something about... gods and kings-"

    show ron neutral at center with dissolve
    show emily smile at right with dissolve

    e "'Even gods and kings must kneel to the might of Lady Justice.' The motto of my university, words to live by."

    show ron awkward at center with dissolve

    r "Well, that's nice."

    show ron neutral at center with dissolve

    r "Anyway, we should get going; got places to go before night falls. Speak to you later Mayor Sawyer—sorry, {i}Emily{/i}."

    show emily smile at right with dissolve

    e "I'll see y'all around! If ya' ever need anything, feel free to drop by!"
    r "We will. Goodbye!"

    scene black with fade

    jump d1s5_map