

label welcomeToKingston:
    # [D1] [S2]- Welcome to Kingston
    scene bg kingston_streets 
    show marley smile at right
    with fade
    # Location- Street in Kingston
    # SFX- Town noises, crows cawing
    mar "So this is the place that raised you."
    ron awkward "Shut it, Mar."
    mar "Jeez, you look as if someone just stole all your candy!"
    ron "I don't like this town, Mar..."
    show danny smile at left with dissolve
    dan "Ron! Hiya buddy! It's great to see you again!"
    ron neutral "Hey Danny. It's great to see you too. You remember my friend, Marley Shipway, don't you?"
    mar "Hiya!"
    dan "Uh... sure, yeah. Hi Marry."
    show marley moody with dissolve
    mar "Um, actually, it's—"
    show danny smile at left with dissolve
    dan "I've missed you so much, Ron!"
    ron "Yeah. Missed you too."
    dan "Why don't I take your bags? You must be exhausted after all that travel."
    ron smile "Oh that's kind of you!"
    "I pass him my suitcase. And he immediately presses it into Mar's hands."
    show marley angry with dissolve
    mar "Hey!"
    show danny serious with dissolve
    dan "Well, you are his assistant, aren't you? Assist!"
    "Same old Danny."
    mar "Why you little—"
    show danny smile with dissolve
    dan "Why don't I give you a tour around town, Ron? Help you re-familiarize yourself."
    ron awkward "Uh... good idea."
    "Before Marley teleports him into a river."
    dan "Where shall we head to first?"
    # MAP
    # Only the research locations will be unlocked-
    # -	[D1] [S3a]- Laptop (Danny's house) 
    # -	[D1] [S3b]- Books (Library)
    # -	[D1] [S3c]- Old birth/death records and family trees (Town Hall)
    # -	[D1] [S3d]- Arrest records (Sheriff's office)
    # -	[D1] [S3e]- Old Maddux stories (Kingston High)
    # -	[D1] [S3f]- Recent birth/death records (Hospital)
    # -	[D1] [S3g]- Historic political stuff, old maps (Museum)
    # -	[D1] [S3h]- Once all options on the map have been explored, go to Danny's house

label thisIsAComputer:
    # [D1] [S3a]- This is a computer
    # Location- Ron's office (Computer)
    scene bg rons_office
    show marley neutral at right
    show danny smile at left
    with fade
    dan "This is my place—feel free to use my computer for any research! Try it! Click on the search box and type in a question. What about 'The History of Kingston'?"
    #Player must type 'History of Kingston' into the search bar and press the search button. A Wikipedia-style article will come up
    "Kingston, TX"
    "A small town in eastern Texas, USA, Kingston is one of the oldest in the area."
    "Kingston was founded in 1673 by Terence Maddux. He and his fellow settlers came over from England on a ship called 'The Conquest.' Maddux had been tasked, by England's Grand Wizard Nathan Pulsifer, to settle in that territory specifically. Pulsifer foresaw that an English settlement in the area would have great importance in any battle over the land."
    "To protect the settlers from hostile Indigenous Peoples and Spaniards, Pulsifer gave Maddux five special pillars, named 'The Protective Pillars of Kingston,' which Pulsifer carved from sacred birch wood and inscribed with protective runes. Once Maddux and his people made their way to the specified area, they planted the five posts around the perimeter of the settlement. Maddux anointed the tops with his own blood. The pillars remained in place for 321 years. They prevented any who wished harm on the people that resided within those pillars from passing through the town's perimeter. Thus, Kingston soon began a healthy trade with the Indigenous Peoples in the area while the Spanish settlers remained entirely unaware of the town's existence. When they finally noticed the town in 1820, their hold over the area was slipping too much for them to strike."

    "Kingston has a colorful set of local legends, including stories of a chaotic Witch who wanted to bring the people of Kingston to their knees. This legend has been added to by the fact that Kingston has been the site of many interesting crimes, and"
    # The rest of the page is cut off
    # Once the player clicks, the following conversation is triggered-
    dan "Come on, there's lots more to see!"
    show marley moody with dissolve
    mar "These bags are so heavy!"
    # RETURN TO MAP

label libraryShelves:
    # [D1] [S3b]- Books!
    # Location- The library (Shelves)
    scene bg library
    show marley smile at right
    show danny neutral at left
    with fade
    dan "Here's the library."
    mar "Ooh, I love a good library!"
    dan "Then you're going to be disappointed. This library is tiny and seriously underfunded. But we've got a few interesting books! Feel free to flick through some—like that one there."
    # Player must pick the book available on the first page of shelves- the book is called 'Local Wildlife of Kingston, Texas'.

    # The book opens to the following page:
    "The Mexican Grey Wolf"
    "I had an interesting internal debate as to whether to include the Mexican Grey Wolf in this book. Officially, the wolf has not been seen in the area since 1970. However, several more recent reports have claimed sighting these majestic beasts in the Kingston area. None have been confirmed, and no photographic evidence has been found, but these intriguing wolves are a personal interest of mine, so I shall include them."
    "These animals are small for wolves and typically have a narrow skull and dark pelt. If you come across a wolf, any wolf, remember that these are not dogs, despite any outward resemblance. They need to be treated with the upmost respect at all times. They are not your friendly puppy."
    # The page cannot be turned. When the player clicks, the following dialogue will play
    dan "Come on; can't say in a musty old library all day."
    # RETURN TO MAP

label hospitalPC:
    # [D1] [S3c]- Breaking all the HIPPA rules
    # Location- The hospital (Desktop computer)
    scene bg hospital_pc
    show marley neutral at right
    show danny neutral at left
    with fade
    dan "This is the hospital computer. You can look up anyone from the town here. As long as they're alive, it'll have their medical records. Try it—look me up: Daniel Sawyer."
    # Player must type 'Daniel Sawyer' into the hospital search engine. A medical file will come up- see Danny.
    # Once the player clicks, the following conversation will play.
    mar "How'd you break your hand?"
    show danny moddy with dissolve
    dan "Mind your own business."
    show danny neutral with dissolve
    dan "Come on, Ron. More to see!"
    # RETURN TO MAP

label bigFilingCabinets:
    # [D1] [S3d]- Big Filing cabinets
    # Location- Town Hall (Old birth/death records)
    scene bg townhall_records
    show marley neutral at right
    show danny neutral at left
    with fade
    dan "These are the official historic records of the town. We keep them in the Town Hall. I doubt you'll need them—most of this stuff is about people who died ages ago, and it's only birth, death, and marriage records. But it might be useful."
    dan "Super old system though. It's all alphabetized by surname. You're probably in here. Why don't you look yourself up? Think ‘K' is in the second filing cabinet."
    # Player must click on the cabinet drawer labelled K-L. The drawer will open, with files containing various surnames beginning with K or L. There is a very large section on the Kitzingers.
    show marley thoughtful with dissolve
    mar "Wow, there's a lot of Kitzingers."
    ron "My ancestors were one of the town's founding families."
    # Player must click on the Kitzinger file. It opens to reveal a large file divided by the first letter of the first name.
    dan "I guess you'll be under 'R.'"
    # Player must click on the R section. It opens straight to Ron's file- Ronald Kitzinger
    # When player clicks the following dialogue plays
    mar "I didn't know you had siblings!"
    dan "Humph. You mustn't be a very good friend if you didn't know that."
    show marley moody with dissolve
    mar "What's your dang problem?"
    ron "Stop being a pain."
    show danny smile with dissolve
    dan "Yeah!"
    mar "He was talking to you, dumbutt!"
    show danny moody with dissolve
    "Jesus. Time to move on before fists start flying."
    ron "Cone on, let's get going. What's next on the tour, Danny?"
    # RETURN TO MAP

label moreRuleBreaking:
    # [D1] [S3e]- More rule breaking
    scene bg sherrifs_office # Location- Sheriff's office (Files)
    show marley neutral at right
    show danny smile at left
    with fade
    dan "We've got access to all the sheriff's records, but I'm afraid he's not very organized. I've asked for any records to do with people connected to the case, but so far, he's only got mine available. Not much there."
    # Player must click on Danny's file- Danny
    # When player clicks the following dialogue plays
    mar "Just a speeding ticket? That's all? Well, you've got a record cleaner than mine."
    ron neutral "It's true. I've had to bail her out twice."
    show danny moody with dissolve
    dan "What great company you keep, Ron. Come on."
    # RETURN TO MAP

label checkingOutDannysJob:
    # [D1] [S3f]- Checking out Danny's job
    # Location- Museum (Exhibits)
    scene bg museum_clean
    show marley neutral at right
    show danny smile at left
    with fade
    dan "This is the museum; it's where I work. I'll have to be here for shifts during some of your visit, but if you need me, Ron, I'll always be here."
    mar "Thanks—"
    dan "I was talking to Ron, Maisy."
    show marley moody with dissolve
    mar "Marley."
    dan "We're currently showing a display on how the town has changed over the years. I doubt it'll be much help, but it's kinda interesting."
    # Display the maps. After player has clicked through all, following dialogue will play.
    show marley curious with dissolve
    mar "What happened to that lake there?"
    ron neutral "They built a damn and turned it into a reservoir which they still call Mallory Lake. It's just further to the west."
    dan "Come on, we don't have all day."
    # RETURN TO MAP

label returningToHappyMemories:
    # [D1] [S3g]- Returning to happy memories
    # Location- School (Display)
    scene bg school_display
    show marley thoughtful at right
    show danny neutral at left
    with fade
    ron moody "Oh good. It's this place."
    mar "Is this where you went to school?"
    ron "Unfortunately. My own personal hell."
    dan "You're being a mite dramatic, Ron. Anyway, the kids have a display on the Madduxes up at the moment. You remember them, don't you?"
    ron "Unfortunately."
    mar "Not a fan of the family?"
    ron "Terry Maddux—the youngest in the family—he went to school with us. He was a bully, but the teachers let him get away with it because his family was such a big deal."
    dan "Oh come on, Terry wasn't that bad. Anyway, since the family founded the town, they have school projects on them a bunch. Why don't you look through this first one? There's some more, but I doubt they'll be useful."
    # When clicked on, TERENCE MADDUX DISPLAY will come up.
    # Once the display has been looked through and the player clicks, the following dialogue will play.
    ron "Come on. I have no interest in staring at this shrine to my old bully's great-great-grandpa. Or staying in this godforsaken place any longer."
    dan "It's gotten a lot better here recently. Mom got some interesting projects funded—"
    ron "Yes, yes, we get it, your mum is amazing. Now come on, let's get out of here."
    # RETURN TO MAP


label theFirstClues:
    # [D1] [S3h]- The first clues
    # FADE IN
    # Location- Ron's office
    scene bg rons_office
    show marley thoughtful at right
    show danny smile at left
    with fade
    dan "Home sweet home!"
    ron thoughtful "Wh- what the hell?"
    dan "Surprise!"
    ron "Wh- why does your spare room look like my office?"
    dan "I redecorated it to look like your place back in the city, to make you feel more at home!"
    ron "I- I don't remember you ever having been to our office."
    dan "No, haha. You never invited me. I had to do a bit of snooping on your social media!"
    mar "That's not creepy at all. Is that a papier-mâché bust of Ron?"
    ron "Well, uh... it's nice of you to go to all this trouble, Danny."
    dan "Any time! I just really want you to be comfortable here."
    ron "But didn't you get in trouble with your landlord? This must have required some serious renovations!"
    dan "I had to have the back wall completely redone. But mom smoothed it over with the landlord for me."
    mar "Uh-huh... um, anyway, why don't you tell us what's going on?"
    dan "If you need anything, you just let me know! I'm always happy to help in any way I can!"
    mar "Well, we 'need' you to tell us what's going on so we can solve the case, so—"
    dan "Anything at all, Ron. Anything you want. Don't hesitate to ask. No holds barred."
    show marley serious with dissolve
    mar "So what's happening—"
    dan "I can get you a TV in here, a coffee machine—"
    ron neutral "Uh... why don't you just tell us what's been going on, Danny?"
    show marley neutral
    show danny neutral
    with dissolve
    dan "Of course, Ron! Well, long story short, three places in town have been attacked over the last week: the mayor–my mom's–office, the library, and the sheriff's office."
    dan "I can't remember in what order. Anyway, luckily no one's been killed yet; the bastards only appear at night when there's not many people around."
    ron "Yeah, ghouls de-animate when the sun comes up."
    dan "Ahh. Well, they've caused quite a lot of damage."
    ron "Right. I'll need to have a look at the scenes."
    dan "Maybe you should also talk to Seb. You know, interrogate the prime suspect?"
    ron serious "Uh, no. Not just yet. It's too soon."
    dan "If you're sure."
    mar "Why do you think this Seb guy is behind it?"
    show danny moody with dissolve
    dan "Your secretary sure asks a lot of questions, don't she?"
    show marley angry with dissolve
    mar "Hey, what the hell?"
    ron angry "Knock it off, Danny. She's my assistant, a Witch, and a doggone good friend. So answer her question."
    dan "Fine. Well, Marie—"
    mar "Marley!"
    dan "I've checked out all the scenes–they've been left as they were after the attack for you to examine. And I've found things belonging to Seb at each place. Look—"
    show marley neutral
    show danny neutral
    with dissolve
    "He pulls out a plastic zipper bag from one of the desk's drawers and holds it out to me."
    "There are three objects in it."
    "Danny's Evidence"
    # The image is three things in a plastic bag. When you click on each, it gives you information. 
    "OBJECT 1"
    "Description- Hair the same colour as Seb's, tied up in a red ribbon"
    "Information given- \"A lock of purple hair tied up with a red bow. Seb's hair changed that color a few years back thanks to his elf's blood according to his Instachat...that I absolutely didn't stalk."
    "OBJECT 2"
    "Description- A knock off Pokémon looking card"
    "Information given- \"An old Pikiman card–a fancy Balaturtle. Seb got one back when he was collecting them in school."
    "OBJECT 3"
    "Description- A neckless with a pretty blue heart-shaped locket on it. When clicked, it opens to show an elf woman and a human man- Seb's parents."
    "Information given- \"A heart-shaped locket... My breath catches in my throat–this was his mother's locket. Or it had been hers, many, many years ago. I've never seen Seb take it off, not since the day she pressed it into his hand as he cried over her hospital bed."
    dan "They're all his, right?"
    ron thoughtful "Um. You found these all at the locations that were attacked?"
    dan "Uh-huh."
    ron "That's strange."
    show danny thoughtful with dissolve
    dan "What?"
    ron "Seb's a smart guy. You'd think he wouldn't leave such easily identifiable things at a crime scene. Part of the process to summon a ghoul is to give it an item that's important to you... an anchor—but surely he would have found a way to grab them back afterwards."
    show danny neutral with dissolve
    dan "I don't know. Anyway, we should start checking out the scenes before it gets too late—"
    show marley serious with dissolve
    mar "Not yet."
    show danny moody with dissolve
    dan "What? Why not, what's wrong?"
    mar "I need to meditate."
    dan "WHAT? What bullcrap is that?"
    mar "Again... I. Am. A. Witch. All my power relies on nature. And I don't know the nature here. I'm not in tune with it. To use my magic, I have to get in touch with nature each and every day."
    mar "I need access to my magic in all times during an investigation. So, before we do anything, I need to find somewhere to meditate."
    dan "Jesus. Not that amazing of a power set you got there if you have to mediate every day."
    "Marley looks Danny up and down, judgment in her eyes."
    mar "Maybe you should try it, Danny. Think it would really... benefit you. Fix your whole vibe."
    "I fight off a laugh as Marley turns and leaves before Danny can muster a comeback."
    hide marley
    show danny angry
    with dissolve
    dan "SON OF A-!"
    ron "You deserved that."
    show danny smile with dissolve
    dan "Listen, Ron—you know, we could just go without her. We've got lots to do that we don't need her weird magic for, like interrogating suspects—"
    show danny curious with dissolve
    dan "You got a strategy in mind for the questioning?"
    ron neutral "Same one I always do."
    dan "Yeah?"
    ron "Well, there are a few possible ways you may want a suspect to feel about you."
    ron "First, you can try and get them to trust and respect you as a professional. Be a peacemaker, seem smart and 'adult.' Be bold. Be honest. Straightforward." 
    ron "Make them trust in your competence; if they're innocent, they'll help you and feel safe around you. But, if they're guilty, seeming smart and competent will usually make them up their game... They might try and get rid of you."
    ron "Next, you can try to be their friend. You get on their good side, get them to want to help you. If they're innocent, they might go out of their way to lend a hand in the investigation–but, of course, the flip side is that this puts them in danger."
    ron "If they're guilty, sometimes it makes them drop their defenses, makes 'em slip up. But it can be dangerous–you think you're getting under their defenses, but really, they're getting under yours."
    ron "Then, finally, you can try and make 'em angry. That's the most dangerous one; even if they're innocent, the suspect might try and screw you up out of spite. They stonewall you. Although, I have known people who responded well when I tried to make them mad—liked the brutal honesty of it, I guess."
    ron "But in a case like this, ego is always involved, so if you make the guilty suspect angry, they'll take it to heart. They'll probably try to screw you over, but they'll also probably make mistakes—ones big enough to show themselves."
    show danny thoughtful with dissolve
    dan "I see. So ya' assess each suspect and pick the best technique?"
    ron smile "Exactly. None of the methods are wrong, but some are better than others depending on the situation. They'll each get different results. Every decision I make when talking to a suspect aims to make them feel a certain way about me. Everything I do is trying to get them to feel one of those ways."
    dan "That's very clever, Ron."
    ron "Thank you."
    show danny neutral with dissolve
    dan "Should we go?"
    ron serious "Nope. No, we wait for Marley."
    "I wonder how her meditation is going."

label theWolf:
    # [D1] [S4] [Optional]- The Wolf
    # FADE IN
    # SFX- Nature noises, crows
    scene bg cg_witch with fade
    "I follow nature's pull on my soul away from the tiny town. I head past some farms and find myself in thick woodland."
    "Perfect."
    "After a bit of walking, I find a small clearing and sit myself down. I close my eyes and focus on my breathing."
    # SFX- Deep breathing
    "With every breath in, the smell of flowers, the trees' bark, the rotting leaves, animals' musk all mix in my noise. A wonderful orchestra of scents."
    "Then the sounds—the leaves rustling through the trees. The cawing of the crows above."
    "Slowly, from deep in my gut, I can feel little tendrils of my magic reaching out, stretching like someone waking up after a long sleep."
    "It connects itself to the plants as they slowly push their roots deep into the ground, sucking up moisture, their leaves bathing in the delicious sun."
    "Connects to the creatures as they scurry around, chasing each other or hunting for food, and the crows in the branches high above me. I can feel them watch me curiously. Figuring out if I'm friend or foe. But knowing in their hearts that I am no ordinary mortal."
    "The forest around me feels like I'm home, even though I'm miles from Chicago. And even further away from where I was born."
    # SFX- loud twig snap
    "I open my eyes."
    scene bg cg_witch_wolf with dissolve
    "Normally only a powerful Witch could speak to an animal. But here, in this clearing, with my magic connected to everything around me, including the wolf—"
    mar "Hello sister."
    w "*Sniff* You are human."
    mar "I am."
    w "*Sniff sniff* But that's not all you are."
    mar "No. I am a Witch. A person who connects to nature for magical powers."
    w "Hm. Humans. Always chasing power like a pup chases a squirrel. Ignorant of or uncaring for whatever you trample under-paw in your never-ending hunt for your goal."
    "Well... she's not wrong. I can feel the anger and rage at humans, nestled deep in her lupine heart. Perhaps it's best I change the topic."
    "I'm surprised to see a wolf here at all—I did some research on the wildlife in this area on the way over—the wolves that once lived here were wiped out ages ago."
    mar "This must be lonely hunting for you, sister. Your pack must be the only one for many territories."
    w "I have not seen another of my kind since my brother went to the earth. When I join him, the great hunters will no longer roam this land. And, for that, I am grateful."
    "That surprises me. Wolves guard their territories fiercely, and nothing is more important to them then the continuation of their pack—their family. So why is this one so happy about her line's demise?"
    mar "Is this land so unkind to you, sister? The hunting's too meagre?"
    w "No, Witch. The prey is unending. But this is not the place for my kind. This pace is too full of the un-us."
    "The what?"
    mar "The... un-us?"
    w "Those that look like us, but are not us. The more you look, the more you see—they're short, with too-long limbs, too-silky hair, stretched out faces. Eyes to black. Glassy. Their words so garbled. A false reflection of us."
    w "They are beasts of humans—like their perverted cubs."
    "Oh, she must be talking about dogs."
    w "They infest the land, take over territories. And if you defeat one—then come the men with their explosion sticks. My pack used to curse the day our forefathers and mothers were tricked into building our den here."
    mar "'Tricked'? How do you mean 'tricked'?"
    w "That is a long story, witch. The story of my pack. You do not wish to hear so sad a history."
    "Like hell I don't."
    "But how do I get her to share it? She's very stiff. Formal. She doesn't trust me—I can't blame her for that. Should I be stiff and formal too? Show respect? Or try to be kind? Friendly?"
    menu wolfMenu:
        "It would be a great honor to hear your ancestor's story, sister. If you would do me the kindness of sharing it.":
            jump wolfRejectsYou # {Go to [D1] [S4] [O1]}

        "You've piqued my curiosity! Come, sit comfortably. I'm most intrigued, be a friend and tell me your tale.":
            # Add she-wolf to Marley's list of allies
            jump wolfAcceptsYou # {Go to [D1] [S4] [O2]}

label wolfRejectsYou: # [D1] [S4] [O1]
    "For a few minutes, the wolf considers me wearily, as if deciding whether to trust me."
    "Then she gives a thoughtful little huff."
    w "*Huff* Fine. If you are so curious, I will tell you. But watch that curiosity of yours, Witch. Many a sibling has followed their curiosity, only to have it ensnare them."
    "Well, that's something I can definitely relate to."
    mar "Thank you sister—your advice is good—I will remember it."
    w "Good. Here is my pack's story. Heed it well. It all began many years ago, when my mother's mother's mother was barely older than a cub. This is her story. She still lived with her parents and brethren. One day, they smelt another wolf in their territory."
    w "They tracked him down and found a male. But rather than fight, he begged them to listen to him. He spoke of the hardship his pack faced in their old territory—competing for food and hiding from humans and their fire sticks."
    w "He said that he knew a place where they would be safe and have plenty of prey. He offered to lead them there. My mother's mother's mother's father was very suspicious of this too-perfect promise."
    w "But my foremother... one look at this stranger, and she knew she would follow him to the ends of the earth. He was strong, but clever too—the cleverest wolf she had ever met. So, she begged her father to listen. And eventually, he agreed."
    w "The stranger eventually convinced three packs to follow him to this promised land. It was a long and painful journey—hiding by day, sneaking through the strange, busy human territories by night. It was terrifying."
    w "But over the journey, the stranger and my foremother fell in love and became mates. Eventually, the three packs reached this land. And at first, all seemed perfect. They prey was plentiful and easy to catch."
    w "Occasionally a wolf would be killed by one of the humans sticks, but it was rare enough that they could manage. For my foremother, life seemed like a dream. Her mate was sweet and kind and tough, and when they had pups, he was a wonderful father."
    w "Except for one thing: he was barley there during the time of the light while she slept. He usually returned soon after she woke to hunt, but when she woke during the middle of the light time, his side of the den was cold."
    w "And sometimes, when he was there, he'd be... different. None of that intelligent spark. More aggressive. Obsessed with the hunt. And then he wouldn't remember what happened during those times."
    w "So, one day, my foremother decided to follow him after the lighting of the sky to see where he went. It's hard to stalk a wolf like you'd stalk pray."
    w "She followed him through the shadows of the forest until they reached some land that the humans had grown tall metal bushes around, to keep creatures out. He went through a gap, and as she watched through the hedge, she saw the most terrible thing."
    w "As the light struck him, he began to change. He struggled and writhed, as if in pain, and his legs got longer, his face flattened. The pads of his paws distorted and stretched. His fur seemed to pull back into his body. Until there stood not her mate, but a human."
    w "He gathered some of the removable pelts you humans wear and walked off as my poor, foolish foremother tried to make sense of what she had seen. Eventually, after the creature had left, she gathered the energy to return to the woods."
    w "Although she wanted to crawl back into her den with her pups—his pups—and forget all that she had seen, she went out to the dens of all other packs in the forest. She gathered all the adult wolves that had once followed the not-wolf to this land."
    w "She told to them what she saw, and at first, they did not believe her. But they smelt her fear. Saw the horror in her eyes. And so they agreed to follow her and let her prove what she had seen."
    w "So, together, they went to the land where she had seen her mate's transformation and hid amongst the trees around the tall metal bushes. They waited all through the light time, until the safety of the darkness descended again, and they saw a human approach."
    w "A human who smelt of the wolf. They watched in horror as the man turned back into their brethren. But when he tried to leave the metal bushes enclosure, out stepped my foremother and the other wolves."
    w "They told him that if he dared show his face near any of their dens again, they would rip him apart. He was not a wolf and not their brother. The not-wolf begged them to listen, insisted that he was one of them, more one of them than one of the humans."
    w "But the wolves felt too deceived—they had trusted him, followed him far from their old dens—and he was not even a true wolf. He went to my foremother, asked for her to listen, to think of the love they shared—and the cubs."
    w "And she struck him. Bit deep into his neck until her mate's blood dribbled into her mouth. Terrified and heartbroken, he ripped himself free and fled. They never saw him again."
    w "As for my foremother—life was difficult, raising her pups alone. No other wolf would come near her pups if they could help it, for they were his pups too. Sometimes, as they grew, she'd wake during the light time and find the den empty."
    w "She'd go outside and there her pups would be, staring up at the moon's bright brother the same as she gazed at the moon. They were smart too, like their father. Often she'd find them too close to the human territories, watching them curiously."
    w "Of her five pups, only one found a mate, as most were too scared to go near them. And from the litters that came from that coupling, only one wolf reached adulthood, as the prey grew scarcer and the humans and their fire sticks crept into the woods more and more."
    w "And many of my blood fell to the allure of your people. And they were shot. And some just disappeared. The single surviving wolf of that line had only one litter—my litter."
    w "And of them, most have died or disappeared. The other packs have died out too. I am the last wolf left from the families the not-wolf brought here. And the last of his descendants."
    w "Although many generations have diluted his blood in my body, I still feel it—the lure of the moon's bright brother, the call of the humans and their strange above ground dens that reach as high as the trees."
    w "When my final hunt is over, my body given over for the scavengers to feast on, it gives me peace to know that no more of the not-wolf's children will walk this earth."
    w "Sometimes, at the height of the light-time, I think I can feel him. In my blood. My heart. Longing to stretch out my paws until they lengthen. Pull myself up on my hind legs and reach up a high as I can. To feel the wind on my bare skin, free from fur."
    w "It's wrong to want these things. Unnatural. That urge will die with me."
    "Finally, the wolf falls silent, giving me time to mull over her story. It sounds like, many years ago, her pack encountered... No. No, they couldn't have. They're an incredibly regulated group of people. No way one could live out here."
    "But... it is very isolated..."
    "Well, dogs can have vivid imaginations, maybe wolves can too. But I probably shouldn't tell her that. Remember—respectful."
    mar "Thank you for telling me your pack's story. I am sorry for the pain of your past."
    w "Remember the tale, Witch. Remember that the face a stranger shows can be a well-made lie. And you never know what's behind it."
    mar "Thank you, sister. I will not forget your advice."
    w "I need to go. The more time I spend in the light, the more I can feel the unnatural desire to... change."
    mar "Go in peace, sister. Regardless of your family's past, I wish you well. May your hunts be plentiful. May you always find fresh water. And when your time is done, may the earth accept your remains with open arms as you return to the Mother of all life."
    "The wolf cocks her head at me."
    w "What are these strange words you speak?"
    mar "It's an ancient Witch blessing."
    w "Oh. Well... thank you. The same to you... sister."
    # SFX- 	Deep breath
    #     Padding feet
    "As the she-wolf stands, I close my eyes and take another deep breath."
    "When I open them again, she is gone."
    jump theCharms # Go to[D1] [S5]- The Charms

label wolfAcceptsYou: # [D1] [S4] [O2]
    # CG doesn't change
    "To my dismay, the she-wolf just glares at me."
    w "My story is not for your amusement, Witch. It is not a tale to tell your cubs when they cannot sleep. It is a painful history!"
    "Crap—she's offended. Back track, back track!"
    mar "I'm sorry, sister. I did not mean to offend—"
    #SFX- Continuous low growling
    w "Do not call me sister. You may be a Witch, but you are still human."
    "Her words make my stomach knot, and my jaw clenches."
    mar "I know many humans who would disagree."
    w "I don't care how petty your kind are—they are all the same. And my kind learnt not to trust them eons ago."
    "Before I can open my mouth to argue, she stands, her tail low and stiff, her body tense. Then she turns and walks off into the forest."
    jump theCharms # Go to[D1] [S5]- The Charms

label theCharms: # [D1] [S5]- The Charms
    # FADE IN
    # Location- Ron's office
    scene bg rons_office
    show marley neutral at right
    show danny neutral at left
    with fade
    mar "I'm back!"
    show danny moody with dissolve
    dan "Great. Can we go now?"
    mar "Nope! Not yet."
    dan "Ugh, what now?"
    ron  neutral "We need to make charms!"
    show danny confused with dissolve
    dan "Charms?"
    "I watch as Marley grabs her box of beads."
    ron "Like I said, Marley's a Witch. Me and her are gonna make these special charms."
    show marley thoughtful with dissolve
    mar "We'll put one in each crime scene's possible entry points. You can't remove them unless you know this specific spell. Nothing under another's command will be able to pass through. It'll keep any ghouls out or trapped inside. How many should we make, Ron?"
    ron thoughtful "Police station, library, mayor's office—let's say fifteen to be sure."
    mar "Alright, can you thread the charms while I do the special hand movements?"
    ron smile "Sure thing."
    # Open Charm Making game
    # There are seven pots on the desk, each labelled-
    # -	Unicorn hair
    # -	Mermaid-harvested pearls 
    # -	Gilded fey tears
    # -	Wooden beads whittled by a wood-elf
    # -	Phoenix feather
    # -	Opals from a dwarven mine
    # -	Sprite-dragon bone
    mar "I have to do these special sacred hand movements over them to do the spell. You'll have to thread the charms in the order I tell you."
    ron "Sure thing!"
    mar "Click on each pot to open it."
    # Game will wait until each pot is open.
    mar "Perfect! Now pull out fifteen unicorn hairs."
    # Only clickable option will be the unicorn hair. Players have to click and drag each of the fifteen hairs out of the pot and onto the table.
    mar "Great! Next, you'll put the beads on them."
    mar "Start by tying a phoenix feather to one end of each of the hairs—that's what gives the spell its force."
    ron "I see, okay."
    # Only clickable option will be the phoenix feathers. Players will have to drag and drop the feathers to the hairs- when released close enough to the hair, it will knot its end around the feather.
    # Game will only move on when all fifteen feathers are attached.
    mar "Wonderful! Alright, next, we need to put an opal on each of the strings. Opals have a strong connection to the moon and will channel its energy into the charm. This will make ghouls more susceptible to the charm since they can only be animated at night. The opals already have holes in them, you just need to thread them."
    # Player has to click and drag each opal onto each charm.
    mar "Okay, next we need mermaid-harvested pearls."
    # Player has to click and drag each pearl onto each charm.
    mar "Next are the gilded tears—they work together with the pearls to channel the element of water. It'll give the charm longevity—these bad boys will made sure the charms will keep working for years to come."
    # Player has to click and drag each tear onto each charm.
    mar "Perfect! Okay, two more left—the wooden beads are next. These were carved by wood elves. They work as the sensor of the charm. This bead basically checks for ghouls. But, the eyes have to be uncovered or the charm won't work."
    # Player has to click and drag each carved bead onto each charm.
    mar "Nice! Right, nearly done—just tie the sprite-dragon bone to the end of each charm!"
    # Player has to click and drag each bone onto each charm.
    # Game closes
    ron "Done!"
    show marley smile with dissolve
    mar "Great! Any ghouls that try and pass under these bad boys will get barbecued!"
    show danny curious with dissolve
    dan "Can't the summoner just pull them down?"
    mar "Nope. The magic will keep them up—the only way to take this down is to spin the wooden bead counter-clockwise three times. Then it can be taken down."
    mar "Besides that, like I said, if the charm is covered, the eyes on that bead can't see. So, the charm will be useless until it's uncovered."
    show danny thoughtful with dissolve
    dan "I see."
    show marley smile with dissolve
    mar "So, Ron—first day of the investigation! What will be the first question?"
    show danny curious with dissolve
    dan "Huh? What do you mean?"
    mar "As part of our method for solving investigations like this, we divide the whole mystery into smaller, simple questions. If we try to answer at least one question each day, hopefully we can get a full picture of what's going on."
    dan "I see."
    ron thoughtful "Well Danny said that he can't remember the order of the attacks—let's figure those out first. Nice and easy. And let's get some alibis."
    mar "Good idea."
    ron "Okay, now that that's decided, we should get going."
    show danny smile with dissolve
    dan "Sure thing. Where shall we head first?"
    # MAP
    # The map comes up. Four locations are unlocked- The sheriff's office, the mayor's office, the library, and Ron's office. The first time they go to each place, they do choice a. The second time, they do the optional b one.
    # Mayor's office-		1	[D1] [S6a]- Mayor Emily Sawyer
    # 2	[D1] [S6b] [Optional]- Mayor Emily Sawyer 2
    # Sheriff's office-		1	[D1] [S6c]- Terry Maddux
    # 2	[D1] [S6d] [Optional]- Terry Maddux 2 
    # Library-			1	[D1] [S6e]- Mrs. Pear
    # 2	[D1] [S6f] [Optional]- Mrs. Pear 2
    # Ron's office- 		1	[D1] [S6g] [Optional]- Back at the office (short)
    # Once all non-optional map scenes have been played, go to [D1] [S7]- Discussing the evidence 

label mayorEmilySawyer:
    # [D1] [S6a]- Mayor Emily Sawyer
    # FADE IN
    scene bg mayors_office with fade
    # SFX- muffled arguing
    "As I head up to the Mayor's Office, I can hear angry voices coming from inside. One sounds like Emily—Danny's mom. Then someone I don't know, a man."
    "I reach for the door handle and start to pull it open."
    # SFX- Door opening
    show emily angry at right
    show norman angry at left
    with dissolve
    "???" "Well well well. Hello there. And who might you be?"
    "The voice is quiet, almost drowned out by the yelling. Barley more than a whisper. It sounds like it's simultaneously miles away and right in my ear. And my gut is telling me that whoever said that isn't part of the pair in the room."
    ron confused "Huh?"
    n "You're firing me, you soul-sucking DEMON?"
    e "Oh, this has been a long time coming, Norman, and you know it!"
    "As I gape at the mayor screaming at the strange man, all other thoughts fly out of my mind."
    n "You're reveling in this, aren't you?"
    "He waves a fistful of crumpled paper at her then throws it dramatically on the floor. It's like a scene from a soap opera come to life—one where I don't know the plot."
    e "Stop whining, you sniveling, little rat. You've lost. End of story."
    ron "Eh-hem. Uh, hello?"
    show emily shocked with dissolve
    e "Oh!"
    show emily smile with dissolve
    e "Oh my, is that Ronald Kitzinger I see?"
    ron neutral "Hi Mayor Sawyer."
    e "Please, call me Emily! You're not a little boy anymore! Gosh, you've grown so much! Aww, aren't you handsome!"
    ron "It's great to see you again after so long."
    e "Danny has been so excited about you coming!"
    n "Oh yes, as long as the little prince is happy."
    ron "Uh..."
    "I stare at the man, confused and watch him pack things from around the wrecked secretary's desk into cardboard boxes."
    "He doesn't look like a secretary, though. I recognize his jacket as an expensive, designer brand, and his watch is a fancy Swiss make."
    "He glowers at Emily as he packs."
    "The computer on the desk, I notice, is broken and destroyed. A casualty of the ghoul attack, I'd guess."
    show emily surprised with dissolve
    e "So, Ron, uh, ghouls. What can you tell me about them?"
    ron "Well, um, the corpses will be from a local graveyard. The summoner will have taken earth from the grave of the body, then used it in a ritual. They'll obey the summoner's commands until dawn, at which point they'll de-animate."
    show emily neutral with dissolve
    e "Ooh, that's so interesting! I don't really know anything about the topic. I'm very interested in magic, but I never investigated the whole 'undead' type of magic."
    n "I find that hard to believe. You look like a darned ghoul, and your soul has been dead for years. You should be an expert."
    e "Why don't you do the whole world a favor, Norman; go take a li'l dip in Mallory Lake, swim down to the very bottom, and stay there until you drown."
    "Jesus Christ! As a kid, I went around to Mayor Emily's house hundreds of times—she never even raised her voice once."
    "But I think she might actually try and kill this Norman guy—I should say something before they actually start fighting."
    "But should I help her or him? He started it, and she's the one who got me this job, but she's being so... vicious. Maybe I should try and stay neutral instead?"
    menu mayorAngryVoices:
        "Hey cowboy, that ain't no way to talk to the mayor!":
            jump defendMayor # {Go to [D1] [S6a] [O1]}
            # +_ to Emily's Friendship meter
            # +_ to Norman's Anger meter

        "Maybe go easier on him, Mayor Sawyer—that's kinda intense.":
            jump defendNorman # {Go to [D1] [S6a] [O2]}
            # +_ to Emily's Anger meter
            # +_ to Norman's Friendship meter

        "Okay, okay, why don't you both take a breath and calm down.":
            jump mediateBetweenTheTwo # {Go to [D1] [S6a] [O3]}
            #+_ to Emily's Trust meter
            # +_ to Norman's Trust meter

label defendMayor: # [D1] [S6a] [O1]
    scene bg mayors_office
    show emily angry at right
    show norman angry at left
    with fade
    n "Oh yeah? What are ya' gonna do about it, ya' li'l punk?"
    ron "You need to apologize to her, then you need to get the hell out, 'cos I ain't gonna stand here and listen to you disrespect her."
    show emily smile with dissolve
    e "Oh, pay that idiot no mind, Ron. The little rat's just been fired, after clinging to this office like crap on a shoe for far too long."
    jump mayorAngryVoicesJoinScene # Go to [D1] [S6a] [C1]

label defendNorman:
    # [D1] [S6a] [O2]
    # Location- Mayor's office
    scene bg mayors_office
    show emily serious
    show norman smile
    with fade
    e "Ron, I don't—"
    n "Don't worry about it, buddy. She's probably just on the rag or something."
    show emily angry with dissolve
    e "Oh shut up, you little turd."
    jump mayorAngryVoicesJoinScene # Go to [D1] [S6a] [C1]

label mediateBetweenTheTwo: # [D1] [S6a] [O3]
    # Location- Mayor's office
    scene bg mayors_office
    show emily angry at right
    show norman angry at left
    with fade
    n "Stay out of this!"
    show emily neutral with dissolve
    e "Thank you for trying to help, Ron, but really, it's not necessary. You won't get through to him. He doesn't speak 'common sense.'"
    jump mayorAngryVoicesJoinScene # Go to [D1] [S6a] [C1]

label mayorAngryVoicesJoinScene: # [D1] [S6a] [C1]
    # Location- Mayor's office
    scene bg mayors_office
    show emily smile at right
    show norman angry at left
    with fade
    e "Anyway, Ron, what's the difference between these ghouls and zombies? ‘Cos that's what we thought the moldy monsters were before my Danny set us straight."
    ron awkward "Uh..."
    "Her sudden tone change catches me off guard."
    ron "Eh-hem."
    ron neutral "Well, ghouls are corpses that are given life on an individual level by the summoner. Zombies are infected by a disease someone has created that's laced with magic."
    show emily confused with dissolve
    e "Huh?"
    ron thoughtful "In simple terms, ghouls are given life by someone and will obey that person's orders. They last until sunrise. Zombies are animated by a disease that can be spread. They last until they rot away or are killed. But outside of that, they're pretty similar. They both tear their victims apart. They're both very strong."
    ron "But ghouls are faster, and as a part of the spell to revive them, the summoner has to ensure that at least one of the ghouls has either something important to the caster or the caster's DNA on them. It keeps the ghoul tied to them, anchors them."
    ron "If the ghouls lose it, they'll just wonder around aimlessly until dawn."
    show emily smile with dissolve
    e "Ooh, I see! This is all very fascinating!"
    ron serious "Would you mind if I asked you some questions?"
    e "Of course not—one second."
    show emily moody with dissolve
    e "Norman?"
    n "What?"
    e "Stop eavesdropping and get the hell out of here."
    n "I hope you drive off a cliff."
    hide norman
    show emily smile
    with dissolve
    e "Ahh. Air feels cleaner already, don't it? Anyway, what did you want to ask?"
    ron awkward "Uh..."
    ron neutral "Well, was anyone here the night of the attack?"
    show emily neutral with dissolve
    e "No, thank God. We had no idea until we came in the next day and found the back door smashed in."
    ron "Where were you at the time?"
    e "At a dinner meeting with the head of the town council to discuss some things."
    ron "Danny told me that three places were attacked: here, the library, and the sheriff's office. But he couldn't remember what order that was in. Do you know?"
    e "Let me think—so today is Sunday. Yesterday must have been Saturday, so... the attack on the... I think it must have been the library. Then Friday was here. And that means Thursday must have been the sheriff's office."
    ron "Great, thank you. Do you have any idea what they were doing in here?"
    e "No, we don't have cameras inside the building—don't have the funding. The police found the bodies in here, by the smashed computer."
    ron "Where are the bodies now?"
    e "There's an emergency bunker beneath this building. We've locked them all down there, including the ones from the other scenes."
    ron "Good call. They shouldn't be able to re-animate anymore, but I've seen summoners put evil little booby traps in the corpses."
    e "Oh."
    show emily sad with dissolve
    e "They're- they're not going to come back, are they? The ghouls?"
    ron "Not once Marley's done."
    show emily curious with dissolve
    e "Who?"
    ron "My assistant, Marley. She's a Witch. She's outside. Putting protections around your office."
    e "Ooh! That sounds very exciting! I wonder how it's going?"
    ron "And I wonder if she's met that assistant of yours yet."
    show emily sad with dissolve
    e "Oh no! Your poor assistant! Norman isn't the kind of man you want to talk to when he's in a bad mood."
    ron "Oh believe me, no matter how bad his mood is, he ain't a threat to Marley. I once saw her get groped on the subway—she turned that swine into a darned frog, right before my eyes!"
    ron "But there's no need to fear her, not really. Sure, she's got one hell of a bite, but deep down, she's a sweetheart—but don't go telling her I said that. If Norman wants to start something, then I pity him."
    jump outsideTheMayorsOffice # [D1] [S6a] [C2] - Outside the Mayors Office

label outsideTheMayorsOffice: # [D1] [S6a] [C2] - Outside the Mayors Office
    scene bg kingston_streets
    show danny neutral at center 
    with fade
    # Location- The Streets of Kingston
    # SFX- Crow caws, small town noises
    "Danny is watching me uncomfortably closely as I examine the doorway of the mayor's office building, shaking my water bottle as a I do."
    mar thoughtful "So this is where they got in?"
    dan "Yes, we think so. We found... bits of the corpses. Caught on the doorhandle."
    mar "But the door... it looks fine. Doesn't look like they broke in. Was the door unlocked?"
    dan "I dunno. So, what exactly are you doing?"
    mar "Runes."
    dan "Runes?"
    mar "How many doors does this place have? Including this one."
    dan "What? Why do you need to know?"
    mar "It's important. How many?"
    dan "Two. Front and this one at the back. Why?"
    mar "Any big windows? Big enough to climb through?"
    dan "I- I don't think so."
    mar "Great. Well, this water bottle is full of blood. I'm going to paint runes next to both doors. They'll stop anything dead from entering the building."
    dan "Wait, for real? You can do that? You understand runes?"
    mar neutral "Not exactly. But it's not about that."
    show danny confused with dissolve
    dan "Huh?"
    mar "Magic is all about intent. To be honest, I could easily write 'protect this place from ghouls plz' on the door and, as long as I have enough intent behind it, it would work. I could even just draw a pretty picture of a ghoul's head exploding."
    mar "But in all things magical, the... 'vibe' is incredibly important. Like... think of it as an actor. You give an actor a terrible script, then no matter how good they are, the feeling they put into it isn't going to be the same as if it's a great script."
    mar "Runes can channel magic better than normal words because of their perceived mysticism. Also, your average person going by won't have any idea what it's saying. That can be very useful."
    dan "But wait, if you're using runes, what was all that time making charms for?"
    mar "The magic works better if there's multiple elements working in harmony to achieve the same goal. Also, this way, if one is bypassed for some reason, the other can act as a failsafe."
    show danny thoughtful with dissolve
    dan "I see."
    mar "I'll be honest, studying runes is more a Level Two Witch thing, and I'm just at Level One. I only know a handful of runes. But there are two—technically three—that I need here."
    # Marley's Rune Writing Game
    # We open on a wall. The cursor is a paint brush. On the wall is the faint outline of two runes-


    mar "Okay, we're going to draw two runes. Click on the water bottle to dunk the paint brush in the blood, then click and drag over the outlines of the runes to draw them!"
    # Game closes once the three runes have been drawn
    dan "What do they mean?"
    mar "The first one—the one that looks like a capital Y with a stick in the middle—that's Algiz. It's a protection rune."
    dan "Right."
    mar "The other two, they're a bound rune—two runes put together. Originally, there's one that looks like a stickman shrugging. That's Ear. The interpretation on that's a bit vague, but I'm using it to mean 'death.'"
    mar "The final rune is Kaunan. Looks like the less-than math symbol. Or crocodile jaws. I'm using it to mean ‘fire.' So, putting them together: burn the dead. The three of them will protect the building and burn anything dead that tries to enter it."
    ron "But, uh, won't the rain wash the runes away once you've done them?"
    mar smile "Nope! Once the spell is complete, nothing can wash it off. The spell will keep going until either ninety days pass or each rune is struck through—also with blood."
    dan "I see."
    "As I pause to examine my handywork, my attention wanders to the crows scattered around the nearby buildings. They're watching me. Carefully. Danny follows my gaze."
    show danny worried with dissolve
    dan "Those things creep me the hell out."
    mar thoughtful "They're just birds. Overwatching."
    dan "There never used to be this amount of them before. They've all come over the past week or so."
    mar curious "Is that so?"
    "Suddenly the door to the council office flies open, nearly hitting me in my face."
    show norman moody
    show danny thought
    with dissolve
    mar moody "Oi!"
    n "Get lost!"
    "The strange man glances at me out of the corner of his eye, then pauses."
    n "Hey—I don't know you. You're not from here."
    mar curious "Uh- no. No, I'm not."
    n "What, are you from the council? Or do you work for that twit, Mayor Sawyer? 'Cos if you is, you can go screw yourself!"
    mar confused "What?? No, I'm not! I'm just—"
    "My gut is telling me to lie here. Not to let this angry weirdo know anything about me."
    mar "I'm just a friend of—well, a friend of a friend of Danny's. That's all. Me and my friend Ron are saying with him."
    show norman angry with dissolve
    "The stranger glowers at Danny."
    n "Get lost, Sawyer."
    show danny worried with dissolve
    dan "I- I'm not scared of you, Norman!"
    "Norman takes a menacing step forward."
    show danny scared with dissolve
    dan "Uh- but I think I can hear Ron calling... Got to go!"
    hide danny with dissolve
    "Coward. Nathaniel's eyes turn back to me."
    show norman suspicious with dissolve
    n "... You... you don't work for Sawyer?"
    mar "You mean Danny's mom, the mayor? No, I haven't met her."
    n "Or the council?"
    mar "No!"
    show norman thoughtful with dissolve
    n "Oh. I see."
    n "Well, if you're smart, you'll stay the hell away from all of 'em."
    "Ooh, this feels like a clue. I don't exactly want to keep talking to this angry dude, but I guess this is my job."
    mar curious "Oh? And why's that?"
    show norman serious with dissolve
    n "The council is full of a bunch of old, power-hungry farts, led by that spoilt bastard, Chris Maddux. And the mayor—well, she's a conniving witch."
    mar "Really?"
    n "Don't trust her. No matter how much she prattles on about 'helping Kingston,' and 'bringing it into the modern age,' she's just here for the power."
    n "It's all she cares about—she has this whole town wrapped around her damn finger. And has done for... well, for too long."
    "The hell is he talking about?"
    mar "Why? What's she done?"
    n "That ain't none of your business. But listen, the long an' the short of it is this: don't trust no one in Kingston. They all got secrets and agendas."
    n "An' we got some real freaks, too, like the homo half-elf up at the school. Why these fools would ever let someone like that around kids is beyond me."
    "Wow, what a charmer."
    "If we're looking for someone who hates the town and would want to destroy it, I think there's a good candidate here."
    mar "Has she done something to you?"
    show norman moody with dissolve
    n "That ain't none of your business."
    n "If you're smart, you'll get the hell out of Kingston. As soon as possible."
    "With that, Norman turns and marches off down the street."
    "He doesn't seem like the most stable of men. But in all honesty, I don't disagree with him about leaving this darn place."

label searchingTheBustedUpDesk: # [D1] [S6a] [C3] - Searching the busted up desk
    # FADE IN
    scene bg mayors_office
    show emily neutral at center with dissolve
    ron neutral "Do you mind if I have a quick look over the desk that was destroyed? In fact, I should have a look round the whole office if this was the ghouls' target."
    e "Go ahead. I need to visit the li'l girls' room anyway, so I'll give you some privacy."
    ron "Thank you ma'am."
    hide emily with dissolve
    "As Mayor walks out of her office, I look around her room. The assistant's desk is completely destroyed. A total wreckage. I don't think I'll be able to find much there. But there's a lot of interesting things around the office that catch my eye."
    # Search in Mayor's office
    # We have a search game around the mayor's office. There are several things that must be clicked on, and some that can be. When each are selected, Ron will give commentary.

    # Emily's Diploma (Compulsory)
    # We see a certificate. The writing is very fancy. It is titled 'Barkson Law School' and has the slogan 'Etiam dii et reges ad Dominae Iustitiae potestatem flectere debent'. In the centre is the name Emily Sawyer. However, the paper of the certificate under the name is a very slightly different colour, as if a tiny bit of paper with the name written on it was stuck onto the certificate.

    "Oh yeah, the mayor used to be a lawyer before she came to Kingston."


    # Screwed up paper (Compulsory)
    # It is found on the floor. When clicked on, it unfolds to reveal a letter;
    # Emily Sawyer
    # 6 Redstone Road
    # Kingston, TX 
    # USA

    # Norman Conlee
    # 102 Terence Boulevard
    # Kingston, TX
    # USA
    # Friday, May 8th 

    # Dear Mr. Conlee,

    # We regret to inform you that your employment with the Mayoral Office of Kingston has been terminated effective immediately.
    # This is due to persisting problematic conduct, which continued after multiple verbal and written warnings. These included complaints about your attitude from more than a dozen of your colleges, general ineptitude at your job, and a significant amount of funds that you had access to going missing (a sum of more than $25,000 just this year). Although we have decided not to pursue criminal charges as an act of goodwill, if you behave unprofessionally with this termination, we will rethink our leniency.
    # Please return your company access card to the reception desk within the week.
    # We are regretful that we were forced to make this decision, Mr. Conlee, and wish you all the best with your future endeavors.

    # Respectfully,

    # E. Sawyer
    # Mayor Emily Sawyer
    "Hmm, so this is Norman's letter of termination. It seems funds have been going missing... and they think it's Norman? Very interesting."


    # A post-it note (Optional)
    # Stuck to the mayor's computer is a yellow post-it note that reads: 'Don't forget to ask Jeff to higher Marianna and Bethany.'
    "Marianna and Bethany? Wonder what they did to get a favor from the mayor."


    # Photo of Emily and Danny (Optional)
    # A framed photo of Emily holding a young Danny, on Emily's desk.
    "Aw. That's sweet."

    # The Diary (Compulsory)
    # The diary is lying open on Emily's desk, showing last week's entries, which are as follows:
    "Monday 6th May"
    "15:00	Meeting with treasury guy—Tony? Terry? Terrance? Something T"

    "Tuesday 7th May"
    "13:30	Meet with the school board. They want to cancel the clubs again, so drink coffee on the way. Going to need it."
    "17:00	Opening shop on Sycamore Street"

    "Wednesday 8th May"
    "09:30	Meet with the council about library funding AGAIN!"
    "Need to finish the new library proposal before meeting."
    "22:00- Meet with S"

    "Thursday 9th May"
    "12:00- Meet with S"
    "19:30	Meeting with C at Marianna's"

    "Friday 10th May"
    "Lunch with Mrs. Pear"
    "Cancel dinner with D. Need to work late to edit darn library proposal."
    "Dinner with D"

    "Saturday 11th May"
    "BLOODY TERRY!"
    "11:30	Meet with sheriff to discuss rising crime rates. Moron."

    "Hum. That's odd. Emily said that her office was attacked on Friday when she was out having a dinner meeting with the head of the town council. Now, she was booked to have dinner that day—with 'D.'"
    "But her diary says she needs to cancel it to work late. Meaning she would have been here when the attack happened."


    # The Card Collection (Optional)
    # On Emily's desk is a small collection of business cards. Most can be made up, but 3 are important.
    # -	A scrap of paper with the names Marianna and Bethany written on, with two a half-concealed phone numbers written on it.
    # -	A business cark of Robert Saffer, a plumber
    # -	A fancy black card with gold lettering, with the name 'Thirofel Dorali' written in fancy letters and a half-concealed email address.
    "Hm. Didn't realize people used business cards anymore. Maybe I should make some?"

    # Newspaper Clipping 1 (Optional)
    # (1/3)
    # A framed newspaper article showing a young Emily and a large, hulking, hairy man, standing together on the steps of a courthouse. The pair look triumphant. The article reads:
    "Victory for Were's over MeTuber!"
    "This Wednesday saw the dramatic conclusion of the Manny Rudeson vs Were Commune of Harris County case. The sentence came back today: GUILTY on all counts."
    "For those of you who haven't been keeping up with the case, we have all details of the events as described by the legal representative of the Were Commune of Harris County, Miss Emily Sawyer."
    "On the fourth of November, two years ago, Manny Rudeson snuck onto Were Commune grounds. This day was the first day of the full moon, and Rudeson found his way into the area containing the cages that the predator Weres are locked in for the three nights. He hid himself there and, as the sun set, filmed Miss Sawyer's clients as they stripped down naked and began their painful physical transformation. He continued filming her clients all night. During this time, Rudeson often acted to deliberately anger the transformed Weres by using a stick to poke them through the cage's bars."
    "Rudeson even went so far as to put his hand into some of the cages, pulling it out when the Weres tried to bite it."
    "Rudeson then left the compound with the help of a guard he had bribed and went home to upload the video to the internet, violating the Weres' privacy."
    "During this case, the two lawyers made vastly different legal arguments."
    "Miss Sawyer pointed out that the Were-animal community is an often-abused minority, citing multiple scandals from the last five years of cruelty aimed at the Weres that were perpetrated by the humans that run the Were communes and provide security."
    "Some of her most dramatic lines included: 'These people have been infected by a terrifying, life altering disease. And our society's reaction? Lock them away, not just for the nights of the full moon, but twenty-four-seven. The Lycanthropy condition can be dangerous to both the infected and those around them, but it doesn't mean they are any less human. Rudeson and his video have treated my clients like exhibits in a freak show. Just because we unfairly push Weres to the outskirts of society, doesn't mean they are not owed their privacy and dignity.'"
    "Rudeson's lawyer, however, had a very different opinion of the Were-community. His argument included: 'Were-communes are funded by taxpayer money. Surely my client, as a tax-paying American, has the right not only to see what his money is funding, but also to share that information with his followers. This is a freedom of information issue.'"
    "Evidently, Sawyer's argument won over the judge, and Rudeson was ordered to give the individuals his video captured a total of $15,000 as well as all money made from the video, take down the video, and pay all court fees."
    "Rudeson was angered by the ruling and has suggested that he may contest it, telling reporters, 'I ain't giving those freaks a single dime! And darn that monster-screwing lawyer!'"
    "This has certainly been a dramatic case so far, and this reporter will be following any further actions with interest."

    "Hmm, looks like Mayor Sawyer has done some interesting stuff in her career."

    # Newspaper Clipping 2 (Optional)
    # (2/3)
    # Another framed newspaper clipping. There's a picture of Emily speaking at the front of a trial.
    "Beloved Children's Park to be Torn Down to Appease Immigrants!"
    "The children's playground on Marigold Boulevard is scheduled for demolition and rebuilding thanks to the interference of inhuman immigrants."
    "Some elf, who moved here from whatever hellscape they crawl out off, had a bone to pick over, of all things, the material the playground was built with—iron."
    "This elf, a male named Thirofel Dorali, with the help of his lawyer from the distant Podunk town of Kingston, has somehow convinced the judge to have our beloved playground removed."
    "This is a sad day for the reasonable humans of Dallas."

    "Huh. Emily must have been the one representing the elf in this case. But this article seems pretty biased against her. I wonder why she picked this report to frame?"


    # Newspaper Clipping 3 (Optional)
    # (3/3)
    "The third and final framed newspaper clippings"
    "Yeti of Austin Zoo will NOT be Put Down After Death of Child"
    "Yesterday a judge ruled that Marvin, the Austin Zoo's prize Yeti, will not be put down and was not culpable for the death of a child."
    "Emily Sawyer, the lawyer representing the zoo, swayed the judge after showing CCTV footage of the child's mother dangling her son over the pit in which Marvin was kept. The mother, Mrs. Dias, then tragically dropped the child, who landed directly onto the sleeping yeti, who proceeded to hit the child into the wall, causing his death."
    "Now that this tragic case has come to a close, judge Benjamin Roosevelt ruled that the death was accidental. Marvin was simply acting on instinct when he struck the child and would not be put down."
    "Sawyer said that 'This was a great victory for justice. Although it is our duty to acknowledge the tragedy of this situation, we must also remember that Martin is an animal. There was no cruelty in his actions. No hatred. Just the pure instincts that would keep him alive in his natural habitat.'"
    "The Dias' and their representative were not available for comment."

    "She really was a defender of all magical beings."


    # The Pillar (Optional)
    # In a large case hanging on the wall behind the mayor's desk is a rotting black wooden post, covered in runes and marks. There is a small plaque that reads 'One of the five protection pillars of Kingston'.

    "What the hell is that?"


    # The Memo (Compulsory)
    # A neatly handwritten memo lying on the mayor's desk that reads, 'Emily, I am dismayed to once again inform you that $5,000 has gone unaccounted for in the town's treasury, despite the more vigorous security systems put in place. The possibility of getting this officially investigated has come up, but we'll need you to sign off on this. Paris.'

    "Oh dear. That's worrying—missing money."


    # Receipt (Compulsory)
    # A receipt on the mayor's desk. It's from a shop called The Magical Tome Emporium. The receipt lists three books:
    "The History of the 13 Branches of Thremmatology............................................................ $23.99"
    "The Idiot's Guide to Ghouls......................................................................................................$14.99"
    "A Visual Tour of Bellua Island...................................................................................................$29.99"
    "The receipt is dated the May 9th."

    "Hmm. Looks like Emily has an interesting reading list."


    # Norman's letter (Compulsory)
    # A grubby, dog-eared note that reads:
    "May 5th"
    "Dear Emily,"
    "I am formely rekwesting an advancmant of my salery as soon as possibal."
    "Norman"

    "So, Norman wanted his salary early? I wonder why."
    "He's also really bad at spelling..."


    # St. John's Wart (Compulsory)
    # A plant, placed near the doorway. Fresh. 

    "That's strange, why is there a plant here?"

    # Once all the compulsory things have been found, an 'Exit' button will appear at the top right of the screen. After ‘Exit' is hit, the scene continues.

    "As I give the room a final once-over, Emily returns."
    show emily neutral at right with dissolve
    e "Find anything useful?"
    "My response is interrupted by footsteps coming down the hall. I turn and wave to Marley as she enters the room."
    show marley neutral at left with dissolve
    mar "Hiya. I'm all done, Ron. Put up the runes and used two charms—front door and back. None of the windows are big enough to need it."
    show emily confused with dissolve
    e "What's she talking about?"
    ron "Oh, Marley put special charms at each of the building's entrances. Should give some protection if anything happens again."
    show emily smile with dissolve
    e "Oh, thank you! That's so kind of you."
    show emily neutral with dissolve
    e "And—thank you for coming. Danny told me you're having difficulty being back here. It means a lot that you want to help us. This town is so important—I've lived here most of my life—Kingston means everything to me."
    ron serious "Of course, ma'am. We'll do everything we can to protect it."
    e "And I want justice, against whoever has been doing this. Etiam dii et reges ad Dominae Iustitiae potestatem flectere debent."
    ron confused "Huh?"
    show marley thoughtful with dissolve
    mar "It's Latin. Something about... gods and kings—"
    show emily smile with dissolve
    e "'Even gods and kings must kneel to the might of Lady Justice.' The moto of my university, words to live by."
    ron neutral "Well that's nice. Marley, where's Danny?"
    mar "Watching some angry weirdo screaming in the car park."
    ron "Ah. I think I met the angry, screaming weirdo. Anyway, we should get going; got places to go before night falls. Speak to you later Mayor Sawyer—sorry, Emily."
    e "I'll see y'all around! If ya' ever need anything, feel free to drop by!"
    ron "We will. Goodbye!"
    # FADE OUT
    # Return to MAP

label mayorEmilySawyer2: # [D1] [S6b] [Optional]- Mayor Emily Sawyer 2
    # FADE IN
    scene bg mayors_office
    show emily neutral at right
    show danny smile at center
    show marley neutral at left
    with fade
    e "Oh, hello! You're back!"
    dan "I wanted to say hi, Mom."
    show emily smile with dissolve
    e "Hello, Danny-boo!"
    show marley smile with dissolve
    mar "Hehe, Danny-boo."
    show marley neutral
    show danny annoyed
    with dissolve
    dan "Mom, I told you not to call me that! I'm twenty-six; I'm not a kid anymore!"
    show emily awkward with dissolve
    e "Sorry, sorry, I keep forgetting you don't like being called that. I'll try to be better."
    dan "Good."
    show danny neutral with dissolve
    dan "Now, can I borrow some money? I'm super broke."
    e "Of course, sweetie! I knew I stopped your allowance too soon–back to $100 a week?"
    dan "Maybe $200?"
    show marley smile with dissolve
    mar "Oh my God."
    e "Absolutely, darling!"
    dan "Thanks, Mom! See you later!"
    e "Oh wait, hon, I was wondering if you could help me move some furniture—"
    dan "Love you, bye!"
    hide danny
    show marley neutral
    show emily awkward
    with dissolve
    e "Ah well. Kids, you know how they are."
    mar "No. No, I do not. And he's not a kid."
    ron awkward "Uh, we- we should be going. Nice to see you again, Ms. Sawyer."
    # FADE OUT
    # Return to MAP

label terryMadux: # [D1] [S6c]- Terry Maddux
    # FADE IN
    scene bg sheriffs_office
    show danny serious at right
    show marley neutral at left
    # Location- Sheriff's office
    # SFX- soft office noises- talking, phone ringing, and occasional radio beep and crackle.
    "As Marley, Danny, and I head into the office, I look around. I've never seen this place properly before—don't think I ever went here as a kid. Its small. Quaint."
    "???" "Hmm. It seems another player has entered the game."
    ron confused "Sorry?"
    mar "Huh?"
    ron "Who said that?"
    mar "Said what?"
    dan "Hey Ron, there's something I should probably tell you, before the sheriff comes over here."
    ron "Did you guys not hear—"
    dan "Come on Ron, this is important! It's about the sheriff."
    ron curious "Oh yeah? What about them?"
    dan "You... you know him."
    ron "Huh?"
    dan "We went to school with him."
    ron worried "Who is it?"
    dan "Uh..."
    ron "Danny, who is it?"
    show terry smile at center with dissolve
    ter "Ron, you old dog, is that you?"
    "Oh crap oh crap oh crap oh crap oh crap."
    ron awkward "Terry Maddux—how nice to see you again after all these years."
    "I have literally had a vampire pin me down and try to tear out my throat. Not the sexy type either. The face-melty, ugly ones that smell like rats. I've had evil priests try to rip out my heart. I've had an infernal possess me."
    "I'd rather go through any of those again than be here, with him."
    ter "Gosh, it's been so long!"
    ron "Yes, the last time we saw each other was when you broke into the principal's office and announced I was 'one of them queers' over the loudspeakers."
    ter "Haha, oh yeah! Sorry about that, I always took those little pranks a smidge too far."
    ron neutral "Yeah. A smidge."
    ter "My bad, haha. Hey Danny, go grab me a coffee, will you? Black. Machine's over there."
    show danny neutral with dissolve
    dan "Uh... sure. Be right back."
    show marley neutral with dissolve
    ron "This definitely isn't where I figured you'd end up. Didn't you get a scholarship somewhere?"
    show terry awkward with dissolve
    ter "No, no there was a change of plans. But I love my job! All my old friends are still in town—Zack works at the timber mill; Steve helps out at my pa's farm. Oh, and my old friend Brent is a doc up at the hospital. We still meet every month and go hunting."
    show terry smile with dissolve
    ter "Ooh, and, who's this fine filly?"
    show marley confused with dissolve
    ron "This is Marley, my assistant."
    ter "Oh, thank the Lord. I was worried you'd turned straight and this was your missus."
    ron "Uh... no. No, still gay."
    ter "So, uh, are you single then, ma'am?"
    show marley moody with dissolve
    mar "Why do you ask?"
    ter "'Cos you've dang near taken my breath away."
    mar "I wish that was literal. Your halitosis is a serious problem."
    show terry confused with dissolve
    ter "Well, uh... that's mighty kind of you to say, ma'am."
    show terry neutral with dissolve
    "From the look on Marley's face, I think I'd better step in before she gives the idiot a black eye."
    ron "So, uh, this place was attacked? As was the mayor's office and the library? What happened?"
    ter "Well, this was attacked on Saturday—after the attack on the library, two days after the mayor's office. In the dead of night, one of the bastards came in and attacked my poor Chief Deputy, Derek Prikus, who was working late. Wrecked his desk."
    ter "He's fine. Physically. It seems to have given his nerves a bit of a crack. He's been committed to the psych ward at a nearby hospital, ranting and raving like a loon. Luckily for the guy, I was there and managed to beat the little wretch back."
    ron "And where were you when the attack happened?"
    ter "I was out with your Danny. I was trying to teach him how to hunt."
    show terry moody with dissolve
    ter "Difficult to do when that weasel of a mayor has got the land 'round here designated as no hunting. Typical woman, always ruining people's fun."
    "Ugh—why would Danny want to spend time with this idiot?"
    ron "Why don't you show us where the attack happened?"
    show terry neutral with dissolve
    ter "Right there, over by the chief deputy's desk."
    # Search in Sheriff's office
    # We mainly see Derek's desk- completely destroyed, the computer nothing but a wreck. There are odd things all over the desk- a picture frame, pot of pens, etc. Next to Derek's desk is Ted's desk. It is a mess. Wrappers, papers, even moldy food.


    # Calendar (Compulsory)
    # On Terry's desk is a month-by-month calendar. It shows the month of June, starting on a Wednesday. The calendar is printed to show the full moons- a tiny circle on the 13th, 14th and 15th. The following days are written on-
    "9th-	Meet with Derek here- 7:15pm"
    "11th-	Meet with weasel at her office- 11:30"
    "13th-	Time off"
    "14th-	Time off"
    "14th-	Time off"

    "Hm. Looks like Terry originally had the next three days off, but they've been crossed out. Did he cancel because of all this? Wonder what he had planned."


    # Photo 1 (Compulsory)
    # Blue-tacked to Teds computer is an unframed photo. It's relatively modern photo of Terry and a man, each holding a dead rabbit. When clicked on, it will turn around to reveal the words 'T. Maddux + B. Nelmes in Kingston Woods. 12/7/25'.

    "Ug. I remember Brent Nelmes. He went to school with Terry and me. Really embraced the whole 'side kick to a bully' role."


    # Photo 2 (Optional)
    # This photo is better looked after than the first, still on Terry's desk, and sits in a fancy frame. It shows a young Terry sitting on an old man's lap. The man looks like an older version of Chris. This is Freddy Maddux.

    "Hm. Guess this must be young Terry and his grandpa or uncle or something. This photo looks a lot more taken care of than the rest of the stuff on this desk."


    # Book (Compulsory)
    # Terry's desk. Underneath a ragged pile of papers and a half-eaten doughnut, sits a pristine, untouched book- The Idiot's Guide to Magic.

    "Huh. Looks like Terry's been researching magic. Or... meaning to. This looks untouched."


    # Small pile of ripped up paper (Compulsory)
    # Around Terry's bin is scattered small scraps of paper. When clicked on, we see one of the lager scraps- a top corner that reads 'Arrest File of-' The rest is cut off.

    "This... this looks important! Should it be here?!"


    # Evidence Bag (Compulsory)
    # Inside Terry's bin sits a plastic bag. When clicked on, it's pulled out to show a hair sample.

    "What the- this is bagged evidence! It shouldn't be in his trash!"


    # Empty Coffee cup and apple core (Optional)
    # The litter sits in the middle of Terry's desk. The core has started to rot.

    "What the hell— this is the desk of the Kingston sheriff! Not a darn pigsty!"


    # Email chain (Compulsory)
    # On Terry's computer. When clicked on, you can scroll through this email chain;

    "From: 	Tertopdog69@Kingstonsheriffsoffice.com"
    "To:		Derek_Prikus@Kingstonsheriffsoffice.com" 
    "Date 	Tuesday, June 7th, 12:16 pm"
    "Subject: Re: Re: Re: Re: Re: Meeting"

    "Fine. At som pont today I'll pick a time with u."


    "From: 	Derek_Prikus@Kingstonsheriffsoffice.com"
    "To:		Tertopdog69@Kingstonsheriffsoffice.com"
    "Date 	Monday, June 6th, 12:23 pm"
    "Subject: Re: Re: Re: Re: Meeting"

    "Dear Terence,"

    "I am intending to schedule a meeting with the mayor within the next week, but I would like to speak with you first. My insistence on meeting with you is due in part to my respect for your father and the friendship I had with your brother. But this is your last chance. You will meet with me within the next few days."

    "Yours,"
    "Deputy Derek Prikus"
    "Kingston Sheriff Department"


    "From: 	Tertopdog69@Kingstonsheriffsoffice.com"
    "To:		Derek_Prikus@Kingstonsheriffsoffice.com"
    "Date 	Monday, May 30th, 5:53 pm"
    "Subject: Re: Re: Re: Meeting"

    "Jesus Derek, we're not doing this. I'm not going to reck my day by talkng with you about watever bulcap you've got up your butt."


    "From: 	Derek_Prikus@Kingstonsheriffsoffice.com"
    "To:		Tertopdog69@Kingstonsheriffsoffice.com"
    "Date 	Tuesday, May 17th, 3:42 pm"
    "Subject: Re: Re: Meeting"

    "Dear Sheriff Maddux,"

    "Please take this seriously, Terry. Information has come into my possession which we need to discuss. If we do not, I will have to escalate this further."

    "Yours,"
    "Deputy Derek Prikus"
    "Kingston Sheriff Department"


    "From: 	Tertopdog69@Kingstonsheriffsoffice.com"
    "To:		Derek_Prikus@Kingstonsheriffsoffice.com"
    "Date 	Tuesday, May 17th, 3:36 pm"
    "Subject: Re: Meeting"

    "Derek-"
    "Piss off"


    "From: 	Derek_Prikus @Kingstonsheriffsoffice.com"
    "To:		Tertopdog69@Kingstonsheriffsoffice.com"
    "Date 	Friday, May 13th, 1:05 pm"
    "Subject: Meeting"

    "Dear Sheriff Maddux,"

    "I'm emailing you to request a meeting to discuss certain problematic things that have come to my attention. This is an urgent matter, and I trust you will respond with appropriate urgency."

    "Yours,"
    "Deputy Derek Prikus"
    "Kingston Sheriff Department"


    # Post-it-notes (Optional)
    # There are post it notes stuck to the wrecked computer on Derek's desk. When clicked on, we see they say things like: 
    # -	'Don't forget to spell-check your paperwork' 
    # -	'Don't forget your dry-cleaning'
    # -	'Appointment with mechanic on 13th, 3:30 pm'

    "Hm. Whoever's desk this is seems very organized."


    # Yearbook (Compulsory)
    # There's an old yearbook hidden under the wreckage. It is from Kingston High

    "And, what's this— an old yearbook?"


    # Request to stay late (Compulsory)
    # This is a memo in the wreckage of Derek's desk. It is written in Terry's handwriting, but there's teacher style corrections over it in red-
    "Meamo"
    "Fri, June 10th "
    "Hi Darek,"
    "Im sory to do this to U, but can U finish this peper wark for tomoro?"
    "Thanxs!"

    "Man, these two do not get along."
    "Wait, hang on— this is dated for Friday. The day Terry said this place was attacked. So then, Terry is the reason that his deputy was here to be attacked. That might be just a coincidence... but Derek does seem to hate Terry..."

    # USB stick (Compulsory)
    # There are the remains of a drawer, which, when clicked on, will turn over, revealing a small USB stick taped to the back of it. 

    "Hmm... Looks like the deputy used a trick I've done myself. Tape something you don't want found to the underside or back of a drawer."
    "First time I used it was when I wanted to hide Men's Sports: Swimsuit Edition from my parents."


    "This part will play once all compulsory items have been found."
    ter "That's a pretty accent ya got there, Miss Marley. Where ya from?"
    mar "England."
    ter "Oh awesome, whereabouts? Maine? You look like a Maine girl."
    mar "...Old England. Not New."
    "I snatch up the hidden flash drive and tuck the yearbook under my coat while Terry's distracted making goo-goo eyes at a very irritated Marley."
    ron "Whoever was controlling them ghouls really wanted that computer destroyed."
    mar "You think the chief deputy might have been investigating the summoner and this was to cover it up?"
    ron "The idea has cross my mind."
    ter "Oh, I think you big city detectives are jumping to conclusions. I reckon the perp just wants to cause a ruckus."
    "That's a mighty strange motive, to 'case a ruckus'. A ghoul summoning spell— well, that's restricted magic. The kinda spell that ain't readily available. Too much effort for just 'causing a ruckus.'"
    "Terry's a fool, always had been, but he can't be that stupid. Maybe he's trying to brush it under the rug? This is his turf, maybe he's embarrassed that it's all going to hell under his watch."
    "Or maybe he just doesn't like his old high school nemesis is doing his job? If I'm careful, I think I can get his real opinions on the case."
    "Perhaps I can bully it out of him. Or coax it out of him by being overly nice. Or if I prove I'm a professional and not here to show him up."
    menu terryMaduxChoices: # Option 1
        "You're really dumb enough to think this is just some bored kid looking to cause trouble on a Friday night? 'Cos if you do, you're as stupid as you were when we were kids.":
            jump attackVerballyTerry # {Go to [D1] [S6c] [O1]}
            # +_ to Terry's Anger meter

        "You're probably right, Terry. After all, you've been here longer than I have. You've certainly got a better sense of the town. But it seems like an awful lot of fuss to go through jut to 'cause a ruckus.' Ghoul summoning spells are forbidden magic after all— mighty hard to get a hold of. Are the teens these days particularly troublesome? The type to go too far to get some fun?":
            jump defendTerry # {Go to [D1] [S6c] [O2]}
            # +_ to Terry's Friendship meter
        
        "And that's your professional opinion, is it? Do you have any suspects? Any one in town with a record who you think would go this far to 'cause a ruckus'? 'Cos ghoul summoning spells, they're forbidden by all the magic councils. Mighty tricky to get a hold of one.":
            jump makeTerryTrustYou # {Go to [D1] [S6c] [O3]}
            #+_ to Terry's Trust meter

label attackVerballyTerry: # [D1] [S6c] [O1]
    scene bg sheriffs_office
    show terry angry at left
    show marley neutral at right
    with dissolve
    ter "How dare you! Here I am, extending the hand of friendship after all our years of difficulties, and you spit in my face!"
    ron smile "Ha!"
    ron moody "That's a damn joke. You 'extending a hand of friendship' is a load of crock, and you know it. You're just puffing up your chest like a darn rooster. Trying to prove you're some big bad alpha craphead like you did when we were kids."
    ron "And you're as stupid as you always were then. So, I ask you again: do you really think someone went to all the trouble of summoning ghouls just to cause a darn 'ruckus'?"
    ter "I don't think it's just dumb kids, I ain't never said that! It's clearly someone who wants to screw up the town! Someone who hates Kingston."
    ter "I ain't a fool, Ron. I'm the sheriff, not a darned kid anymore. There are people who have vendettas against the town."
    ron confused "What? Why would someone hate the town?"
    show terry moody with dissolve
    ter "Oh I don't know, 'cos they've got a damn chip on their shoulder about how they didn't fit in or whatever, or they're hungry for power or some bullcrap."
    "The unvoiced accusation hangs in the air. I can practically hear it."
    "'People like you, Ron.'"
    ter "*Sigh* Look, Ron, I get it. Our time here when we were kids weren't... great. But we're adults now. We need to be better than we were. So... so I understand why you don't trust me. But... we gotta work together on this."
    show terry serious with dissolve
    ter "So, for the sake of this investigation, I'll be a bigger man than I was when I was a boy. And say that I'm sorry. About the way I treated you, back then."
    "..."
    "..."
    "BULLCRAP."
    "I ain't never heard such bullcrap before."
    "Terry's full of crap."
    "But... but if I call him on it, I'll look like a petulant child."
    "So, I smile."
    ron smile "Well, that's mighty good of you to say, Terry."
    ron "I ain't here to get revenge or nothing. I'm here to solve the case. And we have to work together on that. I'll do what I can to make that goal come true."
    show terry smile with dissolve
    ter "Good. I know that we can put our differences aside and crack this puzzle together."
    "Bull."
    "Crap."
    "He looks like some darn kids' TV character, talking about peace and working together."
    "I can smell the lies on his stinkin' breath."
    jump terryMaduxJoinScene # Go to [D1] [S6c] [C1] 

label defendTerry: # [D1] [S6c] [O2]
    scene bg sheriffs_office
    show marley neutral at right
    show terry thoughtful at left
    with dissolve
    ter "Oh, I don't mean kids, more people who want to cause a ruckus out of spite."
    ron confused "Huh? Why?"
    show terry neutral with dissolve
    ter "Oh, people have reasons. There are folks round here that sure seem to hate Kingston."
    show terry smile with dissolve
    ter "But I bet together, the two of us can work this out! We'll be a great team. I just know it!"
    "Slime bag."
    ron awkward "Oh definitely. I'm sure we'll work excellently together."
    jump terryMaduxJoinScene # Go to [D1] [S6c] [C1] 

label makeTerryTrustYou: # [D1] [S6c] [O3]
    scene bg sherrifs_office
    show marley neutral at right
    show terry confused at left
    with dissolve
    ter "Huh? 'The magic councils'? What are they?"
    mar "The thirteen councils that govern all branches of magic. They monitor what magic their members have access too. And ghoul summoning isn't really openly available. It's dangerous stuff."
    show terry smile with dissolve
    ter "Beauty and brains, huh? Ain't you just the full package?"
    show marley smile with dissolve
    mar "And you're not even half an envelope."
    show terry thoughtful with dissolve
    ter "Well, I have a few guesses in mind. But no one with a record or nothing."
    show terry neutral with dissolve
    ter "But there are people 'round here who've got problems with the town. Who'd pull something like that just as an eff-you to Kingston."
    # Bottom sprite- Ron (Confused)
    ron "Huh? Why would anyone hate Kingston?"
    ter "Beats me. I love this town."
    "Of course he does. This damn place worships him."
    jump terryMaduxJoinScene # Go to [D1] [S6c] [C1] 

label terryMaduxJoinScene: # [D1] [S6c] [C1]
    show terry neutral at left
    show marley neutral at right
    with dissolve
    ter "Anywho, where's that dang Danny with my cup o' joe?"
    hide terry with dissolve
    ron neutral "You know something, Mar?"
    mar "What, Ron?"
    ron "I got a hunch there's more to this whole mess than meets the eye."
    mar "You don't say. Let me just put up some protection charms, then we can go. Looks like I'll need four—those windows there, there, the front door and the back."
    ron "Get Danny to help you if you don't mind. It'll give him an excuse not to deal with Terry."
    # FADE OUT
    # Return to MAP

    return