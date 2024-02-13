# Mrs. Pear or Emily?
label d1s11b:
    show pear worried at centerright with dissolve
    show emily smile at center with dissolve
    show ron neutral at centerleft with dissolve

    "As we approach the open door of the mayor's office, we hear Emily chatting with a familiar voice."

    l "I just don't want you to get hurt again."
    e "Oh, you worry too much, Sandra. I'm not dating the man. Just going on... business dinners."
    l "Listen hon', if this is about them library renovations, just let it go! I'm quite happy with it the way it is, and I'm sure the visitors are too."

    show emily neutral at center with dissolve

    e "What visitors?! No one ever goes there except a handful of moms with their kids and Marianna's son!"

    show pear serious at centerleft with dissolve

    l "Well, exactly—don't go wasting money on somethin' the community don't never use!"

    show emily moody at center with dissolve

    e "Don't you think that maybe the reason the community don't use it is 'cause of the {i}building{/i}? As in, the main thing I want renovated?"
    l "Don't be silly—"
    e "There haven't been any renovations to the structure since it was built! It's as old as the town!"
    l "Oh come now—"
    e "It has no aircon, a leaky roof, and the plumbing spends more time blocked than unblocked!"

    show emily worried at center with dissolve

    e "Come on Sandra, stop your frettin' about me! I can deal with Mr. high-an'-mighty. I'm determined to make this town {i}better{/i} than it was when I came into office."
    e "And I'm gonna do that by fixin' up the library, no matter how many times he an' his council get in my way!"

    # TODO: SFX- Two steps of footsteps

    show marley neutral at centerleft with dissolve
    show ron neutral at centerleft with dissolve
    show emily surprised at center with dissolve

    e "Oh, Ron! Miss Marley! I didn't see you there!"

    show emily neutral at center with dissolve

    r "Good afternoon, ladies."
    e "How can we help you?"
    r "Well actually, I was wondering if I could have a word with..."

    "Oh crap, I don't have time to interview both of them. I need to pick one to talk to—but which?"

    menu:
        "Emily. With the drama between her and that assistant of hers we saw, I'm sure she's got some interesting secrets up her sleeve.":
            jump d1s11b_emily

        "Mrs. Pear. There's something about the library attack that feels off to me.":
            jump d1s11b_pear

label d1s11b_emily:
    show pear neutral at centerright with dissolve
    show emily neutral at center with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at centerleft with dissolve

    r "... Emily."
    l "Well I'll leave y'all to it. I need to head off anyway—got things to do."
    e "Okay, Sandra. Take care."

    show pear neutral at offscreenright with move
    show emily smile at centerright with move
    show ron neutral at center with move

    e "So, what can I do for you two?"
    r "I was wondering if I could ask you some questions?"
    e "Sure, go ahead."

    "Okay, I want to find out where she was at each time of attack, but there seems to be some confusion about which day the mayor's office was hit. She said it was Friday, but Mrs. Pear and Terry disagreed."
    "Maybe I should ask about Saturday—her diary didn't have much to say about that day, and that's when Mrs. Pear said the mayor's office was struck."

    r "What were you doing Saturday, during the attack?"
    e "Working late, as usual. I'd met with Terry earlier that day to discuss rising crime rates, but that idiot was no help. So, I was trying to come up with a proposal to tackle the problem."
    e "But coming up with a solution that pleases our old-fashioned town council, involves Terry as little as possible, and actually works seems pretty much impossible. I worked until about ten, but I didn't have much luck."
    r "I see."

    "Mrs. Pear had said that the mayor's office was attacked Saturday. But if Emily's telling the truth, it couldn't have been..."

    r "Thank you, Mayor Sawyer. Was anyone with you during this time? Your assistant? Or... ex-assistant?"

    show emily curious at centerright with dissolve

    e "Oh wait wait wait— You're trying to get my {i}alibi{/i}, aren't you?"

    show ron awkward at center with dissolve

    r "Uh... yes. I apologize ma'am, but it's protocol—"

    show emily smile at centerright with dissolve

    e "Oh good Lord, that's so exciting! I've never been asked to give an alibi before! This is so fun!"

    show ron confused at center with dissolve

    r "Uh..."

    "You know that was absolutely not the reaction I was expecting. Not a reaction I've ever seen before."

    if visited_d1s11c_norman:
        "It seems like everyone is happy I'm investigating the mayor. Including the mayor herself. Norman only cooperated when I said she was a suspect... but I don't think he realized she'd be so excited about it..."

    e "Oh it's just like a {i}real{/i} investigation!"
    r "Ma'am... this {i}is{/i} a real investigation."
    e "THIS IS SO COOL!"
    r "..."

    show ron serious at center with dissolve

    r "And do you actually have an alibi?"

    show emily awkward at centerright with dissolve

    e "Oh, uh... no. No, I don't."

    show emily moody at centerright with dissolve

    e "I worked alone that night—Norman never worked a full shift in his entire career here, let alone worked late."

    show ron neutral at center with dissolve
    show emily neutral at centerright with dissolve

    r "I see. Okay, next question—"

    "I want to get a sense of the different relationships she has with the people of the town, but I don't have time to do this all at once. Who should I ask about?"

    menu:
        "Do you remember Seb Daley? He went to school with me and Danny.":
            # Fill in section 2.1.1 of Emily's suspect file and 2.1.2 section of Seb's.
            jump d1s11b_emily_o1

        "You and your ex-assistant seem to have some pretty bad blood. Could you tell us a bit about that?":
            # Fill in section 2.2.1 of Emily's suspect file and 2.1.2 section of Norman's.
            jump d1s11b_emily_o2

        "You mentioned earlier that you met with Terry recently. I get the sense that there ain't love lost between the two of you?":
            # Fill in section 2.3.1 of Emily's suspect file and ___ section of Terry's.
            jump d1s11b_emily_o3

        "So you and Mrs. Pear seem to be on good terms, is that right?":
            # Fill in section 2.4.1 of Emily's suspect file and 2.1.2 section of Mrs. Pear's.
            jump d1s11b_emily_o4

        "You and Danny are still pretty close, huh?":
            # Fill in section 2.5.1 of Emily's suspect file and 2.1.2 section of Danny's.
            jump d1s11b_emily_o5

label d1s11b_emily_o1:
    show emily neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "Do you remember Seb Daley? He went to school with me and Danny."
    e "Sure, I know Seb. I used to be good friends with his ma'. A real nice woman. And Seb—well, he's done her proud."
    r "So you're friends with him?"
    e "In a vague sorta way. I see him at the library a lot. He helps out Mrs. Pear, which is mighty good of him. Kingston could do with more folk like him."

    show ron curious at center with dissolve

    r "'Like him' as in with a similar personality or as in not entirely human?"

    show emily smile at centerright with dissolve

    e "Both! Diversity always makes a community stronger."

    show ron thoughtful at center with dissolve

    r "If you could describe your relationship with Seb in one sentence, what would it be?"

    show emily thoughtful at centerright with dissolve

    e "I guess I'd say, 'He's a friend an' a mighty fine citizen of Kingston.'"

    show ron neutral at center with dissolve

    r "That's perfect."

    jump d1s11b_emily_c1

label d1s11b_emily_o2:
    show emily neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "You and your ex-assistant seem to have some pretty bad blood. Could you tell us a bit about that?"

    show emily moody at centerright with dissolve

    e "Ugh. Norman. He's a rude, self-centered, and never up to any good."

    show ron thoughtful at center with dissolve

    r "So why'd he work for you so long? I mean, I heard he got the job as a favor to his dad, but Norman seems like he was actively making life difficult for you."

    show emily awkward at centerright with dissolve

    e "Well, uh...honestly, the whole 'Norman' situation was a rather... complex affair. Politics usually ends up that way."
    r "I see..."

    "I do not see. If it's so 'complex,' why is she free to fire him now? Maybe she isn't, but has finally been pushed far enough to say, 'damn the consequences'?"

    show ron neutral at center with dissolve

    r "I wonder if you could sum up your relationship and how you feel about him in one sentence?"

    show emily moody at centerright with dissolve

    e "I'd say 'hated ex- colleague' does the job quite nicely."
    r "Then that's what we'll put down."

    jump d1s11b_emily_c1

label d1s11b_emily_o3:
    show emily neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "You mentioned earlier that you met with Terry recently. I get the sense that there ain't love lost between the two of you?"

    show emily moody at centerright with dissolve

    e "Humph. Terry. What did I ever do to deserve a moron like that for a sheriff?"
    r "You ain't a fan of his then?"
    e "No. It's ridiculous he ever got that job in the first place. An' I still remember what he was like in school with you and Danny when y'all were youngins. I don't figure he's changed much."
    r "But as mayor, you've gotta work with him? That must be hard."
    e "Ain't it just. He doesn't do real work, he doesn't care about people, he's rude—all in all, he's a pain in my ass."

    show ron thoughtful at center with dissolve

    r "Then how'd he get the job—is it an elected position?"
    e "No, most of the sheriff gigs in other towns around here are, but 'cos Kingston's a lot older than the other towns in the area, it's got this special founding document that lays out certain legislation."
    e "The front page of it is on display in the town hall, but the whole thing is pretty important."
    r "Yeah, I remember doing a semester on that in high school—we all had to learn a passage of it off by heart."

    show emily smile at centerright with dissolve

    e "Oh, that brings back memories."

    show ron awkward at center with dissolve

    r "I'm afraid I wasn't the best student in that class."
    e "Well, to give you a reminder—in the original founding document, it states that a mayoral election is held every five years and a mayor can run for re-election as many times as they want. The same is true for the town council."

    show emily serious at centerright with dissolve

    e "But the sheriff is selected by the council. And although we're a part of Texas, the citizens chose to go by the original laws, not those of the state."

    show ron thoughtful at center with dissolve

    r "So the town council picked Terry. But why?"

    "Emily shrugs."

    e "Madduxes."
    r "Hm. Well, if you could describe your relationship with and feelings towards Terry in one sentence, what would it be?"

    show emily moody at centerright with dissolve

    e "An egotistical, misogynistic, rude pain in my ass."

    show ron thoughtful at center with dissolve

    r "I don't think I can disagree with any of that."

    jump d1s11b_emily_c1

label d1s11b_emily_o4:
    show emily neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "So you and Mrs. Pear seem to be on good terms, is that right?"

    show emily smile at centerright with dissolve

    e "Oh yes, Sandra. She and I go way back—I knew her when I was a kid."
    r "Yeah, I remember her working at the library when I was young. I'm amazed she's still with us."
    e "Oh she's a tough old bird. Honestly, she's helped keep me sane through all this."

    show ron thoughtful at center with dissolve

    r "If you could sum up your relationship and feelings towards her in one sentence, what would it be?"

    show emily thoughtful at centerright with dissolve

    e "She's a good friend and a good woman."
    r "I see."

    jump d1s11b_emily_c1

label d1s11b_emily_o5:
    show emily neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "You and Danny are still pretty close, huh?"

    show emily smile at centerright with dissolve

    e "Oh yes, I'm very close with my little Danny-boo."

    show marley laughing at centerleft with dissolve

    e "Before we moved back here, when we were in Austen, poor Danny didn't make many friends. He was a very shy boy. So he and I, we were all each other had. We got real close and have been ever since."

    show marley neutral at centerleft with dissolve

    r "If you could sum up your relationship with Danny in one sentence, what would it be?"
    e "The best son a woman could ask for."

    show ron smile at center with dissolve

    r "Well that's real sweet, Ms. Sawyer."

    jump d1s11b_emily_c1

label d1s11b_emily_c1:
    show emily neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "Thank you. Now, I've got one last set of questions for you, Emily."
    e "Sure, go ahead."

    "Now, this is the part where I ask about the last time she was at one of the crime scenes before it was attacked. But one of the crime scenes was here, and she's here every day, so her answer would depend on which day it was attacked."
    "And there's some confusion about that. I'll ask about one of the others."

    menu:
        "So the sheriff's office was one of the places that was attacked, right? When was the last time you were there? Before the attack I mean.":
            # Fill in section 3.1 of Emily's suspect file
            jump d1s11b_emily_c2o1

        "Do you visit the library often, Mayor Sawyer?":
            # Fill in section 3.2 of Emily's suspect file
            jump d1s11b_emily_c2o2

label d1s11b_emily_c2o1:
    show emily neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "So the sheriff's office was one of the places that was attacked, right? When was the last time you were there? Before the attack I mean."

    show emily thoughtful at centerright with dissolve

    e "The sheriff's office... Honestly, I'm not in the habit of heading over there. I haven't had to report any crimes recently. And I ain't fond of socializing with Terry and his crew."

    "Didn't have a crime to report? What about that memo about money going missing from the treasury? Hasn't that been reported to the cops? That's odd..."
    "But I can't ask about that—I found it by snooping."

    show ron awkward at center with dissolve

    r "You, uh... you haven't had any criminal issues around here?"
    e "No, not really. I suppose the last time I was there was... Tuesday, actually, but only briefly."

    show ron thoughtful at center with dissolve

    r "Oh yeah? And what time was this?"
    e "12:30. I was asked to come in for a meeting with the deputy—Derek—but he cancelled at the last minute. I didn't see that before I left, though. So, I more or less got there, got told it was cancelled, and turned straight around."

    show ron curious at center with dissolve

    r "Do you know what the meeting was meant to be about?"

    show emily thoughtful at centerright with dissolve

    e "No, he never said, but he did say it was urgent. I figured maybe it was about how crime rates have been going up around here? That whole department knows I've been trying to crack down on it."
    e "I'm surprised he didn't reschedule the meeting. He was very cagey about it when I saw him—said that he {i}might{/i} reschedule, that he'd get back to me at some point after Thursday."
    r "I see. Besides that, did you notice anything odd?"
    e "I saw Terry there. He seemed pretty moody. He and Derek were snappish with each other."

    "Hm. Terry and Derek really ain't on good terms."

    jump d1s11b_emily_c3

label d1s11b_emily_c2o2:
    show emily neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "Do you visit the library often, Mayor Sawyer?"
    e "The library? Yeah, sure, all the time."

    show emily laughing at centerright with dissolve

    e "Well, uh, when I'm not at the office."

    show emily serious at centerright with dissolve

    e "I'll be frank with you, Ron, I am a very determined woman. I set myself a goal. I achieve that goal. I did it when I got my degree. I did it when I decided to raise Danny on my own. I did it when I got elected."

    "Well, you can't say she doesn't follow through."

    e "And when I got this position, my goal became to make Kingston better. I want to focus on academics and culture. Improve the schools, increase funds and resources for the museum, improve the library."
    e "And, of course, now I have to focus on the rising crime rates, thanks to Terry doin' a pits-poor job."
    e "I've finished working on the school. The museum has the resources it needs and my Danny-boo is making sure its development is going smoothly. And I'll deal with Terry... somehow."
    e "But right now, I need to fix up the library. It's a key community resource. And that building—it's ancient. It's as old as the town! It started out as the manor house of one of the founding families, the Halls."
    e "The only building as old is Kingston High—that used to be the Madduxes' place. But that building has been renovated a bunch. The library, not so much. We need to bring it into the present. Need to show people its potential."
    e "It's going to happen. It needs to happen. No matter how many obstacles the darned town council puts in my way."
    e "So I've been drawing up plans for its renovation. That's mainly why I spend time there. That and... I like the calm. The solitude. Ironic, since that's what I'm trying to change. But yeah, I go there when I can."

    "She seems pretty passionate about this. I guess she really is serious about her goals."

    show ron thoughtful at center with dissolve

    r "So when was the last time you went to the library? Before the attack there, I mean."

    show emily thoughtful at centerright with dissolve

    e "That would have been... Thursday. Right before my meeting—"

    show emily awkward at centerright with dissolve

    e "I mean, uh—"

    show emily neutral at centerright with dissolve

    e "Right before I headed home for the day. Seb was there, but no Mrs. Pear. It was her I'd wanted to talk to, so I just said hi to Seb, looked around to check something for my plans, then left."
    r "And what time would that have been?"

    show emily thoughtful at centerright with dissolve

    e "Just before it closed, so... 6:50? It stays open real late."
    r "And did you notice anything odd while you were there?"

    show emily thoughtful at centerright with dissolve

    e "I guess, uh... Seb... he seemed distracted. Zoned out. I thought maybe he'd just taken some pain killers or something. But when I asked if he was okay, he sort of blinked a bunch, then seemed to come back to himself."

    show ron worried at center with dissolve

    r "I see... I hope he's okay."

label d1s11b_emily_c3:
    show emily neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "Well, thank you for your time, Mayor Sawyer. You've been very helpful to our investigation."

    show emily smile at centerright with dissolve

    e "Well, I'm always happy to help! This is all mighty exciting!"
    r "We'll let you get on with your work. We know you're very busy. I'll see you around."

    scene black with fade

    jump d1s10_map

# ===============================================================================================

label d1s11b_pear:
    show pear neutral at centerright with dissolve
    show emily neutral at center with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at centerleft with dissolve

    r "... Mrs. Pear."
    l "Of course, dearies. I'd be happy to help."
    e "I was thinking of going on a walk to clear my head. You're welcome to use my office if it's privacy you want."

    show ron smile at centerleft with dissolve

    r "Thank you, Mayor Sawyer. That'll be mighty useful."

    show emily neutral at offscreenright with move
    show ron smile at center with move
    show pear smile at centerright with dissolve

    l "Now, how can I help you two? Oh, this must be about the ghoul attacks y'all are investigating, right?"
    r "Indeed it is, ma'am. I wanted to ask you what you were doing on..."

    "Now, she said the attack on the library was Thursday. But Terry said it was Friday. And Emily said it was Saturday. And Mrs. Pear's mighty old, she could easily get confused."
    "Let's see if Mrs. Pear can remember what happened Saturday—the day Emily said the library was attacked."

    r "...Saturday."

    show pear thoughtful at centerright with dissolve

    l "Saturday—you mean yesterday? Now let me think... well, I was at the library till it closed at seven. Then I... yes—I stayed late that day."

    show ron curious at center with dissolve

    r "Oh yeah?"
    l "Yep. The ghouls had made such a mess two days before, that I was still working on cleaning it up. Left at... maybe ten?"

    "Hmm... Emily had said that the library was attacked Saturday. But if Mrs. Pear was working late that day... then it couldn't have been..."

    r "Was anyone else there?"
    l "Afraid not, dearie. We're very understaffed at the moment—only me working there."

    # Fill in section 1.3 of Mrs. Pear's suspect file.

    show ron neutral at center with dissolve

    r "Okay Mrs. Pear, next I'm going to ask about your relationship with..."

    "Hmm. Who should I ask about?"

    menu:
        "... Emily. Are you two close?":
            # Fill in section 2.1.1 of Mrs. Pear's suspect file and 2.4.2 section of Emily's.
            jump d1s11b_pear_o1

        "... Terry. He's the new sheriff. Have you had any dealings with him?":
            # Fill in section 2.3.1 of Mrs. Pear's suspect file and __ section of Terry's.
            jump d1s11b_pear_o2

        "... Norman, Emily's old secretary. Did you ever meet him?":
            # Fill in section 2.2.1 of Mrs. Pear's suspect file and 2.4.2 section of Norman's.
            jump d1s11b_pear_o3

        "... Seb. Does he regularly read at the library?":
            # Fill in section 2.5.1 of Mrs. Pear's suspect file and 2.4.1 section of Seb's.
            jump d1s11b_pear_o4

        "... Danny. Emily's kid. If you know Emily quite well, do you know him too?":
            # Fill in section 2.4.1 of Mrs. Pear's suspect file and 2.4.2 section of Danny's.
            jump d1s11b_pear_o5

label d1s11b_pear_o1:
    show pear neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "... Emily. Are you two close?"
    l "Oh yes, Emily's a mighty fine woman. And I can't complain about her work as mayor. She's got new blood that the town needs."
    r "I understand she's pretty controversial—I saw that column about her in the newspaper today."
    l "Well, some folk around these parts can be very stuck in their ways. Don't like her pro-LBGT stance, how she's changin' up the school, and how she got Kingston's woods declared a protected space."
    l "But others think she's taking steps in the right direction. To be honest, a lot of folks were plumb tired of the way the place used to run."

    show ron thoughtful at center with dissolve

    r "But still... she's been mayor for how long?"

    show pear thoughtful at centerright with dissolve

    l "Well she was elected in 2008, so... fourteen years."
    r "So that's three elections she's won. For such a controversial politician, that's amazing!"

    show pear neutral at centerright with dissolve

    l "I don't think she's as controversial as she seems. The people who ain't fond of her ain't afraid to make it know—they always cause a ruckus. The people that like her tend to stay quiet."
    l "So it seems like more hate than like her, but I reckon it's the other way 'round. Anyway, I'm mighty fond of her. She reminds me of myself at her age—strong willed. Determined."

    show ron neutral at center with dissolve

    r "If you could describe your relationship with her in one sentence, what would it be?"

    show pear thoughtful at centerright with dissolve

    l "She's a good person who I try my best to help when I can."
    r "That'll do nicely."

    jump d1s11b_pear_c1

label d1s11b_pear_o2:
    show pear neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "... Terry. He's the new sheriff. Have you had any dealings with him?"

    show pear moody at centerright with dissolve

    l "Idiot boy. Those darned Madduxes are a curse on this town, and Terry's no different! Only one worse is his father."

    show ron thoughtful at center with dissolve

    r "So you ain't a fan of the sheriff?"
    l "No, I am most certainly not! And he don't deserve that badge of his. He's a disgrace to this town."
    r "Do you see him around much? Talk to him ever?"
    l "Sure—I've had some things I've tried to report to him in the past, but he won't listen. Thinks I'm crazy!"

    show ron curious at center with dissolve

    r "You've been reporting things to him? What kind of things?"

    show pear awkward at centerright with dissolve

    l "I... I don't wanna say."

    show ron confused at centerright with dissolve

    r "What? Why not?"
    l "You'll think I'm crazy too, just like everyone else around here."

    "Well that sounds important!"

    r "I swear I won't, Mrs. Pear. I'll take anything you tell me very seriously."
    l "Well... sometimes... sometimes I {i}hear{/i} things. At night. {i}Howls{/i}."
    r "Ain't... ain't this coyote country? They howl—"

    show pear moody at centerright with dissolve

    l "No! No, this is different! You ain't listening!"
    r "Then... then what is it, Mrs. Pear?"
    l "Beasts. Beasts that ain't... ain't {i}natural{/i}."
    r "What do you mean?"

    show pear serious at centerright with dissolve

    l "I mean that young Seb Daley ain't the only not-fully-human individual in these parts!"

    "For God's sake, why is this woman being so cryptic?!"

    l "An' that's all I'm gonna say on the matter."

    show ron moody at center with dissolve

    r "Why? Why won't you explain properly?"
    l "Ain't you a fancy detective man? Detect!"

    show pear neutral at centerright with dissolve

    l "Now, to your actual question—"

    "I grind my teeth in frustration."

    l "I ain't fond of Terry Maddux. He's not my choice of sheriff."
    r "I... I guess I'll put that down."

    jump d1s11b_pear_c1

label d1s11b_pear_o3:
    show pear neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "... Norman, Emily's old secretary. Did you ever meet him?"

    show pear moody at centerright with dissolve

    l "Yeah, I've had the displeasure of meetin' him a few times when I came in to visit Emily. Foul little man."
    r "Yes, he seems like an... interesting fella."
    l "He calls me 'crazy old bat.' He doesn't even have the decency to whisper it, just says it outright. That man should've had his hide tanned more when he was a boy!"

    show ron thoughtful at center with dissolve

    r "Any idea why he got the job? Being the mayor's assistant is a pretty good gig, right? How come {i}he{/i} got it?"

    show pear thoughtful at centerright with dissolve

    l "Lord knows. I suppose... well, the pair of 'em have an interesting history, I guess."

    show ron curious at center with dissolve

    r "Wait, what? What do you mean?"

    show pear awkward at centerright with dissolve

    l "Uh, well, it ain't really my business. I'm not gonna gossip about Emily and her affairs."
    r "But that could be important!"

    show pear serious at centerright with dissolve

    l "I won't talk behind my friend's back. If you wanna know about that, I suggest you ask Emily about it. Now, you wanted to ask about Norman, right?"

    "No! I want to know about the past between Emily and Norman!"
    "But I can tell by the look in her eyes that I ain't gonna get another word out of her on that subject."

    show ron moody at center with dissolve

    r "Fine. Could you sum up your feelings towards Norman in one sentence?"

    show pear moody at centerright with dissolve

    l "As far as I can tell, Norman is a grade-A prick with less use than dog feces."

    show ron thoughtful at center with dissolve

    r "Well that certainly is decisive."

    jump d1s11b_pear_c1

label d1s11b_pear_o4:
    show pear neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "... Seb. Does he regularly read at the library?"

    show pear smile at centerright with dissolve

    l "Ah, Seb. Such a good boy. I really don't know where I'd be without him."

    show marley thoughtful at centerleft with dissolve

    m "I'm surprised you're so fond of him. You made it very clear that you don't like magic, and Seb is a half-elf, a born sorcerer."

    show pear neutral at centerright with dissolve

    l "Well sure, but Seb don't never use his magic. He sees that it's dangerous and steers well clear. Very sensible."

    "She gives Marley a look."

    show pear serious at centerright with dissolve

    l "Some people would do well to follow his example."

    show marley moody at centerleft with dissolve

    m "Uh huh."

    "Marley doesn't look impressed at Mrs. Pears passive aggressive digs."

    show ron serious at center with dissolve

    r "I know that he, Danny, an' me visited the library a bunch when we were young. I'm guessing he just... never stopped coming?"

    show pear neutral at centerright with dissolve

    l "Uh huh. Then he became an official library volunteer—the only one that the library has. He comes by after school, before his pa's restaurant opens up."

    show ron thoughtful at center with dissolve

    r "Keeps himself busy, don't he?"
    l "Idle hands do the devil's work, Mr. Kitzinger."

    show ron confused at center with dissolve

    r "Uh... they... they sure do..."

    show ron serious at center with dissolve

    r "Would you sum up your feelings towards Seb in one sentence, please?"
    l "He's a kind boy and he helps this old bat out quite a lot."
    r "Alrighty then."

    jump d1s11b_pear_c1

label d1s11b_pear_o5:
    show pear neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "... Danny. Emily's kid. If you know Emily quite well, do you know him too?"

    show pear thoughtful at centerright with dissolve

    l "Danny..."
    m "Yeah. Danny. Light skin, dark hair, green eyes. Annoying little blockhead."

    show ron moody at center with dissolve

    r "Marley!"

    show pear neutral at centerright with dissolve

    l "Oh, I know who he is. Emily yaps on about her precious baby boy whenever she gets the chance. But I don't really interact with him much myself. Before today, when he came by with you, the last time I really spoke to him was when he was a boy."
    l "Back when you, him, and Seb came to the library every day after school so you could avoid your folks."

    show ron awkward at center with dissolve
    show marley curious at centerleft with dissolve

    r "Wha- I, uh... I don't, uh..."

    show pear serious at centerright with dissolve

    l "I might be old, but I ain't stupid, Ron. I know you didn't get on with your folks. So you spent as much time away from there as you could. And Seb and Mr. Sawyer stayed with you to keep you company."
    r "..."

    show ron serious at center with dissolve

    r "Could you please describe your relationship with Danny in one sentence?"

    show pear thoughtful at centerright with dissolve

    l "He's the son of a friend. Nothing more."
    r "Alrighty then."

    jump d1s11b_pear_c1

label d1s11b_pear_c1:
    show pear neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "Thank you for that, Mrs. Pear. You've been very helpful."
    l "I do my best."
    r "I have one last set of questions for you."
    l "Go ahead."

    "I want to know when she was last at each scene. But she's one of the people disagreeing about the order of attacks... so her answer would depend on when she thinks each place was attacked."
    "Maybe I'll ask about either the mayors or the sheriff's office and save questions about the library for after I figure out which day it was attacked."

    menu:
        "So one of the places that was attacked was the sheriff's office. Can I ask when you visited it last?":
            # Fill in section 3.1 of Mrs. Pear's suspect file
            jump d1s11b_pear_c2o1

        "Obviously the ghouls left this place in a bit of a state. When was the last time you visited before it was attacked?":
            # Fill in section 3.2 of Mrs. Pear's suspect file
            jump d1s11b_pear_c2o2

label d1s11b_pear_c2o1:
    show pear neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "So one of the places that was attacked was the sheriff's office. Can I ask when you visited it last?"

    show pear thoughtful at centerright with dissolve

    l "The sheriff's office, huh? Hmm, let me think..."

    show pear neutral at centerright with dissolve

    l "Why I reckon that would have been Tuesday, during my lunch, I had a meeting at 12:30."

    show ron curious at center with dissolve

    r "Why were you there?"
    l "That nice deputy—Derek, I think his name was—he asked me to come in."
    r "Oh? Why?"

    show pear thoughtful at centerright with dissolve

    l "He was doin' some project—something about the town's history. He wanted to ask me a few questions about it."
    r "The town's history?"
    l "Yes. Lord knows what it had to do with his job."
    r "What did he want to know?"

    show pear awkward at centerright with dissolve

    l "Honestly, I can't remember the details. But it got me all confused—I don't think I was any help to him. I left after five minutes."

    show ron thoughtful at center with dissolve

    r "You can't remember any of the questions?"
    l "I'm afraid not. My memory ain't what it used to be."
    r "Well, uh- did you notice anything odd while you were there?"

    show pear thoughtful at centerright with dissolve

    l "Hmm... Terry wasn't there. I thought that was odd, since he was sheriff an' all. And I overheard the folks there talking about him. I don't think they like him much."
    r "Can you remember what people said specifically?"
    l "Well Derek, he- he said that Terry was... dirty. A dirty cop. Hid stuff—I dunno. I didn't really understand it."
    r "I see."

    jump d1s11b_pear_c3

label d1s11b_pear_c2o2:
    show pear neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "Obviously the ghouls left this place in a bit of a state. When was the last time you visited before it was attacked?"

    show pear thoughtful at centerright with dissolve

    l "Uh, let me think... I suppose the last time I visited before the attack would have been... Monday. On my lunch break. I came round here, then Emily and I went to grab lunch."
    r "And when was that?"
    l "Maybe ten past noon?"
    r "And did anything particular happen?"

    show pear thoughtful at centerright with dissolve

    l "I went in, waited a few minutes for Emily to finish what she was doing, then we left."
    r "And did you notice anything odd?"
    l "Well... that creepy assistant of hers—he seemed smug. Pleased with himself. And Emily seemed angry. Snapped at him on the way out."
    r "I see."

    jump d1s11b_pear_c3

label d1s11b_pear_c3:
    show pear neutral at centerright with dissolve
    show marley neutral at centerleft with dissolve
    show ron neutral at center with dissolve

    r "Thank you, Mrs. Pear. This will be very useful."

    # TODO: SFX- Knock knock

    e "Hello? Is it okay for me to come back in?"
    r "Yes, Mayor Sawyer. We're done here."

    # TODO: SFX- Door opens

    show emily smile at center with dissolve

    e "How did it go?"
    r "Good. We've got some interesting stuff."
    e "Oh, I'm so glad! Is there anything else I can do to help?"
    r "Not for now. We've got other things we need to do before nightfall."

    show emily sad at center with dissolve

    e "So you... you don't want to interrogate me, then?"

    "Does... does she look {i}disappointed{/i}?!"

    show ron awkward at center with dissolve

    r "Umm... I'm sure I'll have time to question you at some point, mayor. Now, we need to go. I'll see you around."

    scene black with fade

    jump d1s10_map