label d1s11c_terry:
    show terry neutral at centerright with dissolve
    show norman neutral at right with dissolve
    show ron neutral at centerleft with dissolve
    show marley neutral at left with dissolve

    r "...Terry. Since this is one of the places that was attacked, I need to check a few things with you."

    show terry smile with dissolve

    t "Go ahead, Kitzinger. I knew it would only be a matter of time before you came to the trusty sheriff for help, but I didn't think it would be so soon!"

    show ron serious with dissolve

    r "I'm questioning you as a witness, Terry."

    "'And as a suspect' is what I leave unsaid."

    show terry serious with dissolve
    show norman moody with dissolve

    n "Look, Mr. I-Peaked-in-High School, are you gonna arrest Sawyer or not?"

    show terry moody with dissolve

    t "Still no. And last time I checked, Mr. Conlee, one of us is the sheriff, and the other is a recently unemployed—because he was {i}fired{/i}—personal underling of the mayor. So, I ain't so sure {i}you're{/i} in any position to insult {i}me{/i}."

    show norman angry with dissolve

    n "You only got that job because of your darn pa!"

    show norman moody with dissolve

    n "Ug, whatever. This is a waste of time."

    show norman moody at offscreenleft with move

    show terry moody at right
    show ron serious at center 
    with move

    t "Pfft. Little creep."

    show terry neutral with dissolve
    
    t "Now then, how can I help the two of you?"

    show ron serious with dissolve

    r "Well Terry, it seems like there's some... discrepancies with the witness stories."

    show terry curious with dissolve

    t "Discrepancies? What are you on about?"
    r "It's about the order of when the attacks happened."

    show terry neutral with dissolve

    t "I already told you that! Thursday was the mayor's office, Friday the library, an' Saturday was right here."
    r "Well, other folks are tellin' a different story. There're {i}three{/i} conflicting accounts!"

    show terry moody with dissolve

    t "What 'other folks'?"

    show ron thoughtful with dissolve

    r "Well, uh—"

    "Hmm. I'm not sure what to tell him. Maybe... maybe if he doesn't like either Emily or Mrs. Pear, then mentioning their order of events could goad him into telling us something important... or I could tell him about both... or neither..."

    menu:
        "Well it's Mrs. Pear, you see. She said that Thursday was the library, Friday here, and Saturday the mayor's office.":
            jump d1s11c_terry_o1

        "The mayor for one. She told us a completely different story—she said Thursday was here, Friday her office, and Saturday the library.":
            jump d1s11c_terry_o2

        "Well both Mrs. Pear and Mayor Sawyer disagree with your story. Can you think of any reason for these discrepancies?":
            jump d1s11c_terry_o3

        "I can't speak about other witnesses, sheriff. You should know that. It's confidential information.":
            jump d1s11c_terry_o4

label d1s11c_terry_o1:
    show marley neutral with dissolve
    show ron neutral with dissolve
    show terry neutral with dissolve

    r "Well it's Mrs. Pear, you see. She said that Thursday was the library, Friday here, and Saturday the mayor's office."

    show terry smile with dissolve

    t "Mrs. Pear—you mean that ancient librarian? Oh, I wouldn't mind her. She spouts nonsense sometimes."

    show ron serious with dissolve

    r "She does work at one of the scenes, and she's sure that it was attacked Thursday."

    show terry serious with dissolve

    t "Well it wasn't. I'm the sheriff, I've investigated each of the scenes, and I know the order! You can't seriously be listening to her over me? Honestly, if you ask me, it's high time that particular mare was taken out to pasture—"
    t "Put her out of her misery like a horse with a broken leg."

    "It's good to see some things never change—Terry's just as kind an' sensitive as ever."
    "But this business seems to be riling him up. Maybe I should lay off him..."

    show ron thoughtful with dissolve

    r "Well she ain't the only one who's story don't line up with yours, Terry. An' I ain't seen no hard evidence corroborating the day any of 'em were hit—"

    show terry moody with dissolve

    t "Look, who are you gonna take seriously here, me, the {i}sheriff{/i}, or crazy Mrs. Pear?"

    "Well, he's right about one thing—he is the sheriff. And... and I guess it's plausible that Mrs. Pear might be... getting on a bit. Mentally. So maybe I should let it go."
    "On the other hand, he does seem real defensive. Too defensive? Maybe I should keep pressing."

    menu:
        "Alright fine, Terry. You might have a point there. I don't know much about Mrs. Pear, I ain't seen her in years. She- she could have changed.":
            jump d1s11c_terry_o12o1
        
        "I know it's been a while, but I was close to Mrs. Pear once. And it don't seem like she's changed much—as far as I can see, she's as sharp as ever. Listen, Terry, I need evidence. Cold hard evidence.":
            jump d1s11c_terry_o12o2

label d1s11c_terry_o12o1:
    show marley neutral with dissolve
    show ron thoughtful with dissolve
    show terry neutral with dissolve

    r "Alright, fine, Terry. You might have a point there. I don't know much about Mrs. Pear, I ain't seen her in years. She- she could have changed."

    show terry smile with dissolve

    t "Exactly! Look, Mrs. Pear—she's old. Older than anyone else in this town. And I know you were close to her back in the day, but you gotta accept that the old coot just ain't got it all there anymore. Ain't all there like she used to be."

    show ron curious with dissolve

    r "Does she... {i}do{/i} things that are unusual? That suggests she's... degrading?"

    show terry thoughtful with dissolve

    t "Yeah, she makes a fuss about things that are... just nuts. She hears things—I'm sure you'll see."
    r "Okay..."

    jump d1s11c_terry_c1

label d1s11c_terry_o12o2:
    show marley neutral with dissolve
    show ron neutral with dissolve
    show terry neutral with dissolve

    r "I know it's been a while, but I was close to Mrs. Pear once. And it don't seem like she's changed much—as far as I can see, she's as sharp as ever. Listen, Terry, I need evidence. Cold hard evidence."

    show terry moody with dissolve

    t "Pfft! Evidence? Like what?"

    show marley thoughtful with dissolve

    m "Well, shouldn't there be, like, crime scene photos, forensic evidence that's dated, reports—can't we see those?"

    show terry awkward with dissolve

    t "Well, uh... n-no."

    show terry serious with dissolve

    t "No, you can't."

    show marley curious with dissolve

    m "And whyever not?"
    t "It's classified police evidence."

    show ron serious with dissolve

    r "But you're meant to be helping us."

    show terry awkward with dissolve
    
    t "Uh, well, it's official police records. Can't let you look without the proper... clearance."

    "No way. I'd bet my left boot that he ain't collected any evidence at all. Just closed off each scene an' left it at that."

    t "An' what's more, we didn't know what we were looking at until we found the corpses in the mayor's office—"

    show terry serious with dissolve

    t "Because that was the place attacked first. Before that, we just thought it was a regular vandal attack."

    show marley serious with dissolve

    m "How could you have had an opinion 'before' if you found corpses at the first scene?"

    show terry smile with dissolve

    t "Well aren't you paying attention, little lady. It was just what we thought before we found the bodies—you know, during the initial assessment."

    "He says that like they did more than look around the scene and jump to the first conclusion before alternate evidence dropped into their laps."

    m "Call me 'little lady' again and I'll prove how closely I'm paying attention—specifically to the location of your jugular."

    "Alright, time to change topics..."

    jump d1s11c_terry_c1

label d1s11c_terry_o2:
    show marley neutral with dissolve
    show ron neutral with dissolve
    show terry neutral with dissolve

    r "The mayor for one. She told us a completely different story—she said Thursday was here, Friday her office, and Saturday the library."
    t "And what does the mayor know? She spends so long running around, I'm surprised she even knows what day it is, let alone what days attacks happened."

    "He's got a good point there. Emily has a lot going on; she could've mixed up the dates."

    t "Look, I've got it all down in the official police reports. I'm right and everyone else you spoke to is wrong. End of story."
    r "Um..."
    t "End. Of. Story."

    jump d1s11c_terry_c1

label d1s11c_terry_o3:
    show marley neutral with dissolve
    show ron neutral with dissolve
    show terry neutral with dissolve

    r "Well both Mrs. Pear {i}and{/i} Mayor Sawyer disagree with your story. Can you think of any reason for these discrepancies?"
    t "Yeah I can think of two! They're crazy and they're tryin' to sabotage this case. They wan' me to look incompetent. Huh, like anyone would believe that!"

    "Right... how could anyone believe that."

    jump d1s11c_terry_c1

label d1s11c_terry_o4:
    show marley neutral with dissolve
    show ron neutral with dissolve
    show terry neutral with dissolve

    r "I can't speak about other witnesses, sheriff. You should know that. It's confidential information."
    t "Well that's just a load of crock! I'm the doggone sheriff, I should have the clearance to hear whatever you've learned."
    t "In any case, I thought this was supposed to be a collaborative investigation. You trying to usurp me, Kitzinger?"
    r "Wouldn't dream of it, Terry."

    "We're only working 'collaboratively,' if the definition changed to 'one person does all the work and the other takes all the credit' while I wasn't looking."
    "It'd probably be easier to just lie at this point. Arguing with him is exhausting."

    r "It's just that there's some sensitive information around these witnesses. It wouldn't be professional for me to disclose the details."
    r "I'm sure a capable sheriff like you understands."

    "Terry humphs unhappily."

    t "Right, sure. I get that."

    jump d1s11c_terry_c1

label d1s11c_terry_c1:
    show marley neutral with dissolve
    show ron neutral with dissolve
    show terry neutral with dissolve

    r "Alright, Terry. Well thanks for answering my questions. I'm sure it'll all be very... useful."

    "I'd ask him about his relationships with others, but it seems clear that most people I've spoken to hate his guts. Well, except for Danny. But even he described their relationship as awkward."

    r "I think that's all the questions I've got for now."

    show terry smile with dissolve

    t "Sure thing, Ron. No problem at all!"
    t "And, hey, I'll see y'all at patrol tonight."

    "I plaster on the fakest smile I've got."

    r "Yeah, see you then."

    "I try to add 'I'm looking forward to it' but can't bring myself to. Terry seems to get that sense from my words though, since he gives me a big slap on the back and grins from ear to ear."

    t "It'll be a treat!"
    r "I'm sure..."

    scene black with fade

    jump d1s10_map