label d1s11c_norman:
    $ visited_d1s11c_norman = True

    show norman neutral at right with dissolve
    show terry neutral at centerright with dissolve
    show ron neutral at centerleft with dissolve
    show marley neutral at left with dissolve

    r "...Norman. You used to work in the mayor's office, right? That's one of the crime scenes."

    show norman moody with dissolve

    n "Yeah, I worked there with the evil cow. What do you wanna know?"
    t "Umm do y'all want some privacy for this? 'Cos I was just about to head out. You can use my desk if you want."
    r "Thanks. And yeah, you can go if you'd like."
    t "Cool, see ya later!"

    show terry smile with dissolve

    t "And goodbye to you, Miss Marley. Until we meet again."

    show marley moody with dissolve

    m "I'd say 'I'll miss you,' but my therapist told me I should work on being more honest."

    "And with a wink to Marley, he's gone."

    show terry smile at offscreenleft with move

    show norman moody at right
    show ron neutral at center 
    with move

    "Norman glowers at Marley."

    n "If you're smart, you'll keep your legs closed around Terry Maddux."
    m "... Thanks for the heads up?"
    n "Not that you'll listen to me. Women are so dumb an' shallow, always going for good looking bullies, rather than nice guys. And by the time they realize how dumb they're being, they're worn out!"

    show marley angry with dissolve

    "What the hell?!! I can't believe someone would actually say that!"
    "But... even though he's talking to Marley, there's a faraway look in his eye that makes me wonder if there's someone else on his mind."
    "Of course, that means jack to Marley. Understandably."

    m "How {i}dare{/i} you—"

    "Okay, time to start the interview, before she draws blood."

    show ron serious with dissolve

    r "Okay Norman, I'm wondering if you can help me clear something up. I know that here, the library, and the mayor's office were all attacked. But I can't get a straight answer about what order they were attacked in."
    r "One was Thursday, one was Friday, and one Saturday. But people have given different orderings—"

    show norman thoughtful with dissolve

    n "Is that so? Well, if that dog of a mayor is one of the people with a different story, then I reckon she's lying through her teeth."

    show ron thoughtful with dissolve

    r "Wait, really? Why would she lie?"

    show norman moody with dissolve

    n "Because she's a liar! That's what she does!"

    "Wow, he really doesn't like her. But that doesn't mean that the mayor is wrong about the order..."

    show ron thoughtful with dissolve

    r "Well, you worked at one of the scenes—it was your desk that was smashed, wasn't it?"
    n "It was! And don't you forget it!"
    r "So, can you tell us when it was smashed? If it was Thursday night, you would have seen on Friday when you came into work—"

    show norman neutral with dissolve

    n "Nah, I skipped work Friday. Couldn't be bothered going in."

    "Wow—how was this guy the workaholic mayor's assistant?"

    show ron serious with dissolve

    r "So you don't know when it was attacked?"

    show norman thoughtful with dissolve

    n "Well, uh... I know it weren't Saturday."

    show ron surprised with dissolve

    r "What? Really?"
    n "Yeah. I came back on Saturday."

    show ron confused with dissolve

    r "To work?"
    n "God, no! No, I left my cigarettes there. But the office was already screwed when I got there that day. I thought that cow had finally gone crazy and wrecked it. But yeah, I guess that means it weren't attacked on Saturday night."

    "Hmm... so that means Mrs. Pear isn't right about the order of attacks."
    "That's good to know—that means either Terry or Emily is right..."

    show ron neutral with dissolve

    r "Thank you, Norman. That'll be very useful."

    show ron thoughtful with dissolve

    r "Now, no offence, Norman, but you... you don't exactly seem like the work-orientated type."

    show norman moody with dissolve

    n "That work was beneath me!"

    "Uh huh."

    r "So, how come you were at the office earlier today? It's Sunday."

    show norman angry with dissolve

    n "I got a darn letter telling me I been fired! I got it Saturday, but I didn't check my mail till Sunday. And once I read it, I rushed in to confront that worm."
    r "I see."
    r "Okay, moving on—can you tell me where you were on..."

    "Hm... I want to get his alibi for all three attacks. But I only have time to ask about one."

    menu:
        "... Thursday night? What were you up to after work?":
            # Fill in section 1.1 of Norman's suspect file.
            jump d1s11c_norman_o1

        "Friday night? You do anything after, say, 8:30?":
            # Fill in section 1.2 of Norman's suspect file.
            jump d1s11c_norman_o2

        "Saturday night? Last night, I mean. Anything fun?":
            # Fill in section 1.3 of Norman's suspect file.
            jump d1s11c_norman_o3

label d1s11c_norman_o1:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "... Thursday night? What were you up to after work?"

    show norman moody with dissolve

    n "Wait—wait, are you getting my alibi? Are you {i}suspecting{/i} me?!"

    show ron awkward with dissolve

    r "Well, uh—"

    "I don't think I can get out of this one. Might as well bite the bullet and be honest."

    show ron serious with dissolve

    r "Frankly, yes, I am. I'm treating everyone involved in this case as a suspect, until I can rule them out."
    n "..."

    "He's glowering at me in awkward silence..."

    show norman thoughtful with dissolve

    n "Wait, hang on..."

    show norman smile with dissolve

    n "Does that mean Emily Sawyer is a suspect?"
    r "... Yes. Yes, it does."
    n "Good! Don't take your eyes off that conniving leech!"

    show ron awkward with dissolve

    r "O-okay then. And why is that?"

    show norman moody with dissolve

    n "You'll see. If you're smart enough."

    show norman neutral with dissolve

    n "Anyway, Thursday night, I was at a bar. Get there maybe... 5:00? Left... I don't know what time—I was black out drunk. It's a miracle I didn't crash on the way home!"

    "Oh good. Drunk driving. Upstanding member of the community."

    n "And that's why I didn't go into work on Friday—hangover from hell."

    show ron thoughtful with dissolve

    r "I see. Did you know anyone there? Anyone who can vouch for you?"
    n "No, I don't really know anyone there."

    jump d1s11c_norman_c1

label d1s11c_norman_o2:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "Friday night? You do anything after, say, 8:30?"

    show norman moody with dissolve

    n "Wait—wait, are you getting my alibi? Are you {i}suspecting{/i} me?!?"

    show ron awkward with dissolve

    r "Well, uh—"

    "I don't think I can get out of this one. Might as well bite the bullet and be honest."

    show ron serious with dissolve

    r "Frankly, yes, I am. I'm treating everyone involved in this case as a suspect, until I can rule them out."
    n "..."

    "He's glowering at me in awkward silence..."

    show norman thoughtful with dissolve

    n "Wait, hang on..."

    show norman smile with dissolve

    n "Does that mean Emily Sawyer is a suspect?"
    r "... Yes. Yes, it does."
    n "Good! Don't take your eyes off that conniving leech!"

    show ron awkward with dissolve

    r "O-okay then. And why is that?"

    show norman moody with dissolve

    n "You'll see. If you're smart enough."

    show norman neutral with dissolve

    n "So anyway, Friday—spent most of the day bummin' around—playing video games, scrolling 4chat, whatever. Around sundown, I was probably playing Guild of Greats."

    show ron neutral with dissolve

    r "And were you with anyone?"

    show norman awkward with dissolve

    n "What, like a chick?"

    show norman moody with dissolve

    n "No."
    r "Okay—"

    show norman awkward with dissolve

    n "Not 'cos I can't pull or nothing—"

    "Who the hell calls it 'pulling' anymore?"

    show norman moody with dissolve

    n "Just 'cos I ain't interested in the women 'round here! They ain't up to my standards!"

    "... Sure buddy."

    r "And did you stream this or anything? Got any evidence of you being there? Or like CCTV?"

    show norman neutral with dissolve

    n "Nah, nothin' like that."
    r "Alrighty then."

    jump d1s11c_norman_c1

label d1s11c_norman_o3:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "Saturday night? Last night, I mean. Anything fun?"

    show norman moody with dissolve

    n "Wait—wait, are you getting my alibi? Are you {i}suspecting{/i} me?!?"

    show ron awkward with dissolve

    r "Well, uh—"

    "I don't think I can get out of this one. Might as well bite the bullet and be honest."

    show ron serious with dissolve

    r "Frankly, yes, I am. I'm treating everyone involved in this case as a suspect, until I can rule them out."
    n "..."

    "He's glowering at me in awkward silence..."

    show norman thoughtful with dissolve

    n "Wait, hang on..."

    show norman smile with dissolve

    n "Does that mean Emily Sawyer is a suspect?"
    r "... Yes. Yes, it does."
    n "Good! Don't take your eyes off that conniving leech!"

    show ron awkward with dissolve

    r "O-okay then. And why is that?"

    show norman moody with dissolve

    n "You'll see. If you're smart enough."

    show norman neutral with dissolve

    n "Anyway, yesterday? I binged my shows."

    show ron curious with dissolve

    r "Shows?"

    show norman thoughtful with dissolve

    n "You know, TV-there's {i}'Keeping up with the Vanrunians'{/i} and {i}'Dr. Fill'{/i} and the one with all the hot people who aren't allowed to get it on."

    show norman smile with dissolve

    n "'Sides from when I went to get my cigarettes, I didn't move from the couch once! Not even to pee!"

    show marley disgusted with dissolve

    m "Wait, what?"

    show ron awkward with dissolve

    r "And you were alone?"

    show ron worried with dissolve

    r "I hope."

    show marley neutral with dissolve
    show norman awkward with dissolve

    n "For once, haha! Normally I bring home a solid 10 every night! At least one! Usually more! But sometimes, a guy needs some 'me' time! Gotta be a lone wolf for a day, you know?"

    show ron serious with dissolve

    r "... Uh... huh..."
    n "So I had to disappoint the ladies last night. But they were texting me all night, begging to come over. But I stayed strong!"

    "Sure they did buddy."

    r "Can I see these texts?"

    show norman worried with dissolve

    n "What? Why?"

    "I suppose I can't actually say, 'Because I know you're lying and I want to watch you squirm.'"

    r "... For the investigation."

    show norman awkward with dissolve

    n "Well, uh... I can't show you. I deleted all the texts. And my regular phone is..."

    show norman moody with dissolve

    "It got stolen! And then trashed, and then stolen again! Long story. Anyway, I only have the junk flip phone I keep for emergencies. And it has, like, no memory."

    "Riiiiight."

    r "Well, do you have any evidence that you were doing what you said you were doing?"

    show norman thoughtful with dissolve

    n "Besides the new stain on my couch, no."

    show marley scared with dissolve

    m "WHAT STAIN?!"

    "Oh God, I don't even wanna know!"

    jump d1s11c_norman_c1

label d1s11c_norman_c1:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "Well, thank you for that, Norman. That'll be very useful. Now, we know about some folks that seem to be involved in the case. I'm tryin' to get a sense of how everyone feels about each other. All the different relationships."

    show norman moody with dissolve

    n "Okay?"
    r "So I wanted to ask you about your relationship with..."

    "Now who should I ask about? He an' Emily seem so {i}icy{/i}. And there was certainly no love lost between him an' Terry, from what we saw when we came in... Would he even know who Mrs. Pear or Danny are? Or Seb?"

    menu:
        "... Emily. The two of you don't seem fond of each other. She just fired you, didn't she?":
            # TODO: Fill in section 2.1.1 of Norman's suspect file and section 2.2.2 of Emily's.
            jump d1s11c_norman_c2o1

        "... Terry, the sheriff. You two know each other at all?":
            # TODO: Fill in section 2.3.1 of Norman's suspect file and section __ of Terry's.
            jump d1s11c_norman_c2o2

        "... Mrs. Pear, the librarian. You ever meet her? Know her at all?":
            # TODO: Fill in section 2.4.1 of Norman's suspect file and section 2.2.2 of Mrs. Pear's.
            jump d1s11c_norman_c2o3

        "... Danny, Emily's boy. You have much to do with him?":
            # TODO: Fill in section 2.5.1 of Norman's suspect file and section 2.2.2 of Danny's.
            jump d1s11c_norman_c2o4

        "... Seb. You know him? Seb Daley.":
            # TODO: Fill in section 2.2.1 of Norman's suspect file and section 2.2.2 of Seb's.
            jump d1s11c_norman_c2o5

label d1s11c_norman_c2o1:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "... Emily. The two of you don't seem fond of each other. She just fired you, didn't she?"

    show norman moody with dissolve

    n "That's no understatement. If I was locked in a room with her, Hitler, an' Mussolini, an' I had a gun with two bullets, I'd shoot her twice."

    show ron surprised with dissolve

    r "Seriously? You hate her that much?"
    n "More."

    show ron curious with dissolve

    r "Why?"
    n "Well for one thing, she's a bossy cow. 'Norman do this,' 'Norman do that,' all the time!"

    show ron awkward with dissolve

    r "Well... well she {i}was{/i} your boss."

    show norman angry with dissolve

    n "Look, she's a lyin', manipulative cow! And that's the truth."

    show ron curious with dissolve

    r "And you say this, why? What's she done that's so manipulative? What's she lying about?"

    show ron awkward with dissolve

    n "Well, uh—"

    show norman serious with dissolve

    n "Like- like that extra fundin' for the school. She gave it under the condition that it only be used for certain things—things {i}she{/i} approved of!"
    r "Like what?"
    n "Academics!"

    show ron confused with dissolve

    r "... Well, it {i}is{/i} a school."
    n "Clubs! But, like, not sport ones—"

    show ron serious with dissolve

    r "I gotta say, when I was there, they didn't much care for grades. In my class, only one that ever got A's was Seb Daley, an' that was 'cos his dad tutored him. An' the only clubs we had were soccer, football, hockey, baseball, an' basketball."
    r "But the teams, they had everything. New uniforms every season, coaches on head-spinning salaries, fancy training equipment."
    r "Now, don't get me wrong, I keep myself fit. But I don't much like sports now, an' I hated them back then. Those teams, they were nasty to anyone who weren't one of 'em. Who weren't good enough. Young me would've killed to have clubs that interested me."
    r "Do you really care that much about the money sent to the school having strings attached?"

    show norman moody with dissolve

    n "It's just... not right! It's her manipulating things!"

    "No. No, I don't believe for one second that Norman has this much hatred for the mayor just because she acted like his boss an' because she—a politician—has a political agenda."
    "There's something he's not tellin' me here. Something's not adding up. But I don't think I'm gonna get it from him—not so easily. I'm gonna need to work on him for some time, I think. But for now..."

    r "Alright, well, can you sum up your feelings towards Emily Sawyer in one sentence?"
    n "One sentence?"

    show norman angry with dissolve

    n "One sentence ain't enough to say all the hatred I got for that wretch."
    r "... Well, I think that'll do."

    jump d1s11c_norman_c3

label d1s11c_norman_c2o2:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "... Terry, the sheriff. You two know each other at all?"

    show norman moody with dissolve

    n "Terry Maddux is a blight on this town—his whole dang family is."

    show ron surprised with dissolve

    r "Really? Most folks 'round here seem real fond of the Maddux family—they founded the town, after all."
    n "Over three hundred years ago! Why do Terry an' his pa' get glory for something some dead guy did forever ago?!"

    "I can't believe I actually agree with Norman on something."

    show ron thoughtful with dissolve

    r "Okay, so you don't like the Madduxes as a whole, but what about Terry specifically? You interact with him much?"

    show norman thoughtful with dissolve

    n "Not really. I was close to Freddy—Terry's grandpap. Only Maddux I could stomach. An' Terry was his li'l darlin'. But we never really interacted back then—he was a kid. Then Freddy died. Avoided the family after that."

    show norman moody with dissolve

    n "Then that bastard got made sheriff. Pokes his nose into everyone's business. I do my best to avoid him, but recently I've had to speak to him once or twice."

    show ron curious with dissolve

    r "Oh yeah? How come?"
    n "Because some maggots ruined my life!"

    show ron confused with dissolve

    r "Huh?"

    show norman curious with dissolve

    n "Eh, it's a long story. But basically, I needed his help—needed that lazy bum to do his darn job. But the bastard never bothered to help."

    "Hmm. That's a bit of the pot calling the kettle black."

    show ron serious with dissolve

    "Could you please sum up your relationship with him an' what you think of him in one sentence?"

    show norman thoughtful with dissolve

    n "Well to put it polite-like, I think he's a moron an' I hope him an' his family all burn!"

    "Well, that seems extreme..."

    jump d1s11c_norman_c3

label d1s11c_norman_c2o3:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "... Mrs. Pear, the librarian. You ever meet her? Know her at all?"

    show norman thoughtful with dissolve

    n "The ancient librarian? The one that looks like a walking corpse? Yeah, I kinda know her. She's friends with that cow, Emily."

    show norman neutral with dissolve

    n "They go to lunch together a few times a week. The old bat is probably the mayor's only friend."
    r "But what about you? Do you ever speak to her?"
    n "No. I mean I {i}know{/i} her, but we pretty much ignore each other."
    r "I see."

    jump d1s11c_norman_c3

label d1s11c_norman_c2o4:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "... Danny, Emily's boy. You have much to do with him?"

    show norman moody with dissolve

    n "Humph. He's a spoiled little brat. Regular mamma's boy."

    show ron curious with dissolve

    r "Oh yeah?"

    show norman thoughtful with dissolve

    n "We {i}used{/i} to just... I dunno, coexist. Didn't really acknowledge each other. I just saw him at the end of every Friday workday, when the two of them went off for their weekly mommy-son bonding."
    n "They always go for a walk through Kingston woods then get dinner together. Whenever he'd get to the office to pick her up, we'd kinda just nod to each other. Make small talk sometimes."
    n "But then a few weeks back, he became rude. Terse. Called me names. If he weren't my boss's son, I would've beat him black 'n blue."

    show norman moody with dissolve

    n "He became a real butt. Fakes bein' normal around his ma' an' other folks, but when there ain't no one to see, he's real vile."

    "Really? Huh. That ain't a side I've ever seen of Danny. Of course, Norman could just be full of it. That sounds pretty likely, come to think of it."

    jump d1s11c_norman_c3

label d1s11c_norman_c2o5:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "... Seb. You know him? Seb Daley."

    show norman moody with dissolve

    n "Before that boy's momma came here, everyone in Kingston was nice {i}human{/i} folk. Now, we got to put up with her half-orphan mutt running about."

    show marley serious with dissolve

    "Don't get mad. Don't shout. Stay professional. Don't compromise the investigation."

    r "Uh huh?"
    n "An' now he's at the school, indoctrinating kids into thinking this kinda thing is natural."

    show marley angry with dissolve

    "Deep breath, calming thoughts... Oh no, Marley looks like she's about to snap."

    n "An' what's more, I hear he's gay!"
    r "Bisexual."

    show norman confused with dissolve

    n "Huh?"
    r "He's bisexual. Attracted to more than one gender."

    show norman moody with dissolve

    n "Humph! All seems like junk to me! Seems like he's either gay and won't admit it, or straight but he wants to feel special."

    "And with that, the last of my willpower vanishes."

    show ron angry with dissolve

    r "I'm gay."

    show norman surprised with dissolve

    n "Uh-w... what now?"
    r "I'm gay. Homosexual. I sleep with and have romantic feelings for men. And if you have a problem with me or people like me, I suggest you keep your opinions to yourself."

    show norman awkward with dissolve

    r "Now, I'd thank you to answer my question. Do you {i}know{/i} Seb? Properly? Or just know gossip about him?"
    n "Uh, I... I don't. Don't know him. Not really. Knew his ma'. But that's it."

    show ron moody with dissolve

    r "That's all I need."

    jump d1s11c_norman_c3

label d1s11c_norman_c3:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "Thank you, Mr. Conlee, that'll be very helpful. Now, I have one last set of questions for you."

    show norman moody with dissolve

    n "Well hurry the hell up. I ain't got time to yap for hours on end!"

    show ron serious with dissolve

    r "That's fine. Now, like I said, the mayor's office, the library, an' here were all attacked. So can you tell me about the last time you were at..."

    menu:
        "... the mayor's office before it was vandalized. Would this have been Thursday?":
            # TODO: Fill in section 3.1 of Norman's suspect file.
            jump d1s11c_norman_c4o1

        "... here, before the attack. You been over recently?":
            # TODO: Fill in section 3.2 of Norman's suspect file.
            jump d1s11c_norman_c4o2

        "... the library, before it was hit?":
            # TODO: Fill in section 3.3 of Norman's suspect file.
            jump d1s11c_norman_c4o3

label d1s11c_norman_c4o1:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "... the mayor's office before it was vandalized. Would this have been Thursday?"
    n "Yeah, that would have been it."
    r "And what time did you arrive and leave?"

    show norman thoughtful with dissolve

    n "Well, my shift is meant to start at 9, but I remember that witch of a boss bein' mad I was late, so I probably got there... I think she moaned at me for being an hour and a half late, so probably 10:30. And then I left at 4:30."
    r "And you just worked all day? Nothing interesting happened?"

    show norman neutral with dissolve

    n "Nope."
    r "You notice anything odd that day? Anything out of the ordinary?"

    show norman thoughtful with dissolve

    n "Well, I guess... Emily left early that day."

    show norman neutral with dissolve

    n "She {i}never{/i} leaves early. Ever. But that day, she left the same time as me. An' she seemed... {i}happy{/i}. I mean she's often disgustingly chipper, but it was way worse. She was beaming ear to ear the whole way out."

    show ron curious with dissolve

    r "Did she tell you why she was so happy?"
    n "Nah—we don't got that 'making small talk' kinda relationship."

    show ron thoughtful with dissolve

    r "I see."

    jump d1s11c_norman_c5

label d1s11c_norman_c4o2:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "... here, before the attack. You been over recently?"

    show norman thoughtful with dissolve

    n "Here? Well, that would have been Friday. From maybe 3:20 to 3:50 p.m."

    show ron curious with dissolve

    r "Really? Did you see the busted up desk while you were there?"
    n "Nah. Didn't come far enough into the room to see it."

    show ron serious with dissolve

    r "I see. And why were you here?"

    show norman serious with dissolve

    n "Well, I had some belongings of mine—some tech—broken. I took it to this local repair shop to get it fixed. Well, on Thursday night, the shop got broken into. My stuff—{i}and only my stuff, mind you{/i}—was taken!"

    show ron thoughtful with dissolve

    r "Really? That sure is interesting... Any idea why?"

    show norman moody with dissolve

    n "... No. No clue. But it's a {i}real{/i} pain in my butt! Anyway, as soon as I heard on Friday, I came right over here. The owner—some immigrant fella with a funny name—he'd already reported it."
    n "But I wanted the cops to know that if they didn't get their behinds in gear an' find my stuff, they'd have me, the mayor's personal assistant, to answer to!"

    "Except... he's not the mayor's personal assistant anymore, is he? Did he often use his old position to throw his weight around? Because he suddenly ain't got nothing to back himself up with."

    show ron serious with dissolve

    r "So who did you talk to about this theft?"
    n "Terry—he's the one that took the shop owner's report, so he was the guy to talk to."
    r "And did you notice anything odd when you were there?"

    show norman thoughtful with dissolve

    n "Terry... well, he seemed real distracted. He had a notebook, but I don't think he wrote down a word."

    show norman moody with dissolve

    n "Lazy bones. But he kept glancing back at the doors to the bullpen. Think something else was on his mind."

    "Hmm. Well, I guess that would have been the day after the first attack, so I guess him being distracted makes sense."

    jump d1s11c_norman_c5

label d1s11c_norman_c4o3:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "... the library, before it was hit?"

    show norman thoughtful with dissolve

    n "The library, huh? I ain't been there in years—I'm pretty sure I had an account there once... but I think it got suspended."

    show norman surprised with dissolve

    n "Oh no wait, I remember now!"

    show norman neutral with dissolve

    n "I {i}did{/i} go back there a while back—like ages ago."

    "Hm. If it was so far back, I doubt it'll be useful. But you never know."

    r "When was this?"

    show norman thoughtful with dissolve

    n "God, I don't know... it... actually, it must have been... maybe four years ago? Ish? Yeah—'cos it was right at the beginning of her whole 'fix up the library' crusade."

    "Wait—Emily's been working on this library thing for four years?!"

    n "The evil leech was examining the building that day with some fancy-shmancy experts. But, once she got back to her office, she realized she'd left some important documents back in the library an' sent me to go grab them."
    n "So I ran in and found them on a table."
    r "And did anything odd happen that you can remember?"

    show norman serious with dissolve

    n "Oh did it ever. I remember that it was late—right before the library closed. Only person there was that ancient librarian, Mrs. Pear. But at first, I didn't realize she was there."
    n "I ran in, found the documents, an' then... I heard rustling. Creepy whispering. I followed it an' found the creepy hag sittin' at a table, looking over this ancient book—and I mean {i}ancient{/i}; as in, I don't think it was a library book—looked like it belonged in a museum."

    show norman thoughtful with dissolve

    n "She was reading it carefully—she was wearing these big white gloves , I think—an' muttering to herself. I dunno—it was {i}hella{/i} creepy."

    show norman serious with dissolve

    n "An' then she saw me watching her. And she went nuts! Screamed at me to get out, so I ran."

    show ron thoughtful with dissolve

    r "I see. That's... curious. Did she mention it the next time you saw her?"

    show norman neutral with dissolve

    n "Nope. She kinda pretended it never happened. So, I went along with that."
    r "Hmm. Okay."

    jump d1s11c_norman_c5

label d1s11c_norman_c5:
    show norman neutral with dissolve
    show marley neutral with dissolve
    show ron neutral with dissolve

    r "Alright, thank you for that, Norman. That's all the questions I got for you."

    show norman thoughtful with dissolve

    n "This is a mighty amount of work just for some attacks on public property. The cops were sayin' they think it's just kids."

    show ron awkward with dissolve

    r "Well, uh—"

    show ron serious with dissolve

    r "Well, it- it probably is. But being that two of the attacks happened at what were meant to be secure locations, they've brought me in just to make sure there ain't anythin'... {i}sinister{/i}, going on."

    show norman curious with dissolve

    n "Wait—do y'all think this could be like... a {i}spy{/i}, or something? Maybe someone sent by 'em magic freaks on that island—"

    "Okay, I think I need to stop his speculating—"

    r "That ain't a current theory, Mr. Conlee."

    show norman serious with dissolve

    n "Well you should consider it! You can't trust these—"
    r "Thank you, Mr. Conlee. That'll be all, for now."

    scene black with fade

    jump d1s10_map