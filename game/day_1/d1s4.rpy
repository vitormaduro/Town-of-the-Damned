# The Wolf
label d1s4:
    scene black
    scene bg cg_witch with fade

    # sfx Nature noises

    "I follow nature's pull on my soul away from the tiny town. I head past some farms and find myself in thick woodland."
    "Perfect."
    "After a bit of walking, I find a small clearing and sit myself down. I close my eyes and focus on my breathing."

    # sfx deep breathing

    "With every breath in, the smell of flowers, the trees' bark, the rotting leaves, animals' musk all mix in my nose. A wonderful orchestra of scents."
    "Then the sounds—the leaves rustling through the trees. The cawing of the crows above."
    "Slowly, from deep in my gut, I can feel little tendrils of my magic reaching out, stretching like someone waking up after a long sleep."
    "It connects itself to the plants as they slowly push their roots deep into the ground, sucking up moisture, their leaves bathing in the delicious sun."
    "Connects to the creatures as they scurry around, chasing each other or hunting for food, and the crows in the branches high above me. I can feel them watch me curiously. Figuring out if I'm friend or foe. But knowing in their hearts that I am no ordinary mortal."
    "The forest around me feels like I'm home, even though I'm miles from Chicago. And even further away from where I was born."

    # SFX- loud twig snap

    "I open my eyes."

    scene bg cg_witch_wolf with fade

    "Normally only a powerful Witch could speak to an animal. But here, in this clearing, with my magic connected to everything around me, including the wolf—"

    m "Hello sister."
    w "{i}*Sniff*{/i} You are human."
    m "I am."
    w "{i}*Sniff sniff*{/i} But that's not all you are."
    m "No. I am a Witch. A person who connects to nature for magical powers."
    w "Hm. Humans. Always chasing power like a pup chases a squirrel. Ignorant of or uncaring for whatever you trample under-paw in your never-ending hunt for your goal."

    "Well… she's not wrong. I can feel the anger and rage at humans, nestled deep in her lupine heart. Perhaps it's best if I change the topic."
    "I'm surprised to see a wolf here at all—I did some research on the wildlife in this area on the way over—the wolves that once lived here were wiped out ages ago."

    m "This must be lonely hunting for you, sister. Your pack must be the only one for many territories."
    w "I have not seen another of my kind since my brother went to the earth. When I join him, the great hunters will no longer roam this land. And, for that, I am grateful."

    "That surprises me. Wolves guard their territories fiercely, and nothing is more important to them than the continuation of their pack—their family. So why is this one so happy about her line's demise?"

    m "Is this land so unkind to you, sister? The hunting's too meagre?"
    w "No, Witch. The prey is unending. But this is not the place for my kind. This place is too full of the un-us."

    "The what?"

    m "The… un-us?"
    w "Those that {i}look{/i} like us, but are not us. The more you look, the more you see—they're short, with too-long limbs, too-silky hair, stretched out faces. Eyes to black. Glassy. Their words so garbled. A false reflection of us."
    w "They are beasts of humans—like their perverted cubs."

    "Oh, she must be talking about dogs."

    w "They infest the land, take over territories. And if you defeat one—then come the men with their explosion sticks. My pack used to curse the day our forefathers and mothers were tricked into building our den here."
    m "'Tricked'? How do you mean 'tricked'?"
    w "That is a long story, Witch. The story of my pack. You do not wish to hear so sad a history."

    "Like hell I don't."
    "But how do I get her to share it? She's very stiff. Formal. She doesn't trust me—I can't blame her for that. Should I be stiff and formal too? Show respect? Or try to be kind? Friendly?"

    menu:
        "It would be a great honor to hear your ancestor's story, sister. If you would do me the kindness of sharing it.":
            # add She-World to Marley's companions
            jump d1s4o1

        "You've piqued my curiosity! Come, sit comfortably. I'm most intrigued, be a friend and tell me your tale.":
            jump d1s4o2

# Correct choice
label d1s4o1:
    m "It would be a great honor to hear your ancestor's story, sister. If you would do me the kindness of sharing it."

    "For a few minutes, the wolf considers me wearily, as if deciding whether to trust me."
    "Then she gives a thoughtful little huff."

    w "{i}*Huff*{/i} Fine. If you are so curious, I will tell you. But watch that curiosity of yours, Witch. Many a sibling have followed their curiosity, only to have it ensnare them."

    "Well, that’s something I can definitely relate to."

    m "Thank you sister—your advice is good—I will remember it."
    w "Good. Here is my pack’s story. Heed it well. It all began many years ago, when my mother’s mother’s mother was barely older than a cub. This is her story. She still lived with her parents and brethren. One day, they smelt another wolf in their territory."
    w "They tracked him down and found a male. But rather than fight, he begged them to listen to him. He spoke of the hardship his pack faced in their old territory—competing for food and hiding from humans and their fire sticks."
    w "He said that he knew a place where they would be safe and have plenty of prey. He offered to lead them there. My mother’s mother’s mother’s father was very suspicious of this too-perfect promise."
    w "But my foremother... one look at this stranger, and she knew she would follow him to the ends of the earth. He was strong, but clever too—the cleverest wolf she had ever met. So, she begged her father to listen. And eventually, he agreed."
    w "The stranger eventually convinced three packs to follow him to this promised land. It was a long and painful journey—hiding by day, sneaking through the strange, busy human territories by night. It was terrifying."
    w "But over the journey, the stranger and my foremother fell in love and became mates. Eventually, the three packs reached this land. And at first, all seemed perfect. Their prey was plentiful and easy to catch."
    w "Occasionally a wolf would be killed by one of the human’s sticks, but it was rare enough that they could manage. For my foremother, life seemed like a dream. Her mate was sweet and kind and tough, and when they had pups, he was a wonderful father."
    w "Except for one thing: he was barely there during the time of the light while she slept. He usually returned soon after she woke to hunt, but when she woke during the middle of the light time, his side of the den was cold."
    w "And sometimes, when he was there, he'd be... different. None of that intelligent spark. More aggressive. Obsessed with the hunt. And then he wouldn't remember what happened during those times."
    w "So, one day, my foremother decided to follow him after the lighting of the sky to see where he went. It's hard to stalk a wolf like you'd stalk prey."
    w "She followed him through the shadows of the forest until they reached some land that the humans had grown tall metal bushes around, to keep creatures out. He went through a gap, and as she watched through the hedge, she saw the most terrible thing."
    w "As the light struck him, he began to change. He struggled and writhed, as if in pain, and his legs got longer, his face flattened. The pads of his paws distorted and stretched. His fur seemed to pull back into his body. Until there stood not her mate, but a human."
    w "He gathered some of the removable pelts you humans wear and walked off as my poor, foolish foremother tried to make sense of what she had seen. Eventually, after the {i}creature{/i} had left, she gathered the energy to return to the woods."
    w "Although she wanted to crawl back into her den with her pups—{i}his{/i} pups—and forget all that she had seen, she went out to the dens of all other packs in the forest. She gathered all the adult wolves that had once followed the {i}not-wolf{/i} to this land."
    w "She told them what she saw, and at first, they did not believe her. But they smelt her fear. Saw the horror in her eyes. And so they agreed to follow her and let her prove what she had seen."
    w "So, together, they went to the land where she had seen her mate's transformation and hid amongst the trees around the tall metal bushes. They waited all through the light time, until the safety of the darkness descended again, and they saw a human approach."
    w "A human who smelt of the wolf. They watched in horror as the man turned back into their brethren. But when he tried to leave the metal bushes enclosure, out stepped my foremother and the other wolves."
    w "They told him that if he dared show his face near any of their dens again, they would rip him apart. He was not a wolf and not their brother. The not-wolf begged them to listen, insisted that he was one of them, more one of them than one of the humans."
    w "But the wolves felt too deceived—they had trusted him, followed him far from their old dens—and he was not even a true wolf. He went to my foremother, asked for her to listen, to think of the love they shared—and the cubs."
    w "And she struck him. Bit deep into his neck until her mate’s blood dribbled into her mouth. Terrified and heartbroken, he ripped himself free and fled. They never saw him again."
    w "As for my foremother—life was difficult, raising her pups alone. No other wolf would come near her pups if they could help it, for they were his pups too. Sometimes, as they grew, she'd wake during the light time and find the den empty."
    w "She'd go outside and there her pups would be, staring up at the moon’s bright brother the same as she gazed at the moon. They were smart too, like their father. Often she'd find them too close to the human territories, watching them curiously."
    w "Of her five pups, only one found a mate, as most were too scared to go near them. And from the litters that came from that coupling, only one wolf reached adulthood, as the prey grew scarcer and the humans and their fire sticks crept into the woods more and more."
    w "And many of my blood fell to the allure of your people. And they were shot. And some just disappeared. The single surviving wolf of that line had only one litter—my litter."
    w "And of them, most have died or disappeared. The other packs have died out too. I am the last wolf left from the families the not-wolf brought here. And the last of {i}his{/i} descendants."
    w "Although many generations have diluted his blood in my body, I still feel it—the lure of the moon’s bright brother, the call of the humans and their strange above ground dens that reach as high as the trees."
    w "When my final hunt is over, my body given over for the scavengers to feast on, it gives me peace to know that no more of the not-wolf’s children will walk this earth."
    w "Sometimes, at the height of the light-time, I think I can feel him. In my blood. My heart. Longing to stretch out my paws until they lengthen. Pull myself up on my hind legs and reach up as high as I can. To feel the wind on my bare skin, free from fur."
    w "It's wrong to want these things. Unnatural. That urge will die with me."

    "Finally, the wolf falls silent, giving me time to mull over her story. It sounds like, many years ago, her pack encountered… No. No, they couldn't have. They're an incredibly regulated group of people. No way one could live out here."
    "But… it is very isolated..."
    "Well, dogs can have vivid imaginations, maybe wolves can too. But I probably shouldn't tell her that. Remember—respectful."

    m "Thank you for telling me your pack’s story. I am sorry for the pain of your past."
    w "Remember the tale, Witch. Remember that the face a stranger shows can be a well-made lie. And you never know what's behind it."
    m "Thank you, sister. I will not forget your advice."
    w "I need to go. The more time I spend in the light, the more I can feel the unnatural desire to… change."
    m "Go in peace, sister. Regardless of your family’s past, I wish you well. May your hunts be plentiful. May you always find fresh water. And when your time is done, may the earth accept your remains with open arms as you return to the Mother of all life."

    "The wolf cocks her head at me."

    w "What are these strange words you speak?"
    m "It's an ancient Witch blessing."
    w "Oh. Well... thank you. The same to you... sister."

    # SFX- Deep breath
    #      Padding feet

    "As the she-wolf stands, I close my eyes and take another deep breath."

    scene black with fade
    scene bg cg_witch with fade

    "When I open them again, she is gone."

    jump d1s5

# Wrong choice
label d1s4o2:
    m "You've piqued my curiosity! Come, sit comfortably. I'm most intrigued, be a friend and tell me your tale."

    "To my dismay, the she-wolf just glares at me."

    w "My story is not for your amusement, Witch. It is not a tale to tell your cubs when they cannot sleep. It is a painful history!"

    "Crap—she's offended. Back track, back track!"

    m "I'm sorry, sister. I did not mean to offend—"

    # SFX- Continuous low growling

    w "Do not call me sister. You may be a Witch, but you are still human."

    "Her words make my stomach knot, and my jaw clenches."

    m "I know many humans who would disagree."
    w "I don't care how petty your kind are—they are all the same. And my kind learnt not to trust them eons ago."

    "Before I can open my mouth to argue, she stands, her tail low and stiff, her body tense. Then she turns and walks off into the forest."

    scene black with fade

    jump d1s5