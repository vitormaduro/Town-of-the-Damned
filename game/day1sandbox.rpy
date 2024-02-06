label terryMaddux2:
    #[D1] [S6d] [Optional]- Terry Maddux 2
    #FADE IN
    #Location- Sheriff's office
    scene bg sherrifs_office
    show terry smile at right
    show danny neutral at center
    show marley moody at left
    with fade
    ter "Heh, couldn’t stay away from me, huh sugar?"
    mar "Oh God, I think I'm gonna puke."
    ter "I love it when a gal plays hard to get."
    mar "I'm not playing hard to get—I don't like you. Stop flirting with me."
    ter "Hehe, I find it hard to believe you don't want a piece of this; all the girls want me in their bed."
    show marley smile with dissolve
    mar "Yeah, you should keep in mind that low prices always attract lots of customers. Come on guys, let's go. Every time he opens his mouth, I wanna tear my ears off."
    #FADE OUT
    #Return to MAP


    #[D1] [S6e]- Mrs. Pear
    #FADE IN
    scene bg library
    show danny neutral at right
    show marley neutral at center
    with fade
    "Walking into the library is like being dragged back through time. The musty smell of the books. The perfect silence. The calm."
    ron "This place hasn't changed a bit."
    dan "Yeah, Mom says that she keeps trying to give it funding for refurbishment, but the council keeps blocking her."
    #SFX- knocking on wood
    "The sound of knocking on wood makes me glance over to the library's main desk."
    #Sprite L- Mrs. Pear (Neutral)
    ron "Holy cow, it's Mrs. Pear! I thought she'd be long dead!"
    #Sprite L- Mrs. Pear (Angry)
    p "I ain't dead, Ronald Kitzinger, and I sure ain't deaf, either."
    ron blushing "Oh shoot, uh, sorry, Mrs. Pear. I hear the library was attacked by ghouls a few days ago?"
    #Sprite L- Mrs. Pear (Neutral)
    p "That's what they tell me. Of course, I told them first, but everyone thought it must have been a racoon or something, and I was going batty. That's until they found the ghouls’ bodies, of course."
    p "Of course, the fact that the sheriff’s office was attacked the next day and the mayor’s the day after helped. Not even the sheriff could believe raccoons did all that; although, I wouldn’t put it past him."
    ron neutral "I, uh—I'm sorry about that, Mrs. Pear. That sucks. Can I ask what area was attacked?"
    p "The occult section. As if that wasn’t suspicious enough! If the sheriff really thought a racoon would only attack books that fall between 131 and 139 on the Dewey Decimal System, then he needs a lobotomy."
    ron smile "Haha, yeah. Do you know what books were destroyed in the attack?"
    p neutral "Not off the top of my head. But I have a record of them somewhere."
    ron "Can I see?"
    p "Well, it'll probably take me a while to compile but I can get a list to you over the next few days."
    ron "Thank you. Is the occult section still where it used to be?"
    p "Sure is. The old chair you used to sit on is still there too. And the one your skinny friend sat in. But not the one the plump little one that always used to pick his nose used. We had to get rid of that one. The base was… crusty."
    show marley angry with dissolve
    mar "Oh eww."
    show danny angry with dissolve
    dan "Hey! I never picked my nose!"
    p "Oh, it's you. I didn't recognize you."
    dan "And I wasn't fat! I was big boned."
    p "Uh-huh…"
    ron smile "Hehe."
    show marley smile with dissolve
    mar "Hehehe, I like this woman."
    ron "Oh, sorry Marley—Mrs. Pear. Mrs. Pear, this is Marley, my assistant. She's a Witch."
    #Sprite L- Mrs. Pear (Moody)
    p "Oh. You are? You ain't planning to do any of that creepy magic crap, are you? I don’t like that stuff. Keep it away from me."
    "What the hell? I've never heard Mrs. Pear talk about magic like that; I had no idea she was so suspicious of it."
    show marley moody with dissolve
    mar "Well, I have my level one license, ma'am. I'm permitted by law to do—"
    p "I don't care about your darn license. You don't do that mumbo-jumbo junk around me, you hear?"
    "As I watch, astounded, Mrs. Pear digs her hand into the pocket of her jacket and pulls out a packet of salt—the kind they keep at diners to put on your fries. She rips open the paper wrapper and tosses the contents over her shoulder."
    "What the actual hell?"
    "But Marley seems to recognize the gesture. And her face turns thunderous."
    show marley angry with dissolve
    "But she bites her tongue, keeping silent. Letting me deal with the old woman who was once one of my only friends. Who is now insulting my current best friend."
    "Damn."
    "Okay, okay, think this through, Ron."
    "I can tell her off."
    "I can focus on being serious, professional."
    "Or I can talk to her as a friend."
    menu resolveArguement:
        "Hey, don't you dare talk to her like that! That's my assistant and friend you’re disrespecting, and I ain't gonna abide that kind of attitude against her.":
            jump defendAssistant #+_ to Mrs. Pear's Anger meter, {Go to [D1] [S6e] [O1]}
        "I can't promise we won't utilize Miss Shipway's specific skill set. This is an important case. And please, my assistant deserves all the respect and politeness you afford me. She's a responsible magic wielder and a key part of this investigation.":
            jump middleGroundAgreement #+_ to Mrs. Pear's Trust meter, {Go to [D1] [S6e] [O2]}
        "Don't get me wrong Mrs. P, sometimes she freaks me out with all the crazy crap she can do. But she's a good woman; she don't deserve no disrespect. So kindly treat her with dignity, alright?":
            jump agreeWithPears #+_ to Mrs. Pear's Friendship meter, {Go to [D1] [S6e] [O3]}

label defendAssistant:
    #[D1] [S6e] [O1]
    scene bg library
    show danny neutral at right
    show marley angry at center
    #Sprite L- Mrs. Pear (Moody)
    with fade
    ron angry "Hey, don't you dare talk to her like that! That's my assistant and friend you’re disrespecting, and I ain't gonna abide that kind of attitude against her."
    #Sprite L- Mrs. Pear (Angry)
    #Sprite L- Mrs. Pear (Sad)
    p "I'm sorry, young lady. I-I've had some… difficult experiences with magic wielders that've made me a tad weary of them."
    p "But I shouldn’t have taken that out on you. And if Ron says you're a responsible spellcaster—well, then I believe him."
    #Sprite L- Mrs. Pear (Awkward)
    p "But, well, if I can ask you a mighty big favor, my gal?"
    show marley awkward with dissolve
    mar "Uh…"
    p "If- if ya do any of your fancy spells, well, could you do it away from me? Just… I don’t mean to be cruel, but it brings back some… bad memories."
    mar "Uh- well, I… I don’t want to make you uncomfortable, ma’am. I don’t want to trigger your trauma."
    #Sprite L- Mrs. Pear (Neutral)
    p "That’s mighty kind of you, dearie. You’re a nice gal, Miss Marley."
    "She is not. Don't get me wrong, I love her like a sister. But she ain't what I would call 'nice.'"
    "Marley looks uncomfortable. I'd better change the subject."
    jump investigationInTheLibrary #Go to [D1] [S6e] [C1]

label middleGroundAgreement:
    #[D1] [S6e] [O2]
    scene bg library
    show danny neutral at right
    show marley angry at center
    #Sprite L- Mrs. Pear (Moody)
    with fade
    ron serious "I can't promise we won't utilize Miss Shipway's specific skill set. This is an important case. And please, my assistant deserves all the respect and politeness you afford me. She's a responsible magic wielder and a key part of this investigation."
    #Sprite L- Mrs. Pear (Thoughtful)
    p "Look, miss, I appreciate I may have been a little… curt. I just… I've had some experiences that make me mighty uncomfortable around people that use magic."
    p "So please, for my sake, keep any magic shenanigans away from me."
    show marley moody with dissolve
    mar "Well, I'm fine doing that."
    "I guess that's something."
    "I think it's best to move on now."
    jump investigationInTheLibrary #Go to [D1] [S6e] [C1]

label agreeWithPears:
    #[D1] [S6e] [O3]
    scene bg library
    show danny neutral at right
    show marley angry at center
    #Sprite L- Mrs. Pear (Moody)
    with fade
    ron smile "Don't get me wrong Mrs. P, sometimes she freaks me out with all the crazy crap she can do. But she's a good woman; she don't deserve no disrespect. So kindly treat her with dignity, alright?"
    #Sprite L- Mrs. Pear (Smiling)
    p "Oh, those Witches and Warlocks and whatever always give me the creepy-crawlies. Have since I was a gal."
    p "I've seen some mighty odd stuff in my time thanks to magic users."
    #Sprite L- Mrs. Pear (Thoughtful)
    p "Some mighty awful things."
    p "Makes a person wary, you know?"
    #Sprite L- Mrs. Pear (Neutral)
    p "Uh, but I probably was a bit too rude to your gal… I'm sorry, dearie. But—well, when you do your fancy magic, would you mind terribly just keeping it away from me?"
    show marley moody with dissolve
    mar "Yeah, sure."
    "Well, situation diffused—kinda."
    "Think I'd better change the topic."
    jump investigationInTheLibrary #Go to [D1] [S6e] [C1]

label investigationInTheLibrary:
    #[D1] [S6e] [C1]
    scene bg library
    show danny neutral at right
    show marley neutral at center
    #Sprite L- Mrs. Pear (neutral)
    with fade
    ron "Do you have any CCTV around the building?"
    #Sprite L- Mrs. Pear (Nervous)
    p "Oh, well, yes, but I don't understand this new-fangled computer system it's hooked up to."
    ron "Well, uh, would you mind taking Danny to the back office so he can have a look at it?"
    show danny thinking with dissolve
    #Sprite L- Mrs. Pear (Neutral)
    dan "Oh, won't you need help examining the scene?"
    ron "No, I've got it, don’t worry."
    p "Come on, nose picker."
    dan "Don't call me that!"
    hide danny
    # hide mrs pear
    with dissolve
    "I turn to Marley."
    ron confused "What was that thing she did? The thing with the salt packet?"
    "My eyes glance down to the little clear crystals scattered across the floor."
    show marley serious with dissolve
    mar "It's one of those superstitions. Meant to ward off Infernals. To Warlocks, it's a real eff-you. To a Witch, it's… ignorant. Not only is it an attempt at hurting part of who I am at my core, but… it’s the wrong core. Like calling an English person 'Yankee scum.'"
    mar "Anyway, I'll go put up the charms."
    hide marley with dissolve
    "Strange. Very strange. Seb's half-elf, so he's a magical creature. But Mrs. Pear seemed to like him, at least when we were kids. And she always seemed to like talking about magic and stuff."
    "So why was she so frosty to Marley?"
    "I head towards the stacks, my feet remembering the route before my mind does."
    "The occult section looks pretty bad. The bookcase has been trashed and none of the books on it seem to have survived. Scraps of paper are sprinkled over everything like snow. There's no way to tell which shreds belong together or which torn up covers they've come from." 
    "If I were a betting man, I'd say someone really didn't want folks knowing what books were in that wreckage. Or maybe they didn't want anyone reading up on what they've been doing."
    "There's glass everywhere from a nearby window that’s been smashed in. I wander over to it and see mud and dirt tracked onto the carpet, forming the shape of shuffling footprints."
    seb "'And the hungry worm went chomp chomp chomp, and soon, there was nothing left of the apple!'"
    "The familiar voice hits me like a punch to the gut."
    "Seb."
    "I slink through the shelves, keeping my head low so no one can see me."
    "I follow the voice to the children's section. I peer around the shelf and see him in a small nook, sitting on a low chair, surrounded by wide-eyed five-year-olds."
    #CG- Seb sitting in a small chair, surrounded by little children. He's reading a big picture book- in the style of The Gruffalo, or The Very Hungry Caterpillar.
    seb "So what do you think happened to the hungry worm?"
    k1 "It got bigger!"
    seb "That's right, it got even bigger than it was before!"
    "I can't stop the slow smile that creeps across my face as I watch him."
    "My first ever crush. He hasn't changed. Oh, sure, he's gotten taller. But he's got the same kind smile. Same cheeky, laughing eyes. Same bright purple hair—though I can’t help but notice a tuft has been chopped off, ruining his otherwise careful hairdo."
    "The children are looking at him adoringly as he reads from a colorful picture book, displaying the drawings on each page for them."
    "The scene is perfect."
    "And I'm a coward."
    "So I turn away, not wanting to disturb him."
    "But behind me, I hear Seb's voice falter."
    seb "'Bigger and bigger—' Oh my God, Ron?"
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
    seb "Uh, the worm got so big that he exploded. The end."
    "He snaps the book shut."
    seb "Okay, reading time's over now."
    k3 "What? That's not how that story ends!"
    seb "Um, yes it is. Very sad."
    k4 "I've got that book at home. It definitely doesn’t end like that!"
    seb "Well, uh, it's not the same book. This is an off-brand version. Anyway, I've got to go."
    #CG ends- back to Library background
    #Sprite R- Seb (Nervous)
    show seb awkward at center with dissolve 
    "I watch as he leaps to his feet and makes his way through the sea of children, dancing left and right to avoid stepping on their little hands and feet, until he's suddenly standing right in front of me."
    "Oh man. Come on, Ron. Calm down. Be smooth."
    "And my God is he gorgeous."
    "It takes me a good few attempts to remember how to speak again."
    ron awkward "I, uh… I think you've left your audience with some complaints, Seb."
    seb "Umm… don't- don’t worry about it. Kids are the worst critics. What are you doing here, Ron?"
    "Okay, smooth. I can do this."
    ron "Well, a little bird told me there's trouble in town. I'm here to fix it."
    "Yep. That was smooth, right?"
    seb "Huh. That'll be a first, Ron. You're always the one starting trouble if I remember correctly."
    ron "That’s an awfully mean thing for such a pretty mouth to say."
    show seb blushing with dissolve
    "OH MY GOD OH MY GOD TOO SMOOTH DID I JUST SAY THAT OUT LOUD?"
    "I sound like a corny, misogynistic superhero from a 40-year-old comic!"
    "I once saw the Earth open and swallow someone whole. I think it’s darn rude that it’s not offering me a repeat performance and devouring me right now. Anything to get me away from those eyes, from the embarrassment, from my soul wanting to vomit itself out of my body."
    seb smile "Hehe, same old Ron."
    "Huh. Laughing. Not the reaction I was expecting."
    "Honestly, I thought he'd storm off."
    "Okay, maybe keep up the flirt?"
    ron "Did you miss me?"
    seb "I'm not going to answer that, Ron."
    ron "Maybe that's answer enough, Seb."
    seb "Always so cheeky. Anyway, how… how have you been? What’ve you been up to?"
    ron "I've been good. I started up my own detective agency. You?"
    seb "I'm an English teacher up at the high school. Go Kingston Wolves, et cetera an' whatever. So, if you're a detective, are you the one investigating the attacks?"
    ron "That's right. You know anything about them?"
    show seb neutral with dissolve
    seb "No. No, but I do know the kids have all been really shaken up about it. I know there's rumors that kids messing about are responsible for these attacks, but I'm sure it's not anyone in any of my classes."
    seb "But to be honest, I've been trying not to get involved, and even if I was feeling nosy, no one would tell me anything."
    ron neutral "Huh?"
    show danny neutral at left with dissolve
    dan "The cameras didn't show nothing. The ones that worked, at least—the whole setup is old as hell. And that hag was breathing down my neck the whole time. She is so bad with technology."
    ron "Like you can talk, you used your mom's email account till you were eighteen."
    dan "I thought you had to pay for each account— Oh."
    show danny moody with dissolve
    dan "Seb. It's you."
    show seb moody with dissolve
    seb "Danny."
    dan "Oh dear. Looks like you're having one of those 'hair don't' days."
    ron "Danny!"
    seb "At least for me, it's a one-off. It seems like all your days are 'hair oh-hell¬-no’ days."
    ron "Seb!"
    seb "I'm sorry, Ron, I've got to go. I'll see you around."
    ron "Wait, Seb—"
    hide seb with dissolve
    dan "Come on Ron, we should go."
    ron angry "What the hell, Danny? Why were you so rude to Seb?"
    dan "Because I remember what he did, Ron. I remember that he drove you away—"
    show marley at right with dissolve
    mar "I've finished putting up the protection charms, Ron. I used four—one for the front door, one for the back, one over the window that's already broken, and one on the windows on the other side of the building."
    ron neutral "Huh? Oh, right, great. Thanks, Mar. I guess we're done here, then. Let's go."
    #FADE OUT
    #Return to MAP


    #[D1] [S6f] [Optional]- Mrs. Pear 2
    #FADE IN
    scene bg library
    show danny neutral at right
    show marley neutral at center
    #Sprite L- Mrs. Pear (neutral)
    with fade
    #Location- Library
    #Sprite R- Mrs. Pear (Neutral)
    #Sprite M- Danny (Neutral)
    #Sprite L- Marley (Neutral)
    p "Oh, you're back. And you've brought your lovely wife with you again!"
    #Bottom Sprite- Ron (Surprised)
    ron neutral "What? Oh, no, she's not my wife!"
    #Sprite L- Marley (Laughing)
    mar "Hehe, definitely not."
    p "Oh. Well, she's very pretty. If I were you, I'd put a ring on her finger real fast, or someone else will snap her up. She's quite the catch!"
    mar "Aw, thank you! That's really kind of you! You should listen to the lady, Ron. She's very wise."
    p "Thank you, dear."
    #Bottom Sprite- Ron (Indignant)
    ron "Stop encouraging her! Ugh. Come on, let's go before she shoves a ring in my hand and forces me down on one knee."
    #FADE OUT
    #Return to MAP


    #[D1] [S6g] [Optional]- Back at the office (short)
    #FADE IN
    #Location- Ron's office
    #Sprite R- Danny (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    mar "Did we forget something?"
    ron "Uh, no, I don't think so."
    mar "Well, then let's head off."
    #FADE OUT
    #Return to MAP


    #[D1] [S7]- Discussing the evidence
    #FADE IN
    #Location- Ron's office
    #Sprite R- Marley (Neutral)
    #Sprite L- Danny (Neutral)
    #Bottom Sprite- Ron (Moody)
    ron "Danny, you could have warned me that the doggone sheriff was Terry frickin’ Maddux."
    dan "Sorry, sorry. But Terry ain’t that bad." 
    mar "You really hate discount Biff Tannen, huh Ron?"
    dan "Who?"
    mar "Uh… bad guy from Back to the Future?"
    ron "Terry was our high school bully. He beat me up. Stole my lunch money. Beat me up. Made me give him my stuff. Beat me up. Threw me in the dumpster. Beat me up. Ripped up my homework. Beat me up. Poured food all over me. And did I mention he beat me up?"
    dan "You’re exaggerating."
    ron "I once had to get three stitches ’cos he slammed my head into a desk! Why are you defending him? He was even worse to you."
    dan "It was just childhood teasing; I got over it. And hey, you beat him up pretty bad yourself that one time."
    #Bottom Sprite- Ron (Confused)
    ron "When?"
    dan "The- the day that you… left."
    #Bottom Sprite- Ron (Neutral)
    ron "Oh right, yeah. I remember now. Well, he deserved it."
    #Sprite L- Danny (Annoyed)
    dan "Well, everything kind of blew up for poor Terry after you left."
    #Bottom Sprite- Ron (Confused)
    ron "What do you mean?"
    dan "You don't know?"
    ron "Know what?"
    dan "Well… do you remember how Terry got a full ride to Ohio State on a football scholarship?"
    ron "Yeah. He was the star quarterback in high school. He always talked about how excited he was for it."
    dan "Yeah, it was his dream since he was a kid. Well, after you left, someone sent Ohio State an old video of him being… crappy to you. And they put it online—it went vial. No one knows who it was, but the university rescinded the scholarship."
    ron "Oh. Oh wow. I hate to feel sorry for the guy, but… jeez."
    mar "Let's put aside that muscled twit for now. What have you learnt, Ron? Give me the rundown."
    #Sprite L- Danny (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "Okay, let’s talk about the library first. Occult section looks like it's been put through a shredder."
    mar "Alright, why?"
    ron "I'd guess either to stop people realizing a book or two’s gone missing, or to make it harder to research what's going on. Maybe both."
    mar "Makes sense."
    ron "Scene two: mayor’s office. Ghouls ran amok and smashed the mayor's secretary's computer. She then fired him."
    mar "Angry, screaming weirdo in the car park?"
    ron "Angry, screaming weirdo in the car park. Strange timing. Especially since the mayor seems to loathe him."
    mar "Suspicious."
    ron "Very."
    dan "What, Norman? Nah, he got the job as a favor—his pa used to be on the city council before he died. Norm was awful at his work; he was a jackass to everyone, careless, lazy, whatever. But my mom played nice to butter up his old man. I think this whole ghoul thing’s made her a bit more daring, so she finally gave him the can."
    ron "Hm. I see. Anyway, scene three: the sheriff's office. Again—very targeted attack"
    mar "The chief deputy."
    ron "Uh-huh. Second computer trashed."
    mar "Summoner's a technophobe?"
    ron "But only for certain people's tech? And I found this—"
    "I pulled the stick from my bag."
    mar "A USB stick?"
    ron "Found it hidden in the ruins of the desk."
    mar "Well, that's got to be important."
    "I notice something else in the bag."
    #Bottom Sprite- Ron (Surprised)
    ron "Oh shoot—there's the book. I forgot about that; I didn't mean to bring it."
    mar "What is it?"
    ron "Old yearbook from the local high school. Found it in the desk. I don't think it's important, but we'll stick it in the evidence box."
    dan "Evidence box?"
    ron "That big metal lockbox under the desk—we put all evidence in there to keep it safe."
    dan "Ah right, I see. Well, I guess all that's left now is to go interrogate Seb then lock him up!"
    mar "Kind of jumping the gun a bit there, bucko."
    dan "Why? We've found his stuff at all the crime scenes. What more do we need?"
    mar "A motive, maybe?"
    dan "Revenge? Rage?"
    ron "What do you mean?"
    #Sprite R- Danny (serious)
    dan "I wouldn’t be surprised if Sebastian Daley wanted to see this whole town burned to the ground."
    #Bottom Sprite- Ron (Confused)
    ron "Why?"
    dan "He's not a popular guy. That's all you need to know."
    ron "What the hell are you going on about?"
    #SFX- Ring ring
    "The sound of the office phone makes me jump. I pick it up as Danny fiddles awkwardly with a pen."
    #Bottom Sprite- Ron (Neutral)
    ron "Hello?"
    ter "Ron, my man!"
    ron "Oh. Hey Terry."
    ter "So me and my boys are going patrol the town tonight in case the ghouls show their moldy-rotten faces. Figured I'd invite you, Danny, and that cute little assistant of yours to tag along. Meet us at eight, outside the sheriff's office?"
    ron "Oh, right. Thanks. We'll be there."
    ter "Awesome! You'll get to see how real detectives act."
    #Bottom Sprite- Ron (Moody)
    "I roll my eyes."
    ron "We'll head to the station soon. See you then."
    #SFX- phone being put down
    ron "Well, it sounds like we're in for a delightful evening. Terry has invited us to patrol the town with him."
    #Sprite R- Marley (Moody)
    mar "And you couldn't have told him we had better things to do? Like… anything that didn't involve him?"
    #Sprite L- Danny (Thoughtful)
    dan "Maybe this will be a good opportunity for you, Ron. To, you know, bond with Terry. For you both to put the past behind you."
    ron "I'd rather bond with a benign tumor."
    #SFX- a newspaper drops into a mailbox.
    #Sprite L- Danny (Moody)
    dan "Aww crap."
    #Bottom Sprite- Ron (Curious)
    ron "What?"
    dan "The paper. The Kingston Rag."
    #Sprite R- Marley (Confused)
    mar "Why does that make you mad?"
    dan "There's this gossip columnist, Cléber Chalá, who’s always published in it. Well, I mean, that's probably a pen name. No one in the town has that name."
    #Sprite R- Marley (Thoughtful)
    mar "I've heard that name before. I think he's a football player. Or I guess soccer for you guys."
    dan "Well whoever our Cléber is, they're a pain in my ma's ass. Basically, they can write whatever they want scot-free as long as they say 'there's a rumor that…' in front of it."
    mar "Why read it if it annoys you?"
    dan "Well, the problem, professor, is that the whole darned town reads this stupid column. These idiots eat this garbage up. I need to know what it says so I can be prepared."
    #Sprite R- Marley (Moody)
    mar "Alright, alright, no need for the attitude. Let's see this dreaded column then."
    #Cléber Chalá Clippings for Sunday, May 8th opens. It's a page of a newspaper that reads as this:
    #Chaos Grips Kingston!

    
    
    # I am sure that, just like me, many of you, my darling devoted readers, are deeply disturbed by recent happenings. You may be aware that evidence has emerged showing certain unknown members of our community behaving in a manner that is frankly unacceptable.
    # Although our authorities have been doing their utmost to keep these events quiet, it's come to the attention of this here writer that the office of our mayor, the sheriff's office, and our community library have all been brutally attacked. I can only assume this is the work of local youths looking to cause a ruckus.
    # In my humble opinion, this disrespectful string of attacks can only be blamed on the moral decay of today’s youngins. I don't know if they're restless on account of the controversial changes our mayor has inflicted on Kingston High by diverting funds away from the football team, where our youngsters can burn off excess energy, and towards things like the famously dull chess club, a useless creative writing group, and an unnecessary LBGT society. Or perhaps we should blame this delinquency on the questionable appointment of a half-elf to the teaching staff.  Either way, if our idealistic mayor and ineffective town council don't tackle this issue at its root, I'd bet my bottom dollar that we won’t see an end to these attacks.

    # If these foolish shenanigans were the only problems our community faced, that would be bad enough. But as the proud owner of the 'Town Gossip' title, part of my duties is to be the breaker of bad news. And as such, I need to break something to you good people:
    # My sources have informed me that we have a thief hiding in the high echelons of our town. Word has it that money has gone missing from the town's treasury.
    # This isn’t confirmed and is just gossip, but apparently, every month or so, a sum of around $5,000 has gone missing! That isn’t an amount to sniff at! Although it's not that much compared to the council’s budget, it still means that someone who has authority over the town is deprived enough to steal our money! Like I said, I haven’t had this confirmed, but your faithful Cléber is gonna be like a dog with a bone as far as this is concerned! I will hold the thief or thieves accountable, and I will make sure that you, good people of Kingston, know exactly what is going on in our town! I will shine a light in every dark, deprived crack of our home!
    

    #Newspaper closes
    #Sprite R- Marley (Confused)
    #Bottom Sprite- Ron (Shocked)
    ron "Jeez—whoever this writer is, they really hate your ma'!"
    dan "They hate everyone. Attack anyone they can. Anyone in the public eye. Like I've said, we're trying to keep the whole 'ghoul' thing under the rug. But if whoever this Cléber guy is finds out, half of the local government would be ripped apart."
    #Bottom Sprite- Ron (Thoughtful)
    ron "I see."
    #Sprite R- Marley (Thoughtful)
    mar "We'll have to keep an eye out for this writer."
    dan "Oh definitely. Especially because you two will probably end up in the column as soon as Cléber finds out about you. They adore gossiping about strangers. And you two are mighty strange."
    mar "True."
    ron "Well, nothing we can do about it for now. We need to focus on the case."
    #Bottom Sprite- Ron (Thoughtful)
    #Sprite L- Danny (Neutral)
    ron "But here's what's odd: our question was 'what order did the ghoul attacks happen in?' But of the three people we've interviewed, they’ve all said a different order!"
    #Sprite R- Marley (Surprised)
    mar "Really?"
    ron "Yeah. We know the attacks happened Thursday, Friday, and Saturday."
    ron "But the mayor said it was the sheriff’s office, her office, then the library. Terry said that it was the mayor’s, the library, then his office. And Mrs. Pear said it was the library, the sheriff's office, then the mayor’s."
    ron "That doesn't make any sense."
    #Sprite R- Marley (Thoughtful)
    mar "So… at least two people must have lied."
    #Sprite L- Danny (Awkward)
    dan "Or been confused. Might just be all this stress getting to them."
    #Sprite R- Marley (Thoughtful)
    mar "I dunno—if my place of work was attacked, I'd remember when it happened. And it's only been a few days."
    ron "We have to figure out the order."
    #Sprite R- Marley (Neutral)
    mar "Well, in the meantime, we can at least start on the suspect files."
    #Sprite L- Danny (Curious)
    dan "The what?"
    mar "We always make suspect files for anyone involved in the case. I'll show you what we do if you like—I can make an example one of you!"
    #Sprite L- Danny (Awkward)
    dan "Uh, what? You're going to make a suspect file of me? I don't think—"
    #Bottom Sprite- Ron (Neutral)
    ron "Oh don't worry, it's just an example one. You're not a real suspect."
    dan "Uh… well… okay. If you're sure."
    #Open up blank suspect file.
    ron "Okay, we need your name. Click on where it says 'Name' to fill it in."
    #Player must click on [Name] box on the form. When they do, the name 'Danny Sawyer' will appear inside it.
    ron "Great. Okay, first up, we have alibis. We still don't know where was attacked each day, so we'll leave that blank for now. So, where were you Thursday night?"
    #Sprite L- Danny (Thoughtful)
    dan "Thursday, uh… I'm afraid it's not a great alibi. I was home watching TV."
    ron "Okay, we'll click on the box for Thursday that's next to 'where does the suspect claim they were,’ and that'll fill in automatically."
    #Player must click on [Location of suspect]. The box will fill with the words 'At home, watching TV.'
    ron "Okay, cool. Where you with anyone?"
    #Sprite L- Danny (Blushing)
    dan "Wh-what, like a girlfriend or a b-boyfriend? Uh… nope. No, I don't have one of those. Why… why do you ask?"
    #Bottom Sprite- Ron (Awkward)
    ron "Just wanna know if you can support your alibi."
    #Sprite L- Danny (Awkward)
    dan "Oh. Uh… then no. I can't."
    #Bottom Sprite- Ron (Neutral)
    ron "Okay, so we click on that box to say 'no.'"
    #Player must click on [Name of person suspect was with] . The box will fill with the word 'No.'
    ron "We can skip the next question, so that takes us to…"
    ron "Do you have any evidence you were where you say you were? Any photos? CCTV of you going in?"
    #Sprite L- Danny (Neutral)
    dan "I'm afraid I haven't got anything like that."
    #Player must click on [Yes/No] on the Thursday question about CCTV. The box will fill with the word 'No.'
    ron "Okay, Friday. Where were you?"
    dan "I was in the diner. Meant to have dinner with mom, but she bailed. Then Terry came in, so I had a drink with him instead. But I don't know if there's CCTV in there."
    ron "We'll leave the corroboration and the CCTV ones blank for now."
    #Player must click on [Location of suspect] which will fill with 'The diner'. Then [Name of person suspect was with], with 'Terry'.
    ron "Saturday?"
    #Sprite L- Danny (Awkward)
    dan "Terry again. He took me into the forest behind his pa's farm. Terry likes to hunt, but my ma' made the forest a protected space, so he can't. But he likes to… play-act at hunting. So I basically trailed after him for half the night."
    mar "You… you LARPed being a hunter?"
    dan "Yeah. It was not fun. But no CCTV out there."
    #Player must click on [Location of suspect] which will fill with 'The forest'. Then [Name of person suspect was with], with 'Terry'. Then the [Yes/No] box for the ‘Should there be CCTV or…' will fill with 'No'.
    ron "Okay, that's the alibis done. Now we do the relationships— How are you with your mom?"
    dan "We're pretty close. She's a good ma'."
    #Player needs to click on [Answer] for the 'Relationship with Emily Sawyer according to suspect' question. It will fill in with 'Mother—good relationship.'
    ron "Alright, what about Norman?"
    #Sprite L- Danny (Moody)
    dan "After all he put my ma' through, I ain't exactly a fan of his. He's a bastard."
    #Player needs to click on [Answer] for the 'Relationship with Norman Conlee according to suspect' question. It will fill in with 'Unfriendly.'
    ron "What about Terry?"
    #Sprite L- Danny (Thoughtful)
    dan "I guess to be concise about it… we are awkward friends."
    #Player needs to click on [Answer] for the 'Relationship with Terry Maddux according to suspect' question. It will fill in with 'Awkward Friends.'
    ron "And Mrs. Pear?"
    dan "Don't really know her well enough to hold a real opinion. She's just the senile old librarian."
    #Player needs to click on [Answer] for the 'Relationship with Sandra Pear according to suspect' question. It will fill in with 'Doesn't really know her.'
    #Sprite L- Danny (Neutral)
    dan "Can't we do the rest later?"
    ron "Sure. We also need to ask the others these questions. And we need to work out what order the attacks happened in. Why don't we go back out and see what we can find?"
    #FADE OUT


    #[D1] [S8]- Marley has got an excellent idea
    #FADE IN
    #Location- The streets of Kingston
    #Sprite R- Marley (Thoughtful)
    #Sprite L- Danny (Neutral)
    #Bottom Sprite- Ron (Neutral)
    mar "Why don't we go check out where the corpses came from—I'm guessing the graveyard?"
    "Oh no."
    #Bottom Sprite- Ron (Awkward)
    ron "Uh that ain't necessary."
    mar "Oh I'm sure it'll be useful. The summoner must have gone there to raise the ghouls. Where is it, Danny?"
    dan "This way."
    "I can feel my gut twisting as Danny heads down the street, Marley following close after. I search frantically for an excuse, but none come to my head so I sheepishly trail after the pair."
    ron "We really don't have to—"
    dan "For once, I agree with Maddy—"
    mar "Marley."
    dan "Whatever. It's part of the crime scene."
    "Why can't they just drop it?"
    ron "Sure, but I bet many people trample through there every day. Any evidence will be long gone."
    dan "Actually they closed it off after the attack last night. Don't reckon anyone's been here since them dead was risen."
    "Shoot."
    dan "Anyway, we're here now."


    #[D1] [S9]- First look at the graveyard
    #FADE IN
    #CG- Ron, Marley and Danny standing on the perimeter of a church yard, complete with graveyard. The earth by several graves has been disturbed, as if they were dug up and hastily put back. One of the biggest tomb stones looks relatively new and has zinnia flowers in front of it in a fancy vase. The whole thing is surrounded by police tape.
    mar "Come on—"
    ron "I don't think that's, uh… the… the best use of- of our time at, uh… this point."
    mar "Oh don't be silly—"
    "She tries to drag me underneath the police tape perimeter, but I stand firm. She looks at me, annoyed, then turns to look out over the graves. I don't follow her gaze. Just stare stubbornly at the ground at my feet."
    mar "Those are nice flowers—zinnia flowers."
    "???" "Something here you don’t want to see, detective?"
    ron "What? No, of course not!"
    mar "Yes they are!"
    dan "Uh… she’s right, Ron…"
    "???" "Avoiding something, are we?"
    ron "You don’t know what you’re taking about!"
    mar "I’m a Witch, Ron! Plants are kind of our thing! Look, stop being such a tosser."
    dan "Hey, don’t talk to him like that!"
    "Jesus, it’s that damn voice again! I’m actually going crazy; I need to get out of here!"
    ron "Maybe you should remember who's the boss and who's the assistant, Marley. Now, come on. Let’s go."
    "Marley looks at me with confusion and hurt in her eyes. I didn't want to snap at her like that, but… but I'm not ready to make my way between those graves yet."
    "Danny looks triumphant."
    dan "I couldn't agree more, Ron!"
    mar "Oh shut it, you little weasel!"
    "I turn and start walking away from the graveyard. After a second, Marley and Danny follow."
    #FADE OUT


    #[D1] [S10]- Let's talk about Danny
    #FADE IN
    #Location- The streets of Kingston
    #Sprite R- Marley (Moody)
    #Sprite L- Danny (Moody)
    #Bottom Sprite- Ron (Worried)
    dan "You can't call me names!"
    mar "Just watch me, you human embodiment of a loose toenail!"
    "That voice, I'd heard that voice again! Taunting me! Did… did it know…"
    dan "Oh you’re just jealous!"
    mar "Of what? You're the one that's been acting like an insecure lead cheerleader from a cliché high school film!"
    "Something's wrong here… something deeper than ghouls attacking buildings. I can feel it."
    dan "Oh why don't you buzz off back to England?"
    mar "Oh you'd like that, wouldn't you?"
    "And why won't these two shut the hell up?"
    mar "I'm not blind. I know you're dying for me to bugger off and leave you all alone with—"
    ron "Shut it, both of you!"
    "The pair awkwardly fall silent."
    ron "This is an investigation; I'm not having the two of you following me around squabbling like children!"
    #Sprite L- Danny (Awkward)
    dan "Sorry, Ron."
    "Marley doesn't apologize. Just stares at me stubbornly. She looks mad."
    #Bottom Sprite- Ron (Tired)
    ron "*Sigh* Why don't you do me a favor, Danny?"
    #Sprite L- Danny (Smiling)
    dan "Sure, Ron. Whatever you need!"
    "I need something—anything—to make him scram."
    ron "Why don't you check in with Terry about tonight's patrol? Get an idea of the route and who's going to be there, or anything else that’s useful."
    "Anything to get him to go!"
    dan "Sure, whatever I can do to help!"
    #Sprite L leaves
    "For a second, Marley just keeps staring at me. Not angry anymore. Just… thinking. Calculating. Then, finally, she speaks."
    #Sprite R- Marley (Serious)
    mar "Don't you think you should have told me about that?"
    "I know what she's talking about. But… I don't want to."
    #Bottom Sprite- Ron (Awkward)
    ron "Told you about what?"
    mar "Don't play dumb with me Ronald-bloody-Kitzinger, or I will shout about Danny's crush on you so loud that the whole town will hear."
    #Bottom Sprite- Ron (Blushing)
    ron "Don't you dare!"
    #Bottom Sprite- Ron (Awkward)
    ron "*Sigh* And it's not a crush. Not really."
    mar "No. You're right. It's worse than that!"
    #Bottom Sprite- Ron (Moody)
    ron "Now you're just being dramatic."
    mar "He's like an overprotective guard dog!"
    ron "He doesn't like change. Or… strong personalities."
    #Bottom Sprite- Ron (Tired)
    ron "I would have thought he would have got over it by now."
    #Sprite R- Marley (Thoughtful)
    mar "When did this all start?"
    ron "When we were still at school. It was awkward as hell—I was oblivious at first."
    #Sprite R- Marley (Neutral)
    mar "You? Oblivious? Never."
    ron "Yeah, yeah. Well, he was my best friend back then. And I told him I was gay before anyone else."
    #Bottom Sprite- Ron (Awkward)
    ron "And I also told him I had a crush on someone in our grade."
    mar "And Danny thought you meant him?"
    ron "Exactly. I told Danny I had this big idea to ask my 'mystery man' out. Poor old Danny upped his advances, until even I couldn't mistake them. I finally put two and two together. Realized he was sweet on me and thought I was sweet on him."
    #Sprite R- Marley (Curious)
    mar "So how did he take it when you broke the news?"
    ron "Uh… well, um… about that…"
    #Sprite R- Marley (Worried)
    mar "Ron…"
    ron "I didn't! I never acknowledged it. Just ignored it and hoped it would go away."
    #Sprite R- Marley (Tired)
    mar "Ron!"
    ron "He found out it wasn't him eventually. The day I left. But that was nearly ten years ago! I thought he would have got over it by now."
    #Sprite R- Marley (Moody)
    mar "He didn't, Ron! He absolutely did not!"
    #Bottom Sprite- Ron (Tired)
    ron "Listen, Danny—he's harmless. If you give him a talking to when he's been too much of a pest, he'll back down."
    mar "This is a flaw of yours, Ron. You never deal with problems."
    ron "I'm a detective! My job is to solve problems!"
    mar "Other people's problems. You always run away from your own."
    "I try desperately not to think of the graveyard I'd insisted we leave."
    #Bottom Sprite- Ron (Awkward)
    ron "What, me? When have I ever—"
    #Sprite R- Marley (Moody)
    mar "The office gets like ten different completely useless magazine subscriptions because you couldn't get yourself together and cancel them!"
    ron "It's not that I can’t get myself together! It's that they make it so difficult—"
    mar "The sink in your apartment has been blocked sink since the day you moved in, but you keep putting off telling your landlord."
    ron "You try telling a six-foot-five half-troll that you need him to do some DIY!"
    mar "One time you almost married that siren lady so she could get a green card! The only reason you didn't was because I pretended to be your secret wife that you thought had died! She still sends us anniversary cards!"
    ron "Look, when there's no monster to slay or criminal to catch, problems get… complicated."
    mar "No kidding, Ron! That's why they're called problems!"
    #Bottom Sprite- Ron (Serious)
    ron "Look, can you just promise me you're not going to get involved? You can scare him into backing down if he gets too…"
    #Sprite R- Marley (Serious)
    mar "Too much like a possessive teen obsessed with their ex?"
    ron "If he gets too much, you're welcome to… get him to back off. In that charming way of yours."
    #Sprite R- Marley (Smiling)
    mar "I am charming."
    ron "But don't talk about this whole… crush mess. Promise?"
    #Sprite R- Marley (Moody)
    mar "Shocking as it may seem, Ron, I have no burning desire to fix your screw-ups."
    ron "Say that you promise!"
    mar "I promise, I promise!"
    ron "Good."
    mar "Now can we please get back to some actual work?"
    #Bottom Sprite- Ron (Neutral)
    ron "Great idea. We've got these suspect files to fill in. Where should we head to first?"
    #MAP
    #The map comes up. There are the four unlocked locations, as well as a button in one corner that says 'Go strait to the patrol.' All these scenes are optional
    #Library-			[D1] [S11a] [Optional]- First proper interview of Seb
    #Mayor's office-		[D1] [511b] [Optional]- Mrs. Pear or Emily?
    #Sheriff's office-		[D1] [511c] [Optional]- Norman or Terry?
    #Go straight to patrol-	[D1] [512]- Patrolling with Terry


    #[D1] [S11a] [Optional]- First proper interview of Seb
    #FADE IN
    #Location- Library
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "You got the suspect files?"
    mar "Yep. Ready to fill them in."
    ron "Good. Mrs. Pear works here, and this was attacked one night—course, we don't know which one. Let's see if we can find some evidence to narrow it down."
    ron "The mayor said it was night three, Saturday. Terry said it was Friday, and Mrs. Pear herself said it was Thursday."
    #SFX- Footsteps
    #Sprite R- Seb (Blushing)
    seb "Ron."
    #Bottom Sprite- Ron (Blushing)
    ron "Seb!"
    #Sprite L- Marley (Thoughtful)
    mar "Ooh, so this is the infamous Seb."
    #Bottom Sprite- Ron (Awkward)
    ron "Yeah… Marley, meet Seb. Seb, this is my assistant, Marley, whose job is to say absolutely nothing and take notes."
    #Sprite L- Marley (Laughing)
    mar "Hehehe."
    #Sprite L- Marley (Neutral)
    #Sprite R- Seb (Neutral)
    seb "If you're looking for Mrs. Pear, she left early today."
    #Bottom Sprite- Ron (Thoughtful)
    ron "I thought she was the only librarian—how can she leave?"
    seb "Oh, I'm an official volunteer here. I'm not really meant to be left alone, but I told her I didn't mind. She's not as spry as she used to be, of course. So she often heads home early and leaves me to close up."
    #Sprite R- Seb (Sad)
    seb "Not that anyone notices. It's always so quite round here."
    ron "Oh."
    "Well… I don't think Seb is the summoner. But I suppose we should make a suspect file for him. Just to be thorough and prove that he didn't do it."
    #Bottom Sprite- Ron (Neutral)
    ron "Well I guess I need to talk to you anyway."
    #Sprite R- Seb (Smiling)
    seb "'Need to'?"
    #Bottom Sprite- Ron (Blushing)
    ron "Uh… you know… for- for the investigation."
    seb "I see."
    "Focus! Focus, man!"
    #Bottom Sprite- Ron (Awkward)
    ron "Okay, first question, um… well, uh, there's been some disagreement about the order of these… dangerous attacks. That were done by… people."
    #Sprite R- Seb (Confused)
    seb "Uh… yes… yes, that's what I thought…"
    "So smooth, Ron."
    ron "You have any idea of the order?"
    #Sprite R- Seb (Awkward)
    seb "I'm afraid not. I haven't played much attention. And things have been kept under pretty tight wraps."
    #Bottom Sprite- Ron (Thoughtful)
    ron "Not even the day the library was attacked? 'Cos Mrs. Pear said it was Thursday, the sheriff said it was Friday, and the mayor said it was Saturday."
    seb "Ah. Well, I don't know about Friday or Saturday, but I'm sure it wasn’t Thursday."
    #Bottom Sprite- Ron (Curious)
    ron "Really?"
    #Sprite R- Seb (Sad)
    seb "Poor old Mrs. Pear had a bit of a funny turn Thursday, so I sent her home, said I'd lock up. I ended up staying late, 'till about midnight, alone in the library, grading papers. If I'm here, I don’t have to spend money on lights and the aircon in my apartment."
    #Fill in section 1.1 of Seb's suspect file
    #Bottom Sprite- Ron (Thoughtful)
    ron "So I wonder why she said it was Thursday."
    seb "She's not as young as she used to be, especially recently. Think her mind is going a bit."
    "So it looks like the library was not attacked on Thursday. Good to know. Now I need to ask the questions for the form. It's long, though. I probably can't ask all the questions, maybe one from each section. What should I ask?"
    #Option 1	Option 2
    ron "What about Friday? Where were you Friday night?"
    ron "Well then, what can you tell be about Saturday night?"
    #Fill in section 1.2 of Seb's suspect file
    #Fill in section 1.3 of Seb's suspect file

    #{Go to [D1] [S11a] [O1]}
    #{Go to [D1] [S11a] [O2]}



    #[D1] [S11a] [O1]
    #Location- Library
    #Sprite R- Seb (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "What about Friday? Where were you Friday night?"
    #Sprite R- Seb (Thoughtful)
    seb "Uh, Friday, let me think… There's this new coffee shop near my flat. It's open late. I went there to check it out."
    ron "Where is it?"
    seb "Sycamore Street. Not far from my family's restaurant."
    ron "Did you go with anyone?"
    #Sprite R- Seb (Awkward)
    seb "No."
    ron "Okay. Any idea if the place has CCTV?"
    #Sprite R- Seb (Thoughtful)
    seb "I doubt it. Place looked pretty new but not entirely finished and not that well-funded. But I don't know."
    ron "Okay then. Thanks."
    #Go to [D1] [S11a] [C1]


    #[D1] [S11a] [O2]
    #Location- Library
    #Sprite R- Seb (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "Well then, what can you tell be about Saturday night?"
    #Sprite R- Seb (Thoughtful)
    seb "Saturday—yesterday. Stayed home all day, graded some exams."
    ron "Alone?"
    seb "Uh huh."
    ron "Do you have any security footage in or around your place?"
    seb "Nope."
    ron "Okay, thank you."
    #Go to [D1] [S11a] [C1]


    #[D1] [S11a] [C1]
    #Location- Library
    #Sprite R- Seb (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    "Okay, that's one alibi got. Let's ask him about another suspect. But which one?"
    #Option 1	Option 2	Option 3	Option 4
    ron "So, you've got a pretty good friendship with Mrs. Pear, right?"
    ron "You remember Terry, right? He's the sheriff now, as I'm sure you know. What do you think of him?"
    ron "You ever see Danny's ma', Emily, around?"
    ron "You ever met Norman Conlee? The mayor's secretary—well, ex-secretary."
    #Fill in section 2.4.1 of Seb's suspect file and 2.5.2 section of Mrs. Pear’s.
    #Fill in section 2.3.1 of Seb's suspect file and 2.X.2 section of Terry’s.
    #Fill in section 2.1.1 of Seb's suspect file and 2.1.2 section of Emily's
    #Fill in section 2.2.1 of Seb's suspect file and 2.2.2 section of Norman’s.

    #{Go to [D1] [S11a] [C2] [O1]}
    #{Go to [D1] [S11a] [C2] [O2]}
    #{Go to [D1] [S11a] [C2] [O3]}
    #{Go to [D1] [S11a] [C2] [O4]}



    #[D1] [S11a] [C2] [O1]
    #Location- Library
    #Sprite R- Seb (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "So, you've got a pretty good friendship with Mrs. Pear, right?"
    #Sprite R- Seb (Smiling)
    seb "Yeah, she's really nice. She must be ancient to be honest. But she keeps going, and thank God she does. Besides the mayor and me, she's the only one who cares about the library. Without Mrs. Pear, it would be closed."
    ron "If you could sum up your relationship with her in one sentence, what would it be?"
    #Sprite R- Seb (Thoughtful)
    seb "We’re friends, and I have a lot of respect for her, but I also try to look out for her."
    ron "Great, thanks."
    #Go to [D1] [S11a] [C3]


    #[D1] [S11a] [C2] [O2]
    #Location- Library
    #Sprite R- Seb (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "You remember Terry, right? He's the sheriff now, as I'm sure you know. What do you think of him?"
    #Sprite R- Seb (Moody)
    seb "Yeah, I remember the jerk. Hard to forget him. Especially now that he's got that darned job. I mean, I do my best to avoid the law ’round here in general, but him especially. Haven't had anything much to do with them."
    seb "But from what I've heard, he's a pretty rubbish sheriff."
    ron "If you could sum up your relationship with him in one sentence, what would it be?"
    #Sprite R- Seb (Thoughtful)
    seb "I try to avoid him, and I don't think much of him."
    ron "Cool, thank you."
    #Go to [D1] [S11a] [C3]


    #[D1] [S11a] [C2] [O3]
    #Location- Library
    #Sprite R- Seb (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "You ever see Danny's ma', Emily, around?"
    seb "Yeah, sometimes. She comes into the library now and then—probably the most frequent visitor after myself. I know she wants to renovate it; she’s asked me for my ideas."
    seb "She also gave more funding to the school, and because of her, they started new clubs, which the principal has all made my responsibility. We’ve now got a creative writing club and a GSA, along with a few others."
    "Oh yeah, I read about that in the newspaper column."
    seb "She's pretty nice compared to some of the folks around here. A few months back, some of the parents and my colleagues at the school wanted to get me fired. Something about 'the gay half-elf corrupting their kids.'"
    seb "The principal was happy to do it. He's very much a 'do anything to keep the peace' type. But the mayor heard about it and stepped in. Said she'd get him removed if he listened to those idiots."
    seb "I think this was more of her sticking to her morals and not screwing up her image than helping me out specifically, but still. We're not exactly friends, but she looks out for me. She really tries to make the town better in general."
    seb "So I like her—in a distant kinda way."
    ron "Can you sum up your relationship with her in one sentence?"
    #Sprite R- Seb (Thoughtful)
    seb "She's a vague friend who I think is a good person, and I owe her one."
    ron "That's perfect, thank you."
    #Go to [D1] [S11a] [C3]


    #[D1] [S11a] [C2] [O4]
    #Location- Library
    #Sprite R- Seb (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "You ever met Norman Conlee? The mayor's secretary—well, ex-secretary."
    #Sprite R- Seb (Awkward)
    seb "Yeah, kinda. I mean, it's a small town. People know people around here. And he's got a reputation for being a cantankerous crap-head. And sometimes, if he's had too much to drink and sees me going by, he makes his opinion on elves and half-elves very clear."
    ron "Could you sum up how you feel about him in one sentence?"
    #Sprite R- Seb (Thoughtful)
    seb "We don’t like each other; I avoid him."
    ron "Cool, thank you."
    #Go to [D1] [S11a] [C3]


    #[D1] [S11a] [C3]
    #Location- Library
    #Sprite R- Seb (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    "Okay, great. I think the last thing to ask about is the last time he was at the various crime scenes."
    ron "Okay, one last set of questions."
    seb "Sure—hit me with 'em."
    #Option 1	Option 2	Option 3
    ron "When was the last time you were at the library before the attack? Was it Thursday? You mentioned that earlier."
    ron "When was the last time you were in or near the mayor's office?"
    ron "When was the last time you were in or near the sheriff's office?"
    #Fill in section 3.1 of Seb's suspect file.	Fill in section 3.2 of Seb's suspect file.	Fill in section 3.3 of Seb's suspect file.
    #{Go to [D1] [S11a] [C4] [O1]}
    #{Go to [D1] [S11a] [C4] [O2]}
    #{Go to [D1] [S11a] [C4] [O3]}



    #[D1] [S11a] [C4] [O1]
    #Location- Library
    #Sprite R- Seb (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "When was the last time you were at the library before the attack? Was it Thursday? You mentioned that earlier."
    #Sprite R- Seb (Thoughtful)
    seb "Umm, no. It would have been Friday. Just after school. Needed to return a book."
    ron "What time would this have been, then?"
    seb "School ends at 3, and it takes me about half an hour to get organized and get out of there. But the library is right next door. So, I guess it would have been approximately 3:35."
    ron "Anything happen while you were there?"
    seb "Mrs. Pear was busy, so I went behind her desk to scan through the book’s return myself, shelved it, went to chat with her, then left for my parent's restaurant to help prepare for dinner."
    ron "And before you left, did anything odd happen?"
    #Sprite R- Seb (Sad)
    seb "Yeah, Mrs. Pear was having one of her funny turns. She was in the occult section. I think she was meant to be checking stock and comparing it to what we’re supposed to have."
    "The occult section—that's the section that was attacked."
    seb "But she was muttering to herself kinda frantically. Cursing about every missing book. And when she saw me, she demanded to know if I'd been doing magic. I hadn't, of course. But it was like she didn't even know who I was."
    seb "I made her a cup of sweet tea and got her to calm down eventually. Convinced her to close early and go rest. Then I left as she was getting ready to go."
    #Bottom Sprite- Ron (Sad)
    ron "Oh no. Poor Mrs. Pear. Has she ever done anything else like this?"
    #Sprite R- Seb (Awkward)
    seb "She gets a bit paranoid about things. Sees monsters in every shadow."
    #Bottom Sprite- Ron (Thoughtful)
    ron "I see… That's useful to know. Thank you for telling me."
    #Go to [D1] [S11a] [C5]


    #[D1] [S11a] [C4] [O2]
    #Location- Library
    #Sprite R- Seb (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "When was the last time you were in or near the mayor's office?"
    #Sprite R- Seb (Thoughtful)
    seb "The mayor’s office, huh? I think that would have been… Wednesday. So, four days ago."
    #Bottom Sprite- Ron (Thoughtful)
    ron "So the day before the first attack?"
    seb "Yeah. Emily asked for a meeting—she'd asked me to report on how the clubs she's funding for the school are doing. We were meant to meet up Thursday, because I was helping at my dad's restaurant after work on Wednesday."
    seb "But then at lunch on Wednesday, she called me and said she was going to end up working late today, so asked if I'd mind coming to talk to her when we closed the restaurant. I said sure."
    ron "And what time was this?"
    seb "Ten o'clock."
    "Ah, there was a meeting in the mayors diary on Wednesday at 10 with 'S.' It must have been Seb."
    #Bottom Sprite Ron (Neutral)
    ron "So what happened?"
    seb "She forgot about it, apparently—I ran into her outside. Think she was just heading back into the office. We were both pretty tired, so we just had a quick talk. Then Danny arrived to see her, so I left them to it and headed home."
    ron "I see. So besides meeting outside, was there anything odd happening? With her, with the building, or in the area?"
    seb "Hmm… Emily seemed a bit distracted. Happy distracted—like she'd just had some good news. But when I asked, she said it was nothing and she'd just seen some 'funny karma.' I didn't wanna pry."
    ron "Nothing else odd?"
    seb "Nope."
    ron "Alright."
    #Go to [D1] [S11a] [C5]


    #[D1] [S11a] [C4] [O3]
    #Location- Library
    #Sprite R- Seb (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "When was the last time you were in or near the sheriff's office?"
    #Sprite R- Seb (Thoughtful)
    seb "The sheriff’s office, hm? Let me think… probably Tuesday. Last Tuesday—the seventh."
    ron "Why were you there?"
    #Sprite R- Seb (Awkward)
    seb "Uh… I was… I was reporting a crime, I think."
    #Bottom Sprite- Ron (Confused)
    ron "You think?"
    #Sprite R- Seb (Confused)
    seb "I don't remember. It was a while ago."
    ron "It was last week!"
    seb "It was a busy week."
    "What the hell?"
    ron "What were you reporting?"
    seb "I dunno—I guess it wasn't that important."
    "… Okay. Let's see if he can answer any questions for the file."
    #Bottom Sprite- Ron (Curious)
    ron "What time was this?"
    seb "7:30, I think. Around then. Before school. I went in, talked to someone—can't remember who—then left."
    #Bottom Sprite- Ron (Worried)
    ron "You haven't hit your head or anything, have you?"
    seb "No, no. Nothing like that."
    ron "Hmm. Did you notice anything odd?"
    #Sprite R- Seb (Thoughtful)
    "Seb pauses for a second, looking like he's thinking hard."
    seb "I think… I think I heard arguing. Pretty sure it was Terry and… someone. Not sure who, it was in another room."
    "So he remembers some overheard yelling, but not what he was reporting to the cops?"
    ron "Did you hear what they were arguing about?"
    seb "No, it was all muffled through the walls, so I didn't really hear many individual words… I mean there was one or two, I think. Pretty sure I heard the word 'snooping' from Terry. Then I think whoever he was arguing with called him 'unfit.'"
    "He remembers all that, but not why he was there? What the hell?"
    ron "Do you go there often?"
    seb "Oh God no. I try an avoid it when I can. Not a fan of walking into Terry's lair."
    ron "Well, uh… okay."
    #Go to [D1] [S11a] [C5]


    #[D1] [S11a] [C5]
    #Location- Library
    #Sprite R- Seb (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "Thank you for the information. It'll all be very useful."
    #Sprite R- Seb (Smiling)
    seb "I'm glad I could help! Good luck finding the vandals."
    ron "Thanks."
    "I give him an awkward smile. Gosh, he's mighty fine to look at."
    "But I don't have time to gawk at his face all day."
    #Bottom Sprite- Ron (Serious)
    ron "Eh hem. Thank you for your time. We've got to get going."
    seb "I understand. I guess I'll, uh… see you round, Ron."
    #Bottom Sprite- Ron (Blushing)
    ron "Not- not if I s-see you first."
    seb "Hehe."
    #Sprite R leaves
    #Sprite L- Marley (Laughing)
    mar "*Giggles*"
    #Bottom Sprite- Ron (Moody)
    ron "Don't."
    mar "Was… was that flirting, Ron? With that hot half-elf guy? Because it was painful to watch."
    ron "Ugh. Come on."
    mar "Well, some things in this case are starting to make sense."
    #GO TO MAP


    #[D1] [S11b] [Optional]- Mrs. Pear or Emily?
    #FADE IN
    #Location- Mayor's office
    #Sprite R- Mrs. Pear (Worried)
    #Sprite M- Emily (Smiling)
    #Bottom Sprite- Ron (Neutral)
    "As we approach the open door of the mayor’s office, we hear Emily chatting with a familiar voice."
    p "I just don't want you to get hurt again."
    e "Oh, you worry too much, Sandra. I'm not dating the man. Just going on… business dinners."
    p "Listen hon’, if this is about them library renovations, just let it go! I'm quite happy with it the way it is, and I'm sure the visitors are too."
    #Sprite M- Emily (Neutral)
    e "What visitors?! No one ever goes there except a handful of moms with their kids and Marianna's son!"
    #Sprite L- Mrs. Pear (Serious)
    p "Well, exactly—don't go wasting money on somethin' the community don't never use!"
    #Sprite M- Emily (Moody)
    e "Don't you think that maybe the reason the community don't use it is 'cos of the building? As in, the main thing I want renovated?"
    p "Don't be silly—"
    e "There haven’t been any renovations to the structure since it was built! It's as old as the town!"
    p "Oh come now—"
    e "It has no aircon, a leaky roof, and the plumbing spends more time blocked than unblocked!"
    #Sprite M- Emily (Worried)
    e "Come on Sandra, stop your frettin' about me! I can deal with Mr. high-an'-mighty. I'm determined to make this town better than it was when I came into office."
    e "And I'm gonna do that by fixin' up the library, no matter how many times he an' his council get in my way!"
    #SFX- Two steps of footsteps
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    #Sprite M- Emily (Surprised)
    e "Oh, Ron! Miss Marley! I didn't see you there!"
    #Sprite M- Emily (Neutral)
    ron "Good afternoon, ladies."
    e "How can we help you?"
    ron "Well actually, I was wondering if I could have a word with…"
    "Oh crap, I don't have time to interview both of them. I need to pick one to talk to—but which?"
    #Option 1	Option 2
    #Emily. With the drama between her and that assistant of hers we saw, I'm sure she's got some interesting secrets up her sleeve.	Mrs. Pear. There's something about the library attack that feels off to me.
    #Go to [D1] [S11b] [Emily]
    #Go to [D1] [S11b] [Mrs. Pear]



    #[D1] [S11b] [Emily]
    #Location- Mayor's office
    #Sprite R- Mrs. Pear (Neutral)
    #Sprite M- Emily (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "… Emily."
    p "Well I'll leave y'all to it. I need to head off anyway—got things to do."
    e "Okay, Sandra. Take care."
    #Sprite R leaves.
    #Sprite M- Emily (Smiling)
    e "So, what can I do for you two?"
    ron "I was wondering if I could ask you some questions?"
    e "Sure, go ahead."
    "Okay, I want to find out where she was at each time of attack, but there seems to be some confusion about which day the mayor’s office was hit. She said it was Friday, but Mrs. Pear and Terry disagreed."
    "Maybe I should ask about Saturday—her diary didn't have much to say about that day, and that's when Mrs. Pear said the mayor’s office was struck."
    ron "What were you doing Saturday, during the attack?"
    e "Working late, as usual. I'd met with Terry earlier that day to discuss rising crime rates, but that idiot was no help. So, I was trying to come up with a proposal to tackle the problem."
    e "But coming up with a solution that pleases our old-fashioned town council, involves Terry as little as possible, and actually works seems pretty much impossible. I worked until about ten, but I didn't have much luck."
    ron "I see."
    "Mrs. Pear had said that the mayor's office was attacked Saturday. But if Emily's telling the truth, it couldn't have been…"
    ron "Thank you, Mayor Sawyer. Was anyone with you during this time? Your assistant? Or… ex-assistant?"
    #Sprite M- Emily (Curious)
    e "Oh wait wait wait— You're trying to get my alibi, aren't you?"
    #Bottom Sprite- Ron (Awkward)
    ron "Uh… yes. I apologize ma'am, but it's protocol—"
    #Sprite M- Emily (Smiling)
    e "Oh good Lord, that's so exciting! I've never been asked to give an alibi before! This is so fun!"
    #Bottom Sprite- Ron (Confused)
    ron "Uh…"
    "You know that was absolutely not the reaction I was expecting. Not a reaction I've ever seen before."

    #Add in if player has gone through [D1] [S11c] [Norman]
    "It seems like everyone is happy I’m investigating the mayor. Including the mayor herself. Norman only cooperated when I said she was a suspect… but I don't think he realized she'd be so excited about it…"

    #Continuing
    e "Oh it's just like a real investigation!"
    ron "Ma'am… this is a real investigation."
    e "THIS IS SO COOL!"
    ron "…"
    #Bottom Sprite- Ron (Serious)
    ron "And do you actually have an alibi?"
    #Sprite M- Emily (Awkward)
    e "Oh, uh… no. No, I don't."
    #Sprite M- Emily (Moody)
    e "I worked alone that night—Norman never worked a full shift in his entire career here, let alone worked late."
    #Bottom Sprite- Ron (Neutral)
    #Sprite M- Emily (Neutral)
    ron "I see. Okay, next question—"
    "I want to get a sense of different relationships she has with the people of the town, but I don’t have time to do this all at once. Who should I ask about?"
    #Option 1	Option 2	Option 3	Option 4	Option 5
    ron "Do you remember Seb Daley? He went to school with me and Danny."
    ron "You and your ex-assistant seem to have some pretty bad blood. Could you tell us a bit about that?"
    ron "You mentioned earlier that you met with Terry recently. I get the sense that there ain't love lost between the two of you?"
    ron "So you and Mrs. Pear seem to be on good terms, is that right?"
    ron "You and Danny are still pretty close, huh?"
    #Fill in section 2.1.1 of Emily's suspect file and 2.1.2 section of Seb's.
    #Fill in section 2.2.1 of Emily's suspect file and 2.1.2 section of Norman's.
    #Fill in section 2.3.1 of Emily's suspect file and ___ section of Terry's.
    #Fill in section 2.4.1 of Emily's suspect file and 2.1.2 section of Mrs. Pear's.	Fill in section 2.5.1 of Emily's suspect file and 2.1.2 section of Danny's.

    #{Go to [D1] [S11b] [Emily] [O1]}
    #{Go to [D1] [S11b] [Emily] [O2]}
    #{Go to [D1] [S11b] [Emily] [O3]}
    #{Go to [D1] [S11b] [Emily] [O4]}
    #{Go to [D1] [S11b] [Emily] [O5]}


    #[D1] [S11b] [Emily] [O1]
    #Location- Mayor's office
    #Sprite M- Emily (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "Do you remember Seb Daley? He went to school with me and Danny."
    e "Sure, I know Seb. I used to be good friends with his ma'. A real nice woman. And Seb—well, he's done her proud."
    ron "So you're friends with him?"
    e "In a vague sorta way. I see him at the library a lot. He helps out Mrs. Pear, which is mighty good of him. Kingston could do with more folk like him."
    #Bottom Sprite- Ron (Curious)
    ron "'Like him' as in with a similar personality or as in not entirely human?"
    #Sprite M- Emily (Smiling)
    e "Both! Diversity always makes a community stronger."
    #Bottom Sprite- Ron (Thoughtful)
    ron "If you could describe your relationship with Seb in one sentence, what would it be?"
    #Sprite M- Emily (Thoughtful)
    e "I guess I'd say, 'He's a friend an' a mighty fine citizen of Kingston.'"
    #Bottom Sprite- Ron (Neutral)
    ron "That's perfect."
    #Go to [D1] [S11b] [Emily] [C1]


    #[D1] [S11b] [Emily] [O2]
    #Location- Mayor's office
    #Sprite M- Emily (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "You and your ex-assistant seem to have some pretty bad blood. Could you tell us a bit about that?"
    #Sprite M- Emily (Moody)
    e "Ugh. Norman. He's an internet troll come to life."
    #Bottom Sprite- Ron (Thoughtful)
    ron "So why'd he work for you so long? I mean, I heard he got the job as a favor to his dad, but Norman seems like he was actively making life difficult for you."
    #Sprite M- Emily (Awkward)
    e "Well, uh…honestly, the whole 'Norman' situation was a rather… complex affair. Politics usually ends up that way."
    ron "I see…"
    "I do not see. If it's so 'complex,' why is she free to fire him now? Maybe she isn't, but has finally been pushed far enough to say, 'damn the consequences'?"
    #Bottom Sprite- Ron (Neutral)
    ron "I wonder if you could sum up your relationship and how you feel about him in one sentence?"
    #Sprite M- Emily (Moody)
    e "I'd say 'hated ex- colleague' does the job quite nicely."
    ron "Then that's what we'll put down."
    #Go to [D1] [S11b] [Emily] [C1]


    #[D1] [S11b] [Emily] [O3]
    #Location- Mayor's office
    #Sprite M- Emily (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "You mentioned earlier that you met with Terry recently. I get the sense that there ain't love lost between the two of you?"
    #Sprite M- Emily (Moody)
    e "Humph. Terry. What did I ever do to deserve a moron like that for a sheriff?"
    ron "You ain't a fan of his then?"
    e "No. It's ridiculous he ever got that job in the first place. An' I still remember what he was like in school with you and Danny when y'all were youngins. I don't figure he's changed much."
    ron "But as mayor, you’ve gotta work with him? That must be hard."
    e "Ain't it just. He doesn't do real work, he doesn't care about people, he's rude—all in all, he's a pain in my ass."
    #Bottom Sprite- Ron (Thoughtful)
    ron "Then how'd he get the job—is it an elected position?"
    e "No, most of the sheriff gigs in other towns around here are, but 'cos Kingston's a lot older than the other towns in the area, it's got this special founding document that lays out certain legislation."
    e "The front page of it is on display in the town hall, but whole thing is pretty important."
    ron "Yeah, I remember doing a semester on that in high school—we all had to learn a passage of it off by heart."
    #Sprite M- Emily (Smiling)
    e "Oh, that brings back memories."
    #Bottom Sprite- Ron (Awkward)
    ron "I'm afraid I wasn’t the best student in that class."
    e "Well, to give you a reminder—in the original founding document, it states that a mayoral election is held every five years and a mayor can run for re-election as any times as they want. The same is true for the town council."
    #Sprite M- Emily (Serious)
    e "But the sheriff is selected by the council. And although we're a part of Texas, the citizens chose to go by the original laws, not those of the state."
    #Bottom Sprite- Ron (Thoughtful)
    ron "So the town council picked Terry. But why?"
    "Emily shrugs."
    e "Madduxes."
    ron "Hm. Well, if you could describe your relationship with and feelings towards Terry in one sentence, what would it be?"
    #Sprite M- Emily (Moody)
    e "An egotistical, misogynistic, rude pain in my ass."
    #Bottom Sprite- Ron (Thoughtful)
    ron "I don't think I can disagree with any of that."
    #Go to [D1] [S11b] [Emily] [C1]


    #[D1] [S11b] [Emily] [O4]
    #Location- Mayor's office
    #Sprite M- Emily (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "So you and Mrs. Pear seem to be on good terms, is that right?"
    #Sprite M- Emily (Smiling)
    e "Oh yes, Sandra. She and I go way back—I knew her when I was a kid."
    ron "Yeah, I remember her working at the library when I was young. I'm amazed she's still with us."
    e "Oh she's a tough old bird. Honestly, she's helped keep me sane through all this."
    #Bottom Sprite- Ron (Thoughtful)
    ron "If you could sum up your relationship and feelings towards her in one sentence, what would it be?"
    #Sprite M- Emily (Thoughtful)
    e "She's a good friend and a good woman."
    ron "I see."
    #Go to [D1] [S11b] [Emily] [C1]


    #[D1] [S11b] [Emily] [O5]
    #Location- Mayor's office
    #Sprite M- Emily (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "You and Danny are still pretty close, huh?"
    #Sprite M- Emily (Smiling)
    e "Oh yes, I'm very close with my little Danny-boo."
    #Sprite L- Marley (Laughing)
    e "Before we moved back here, when we were in Austen, poor Danny didn't make many friends. He was a very shy boy. So he and I, we were all each other had. We got real close and have been ever since."
    #Sprite L- Marley (Neutral)
    ron "If you could sum up your relationship with Danny in one sentence, what would it be?"
    e "The best son a woman could ask for."
    #Bottom Sprite- Ron (Smiling)
    ron "Well that's real sweet, Ms. Sawyer."
    #Go to [D1] [S11b] [Emily] [C1]


    #[D1] [S11b] [Emily] [C1]
    #Location- Mayor's office
    #Sprite M- Emily (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "Thank you. Now, I’ve got one last set of questions for you, Emily."
    e "Sure, go ahead."
    "Now, this is the part where I ask about the last time she at one of the crime scenes before it was attacked. But one of the crime scenes was here, and she's here every day, so her answer would depend on which day it was attacked."
    "And there's some confusion about that. I'll ask about one of the others."
    #Option 1	Option 2
    ron "So the sheriff's office was one of the places that was attacked, right? When was the last time you were there? Before the attack I mean."
    ron "Do you visit the library often, Mayor Sawyer?"
    #Fill in section 3.1 of Emily's suspect file
    #Fill in section 3.2 of Emily's suspect file

    #{Go to [D1] [S11b] [Emily] [C2] [O1]}
    #{Go to [D1] [S11b] [Emily] [C2] [O2]}



    #[D1] [S11b] [Emily] [C2] [O1]
    #Location- Mayor's office
    #Sprite M- Emily (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "So the sheriff's office was one of the places that was attacked, right? When was the last time you were there? Before the attack I mean."
    #Sprite M- Emily (Thoughtful)
    e "The sheriff's office… honestly, I'm not in the habit of heading over there. I haven't had to report any crimes recently. And I ain't fond of socializing with Terry and his crew."
    "Didn't have a crime to report? What about that memo about money going missing from the treasury? Hasn't that been reported to the cops? That's odd…"
    "But I can't ask about that—I found it by snooping."
    #Bottom Sprite- Ron (Awkward)
    ron "You, uh… you haven't had any criminal issues around here?"
    e "No, not really. I suppose the last time I was there was… Tuesday, actually, but only briefly."
    #Bottom Sprite- Ron (Thoughtful)
    ron "Oh yeah? And what time was this?"
    e "12:30. I was asked to come in for a meeting with the deputy—Derek—but he cancelled at the last minute. I didn't see that before I left, though. So, I more or less got there, got told it was cancelled, and turned straight around."
    #Bottom Sprite- Ron (Curious)
    ron "Do you know what the meeting was meant to be about?"
    #Sprite M- Emily (Thoughtful)
    e "No, he never said, but he did say it was urgent. I figured maybe it was about how crime rates have been going up around here? That whole department knows I've been trying to crack down on it."
    e "I'm surprised he didn't reschedule the meeting. He was very cagey about it when I saw him—said that he might reschedule, that he'd get back to me at some point after Thursday."
    ron "I see. Besides that, did you notice anything odd?"
    e "I saw Terry there. He seemed pretty moody. He and Derek were snappish with each other."
    "Hm. Terry and Derek really ain't on good terms."
    #Go to [D1] [S11b] [Emily] [C3]


    #[D1] [S11b] [Emily] [C2] [O2]
    #Location- Mayor's office
    #Sprite M- Emily (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "Do you visit the library often, Mayor Sawyer?"
    e "The library? Yeah, sure, all the time."
    #Sprite M- Emily (Laughing)
    e "Well, uh, when I'm not at the office."
    #Sprite M- Emily (Serious)
    e "I'll be frank with you, Ron, I am a very determined woman. I set myself a goal. I achieve that goal. I did it when I got my degree. I did it when I decided to raise Danny on my own. I did it when I got elected."
    "Well, you can’t say she doesn’t follow through."
    e "And when I got this position, my goal became to make Kingston better. I want to focus on academics and culture. Improve the schools, increase funds and resources for the museum, improve the library."
    e "And, of course, now I have to focus on the rising crime rates, thanks to Terry doin' a pits-poor job."
    e "I've finished working on the school. The museum has the resources it needs and my Danny-boo is making sure its development is going smoothly. And I'll deal with Terry… somehow."
    e "But right now, I need to fix up the library. It's a key community resource. And that building—it's ancient. It's as old as the town! It started out as the manor house of one of the founding families, the Halls."
    e "The only building as old is Kingston High—that used to be the Madduxes' place. But that building has been renovated a bunch. The library, not so much. We need to bring it into the present. Need to show people its potential."
    e "It's going to happen. It needs to happen. No matter how many obstacles the darned town council puts in my way."
    e "So I've been drawing up plans for its renovation. That's mainly why I spend time there. That and… I like the calm. The solitude. Ironic, since that's what I'm trying to change. But yeah, I go there when I can."
    "She seems pretty passionate about this. I guess she really is serious about her goals."
    #Bottom Sprite- Ron (Thoughtful)
    ron "So when was the last time you went to the library? Before the attack there, I mean."
    #Sprite M- Emily (Thoughtful)
    e "That would have been… Thursday. Right before my meeting—"
    #Sprite M- Emily (Awkward)
    e "I mean, uh—"
    #Sprite M- Emily (Neutral)
    e "Right before I headed home for the day. Seb was there, but no Mrs. Pear. It was her I'd wanted to talk to, so I just said hi to Seb, looked around to check something for my plans, then left."
    ron "And what time would that have been?"
    #Sprite M- Emily (Thoughtful)
    e "Just before it closed, so… 6:50? It stays open real late."
    ron "And did you notice anything odd while you were there?"
    #Sprite M- Emily (Thoughtful)
    e "I guess, uh… Seb… he seemed distracted. Zoned out. I thought maybe he'd just taken some pain killers or something. But when I asked if he was okay, he sort of blinked a bunch, then seemed to come back to himself."
    #Bottom Sprite- Ron (Worried)
    ron "I see… I hope he's okay."
    #Go to [D1] [S11b] [Emily] [C3]


    #[D1] [S11b] [Emily] [C3]
    #Location- Mayor's office
    #Sprite M- Emily (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "Well, thank you for your time, Mayor Sawyer. You've been very helpful to our investigation."
    #Sprite M- Emily (Smiling)
    e "Well, I'm always happy to help! This is all mighty exciting!"
    ron "We'll let you get on with your work. We know you're very busy. I'll see out around."
    #FADE OUT
    #GO TO MAP


    #[D1] [S11b] [Mrs. Pear]
    #Location- Mayor's office
    #Sprite R- Mrs. Pear (Neutral)
    #Sprite M- Emily (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "… Mrs. Pear."
    p "Of course, dearies. I'd be happy to help."
    e "I was thinking of going on a walk to clear my head. You're welcome to use my office if it's privacy you want."
    #Bottom Sprite- Ron (Smiling)
    ron "Thank you, Mayor Sawyer. That'll be mighty useful."
    #Sprite M leaves
    #Sprite R- Mrs. Pear (Smiling)
    p "Now, how can I help you two? Oh, this must be about the ghoul attacks y'all are investigating, right?"
    ron "Indeed it is, ma'am. I wanted to ask you what you were doing on…"
    "Now, she said the attack on the library was Thursday. But Terry said it was Friday. And Emily said it was Saturday. And Mrs. Pear's mighty old, she could easily get confused."
    "Let's see if Mrs. Pear can remember what happened Saturday—the day Emily said the library was attacked."
    ron "…Saturday."
    #Sprite R- Mrs. Pear (Thoughtful)
    p "Saturday—you mean yesterday? Now let me think… well, I was at the library till it closed at seven. Then I… yes—I stayed late that day."
    #Bottom Sprite- Ron (Curious)
    ron "Oh yeah?"
    p "Yep. The ghouls had made such a mess two days before, that I was still working on cleaning it up. Left at… maybe ten?"
    "Hmm… Emily had said that the library was attacked Saturday. But if Mrs. Pear was working late that day… then it couldn't have been…"
    ron "Was anyone else there?"
    p "Afraid not, dearie. We're very understaffed at the moment—only me working there."
    #Fill in section 1.3 if Mrs. Pear's suspect file.
    #Bottom Sprite- Ron (Neutral)
    ron "Okay Mrs. Pear, next I'm going to ask about your relationship with…"
    "Hmm. Who should I ask about?"
    #Option 1	Option 2	Option 3	Option 4	Option 5
    ron "… Emily. Are you two close?"
    ron "… Terry. He's the new sheriff. Have you had any dealing with him?"
    ron "… Norman, Emily's old secretary. Did you ever meet him?"
    ron "… Seb. Does he regularly read at the library?"
    ron "… Danny. Emily's kid. If you know Emily quite well, do you know him too?"
    #Fill in section 2.1.1 of Mrs. Pear's suspect file and 2.4.2 section of Emily's.
    #Fill in section 2.3.1 of Mrs. Pear's suspect file and __ section of Terry's.
    #Fill in section 2.2.1 of Mrs. Pear's suspect file and 2.4.2 section of Norman's.
    #Fill in section 2.5.1 of Mrs. Pear's suspect file and 2.4.1 section of Seb's.
    #Fill in section 2.4.1 of Mrs. Pear's suspect file and 2.4.2 section of Danny's.

    #{Go to [D1] [S11b] [Mrs. Pear] [O1]}
    #{Go to [D1] [S11b] [Mrs. Pear] [O2]}
    #{Go to [D1] [S11b] [Mrs. Pear] [O3]}
    #{Go to [D1] [S11b] [Mrs. Pear] [O4]}
    #{Go to [D1] [S11b] [Mrs. Pear] [O5]}



    #[D1] [S11b] [Mrs. Pear] [O1]
    #Location- Mayor's office
    #Sprite R- Mrs. Pear (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "… Emily. Are you two close?"
    p "Oh yes, Emily's a mighty fine woman. And I can’t complain about her work as mayor. She's got new blood that the town needs."
    ron "I understand she's pretty controversial—I saw that column about her in the newspaper today."
    p "Well, some folk around these parts can be very stuck in their ways. Don't like her pro-LBGT stance, how she's changin' up the school, and how she got Kingston’s woods declared a protected space."
    p "But others think she's taking steps in the right direction. To be honest, a lot of folks were plumb tired of the way the place used to run."
    #Bottom Sprite- Ron (Thoughtful)
    ron "But still… she's been mayor for how long?"
    #Sprite R- Mrs. Pear (Thoughtful)
    p "Well she was elected in 2008, so… fourteen years."
    ron "So that's three elections she's won. For such a controversial politician, that's amazing!"
    #Sprite R- Mrs. Pear (Neutral)
    p "I don't think she's as controversial as she seems. The people who ain't fond of her ain't afraid to make it know—they always cause a ruckus. The people that like her tend to stay quiet."
    p "So it seems like more hate than like her, but I reckon it's the other way ’round. Anyway, I'm mighty fond of her. She reminds me of myself at her age—strong willed. Determined."
    #Bottom Sprite- Ron (Neutral)
    ron "If you could describe your relationship with her in one sentence, what would it be?"
    #Sprite R- Mrs. Pear (Thoughtful)
    p "She's a good person who I try my best to help when I can."
    ron "That'll do nicely."
    #Go to [D1] [S11b] [Mrs. Pear] [C1]

    #[D1] [S11b] [Mrs. Pear] [O2]
    #Location- Mayor's office
    #Sprite R- Mrs. Pear (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "… Terry. He's the new sheriff. Have you had any dealing with him?"
    #Sprite R- Mrs. Pear (Moody)
    p "Idiot boy. Those darned Madduxes are a curse on this town, and Terry's no different! Only one worse is his father."
    #Bottom Sprite- Ron (Thoughtful)
    ron "So you ain't a fan of the sheriff?"
    p "No, I am most certainly not! And he don't deserve that badge of his. He's a disgrace to this town."
    ron "Do you see him around much? Talk to him ever?"
    p "Sure—I've had some things I've tried to report to him in the past, but he won’t listen. Thinks I'm crazy!"
    #Bottom Sprite- Ron (Curious)
    ron "You've been reporting things to him? What kind of things?"
    #Sprite R- Mrs. Pear (Awkward)
    p "I… I don't wanna say."
    #Bottom Sprite- Ron (Confused)
    ron "What? Why not?"
    p "You'll think I'm crazy too, just like everyone else around here."
    "Well that sounds important!"
    ron "I swear I won't, Mrs. Pear. I’ll take anything you tell me very seriously."
    p "Well… sometimes… sometimes I hear things. At night. Howls."
    ron "Ain't… ain't this coyote country? They howl—"
    #Sprite R- Mrs. Pear (Moody)
    p "No! No, this is different! You ain't listening!"
    ron "Then… then what is it, Mrs. Pear?"
    p "Beasts. Beasts that ain't… ain't natural."
    ron "What do you mean?"
    #Sprite R- Mrs. Pear (Serious)
    p "I mean that young Seb Daley ain't the only not-fully-human individual in these parts!"
    "For God’s sake, why is this woman being so cryptic?!"
    p "An' that's all I'm gonna say on the matter."
    #Bottom Sprite- Ron (Moody)
    ron "Why? Why won't you explain properly?"
    p "Ain't you a fancy detective man? Detect!"
    #Sprite R- Mrs. Pear (Neutral)
    p "Now, to your actual question—"
    "I grind my teeth in frustration."
    p "I ain't fond of Terry Maddux. He’s not my choice in sheriff."
    ron "I… I guess I'll put that down."
    #Go to [D1] [S11b] [Mrs. Pear] [C1]


    #[D1] [S11b] [Mrs. Pear] [O3]
    #Location- Mayor's office
    #Sprite R- Mrs. Pear (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "… Norman, Emily's old secretary. Did you ever meet him?"
    #Sprite R- Mrs. Pear (Moody)
    p "Yeah, I've had the displeasure of meetin' him a few times when I came in to visit Emily. Foul little man."
    ron "Yes, he seems like an… interesting fella."
    p "He calls me 'crazy old bat.' He doesn't even have the decency to whisper it, just says it outright. That man should’ve had his hide tanned more when he was a boy!"
    #Bottom Sprite- Ron (Thoughtful)
    ron "Any idea why he got the job? Being the mayor’s assistant is a pretty good gig, right? How come he got it?"
    #Sprite R- Mrs. Pear (Thoughtful)
    p "Lord knows. I suppose… well, the pair of 'em have an interesting history, I guess."
    #Bottom Sprite- Ron (Curious)
    ron "Wait, what? What do you mean?"
    #Sprite R- Mrs. Pear (Awkward)
    p "Uh, well, it ain't really my business. I’m not gonna gossip about Emily and her affairs."
    ron "But that could be important!"
    #Sprite R- Mrs. Pear (Serious)
    p "I won’t talk behind my friend’s back. If you wanna know about that, I suggest you ask Emily about it. Now, you wanted to ask about Norman, right?"
    "No! I want to know about this past between Emily and Norman!"
    "But I can tell by the look in her eyes that I ain't gonna get another word out of her on that subject."
    #Bottom Sprite- Ron (Moody)
    ron "Fine. Could you sum up your feelings towards Norman in one sentence?"
    #Sprite R- Mrs. Pear (Moody)
    p "As far as I can tell, Norman is a grade-A prick with less use than dog feces."
    #Bottom Sprite- Ron (Thoughtful)
    ron "Well that certainly is decisive."
    #Go to [D1] [S11b] [Mrs. Pear] [C1]


    #[D1] [S11b] [Mrs. Pear] [O4]
    #Location- Mayor's office
    #Sprite R- Mrs. Pear (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "… Seb. Does he regularly read at the library?"
    #Sprite R- Mrs. Pear (Smiling)
    p "Ah, Seb. Such a good boy. I really don't know where I'd be without him."
    #Sprite L- Marley (Thoughtful)
    mar "I'm surprised you're so fond of him. You made it very clear that you don't like magic, and Seb is a half-elf, a born sorcerer."
    #Sprite R- Mrs. Pear (Neutral)
    p "Well sure, but Seb don't never use his magic. He sees that it's dangerous and steers well clear. Very sensible."
    "She gives Marley a look."
    #Sprite R- Mrs. Pear (Serious)
    p "Some people would do well to follow his example."
    #Sprite L- Marley (Moody)
    mar "Uh huh."
    "Marley doesn't look impressed at Mrs. Pears passive aggressive digs."
    #Bottom Sprite- Ron (Serious)
    ron "I know that he, Danny, an' me visited the library a bunch when we were young. I'm guessing he just… never stopped coming?"
    #Sprite R- Mrs. Pear (Neutral)
    p "Uh huh. Then he became an official library volunteer—the only one that the library has. He comes by after school, before his pa's restaurant opens up."
    #Bottom Sprite- Ron (Thoughtful)
    ron "Keeps himself busy, don't he?"
    p "Idle hands do the devil’s work, Mr. Kitzinger."
    #Bottom Sprite- Ron (Confused)
    ron "Uh… they… they sure do…"
    #Bottom Sprite- Ron (Serious)
    ron "Would you sum up your feelings towards Seb in one sentence, please?"
    p "He's a kind boy and he helps this old bat out quite a lot."
    ron "Alrighty then."
    #Go to [D1] [S11b] [Mrs. Pear] [C1]


    #[D1] [S11b] [Mrs. Pear] [O5]
    #Location- Mayor's office
    #Sprite R- Mrs. Pear (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "… Danny. Emily's kid. If you know Emily quite well, do you know him too?"
    #Sprite R- Mrs. Pear (Thoughtful)
    p "Danny…"
    mar "Yeah. Danny. Light skin, dark hair, green eyes. Annoying little blockhead."
    #Bottom Sprite- Ron (Moody)
    ron "Marley!"
    #Sprite R- Mrs. Pear (Neutral)
    p "Oh, I know who he is. Emily yaps on about her precious baby boy whenever she gets the chance. But I don’t really interact with him much myself. Before today, when he came by with you, the last time I really spoke to him was when he was a boy."
    p "Back when you, him, and Seb came to the library every day after school so you could avoid your folks."
    #Bottom Sprite- Ron (Awkward)
    #Sprite L- Marley (Curious)
    ron "Wha- I, uh… I don't, uh…"
    #Sprite R- Mrs. Pear (Serious)
    p "I might be old, but I ain't stupid, Ron. I know you didn’t get on with your folks. So you spent as much time away from there as you could. And Seb and Mr. Sawyer stayed with you to keep you company."
    ron "…"
    #Bottom Sprite- Ron (Serious)
    ron "Could you please describe your relationship with Danny in one sentence?"
    #Sprite R- Mrs. Pear (Thoughtful)
    p "He's the son of a friend. Nothing more."
    ron "Alrighty then."
    #Go to [D1] [S11b] [Mrs. Pear] [C1]


    #[D1] [S11b] [Mrs. Pear] [C1]
    #Location- Mayor's office
    #Sprite R- Mrs. Pear (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "Thank you for that, Mrs. Pear. You've been very helpful."
    p "I do my best."
    ron "I have one last set of questions for you."
    p "Go ahead."
    "I want to know when she was last at each scene. But she's one of the people disagreeing about the order of attacks… so her answer would depend on when she thinks each place was attacked."
    "Maybe I'll ask about either the mayors or the sheriff's office and save questions about the library for after I figure out which day it was attacked."
    "But which place should I ask about?"
    #Option 1	Option 2
    ron "So one of the places that was attacked was the sheriff’s office. Can I ask when you visited it last?"
    ron "Obviously the ghouls left this place in a bit of a state. When was the last time you visited before it was attacked?"
    #Fill in section 3.1 of Mrs. Pear's suspect file
    #Fill in section 3.2 of Mrs. Pear's suspect file

    #{Go to [D1] [S11b] [Mrs. Pear] [C1] [O1]}
    #{Go to [D1] [S11b] [Mrs. Pear] [C1] [O2]}



    #[D1] [S11b] [Mrs. Pear] [C2] [O1]
    #Location- Mayor's office
    #Sprite R- Mrs. Pear (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "So one of the places that was attacked was the sheriff's office. Can I ask when you visited it last?"
    #Sprite R- Mrs. Pear (Thoughtful)
    p "The sheriff's office, huh? Hmm, let me think…"
    #Sprite R- Mrs. Pear (Neutral)
    p "Why I reckon that would have been Tuesday, during my lunch, I had a meeting at 12:30."
    #Bottom Sprite- Ron (Curious)
    ron "Why were you there?"
    p "That nice deputy—Derek, I think his name was—he asked me to come in."
    ron "Oh? Why?"
    #Sprite R- Mrs. Pear (Thoughtful)
    p "He was doin' some project—something about the town’s history. He wanted to ask me a few questions about it."
    ron "The town’s history?"
    p "Yes. Lord knows what it had to do with his job."
    ron "What did he want to know?"
    #Sprite R- Mrs. Pear (Awkward)
    p "Honestly, I can't remember the details. But it got me all confused—I don't think I was any help to him. I left after five minutes."
    #Bottom Sprite- Ron (Thoughtful)
    ron "You can't remember any of the questions?"
    p "I'm afraid not. My memory ain't what it used to be."
    ron "Well, uh- did you notice anything odd while you were there?"
    #Sprite R- Mrs. Pear (Thoughtful)
    p "Hmm… Terry weren’t there. I thought that was odd, since he was sheriff an' all. And I overheard the folks there talking about him. I don't think they like him much."
    ron "Can you remember what people said specifically?"
    p "Well Derek, he- he said that Terry was… dirty. A dirty cop. Hid stuff—I dunno. I didn't really understand it."
    ron "I see."
    #Go to [D1] [S11b] [Mrs. Pear] [C3]


    #[D1] [S11b] [Mrs. Pear] [C2] [O2]
    #Location- Mayor's office
    #Sprite R- Mrs. Pear (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "Obviously the ghouls left this place in a bit of a state. When was the last time you visited before it was attacked?"
    #Sprite R- Mrs. Pear (Thoughtful)
    p "Uh, let me think… I suppose the last time I visited before the attack would have been… Monday. On my lunch break. I came round here, then Emily and I went to grab lunch."
    ron "And when was that?"
    p "Maybe ten past noon?"
    ron "And did anything particular happen?"
    #Sprite R- Mrs. Pear (Thoughtful)
    p "I went in, waited a few minutes for Emily to finish what she was doing, then we left."
    ron "And did you notice anything odd?"
    p "Well… that creepy assistant of hers—he seemed smug. Pleased with himself. And Emily seemed angry. Snapped at him on the way out."
    ron "I see."
    #Go to [D1] [S11b] [Mrs. Pear] [C3]

    #[D1] [S11b] [Mrs. Pear] [C3]
    #Location- Mayor's office
    #Sprite R- Mrs. Pear (Neutral)
    #Sprite L- Marley (Neutral)
    #Bottom Sprite- Ron (Neutral)
    ron "Thank you, Mrs. Pear. This will be very useful."
    #SFX- Knock knock
    e "Hello? Is it okay for me to come back in?"
    ron "Yes, Mayor Sawyer. We're done here."
    #SFX- Door opens
    #Sprite M- Emily (Smiling)
    e "How did it go?"
    ron "Good. We've got some interesting stuff."
    e "Oh, I'm so glad! Is there anything else I can do to help?"
    ron "Not for now. We've got other things we need to do before nightfall."
    #Sprite M- Emily (Sad)
    e "So you… you don't want to interrogate me, then?"
    "Does… does she look disappointed?!"
    #Bottom Sprite- Ron (Awkward)
    ron "Umm… I'm sure I'll have time to question you at some point, mayor. Now, we need to go. I'll see you around."
    #FADE OUT
    #GO TO MAP    

