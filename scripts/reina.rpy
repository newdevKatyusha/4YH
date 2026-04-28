label disciplinary_route_jinus(month, date):
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Month 1/Reina_Month1_"

    call screen calendar(month, date, "Jinus", 5)
    scene bg mainstreet_afternoon with fade

    $ renpy.notify("Reina - \nZynday, Jinus 5th, 1027 RD")

    "It's been one week since I arrived in Huntsdale, and I'm finally getting my bearings."
    "I'm growing accustomed to the familiar sights and sounds of MIA– the rustling of uniforms and the crackling fireplace at House Lychester."
    "The falling leaves and the way Magis Hall glows in the late afternoon sun as if the building were made of gold."

    "I've gotten better at navigating, too. While my classmates caught up with friends, I spent my first nights studying the campus map like a textbook."
    "Yet, somehow, I still feel adrift."
    "The other fourth-years have already settled into the new trimester, resuming the lives they've built for themselves over the past three years."

    a "My classmates are friendly enough, but they're too focused on their courses and, for some, our impending graduation to worry about the new kid."
    a "I suppose there's Prince Philip, but between starting his first year and being, you know, royalty, he's got more than enough on his plate."

    show reina neutral at center with moveinright
    vl reina_vl_prefix 1
    r "Are you lost?"

    "I turn to find the same girl who wrote me up during my tour. She flashes a polite smile, unaware of how deeply her words cut my soul."
    a "Gods, I'm getting dramatic. This is why I need friends."

    show reina neutral 
    vl reina_vl_prefix 2
    r "Ah, the new fourth year. I don't believe I caught your name?"

    a "[a] Blakesley."

    show reina happy 
    vl reina_vl_prefix 3
    r "A pleasure to see you again, [a]."

    "She extends a dainty hand to me."

    vl reina_vl_prefix 4
    r "I'm Reina Dreyar."

    a "As in, Tobias Dreyar? The Duke of Centra?"

    vl reina_vl_prefix 5
    r "That's my father, yes."

    "I'm not normally starstruck. As a lesser noble, I grew up attending more than my fair share of banquets and galas."
    "But Tobias Dreyar isn't just any duke– he's the richest man in the world. And I've already pissed off his daughter once."

    show reina worried
    "As if she can read my mind, Reina's gaze flickers to my throat."

    vl reina_vl_prefix 6
    r "I see you removed your necklace."

    "Instinctively, my fingers fly to the collar of my shirt."
    a "That's right."

    show reina neutral 
    vl reina_vl_prefix 7
    r "Are you looking for something? I know it can be a bit disorienting at first."

    a "Actually, I was looking for you. Do you have a moment?"

    show reina worried
    vl reina_vl_prefix 8
    r "I'm afraid that demerits are non-negotiable. But don't fret. So long as you honor the Code of Conduct moving forward–"

    a "I'm not here about demerits..."
    "I draw in a deep breath before making my confession."
    a "I want to join the disciplinary committee."

    show reina neutral with vpunch
    "This time, Reina is taken aback."
    vl reina_vl_prefix 9
    r "You do?"

    a "You look shocked."

    show reina happy
    vl reina_vl_prefix 10
    r "No, I'm just... pleasantly surprised. Come with me."

    # Student Council Room
    scene bg student_councilroom_afternoon with fade

    "When Reina and I enter, the Student Council room is mostly empty."
    "Only two other students are here, making posters at a long table."
    "They look up when we enter. Reina smiles, but they turn away without acknowledging her."

    show reina neutral at center with dissolve
    vl reina_vl_prefix 11
    r "It's usually busier than this. I suspect most of the Council is in class... Over here."

    "Reina leads me to the far end of the room. With no windows back here, this corner is noticeably darker."
    "The lone desk is piled high with papers and folders. Even the desk chair is on its last legs."

    show reina flustered
    vl reina_vl_prefix 12
    r "Here we are– Oh, how rude of me!"
    "She grabs a second chair while I gape at my dismal surroundings."

    a "They stuck you all the way in this dark corner?"

    show reina neutral
    vl reina_vl_prefix 13
    r "It's not so bad with the light on. See?"

    "She clicks on a small desk lamp. Somehow, the feeble light only makes the surrounding space feel darker."

    show reina flustered with dissolve
    "Reina begins shoving aside papers to clear space at the desk."
    vl reina_vl_prefix 14
    r "Apologies for the mess. Between my courses and volunteering, I've been falling behind."

    a "Can't the rest of the committee help?"
    "Reina falters. That's when it hits me..."
    a "There's no one else on the committee, is there?"

    show reina worried
    "Reina looks away, more flustered than I've seen her."
    vl reina_vl_prefix 15
    r "At the moment, no. But the involvement fair is coming up."

    "I stare at the mountain of papers, beginning to regret my decision."

    show reina neutral
    vl reina_vl_prefix 16 
    r "If you want to leave, I understand. You wouldn't be the first."
    "Across the room, I hear the other students snicker. Ignoring them, I turn back to Reina."

    a "How can I help?"

    show reina happy with hpunch
    "Reina beams at me– not her usual polite smile but a bonafide grin."
    show reina happy with move
    "Sitting across from me, she hands me a stack of papers."
    vl reina_vl_prefix 17
    r "You can start by filing these. Newest violation on top..."

    "We work in silence for a while. After a time, I look up to find Reina watching me."
    a "Am I doing it wrong?"

    show reina neutral
    vl reina_vl_prefix 18
    r "No. Just... why did you want to join the disciplinary committee?"

    a "I wanted to get involved, I suppose. I don't have much time at MIA, and I wanted to make it count."
    a "Plus, if I have a better understanding of the rules, maybe I won't break another."
    "Reina nods, satisfied with my response."

    a "What about you? Following in your dad's footsteps?"
    show reina happy
    "Reina laughs."
    vl reina_vl_prefix 19
    r "Don't let him hear you say that."

    a "Why?"

    show reina neutral
    vl reina_vl_prefix 20
    r "It's against Roma custom for women to assume leadership positions."

    a "So the head of the disciplinary committee is a rulebreaker?"

    show reina happy
    vl reina_vl_prefix 21
    r "It's not an official rule. At least, not anymore. He's just old-fashioned."
    voice sustain
    r "Above all, our religion values service and giving back to the community. This is my way of honoring my heritage."

    "In the distance, a bell rings. Immediately, Reina jumps to her feet."
    show reina worried
    vl reina_vl_prefix 22
    r "Oh dear, already? I lost track of time."

    "The two of us gather our things and start for the door. Reina lingers in the doorway."
    show reina happy
    vl reina_vl_prefix 23
    r "Thank you for your time today, [a]. I look forward to working with you again."

    a "You, too."
    hide reina exit with moveoutright
    "With a small curtsy, Reina bustles out of the room."
    "I watch her go, smiling a little to myself. She's certainly not what I expected."

    scene black with fade
    
    # jump to phillip jinus
    call phillip_jinus("Jinus", 5) from _call_phillip_jinus_4
    #jump disciplinary_route_dallinus

label disciplinary_route_dallinus(month, date):
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Month 2/Reina_Month2_"

    call screen calendar(month, date, "Dallinus", 19)
    scene bg classroom_anime_afternoon with fade

    $ renpy.notify("Reina - \nNyday, Dallinus 19th, 1027 RD")

    "I've officially been at MIA for a month now."
    "As the lone new fourth-year and half of the disciplinary committee, I still catch a few stares from time to time."
    "But, for the most part, I've started to blend in–"

    a "Uhhhhhnnnn..."
    "Or I was, until my last class."

    "I've always been prone to bloody noses, but what happened in my potion brewing class looked like a godsdamn murder scene."
    "Somehow, I managed to bleed not only all over myself and my concoction but also splatter several classmates."

    a "Is it too late to drop a class?"
    "After a brief visit to the infirmary, I returned to House Lychester to change out of my bloody uniform and hide from my classmates."
    scene bg dorm_common_noon with fade
    "I'm lying on the couch, trying to recover what's left of my dignity, when..."

    show reina sickly at center with moveinright
    vl reina_vl_prefix 1
    pause .2
    with vpunch
    voice sustain
    r "ACHOO!"
    "Reina enters, looking almost as horrible as me."
    "Her eyes are red and puffy, her hair is wet and frizzy from the rain, and she dabs at her nose with a lacy handkerchief."

    show reina sickly
    play sound reina_vl_prefix + "2.ogg"
    r "Oh! [a], {w=0.9}what are you– {nw=1.7}"
    with vpunch
    extend "ACHOO!{w=0.9}– doing here?"
    stop sound

    "I hold up a red-soaked tissue."
    a "Bloody nose. You?"

    play sound reina_vl_prefix + "3.ogg"
    r "I had to go to the veterinarian, but I'm— {nw=3.9}"
    with vpunch
    extend "ACHOO!{w=0.9}— allergic to fur."
    stop sound
    
    a "Why don't you sit down? I'll make you a cup of tea."
    "She eyes my bloody tissue."

    a "Don't worry, the bleeding's stopped. I'm just tending to my ego."

    show reina worried
    vl reina_vl_prefix 4
    r "Was it that bad?"

    a "I dribbled blood into my lab partner's hair, so..."
    window hide

    show reina happy
    vl reina_vl_prefix GiggleSneeze
    pause 2.3
    voice sustain
    show reina happy with vpunch
    window show
    "Reina laughs, triggering another sneeze."

    vl reina_vl_prefix 1
    pause .3
    voice sustain
    show reina sickly with vpunch
    r "ACHOO!"

    a "Tea, then?"

    show reina sickly
    play sound reina_vl_prefix + "5.ogg"
    r "Yes– {nw=1.3}"
    with vpunch
    extend "ACHOO!{w=0.9}– please."
    stop sound

    "I heat the kettle and prepare two steaming mugs of herbal tea."
    show reina sickly
    "Returning to the couch, I hand one to her."

    a "I'm afraid it's nothing fancy."

    show reina happy
    play sound reina_vl_prefix + "6.ogg"
    r "It looks— {nw=1.35}"
    with vpunch
    extend "ACHOO!{w=0.9}— wonderful. Thank you."
    "We sip our tea in silence for a moment, savoring the warmth."

    a "So, why were you at the vet? You don't have any animals."

    show reina neutral
    play sound reina_vl_prefix + "7.ogg"
    r "I volunteer at the soup kitchen in Huntsdale. One of our customers found a box of– {nw=5.55}"
    with vpunch
    extend "ACHOO!{w=0.7}– kittens outside in the rain, so I took them in."
    stop sound

    a "But, you knew you were allergic. Couldn't someone else have taken them?"

    show reina worried
    play sound reina_vl_prefix + "8.ogg"
    r "The cook had her hands full, and I couldn't just leave them in the– {nw=4.1}"
    with vpunch
    extend "ACHOO!{w=0.9}– cold."
    stop sound

    a "So, you took these kittens to the vet by yourself, in the rain?"

    show reina neutral
    play sound reina_vl_prefix + "9.ogg"
    r "Yes. I missed class, too. Thankfully, the nurse wrote me a note, or I'd have to write myself up for– {nw=7.5}"
    with vpunch
    extend "ACHOO!{w=0.84}– an unexcused absence."
    stop sound

    "I stare at Reina a moment, taken aback."
    "This girl has such a strict reputation, and she's the daughter of one of the most powerful people in the world."
    "Yet, seeing her now... I can't help but chuckle."

    show reina worried
    play sound reina_vl_prefix + "10.ogg"
    r "What is it? Oh, I must look– {nw=4.3}"
    with vpunch
    extend "ACHOO!{w=0.9}– ridiculous... Hand me another tissue, will you?"
    stop sound

    a "It's not that. I just didn't know you were such a... softie."

    show reina neutral
    play sound reina_vl_prefix + "11.ogg"
    r "I was only doing what was– {nw=2.4}"
    with vpunch
    extend "ACHOO!{w=0.9}– right. Anyone in my shoes would do the same."
    stop sound

    a "Not anyone."

    vl reina_vl_prefix SneezeGroan
    pause .4
    voice sustain
    show reina sickly with vpunch
    "Reina sneezes again. She lets out a groan."

    vl reina_vl_prefix 12
    r "Gods, I feel terrible... We're quite the pair, aren't we?"
    "We share a laugh and finish our tea."

    show reina worried 
    vl reina_vl_prefix 13
    r "I think I'll rest up before dinner. Thank you for this, [a]."

    a "My pleasure."

    show reina flustered 
    "She hesitates for a moment, as if there's something more she wants to say."
    show reina neutral 
    "Then, deciding against it, Reina flashes me a polite smile."
    vl reina_vl_prefix 14
    pause .4
    voice sustain
    show reina with vpunch
    "With a final sneeze, she heads to her room."
    hide reina exit with MoveTransition(2, leave=offscreenright)

    scene black with fade
    call student_council_dallinus("Dallinus", 19) from _call_student_council_dallinus_4

label disciplinary_route_vanus(month, date):
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Month 3/Reina_Month3_"
    $ val_vl_prefix = "audio/voices/Supporting-Extra/Val/Reina/Val_Reina_Month3_"
    
    call screen calendar(month, date, "Vanus", 22)
    scene bg mainstreet_afternoon with fade

    $ renpy.notify("Reina - \nNyday, Vanus 22nd, 1027 RD")
    
    show reina happy at center with dissolve
    "Over the past two months, Reina has become my closest acquaintance at MIA. I look forward to our time in the back corner of the Student Council room together, chatting and snacking as we assemble files."

    show reina neutral
    "Little by little, we've begun spending time together outside of the disciplinary committee, too."
    "Since we're both in House Lychester, we often walk to breakfast together and sit by the fire in the evenings."

    "Initially, I was surprised by Reina's attention. I mean, she's been here for two years already, she's head of the disciplinary committee, and her father is the richest man in the world."

    "Surely, there are better ways for her to spend her time than babysitting the new kid."

    show reina worried
    "In recent weeks, I've grown self-conscious. What if Reina doesn't actually like me?"
    "Noblesse oblige dictates that the privileged have an obligation to help those less fortunate than themselves, and I certainly fit the bill."

    "In Reina's eyes, are we actually friends, or am I just another cumbersome charity case, like that box of kittens?"

    show reina neutral
    "All of these anxieties are flitting through my head as Reina and I walk to breakfast this morning."
    "We trudge down the tree-lined path in silence, fallen leaves crunching beneath our feet, while I find the words to voice my concern."

    "At last, I clear my throat."

    a "Hey, Reina–"

    show reina flustered
    "Before I can continue, something up ahead catches Reina's eye."

    vl reina_vl_prefix 1
    r "One moment…"

    show reina neutral
    "She rushes ahead of me, toward a haughty-looking student wearing headphones. Oblivious to Reina, the student walks on, bobbing their head to the beat."

    vl reina_vl_prefix 2
    r "Hi, excuse me?"

    "The student keeps walking. Reina taps them on the shoulder."

    vl reina_vl_prefix 3
    r "Excuse me… Val, isn't it?"

    "The student eyes her, annoyed."

    vl val_vl_prefix 1
    v "Here we go again."

    vl reina_vl_prefix 4
    r "Would you mind removing your headphones?"

    "Annoyed, Val obliges."

    vl reina_vl_prefix 5
    r "As I told you last week, it is against the Code of Conduct for students to have visible piercings or body markings outside of–"

    vl val_vl_prefix 2
    v "\"–a single earlobe piercing for female students.\" Gods, you're a broken record."

    show reina worried
    vl reina_vl_prefix 6
    r "If you'd like me to stop repeating myself, you should heed my instructions and remove your cartilage piercing."

    vl val_vl_prefix 3
    v "Why don't you heed my instructions and piss off?"

    show reina flustered

    "By this point, other students have gathered to watch the commotion. Reina ignores them, struggling to maintain her composure."

    vl reina_vl_prefix 7
    r "Fine. Then, you leave me no choice but to assign another demerit."

    show reina neutral
    "Reina pulls out her notepad and jots something down."

    vl reina_vl_prefix 8
    r "Three demerits are grounds for a disciplinary hearing. If you do not attend your hearing, you will be suspended."

    "Reina tears out the sheet of paper and hands it to Val. With a snort, Val crumples up the paper and starts to walk off. Reina follows after."

    show reina worried
    vl reina_vl_prefix 9
    r "Did you hear me? I said, if you miss your hearing–"

    vl val_vl_prefix 4
    v "What in the Abyss is wrong with you? You think you're better than everyone because your daddy's a duke?"

    show reina flustered
    vl reina_vl_prefix 10
    r "This isn't about my father–"

    vl val_vl_prefix 5
    v "No, it's about the massive stick up your ass."

    "A few other students giggle. I hang back, unsure whether or not to intervene."

    vl val_vl_prefix 6
    v "No one likes you, Reina. You're only on the Council because no one else wanted your job. You're lucky it wasn't up to a vote."

    show reina worried

    "Reina's lower lip begins to tremble. I've never seen her this upset. I can't let my only friend be humiliated like this. I take a step forward."

    a "What's your problem? Reina didn't write the Code of Conduct. She's just doing her job."

    "Val turns on me, sizing me up. They flash me a smirk."

    vl val_vl_prefix 7
    v "You're the new fourth-year, aren't you? Here's a tip– you want to make friends, stay away from Reina."

    a "Reina is my friend."

    vl val_vl_prefix Giggle
    "Val laughs."

    a "Why is that funny? I don't see anyone jumping to your aid."

    "The crowd giggles once more. This time, Val doesn't join them."

    vl val_vl_prefix Muttering
    "Annoyed, Val reaches up and yanks out their cartilage piercing. They toss it to the dirt and start to walk away…"

    a "You know, littering is against the Code of Conduct."

    show reina flustered

    "Mumbling under their breath, Val retrieves the earring and stalks off."

    show reina neutral
    "The crowd starts to dissipate. Once Reina and I are alone again, she turns to me." 

    vl reina_vl_prefix 11
    r "Did you mean that?"

    a "Oh, no. I know littering isn't actually part of the Code of Conduct. I just wanted to–"

    show reina flustered
    vl reina_vl_prefix 12
    r "I mean, about being friends."

    a "Of course."

    "I quickly correct myself."

    a "Unless, that's not something you want?"

    show reina happy
    vl reina_vl_prefix 13
    r "No. I mean– yes, certainly. I'm honored to be your friend, [a]."

    "We share a smile. Then, a little flustered, we both look away."

    show reina flustered
    a "How about breakfast?"
    
    show reina neutral
    "Together, we walk to the dining hall."

    # jump to second club route dyalt
    $ renpy.call(chosen_club2 + "_route_dyalt", "Vanus", 22)
    #jump disciplinary_route_dyalt

label disciplinary_route_dyalt(month, date):
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Month 4/Reina_Month4_"

    call screen calendar(month, date, "Dyalt", 21)
    scene bg mainstreet_night with fade

    $ renpy.notify("Reina - \nZaeday, Dyalt 21st, 1027 RD")

    "Winter has arrived at MIA. There's snow on the ground and an impenetrable chill in the air."
    "Walking across campus, my classmates are bundled up beyond recognition, and there have already been several ice-related injuries."

    "Was a second-year actually knocked out by a poorly-timed fallen icicle, or was it simply a creative excuse to miss class?" 
    "Either way, she deserved to stay home."

    "That's all to say, between early sunsets and the abysmal weather, it's hard to find the motivation to leave House Lychester."
    "But, this evening, I opted for a change of scenery."

    "I ventured to the salon– only to find a \"CLOSED\" sign on the door and no waitstaff in sight. It seems I'm the only sucker dumb enough to go out in this weather."

    a "At least I got my steps in…"

    "I buy a cookie from The Amity to justify my trip. Then, wrapping my arms around myself, I start down the path back toward House Lychester when I hear muffled voices from nearby."

    show reina worried at center with dissolve
    vl reina_vl_prefix 1
    r "…Father, please. You're not listening…"

    "I follow the source of the noise to one of the walking paths between Huntsdale and campus."
    "Positioning myself behind a large tree trunk, I watch as Reina and an imposing older man speak in hushed tones, lit by the glow of a streetlamp."

    "Even from a distance, I recognize the man as Reina's father, Duke Tobias Dreyar."
    "I've only seen him once in person, but for as long as I can remember, his face has been all over the news: angular, dignified, and surprisingly similar to Reina's."

    "I contemplate introducing myself, but I can tell from Reina and Tobias's body language that this isn't a happy conversation. Finally, Tobias turns on his heel and walks away."

    show reina sickly
    "Dejected, Reina sits on a bench, unfazed by the falling snow. She dabs at her eyes. I watch her for a moment, unsure what to do."

    "A twig crunches beneath my feet. Reina's head snaps up."

    show reina flustered
    vl reina_vl_prefix 2
    r "Is someone there?"

    "Hesitantly, I emerge from my hiding spot."

    vl reina_vl_prefix 3
    r "[a], how long were you over there?"

    a "Just a few minutes. I didn't mean to eavesdrop or scare you. It seemed like a… tense conversation."

    show reina worried
    vl reina_vl_prefix 4
    "Reina sighs."
    voice sustain
    r "That was my father. He's visiting for some donor event. I thought I'd meet him in town for dinner, but–"

    show reina sickly
    vl reina_vl_prefix Shiver
    pause .2
    voice sustain
    "The wind picks up. Reina shivers."

    a "You must be freezing. Why don't we go inside?"

    show reina neutral
    vl reina_vl_prefix 5
    r "Good thinking."

    "Together, we head into the Wilson building."

    scene bg wilson_salon_night with fade 

    show reina worried at center with dissolve
    "Upon entering the building, we find the student council room locked. But, for whatever reason, the salon door remains open."
    "Someone must have forgotten to lock up. So, I push open the door and turn on the lights."

    vl reina_vl_prefix 6
    r "I don't know if we should be here."

    show reina neutral
    a "As nobility, we're allowed access to the salon during regular business hours. Oh…"

    "I reach into my bag and pull out my cookie, now slightly squished from the journey."

    show reina flustered
    vl reina_vl_prefix 7
    r "What's that?"

    a "It's from The Amity. They make a killer snickerdoodle."

    "I offer her half, but she declines."

    show reina neutral
    vl reina_vl_prefix 8
    r "I'm not hungry, thank you."

    "We sit in silence for a moment. Biting into my cookie, I consider my approach. I don't want to pry into Reina's personal life, but clearly, that chat with her father took a toll."

    "I decide to take my chances."

    a "You sounded pretty upset down there. What were you two talking about, if you don't mind me asking?"

    show reina worried
    vl reina_vl_prefix 9
    "Reina sighs."
    voice sustain
    r "We were discussing the whole Code of Conduct debacle. I didn't ask for advice– I know he disapproves of my position on the disciplinary committee."
    voice sustain
    r "I suppose I just wanted affirmation. For him to comfort me, like a parent…"

    show reina sickly
    "She trails off."

    a "And, what did he say?"

    show reina worried
    vl reina_vl_prefix 10
    r "That this is the cost of doing business, and if I couldn't handle it, I should step down from the Council."

    "I recognize the look in her eyes: not just sadness but grief. Feeling my gaze, Reina smoothes her skirt, self-conscious."

    show reina sickly
    vl reina_vl_prefix 11
    r "I don't mean to complain. I know I should be grateful for the life he's given me. But, sometimes, I wish he treated me less like a cadet and more like a daughter."
    voice sustain
    r "I wonder if it would be different, if my mother…"

    show reina worried
    "She trails off, then catches herself."

    vl reina_vl_prefix 12
    r "Anyway, he's always like this."

    show reina neutral
    "She goes quiet, but I can sense her pain. Reina and I had very different upbringings, but I know how she feels all too well. I clear my throat to speak."

    a "You know, when my dad passed, my mom started treating me like a completely different person, almost like a business partner."
    a "She expected me to take his place caring for her and my siblings and forgot I was just a scared kid who lost my dad."

    show reina worried
    "Reina eyes me with sympathy."

    vl reina_vl_prefix 13
    r "I'm sorry, [a]. I didn't know you'd lost your father."

    a "It's been a long time. I was 12 when he passed."

    show reina sickly
    vl reina_vl_prefix 14
    r "That doesn't matter. I was 10 when I lost my mother, and it still feels like it was yesterday."

    #a "It's wild to think, my siblings barely even knew him. They were so young when it happened. He's more of a story than a person to them."
    a "It’s wild to think, my siblings have spent almost half of their lives without him. He’s more of a distant memory than a person to them."

    show reina worried
    vl reina_vl_prefix 15
    r "Still, it must be nice to share his memory with someone." 

    a "Your father doesn't talk about her?"

    "Reina shakes her head."

    vl reina_vl_prefix 16
    r "He's not big on reminiscing."

    show reina neutral
    a "I'm sure he doesn't mean anything by it. They get so swept up in their own pain that they forget we're in the trenches with them."

    show reina sickly
    vl reina_vl_prefix 17
    r "I don't know if my father is even capable of pain. The day after Mother's funeral, it was business as usual for him. Sometimes, we went weeks without speaking."

    show reina worried
    "She shakes her head, remembering."

    a "Was he like that when your mom was alive?"

    show reina sickly
    vl reina_vl_prefix 18
    r "I didn't think so. Or, perhaps she just made up for it? I don't know. There's no one left to ask."

    "She dabs at the corner of her eyes."

    show reina flustered
    vl reina_vl_prefix 19
    r "Gods... I always seem to be falling apart around you."

    show reina neutral
    a "Or, maybe you just can't always take care of yourself."

    show reina happy
    "Something about this moves Reina. She turns to me, suddenly determined."

    vl reina_vl_prefix 20
    r "What if we took care of each other?"

    show reina flustered
    a "What do you mean?"

    show reina happy
    vl reina_vl_prefix 21
    r "Neither of us had the childhood we should have. Like you said, we were forced to take care of ourselves."
    voice sustain
    r "So, what if, for as long as we're both at MIA, we took care of each other?"

    show reina flustered
    "I stare at her a moment, taken aback. Since my father's death, no one's ever offered to take care of me. Reina grows flustered."

    vl reina_vl_prefix 22
    r "Forgive me, I got carried away. What I meant to say was–"

    show reina happy
    a "It's a deal."

    "I hold out my hand for Reina to shake. She takes it, and we laugh a little, in spite of ourselves. Reina eyes the other half of my cookie."

    show reina neutral
    vl reina_vl_prefix 23
    r "I suppose I'll take you up on that snickerdoodle."

    show reina happy
    "We remain there together until curfew. When it's finally time to leave, we brave the winter chill together, each warmed by the other's presence."
    call student_council_dyalt("Dyalt", 21) from _call_student_council_dyalt_4

label disciplinary_route_neralt(month, date):
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Month 5/Reina_Month5_"

    call screen calendar(month, date, "Neralt", 10)
    scene bg student_councilroom_afternoon with fade 

    $ renpy.notify("Reina - \nLenday, Neralt 10th, 1027 RD")

    "With the dress code controversy behind us, the drama at MIA has started to die down."
    "Somehow, I'm already halfway through the school year, and I've fallen into a familiar, pleasant rhythm of work, classes, and spending time with Reina."

    show reina neutral at center
    "I'm alone in the Student Council room, filing citations and daydreaming of warmer weather, when Reina arrives, ten minutes late and visibly frazzled."

    "I'm surprised to see her this out of sorts. Since the Code of Conduct fiasco, Reina has been significantly more cheerful– which is to say, as prim and proper as ever, but she cracks the occasional joke."

    show reina flustered
    "But, today is different. In a whirlwind of textbooks and anxiety, Reina bustles over to the desk."

    vl reina_vl_prefix 1
    r "Gods, I am terribly sorry, [a]. I've had the worst day."

    a "Why? What happened?"

    show reina worried
    vl reina_vl_prefix 2
    r "Today, in Fundamentals of Magic, we did a practice exam for the final, and I did terribly. What if I botch the real thing? This could lower my GPA!"

    a "Whoa, slow down. It's just a practice test, and you still have another week to study."
    
    pause 1.0
    
    a "What did you get, anyway?"

    show reina flustered
    "Reina bites her lip, uncertain."

    vl reina_vl_prefix 3
    r "You mustn't tell anyone."

    a "Who would I tell?"

    "Relenting, Reina reaches into her bag and extracts a sheet of paper. With a pained expression, she passes it to me, face-down. Bracing myself, I turn the quiz over…"

    a "You got a B?"
    
    vl reina_vl_prefix 4
    r "I know. It's horrible. I'm the daughter of a duke, and I don't know the history of magic? I'm a failure."

    "Seeing her grave expression, I can't help but chuckle."

    show reina worried
    vl reina_vl_prefix 5
    r "Why are you laughing? This is serious!"

    a "Reina, a B is a good grade."

    vl reina_vl_prefix 6
    r "A good grade. Not a great one. What if I get a B on the final? Then, I'll get a B in the class!"

    show reina sickly
    "She flops onto the desk, dejected. Unsure what else to do, I place a gentle hand on her shoulder."

    a "I can help you study."

    show reina flustered
    vl reina_vl_prefix 7
    "With a gasp, Reina shoots upright."
    voice sustain
    r "You would do that?"

    show reina happy
    a "Of course… as long as you promise not to be too hard on yourself."

    vl reina_vl_prefix 8
    r "Deal."

    "She holds out her hand to shake. We share a smile."

    call screen calendar("Neralt", 10, "Neralt", 15)
    scene bg weaver_library_night with fade

    $ renpy.notify("Reina - \nToleday, Neralt 15th, 1027 RD")

    "Reina and I spend the next week studying nonstop. Naturally, she's not nearly as bad at Fundamentals of Magic as she'd have you think, but initially, she struggles in a few areas."

    show reina neutral at center
    "By the end of the week, however, she seems to have mastered everything."

    a "What are the three major global alliances of the early modern–"

    vl reina_vl_prefix 9
    r "The Oceanic Alliance, the Culmarean League, and the Eastern Confederation."

    a "Okay. This conflict broke out in Spring 700 RD over the ownership of a manite–"

    vl reina_vl_prefix 10
    r "The Three Seasons' War."

    a "Don't you think you should listen to the full question before answering?"

    show reina flustered
    vl reina_vl_prefix 11
    r "I don't have time for that. Next question."

    show reina neutral
    a "Alright. Which imperial scientist first coined the term \"mana lobe\" to refer to the part of the brain–"

    vl reina_vl_prefix 12
    r "Dr. William Richardson."

    a "Nope."

    show reina worried
    vl reina_vl_prefix 13
    r "What? Let me see that."

    "She cranes her neck for a look at my textbook."

    vl reina_vl_prefix 14
    r "\"Dr. William Richardson identified that there was a part of the brain that allowed people to use magic, calling it the Mana Lobe.\" That's what I said."

    a "I know. I was testing you."

    show reina flustered
    "Reina picks up the book and playfully smacks me with it."

    a "Ow! Violence is against the Code of Conduct."

    show reina neutral
    vl reina_vl_prefix 15
    r "What's next?"

    a "That's all." 

    vl reina_vl_prefix 16
    r "Okay, then. Let's start from the top."

    "She sets the book back in front of me, but I don't pick it up."

    a "The test's in twelve hours. Why don't you rest up?"

    show reina worried
    vl reina_vl_prefix 17
    r "It's alright. I won't be able to sleep anyway."

    a "We've gone through everything twice. I think you know as much about early modern magical history as a third-year possibly could."

    "Reina doesn't look convinced. She nervously picks at the hem of her dress."

    vl reina_vl_prefix 18
    r "What if she throws in a trick question? Or I forget the Sixfold Path?"

    show reina neutral
    a "You promised me you wouldn't be too hard on yourself."

    show reina worried
    vl reina_vl_prefix 19
    r "I know…"

    a "Whatever happens tomorrow, it doesn't make you any less annoyingly brilliant."

    show reina happy
    vl reina_vl_prefix 20
    r "But, I'm going to get an A."

    a "That's the spirit. And, if Instructor Acre gives you anything less, she'll have me to answer to."

    show reina flustered
    vl reina_vl_prefix 21
    r "You know, threatening faculty is grounds for expulsion."

    a "Only if you're caught."

    show reina happy
    "Reina cracks a smile, then reaches across the table to squeeze my hand."

    vl reina_vl_prefix 22
    r "Thank you, [a]. You're a good friend."

    "I meet Reina's gaze with a smile. We remain there in silence for a moment, then Reina catches sight of the clock on the wall."

    show reina flustered
    vl reina_vl_prefix 23
    r "8:45? We'd better hurry, or we'll miss curfew."

    show reina neutral
    "Gathering our belongings, we return to House Lychester."
    
    # jump to second club route neralt
    $ renpy.call(chosen_club2 + "_route_neralt", "Neralt", 15)
    #jump student_council_exalt

label disciplinary_route_exalt(month, date):
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Reinas Route/Reina/Elio_Reina_Month6_"
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Month 6/Reina_Month6_"

    call screen calendar(month, date, "Exalt", 26)
    scene bg wright_field_afternoon with fade

    $ renpy.notify("Reina - \nToleday, Exalt 26th, 1027 RD")

    "Warm weather is finally upon us. After a miserable, seemingly endless cold snap, the sun finally broke through, offering a taste of early spring just in time for the Week of Life."

    "Between the sunny weather and the upcoming festivities, MIA is abuzz with activity."

    "I'm not particularly religious, but I have been savoring every moment of warmth, taking the long route to classes and wandering the farthest corners of campus."

    "It seems I'm not the only one. Today, as I pass by the archery field, I hear a frantic shout."

    vl elio_vl_prefix 1
    e "WATCH OUT!"

    "I turn to see Elio, the archery club president, racing over to knock the bow from another student's hands."

    "Behind the wooden target, a uniformed figure is visible, crouched amongst a small patch of wildflowers."
    "Elio marches over and addresses them with annoyance."

    vl elio_vl_prefix 2
    e "What in the Abyss is wrong with you? You realize you could've been–"

    show reina flustered at center
    "The figure straightens, revealing a flustered, wide-eyed Reina. She stuffs something into a woven basket hanging from her arm."

    "At the sight of her, Elio composes himself."
    
    vl elio_vl_prefix 3
    e "Oh, it's you." 

    "Cheeks reddening, Reina steps out from the bushes."

    vl reina_vl_prefix 1
    r "My apologies, Elio. I didn't know the field was in use."

    vl elio_vl_prefix 4
    e "Archery practice runs from eleven to three."

    show reina worried
    vl reina_vl_prefix 2
    r "Of course. I am terribly sorry for the inconvenience. I'll be going now."

    "With a sheepish curtsy, Reina walks off. I jog after her."

    a "Reina!"

    show reina flustered
    "Seeing me, she halts and plasters on a smile."

    vl reina_vl_prefix 3
    r "Oh, hello, [a]. Please tell me you didn't see that."

    a "Unfortunately, I did. What were you doing back there?"

    show reina neutral
    "She holds out her basket, revealing an assortment of colorful wildflowers. I can't help but gape at their beauty."

    a "They're beautiful."

    show reina happy
    vl reina_vl_prefix 4
    r "Aren't they? I've been out all morning, trying to gather enough for a garland."

    a "A garland?"

    "Reina nods."
    vl reina_vl_prefix 5
    r "It's a Roma tradition. Just before the Week of Life, we gather the first blooms of the year and weave them together to decorate our homes."
    voice sustain
    r "It's meant to celebrate life and the coming spring, and the act of creation is an important part of our religion."

    a "Ingenuity is one of the Links of Life, isn't it?"

    vl reina_vl_prefix 6
    r "That's correct. When I was little, my mother and I would scour the garden for flowers and weave our garlands together."
    voice sustain
    show reina sickly
    r "But, since she passed, I've been on my own."

    a "Aren't there other Roma students at MIA?"

    show reina worried
    vl reina_vl_prefix 7
    r "Not many. There are maybe nine or ten of us in total, but I've never quite fit in."

    a "That must be difficult."

    show reina neutral
    "Reina shrugs."
    vl reina_vl_prefix 8
    r "Most of the time, I don't notice it, but this time of year can be… challenging."

    "Reina and I have been through so much together, but standing there with flushed cheeks and her basket of flowers, she seems more vulnerable than ever."
    "I know I can't let her face the holiday alone again."

    a "Can I celebrate with you?"

    show reina flustered
    "Reina looks surprised."

    vl reina_vl_prefix 9
    r "Are you sure? I don't want to force you."
    
    pause 1.0
    
    a "You're not forcing me. It sounds fun. Come to think of it, I saw some flowers behind Magis Hall."

    show reina happy
    "Smiling, Reina hands me the basket of flowers."

    vl reina_vl_prefix 10
    r "Lead the way."

    scene bg maincastle with fade

    "Reina and I spend the rest of the afternoon together, gathering flowers and supplementing our haul with a bouquet from the florist in town."

    show reina neutral at center
    "After cobbling together some food from the dining hall, we pick a spot on the grass in front of Magis Hall and set to work weaving our garlands."

    "Once we finish, we drape our garlands over the branches of a nearby tree and tuck into our celebratory feast."
    "We end our celebration by lying side by side on the grass and watching the first stars appear in the sky."

    a "Isn't that Rex?"

    vl reina_vl_prefix 11
    r "No, it's Orphan."

    a "Well, close enough."

    show reina flustered
    vl reina_vl_prefix 12
    r "Close enough? You do know Orphan is a major figure in both of our religions?"

    a "I'm not observant."

    show reina neutral
    "Reina shoots me a curious look and scooches closer to lean her head on my shoulder."

    vl reina_vl_prefix 13
    r "I never asked you… what does your necklace mean?"

    "I blink in surprise, caught off-guard."

    vl reina_vl_prefix 14
    r "It must be very special for you to repeatedly break the dress code, despite being half of the disciplinary committee."

    a "The dress code was amended."

    vl reina_vl_prefix 15
    r "Before that. You think I never saw it under your shirt collar?"

    "Gingerly, I pull the pendant out from beneath my collar, revealing the ornately-carved pendant."

    a "It belonged to my father. It's the Blakesley family crest."

    show reina flustered
    vl reina_vl_prefix 16
    r "Can I?"

    "I nod. Gently, Reina catches the pendant in her fingers and runs her thumb over the carvings."

    a "It's supposed to be a black wolf. That's what Blakesley means."

    show reina happy
    vl reina_vl_prefix 17
    r "It's beautiful."

    a "Thanks."

    "I tuck the pendant beneath my collar once again. Reina looks up at me, the stars reflected in her dark eyes."

    vl reina_vl_prefix 18
    r "Thank you for celebrating with me, [a]."

    a "Of course."

    "We lie there together in content silence, watching the stars blink to life."
    call phillip_elvera("Exalt", 26) from _call_phillip_elvera_4

label disciplinary_route_elvera(month, date):
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Month 7/Reina_Month7_"
    $ sue_vl_prefix = "audio/voices/Love Interests/Sue/Reina/SueDaengQan_Reina/SueDaengQan_Reina_"

    call screen calendar(month, date, "Elvera", 14)
    scene bg mainstreet_afternoon with fade

    $ renpy.notify("Reina - \nZynday, Elvera 14th, 1028 RD")

    "The school has been abuzz with excitement about the upcoming election."
    "Posters cover every wall and lamppost, and at all hours, the Student Council room and library are bustling with activity as current and prospective Council members set to work on their campaigns."

    "My classmates' enthusiasm is infectious, but for me, the elections are bittersweet."
    "They signal the end of my own brief time on the disciplinary committee and at MIA."

    "I still can't believe how quickly this year has passed me by, nor do I have the faintest idea what I'll do after graduation."

    "I head to to the Student Council room myself in hopes that some mindless filing will quiet my racing thoughts, only to find a sign posted outside of the Wilson Building:"

    "\"STUDENT COUNCIL ROOM CLOSED FOR A PRIVATE EVENT.\""

    "Of course, how could I forget? Tonight is the annual Student Council \"formal\"- which is really just a nice dinner for sitting Council members, celebrating the past year's achievements."

    "I wouldn't mind the upgrade from dining hall food, but unfortunately, the event is invite-only, limited to executive Council members and committee heads."

    "Disappointed, I begin my walk back to House Lychester when I hear someone calling out to me."

    show reina happy at center
    vl reina_vl_prefix 1
    r "[a]! There you are!"
    vl reina_vl_prefix 2
    "Breathless, Reina rushes over to me."
    voice sustain
    r "I thought you'd be back at House Lychester by now."

    a "I thought I'd help with some filing. I completely forgot about the formal. Are you going?"

    show reina neutral
    vl reina_vl_prefix 3
    r "Actually, that's why I was looking for you. I wanted to know if you'd come with me."

    a "You want me to be your date?"

    show reina flustered
    vl reina_vl_prefix 4
    r "Not a date! A… platonic escort to keep me company."

    a "When does it start?"

    vl reina_vl_prefix 5
    r "Six o'clock… "

    a "Six? That's only three hours from now. Did your other date cancel?"

    vl reina_vl_prefix 6
    r "What? No! I didn't ask anyone else.  Truth be told, I didn't think I'd be attending. After everything that happened this year–"

    "I cut her off."

    a "Reina, I'm kidding. I'd love to be your platonic escort."

    show reina happy
    "Reina beams with delight."

    vl reina_vl_prefix 7
    r "Wonderful! We could get ready together if you'd like. Perhaps I could help with your hair."

    a "What's wrong with my hair?"

    show reina worried
    vl reina_vl_prefix 8
    r "Nothing. It just looks a bit… informal."

    a "Alright, if you insist."

    "We head back to House Lychester together."

    hide reina
    scene bg dorm_common_night with fade

    "After freshening up and fearing that Reina might rip my hair out–"

    show reina neutral at center
    a "Ouch!"

    show reina flustered
    vl reina_vl_prefix 9
    r "Sorry! Almost finished!"

    "–we head back to the Wilson Building together."

    hide reina
    scene bg student_councilroom_night with fade 

    "The Student Council room has been completely transformed: warm lights, flowers, soft music."
    "The beat-up work tables and desks have been pushed together and draped in fabric to form a long, elegant banquet table, piled with food."

    show reina neutral
    "I pause in the doorway, frozen in awe, and Reina gently steers me by the elbow."

    vl reina_vl_prefix 10
    r "Come, let's find our seats."

    "We scour the length of the table for our nametags. As we pass, more than a few students greet Reina with smiles and even a few hugs."
    "She seems flustered by the attention but manages to return their pleasantries."

    "Eventually, we find our place settings– \"Miss Reina Dreyar\" and \"Miss Reina Dreyar's Guest\"– at the far end of the table– only for Reina to be summoned across the room to chat with the Student Council secretary."

    hide reina
    "I'm sitting by myself, eyeing the prime rib, when someone taps me on the shoulder."
    "I turn to see a familiar face smiling down at me."

    show sue happy at center
    a "Sue! How are you?"

    vl sue_vl_prefix 1.1
    s "Good. Still in denial that the school year is ending. How about yourself?"

    a "Same here. I feel like I finally settled in, just in time to graduate."

    show sue neutral
    vl sue_vl_prefix 2.1
    s "Well, you certainly made your time at MIA count. Which reminds me..."

    "Ensuring that Reina isn't looking, Sue lowers her voice."

    vl sue_vl_prefix 3.1
    s "Are you and Reina–"

    a "Oh, I'm just her platonic escort."

    show sue happy
    vl sue_vl_prefix 4.1
    "Sue bursts out laughing."
    voice sustain
    s "I was going to ask if you're working on her campaign."

    "I stare at her in confusion."

    show sue neutral
    vl sue_vl_prefix 5.1
    s "For president? People keep asking if Reina's running. I wanted to speak with her about it, but I don't want her to feel pressured if she's not interested."

    a "She hasn't said anything to me."

    vl sue_vl_prefix 6.1
    s "Damn. She'd be great, don't you think? "

    "Before I can continue, the Vice President approaches and pulls Sue into another conversation. She claps a hand on my shoulder."

    show sue happy
    vl sue_vl_prefix 7.2
    s "Excuse me. Nice seeing you, [a]."

    a "You, too."

    hide sue
    "She excuses herself, leaving me to own devices. I begin to serve myself when Reina returns to her seat, breathless."

    show reina flustered at center
    vl reina_vl_prefix 11
    r "Sorry to leave you on your own."

    a "Don't be. I'm glad you're enjoying yourself."

    hide reina
    "After dinner, the guests leave the table and make their way to a makeshift dancefloor."
    "At first, Reina hangs back, but after thoroughly embarrassing myself, I manage to coax her into performing some silly moves of her own."

    "The final song is a slower number– a popular love song from a few years back."
    "Reina tries (and fails) to coach me on proper ballroom form, and we end up dissolving into laughter."

    "At the end of the night, after an emotional speech from Sue, we bid farewell to the other guests and walk back to House Lychester together."

    scene bg mainstreet_night with fade 

    show reina neutral at center
    "Reina and I walk in silence for a while, the rustling of leaves and chirping of crickets filling the space between us. Eventually, Reina clears her throat."

    show reina happy
    vl reina_vl_prefix 12
    r "Thank you for being my date tonight, [a]."

    a "Platonic escort."

    show reina neutral
    "Reina doesn't laugh. I can tell something is on her mind."

    a "What's wrong?"

    show reina worried
    r "Nothing's wrong. I've just been thinking…"

    a "Of running for President?"

    show reina neutral 
    "She stares at me, stunned."

    vl reina_vl_prefix 13
    r "How did you know that?"

    a "Sue asked me if you had mentioned it."
    a "She said she wanted to talk to you about it herself but didn't want to put you on the spot."

    "Reina looks surprised."

    vl reina_vl_prefix 14
    r "Really?"

    "I nod."

    show reina happy
    a "It sounds like the rest of the Council has been asking her. She thinks you'd make a great president, and I agree."

    "Reina allows herself to smile."

    show reina worried
    vl reina_vl_prefix 15
    r "I know what my father will say. A woman as Class President… At least on the disciplinary committee, I was bending one rule to uphold others."
    voice sustain
    r "But, somehow I feel… called to this. MIA is changing, fast, and I want to be part of it."

    a "Maybe some rules are meant to be broken."

    show reina happy
    vl reina_vl_prefix Chuckle
    "Reina chuckles, then meets my eyes, more earnest than ever."

    show reina neutral
    vl reina_vl_prefix 16
    r "[a], I know you have graduation coming up, and I don't want to put more on your plate… but would you be willing to help with my campaign?"

    "Now, it's my turn to be surprised.  My time here might be drawing to a close, but there's still time for me to leave my mark here."
    "And, I know Reina will be the most devoted leader MIA could hope to have."

    show reina flustered
    vl reina_vl_prefix 17
    r "I'm sorry, I feel like I'm always pressuring you into something. You've already done more than enough, and–"

    a "I would be honored to help, Reina."

    show reina happy
    "Delighted, she pulls me in for a hug."

    vl reina_vl_prefix 18
    r "Thank you, thank you, thank you!"

    show reina neutral
    "Then, she pulls away, all business."

    vl reina_vl_prefix 19
    r "So, I have a few ideas for my slogan…"

    "We strategize the whole walk back to House Lychester."
    call disciplinary_route_verabris("Elvera", 14) from _call_disciplinary_route_verabris

label disciplinary_route_verabris(month, date):
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Month 8/Reina_Month8_"

    call screen calendar(month, date, "Verabris", 8)
    scene bg dorm_common_noon with fade

    $ renpy.notify("Reina - \nLenday, Verabris 8th, 1028 RD")

    "Reina and I have spent the last month working on her presidential campaign. I won't lie– it's been significantly more work than I expected."

    "Between studying for final exams and helping Reina table and hang posters, I've scarcely had time to slip away for a meal."

    "Still, I'm grateful for the excuse not to think about my impending graduation, and I've never seen Reina more animated about anything."
    "She's poured her heart and soul into every poster, Council meeting, and line of her campaign speech."

    "Not even a disapproving letter from her father could pull her down. I overheard her on the phone with him several nights ago."

    show reina neutral at center
    vl reina_vl_prefix 1
    r "I understand your concern, Father, but this is my decision." 
    voice sustain
    r "If you decide you'd rather not pay my tuition, I'm more than happy to take out a loan to finance it myself– though, I'm not sure how you'd explain it to the rest of the board."

    hide reina
    "On the final afternoon before the election, all of MIA is outdoors, lounging on the green and enjoying the sunshine– "

    "Except for me and Reina. She paces back and forth in the House Lychester common room, reading a print-out of her speech while I sit on the couch, fanning myself with a notebook."

    show reina neutral at center
    # TODO: Add missing Reina line
    r "\"The next few years for us students will no doubt be turbulent, and a steady guide will be needed to guide us through it.\" Ugh, I said \"guide\" twice."

    "She halts to scribble out the offending word and jot down a replacement. Then, standing up again, she clears her throat."

    vl reina_vl_prefix 2
    r "Okay. \"The next few years for us students will no doubt be turbulent, and a steady hand will be needed to guide us through it.\""
    voice sustain
    r "That sounds better, right?"

    a "Hmm?"

    show reina worried
    vl reina_vl_prefix 3
    "Reina sighs."
    voice sustain
    r "Are you even paying attention?"

    a "Of course. But, I thought it sounded great three drafts ago."

    vl reina_vl_prefix 4
    r "Three drafts ago, I didn't even have a conclusion."

    a "I just think maybe you're overthinking it. You've put everything into this campaign for a month now."
    a "You're clearly the best person for the job–"

    show reina flustered
    vl reina_vl_prefix 5
    r "Everyone hated me for the first half of the school year."
    
    a "I didn't hate you."

    vl reina_vl_prefix 6
    r "Besides you."

    a "That was months ago, and you've worked yourself to the bone."
    a "Don't you think you should take some time to rest up before the big day? You've earned it."

    show reina worried
    "She frowns at me, unconvinced. Birdsong filters from the window. I hold a hand up to my ear to listen."

    a "What's that? They're saying, \"Reina, come outside. You're already Vitamin D deficient.\""

    show reina neutral
    "Reina rolls her eyes."

    vl reina_vl_prefix 7
    r "I am not."

    a "You will be if you spend every sunny day cooped up in this room. Did you know that sunshine has been linked to a 100 percent increase in Presidential campaign success?"

    show reina happy
    vl reina_vl_prefix 8
    r "You're ridiculous."

    "I shoot her a pleading look. She cracks a smile."

    vl reina_vl_prefix 9
    r "I suppose I could take an hour off."

    a "Or three."

    vl reina_vl_prefix 10
    r "Now you're being greedy."

    "I flash her a mischievous grin."

    a "Wait here. I'll grab a blanket."

    scene bg wright_field_afternoon with fade 

    "The two of us make our way to the field, careful to avoid a few darting athletes or poorly-timed arrows."
    "Finding a shaded spot on the grass, I lay out my picnic blanket."

    show reina neutral at center
    vl reina_vl_prefix 11
    r "All this talk of Vitamin D, and you choose a spot in the shade."

    a "I'm sure my sunburn from the walk over evens it out."

    "Chuckling, she plops down beside me on the blanket. We lie there for a long while, cloud-watching and savoring the early summer breeze."

    show reina happy
    "Then, out of the blue, Reina turns to me and grabs my hand."

    vl reina_vl_prefix 12
    r "Thank you, [a]."

    a "I told you it was a nice day."

    vl reina_vl_prefix 13
    r "Not just for this. For everything. I couldn't have done this campaign without you."

    a "All I did was hang posters."

    vl reina_vl_prefix 14
    r "That's not true. Without you, I wouldn't have had the courage to run in the first place."
    voice sustain
    r "Whatever happens tomorrow, it means the world to me."

    "I squeeze her hand."

    #a "It was the least I could do. You helped make MIA my home."
    #a "And, whether  you're here or off in Apanaʻoha, I know you'll do the same for the incoming students next year, too. And, who knows? Maybe you'll meet another fourth-year stray to take my place."
    a "It was the least I could do. You helped make MIA my home. And, whether  you’re here or off in Ekaska, I know you’ll do the same for the incoming students next year, too."
    a "And, who knows? Maybe you’ll meet another fourth-year stray to take my place."

    show reina flustered
    "She smiles at me, eyes glistening with tears."

    vl reina_vl_prefix 15
    r "No one could do that, [a]."

    "We remain there for a long time, hand in hand, listening to the birdsong and savoring each other's company."
    
    #jump to second clubd route verabris
    $ renpy.call(chosen_club2 + "_route_verabris", "Verabris", 8)
    #jump student_council_verabis

label disciplinary_route_overa(month, date):
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Epilogue/Reina_Epilogue_"

    call screen calendar(month, date, "Overa", 19)
    scene bg student_councilroom_afternoon with fade

    $ renpy.notify("Reina - \nLenday, Overa 19th, 1028 RD")

    #"It's been an hour since they called the final vote, and Sue has officially passed the torch to Reina as IHA's first elected student body president."
    #"She should be celebrating her victory, resting on her laurels and savoring the hard-won fruits of her labor– but, of course, Reina's never been one to rest."
    "It’s been four days since they called the final vote, and Sue has officially passed the torch to Reina as IHA’s first elected student body president."
    "The final day of the Student Council term just ended. So, Reina {b}should{/b} be celebrating her victory, resting on her laurels and savoring the hard-won fruits of her labor– but, of course, Reina’s never been one to rest."
    "So, when I enter the Student Council room in hopes of locating my ever-elusive water bottle, I'm only half-surprised to find Reina seated at our old desk, sorting through the school year's final batch of citations."

    show reina neutral 
    a "You're still here? Everyone's headed to The Amity to celebrate."

    vl reina_vl_prefix 1
    r "I'm almost finished."

    a "You realize you're off of the disciplinary committee now?"

    vl reina_vl_prefix 2
    r "Technically, my term ends tonight."

    "Rolling my eyes, I take the seat across from her."

    vl reina_vl_prefix 3
    r "What're you doing?"

    a "Many hands make light work. And, the quicker I get you out of here, the quicker I get my cheese fries." 

    "Reina hands me a folder. After a quarter hour of working in silence, we file away our last citations and lock the cabinets."

    "One of Reina's campaign posters on the wall catches her eye. She lets out a sigh."

    show reina worried at center
    vl reina_vl_prefix 4
    r "I think I'm still in shock. I mean, class president? How did I get so lucky?"

    a "It's not luck. You busted your ass for this, and you're going to be the best president MIA's ever had."
    a "I just wish I could be here to see it."

    show reina happy
    vl reina_vl_prefix 5
    "Reina smiles at me, then gasps, remembering something."
    voice sustain
    r "Oh, I almost forgot. I have something for you."

    "She reaches into her bag and pulls out a small, neatly-wrapped box."

    show reina flustered
    vl reina_vl_prefix 6
    r "I was going to wait until after graduation, but now seems as good a time as any..."

    "Fluffing up the bow, she hands me the giftbox."
    
    a "Thank you. Should I open it now?"

    show reina happy
    vl reina_vl_prefix 7
    r "Please do."
    jump disciplinary_route_overa_choice

label disciplinary_route_overa_choice:
    if player_gender == "male":
        $ reina_platonic = True
        jump disciplinary_route_overa_platonic
    else:
        jump disciplinary_route_overa_romance

label disciplinary_route_overa_romance:
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Epilogue/"+ player_gender + " MC/Reina_Epilogue_Fem_"

    show reina happy 
    "I unwrap the box, revealing a stunning black opal necklace. The pendant is carved in the shape of a wolf's head."

    vl reina_vl_prefix 1
    r "It's meant to match your other necklace. The chain should be a little longer so you can wear them together– provided your future job doesn't have a dress code."

    "I gawk at the necklace, speechless. If this truly is black opal, it must have been imported and cost a small fortune."
    "It's the most lavish and thoughtful present anyone's ever given me."

    vl reina_vl_prefix 2
    r "Do you like it?"

    a "Like it? It's incredible. Thank you, Reina."

    "I pull her into a tight embrace."

    show reina flustered
    vl reina_vl_prefix 3
    r "Here, I'll help you put it on."

    "I lift my hair, and Reina steps behind me to clasp the necklace around my throat."
    "She lingers there a moment. When she steps away to face me, I notice that her cheeks are red. She evades my eyes, looking sheepish."

    a "What's wrong?"

    show reina worried
    vl reina_vl_prefix 4
    r "I have to tell you something."

    a "Alright…"

    "Reina clears her throat, still avoiding my gaze."

    vl reina_vl_prefix 5
    r "Since my mother passed, no one ever took a personal interest in me."
    voice sustain
    r "My first two years at MIA, my classmates were so fearful of somehow offending me or my status that they avoided me altogether."

    vl reina_vl_prefix 6
    r "It sounds dramatic, but some days, I thought I was destined to be alone."
    voice sustain
    r "I had made peace with that… Then, I met you. And, after this year, I can't imagine my life without you in it."

    show reina neutral
    "She lifts her eyes to meet mine."

    vl reina_vl_prefix 7
    r "We promised to care for each other for as long as we were both at MIA, but now that I've started caring for you, [a], I don't think I could ever stop."
    voice sustain
    r "So, I need to know: do you feel the same?"

    menu:
        "Accept Reina's confession":
            $ reina_romance = True
            jump disciplinary_route_overa_romance_accept
        "Reject Reina's confession":
            $ reina_romance = False
            $ reina_platonic = True
            jump disciplinary_route_overa_romance_reject

label disciplinary_route_overa_romance_accept:
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Epilogue/"+ player_gender + " MC/Accepted/Reina_Epilogue_FemAccept_"
    $ sue_vl_prefix = "audio/voices/Love Interests/Sue/Reina/SueDaengQan_Reina/SueDaengQan_Reina_"

    show reina flustered 
    a "How could I not?"

    "I'm not exactly playing it cool, but then again, I've never been so flustered in my entire life."
    "This girl– this incredible, brilliant, selfless girl who will absolutely rule the world one day— chose me?"

    "She's miles out of my league, but I won't argue with her. Instead, I reach for her hand."

    a "Reina, I care for you more than anyone I've ever met, which, frankly, terrifies me. But, I'm willing to face my fears."

    show reina happy
    "Delighted, Reina pulls me in close, tears spilling onto her cheeks."

    vl reina_vl_prefix 1
    r "Oh, I'm so relieved! I don't know what I'd have done if you'd said no."

    a "You'd have become president and left me in the dust, obviously. But, I'd rather you didn't."

    "She squeezes my hand."

    vl reina_vl_prefix 2
    r "I know things will be different after you graduate."
    voice sustain
    #r "I imagine you'll return home to Prospera, and I'll be back in Centra for the summer, then in Apanaʻoha, then gods know where after that–"
    r "I imagine you’ll return home to Prospera, and I’ll be back in Centra for the summer, then in Ekaska, then gods know where after that–"

    a "We'll figure that out. For now, we're here together."

    show reina flustered
    "She smiles up at me. Then, closing her eyes, she leans in to kiss me. We remain there for a moment, the only two people in the world–"

    "Without warning, the door to the office flies open–"

    vl sue_vl_prefix 8.2
    s "Hey, [a], I found your–"

    show reina flustered 
    "Reina and I fly apart as Sue pokes her head into the room, carrying my long-lost water bottle. Looking between us, Sue smirks." 

    show sue neutral at right 
    vl sue_vl_prefix 9.2
    s "I'll meet you lovebirds at The Amity."
    hide sue 
    "She sets down my bottle and slips out of the room, closing the door behind her."
    "Giggling, Reina and I turn to face each other. She interlaces her fingers with mine."

    show reina happy
    vl reina_vl_prefix 3
    r "How about those cheese fries?"
    call epilogue_graduation("Overa", 19) from _call_epilogue_graduation_11

label disciplinary_route_overa_romance_reject: 
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Epilogue/"+ player_gender + " MC/Rejected/Reina_Epilogue_FemReject_"
    $ sue_vl_prefix = "audio/voices/Love Interests/Sue/Reina/SueDaengQan_Reina/SueDaengQan_Reina_"

    show reina neutral 
    a "I do care for you… as a friend."

    show reina worried
    "I can see the realization play across Reina's features in real time. Her shoulders slump as she averts her eyes and slowly nods to herself."
    "Gods, I've never seen her so dejected."

    a "I'm sorry. I know that's not what you wanted to hear."

    vl reina_vl_prefix 1
    r "It's alright. I suspected as much."

    a "It's just, I'm graduating, and you'll have such a full plate with the presidency–"

    show reina neutral at center with dissolve
    vl reina_vl_prefix 2
    r "Don't worry, [a]. I understand, and I appreciate your honesty."

    "She plasters on a smile, swallowing her hurt. I'll hand it to her– she's a born diplomat."

    "Suddenly, the door to the office flies open."

    vl sue_vl_prefix 8.2
    s "Hey, [a], I found your–"

    show sue neutral at right
    "Sue enters the room, carrying my long-lost water bottle. Seeing Reina, she cuts herself off."

    vl sue_vl_prefix 10.1
    s "Reina, what are you doing here? They're waiting for you."
    show reina worried
    "Reina subtly dabs her eyes."

    vl reina_vl_prefix 3
    r "I'll catch up shortly."
    show sue melancholic 
    "Sue looks between me and Reina, clearly sensing the tension. She clears her throat and sets my bottle down on the closest table."

    vl sue_vl_prefix 11.1
    s "Right, well… I'll see you over there."
    hide sue 
    "She exits, closing the door behind her. Reina turns to face me."

    vl reina_vl_prefix 4
    r "You should walk with her."

    a "You're not coming?"

    vl reina_vl_prefix 5
    r "I will. I just need some time to clear my head."

    "Remembering Reina's gift, my hand flies to my throat."

    a "Your necklace…"

    show reina neutral
    vl reina_vl_prefix 6
    r "Keep it. It's the least I can do, after everything you've done for me this year."

    "We stare at each other for a moment in awkward silence, then I turn away to grab my things."

    a "Congratulations, Reina."

    vl reina_vl_prefix 7
    r "Thank you, [a]."

    "Forcing a smile, I head for the door, leaving Reina alone with her thoughts."
    call epilogue_graduation("Overa", 19) from _call_epilogue_graduation_12

label disciplinary_route_overa_platonic:
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Own Route/Epilogue/"+ player_gender + " MC/Reina_Epilogue_Masc_"
    
    show reina happy 
    "She nods. I unwrap the box, revealing a stunning black wolf, carved from obsidian."

    vl reina_vl_prefix 1
    r "I saw this in town the other day and had to get it for you."

    "Speechless, I continue to gawk at the figure."

    vl reina_vl_prefix 2
    r "Do you like it?"

    a "Like it? It's perfect. Thank you, Reina."

    "I pull her in for a hug."

    a "Now I feel bad. I should've gotten you something, too."

    show reina happy
    vl reina_vl_prefix 3
    r "Your presence is enough of a present. That said, I wouldn't be opposed to some cheese fries…"

    "I hold out my hand."

    a "You have yourself a deal."

    "Laughing, she shakes it. Together, we leave the Student Council room and head into town."
    jump epilogue_graduation

label epilogue_disciplinary_route:
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Shared Epilogue/Goodbye to Reina/Reina_SharedEpilogue_Goodbye_"

    scene bg maincastle with fade

    "My search for my family remains fruitless. I'd have expected one of them to call me by now."
    "If they haven't done it, I may as well call one of them myself."

    "As I take my phone out of my pocket, someone crashes into me."
    "I drop my phone, but before I can crouch to retrieve it, it's already been snatched off the ground and is being offered to me."

    show reina neutral at center with dissolve
    vl reina_vl_prefix 1
    r "My apologies. It's so busy that it's easy to get jostled about."

    "I take the phone."

    a "Thanks."
    jump epilogue_reina_choice

label epilogue_reina_choice:
    if chosen_club == "disciplinary":
        if reina_romance:
            jump epilogue_disciplinary_route_romance_accept
        elif reina_platonic:
            jump epilogue_disciplinary_route_platonic
        else: 
            jump epilogue_disciplinary_route_romance_reject
    else:
        jump epilogue_disciplinary_route_not_chosen

label epilogue_disciplinary_route_romance_accept:
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Shared Epilogue/Goodbye to Reina/Accepted/Reina_SharedEpilogue_Goodbye_Accepted_"

    show reina neutral at center
    "But why is a third year in all this chaos? It isn't like she's here for family or anything."
    "Hold on a second, of course she's here."

    a "I guess it only makes sense for you to be here, Madame President."
    a "Only you would volunteer to sit in the sun for hours listening to the headmaster rattle off names of people you'll never see again."

    show reina flustered 
    vl reina_vl_prefix 1
    "She huffs."
    voice sustain
    r "Please don't. I'm just passing through, is all."

    show reina happy 
    "Her eyes fall on my diploma, and she smiles."

    vl reina_vl_prefix 2
    r "Congratulations. You worked hard for this."

    a "Thanks."

    vl reina_vl_prefix 3
    r "Before I forget, I will need your address at some point."
    voice sustain
    #r "I'm going to want to send you souvenirs from our time in Apanaʻoha next year."
    r "I’m going to want to send you souvenirs from our time in Ekaska next year."

    a "I'd rather go there. Preferably with you."

    show reina flustered 
    "Reina's eyes widen and her face goes red at my comment. Getting flustered at a little comment like that? How cute."

    vl reina_vl_prefix 4
    r "O-one day, yes..."

    show reina happy 
    vl reina_vl_prefix 5
    "She clears her throat, quickly regaining her composure."
    voice sustain
    r "Creator knows I'll have the money to bring you. And by then, I'll know enough to be your personal tour guide."

    a "I really like the sound of that."

    vl reina_vl_prefix 6
    r "I do have to find the headmaster, so this is goodbye for now. But tonight, after everything winds down, let's talk?"

    a "Let's. Bye, Reina."

    show reina flustered 
    "She steps forward, taking my hand. I'm in danger of getting lost of those beautiful brown eyes of hers, but barely a moment later, she steps back."

    a "What, too many people around?"

    vl reina_vl_prefix 7
    r "I never was particularly fond of public displays of affection. But... soon. Behind closed doors."

    a "I'll be looking forward to it."

    show reina neutral 
    "Her eyes dart around, checking to make sure no one's paying too much attention to us. When she's satisfied, she turns back to me."

    vl reina_vl_prefix 8
    r "As will I."

    "She curtsies."

    vl reina_vl_prefix 9
    r "Take care, [a]. Until the next time we speak. Which will hopefully be soon."

    hide reina with fade
    "Turning, she hurries off into the crowd."
    jump epilogue_literature_route

label epilogue_disciplinary_route_romance_reject:
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Shared Epilogue/Goodbye to Reina/Rejected/Reina_SharedEpilogue_Goodbye_Rejected_"

    show reina neutral at center
    "A moment of silence lingers between us. Even with all of the noise people are making around us, that silence is deafening."

    a "So..."

    vl reina_vl_prefix 1
    r "Congratulations. You worked hard for this."

    show reina worried 
    "My eyes dart down to my diploma."

    a "Right. Thank you."

    vl reina_vl_prefix 2
    r "Thank you for being my friend this past year, [a]. Whatever the future may have in store for you, I wish you the best."

    show reina neutral 
    "She curtsies."

    vl reina_vl_prefix 3
    r "If you'll excuse me, I have to go find the headmaster. Until our next meeting, whenever that may be."

    hide reina with dissolve
    "Turning on a heel, Reina disappears into the crowd again."
    jump epilogue_literature_route

label epilogue_disciplinary_route_platonic:
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Shared Epilogue/Goodbye to Reina/No Confession/Reina_SharedEpilogue_Goodbye_None_"

    show reina neutral at center
    "But why is a third year in all this chaos? It isn't like she's here for family or anything."
    "Hold on a second, of course she's here."

    a "I guess it only makes sense for you to be here, Madame President."
    "Only you would volunteer to sit in the sun for hours listening to the headmaster rattle off names of people you'll never see again."

    show reina flustered 
    vl reina_vl_prefix 1
    "She huffs."
    voice sustain
    r "Please don't. I'm just passing through, is all."

    show reina happy 
    "Her eyes fall on my diploma, and she smiles."

    vl reina_vl_prefix 2
    r "Congratulations. You worked hard for this."

    a "Thanks."

    vl reina_vl_prefix 3
    r "Before I forget, I will need your address at some point. I'm going to want to send you souvenirs from our time in Apanaʻoha next year."

    a "You don't have to put yourself out for me like that. Besides, I still owe you for the wolf."

    vl reina_vl_prefix 4
    r "Perish the thought. The gift wasn't something to be repaid."
    voice sustain
    #r "And sending you all manner of Pacifican presents is the least I can do to thank you for being my friend this past year."
    r "And sending you all manner of Ekaskan presents is the least I can do to thank you for being my friend this past year."

    a "I don't think you have to thank me for being a friend."

    show reina happy
    vl reina_vl_prefix 5
    r "And I think I do, so there."

    a "Touché."

    vl reina_vl_prefix 6
    r "Now that I think about it, Sue tells me you're considering some governance-adjacent degree?"

    a "That's right."

    vl reina_vl_prefix Laugh
    "She laughs."

    vl reina_vl_prefix 7
    r "So there's a chance the future Duchess and Premier of Centra will have been schoolmates. How nice."

    a "Me, a Premier? You have too much faith in me."

    vl reina_vl_prefix 8
    r "And you don't have nearly enough in yourself."

    show reina neutral
    vl reina_vl_prefix 9
    "She gasps."
    voice sustain
    r "I have to find the headmaster. Time for me to go."

    "She curtsies."

    vl reina_vl_prefix 10
    r "Take care, [a]. Until the next time we speak. Which will hopefully be soon."

    hide reina
    "Turning, she hurries off into the crowd."
    jump epilogue_literature_route

label epilogue_disciplinary_route_not_chosen:
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Shared Epilogue/Goodbye to Reina/Not Chosen/Reina_SharedEpilogue_Goodbye_NotChosen_"

    show reina neutral at center
    "Reina stands before me, twiddling her thumbs."

    a "Is... something wrong?"

    show reina worried
    vl reina_vl_prefix 1
    r "I'm sorry. For writing you up on your first day here."

    "It takes me a second to remember that far back. Then it hits me. Father's necklace."

    a "All's well that ends well, I guess. Now it isn't an issue anymore."

    show reina neutral at center with dissolve
    vl reina_vl_prefix 2
    r "True. It's good that our underclassmen won't have to worry about such archaic rules being abused anymore."

    a "Says the one who abused them."

    vl reina_vl_prefix 3
    r "And better it be someone trying to enact change than a bad actor, no?"

    "All of a sudden, she curtsies."

    vl reina_vl_prefix 4
    r "If you'll excuse me, I must go find the headmaster. Take care, Blakesley."

    hide reina with dissolve
    "She turns on a heel and heads back into the crowd."
    jump epilogue_literature_route

label reuinion_disciplinary_route:
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Shared Epilogue/Meet the Family/Reina_SharedEpilogue_Family_"
    $ arline_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Arline/Epilogue/Meet Reina/Arline_Epilogue_MeetReina_"
    $ skylar_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Skylar/Meet Reina/Skylar_Epilogue_MeetReina_"
    $ salem_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Salem/Meeting Reina/Salem_Epilogue_MeetReina_"

    show reina happy at center with dissolve

    $ renpy.notify("Reina - Meeting the Family\nNyday, Overa 25, 1028 RD")

    "When Reina arrives, she performs a picture perfect curtsy for the family."

    vl reina_vl_prefix 1
    r "It's a pleasure to meet you all. My name is Reina Dreyar."

    vl salem_vl_prefix 1
    salem "Whoa. Like the Dreyar?"

    show reina neutral with dissolve
    vl reina_vl_prefix 2
    r "You've no doubt heard about my father, yes."

    vl skylar_vl_prefix 1
    sky "Being around someone so noble is making me feel self-conscious."

    show reina happy
    vl reina_vl_prefix 3
    r "Please, don't be. I'm only a few years older than you, so I'm hoping we'll be able to become friends someday."

    vl skylar_vl_prefix 2
    sky "Where are my manners? I'm Skylar. The rude one is Salem."

    vl salem_vl_prefix 2
    salem "What was that about manners?"

    vl arline_vl_prefix 1
    arline "Arline Blakesley, at your service. It's a pleasure to meet you, Lady Reina."

    show reina flustered with dissolve
    vl reina_vl_prefix 4
    r "The pleasure is all mine. You've raised a fine daughter, ma'am."

    vl arline_vl_prefix 2
    arline "You flatter me, my lady."

    "Mother turns to the twins."

    vl arline_vl_prefix 3
    arline "Salem, Skylar, could you keep Reina company for a minute?"

    hide reina with fade
    "She leads me a short distance away from them."

    vl arline_vl_prefix 4
    arline "You're in a relationship with the daughter of the richest man in the world?"

    a "That's just sort of how it happened. Mother, about why you sent me here..."

    vl arline_vl_prefix 5
    arline "Don't worry, I've changed my mind."

    a "You have?"

    vl arline_vl_prefix 6
    arline "I lost the nerve. Her money would save us, but she deserves better than being used like that."

    a "So we're in agreement."

    "I sigh."

    a "I worried I was going to have to choose between you two for a minute there. Thank the Divines."

    show reina happy at center with dissolve
    "When we return, the three are laughing amongst themselves."
    jump finale