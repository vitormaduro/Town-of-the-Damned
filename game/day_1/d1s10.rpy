# Let's talk about Danny
label d1s10:
    scene bg kingston_streets with fade

    show marley moody at right with dissolve
    show danny moody at left with dissolve
    show ron worried at center with dissolve

    b "You can't call me names!"
    m "Just watch me, you human embodiment of a loose toenail!"

    "That voice, I'd heard that voice again! Taunting me! Did... did it know..."

    b "Oh you’re just jealous!"
    m "Of {i}what{/i}? You're the one that's been acting like an insecure lead cheerleader from a cliché high school film!"

    "Something's wrong here... something deeper than ghouls attacking buildings. I can feel it."

    b "Oh why don't you buzz off back to England?"
    m "Oh you'd like that, wouldn't you?"

    "And why won't these two shut the hell up?"

    m "I'm not blind. I know you're dying for me to bugger off and leave you all alone with—"
    r "Shut it, both of you!"

    "The pair awkwardly fall silent."

    r "This is an investigation; I'm not having the two of you following me around squabbling like children!"

    show danny awkward at left with dissolve

    b "Sorry, Ron."

    "Marley doesn't apologize. Just stares at me stubbornly. She looks mad."

    show ron tired at center with dissolve

    r "{i}*Sigh*{/i} Why don't you do me a favor, Danny?"

    show danny smile at left with dissolve

    b "Sure, Ron. Whatever you need!"

    "I need something—anything—to make him scram."

    r "Why don't you check in with Terry about tonight's patrol? Get an idea of the route and who's going to be there, or anything else that’s useful."

    "Anything to get him to go!"

    b "Sure, whatever I can do to help!"

    show danny smile at offscreenleft with move
    show ron tired at left with move

    "For a second, Marley just keeps staring at me. Not angry anymore. Just... thinking. Calculating. Then, finally, she speaks."

    show marley serious at right with dissolve

    m "Don't you think you should have told me about {i}that{/i}?"

    "I know what she's talking about. But... I don't want to."

    show ron awkward at left with dissolve

    r "Told you about what?"
    m "Don't play dumb with me Ronald-bloody-Kitzinger, or I will shout about Danny's crush on you so loud that the whole town will hear."

    show ron blushing at left with dissolve

    r "Don't you dare!"

    show ron awkward at left with dissolve

    r "{i}*Sigh*{/i} And it's not a {i}crush{/i}. Not really."
    m "No. You're right. It's worse than that!"

    show ron moody at left with dissolve

    r "Now you're just being dramatic."
    m "He's like an overprotective guard dog!"
    r "He doesn't like change. Or... strong personalities."

    show ron tired at left with dissolve

    r "I would have thought he would have got over it by now."

    show marley thoughtful at right with dissolve

    m "When did this all start?"
    r "When we were still at school. It was awkward as hell—I was oblivious at first."

    show marley neutral at right with dissolve

    m "You? Oblivious? Never."
    r "Yeah, yeah. Well, he was my best friend back then. And I told him I was gay before anyone else."

    show ron awkward at left with dissolve

    r "And I {i}also{/i} told him I had a crush on someone in our grade."
    m "And Danny thought you meant him?"
    r "Exactly. I told Danny I had this big idea to ask my 'mystery man' out. Poor old Danny upped his advances, until even I couldn't mistake them. I finally put two and two together. Realized he was sweet on me and thought I was sweet on him."

    show marley curious at right with dissolve

    m "So how did he take it when you broke the news?"
    r "Uh... well, um... about that..."

    show marley worried at right with dissolve

    m "Ron..."
    r "I didn't! I never acknowledged it. Just ignored it and hoped it would go away."

    show marley tired at right with dissolve

    m "Ron!"
    r "He found out it wasn't him eventually. The day I left. But that was nearly ten years ago! I thought he would have got over it by now."

    show marley moody at right with dissolve

    m "He didn't, Ron! He absolutely did not!"

    show ron tired at left with dissolve

    r "Listen, Danny—he's harmless. If you give him a talking to when he's been too much of a pest, he'll back down."
    m "This is a flaw of yours, Ron. You never deal with problems."
    r "I'm a detective! My {i}job{/i} is to solve problems!"
    m "Other people's problems. You always run away from your own."

    "I try desperately not to think of the graveyard I'd insisted we leave."

    show ron awkward at left with dissolve

    r "What, me? When have I ever—"

    show marley moody at right with dissolve

    m "The office gets like ten different completely useless magazine subscriptions because you couldn't get yourself together and cancel them!"
    r "It's not that I can’t get myself together! It's that they make it so difficult—"
    m "The sink in your apartment has been blocked since the day you moved in, but you keep putting off telling your landlord."
    r "You try telling a six-foot-five half-troll that you need him to do some DIY!"
    m "One time you almost married that siren lady so she could get a green card! The only reason you didn't was because I pretended to be your secret wife that you thought had died! She still sends us anniversary cards!"
    r "Look, when there's no monster to slay or criminal to catch, problems get... complicated."
    m "No kidding, Ron! That's why they're called {i}problems{/i}!"

    show ron serious at left with dissolve

    r "Look, can you just promise me you're not going to get involved? You can scare him into backing down if he gets too..."

    show marley serious at right with dissolve

    m "Too much like a possessive teen obsessed with their ex?"
    r "If he gets too {i}much{/i}, you're welcome to... get him to back off. In that charming way of yours."

    show marley smile at right with dissolve

    m "I am charming."
    r "But don't talk about this whole... crush mess. Promise?"

    show marley moody at right with dissolve

    m "Shocking as it may seem, Ron, I have no burning desire to fix your screw-ups."
    r "Say that you promise!"
    m "I promise, I promise!"
    r "Good."
    m "Now can we please get back to some actual work?"

    show ron neutral at left with dissolve

    r "Great idea. We've got these suspect files to fill in. Where should we head to first?"

    jump d1s10_map

label d1s10_map:
    menu:
        "First proper interview of Seb":
            jump d1s11a

        "Mrs. Pear or Emily?":
            jump d1s11b

        "Norman or Terry?":
            jump d1s11c

        "Patrolling with Terry":
            jump d1s12