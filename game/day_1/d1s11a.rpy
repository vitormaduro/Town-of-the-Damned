# First proper interview of Seb
label d1s11a:
    scene bg library with fade

    show marley neutral at left with dissolve
    show ron neutral at right with dissolve

    r "You got the suspect files?"
    m "Yep. Ready to fill them in."
    r "Good. Mrs. Pear works here, and this was attacked one night—’course, we don't know which one. Let's see if we can find some evidence to narrow it down."
    r "The mayor said it was night three, Saturday. Terry said it was Friday, and Mrs. Pear herself said it was Thursday."

    # SFX- Footsteps

    show ron neutral at center with move
    show seb blushing at right with dissolve

    s "Ron."

    show ron blushing at center with dissolve

    r "Seb!"

    show marley thoughtful at left with dissolve

    m "Ooh, so {i}this{/i} is the infamous Seb."

    show ron awkward at center with dissolve

    r "Yeah… Marley, meet Seb. Seb, this is my assistant, Marley, whose job is to say absolutely nothing and take notes."

    show marley laughing at left with dissolve

    m "Hehehe."

    show marley neutral at left with dissolve
    show seb neutral at right with dissolve

    s "If you're looking for Mrs. Pear, she left early today."

    show ron thoughtful at center with dissolve

    r "I thought she was the only librarian—how can she leave?"
    s "Oh, I'm an official volunteer here. I'm not really meant to be left alone, but I told her I didn't mind. She's not as spry as she used to be, of course. So she often heads home early and leaves me to close up."

    show seb sad at right with dissolve

    s "Not that anyone notices. It's always so quiet ‘round here."
    r "Oh."

    "Well… I don't think Seb is the summoner. But I suppose we should make a suspect file for him. Just to be thorough and prove that he {i}didn't{/i} do it."

    show ron neutral at center with dissolve

    r "Well I guess I need to talk to you anyway."

    show seb smile at right with dissolve

    s "'{i}Need{/i} to'?"

    show ron blushing at center with dissolve

    r "Uh… you know… for- for the investigation."
    s "I see."

    "Focus! Focus, man!"

    show ron awkward at center with dissolve

    r "Okay, first question, um… well, uh, there's been some disagreement about the order of these… dangerous attacks. That were done by… people."

    show seb confused at right with dissolve

    s "Uh… yes… yes, that's what I thought…"

    "So smooth, Ron."

    r "You have any idea of the order?"

    show seb awkward at right with dissolve

    s "I'm afraid not. I haven't paid much attention. And things have been kept under pretty tight wraps."

    show ron thoughtful at center with dissolve

    r "Not even the day the library was attacked? 'Cos Mrs. Pear said it was Thursday, the sheriff said it was Friday, and the mayor said it was Saturday."
    s "Ah. Well, I don't know about Friday or Saturday, but I'm sure it wasn’t Thursday."

    show ron curious at center with dissolve

    r "Really?"

    show seb sad at right with dissolve

    s "Poor old Mrs. Pear had a bit of a funny turn Thursday, so I sent her home, said I'd lock up. I ended up staying late, 'till about midnight, alone in the library, grading papers. If I'm here, I don’t have to spend money on lights and the aircon in my apartment."

    # Fill in section 1.1 of Seb's suspect file

    show ron thoughtful at center with dissolve

    r "So I wonder why she said it was Thursday."
    s "She's not as young as she used to be, especially recently. Think her mind is going a bit."

    "So it looks like the library was {i}not{/i} attacked on Thursday. Good to know. Now I need to ask the questions for the form. It's long, though. I probably can't ask {i}all{/i} the questions, maybe one from each section. What should I ask?"

    menu:
        "What about Friday? Where were you Friday night?":
            # Fill in section 1.2 of Seb's suspect file
            jump d1s11ao1

        "Well then, what can you tell me about Saturday night?":
            # Fill in section 1.3 of Seb's suspect file
            jump d1s11ao2

label d1s11ao1:
    show seb neutral at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    r "What about Friday? Where were you Friday night?"

    show seb thoughtful at right with dissolve

    s "Uh, Friday, let me think… There's this new coffee shop near my flat. It's open late. I went there to check it out."
    r "Where is it?"
    s "Maple Street. Not far from my family's restaurant."
    r "Did you go with anyone?"

    show seb awkward at right with dissolve

    s "No."
    r "Okay. Any idea if the place has CCTV?"

    show seb thoughtful at right with dissolve

    s "I doubt it. Place looked pretty new but not entirely finished and not that well-funded. But I don't know."
    r "Okay then. Thanks."

    jump d1s11ac1

label d1s11ao2:
    show seb neutral at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    r "Well then, what can you tell me about Saturday night?"

    show seb thoughtful at right with dissolve

    s "Saturday—yesterday. Stayed home all day, graded some exams."
    r "Alone?"
    s "Uh huh."
    r "Do you have any security footage in or around your place?"
    s "Nope."
    r "Okay, thank you."

    jump d1s11ac1

label d1s11ac1:
    show seb neutral at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    "Okay, that's one alibi got. Let's ask him about another suspect. But which one?"

    menu:
        "So, you've got a pretty good friendship with Mrs. Pear, right?":
            # Fill in section 2.4.1 of Seb's suspect file and 2.5.2 section of Mrs. Pear’s.
            jump d1s11ac2o1

        "You remember Terry, right? He's the sheriff now, as I'm sure you know. What do you think of him?":
            # Fill in section 2.3.1 of Seb's suspect file and 2.X.2 section of Terry’s.
            jump d1s11ac2o2

        "You ever see Danny's ma', Emily, around?":
            # Fill in section 2.1.1 of Seb's suspect file and 2.1.2 section of Emily's
            jump d1s11ac2o3

        "You ever met Norman Conlee? The mayor's secretary—well, ex-secretary.":
            # Fill in section 2.2.1 of Seb's suspect file and 2.2.2 section of Norman’s.
            jump d1s11ac2o4

label d1s11ac2o1:
    show seb neutral at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    r "So, you've got a pretty good friendship with Mrs. Pear, right?"

    show seb smile at right with dissolve

    s "Yeah, she's really nice. She must be ancient to be honest. But she keeps going, and thank God she does. Besides the mayor and me, she's the only one who cares about the library. Without Mrs. Pear, it would be closed."
    r "If you could sum up your relationship with her in one sentence, what would it be?"

    show seb thoughtful at right with dissolve

    s "We’re friends, and I have a lot of respect for her, but I also try to look out for her."
    r "Great, thanks."

    jump d1s11ac3

label d1s11ac2o2:
    show seb neutral at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    r "You remember Terry, right? He's the sheriff now, as I'm sure you know. What do you think of him?"

    show seb moody at right with dissolve

    s "Yeah, I remember the jerk. Hard to forget him. Especially now that he's got that darned job. I mean, I do my best to avoid the law ’round here in general, but him especially. Haven't had anything much to do with them."
    s "But from what I've heard, he's a pretty rubbish sheriff."
    r "If you could sum up your relationship with him in one sentence, what would it be?"

    show seb thoughtful at right with dissolve

    s "I try to avoid him, and I don't think much of him."
    r "Cool, thank you."

    jump d1s11ac3

label d1s11ac2o3:
    show seb neutral at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    r "You ever see Danny's ma', Emily, around?"
    s "Yeah, sometimes. She comes into the library now and then—probably the most frequent visitor after myself. I know she wants to renovate it; she’s asked me for my ideas."
    s "She also gave more funding to the school, and because of her, they started new clubs, which the principal has all made my responsibility. We’ve now got a creative writing club and a GSA, along with a few others."

    "Oh yeah, I read about that in the newspaper column."

    s "She's pretty nice compared to some of the folks around here. A few months back, some of the parents and my colleagues at the school wanted to get me fired. Something about 'the gay half-elf corrupting their kids.'"
    s "The principal was happy to do it. He's very much a 'do anything to keep the peace' type. But the mayor heard about it and stepped in. Said she'd get him removed if he listened to those idiots."
    s "I think this was more of her sticking to her morals and not screwing up her image than helping me out specifically, but still. We're not exactly friends, but she looks out for me. She really tries to make the town better in general."
    s "So I like her—in a distant kinda way."
    r "Can you sum up your relationship with her in one sentence?"

    show seb thoughtful at right with dissolve

    s "She's a vague friend who I think is a good person, and I owe her one."
    r "That's perfect, thank you."

    jump d1s11ac3

label d1s11ac2o4:
    show seb neutral at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    r "You ever met Norman Conlee? The mayor's secretary—well, ex-secretary."

    show seb awkward at right with dissolve

    s "Yeah, kinda. I mean, it's a small town. People know people around here. And he's got a reputation for being a cantankerous crap-head. And sometimes, if he's had too much to drink and sees me going by, he makes his opinion on elves and half-elves {i}very{/i} clear."
    r "Could you sum up how you feel about him in one sentence?"

    show seb thoughtful at right with dissolve

    s "We don’t like each other; I avoid him."
    r "Cool, thank you."

    jump d1s11ac3

label d1s11ac3:
    show seb neutral at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    "Okay, great. I think the last thing to ask about is the last time he was at the various crime scenes."

    r "Okay, one last set of questions."
    s "Sure—hit me with 'em."

    menu:
        "When was the last time you were at the library before the attack? Was it Thursday? You mentioned that earlier.":
            # Fill in section 3.1 of Seb's suspect file.
            jump d1s11ac4o1

        "When was the last time you were in or near the mayor's office?":
            # Fill in section 3.2 of Seb's suspect file.
            jump d1s11ac4o2

        "When was the last time you were in or near the sheriff's office?":
            # Fill in section 3.3 of Seb's suspect file.
            jump d1s11ac4o3

label d1s11ac4o1:
    show seb neutral at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    r "When was the last time you were at the library before the attack? Was it Thursday? You mentioned that earlier."

    show seb thoughtful at right with dissolve

    s "Umm, no. It would have been Friday. Just after school. Needed to return a book."
    r "What time would this have been, then?"
    s "School ends at 3, and it takes me about half an hour to get organized and get out of there. But the library is right next door. So, I guess it would have been approximately 3:35."
    r "Anything happen while you were there?"
    s "Mrs. Pear was busy, so I went behind her desk to scan through the book’s return myself, shelved it, went to chat with her, then left for my parent's restaurant to help prepare for dinner."
    r "And before you left, did anything odd happen?"

    show seb sad at right with dissolve

    s "Yeah, Mrs. Pear was having one of her funny turns. She was in the occult section. I think she was meant to be checking stock and comparing it to what we’re supposed to have."

    "The occult section—that's the section that was attacked."

    s "But she was muttering to herself kinda frantically. Cursing about every missing book. And when she saw me, she demanded to know if I'd been doing magic. I hadn't, of course. But it was like she didn't even know who I was."
    s "I made her a cup of sweet tea and got her to calm down eventually. Convinced her to close early and go rest. Then I left as she was getting ready to go."

    show ron sad at center with dissolve

    r "Oh no. Poor Mrs. Pear. Has she ever done anything else like this?"

    show seb awkward at right with dissolve

    s "She gets a bit paranoid about things. Sees monsters in every shadow."

    show ron thoughtful at center with dissolve

    r "I see… That's useful to know. Thank you for telling me."

    jump d1s11ac5

label d1s11ac4o2:
    show seb neutral at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    r "When was the last time you were in or near the mayor's office?"

    show seb thoughtful at right with dissolve

    s "The mayor’s office, huh? I think that would have been… Wednesday. So, four days ago."

    show ron thoughtful at center with dissolve

    r "So the day before the first attack?"
    s "Yeah. Emily asked for a meeting—she'd asked me to report on how the clubs she's funding for the school are doing. We were meant to meet up Thursday, because I was helping at my dad's restaurant after work on Wednesday."
    s "But then at lunch on Wednesday, she called me and said she was going to end up working late today, so asked if I'd mind coming to talk to her when we closed the restaurant. I said sure."
    r "And what time was this?"
    s "Ten o'clock."

    "Ah, there was a meeting in the mayor's diary on Wednesday at 10 with 'S.' It must have been Seb."

    show ron neutral at center with dissolve

    r "So what happened?"
    s "She forgot about it, apparently—I ran into her outside. Think she was just heading back into the office. We were both pretty tired, so we just had a quick talk. Then Danny arrived to see her, so I left them to it and headed home."
    r "I see. So besides meeting outside, was there anything odd happening? With her, with the building, or in the area?"
    s "Hmm… Emily seemed a bit distracted. Happy distracted—like she'd just had some good news. But when I asked, she said it was nothing and she'd just seen some 'funny karma.' I didn't wanna pry."
    r "Nothing else odd?"
    s "Nope."
    r "Alright."

    jump d1s11ac5

label d1s11ac4o3:
    show seb neutral at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    r "When was the last time you were in or near the sheriff's office?"

    show seb thoughtful at right with dissolve

    s "The sheriff’s office, hm? Let me think… probably Tuesday. Last Tuesday—the seventh."
    r "Why were you there?"

    show seb awkward at right with dissolve

    s "Uh… I was… I was reporting a crime, I think."

    show ron confused at center with dissolve

    r "You {i}think{/i}?"

    show seb confused at right with dissolve

    s "I don't remember. It was a while ago."
    r "It was last week!"
    s "It was a busy week."

    "What the hell?"

    r "What were you reporting?"
    s "I dunno—I guess it wasn't that important."

    "… Okay. Let's see if he can answer any questions for the file."

    show ron curious at center with dissolve

    r "What time was this?"
    s "7:30, I think. Around then. Before school. I went in, talked to someone—can't remember who—then left."

    show ron worried at center with dissolve

    r "You haven't hit your head or anything, have you?"
    s "No, no. Nothing like that."
    r "Hmm. Did you notice anything odd?"

    show seb thoughtful at right with dissolve

    "Seb pauses for a second, looking like he's thinking hard."

    s "I think… I think I heard arguing. Pretty sure it was Terry and… someone. Not sure who, it was in another room."

    "So he remembers some overheard yelling, but not what he was reporting to the cops?"

    r "Did you hear what they were arguing about?"
    s "No, it was all muffled through the walls, so I didn't really hear many individual words… I mean there were one or two, I think. Pretty sure I heard the word 'snooping' from Terry. Then I think whoever he was arguing with called him 'unfit.'"

    "He remembers all that, but not why he was there? What the hell?"

    r "Do you go there often?"
    s "Oh God no. I try to avoid it when I can. Not a fan of walking into Terry's lair."
    r "Well, uh… okay."

    jump d1s11ac5

label d1s11ac5:
    show seb neutral at right with dissolve
    show marley neutral at left with dissolve
    show ron neutral at center with dissolve

    r "Thank you for the information. It'll all be very useful."

    show seb smile at right with dissolve

    s "I'm glad I could help! Good luck finding the vandals."
    r "Thanks."

    "I give him an awkward smile. Gosh, he's mighty fine to look at."
    "But I don't have time to gawk at his face all day."

    show ron serious at center with dissolve

    r "Eh hem. Thank you for your time. We've got to get going."
    s "I understand. I guess I'll, uh… see you round, Ron."

    show ron blushing at center with dissolve

    r "Not- not if I s-see you first."
    s "Hehe."

    show seb smile at offscreenright with move
    show ron blushing at right with move
    show marley laughing at left with dissolve

    m "{i}*Giggles*{/i}"

    show ron moody at right with dissolve

    r "Don't."
    m "Was… was that {i}flirting{/i}, Ron? With that hot half-elf guy? Because it was painful to watch."
    r "Ugh. Come on."
    m "Well, some things in this case are starting to make sense."

    jump d1s10_map