# Mrs. Pear
label d1s6e:
    scene bg library with fade

    show danny neutral at right with dissolve
    show marley neutral at center with dissolve
    show ron neutral at left with dissolve

    "Walking into the library is like being dragged back through time. The musty smell of the books. The perfect silence. The calm."

    r "This place hasn't changed a bit."
    b "Yeah, Mom says that she keeps trying to give it funding for refurbishment, but the council keeps blocking her."

    # SFX- knocking on wood

    "The sound of knocking on wood makes me glance over to the library's main desk."

    show pear neutral at left with dissolve

    r "Holy cow, it's Mrs. Pear! I thought she'd be long dead!"

    show pear angry at left with dissolve

    l "I ain't dead, Ronald Kitzinger, and I sure ain't deaf, either."

    show ron blushing at left with dissolve

    r "Oh shoot, uh, sorry, Mrs. Pear. I hear the library was attacked by gh— vandals a few days ago?"

    show pear neutral at left with dissolve
    show ron neutral at left with dissolve

    l "That's what they tell me. ‘Course, I don’t know any of the details. People don’t tell me anything no more. But this all seems mighty suspect to me."

    "Uh oh. Seems like Mrs. Lemon is catching onto the truth. She always was sharp as a whip."

    show pear moody at left with dissolve

    l "When I first called the sheriff’s office about all this, do you know what he said?"
    l "He said it must have been a racoon or something, and I was going batty."
    r "I, uh—I'm sorry about that, Mrs. Pear. That sucks."

    "She waves away my concern with a hand."

    show pear neutral at left with dissolve

    l "Of course, the fact that the sheriff’s office was attacked the next day and the mayor’s the day after doesn’t help. Even the sheriff can’t be thick enough to think this isn’t coordinated attacks."
    r "Right… Can I ask what area was attacked?"
    l "The occult section. As if that wasn’t suspicious enough! If the sheriff {i}really{/i} thought a racoon would only attack books that fall between 131 and 139 on the Dewey Decimal System, then he needs a lobotomy."

    show ron laughing at left with dissolve

    r "Haha, yeah. Do you know what books were destroyed in the attack?"

    show ron neutral at left with dissolve

    l "Not off the top of my head. But I have a record of them somewhere."
    r "Can I see?"
    l "Well, it'll probably take me a while to compile but I can get a list to you over the next few days."
    r "Thank you. Is the occult section still where it used to be?"
    l "Sure is. The old chair you used to sit on is still there too. And the one your skinny friend sat in. But not the one the plump little one that always used to pick his nose used. We had to get rid of that one. The base was… crusty."

    show marley disgusted at center with dissolve

    m "Oh eww."

    show danny angry at right with dissolve

    b "Hey! I never picked my nose!"
    l "Oh, it's you. I didn't recognize you."
    b "And I wasn't fat! I was big boned."
    l "Uh-huh…"

    show ron laughing at left with dissolve
    show marley laughing at center with dissolve

    r "Hehe."
    m "Hehehe, I like this woman."

    show danny neutral at right with dissolve

    r "Oh, sorry Marley—Mrs. Pear. Mrs. Pear, this is Marley, my assistant. She's a Witch."

    show pear moody at left with dissolve

    l "Oh. You are? You ain't planning to do any of that creepy magic crap, are you? I don’t like that stuff. Keep it away from me."

    "What the hell? I've never heard Mrs. Pear talk about magic like that; I had no idea she was so suspicious of it."

    show marley moody at center with dissolve

    m "Well, I have my Level One license, ma'am. I'm permitted by law to do—"
    l "I don't care about your darn license. You don't do that mumbo-jumbo junk around me, you hear?"

    "As I watch, astounded, Mrs. Pear digs her hand into the pocket of her jacket and pulls out a packet of salt—the kind they keep at diners to put on your fries. She rips open the paper wrapper and tosses the contents over her shoulder."

    "What the actual hell?"
    "But Marley seems to recognize the gesture. And her face turns thunderous."

    show marley angry at center with dissolve

    "But she bites her tongue, keeping silent. Letting me deal with the old woman who was once one of my only friends. Who is now insulting my current best friend."
    "Damn."
    "Okay, okay, think this through, Ron."
    "I can tell her off."
    "I can focus on being serious, professional."
    "Or I can talk to her as a friend."

    menu:
        "Hey, don't you dare talk to her like that! That's my assistant and {i}friend{/i} you’re disrespecting, and I ain't gonna abide that kind of attitude against her.":
            jump d1s6eo1

        "I can't promise we won't utilize Miss Shipway's specific skill set. This is an important case. And please, my assistant deserves all the respect and politeness you afford me. She's a responsible magic wielder and a key part of this investigation.":
            jump d1s6eo2

        "Don't get me wrong Mrs. P, sometimes she freaks me out with all the crazy crap she can do. But she's a good woman; she don't deserve no disrespect. So kindly treat her with dignity, alright?":
            jump d1s6eo3

label d1s6eo1:
    show danny neutral at right with dissolve
    show marley angry at center with dissolve
    show pear moody at left with dissolve
    show ron angry at left with dissolve

    r "Hey, don't you dare talk to her like that! That's my assistant and {i}friend{/i} you’re disrespecting, and I ain't gonna abide that kind of attitude against her."

    show pear angry at left with dissolve

    pause(0.5)

    show pear sad at left with dissolve

    l "I'm sorry, young lady. I-I've had some… difficult experiences with magic wielders that've made me a tad weary of them."
    l "But I shouldn’t have taken that out on you. And if Ron says you're a responsible spellcaster—well, then I believe him."

    show pear awkward at left with dissolve

    l "But, well, if I can ask you a mighty big favor, my gal?"

    show marley awkward at center with dissolve

    m "Uh..."
    l "If- if ya do any of your fancy spells, well, could you do it away from me? Just… I don’t mean to be cruel, but it brings back some… bad memories."
    m "Uh- well, I… I don’t want to make you uncomfortable, ma’am. I don’t want to trigger your trauma."

    show pear neutral at left with dissolve

    l "That’s mighty kind of you, dearie. You’re a nice gal, Miss Marley."

    "She is not. Don't get me wrong, I love her like a sister. But she ain't what I would call 'nice.'"
    "Marley looks uncomfortable. I'd better change the subject."

    jump d1s6ec1

label d1s6eo2:
    show danny moody at right with dissolve
    show marley angry at center with dissolve
    show pear moody at left with dissolve
    show ron serious at left with dissolve

    r "I can't promise we won't utilize Miss Shipway's specific skill set. This is an important case. And please, my assistant deserves all the respect and politeness you afford me. She's a responsible magic wielder and a key part of this investigation."

    show pear thoughtful at left with dissolve

    l "Look, miss, I appreciate I may have been a little… curt. I just… I've had some experiences that make me mighty uncomfortable around people that use magic."
    l "So please, for my sake, keep any magic shenanigans away from me."

    show marley moody at center with dissolve

    m "Well, I'm fine doing that."

    "I guess that's something."
    "I think it's best to move on now."

    jump d1s6ec1

label d1s6eo3:
    show danny neutral at right with dissolve
    show marley angry at center with dissolve
    show pear moody at left with dissolve
    show ron smile at left with dissolve

    r "Don't get me wrong Mrs. P, sometimes she freaks me out with all the crazy crap she can do. But she's a good woman; she don't deserve no disrespect. So kindly treat her with dignity, alright?"

    show pear smile at left with dissolve

    l "Oh, those Witches and Warlocks and whatever always give me the creepy-crawlies. Have since I was a gal."
    l "I've seen some mighty odd stuff in my time thanks to magic users."

    show pear thoughtful at left with dissolve

    l "Some mighty awful things."
    l "Makes a person wary, you know?"

    show pear smile at left with dissolve

    l "Uh, but I probably was a bit too rude to your gal… I'm sorry, dearie. But—well, when you do your fancy magic, would you mind terribly just keeping it away from me?"

    show marley moody at center with dissolve

    m "Yeah, sure."

    "Well, situation diffused—kinda."
    "Think I'd better change the topic."

    jump d1s6ec1

label d1s6ec1:
    show danny neutral at right with dissolve
    show marley neutral at center with dissolve
    show pear neutral at left with dissolve
    show ron neutral at left with dissolve

    r "Do you have any CCTV around the building?"

    show pear nervous at left with dissolve

    l "Oh, well, yes, but I don't understand this new-fangled computer system it's hooked up to."
    r "Well, uh, would you mind taking Danny to the back office so he can have a look at it?"

    show danny uncertain at right with dissolve
    show pear neutral at left with dissolve

    b "Oh, won't you need help examining the scene?"
    r "No, I've got it, don’t worry."
    l "Come on, nose picker."
    b "Don't call me that!"

    show pear neutral at offscreenleft with move
    show danny uncertain at offscreenright with move
    show marley neutral at right with move

    "I turn to Marley."

    show ron confused at left with dissolve

    r "What was that thing she did? The thing with the salt packet?"

    "My eyes glance down to the little clear crystals scattered across the floor."

    show marley serious at right with dissolve

    m "It's one of those superstitions. Meant to ward off Infernals. To Warlocks, it's a real eff-you. To a Witch, it's… ignorant. Not only is it an attempt at hurting part of who I am at my core, but… it’s the wrong core. Like calling an English person 'Yankee scum.'"
    m "Anyway, I'll go put up the charms."

    show marley serious at offscreenright with move
    show ron confused at center with move

    "Strange. Very strange. Seb's half-elf, so he's a magical creature. But Mrs. Pear seemed to like him, at least when we were kids. And she always seemed to like talking about magic and stuff."
    "So why was she so frosty to Marley?"
    "I head towards the stacks, my feet remembering the route before my mind does."
    "The occult section looks pretty bad. The bookcase has been trashed and none of the books on it seem to have survived. Scraps of paper are sprinkled over everything like snow. There's no way to tell which shreds belong together or which torn up covers they've come from."
    "If I were a betting man, I'd say someone really didn't want folks knowing what books were in that wreckage. Or maybe they didn't want anyone reading up on what they've been doing."
    "There's glass everywhere from a nearby window that’s been smashed in. I wander over to it and see mud and dirt tracked onto the carpet, forming the shape of shuffling footprints."

    s  "'And the hungry worm went {i}chomp chomp chomp{/i}, and soon, there was nothing left of the apple!'"

    "The familiar voice hits me like a punch to the gut."
    "Seb."
    "I slink through the shelves, keeping my head low so no one can see me."
    "I follow the voice to the children's section. I peer around the shelf and see him in a small nook, sitting on a low chair, surrounded by wide-eyed five-year-olds."
    
    scene bg seb_reading with fade

    s "So what do you think happened to the hungry worm?"
    k1 "It got bigger!"
    s "That's right, it got even {i}bigger{/i} than it was before!"

    "I can't stop the slow smile that creeps across my face as I watch him."
    "My first ever crush. He hasn't changed. Oh, sure, he's gotten taller. But he's got the same kind smile. Same cheeky, laughing eyes. Same bright purple hair—though I can’t help but notice a tuft has been chopped off, ruining his otherwise careful hairdo."
    "My chest begins to hurt and I think of all the things I wanted to say then and all the things I want to say now and all the things I never want him to know."
    "The children are looking at him adoringly as he reads from a colorful picture book, displaying the drawings on each page for them."
    "The scene is perfect."
    "And I'm a coward."
    "So I turn away, not wanting to disturb him."
    "But behind me, I hear Seb's voice falter."

    s "'Bigger and bigger—' Oh my God, Ron?"

    "I stop short."
    "And slowly, hesitantly, look over my shoulder."
    "I meet his gorgeous eyes, and my heart leaps into my throat."
    "He wasn't meant to see me— I'm not ready— Oh crap. Crap!"
    "I should run— No, that would be weird."
    "I could pretend I haven’t seen him and wander away."
    "But it’s pretty darn obvious I've seen him; I'm staring right at him!"
    "Oh blast it, we're just gawking at each other!"
    "I need to do something!"

    k2 "Hey, why've you stopped? Keep reading!"

    "He blinks, as if coming out of a trance, then glances back down at the book."

    s "Uh, the worm got so big that he exploded. The end."

    "He snaps the book shut."

    s "Okay, reading time's over now."
    k3 "What? That's not how that story ends!"
    s "Um, yes it is. Very sad."
    k4 "I've got that book at home. It {i}definitely{/i} doesn’t end like that!"
    "Well, uh, it's not the same book. This is an off-brand version. Anyway, I've got to go."

    scene bg library with fade

    show ron nervous at left with dissolve
    show seb nervous at right with dissolve

    "I watch as he leaps to his feet and makes his way through the sea of children, dancing left and right to avoid stepping on their little hands and feet, until he's suddenly standing right in front of me."
    "Oh man. Come on, Ron. Calm down. Be smooth."
    "And my God is he gorgeous."
    "It takes me a good few attempts to remember how to speak again."

    r "I, uh… I think you've left your audience with some complaints, Seb."
    s "Umm… don't- don’t worry about it. Kids are the worst critics. What are you doing here, Ron?"

    "Okay, smooth. I can do this."

    r "Well, a little bird told me there's trouble in town. I'm here to put it right."

    "Yep. That was smooth, right?"

    s "Huh. That'll be a first, Ron. You're always the one {i}starting{/i} trouble if I remember correctly."
    r "That’s an awfully mean thing for such a pretty mouth to say."

    show ron blushing at left with dissolve
    show seb blushing at right with dissolve

    "OH MY GOD OH MY GOD TOO SMOOTH DID I JUST SAY THAT OUT LOUD?"
    "I sound like a corny, misogynistic superhero from a 40-year-old comic!"
    "I once saw the Earth open and swallow someone whole. I think it’s darn rude that it’s not offering me a repeat performance and devouring me right now. Anything to get me away from those eyes, from the embarrassment, from my soul wanting to vomit itself out of my body."

    show seb laughing at right with dissolve

    s "Hehe, same old Ron."

    "Huh. Laughing. Not the reaction I was expecting."
    "Honestly, I thought he'd storm off."
    "Okay, maybe keep up the flirt?"

    r "Did you miss me?"
    s "I'm not going to answer that, Ron."
    r "Maybe that's answer enough, Seb."
    s "Always so cheeky. Anyway, how… how have you been? What’ve you been up to?"

    "I feel myself teetering on the edge of something deep within myself. I don’t want to fall in and learn what’s lurking within. It might be better to keep it a bit more professional."

    r "I've been good. I started up my own detective agency. You?"

    "My heart drops a bit with the weight of all the things I want to say but don’t. This isn’t the time or the place and as much as he’s smiling now, we aren’t on the same terms we were on all those years ago."

    s "I'm an English teacher up at the high school. Go Kingston Wolves, et cetera an' whatever. So, if you're a detective, are you the one investigating the attacks?"
    r "That's right. You know anything about them?"

    show seb neutral at right with dissolve
    show ron neutral at left with dissolve

    s "No. No, but I do know the kids have all been really shaken up about it. I know there's rumors that kids messing about are responsible for these attacks, but I'm sure it's not anyone in any of my classes."
    s "But to be honest, I've been trying not to get involved, and even if I was feeling nosy, no one would tell me anything."
    r "Huh?"

    show ron neutral at center with move
    show danny neutral at left with dissolve

    b "The cameras don't show nothing. The ones that worked, at least—the whole setup is old as hell. And that hag was breathing down my neck the whole time. She is so bad with technology."
    r "Like you can talk, you used your mom's email account till you were eighteen."
    b "I thought you had to pay for each account— Oh."

    show danny moody at left with dissolve

    b "Seb. It's you."

    show seb moody at right with dissolve

    s "Danny."
    b "Oh dear. Looks like you're having one of those 'hair don't' days."
    r "Danny!"
    s "At least for me, it's a one-off. It seems like all your days are 'hair oh-{i}hell{/i}-no’ days."
    r "Seb!"
    s "I'm sorry, Ron, I've got to go. I'll see you around."
    r "Wait, Seb—"

    show seb moody at offscreenright with move
    show ron neutral at right with move

    b "Come on Ron, we should go."

    show ron angry at right with dissolve

    r "What the hell, Danny? Why were you so rude to Seb?"
    b "Because {i}I{/i} remember what he did, Ron. I remember that he drove you away—"

    show ron angry at center with move
    show marley neutral at right with dissolve

    m "I've finished putting up the protection charms, Ron. I used four—one for the front door, one for the back, one over the window that's already broken, and one on the windows on the other side of the building."

    show ron neutral at center with dissolve

    r "Huh? Oh, right, great. Thanks, Mar. I guess we're done here, then. Let's go."

    scene black with fade

    jump d1s5_map