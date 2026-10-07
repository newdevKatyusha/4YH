label art_route_jinus(month, date):
    $ vince_vl_prefix = "audio/voices/Friends/Vince/Vincent_Month1/Vincent_Month1_"
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Vince_s Route/Month 1/Gwynette_Vince_Month1_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Vince/Month 1/" + player_voice_prefix + "_Vince_Month1_"

    call screen calendar(month, date, "Jinus", 27)
    scene bg art_room_noon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Vince - \nUctday, Jinus 27th, 1027 RD")

    "I’m not big on solitude. I didn’t think about it much back home, but then again, I was constantly surrounded by people – my mom, my siblings, my friends."
    "Even when I sat down at night to read a book or holed up in my room to doom scroll, my family’s muffled voices would filter from the next room, filling the silence– "
    "That, or Salem would throw open my door and barge inside."
    "At MIA, I’m surrounded by more people than ever: in class, in club meetings, sitting by the fire at House Lychester. But, it’s not the same. I don’t have a community here– at least, not yet– and I refuse to be that loser who follows around my one friend like a sad puppy."
    "So, long story long, I decided to join another club. I’ve been meaning to pick up drawing again, and now seems as good a time as any. After leaving the library, I figure I’ll pop into the art room to see if today’s Art Club meeting is still in session."

    show vince neutral at center with dissolve
    "But, when I arrive, I find only Vince, the elf boy I met on my tour. He stands at an easel working on an abstract piece, his hands and apron splattered with paint. Angry metal music filters from his earbuds, so loud I can hear it from the doorway."
    "He doesn’t look up when I enter– he just bangs his head to the beat and flicks his paintbrush, speckling the canvas before him with neon orange paint."
    "Feeling a little awkward, I clear my throat."
    
    vl alexis_vl_prefix 1
    a "Um, hey. Is the Art Club meeting today?"
    
    "Vince doesn’t respond. He just dips his paintbrush in a new color,  lime-green, and continues splattering away."
    stop music fadeout 1.0
    "Unsure how to proceed, I take a few steps toward him. Still, Vince doesn’t acknowledge me, so I reach out to touch his arm–"
    play music hatchling22 fadein 1.0
    with vpunch
    "Vince jolts, splattering me and my uniform in orange and green paint."
    "Grimacing, Vince rips out one earbud. Instead of apologizing, he wheels on me, enraged."
    
    vl vince_vl_prefix 1
    vin "The fuck’s your problem? You almost ruined my painting!"
    
    vl alexis_vl_prefix 2
    a "Well, you probably ruined my uniform, so we’re even."
    
    "Vince squints at me, recognition dawning."
    
    vl vince_vl_prefix 2
    vin "You’re that old new kid."
    
    vl alexis_vl_prefix 3
    a "I’m a fourth-year, thank you."
    
    "Uninterested, Vince pops his earbud back in, but I don’t budge."
    
    vl vince_vl_prefix 3
    vin "What are you still doing here?"
    
    vl alexis_vl_prefix 4
    a "I want to join Art Club. Sue said this was the regular meeting time."
    
    "He sighs with annoyance."
    
    vl vince_vl_prefix 4
    vin "Inspiration doesn’t conform to a weekly schedule. Club members come and go as they please."
    
    vl alexis_vl_prefix 5
    a "Okay, but the club calendar–"
    
    vl vince_vl_prefix 5
    vin "I know what the calendar says. We had to give them a formal meeting time to get funding. Any other questions?"
    
    vl alexis_vl_prefix 6
    a "Sue said something about a showcase?"
    
    vl vince_vl_prefix 6
    vin "We host showcases at the end of each trimester, yeah. I’m working on my piece for the fall one– or I was, until you ruined my focus."
    
    vl alexis_vl_prefix 7
    a "Sorry."
    
    stop music fadeout 1.0
    "Glowering, Vince presses play on his music and resumes painting. Whatever. I didn’t come here for him."
    hide vince with dissolve
    play music hatchling1 fadein 1.0
    "So, after washing some of the paint off my uniform. I head to the cabinets and raid them for supplies. Colored pencils are my medium of choice, but today, I settle for a frayed paintbrush and a few crusty bottles of acrylic paint."
    "Then, I set up my station across the room, as far from Vince as possible. I take a few minutes to sketch out my design – a massive black wolf, the emblem of House Blakesley, with my family crest behind it."
    "If it turns out well, I’ll mail it home to mom as a birthday gift. If it doesn’t… Well, House Lychester has a fireplace."
    "I set to work mixing my paints. But, before my brush touches the canvas–"
    
    show vince neutral at center with dissolve
    vl vince_vl_prefix 7
    vin "Here."
    
    "–I turn to see Vince, holding out a blue-handled paintbrush."
    
    vl vince_vl_prefix 8
    vin "The school brushes are dogshit. I’ve begged the Council for new supplies, but Reina led a vote against it. Probably because of what I did to the Magis Hall bathrooms… Anyway, use this."
    
    "I stare at the brush for a moment, taken aback by his generosity."
    
    vl vince_vl_prefix 9
    vin "You gonna take it or what?"
    
    vl alexis_vl_prefix 8
    a "Um, yeah. Thanks."
    
    vl vince_vl_prefix 10
    vin "There’s an art supply shop in town. They’re overpriced, but they run sales every month or so."
    
    vl alexis_vl_prefix 9
    a "I’ll check it out."
    
    "He lingers a moment, studying my sketch."
    
    vl vince_vl_prefix 11
    vin "You’re pretty good."
    
    vl alexis_vl_prefix 10
    a "Thank you. I haven’t drawn in years."
    
    vl vince_vl_prefix 12
    vin "I mean, the design’s derivative, but the raw talent’s there."
    
    "There’s the backhanded comment I was waiting for. Before I can respond, the door to the art room opens."
    
    show vince neutral at character_pos3 with move
    show gwynette neutral at character_pos6 with dissolve
    vl gwynette_vl_prefix 1
    gw "VV!"
    
    "Gwynette barrels across the room. She wraps her arms around Vince."
    
    vl vince_vl_prefix 13
    vin "You’re gonna get paint on your uniform."
    
    vl gwynette_vl_prefix 2
    gw "Good."
    
    "Vince cracks a smile and drapes an arm around her. Around Gwynette, he’s a completely different person."
    "After a moment, Gwynette releases Vince and turns to me with a smile."
    
    if eval(a.name)[0] == "Alexis":
        vl gwynette_vl_prefix 3A
    else:
        vl gwynette_vl_prefix 3B
    gw "Hi! [a], right?"
    
    vl alexis_vl_prefix 11
    a "Yup. And you’re Gwynette?"
    
    "She nods."
    
    vl gwynette_vl_prefix 4
    gw "That’s right. You’re joining the Art Club, then?"
    
    vl alexis_vl_prefix 12
    a "Mhmm. Are you a member, too?"
    
    vl gwynette_vl_prefix 5
    gw "Oh, no. I’m strictly a singer. Speaking of…"
    
    "She turns to Vince."
    
    vl gwynette_vl_prefix 6
    gw "I told my choir friends we’d meet at the Amity twenty minutes ago."
    
    "Vince groans."
    
    vl vince_vl_prefix 14
    vin "Ugh, why don’t you go without me? You know I’m not religious."
    
    vl gwynette_vl_prefix 7
    gw "We’re not going to services. This is just dinner."
    
    vl vince_vl_prefix 15
    vin "Yeah, but I don’t get along with church people."
    
    vl gwynette_vl_prefix 8
    gw "I’m a church person."
    
    vl vince_vl_prefix 16
    vin "You’re different."
    
    "Gwynette rolls her eyes and shoots me a look."
    
    vl alexis_vl_prefix 13
    a "I can wash your brushes if you’d like."
    
    vl vince_vl_prefix 17
    vin "You know, I was almost starting to like you."
    
    vl alexis_vl_prefix 14
    a "You were?"
    
    vl vince_vl_prefix 18
    vin "I said \"almost.\" "
    
    "Gwynette loops her arm around Vince."
    
    vl gwynette_vl_prefix 9
    gw "C’mon, let’s get you cleaned up."
    
    "Reluctantly, Vince removes his apron and allows Gwynette to wipe the speckled paint from his cheeks. Then, the two gather their things. I call out as they head for the door."
    
    vl alexis_vl_prefix 15
    a "Have fun!"
    
    hide gwynette with dissolve
    hide vince with dissolve
    "Vince flips me off and disappears into the hallway."
    "Smirking to myself, I return to my painting."
    stop music fadeout 1.0
    
    call art_route_dallinus("Jinus", 27) from _call_art_route_dallinus

label art_route_dallinus(month, date):
    $ vince_vl_prefix = "audio/voices/Friends/Vince/Vincent_Month2/Vincent_Month2_"
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Vince_s Route/Month 2/Gwynette_Vince_Month2_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Vince/Month 2/" + player_voice_prefix + "_Vince_Month2_"

    call screen calendar(month, date, "Dallinus", 6)
    scene bg art_room_noon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Vince - \nLenday, Dallinus 6th, 1027 RD")
    
    "Somehow, Vince didn’t scare me off from Art Club. So, I’ve been stopping by the art room in my free time."
    "People really do come and go as they please. Sometimes, I show up to find a smattering of fellow club members. We chat and compare notes as we work. Other times, the room is empty, and I take advantage of the stillness to sketch and mentally reset."
    "But, more often than not, it’s just Vince: glued to his easel, locked into his latest piece. We talk a little when he comes up for air, but most of the time, he’s dead silent, save the metal music filtering from his earbuds."
    "So, today, when I approach the art room after class, I’m surprised to hear two voices carry into the hallway."
    
    vl vince_vl_prefix 1
    vin "If you had just checked the art room–"
    
    vl gwynette_vl_prefix 1
    gw "VV… "
    
    stop music fadeout 1.0
    "Is that Gwynette? I’ve never heard her sound so serious. Curious, I creep closer."

    show gwynette neutral at character_pos5 with dissolve
    show vince neutral at character_pos2 with dissolve
    play music hatchling14 fadein 1.0
    "Gwynette stands facing Vince, her expression uncharacteristically solemn. Vince is equally exasperated."
    
    vl gwynette_vl_prefix 2
    gw "I called you five times, and we were already late for the movie. You expected me to walk back across campus in the rain? "
    
    vl vince_vl_prefix 2
    vin "No. Look, I’m sorry. I had a really shitty day, and I had to get it out of my system. I just… lost track of time."
    
    vl gwynette_vl_prefix 3
    gw "You could have talked to me."
    
    vl vince_vl_prefix 3
    vin "That’s not how it works."
    
    "Gwynette sighs with frustration."
    
    vl gwynette_vl_prefix 4
    gw "VV, you know I love you, but I can’t keep begging for attention like a needy puppy…"
    
    "One of my classmates appears down the hall. They wave my direction."
    anek2 "Hey, [a]!"
    
    "Sheepishly, I wave back."
    stop music fadeout 1.0
    with hpunch
    "At the sound of my voice, Gwynette and Vince turn and notice me in the doorway. Gwynette plasters on a smile."
    play music hatchling1 fadein 1.0

    vl gwynette_vl_prefix 5
    gw "BB! I didn’t see ya there."
    
    vl alexis_vl_prefix 1
    a "Hey, uh, I can come back–"
    
    vl gwynette_vl_prefix 6
    gw "Nah, that’s okay. I was just heading out."
    
    "She shoulders her bag and heads for the door without looking at Vince."
    
    hide gwynette with dissolve
    vl vince_vl_prefix 4
    vin "Gwyn–"

    stop music fadeout 0.5
    play music hatchling14 fadein 1.0
    "But, she’s already gone. Groaning, Vince sinks into his stool. He sweeps a hand across the bottom of his easel, sending some paintbrushes and a pencil clattering to the ground. Then, he buries his face in his hands."
    
    show vince neutral at center with move

    vl alexis_vl_prefix 2
    a "What ha–"
    
    vl vince_vl_prefix 5
    vin "I don’t want to talk about it."
    
    "Throwing up my hands in surrender, I head to my usual work station. I pull out my latest piece – a sketch of Magis Hall in the autumn light - and a fresh set of colored pencils."
    "After adding some detail to the front door, I look over at Vince. He remains slumped in his stool, near-catatonic. I clear my throat."
    
    vl alexis_vl_prefix 3
    a "Still don’t want to talk about it?"
    
    "Sighing, Vince turns to face me."
    
    vl vince_vl_prefix 6
    vin "Gwynette and I were supposed to see a movie in town last night, but I missed it."
    
    vl alexis_vl_prefix 4
    a "Because you were painting?"
    
    "Vince nods."
    
    vl vince_vl_prefix 7
    vin "She {b}wanted{/b} to go dancing at The Amity. They have live music or some shit on Nydays and Zyndays. But, I hate dancing, so Gwynette agreed to see this horror movie instead."
    vl vince_vl_prefix 8
    vin "I guess she waited for thirty minutes and called a bunch of times, but I didn’t pick up."
    
    vl alexis_vl_prefix 5
    a "You didn’t have your phone? You always listen to music when you paint."
    
    vl vince_vl_prefix 9
    vin "It was on \"do not disturb.\""
    
    vl alexis_vl_prefix 6
    a "Well, I’m sure it’ll blow over. It’s not like this happens all the time."
    
    "Vince looks away, sheepish."
    
    vl alexis_vl_prefix 7
    a "…Or does it?"
    
    "Vince sighs."
    
    vl vince_vl_prefix 10
    vin "Not all the time, but enough to make me an asshole. I dunno, it’s like, I sit at my easel, and time just… stops. You could literally scream my name, and I wouldn’t hear it. What the fuck is wrong with me? "
    
    "He buries his face in his hands again. I set down my colored pencil and walk toward him. Unsure what else to do, I reach out to place a hand on his shoulder. He speaks without looking up."
    
    vl vince_vl_prefix 11
    vin "Don’t touch me."
    
    vl alexis_vl_prefix 8
    a "Sorry."
    
    "I quickly retract my hand."
    
    vl alexis_vl_prefix 9
    a "Look, Gwynette knows how passionate you are about your art. Maybe there’s a way to make it up to her?"
    
    vl vince_vl_prefix 12
    vin "Like what?"
    
    vl alexis_vl_prefix 10
    a "What about that dance night at the Amity? You could take her on Zynday."
    
    vl vince_vl_prefix 13
    vin "I told you, I hate dancing."
    
    vl alexis_vl_prefix 11
    a "Exactly. It’ll show her how much you care."
    
    "Vince frowns, mulling this over… "
    hide vince with dissolve
    stop music fadeout 1.0
    
    call screen calendar("Dallinus", 6, "Dallinus", 9)
    scene bg mainstreet_noon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Vince - \nUctday, Dallinus 9th, 1027 RD")

    "Over the next couple days, I’m too busy with homework to pop by the art room. I’ve almost forgotten about Vince and Gwynette’s quarrel when, on the way to potion brewing– "
    
    if eval(a.name)[0] == "Alexis":
        vl gwynette_vl_prefix 7A
        gw "[a]!"
    else:
        vl gwynette_vl_prefix 7B
        gw "BB!"
    
    show vince happy at character_pos2 with dissolve
    show gwynette neutral at character_pos5 with dissolve
    "–I turn to see Vince and Gwynette, cuddled up together on a bench. I walk over to them."
    
    vl alexis_vl_prefix 12
    a "Hey, lovebirds. How are you two?"
    
    vl gwynette_vl_prefix 8
    gw "Amazing! VV took me out to the Amity last night. Did you know they have dancing on Istdays? "
    
    "I try to hide my smirk."
    
    vl alexis_vl_prefix 13
    a "Really? I didn’t know Vince was a dancer."
    
    "Vince flips me off. Gwynette giggles."
    
    vl gwynette_vl_prefix 9
    gw "Right? Took him a bit to warm up, but by the end of the night, he didn’t want to leave. He begged the band to play another song."
    
    vl vince_vl_prefix 14
    vin "That’s not true!"
    
    vl gwynette_vl_prefix Laugh
    "Gwynette and I laugh."
    
    vl alexis_vl_prefix 14
    a "Well, I should get going. See you two around."
    
    "Vince and Gwynette bid me farewell. As I walk away, Gwynette curls up against Vince’s arm. He peers over the top of her head to meet my eyes and mouths two words: \"Thank you.\""
    "Smiling, I flash him a thumbs–up and head to class."
    stop music fadeout 1.0
    
    # jump to main club route dallinus
    $ renpy.call(chosen_club + "_route_dallinus", "Dallinus", 9)
    #jump art_route_dyalt

label art_route_dyalt(month, date):
    $ vince_vl_prefix = "audio/voices/Friends/Vince/Vincent_Month4/Vincent_Month4_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Vince/Month 4/" + player_voice_prefix + "_Vince_Month4_"

    call screen calendar(month, date, "Dyalt", 13)
    scene bg mainstreet_noon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Vince - \nLenday, Dyalt 13th, 1027 RD")

    "I never expected much out of Vince. But, over the past few months of Art Club, we’ve become unexpected friends. Today, we both had a free afternoon, so we headed into town to shop for art supplies."
    "As usual, I gravitated toward the cheapest paints and pencils possible, absolutely horrifying Vince."
    
    show vince neutral at center with dissolve
    vl vince_vl_prefix 1
    vin "You’re not using that shit on your showcase piece."
    
    vl alexis_vl_prefix 1
    a "What? I’m on a budget."
    
    "Aghast, Vince confiscated my basket and insisted on buying me three tubes of his preferred brand of paint. I tried to pay, but he refused."
    
    vl vince_vl_prefix 2
    vin "You can get lunch."
    
    "So, shopping bags in tow, we’re en route to The Amity. As we walk down the street, Vince’s phone buzzes. Checking the screen, he groans."
    
    show vince annoyed at center with dissolve

    vl alexis_vl_prefix 2
    a "Who is it?"
    
    vl vince_vl_prefix 3
    vin "My dad. Hang on."
    
    hide vince with moveoutleft
    "He steps away and answers. Not wanting to invade his privacy, I keep my distance, but I can tell it’s not a pleasant conversation. Vince gesticulates with annoyance, waving his black-painted fingernails as he speaks."
    "Eventually, he hangs up and storms back over to me, his expression grim."
    
    show vince neutral at center with moveinleft
    vl vince_vl_prefix 4
    vin "Sorry about that."
    
    vl alexis_vl_prefix 3
    a "It’s fine. Everything okay?"
    
    vl vince_vl_prefix 5
    vin "Not really, but let’s go inside. It’s cold as shit out here."
    
    "I follow Vince down the street, into The Amity."
    # TODO: Update BG once The Amity is available

    scene bg mainstreet_afternoon

    show vince neutral at center with dissolve
    "The cafe is packed – no surprise on a chilly day like this. Locals and IAH students stuff their faces with food or sip hot beverages as they study."
    
    vl vince_vl_prefix 6
    vin "Over here."
    
    "Vince leads up to a corner table. I study him as he scans the menu, trying to get a read on his mood. He speaks without looking up."
    
    vl vince_vl_prefix 7
    vin "Stop staring at me."
    
    vl alexis_vl_prefix 4
    a "Sorry."
    
    "A waitress approaches to take our order. I order a bowl of the soup du jour with a side of cheese fries. (It’s been a long week.) Vince just requests a cappuccino."
    
    vl alexis_vl_prefix 5
    a "Lunch is on me, remember?"
    
    vl vince_vl_prefix 8
    vin "I’m not hungry."
    
    "Satisfied, the waitress walks off. I wait for her to be out of earshot before turning back to Vince."
    
    vl alexis_vl_prefix 6
    a "So, you gonna tell me what’s up?"
    
    vl vince_vl_prefix 9
    vin "Just my parents being assholes. Nothing new."
    
    vl alexis_vl_prefix 7
    a "What did they want?"
    
    vl vince_vl_prefix 10
    vin "Goude told them I’ve been missing class, so they’re threatening to pull me out of Art Club."
    
    vl alexis_vl_prefix 8
    a "Ugh, I’m sorry. How much class did you miss?"
    
    vl vince_vl_prefix 11
    vin "I skipped last week."
    
    vl alexis_vl_prefix 9
    a "All week?"
    
    vl vince_vl_prefix 12
    vin "Whose side are you on?"
    
    vl alexis_vl_prefix 10
    a "I’m not judging. Just, why?"
    
    vl vince_vl_prefix 13
    vin "Because it’s bullshit. I didn’t ask to come here. My art’s the one thing that’s keeping me from exploding, and now they’re threatening to take that away."
    
    vl alexis_vl_prefix 11
    a "Wait, you didn’t want to come here?"
    
    vl vince_vl_prefix 14
    vin "Gods no. I got kicked out of my old school back in Archos. I had some… issues with the other kids. After that, I wanted to go to art school, but they sent me to this shithole instead."
    
    vl alexis_vl_prefix 12
    a "Why MIA? Why not somewhere else in Archos? "
    
    vl vince_vl_prefix 15
    vin "They thought the change of scenery would be good for me, plus MIA’s known for their science program."
    
    vl alexis_vl_prefix 13
    a "Are your parents scientists?"
    
    vl vince_vl_prefix 16
    vin "My mom’s a surgeon. My dad’s a theologist. Classic elf rationalism bullshit. You can imagine their reaction when I got into painting."
    
    vl alexis_vl_prefix 14
    a "So, they thought if they sent you to MIA, you’d have a change of heart?"
    
    vl vince_vl_prefix 17
    vin "I guess, but I’m a year in and nothing’s changed. I hate everything about this godsdamn place."
    
    vl alexis_vl_prefix 15
    a "What about Gwynette?"
    
    vl vince_vl_prefix 18
    vin "Alright, fine. There’s one good thing about this place."
    
    vl alexis_vl_prefix 16
    a "What about me?"
    
    vl vince_vl_prefix 19
    vin "You’re okay."
    
    "I smile. That’s the best I’ll get out of him. As we wait for our order, Vince taps on the table impatiently. I can tell the phone call is still weighing on him."
    
    vl alexis_vl_prefix 17
    a "Maybe you should play along."
    
    vl vince_vl_prefix 20
    vin "Huh?"
    
    vl alexis_vl_prefix 18
    a "I mean, appease your parents. Go to class. Then, they won’t pull you out of Art Club."
    
    vl vince_vl_prefix 21
    vin "Or, I could keep skipping and convince Goude to kick me out."
    
    "Before I can retort, the door to the cafe opens, revealing Headmaster Goude."
    
    vl alexis_vl_prefix 19
    a "Speak of the Fiend."
    
    stop music fadeout 2.0
    "Vince turns, following my eyeline. Seeing the headmaster, his eyes go wide."
    play music hatchling22 fadein 1.0
    
    vl vince_vl_prefix 22
    vin "Fuck."
    
    "Vince ducks down under the table as Headmaster Goude crosses the restaurant, unwinding his scarf. I whisper to Vince."
    
    vl alexis_vl_prefix 20
    a "I thought you wanted to be–"
    
    vl vince_vl_prefix 23
    vin "Shh!"

    "Oblivious, the headmaster sets down his coat and heads to the restroom."
    "Vince rises, sighing with relief."
    
    vl alexis_vl_prefix 21
    a "Thought you wanted to be kicked out?"
    
    vl vince_vl_prefix 24
    vin "I do, but not before I’ve cleared out the art room."
    
    "He grabs his bag."
    
    vl alexis_vl_prefix 22
    a "Where are you going?"
    
    vl vince_vl_prefix 25
    vin "Back to Crowlin."
    
    vl alexis_vl_prefix 23
    a "What about your cappuccino?"
    
    vl vince_vl_prefix 26
    vin "Keep it… Oh, catch."
    
    "He grabs my paints from his shopping bag and tosses them at me. I scramble to gather them as he organizes his things."
    
    vl vince_vl_prefix 27
    vin "See ya at Art Club."
    
    vl alexis_vl_prefix 24
    a "See ya–"
    hide vince with dissolve
    
    "But, he’s already gone. As Vince disappears outside, the waitress reappears with his cappuccino. Sighing, I take a sip."
    stop music fadeout 1.0

    # jump to main club route dyalt
    $ renpy.call(chosen_club + "_route_dyalt", "Dyalt", 13)
    #jump art_route_neralt

label art_route_neralt(month, date):
    $ vince_vl_prefix = "audio/voices/Friends/Vince/Vincent_Month5/Vincent_Month5_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Vince/Month 5/" + player_voice_prefix + "_Vince_Month5_"
    
    call screen calendar(month, date, "Neralt", 25)
    scene bg art_room_noon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Vince - \nZaeday, Neralt 25th, 1027 RD")

    "After our shopping day, Vince decided to take my advice. He’s attending classes again– at least, enough classes to keep his parents off his back– and he’s been more prolific than ever."
    "I swear, the guy must have churned out a new painting or sculpture every other day this week."
    stop music fadeout 2.0
    "All in all, my friend’s been in pretty high spirits…"
    show vince annoyed at center with dissolve
    play music hatchling15 fadein 1.0
    "...so, when Vince storms into the art room today and chucks his bag across the room, I’m taken aback."
    
    vl alexis_vl_prefix 1
    a "Hey, is everything–?"
    
    "Before I can finish, Vince barrels over to his easel and snatches up his work-in-progress. He tries to snap the canvas in two, but it won’t yield. Instead, he grabs his palette knife."
    
    vl alexis_vl_prefix 2
    a "Whoa!"
    
    "I rush over to Vince– an unwise move, considering he’s armed and dangerous. (The school palette knives probably aren’t that sharp, but you never know.)"
    "Thankfully, Vince seems not to notice me. Instead, he stabs the palette knife into his painting, shouting and destroying his work in progress. He punctuates each word with a slash."
    
    vl vince_vl_prefix 1
    vin "FUCK! THIS! PLACE!"

    stop music fadeout 1.0
    voice sustain
    "Eventually, he wears himself out."
    play music hatchling10 fadein 1.0
    voice sustain
    "Breathless, Vince sinks down onto his stool and buries his face in his hands, still holding the palette knife."
    "I eye my friend with concern. I’ve seen Vince upset, but never like this. Tentatively, I approach him."
    
    vl alexis_vl_prefix 3
    a "Um, you wanna give me that knife?"

    "Without speaking, Vince drops the palette knife onto the ground. I retrieve it and drop it into the pocket of my apron."
    "At this point, I know not to push Vince. He’ll talk when he’s ready. So, I take a seat nearby and wait. Eventually, he sits upright."
    
    vl vince_vl_prefix 2
    vin "It’s over."
    
    vl alexis_vl_prefix 4
    a "What’s over? You and Gwynette?"
    
    "He nods."
    
    vl alexis_vl_prefix 5
    a "What happened? Did you miss another date?"
    
    vl vince_vl_prefix 3
    vin "I missed her performance."
    
    vl alexis_vl_prefix 6
    a "Shit. Were you painting?"
    
    vl vince_vl_prefix 4
    vin "No, that’s the worst part– I knew her show was in the morning, so I planned to go right back to Crowlin after dinner yesterday and go to bed. But, I woke up feeling like shit– "
    
    vl alexis_vl_prefix 7
    a "Your parents?"
    
    vl vince_vl_prefix 5
    vin "No, nothing like that. I just have these days where everything feels impossible. Like, I can’t even get out of bed."
    
    "I eye him with concern but hold my tongue. Vince continues."
    
    vl vince_vl_prefix 6
    vin "Anyway, I forced myself to go to class, and after, I was feeling even worse. So, I decided to stop by the art room– just for a couple hours. But, I ended up painting past curfew, and then I slept through my alarm…"
    
    vl alexis_vl_prefix 8
    a "Oh no…"
    
    vl vince_vl_prefix 7
    vin "Yeah. So, obviously, I missed Gwynette’s performance… Fuck, I’m a piece of shit."
    
    vl alexis_vl_prefix 9
    a "Alright, just back up. When did you talk to Gwynette?"
    
    vl vince_vl_prefix 8
    vin "Just now. She came to Crowlin after her show. I’d never seen her that upset before."
    
    vl alexis_vl_prefix 10
    a "So, she broke up with you?"
    
    vl vince_vl_prefix 9
    vin "Not exactly… She said she was \"worried about my mental health\" and wants me to \"talk to someone.\" "
    
    vl alexis_vl_prefix 11
    a "Okay. Did you agree?"
    
    "He shakes his head."
    
    vl alexis_vl_prefix 12
    a "Then, what did you say?"
    
    vl vince_vl_prefix 10
    vin "That she’s too good for me and deserves someone who will show up for her."
    
    vl alexis_vl_prefix 13
    a "Wait, you broke up with her?"
    
    vl vince_vl_prefix 11
    vin "I don’t know. I guess?"
    
    vl alexis_vl_prefix 14
    a "Vince!"
    
    vl vince_vl_prefix 12
    vin "Look, I didn’t mean to break up with her. I just felt so shitty, and it’s true. She does deserve better."
    
    "Again, he buries his face in his hands."
    
    vl vince_vl_prefix 13
    vin "I’m so fucking stupid."
    
    vl alexis_vl_prefix 15
    a "Alright, first thing’s first, you’ve gotta stop beating yourself up. It’s not helping anything."
    
    vl vince_vl_prefix 14
    vin "I’m not asking for help."
    
    vl alexis_vl_prefix 16
    a "Which leads me to my next point: Gwynette’s right. You should be talking to someone."
    
    vl vince_vl_prefix 15
    vin "I’ve tried. It doesn’t work on me."
    
    vl alexis_vl_prefix 17
    a "Then, you probably haven’t found the right person. Look, when my dad died, I felt terrible. There were days where I couldn’t even muster the strength to brush my teeth or change my clothes…"

    vl vince_vl_prefix 16
    vin "But, that’s part of the problem– it’s not like I lost someone or something terrible happened. I’ve always been like this, even before MIA. That’s why I started painting in the first place."
    
    vl alexis_vl_prefix 18
    a "And, it’s great that you have an outlet. But, it’s clearly not enough. You know this isn’t healthy, right?"
    
    vl vince_vl_prefix 17
    vin "Obviously."
    
    vl alexis_vl_prefix 19
    a "Look, I’m not trying to make you feel worse. I know you didn’t ask to be depressed or to come to MIA or have your parents constantly on your ass. But, for now, you’re here, and you do have the power to make the most of it and set things right."
    
    vl vince_vl_prefix 18
    vin "No way Gwynette’s taking me back."
    
    vl alexis_vl_prefix 20
    a "Maybe, maybe not. But, you can still work on yourself. And, like it or not, I’m not going anywhere."
    
    vl vince_vl_prefix 19
    "Vince sits there in silence for a moment. Then, he lets out a sigh."
    
    vl vince_vl_prefix 20
    vin "I should go."
    
    vl alexis_vl_prefix 21
    a "Okay. You wanna grab dinner?"
    
    "He shakes his head."
    
    vl vince_vl_prefix 21
    vin "I just need some time to process… everything."
    
    vl alexis_vl_prefix 22
    a "Alright, well, you know where to find me."
    
    "With a small smile, Vince rises. He takes in his ruined painting with a sigh."
    
    vl vince_vl_prefix 22
    vin "Damn. I really liked that one."
    
    vl alexis_vl_prefix 23
    a "Maybe you could fill in the slashes with something: another color, gold leaf, some glitter–"
    
    vl vince_vl_prefix 23
    vin "Yeah, you lost me."
    
    vl vince_vl_prefix 24
    "We laugh a little, in spite of ourselves. Vince starts to gather his fallen supplies, but I stop him."
    
    vl alexis_vl_prefix 24
    a "You go ahead. I’ll clean up."
    
    vl vince_vl_prefix 25
    vin "You sure?"
    
    vl alexis_vl_prefix 25
    a "Yeah. Get some rest."
    
    vl vince_vl_prefix 26
    vin "Thanks. Well… have a good night, [a]."
    
    vl alexis_vl_prefix 26
    a "You, too."

    hide vince with dissolve
    stop music fadeout 1.0
    "I watch Vince disappear from the classroom. There’s still no telling what the fallout will be with Gwynette, but I’m glad I could talk him down. I just hope he takes my advice to heart."

    call student_council_exalt("Neralt", 25) from _call_student_council_exalt_2
    #jump art_route_exalt

label art_route_exalt(month, date):
    $ vince_vl_prefix = "audio/voices/Friends/Vince/Vincent_Month6/Vincent_Month6_"
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Vince_s Route/Month 6/Gwynette_Vince_Month6_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Vince/Month 6/" + player_voice_prefix + "_Vince_Month6_"

    call screen calendar(month, date, "Exalt", 22)
    scene bg dorm_common_morning with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Vince - \nZaeday, Exalt 22nd, 1027 RD")

    "I awake this morning to find House Lychester buzzing with excitement. It’s the Zaeday before the Week of Life– AKA, one week until vacation."
    "And, as much as I love MIA, a week at home with Mom, my siblings, and zero responsibilities  is exactly what I need right now."
    "Fueled by holiday cheer, I decide to stroll into town to grab coffee and admire the decorations."
    
    scene mainstreet_noon with fade

    "Despite the early hour, Huntsdale is already packed. Students and locals stroll down the main street, many en route to morning services."
    "In the middle of the crowd, I spot a familiar face."
    
    show vince neutral at center with dissolve
    pause 1.0

    vl alexis_vl_prefix 1
    a "Vince!"
    
    "Confused, my friend looks around. Spotting me, he weaves through the horde of pedestrians, making his way toward me."
    
    vl vince_vl_prefix 1
    vin "'Scuse me… Sorry… "
    
    "Breathless, he emerges from the crowd. Seeing Vince up close, my jaw drops."
    "Since the night of the breakup, Vince has taken my advice. He’s been talking with the school counselor and making an all-around effort to better himself."
    "Still, this is the most put-together I’ve ever seen my friend. His hair is styled, his pants are ironed, and his blazer is distinctly paint-free. In one hand, he carries a wrapped gift."
    
    vl vince_vl_prefix 2
    vin "Why are you staring at me like that?"
    
    vl alexis_vl_prefix 2
    a "Nothing. Just didn’t expect to see you out and about this early."
    
    vl vince_vl_prefix 3
    vin "Thought I’d catch the morning service."
    
    vl alexis_vl_prefix 3
    a "Aren’t you an atheist?"
    
    vl vince_vl_prefix 4
    vin "Yeah, but Gwynette’s performing. I don’t know if she’ll want to see me, but–"
    
    vl alexis_vl_prefix 4
    a "I’m sure she’ll appreciate the effort."
    
    vl vince_vl_prefix 5
    vin "Gods, if my parents saw me now: going to church, pining over a good Nyrellan girl…"
    
    vl alexis_vl_prefix 5
    a "Are they religious?"
    
    vl vince_vl_prefix 6
    vin "They’re Archosian elves. Of course they’re religious. Growing up, they dragged my ass to church every Zaeday."
    
    vl alexis_vl_prefix 6
    a "I’d love to see that."
    
    vl vince_vl_prefix 7
    "We share a laugh. Then, Vince averts his eyes, a little sheepish."
    
    vl vince_vl_prefix 8
    vin "Actually, now that you mention it, would you mind… coming with me?"
    
    "I hesitate a moment, surprised by his request."
    
    vl vince_vl_prefix 9
    vin "You can say no. Just, this shit makes me uncomfortable, and–"
    
    vl alexis_vl_prefix 7
    a "I’ll go."
    
    vl vince_vl_prefix 10
    vin "Really?"
    
    vl alexis_vl_prefix 8
    a "Yeah. Not like I’ve got anything better to do."
    
    stop music fadeout 2.0
    "Smiling a little, Vince leads the way to the chapel."

    scene bg chapel_day with fade
    show vince neutral at center with dissolve
    play music hatchling21 fadein 1.0

    "The chapel is packed with worshippers, just like I expected. As we weave through the crowd, Vince frowns at a stain on his blazer."
    
    vl vince_vl_prefix 11
    vin "Ugh, is that hot chocolate? Godsdamn kids…"
    
    "An older lady turns to shoot Vince a dirty look. I whisper to him."
    
    vl alexis_vl_prefix 9
    a "I don’t think you’re supposed to curse in the chapel."
    
    vl vince_vl_prefix 12
    vin "Whatever. The gods should be grateful I’m here."
    hide vince with dissolve

    "Suppressing a smirk, I follow Vince in search of a seat. As we head toward the back of the chapel–"
    
    s "[a]! Over here!"
    
    show sue neutral at character_pos1 with dissolve
    show reina neutral at character_pos4 with dissolve
    show ylva neutral at character_pos7 with dissolve
    "–I turn to see Sue waving at me from the one of the front rows. Seated beside her are Reina and Ylva."

    scene bg chapel_day with dissolve
    "I turn to Vince."
    
    vl alexis_vl_prefix 10
    a "Wanna sit with them?"
    
    show vince neutral at center with dissolve
    vl vince_vl_prefix 13
    vin "And deal with Gwynette’s friends’ death-glares for two hours? No thanks."
    
    vl alexis_vl_prefix 11
    a "It’s that or standing for two hours."
    
    "I gesture to the back of the chapel. At least 20 people stand arm to arm, smushed against the back wall. Vince groans, relenting."
    
    vl vince_vl_prefix 14
    vin "Fine. You first."
    hide vince with dissolve
    
    "I lead the way to Sue and company. Taking our seats, we exchange pleasantries with our classmates– or, more accurately, I exchange pleasantries while Vince ignores glares from Ylva."
    "Eventually, the priest arrives, and a hush falls over the chapel. When the priest lifts his chin, I double-take and whisper to Vince."
    
    vl alexis_vl_prefix 12
    a "Is that Instructor Wilson?"
    
    show vince neutral at character_pos1 with dissolve
    vl vince_vl_prefix 15
    vin "Who’s Instructor Wilson?"
    
    show ylva neutral at character_pos7 with dissolve
    "Ylva lets out a sigh of annoyance, but Sue leans to whisper in my ear."
    
    show sue neutral at character_pos4 with dissolve
    s "He gives all the weekly sermons. As a matter of fact–"
    
    hide ylva
    show reina worried at character_pos7
    r "Sue, please, I’m trying to listen."
    show sue embarrassed_closed
    
    "With an apologetic shrug, Sue leans back in her seat."
    "Truth be told, I tune out most of Instructor Wilson’s words. It’s not until I hear Gwynette’s name that I snap back to reality."
    scene bg chapel_day with dissolve
    show gwynette neutral at center with dissolve
    "Instructor Wilson steps aside, allowing Gwynette to take the stage. Beside me, Vince straightens."
    "Gwynette looks out at the crowd. Seeing her friends, she smiles and waves. Then, noticing Vince, she falters, caught off guard. Her eyes glisten ever so slightly with tears. Collecting herself, she clears her throat."
    
    vl gwynette_vl_prefix 1
    gw "Good morning, everyone. Thank you all for joining us here today, on this sacred day, at the beginning of this sacred week."
    vl gwynette_vl_prefix 2
    gw "No doubt, all of us are going to feel all sorts of things during this week, as we spend time with our loved ones and reflect on everything we’ve lost."
    vl gwynette_vl_prefix 3
    gw "So please, allow me to sing you a song that’s near and dear to my heart."
    
    "With that, she begins to sing the Nyrellan Hymn."
    show gwynette singing at center with dissolve
    
    "Instantly, I freeze. It’s been years since I last heard this song, and I’m unprepared for the tidal wave of memories. Images of my father’s funeral flash through my mind: the wooden casket, the sea of mourners, my mother singing through a veil of tears."
    "But, little by little, the painful memories subside, replaced by flashes of a simpler time. I see myself sitting on the couch– sandwiched between Mother, Father, Salem, and Skylar, watching movies and stuffing my face with popcorn until my stomach hurts."
    "I see Salem and Skylar as cherubic toddlers, nestled under the covers while my parents sing the same hymn, hoping to lull them to sleep."
    "And, finally, I see my father holding my own small body close, singing to me as if I were the most precious thing in the world."
    stop music fadeout 2.0
    "I sniffle a little, fighting tears, and one look around the chapel confirms that I’m not alone. Beside me, Sue and Reina dab the corners of their eyes."
    play music hatchling10 fadein 1.0
    "Finishing her song, Gwynette drops down to one knee, too absorbed in her worship to notice her standing ovation."
    "Beside me, Vince slips out of his seat. Before I can ask where he’s going, he’s at Gwynette’s side, offering his hand. Smiling, she accepts, and he leads her over to where we’re sitting."
    "The audience goes silent as Instructor Wilson takes the stage once more. I lean to whisper to Gwynette."
    
    vl alexis_vl_prefix 13
    a "You were incredible."
    
    show gwynette neutral at center with dissolve
    vl gwynette_vl_prefix 4
    gw "Thanks, BB."
    
    "As Instructor Wilson starts to speak, Vince and Gwynette remain hand-in-hand."
    "After the service, most of the audience lingers. While Gwynette chats with her friends and congregants, Vince remains beside her, but his energy has shifted. He’s antsy, fidgeting with his blazer."
    show gwynette neutral at character_pos5 with move
    show vince neutral at character_pos2 with dissolve
    "Noticing him, Gwynette smirks."
    
    vl gwynette_vl_prefix 5
    gw "I know that look. You’re inspired."
    
    "Vince nods."
    
    vl vince_vl_prefix 16
    vin "You looked so beautiful up there, lit by those stained glass windows. I bet I could use watercolors to recreate it…"
    
    "Then, flustered, he clears his throat."
    
    vl vince_vl_prefix 17
    vin "…But, it can wait."
    
    vl gwynette_vl_prefix 6
    gw "Tell you what, you go ahead to the Art Room, and I’ll come find you when I’m finished."
    
    vl vince_vl_prefix 18
    vin "You sure? "
    
    vl gwynette_vl_prefix 7
    gw "Positive."
    
    "Grateful, Vince kisses her, then practically sprints for the door. Gwynette calls after him."
    
    vl gwynette_vl_prefix 8
    gw "Keep your phone on!"
    
    "He flashes a thumbs-up as he disappears through the door."
    hide vince with dissolve
    "Gwynette and I can’t help but laugh."
    
    vl gwynette_vl_prefix 9
    gw "He’s looking better."
    
    vl alexis_vl_prefix 14
    a "Yeah. He took your advice, you know."
    
    vl gwynette_vl_prefix 10
    gw "Really?"
    
    "I nod."
    
    vl alexis_vl_prefix 15
    a "He’s been talking to someone once a week. And, he hasn’t missed class all month."
    
    "Gwynette beams."
    
    vl gwynette_vl_prefix 11
    gw "I knew he could do it."
    
    "Then, she reaches for my hand."
    
    vl gwynette_vl_prefix 12
    gw "Thanks for being such a good friend to VV. I know it means a lot."
    
    vl alexis_vl_prefix 16
    a "He means a lot to me, too. You both do."
    
    "Tearing up once more, Gwynette pulls me in for a hug."

    show sue neutral at character_pos1 with dissolve
    show reina neutral at character_pos7 with dissolve
    "I remain at the chapel for a little longer, chatting with Gwynette, Sue, Reina, and Ylva. Eventually, my stomach lets out a massive growl, interrupting Sue’s story. She laughs."
    
    s "I think breakfast is in order. How about the Amity?"
    stop music fadeout 1.0
    
    scene bg mainstreet_noon with fade
    play music hatchling1 fadein 1.0
    show sue neutral at character_pos1 with dissolve
    show gwynette neutral at character_pos4 with dissolve
    show reina neutral at character_pos7 with dissolve

    "The four of us part from Gwynette and head to breakfast. After seeing the line at the Amity, we change course and head to the salon instead."
    "As I walk across campus with Sue, Reina, and Ylva, I can’t help but feel grateful for everything this place has given me – and strangely inspired, too."
    "Maybe I’ll pay a visit to the art room myself. But first: breakfast."
    stop music fadeout 1.0

    #jump to main club route exalt
    $ renpy.call(chosen_club + "_route_exalt", "Exalt", 22)
    #jump art_route_verabris

label art_route_verabris(month, date):
    $ vince_vl_prefix = "audio/voices/Friends/Vince/Vincent_Month8/Vincent_Month8_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Vince/Month 8/" + player_voice_prefix + "_Vince_Month8_"

    call screen calendar(month, date, "Verabris", 20)
    scene bg confession_tree_noon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Vince - \nToleday, Verabris 20th, 1028 RD")

    "There’s still a month left of school. But, between classes winding down and a persistent heatwave, it’s feeling more and more like summer by the day."
    "As the trimester draws to a close, I can’t help but think about my impending graduation and life after MIA. Soon, I’ll be home again, far from the familiar sights and sounds I’ve taken for granted this past year."
    "That’s all to say, I’ve been in my head and in desperate need of some fresh air. So, after class, I take my sketchbook to the park to work on my piece for the spring showcase."
    "As I head toward an empty bench, I nearly stumble over a motionless figure sprawled out in the grass. Startled, I yelp."
    stop music fadeout 1.0
    
    show vince neutral at center with hpunch
    vl vince_vl_prefix 1
    vin "Whoa! What the–?"
    play music hatchling22 fadein 1.0
    
    "The body sits upright, revealing Vince. Squinting against the sunlight, he removes his earbuds."
    
    if eval(a.name)[0] == "Alexis":
        vl vince_vl_prefix 2A
    else:
        vl vince_vl_prefix 2B
    vin "[a]?"
    
    vl alexis_vl_prefix 1
    a "Godsdamn, you scared me."
    
    vl vince_vl_prefix 3
    vin "You’re the one who almost stepped on my face."
    
    stop music fadeout 1.0

    vl alexis_vl_prefix 2
    a "Fair. What’re you doing here?"
    play music hatchling1 fadein 1.0
    
    vl vince_vl_prefix 4
    vin "Gwynette thinks I should spend more time outside, and my therapist wants me to be more present. So…"
    
    vl alexis_vl_prefix 3
    a "Two birds with one stone."
    
    vl vince_vl_prefix 5
    vin "Exactly."
    
    "I take in my friend’s appearance. He’s dressed in his usual paint-splattered uniform and chipped black nail polish. As always, music filters from his earbuds. But, something about him seems… different. Missing. That’s when I realize–"
    
    vl alexis_vl_prefix 4
    a "You didn’t bring your sketchbook."
    
    "He shrugs."
    
    vl vince_vl_prefix 6
    vin "Like I said, staying present."
    
    vl alexis_vl_prefix 5
    a "So, were you… meditating?"
    
    vl vince_vl_prefix 7
    vin "Gods no. Just chilling. Or, trying to."
    voice sustain
    vin "It’s so damn hot. And bright. And, I think something stung me. But, I did find these."

    "He digs in his pocket and produces a handful of smooth rocks. He hands them to me to examine."
    
    vl vince_vl_prefix 8
    vin "Look at this– see how they catch the light? And, they’re not too heavy. Maybe I’ll put them in a mixed-media piece? Or a sculpture. I haven’t sculpted in months."
    
    "I can’t help but crack a smile at his enthusiasm."
    
    vl vince_vl_prefix 9
    vin "What?"
    
    vl alexis_vl_prefix 6
    a "Nothing. Just glad to see you in high spirits."
    
    vl vince_vl_prefix 10
    vin "Yeah, yeah…"
    
    "He eyes my sketchbook."
    
    vl vince_vl_prefix 11
    vin "Working on your showcase piece?"
    
    vl alexis_vl_prefix 7
    a "I was thinking about it."
    
    vl vince_vl_prefix 12
    vin "Show me."
    
    vl alexis_vl_prefix 8
    a "Okay, but it’s still rough, so don’t judge."
    
    vl vince_vl_prefix 13
    vin "Oh, c’mon. You know I will."
    
    "I take a seat on the grass beside him. After discussing my piece – a charcoal portrait collage of all the friends I’ve met at MIA – Vince and I sit in silence, taking in our surroundings: the wind in the grass, the humming of bees, the warmth of the sun."
    
    vl alexis_vl_prefix 9
    a "I know you hate this place, but you gotta admit, it’s pretty."
    
    vl vince_vl_prefix 14
    vin "Pft, you should see my garden back in Archos. In the spring, the flowers turn this shade of blue — almost, like… glowing? I’ve never seen anything else like it."
    
    vl alexis_vl_prefix 10
    a "Do you know what they’re called?"
    
    vl vince_vl_prefix 15
    vin "No, but once I picked all the buds to mix them into a paint. My mom was PISSED. Honestly, I’m surprised she didn’t ship me to MIA right then and there."
    
    vl vince_vl_prefix 16
    "We share a laugh."
    
    vl alexis_vl_prefix 11
    a "Bet you’re excited to go home."
    
    "Vince shrugs."
    
    stop music fadeout 1.0
    vl vince_vl_prefix 17
    vin "I guess…"
    play music hatchling10 fadein 1.0
    
    "He fidgets with a piece of grass, something clearly weighing on him."
    
    vl vince_vl_prefix 18
    vin "Hey, there’s something I’ve been wanting to tell you. But, I’m really bad at this shit…"
    
    vl alexis_vl_prefix 12
    a "Are you breaking up with me?"
    
    vl vince_vl_prefix 19
    vin "What? No! Fuck you."
    
    "I snicker. Vince jokingly kicks my shin."
    
    vl vince_vl_prefix 20
    vin "I just wanted to say… thank you. If not for you, I don’t know where I’d be right now. I wouldn’t be dating Gwynette. I probably would’ve been kicked out of school – and not in a fun way."
    
    vl alexis_vl_prefix 13
    a "I was gonna say…"
    
    vl vince_vl_prefix 21
    "We laugh in spite of ourselves."
    
    vl alexis_vl_prefix 14
    a "In all seriousness, though, you would’ve done the right thing with or without me. But, I’m glad I could make your time at MIA a little less shitty."
    
    vl vince_vl_prefix 22
    vin "I never said that."
    
    "Now, it’s my turn to shove Vince. Suddenly, Vince’s phone buzzes with a text."
    
    vl alexis_vl_prefix 15
    a "Gwynette?"
    
    vl vince_vl_prefix 23
    vin "Yeah, we’re doing a date night."
    
    vl alexis_vl_prefix 16
    a "Aw, cute. Well, don’t let me keep you."
    
    "He gathers his things and stands upright."
    
    vl vince_vl_prefix 24
    vin "Alright. See you at Art Club."
    
    vl alexis_vl_prefix 17
    a "See ya."
    hide vince with dissolve
    
    "Vince walks off, phone pressed to his ear and an unmistakable spring in his step. Seeing him, I can’t help but smile. I know Vince still has a ways to go, but for once, he’s living in the present–"
    "And so should I. No more mourning my time at MIA before it’s even over. Sitting in the park, I make a promise to myself to savor every last moment of my time here."
    stop music fadeout 1.0

    call student_council_verabris("Verabris", 20) from _call_student_council_verabris_2
    #jump art_route_overa
    
label art_route_overa(month, date):
    $ vince_vl_prefix = "audio/voices/Friends/Vince/Vincent_Epilogue/Vincent_Epilogue_"
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Vince_s Route/Epilogue/Gwynette_Vince_Epilogue_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Vince/Month 9/" + player_voice_prefix + "_Vince_Month9_"

    call screen calendar(month, date, "Overa", 21)
    scene bg art_room_noon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Vince - \nZynday, Overa 21st, 1028 RD")

    "The school year may be winding down, but Art Club has been abuzz with preparations for the final showcase of the year."
    "All week, club members have been popping in and out of the art room, putting final touches on our pieces and rearranging furniture to accommodate the crowd."
    "The days before a showcase are always a little hectic, but this is probably the most time we’ve spent all together this whole school year. The energy (and volume level) in the art room has been… lively, to say the least."
    "Between showcase prep and final exams, the week passes in a blur of paint, paper, and Vince’s latest metal playlist."

    scene bg maincastle_night with fade

    "On the night of the showcase, I make my way across campus to Magis Hall. To my shock, there’s a line out the door. A voice behind me echoes my surprise."
    
    vl vince_vl_prefix 1
    vin "Godsdamn, who are these people?"
    
    show vince neutral at character_pos2 with dissolve
    show gwynette neutral at character_pos5 with dissolve
    "I turn to see Vince dressed in a rare paint-free outfit, hand-in-hand  with Gwynette. Seeing me, she beams."
    
    if eval(a.name)[0] == "Alexis":
        vl gwynette_vl_prefix 1A
        gw "[a]!"
    else:
        vl gwynette_vl_prefix 1B
        gw "BB!"
    
    "She pulls me into a hug."
    
    vl alexis_vl_prefix 1
    a "Hey, fancy seeing you here."
    
    vl gwynette_vl_prefix 2
    gw "I can’t wait to see your piece! VV’s been raving about it."
    
    vl alexis_vl_prefix 2
    a "He has?"
    
    vl vince_vl_prefix 2
    vin "\"Raving’s\" a strong word."
    
    "Gwynette playfully swats him."
    
    vl gwynette_vl_prefix 3
    gw "He’s just jealous. Poor VV’s been trying to get the hang of charcoal for years."
    
    vl vince_vl_prefix 3
    vin "You said you liked my charcoal pieces!"
    
    if eval(a.name)[0] == "Alexis":
        vl gwynette_vl_prefix 4A
        gw "I do like them. I just think you could learn a thing or two from [a]."
    else:
        vl gwynette_vl_prefix 4B
        gw "I do like them. I just think you could learn a thing or two from BB."
    
    vl vince_vl_prefix 4
    "Grumbling, Vince turns his attention to the line."
    
    vl vince_vl_prefix 5
    vin "Screw it, I’m not waiting in this… "
    
    "Taking Gwynette by the hand, Vince pushes past the crowd."
    
    vl vince_vl_prefix 6
    vin "WATCH OUT! ART CLUB COMING THROUGH!"
    
    vl gwynette_vl_prefix 5
    gw "VV–"
    
    "He doesn’t slow down. Relenting, Gwynette reaches out a hand to pull me along with them."
    stop music fadeout 1.0

    scene bg art_room_night with fade
    play music hatchling4 fadein 1.0
    show vince neutral at character_pos2 with dissolve
    show gwynette neutral at character_pos5 with dissolve
    
    "When we enter the classroom, I can’t help but gape at my surroundings. This isn’t my first showcase, but I’m always amazed at the transformation from cluttered classroom to chic gallery space."
    "Vince has probably spent more time than anyone arranging and rearranging the exhibit, but still, he takes the time to walk Gwynette through each piece."
    "Leading her by the hand, Vince weaves the story of every painting, sketch, and sculpture. Gwynette listens with adoration, leaning her head against his shoulder. Seeing them together, I can’t help but smile."
    "Eventually, the couple approaches Vince’s section. When Gwynette steps forward for a closer look at one of Vince’s pieces– a large abstract sculpture– he pulls a wrapped canvas from a cubby. When Gwynette turns, Vince holds it out to her."
    stop music fadeout 1.0
    
    vl gwynette_vl_prefix 6
    gw "What’s this?"

    play music hatchling10 fadein 1.0
    
    vl vince_vl_prefix 7
    vin "Open it."
    
    "Smiling, Gwynette removes the wrapping paper. Inside, she finds an intricate portrait of herself, singing at the chapel for the Week of Life. Gwynette stares at the portrait in stunned silence."
    
    vl vince_vl_prefix 8
    vin "Do you like it?"
    
    "Gwynette is too overwhelmed to speak. Instead, she nods and kisses Vince. Then, after a moment, she breaks away, dabbing her eyes."
    
    vl gwynette_vl_prefix 7
    gw "‘Scuse me, I’m gonna grab a tissue."
    hide gwynette with dissolve
    
    "She scurries off. Vince catches me smiling."
    
    vl vince_vl_prefix 9
    vin "What are you smirking at?"
    
    vl alexis_vl_prefix 3
    a "I told you to paint her something."
    
    vl vince_vl_prefix 10
    vin "Yeah, yeah. Shut up."
    
    "I grin. Then, Vince remembers something."
    
    vl vince_vl_prefix 11
    vin "Actually, wait here."
    
    "He walks off to grab a smaller wrapped gift from his bag and practically shoves it into my hands– much less gentle than he was with Gwynette."
    
    vl alexis_vl_prefix 4
    a "You made me something?"
    
    vl vince_vl_prefix 12
    vin "What’s it look like?"
    
    "Rolling my eyes, I remove the paper. Inside is a small portrait of a woman and a wolf– his own interpretation of my piece from the first day of Art Club."
    
    vl alexis_vl_prefix 5
    a "I thought you said the design was derivative?"
    
    vl vince_vl_prefix 13
    vin "It is…"
    vl vince_vl_prefix 14
    vin "But, it grew on me."
    
    "We share a smile."
    
    vl alexis_vl_prefix 6
    a "Thanks, Vince."
    
    "We stand there in silence for a moment, taking in the bustling classroom. Then, I let out a sigh."
    
    vl alexis_vl_prefix 7
    a "I can’t believe this is my last week here."
    
    vl vince_vl_prefix 15
    vin "I can’t believe you get to leave. Asshole."
    
    vl alexis_vl_prefix 8
    a "Maybe we could live vicariously through each other– you complain to me about MIA, and I’ll complain to you about the real world."
    stop music fadeout 1.0

    vl vince_vl_prefix 16
    vin "Deal."
    
    play music hatchling1 fadein 1.0
    show gwynette neutral at character_pos5 with dissolve
    "Gwynette appears back at Vince’s side, breathless."
    
    vl gwynette_vl_prefix 8
    gw "Okay, sorry. What’d I miss?"
    
    "The three of us spend the rest of the evening together, chatting, laughing, and savoring the last night of Art Club"
    stop music fadeout 1.0

    #jump to main club route overa
    $ renpy.call(chosen_club + "_route_overa", "Overa", 21)