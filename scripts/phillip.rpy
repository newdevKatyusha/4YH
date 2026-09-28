label phillip_jinus(month, date):
    $ phillip_vl_prefix = "audio/voices/Supporting-Extra/Phillip/Own Route/Month 1/Phillip_Month1_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Phillip/Month 1/" + player_voice_prefix + "_Phillip_Month1_"

    call screen calendar(month, date, "Jinus", 20)
    scene bg maincastle with fade

    $ renpy.notify("Phillip - \nUctday, Jinus 20th, 1027 RD")
    
    "The gentle warmth of the early autumn sun is exactly what I need after being cooped up in Magis Hall all day. It's been a few weeks since the school year started properly."
    "I wasn't expecting the material to be so advanced. Language Arts and Math, I'm doing well enough. Science and History, though..."
    "Then there's the fact that I'm in my magic classes with a bunch of first years. Guess that's to be expected when you show up so late."
    "I just got out of a meeting with my Fundamentals of Magic Instructor, but a lot of the talk we had about the ethical use of magitechnology in treating terminal illness went over my head."
    "Lucas did say I could go to him if I ever needed help in class, and he's been through this before. May as well head to the library and see if I can find him."
    
    scene bg weaver_library_afternoon with fade
    
    "The library isn't as dead as the day I first showed up, but it still isn't like there are many people around. Nor is Lucas one of them. I walk around, scanning the aisles, but he's nowhere to be seen."
    "I don't find Lucas, but I do find someone else I recognize, sitting all by his lonesome at a table in the corner. Prince Phillip has a textbook open in front of him but doesn't look like he's reading. Just zoning out."
    "I walk over to him and take a seat."
    
    show phillip contemplative at center with dissolve
    
    vl alexis_vl_prefix 1
    a "Mind if I join you?"
    
    show phillip neutral at center
    if eval(a.name)[0] == "Alexis":
        vl phillip_vl_prefix 1A
        p "Not at all. You were... [a], right?"
    else:
        vl phillip_vl_prefix 1B
        p "Not at all. You were... Blakesley, right?"
    
    #TODO: Missing line
    a "I'm honored that you remember me."
    
    vl phillip_vl_prefix 2
    p "Don't be. I've heard Sue say your name enough times during Student Council meetings that it would be embarrassing if I didn't remember."
    
    "He's right about that. Up to three times a week, we see each other there. Though he's usually about as tuned in there as he was when I found him a second ago."
    "Actually, about that..."
    
    vl alexis_vl_prefix 2
    a "Are you doing alright, Your Highness? You seemed a bit out of it. Need help with some of your work?"
    
    "Sure, I came here to get help, but first year material should be a cakewalk for me."
    
    show phillip contemplative at center
    vl phillip_vl_prefix 3
    p "Not really, no."
    
    vl alexis_vl_prefix 3
    a "Then what's up?"
    
    "He takes a moment to weigh whether or not he actually wants to tell me. Then he sighs."
    
    show phillip tired at center
    vl phillip_vl_prefix 4
    p "I don't know if putting me on the Student Council was the right move. I mean, why?"
    
    vl alexis_vl_prefix 4
    a "You didn't ask? I thought..."
    
    "I trail off. Sue was right about this year being special. The sectors and Headmaster Goude's plan to travel the world with the school have been brought up in most meetings. And usually when they do, eyes drift to the prince."
    
    vl phillip_vl_prefix 5
    p "I didn't ask to be the center of attention."
    
    "But he's in Special Operations, and royalty. 'Leader of the faction that wants to keep the sectors around' was handed to him on a silver platter for those two things alone. All pressure, no privilege."
    
    vl alexis_vl_prefix 5
    a "Sounds rough."
    
    vl phillip_vl_prefix 6
    p "It certainly can be."
    
    "I think about home. Mother, Salem, and Skylar waiting for me, relying on me. Those three are my world, and sometimes thinking about them is overwhelming. Having hundreds of people look to you to fight for them in the Council must be so much worse."
    "And then there's thinking about the entire empire when he takes over some day. How many millions of people are going to have their eyes on him then? Gods, that thought is terrifying."
    
    vl alexis_vl_prefix 6
    a "I'm no good at politicking, but if you ever feel like you need someone to listen to you rant about things, you can always come to me. I'm plugged in but don't really have a dog in the fight. How does that sound?"
    
    show phillip neutral at center
    vl phillip_vl_prefix 7
    p "Very useful, thank you."
    
    "I remember why I came to the library in the first place and stand up."
    
    vl alexis_vl_prefix 7
    a "I've got to run. I was looking for someone. Take care, Your Highness."
    
    if eval(a.name)[0] == "Alexis":
        vl phillip_vl_prefix 8A
        p "You too, [a]."
    else:
        vl phillip_vl_prefix 8B
        p "You too, Blakesley."
    
    hide phillip with dissolve
    
    "As I leave the library, the gravity of the Council's duty this year becomes a bit clearer to me. It isn't just the students now that'll be impacted by what's going on."
    "The next three classes get to travel the world, and then every class after them will still be split up in the sectors, probably. And it's this group's job to decide if they even have that chance."

    $ renpy.call(chosen_club2 + "_route_jinus", "Jinus", 20)

label phillip_vanus(month, date):
    $ phillip_vl_prefix = "audio/voices/Supporting-Extra/Phillip/Own Route/Month 3/Phillip_Month3_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Phillip/Month 3/" + player_voice_prefix + "_Phillip_Month3_"

    call screen calendar(month, date, "Vanus", 7)
    scene bg mainstreet_afternoon with fade

    $ renpy.notify("Phillip - \nToleday, Vanus 7th, 1027 RD")

    "Huntsdale is a nice little town. After all this time, I'm really starting to get used to it."
    "I've had a few chances to head down to the capital on the weekends, but it just can't compare."
    "Glancing over my shoulder, I take in the cafe I just walked out of."
    "I'm really going to miss The Amity at the end of the school year."
    "Where else am I going to find a nice little place as cozy as this?"
    "Much as I want to walk right back in, sit back down with Sue, and continue our talk, homework calls."
    "I start on my way back to House Lychester so I can sequester myself in my room and get it over with."
    "I wait at the edge of a street, waiting for the traffic light to give me the right of way."
    "A few other people join me. It takes several of them whispering for me to realize that the prince is in our little group."

    vl alexis_vl_prefix 1
    a "Your Highness, over here!"

    "He turns towards me. Seeing my familiar face, he lights up a bit and makes his way through the crowd over to me."

    show phillip excited at center with dissolve
    vl phillip_vl_prefix 1
    p "We meet again."

    vl alexis_vl_prefix 2
    a "Yeah. What's up?"

    show phillip neutral
    vl phillip_vl_prefix 2
    p "Just on a patrol."
    
    "A patrol? Like a cop? The question must've been written plainly on my face, because he smirks at me."

    show phillip excited
    vl phillip_vl_prefix 3 
    p "Part of the Special Operations curriculum: helping to keep the peace. Even in a quiet little town like Huntsdale."

    "A silence falls between us. At least the rest of our crowd keeps us from standing in complete quietude."
    "When the crosswalk light turns, we follow the crowd."
    "The pause in the talk reminds me of the meeting Sue had with the presidents last month."

    show phillip neutral
    vl alexis_vl_prefix 3   
    a "Sorry about Ultire, by the way."
    
    "The prince had been thrust into a leadership role in what's become known as the 'Sectorist' faction, but it was Ultire doing most of the legwork."
    "With him out of the Council, it's left them in a bit of a bind."

    show phillip tired
    vl phillip_vl_prefix 4
    p "It isn't like you voted to kick him out. From what I've heard, no one could've saved him, with how the rules are written."

    vl alexis_vl_prefix 4
    a "On the bright side, it lit a fire under everyone's asses."

    show phillip excited
    vl phillip_vl_prefix 5  
    p "Thankfully."

    vl alexis_vl_prefix 5
    a "Where does that leave you, though? The Sectorists are still doing things in the background, aren't they?"

    show phillip neutral
    vl phillip_vl_prefix 6  
    p "We'll make due, somehow. Some allies decided it would be best to use this lull to rework our strategy."

    vl alexis_vl_prefix 6
    a "You don't mind being the only real leader now?"

    show phillip tired
    vl phillip_vl_prefix 7
    p "Doesn't really matter, does it? They're relying on me, so I have to step up, one way or another."

    vl alexis_vl_prefix 7
    a "I guess so."
    
    "He was probably raised with that sort of mindset. After all, it wasn't a secret to anyone he'd be Emperor someday."
    "May as well get him used to the idea of trying to serve the public and all."
    "Just leaving it at that bothers me, though."

    show phillip neutral
    vl alexis_vl_prefix 8
    a "This is off the record, but I like them both. The sectors and the headmaster's crazy idea of going all over the world."
    
    "The prince seems surprised at that."

    show phillip excited
    vl alexis_vl_prefix 9
    a "I can't make any promises, but I can try talking to Sue."

    show phillip contemplative
    vl phillip_vl_prefix 8
    p "Thanks for the offer, but... do you think that would help? I have trouble reading her sometimes."

    "So do I. For better or worse, she seems to prefer a more hands off approach."
    "Facilitate the meetings, be generally likable."
    "But with how she plays her cards close to her chest, I can only imagine what would happen if she were to tip the scales."

    vl alexis_vl_prefix 10
    a "Well, it wouldn't hurt to try, would it?"

    show phillip excited
    vl phillip_vl_prefix 9  
    p "I suppose it wouldn't."

    "He stops walking."

    show phillip neutral
    vl phillip_vl_prefix 10
    p "Looks like we're at your stop."

    "And he's right. Right out in front of House Lychester."

    vl alexis_vl_prefix 11
    a "Then I guess this is goodbye. I'll be in touch if the whole Sue thing works out."
    voice sustain
    a "And good luck with the rest of your patrol."

    show phillip excited
    if eval(a.name)[0] == "Alexis":
        vl phillip_vl_prefix 11A
        p "Thanks again. Until next time, [a]."
    else:
        vl phillip_vl_prefix 11B
        p "Thanks again. Until next time, Blakesley."

    hide phillip with dissolve
    scene black with fade
    
    #jump to main club route vanus
    $ renpy.call(chosen_club + "_route_vanus", "Vanus", 7)
    #jump route_branch_point2

label route_branch_point2:
    if chosen_club == "no_clubs":
        jump no_clubs_route_vanus
    elif chosen_club == "disciplinary":
        jump disciplinary_route_vanus
    elif chosen_club == "literature":
        jump literature_route_vanus
    elif chosen_club == "anime":
        jump anime_route_vanus
    elif chosen_club == "home_ec":
        jump home_ec_route_vanus
    else:
        jump archery_route_vanus

label phillip_neralt(month, date):
    $ goude_vl_prefix = "audio/voices/Supporting-Extra/Isaiah/Phillip/Month 5/Isaiah_Phillip_Month5_"
    $ phillip_vl_prefix = "audio/voices/Supporting-Extra/Phillip/Own Route/Month 5/Phillip_Month5_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Phillip/Month 5/" + player_voice_prefix + "_Phillip_Month5_"


    call screen calendar(month, date, "Neralt", 10)
    scene bg dorm_common_noon with fade

    $ renpy.notify("Phillip - \nLenday, Neralt 10th, 1027 RD")

    vl alexis_vl_prefix 1
    a "Is that…?"

    "I've just gotten off the elevator in House Lychester. I'm on my way out to spend some time with friends and barely out of the elevator before I spot the prince saying goodbye to a few other students."
    "Judging by the pins on their lapels, they're Spec Ops students like him."

    show phillip neutral at center with dissolve
    
    vl alexis_vl_prefix 2
    a "Wasn't expecting to see you here, Your Highness."

    vl phillip_vl_prefix 1
    p "Had a bit of business to attend to. The second Residencies start this weekend, so I was coordinating with some of the Lychesters."

    vl alexis_vl_prefix 3
    a "So you're on the clock even outside of the Student Council room?"

    show phillip tired
    vl phillip_vl_prefix 2
    p "That's how it ended up."

    show phillip neutral at center
    vl alexis_vl_prefix 4
    a "What are these Residencies like, anyway?"

    show phillip excited
    vl phillip_vl_prefix 3
    p "We get on an airship, go somewhere in the empire, stay there for a week, and help people. I know a friend in Civic Magic was helping a local doctor."
    voice sustain
    p "Since we were in a small town, the Spec Ops mainly did odd jobs."

    vl alexis_vl_prefix 5
    a "And in the cities?"

    show phillip neutral
    vl phillip_vl_prefix 4
    p "We help local law enforcement, from what I hear. Like our patrols, but more active."

    vl alexis_vl_prefix 6
    a "So like week long internships. And it's not just Magiana?"

    vl phillip_vl_prefix 5
    p "I was in Troara the first time, and I'm going to Aragon next."

    "So they're already getting to see the world, huh? And not just to see the sights but help locals. No wonder the headmaster thought this up."

    show phillip excited
    vl alexis_vl_prefix 7
    a "Imagine being able to do that in other parts of the world."

    vl phillip_vl_prefix 6
    p "I know. There's so much we could learn."

    "He pauses for a moment."

    show phillip contemplative
    vl phillip_vl_prefix 7
    p "People like me could hop on a flight whenever they want. Most couldn't."

    show phillip neutral
    vl alexis_vl_prefix 8
    a "But even if it's through the school, you run into the same problem stopping them from doing it on their own time."

    "He nods."

    show phillip tired
    vl phillip_vl_prefix 8  
    p "Money. I'll figure something out."

    show phillip excited
    vl alexis_vl_prefix 9
    a "Good luck. With that and the Residency."

    vl goude_vl_prefix 1
    h "What a surprise. I wasn't expecting to see you in House Lychester, Your Highness."

    "The headmaster joins us, nodding to me as he approaches."

    show phillip neutral
    vl goude_vl_prefix 2
    h "And it's nice to see you too, Blakesley. You're used to the school now?"

    vl alexis_vl_prefix 10
    a "I'd sure as sin hope so after all this time. If anything, I'm surprised to see you here, Headmaster."

    vl goude_vl_prefix 3
    h "I was discussing some things with Lychester's Head of House."

    "He turns to the prince."

    vl goude_vl_prefix 4
    h "Like I'm sure you were meeting with your peers in Special Operations?"

    "The prince briefly summarizes his meeting to the headmaster as I stand and listen. And as I do, a question pops into my head."

    #TODO: Missing line
    a "Why are these even on debate in the council anyway? You've already implemented them."

    "The prince crosses his arms and furrows his brow."

    show phillip contemplative
    vl phillip_vl_prefix 9
    p "I haven't thought about it much, but you're right."

    vl goude_vl_prefix 5
    h "The answer to that lies in the school's history."

    "I groan."

    show phillip neutral
    vl goude_vl_prefix 6
    h "Think of it like a royal decree. A court hasn't struck it down, so it remains in place."
    voice sustain
    h "But it isn't the law of the land, so it can't last forever unless Parliament makes it so."

    vl alexis_vl_prefix 11
    a "I think I get it. But why the civics lesson?"

    show phillip excited
    vl phillip_vl_prefix 10
    p "Mother's mentioned this before. The school was founded to train its students for life in imperial society after graduation."

    vl goude_vl_prefix 7
    h "That's right. I'm the executive, the board is the judiciary, the Council is the legislature, and the rest of the students are our subjects."
    voice sustain
    h "Without the Council's consent, my little pet project dies after this year."

    show phillip contemplative
    vl alexis_vl_prefix 12
    a "You're the headmaster, but students can overrule you? That sounds… complicated."

    vl goude_vl_prefix 8
    h "But such is politics. Before I go, Your Highness?"

    show phillip neutral
    vl phillip_vl_prefix 11
    p "What is it?"

    "I haven't seen the headmaster very often, but whenever I do, it's easy to forget that he's one of our teachers and not just an upperclassmen. Always so approachable and unassuming."
    "But there's a certain edge to the look he gives the prince, and to the tone of his voice when he next talks, that feels less like a dependable senior, and more like a wily politician."

    show phillip tired
    vl goude_vl_prefix 9
    h "I wish you the best in securing support for your version of the charter."

    "We leave the building and say goodbye before heading in opposite directions."
    "Most people on the Council would probably see the benefit of keeping the sectors around and approving the headmaster's study abroad plan."
    "The question was just how to come up with the money for it."
    
    hide phillip with dissolve
    
    #jump to main club route neralt
    $ renpy.call(chosen_club + "_route_neralt", "Neralt", 10)
    #jump route_branch_point3

label route_branch_point3:
    if chosen_club == "no_clubs":
        jump no_clubs_route_neralt
    elif chosen_club == "disciplinary":
        jump disciplinary_route_neralt
    elif chosen_club == "literature":
        jump literature_route_neralt
    elif chosen_club == "anime":
        jump anime_route_neralt
    elif chosen_club == "home_ec":
        jump home_ec_route_neralt
    else:
        jump archery_route_neralt

label phillip_elvera(month, date):
    $ goude_vl_prefix = "audio/voices/Supporting-Extra/Isaiah/Phillip/Month 7/Isaiah_Phillip_Month7_"
    $ phillip_vl_prefix = "audio/voices/Supporting-Extra/Phillip/Own Route/Month 7/Phillip_Month7_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Phillip/Month 7/" + player_voice_prefix + "_Phillip_Month7_"
    
    call screen calendar(month, date, "Elvera", 12)
    scene wilson_salon_afternoon with fade

    $ renpy.notify("Phillip - \nLenday, Elvera 12th, 1028 RD")

    "Only two and a half months left to go. Where did the time go? It's been nice, seeing the change in campus over the months."
    "First, it was less general anxiety about Reina writing people up for dress code violations."
    "Now it seems like everyone is in a better mood because of the news of the new charter and the things that come with it."
    "One weekend morning, I head up to the Salon in the Wilson Building, in the mood for a fancy brunch."
    "It was a small part of the Council's business, but there have been some rule changes."
    "Instead of needing to go with someone normally allowed, they can just sponsor a pass for someone."
    "I hear there are talks to fully convert it into a general use space for all students, but it isn't like I'll be around to see it."
    "Or anyone else for the next few years, for that matter."
    "I start looking for a seat when I get to the third floor. Over by a window I spy the prince and the headmaster sitting together."
    "When the prince sees me, he waves to me. It isn't like we're total strangers, so I head over to him."

    show phillip excited at center with dissolve
    
    vl alexis_vl_prefix 1
    a "I'm not interrupting anything?"

    vl goude_vl_prefix 1
    h "Not at all. You can take a seat, if you'd like."

    "I take him up on the offer, turning to the prince once I'm settled."

    show phillip neutral
    vl alexis_vl_prefix 2
    a "How does it feel now that all the hard work paid off?"

    "He lets out a little laugh."

    show phillip excited
    vl phillip_vl_prefix 1
    p "I'm not sure I'd call it \"hard work.\""

    vl alexis_vl_prefix 3
    a "How much money did you throw at this again?"

    show phillip contemplative
    vl phillip_vl_prefix 2
    p "Yes, because throwing money at the problem is hard work."

    vl alexis_vl_prefix 4
    a "When you did it the way you did? Yes. And don't act like you didn't do anything else to get people on board."

    show phillip neutral at center with dissolve
    vl phillip_vl_prefix 3
    p "Alright, I concede. But it is nice to see everyone. The excitement is infectious."

    vl alexis_vl_prefix 5
    a "What's the plan for next year?"

    "I turn to the headmaster, feeling guilty for taking over the conversation he'd been having with the prince."
    "It's like I made him the third wheel when I was the last one to show up."

    show phillip excited
    #a "It was Apanaʻoha, right?"
    #TODO: Missing line / updated line
    vl alexis_vl_prefix 6
    a "It was Ekaska, right?"

    vl goude_vl_prefix 2
    h "That's right. It wasn't easy convincing the government to let in so many foreigners all at once, but the king was very accommodating."

    vl alexis_vl_prefix 7
    a "Well, no wonder they're excited! A year in paradise, and practically for free!"

    "Just like the Salon, another change that mainly went under the radar came to mind."
    "And it's one that would definitely be relevant to him."

    show phillip neutral
    vl alexis_vl_prefix 8
    a "Are you looking forward to the first Student Council elections in a few months?"
    voice sustain
    a "It must be exciting even for you, Headmaster. You graduated from MIA, didn't you?"

    vl goude_vl_prefix 3
    h "I did. The school was always supposed to be a microcosm of the empire. This is long overdue."
    voice sustain
    h "And here we are with the one who might be our first elected Student Council President."

    show phillip contemplative
    # TODO: Voice line repeated. Update once available
    vl phillip_vl_prefix 4
    p "I don't have any plans to run, so I doubt it. Things worked out, but I didn't do any of this hoping to get voted back on for next year."

    "Even if he didn't do it on purpose, it probably won't stop people from voting for him. If they're able to write his name in, anyway."
    "We order some drinks and snacks, passing the time with some idle conversation about how things have gone since the beginning of the new year."

    show phillip neutral
    vl alexis_vl_prefix 9
    a "What were you two talking about before I showed up?"

    show phillip tired
    vl phillip_vl_prefix 5
    p "We're getting ready for next month's Residency, and this one has kept us really busy."

    vl alexis_vl_prefix 10
    a "Where is it?"

    show phillip excited
    vl phillip_vl_prefix 6
    p "Ferenicia. And unlike the others, we're all heading to one place."

    "A bigger city, more students, his hometown. No doubt there are others from the capital, too, but he's like the resident expert."
    "No wonder he'd be running around making sure everyone else knows what to expect. That city is massive."

    vl goude_vl_prefix 4
    h "It only felt right to end the year off with a visit to the Jewel of the Empire. But it's also the largest city, which comes with its own unique challenges."

    show phillip contemplative
    vl alexis_vl_prefix 11
    a "You two are going to be run ragged the entire week, eh?"

    "The prince sighs."

    show phillip tired
    vl phillip_vl_prefix 7
    p "Probably, but it comes with the territory, I guess."

    "His phone vibrates. After checking it, he rises."

    show phillip neutral
    vl phillip_vl_prefix 8
    p "Speaking of, I've got to run. I have another meeting to get to."

    "The headmaster joins him."

    vl goude_vl_prefix 5
    h "As do I. The empress and prime minister are expecting me in the capital for lunch in a few hours and there are preparations to be made."

    show phillip excited
    vl alexis_vl_prefix 12
    a "Good luck with it all. Sounds like you two are going to need it."

    if eval(a.name)[0] == "Alexis":
        vl phillip_vl_prefix 9A
        p "You can say that again. See you around, [a]."
    else:
        # TODO: Repeated voice line. Update once available
        vl phillip_vl_prefix 9B
        p "You can say that again. See you around, Blakesley."

    "At the head of the stairs, the prince gives me a small wave before following the headmaster down."
    "Even if he does step away from the Council this year, I have a feeling the rest of the Spec Ops are going to be in good hands for the next few years."
    
    hide phillip with dissolve
    
    #jump to main club route elvera
    $ renpy.call(chosen_club + "_route_elvera", "Elvera", 12)
    #jump route_branch_point5

label route_branch_point5:
    if chosen_club == "no_clubs":
        jump no_clubs_route_elvera
    elif chosen_club == "disciplinary":
        jump disciplinary_route_elvera
    elif chosen_club == "literature":
        jump literature_route_elvera
    elif chosen_club == "anime":
        jump anime_route_elvera
    elif chosen_club == "home_ec":
        jump home_ec_route_elvera
    else:
        jump archery_route_elvera

label phillip_overa(month, date):
    $ phillip_vl_prefix = "audio/voices/Supporting-Extra/Phillip/Own Route/Epilogue/Phillip_Epilogue_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Phillip/Epilogue/" + player_voice_prefix + "_Phillip_Epilogue_"

    call screen calendar(month, date, "Overa", 19)
    scene bg mainstreet_afternoon with fade

    $ renpy.notify("Phillip - \nLenday, Overa 19th, 1028 RD")

    play music hatchling10
    "Graduation is right around the corner. Only a few more weeks, and then it's time to say goodbye."
    "To MIA, to Huntsdale, to everyone I've known over the past year."
    "I've been spending a lot of my free time wandering around the town to take in the sight one last time."
    "Today's no different. I come to the bus terminal, the place I first stepped foot in Huntsdale."
    "An odd feeling comes over me when I look at it. Some sort of gratitude? In a way, this past year could all be owed to this building, after all."
    "I scan the townscape, just as I did that first day."
    "The buildings I can see are all familiar sights to me now, and a few others that didn't stand out to me then do now."
    "Magis Hall's antiquated appearance doesn't shock me anymore. I'm going to miss the hominess of The Amity and my aimless wandering around the mall."
    "Someone catches my eye. A student, looking up at the street signs of an intersection. He looks lost. I saunter over to him."
    "Unlike the first time, I actually know my way around now."
    "Thinking back to that first time, a wave of melancholia crashes into me."
    "The prince never came back to school after the weird blackout at the end of last month."
    "The only person I know who might've heard anything is Sue, and she's been tight-lipped the entire time."
    "I shake my head. Someone needs my help, and I'm doing to do a piss poor job if I'm worrying about—"
    "The prince."
    "That's the prince standing at that sign. I sprint the rest of the way."

    vl alexis_vl_prefix 1
    a "Your Highness!"

    "When he turns to me, he smiles."

    show phillip excited eyepatch at center with dissolve
    if eval(a.name) == "Alexis":
        vl phillip_vl_prefix 1A
        p "Oh, [a]. How've you been?"
    else:
        vl phillip_vl_prefix 1B
        p "Oh, Blakesley. How've you been?"

    vl alexis_vl_prefix 2
    a "\"How've you been?\" That's what you have to say after being gone for so long?"

    "Well, at least he looks to be in good shape. Except for the eyepatch. What in the Abyss happened in Ferenicia?"

    vl alexis_vl_prefix 3
    a "Where have you been? What happened during your last Residency? And what're you doing back after so long?"

    show phillip neutral eyepatch at center with dissolve
    vl phillip_vl_prefix 2
    p "Let's see… \"How've you been?\" seems like a pretty standard thing to say when you haven't seen someone in a while."

    "He sighs."

    show phillip tired eyepatch
    vl phillip_vl_prefix 3
    p "I've been at home recovering. What happened last month is a… long story, suffice to say."
    voice sustain
    p "And I came back just to finish the year out. Only felt right, now that I'm better."

    "He laughs, no doubt at the flabbergasted look I must have on my face."

    show phillip excited eyepatch
    vl phillip_vl_prefix 4
    p "Now that I think about it, I missed the back half of the Student Council campaign. How's that looking?"

    vl ("<from 0.85>" + alexis_vl_prefix) 4
    a "We voted earlier this week. Results should be posted soon. Might've already happened."
    voice sustain
    a "The Presidency's the one people watched the closest. Reina's the frontrunner there."

    show phillip neutral eyepatch
    vl phillip_vl_prefix 5
    p "That doesn't surprise me. How about we walk and talk a bit?"

    scene bg bulletin_board_afternoon with fade

    "I do most of the talking, catching the prince up on what happened during the weeks he was gone."
    "He's the one leading the way as we talk, and I just follow him."
    "Before long, we're in front of Magis Hall. And surrounding a bulletin board I barely noticed before, there's a crowd gathering."
    "That must be what he was looking for. They got those ballots counted quickly."
    "It's not all that surprising that some younger students in the crowd are less shocked by the prince's reappearance."
    "They're the ones that have known him all year. Some of the people in the crowd probably received him whenever he returned."
    "At the sight of us, someone starts telling people to clear a path."
    "There's no real fanfare until older students like me that would've been out of the loop notice him. That's when the chatter starts."
    "We walk to the bulletin board, where the results of the school's first Student Council elections are posted."
    "In an ironic twist of fate Reginald Ultire, the same first year Spec Op Reina ousted, is filling her role as Disciplinary Committee Chair."
    "The Student Council President, to almost no one's surprise, is Reina herself."
    "The name \"Dreyar,\" the fact that she already had experience on the Council, and her pledge to support the Imperial Scholar Fund all gave her pretty significant boosts."

    show phillip contemplative eyepatch at center with dissolve
    vl phillip_vl_prefix 6
    p "You've got to be kidding me…"

    "Right below her name is that of her Vice President, the runner-up."
    "It does surprise a few people to see the prince's name there, since they no doubt would've expected him to be at the top of the list."

    show phillip tired eyepatch
    vl phillip_vl_prefix 7
    p "I didn't even campaign!"

    vl alexis_vl_prefix 5
    a "Well, not openly."

    show phillip contemplative eyepatch
    vl phillip_vl_prefix 8
    p "I—what?"

    vl alexis_vl_prefix 6
    a "I'll see you in a bit."

    hide phillip with dissolve
    "I take a step back to let his fellow first-years get in their congratulatory pats on the back. They would've been the group he got the most votes from, by far."
    "The news that he was almost single handedly bankrolling a world tour for everyone else would've made quite a few upperclassmen write him in, too."
    "It's true that he didn't campaign, so in that way, this did just make it a popularity contest, but this time around, the popularity was for all the right reasons."
    "A good fifteen minutes pass before he's finally freed and joins me outside of the cluster. He looks winded."

    show phillip tired eyepatch with dissolve
    
    vl alexis_vl_prefix 7
    a "You alright?"

    vl phillip_vl_prefix 9
    p "I'll live."

    "Even when he does catch his breath, he looks disheartened."

    show phillip contemplative eyepatch
    vl phillip_vl_prefix 10
    p "It's really starting to sink in that the year's over."

    vl alexis_vl_prefix 8
    a "Yeah."

    show phillip neutral eyepatch at center with dissolve
    # TODO: Repeated voice line. Update once available
    vl phillip_vl_prefix 11
    p "It's been pretty nice knowing you this year."

    vl alexis_vl_prefix 9
    a "I'm honored that you think so, Your Highness. It's been my pleasure. But it isn't like this has to be the end, right?"

    "He perks up at that."

    show phillip excited eyepatch
    vl phillip_vl_prefix 12
    p "No, I suppose not."

    "He sighs."

    show phillip tired eyepatch
    vl phillip_vl_prefix 13
    p "All of that excitement earlier might've been too much for me. I'm going to head back to House Sloane for some rest."

    vl alexis_vl_prefix 10
    a "Will you need any help getting back?"

    show phillip neutral eyepatch
    vl phillip_vl_prefix 14
    p "I'll be fine. Well… if this is the last time we see each other before graduation, good luck, [a]."

    vl alexis_vl_prefix 11
    a "Thank you. Same to you, Your Highness."

    "I look over to the crowd of students still crowding the bulletin board. So many of them have relied on him, and are going to next year, too."
    "He was already busy running around for the Spec Ops, and now he's going to have to do it for everyone."

    vl alexis_vl_prefix 12
    a "I think you're really going to need it."

    "We say goodbye, and he heads off. I look up at Magis Hall. Well, if I was going around one last time for nostalgia's sake, may as well take advantage of the fact that I'm here."
    "As I go inside, the prince and I with backs turned to each other, I remain hopeful. We're both heirs, but we're worlds apart."
    "Him, to an entire empire. Me, to a faltering viscounty."
    "Normally, we'd never have interacted during the school year, let alone talk about keeping in touch afterwards."
    "But there are ways to reach out. We may have said goodbye, but it was only for a little while."
    
    hide phillip with dissolve
    
    #jump to second club route overa
    # TODO: Modify condition after Said and Vince Overa dates are available
    $ renpy.call(chosen_club2 + "_route_overa", "Overa", 19)
    #jump route_branch_point6

label route_branch_point6:
    if chosen_club == "no_clubs":
        jump no_clubs_route_overa
    elif chosen_club == "disciplinary":
        jump disciplinary_route_overa
    elif chosen_club == "literature":
        jump literature_route_overa
    elif chosen_club == "anime":
        jump anime_route_overa
    elif chosen_club == "home_ec":
        jump home_ec_route_overa
    else:
        jump archery_route_overa