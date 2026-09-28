label student_council_dallinus(month, date):
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Student Council/Killian_StudentCouncilEvents_Month2_"
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Student Council/IAH Student Council/Month 2/Elio_IAHSC_Month2_"
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Student Council/Month 2/Reina_StudentCouncil_Month2_"
    $ sue_vl_prefix = "audio/voices/Love Interests/Sue/Student Council/SueDaengQan_IAHStudentCouncilDallinus/SueDaengQan_IAHStudentCouncilDallinus_"
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Student Council/Month 2/Naomi_SC_Month2_"
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Student Council/Lucas_SC_M2_"

    call screen calendar(month, date, "Dallinus", 28)
    scene bg wilson_salon_noon with fade

    $ renpy.notify("Student Council - \nZaeday, Dallinus 28th, 1027 RD")

    define left_pos = Position(xpos=0.2, ypos=1.0, xanchor=0.5, yanchor=1.0)
    define center_pos = Position(xpos=0.5, ypos=1.0, xanchor=0.5, yanchor=1.0)  
    define right_pos = Position(xpos=0.8, ypos=1.0, xanchor=0.5, yanchor=1.0)

    show sue neutral at center_pos with dissolve
    vl sue_vl_prefix 1.1
    s "Thank you, everyone, for joining us on the weekend."

    "What a week it's been. Most of the first-years—the Spec Ops and Civ Mages—were on something called a 'Residency' last week."
    "They were shipped all over the empire to get that 'real world experience' Sue mentioned on my first day."
    "Apparently, one of them pissed off someone in the military."
    "And when they got back, Reina had him court-martialed."
    
    show lucas neutral at left_pos with dissolve
    vl lucas_vl_prefix 1
    l "Let's just get this farce over with."

    "I learned a lot this week. The presidents of the school's clubs are honorary members of the Student Council."
    "And in instances like this, it's up to them to pass judgement on rulebreakers."
    "But only when said rulebreaker is also on the Council, like Reginald is."
    "The salon on the third floor of the Wilson Building is usually reserved for the nobles and club presidents."
    "Since just about everyone meeting today is in one of those groups, Sue had the whole place reserved so we could vote on the poor kid's fate."

    show naomi neutral at right_pos with dissolve
    vl naomi_vl_prefix 1
    n "It's just a simple majority vote?"
    
    hide lucas with dissolve
    show reina neutral at left_pos with dissolve
    vl reina_vl_prefix 1
    r "That's correct. But first, let's briefly review the facts of the case."
    
    "Reginald Ultire, a first-year Lychester, was stationed in the southwestern Magiana."
    "A drunk sailor on shore leave was harassing people. At first, Ultire tried telling him off, but it came to blows."
    "If you could call what happened a fight. The sailor was fished out of the city's harbor coughing and cursing with a stone weight Ultire had conjured stuck to his foot."
    "He was lucky enough to avoid trouble with the law, between him helping someone out, the school vouching for him, and family connections. But that wouldn't protect him here."

    hide naomi with dissolve
    show killian happy at right_pos with dissolve
    vl killian_vl_prefix 1.2
    k "They saved innocent bystanders from some crazed villain. They should be applauded if anything."

    hide killian with dissolve
    show elio happy at right_pos with dissolve
    vl elio_vl_prefix 1
    e "I'm with you there."
   
    hide elio with dissolve
    show lucas neutral at right_pos with dissolve
    vl lucas_vl_prefix 2
    l "You can disagree with his methods but not the principle of what he did. And isn't that what we should be debating?"
   
    hide lucas with dissolve
    show naomi thinking at right_pos with dissolve

    vl naomi_vl_prefix 2
    n "I agree with Lucas. Reginald did a good thing."

    show naomi thinking with dissolve
    "Naomi sighs."

    vl naomi_vl_prefix 3
    n "But it's nowhere near as simple as that, is it?"

    vl sue_vl_prefix 2.2
    s "Unfortunately, how we feel about what he did doesn't matter here."
    
    "Sue picks up a small book and opens it."
    
    vl sue_vl_prefix 3.1
    s "\"All students at Magiana Imperial Academy are to be treated as if they are cadets of the Magianan Imperial Army, are intended to carry themselves as such, and are subject to all rules and regulations of active soldiers.\""

    vl reina_vl_prefix 2
    r "The Code of Conduct is quite clear on that matter. Would an officer in the Imperial Armed Forces let one of their subordinates off after such an incident because they 'agreed with the principle'?"

    hide naomi with dissolve
    show elio confused at right_pos with dissolve
    vl elio_vl_prefix 2
    e "The rules are centuries old."

    hide elio with dissolve
    show killian angry at right_pos with dissolve
    vl killian_vl_prefix 2.1
    k "And last I checked, we're not his commanding officers."

    hide killian with dissolve
    show lucas neutral at right_pos with dissolve
    vl lucas_vl_prefix 3
    l "Time for the vote, yes?"
    
    "Lucas throws his hand up."
    
    vl lucas_vl_prefix 4
    l "Everyone in favor of acquittal—"

    show reina happy at left_pos
    "Reina smirks. At that, Sue frowns. And I have a bad feeling about what she's going to say next."

    show reina neutral at left_pos
    vl reina_vl_prefix 3
    r "In case some of us need a reminder, we serve at the pleasure of the headmaster. It's his duty to uphold the school's rules just as much as ours."

    hide lucas with dissolve
    show naomi thinking at right_pos with dissolve
    vl naomi_vl_prefix 4
    n "And if we don't, what's happening right now happens to us, too, right?"

    show sue melancholic at center_pos
    vl sue_vl_prefix 4.2
    s "No, actually. The headmaster has the right to just remove us in that case."

    hide naomi with dissolve
    hide sue with dissolve
    show lucas neutral at right_pos with dissolve
    show lucas neutral at center_pos with move
    show lucas neutral at center_pos with hpunch
    
    "Lucas shoots up from his seat, slamming his hands on the table."
    
    vl lucas_vl_prefix 5
    l "That's ludicrous!"

    show lucas neutral at right_pos with move
    show sue melancholic at center_pos

    vl reina_vl_prefix 4
    r "They're the rules."

    "A number of people seated begin speaking to each other and shuffling in their seats, eyes darting around to see how others are reacting."
    "I'm standing at Sue's side, and I'm having some trouble keeping myself still, too."

    hide lucas with dissolve
    show killian angry at right_pos with dissolve
    vl killian_vl_prefix 3.1
    k "Like justice, democracy is blind... This shit wouldn't fly in Blue Meridian, dammit. Are we really just going to roll over and let evil win?"

    hide killian with dissolve
    show naomi thinking at right_pos with dissolve
    vl naomi_vl_prefix 5
    n "I think we might have to."

    hide naomi with dissolve
    show elio confused at right_pos with dissolve
    vl elio_vl_prefix 3
    e "Dammit."

    hide elio with dissolve
    show naomi thinking at right_pos with dissolve
    vl naomi_vl_prefix 6
    n "Reina?"

    vl reina_vl_prefix 5
    r "Yes?"

    vl naomi_vl_prefix 7
    n "Our only option is to convict, isn't it? And unanimously. Anyone who doesn't risks being replaced with someone who would. And you'd just do this all over again if the vote fails."

    show reina happy at left_pos
    vl reina_vl_prefix 6
    r "Very astute of you, Naomi. Of course, any of you are still free to. Just think about whether or not this is the hill you want to die on."

    show sue melancholic at center_pos with dissolve
    vl sue_vl_prefix 5.2
    "Sue clears her throat."
    voice sustain
    s "And with that out of the way. As Lucas was saying, everyone in favor of acquittal, please raise your hands."

    hide naomi with dissolve
    show lucas neutral at right_pos with dissolve
    show lucas neutral at right_pos with hpunch
    "Lucas, still standing, thrusts his hand into the air. No one else joins him. Sue nods."
    
    vl sue_vl_prefix 6.2
    s "And all in favor of conviction?"

    show lucas neutral at right_pos
    "Lucas takes his seat as the rest of those gathered all raise their hands, Sue included."
    "The only one that looks remotely happy about all of this is Reina."

    show sue neutral at center_pos
    vl sue_vl_prefix 7.1
    s "And that's it. From this day forward, Reginald Ultire is no longer a member of the Student Council of the Imperial Academy at Huntsdale."
    voice sustain
    s "This meeting is adjourned. You're all free to go."

    hide lucas with moveoutright
    "Lucas is the first to do so, not sparing the others so much as a glance as he does."
    
    hide sue with dissolve
    hide reina with dissolve
    "They follow at a more relaxed pace. I can't take my eyes off of Reina as she makes her exit."

    "So, this is what she was getting at when she told me off when we first met."
    "Don't like the rules? Go through the Council to change them. Don't just ignore them."
    "I have a feeling that the headmaster's ideas and the worries about funding are going to take a backseat at Student Council meetings for a while."

    scene black with fade
    call phillip_vanus("Dallinus", 28) from _call_phillip_vanus

label student_council_dyalt(month, date):
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Student Council/Killian_StudentCouncilEvents_Month4_"
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Student Council/IAH Student Council/Month 4/Elio_IAHSC_Month4_"
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Student Council/Month 4/Reina_Shared_StudentCouncil_Month4_"
    $ sue_vl_prefix = "audio/voices/Love Interests/Sue/Student Council/SueDaengQan_IAHStudentCouncilDyalt/SueDaengQan_IAHStudentCouncilDyalt_"
    $ phillip_vl_prefix = "audio/voices/Supporting-Extra/Phillip/SC/Month 4/Phillip_SC_Month4_"
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Student Council/Month 4/Naomi_SC_Month4_"
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Student Council/Lucas_SC_M4_"

    call screen calendar(month, date, "Dyalt", 31)
    scene bg student_councilroom_afternoon with fade

    $ renpy.notify("Student Council - \nIstday, Dyalt 31st, 1027 RD")
    
    define left_pos = Position(xpos=0.2, ypos=1.0, xanchor=0.5, yanchor=1.0)
    define center_pos = Position(xpos=0.5, ypos=1.0, xanchor=0.5, yanchor=1.0)  
    define right_pos = Position(xpos=0.8, ypos=1.0, xanchor=0.5, yanchor=1.0)

    show lucas annoyed at center_pos
    vl lucas_vl_prefix 1
    l "You've got to be kidding me."

    "I look over a veritable sea of raised hands from my place beside Sue's desk."
    "The Council just voted on a very important issue today: revised versions of the school's dress code and code of conduct."
    "The vote to approve them as the official rules of the school was unanimous. Including Reina, who had a little smile on her face, her arm bent at a perfect ninety degree angle."
    "Her raised hand wasn't as prominent as the ones people shot into the air in their enthusiasm, but still striking in its discretion."

    vl lucas_vl_prefix 2
    l "You were the one—"

    show reina neutral at right_pos
    vl reina_vl_prefix 1
    r "Who enforced the rules as they were written. The people have made their will known, and now I vote in accordance with it. I thought you'd approve, Mr. Aragon."

    "There are a few laughs mixed into the chorus of voices approving what she said."

    hide lucas with dissolve
    show elio annoyed at left_pos
    vl elio_vl_prefix 1
    e "She played us."

    hide elio with dissolve
    show killian sad at left_pos
    vl killian_vl_prefix 1.2
    k "I'm not mad, I'm disappointed. In myself, mostly."

    "A few strikes of Sue's gavel silences the room and draws attention to her."

    hide killian with dissolve
    show sue neutral at center_pos
    vl sue_vl_prefix 1.1
    s "And by unanimous vote, the Student Council has approved a revised version of the dress code and student code of conduct for the Imperial Academy at Huntsdale."

    "There are cheers, and she gives everyone a minute to get it out of their systems and settle down."

    vl sue_vl_prefix 2.1
    s "I'll inform the headmaster, and he'll work with the school's partners to produce and distribute the 1027 versions of them both to the student body. Good work, everyone."

    "Another round of applause. In the middle of the ovation, the prince stands. That got some people to stop, but not everyone. He begins to speak anyway."

    show phillip neutral at left_pos
    vl phillip_vl_prefix 1
    p "I'd like to echo Sue's congratulations. This is a good day for our peers. But our work is just beginning."

    "The applause peters out."

    vl phillip_vl_prefix 2
    p "The dress code and code of conduct aren't the only outdated documents our school is ruled by. Let's not forget that the charter is just as old. Heck, it's the oldest of them."

    show reina confused at right_pos
    vl reina_vl_prefix 2
    r "And what are you suggesting, exactly?"

    vl phillip_vl_prefix 3
    p "The school doesn't have the same mission now as it did when it was founded."
    vl phillip_vl_prefix 4
    p "We just did away with a code of conduct that said we were military cadets. A dress code that said the girls couldn't wear their hair short or the boys wear their hair long."
    voice sustain
    p "Why shouldn't we do the same with the school's mission statement?"

    hide reina with dissolve
    show naomi neutral at right_pos
    vl naomi_vl_prefix 1
    n "I think I know what you're doing."

    "Up until this point, Naomi's been silent. All eyes turn to her when she speaks."

    vl naomi_vl_prefix 2
    n "You're right about the charter being old and in need of a rewrite, too. But the school's \"new mission\" is inseparable from the sectors, isn't it?"

    vl phillip_vl_prefix 5
    p "That's what I believe, yes."

    a "Well, it was only a matter of time until we got back on this. But do we have to do it now, though?"

    vl phillip_vl_prefix 6
    p "There's no better time than the present."

    vl sue_vl_prefix 3.2
    s "No better time than when everyone's in a reformation fever, you mean."

    "The prince's and Naomi's back and forth got a few comments out of people, but Sue's words silence them all."
    "It's the closest thing to a partisan statement she's said all year, and it could easily be painted as a direct rebuke of the Sectorist leader."

    "But the prince seems unbothered."

    vl phillip_vl_prefix 7
    p "Well, that's just what momentum is, isn't it?"

    vl sue_vl_prefix 4.2
    s "Well played. But not today."

    "Someone in the crowd gasps."

    vl sue_vl_prefix 5.2
    s "We came here to vote on the dress code and code of conduct. We've done that. And some of you look like you're itching for a fight."
    voice sustain
    s "So let's save the tongue lashing until our next meeting, shall we? Oh, and one more thing…"

    "Sue rises from her seat."

    vl sue_vl_prefix 6.2
    s "Don't read too much into my statements today. I delay the debate in the interest of time, and so cooler heads can prevail."

    "She looks right at the prince."

    vl sue_vl_prefix 7.1
    s "I meant no offense with my challenges, Prince Phillip."

    vl phillip_vl_prefix 8
    p "None taken."

    "And just as soon as she'd delivered the Anti-Sectorists some sort of victory, she'd taken it away from them."
    "Based on the whispers, though, it wasn't going to stop people from saying she was just playing damage control."

    vl sue_vl_prefix 8.1
    s "You're all dismissed. Enjoy the rest of your day."

    hide phillip with dissolve
    hide naomi with dissolve
    hide sue with dissolve
    "Once the room is cleared, Sue falls back into her seat."

    show sue neutral at center_pos with dissolve
    vl sue_vl_prefix 9.2
    s "How exhausting. Coffee, please?"

    "I get to work doing what's turned out to be one of my main jobs."

    a "Barely halfway through the year, too."

    vl sue_vl_prefix 10.2
    s "Ugh… Don't remind me."

    "After giving Sue her coffee, I take a seat with a cup of my own. Then it hits me. We are only halfway through the school year. But surely we won't be stuck on this for the next five months."
    
    call phillip_neralt("Dyalt", 31) from _call_phillip_neralt

label student_council_exalt(month, date):
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Student Council/Month 6/Reina_Shared_StudentCouncil_Month6_"
    $ sue_vl_prefix = "audio/voices/Love Interests/Sue/Student Council/SueDaengQan_IAHStudentCouncilExalt/SueDaengQan_IAHStudentCouncilExalt_"
    $ heckler1_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Heckler 1/Heckler1_SC_Month6_Exal_"
    $ heckler2_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Heckler 2/Heckler2_SC_Month6_Exal_"
    $ phillip_vl_prefix = "audio/voices/Supporting-Extra/Phillip/SC/Month 6/Phillip_SC_Month6_"
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Student Council/Month 6/Naomi_SC_Month6_"

    call screen calendar(month, date, "Exalt", 20)
    scene bg student_councilroom_afternoon with fade

    $ renpy.notify("Student Council - \nNyday, Exalt 20th, 1027 RD")

    define left_pos = Position(xpos=0.2, ypos=1.0, xanchor=0.5, yanchor=1.0)
    define center_pos = Position(xpos=0.5, ypos=1.0, xanchor=0.5, yanchor=1.0)  
    define right_pos = Position(xpos=0.8, ypos=1.0, xanchor=0.5, yanchor=1.0)

    "I don't know the last time I've seen the Student Council room so lively. Actually, has it ever been this lively?"
    "People are so fired up it's hard to hear myself think. Not like I can blame them."
    "Today's one of the biggest days we've had, if not the biggest day."
    "The year's ending soon, most of us are looking forward toheading home for the Week of Life, we're voting on a rewritten charter that's already failed to pass, and, of course, the question of the sectors and study abroad are at the forefront."
    "The new charter specifically states that they're valuable educational opportunities the students should be entitled to. Each time the margin's been razor thin, but them being there is obviously the reason it's failed the other votes it needs."
    "So, will today finally end the deadlock, or are we going to have to pick this up again in the new year?"
    "Sue bangs her gavel, bringing the room to order. Even she seems tired of this."

    show sue neutral at center_pos with dissolve
    vl sue_vl_prefix 1.1
    s "Is everyone ready for our next vote on the proposed charter?"

    show naomi neutral at left_pos with dissolve
    show phillip neutral at right_pos with dissolve
    "The prince shifts in his seat, but Naomi speaks first."

    vl naomi_vl_prefix 1
    n "May I say something?"

    vl sue_vl_prefix 2.2
    s "Of course."

    "She stands and turns towards the prince, bowing slightly."

    vl naomi_vl_prefix 2
    n "I mean no offense, Your Highness, but do you really think this is going to work?"
    voice sustain
    n "You refuse to divorce the headmaster's initiatives from the school's new mission, even when it's clear they'll earn the charter the votes it needs to pass."

    vl phillip_vl_prefix 1
    p "Because they're that important to what MIA's trying to accomplish."

    "He stands as well. Neither of them are threatening, and there's a good amount of distance between the two, but it's impossible not to notice the height the prince has on Naomi."

    vl phillip_vl_prefix 2
    p "In the name of making its students well-learned, well-trained, worldly citizens of not just the empire, but the world, money is no object."

    "The comment makes me wince. Judging by the shouts that break out, others find it in as poor taste as I did. It's a bit hard to hear, but not all of them are in disagreement."
    "Just most of them."

    vl heckler1_vl_prefix 1
    h1 "Yeah, of course you'd say that!"

    vl heckler2_vl_prefix 1
    h2 "Just cause one of you Magises founded the school doesn't mean you get to run the place!"

    "Sue again bangs her gavel, more forcefully this time, to quiet everyone down."

    vl sue_vl_prefix 3.3
    s "Naomi and the prince have the floor. Let them speak. Naomi."

    vl naomi_vl_prefix 3
    n "Thank you. My Prince, I don't disagree that people could learn a lot. I don't think anyone does. But money is very much an object."

    "In lieu of shouting again, several people on the Council begin snapping."

    show naomi thinking at left_pos
    vl naomi_vl_prefix 4
    n "What clubs will have to suffer because their funding was drained to send students on Residencies?"
    voice sustain
    n "What events will we have to cancel because hundreds of airship tickets were purchased instead?"

    "Naomi pauses for a moment, bowing her head and taking a breath. When she again meets the prince's eyes, there's a renewed determination behind her gaze."

    vl naomi_vl_prefix 5
    n "Would you really say \"money is no object\" to the common families relying on financial aid to send their students to this school?"
    voice sustain
    n "The thought of my father receiving a bill that he can't afford breaks my heart. Haven't you heard us all this time?"

    "The prince is smiling. I expect people to shout at him for that too, but they just wait. Instead their disapproval comes in the form of contemptuous glares."

    vl phillip_vl_prefix 3
    p "Loud and clear, in fact. You're right; I never could understand what the working families of this school would go through if the costs fell to them."
    voice sustain
    p "I've never had to worry about money a day in my life."

    show naomi neutral at left_pos
    vl naomi_vl_prefix 6
    n "That's in poor taste."

    vl phillip_vl_prefix 4
    p "But it's true. I have more money than I know what to do with."

    "At this point, he's beaming, like he's thought up a great joke he can't wait to tell. He'd better tell it soon before he gets chased out of the room."

    vl phillip_vl_prefix 5
    p "So, why not use it to put all of this funding talk to bed?"

    show naomi surprised at left_pos with hpunch
    vl naomi_vl_prefix 7
    n "You— what?"

    "A few perplexed murmurs break out, echoing Naomi's confusion. The prince spreads his arms, finally ready to let us all in on the joke."

    show phillip happy at right_pos with dissolve
    vl phillip_vl_prefix 6
    p "I've spoken to my mother and other senior officials at The Crown. With their help, I'm setting up the Imperial Scholar Fund."
    voice sustain
    p "The money that's been set aside for me since the day I was born has already been transferred into it."
    vl phillip_vl_prefix 7
    p "Its sole purpose is to fund the sectors and, when they happen, study abroad trips."
    voice sustain
    p "No diverting funds from other parts of the school's budget. And no extra bills for families."

    "The room's stunned into silence. For several agonizing seconds, no one says a word. Then Reina chuckles."

    hide naomi with dissolve
    show reina neutral at left_pos with dissolve
    vl reina_vl_prefix 1
    r "I do suppose that's one solution to the problem."

    "She raises a hand."

    vl reina_vl_prefix 2
    r "I'll speak to my father. I'm sure he'll be interested in donating as well. The question is whether he'll match or exceed the prince's contribution."

    "Again, the room falls silent. Eventually, Naomi speaks, putting words to the thoughts no doubt tumbling around everyone's heads."

    hide reina with dissolve
    show naomi surprised at left_pos with dissolve
    show naomi surprised at left_pos with hpunch

    vl naomi_vl_prefix 8
    n "You're just… paying for it all yourself?"

    "The prince laughs."

    vl phillip_vl_prefix 8
    p "If you knew how much money I was sitting on, you'd agree that someone my age will never need that much."
    voice sustain
    p "This is a much better use of it. Besides, I'll earn it back eventually."

    show reina neutral at left_pos with dissolve
    hide naomi with dissolve
    vl reina_vl_prefix 3
    r "Just to put it back into the fund, I'm sure."

    hide reina with dissolve
    show naomi neutral at left_pos with dissolve
    vl naomi_vl_prefix 9
    n "That is… very gracious of you both."

    vl sue_vl_prefix 4.2
    s "If there are no other comments, are we ready to proceed to the vote?"

    "The prince and Naomi take their seats, and Sue formally calls the vote."
    "It isn't unanimous, but with two of the richest people at the school putting the biggest sticking point to bed, it earns more than enough votes to pass."
    "And with that, the Sectors are enshrined as part of the mission statement of the Imperial Academy at Huntsdale, as well as the occasional year spent abroad."
    "Silence falls again as people digest what's just occurred."
    "Reina rises from her seat."

    show reina neutral at left_pos with dissolve
    hide naomi with dissolve
    vl reina_vl_prefix 4
    r "I think now would be a good time for the Sectorists to spread the good news."
    voice sustain
    r "And to the upperclassmen, I'm sure you can have fun theorizing with friends about where we'll be going next year."

    "She leaves, a gaggle of people following her, clogging the doorway in their rush to leave. More than a few Sectorists congratulate the prince and thank him on their way out."
    "Before long, the only ones remaining are myself, Sue, Naomi, and the prince."

    hide reina with dissolve
    show naomi embarrassed at left_pos with dissolve

    vl naomi_vl_prefix 10
    n "I'm sorry if I was disrespectful."

    show phillip neutral at right_pos with dissolve
    vl phillip_vl_prefix 9
    p "You were right to be worried and demand something of me. No offense taken."

    a "But to bankroll the whole thing yourself? Do I even want to know how many zeroes that means?"

    vl sue_vl_prefix 5.1
    s "It's probably better that you don't. Well, you three, why not go out and join the celebrations?"
    voice sustain
    s "It seems like a good way to close out the year."

    "Sue locks the door behind us when we leave."
    "With that, the duties of the Student Council have concluded for the year, and all there was to do was wait and see what the next would have in store for us."
    
    # TODO: Change this verification once dates for Said and Vince are available
    if chosen_club2 == "swordplay" or chosen_club2 == "music":
        $ renpy.call (chosen_club2 + "_route_exalt", "Exalt", 20)
    elif chosen_club2 == "enseki" or chosen_club2 == "art":
        $ renpy.call (chosen_club2 + "_route_exalt", "Exalt", 20)
    else:
        $ renpy.call(chosen_club + "_route_exalt", "Exalt", 20)
    #jump route_branch_point4

label student_council_verabris(month, date):
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Student Council/Killian_StudentCouncilEvents_Month8_"
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Student Council/IAH Student Council/Month 8/Elio_IAHSC_Month8_"
    $ sue_vl_prefix = "audio/voices/Love Interests/Sue/Student Council/SueDaengQan_IAHStudentCouncilVerabris/SueDaengQan_IAHStudentCouncilVerabris_"
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Student Council/Month 8/Naomi_SC_Month8_"

    call screen calendar(month, date, "Verabris", 27)
    scene bg student_councilroom_afternoon with fade

    $ renpy.notify("Student Council - \nToleday, Verabris 27th, 1028 RD")

    define left_pos = Position(xpos=0.2, ypos=1.0, xanchor=0.5, yanchor=1.0)
    define center_pos = Position(xpos=0.5, ypos=1.0, xanchor=0.5, yanchor=1.0)  
    define right_pos = Position(xpos=0.8, ypos=1.0, xanchor=0.5, yanchor=1.0)

    "Today isn't a day that the Student Council would normally meet, but quite a few people have gathered in its meeting room."
    "There's nothing on the agenda today. Right now, people are just chatting with their friends."

    show killian angry at left_pos
    show sue neutral at center_pos
    show elio neutral at right_pos
    vl killian_vl_prefix 1.1
    k "Where in the Abyss is Lucas? Nose too deep in a book to check his phone or something?"

    vl elio_vl_prefix 1
    e "…It's not just him."

    "The first-years are back from Ferenicia. Two of them that were on the Council have been missing ever since."
    "And one of them was the prince."

    hide elio with dissolve
    show naomi neutral at right_pos

    vl naomi_vl_prefix 1
    n "Don't you know anything, Sue? About that weird blackout last weekend…"

    "She crosses her arms and frowns."

    vl sue_vl_prefix 1.1
    s "Even if I did, I wouldn't be at liberty to say."

    vl killian_vl_prefix 2.3
    k "Keeping us in the dark. Great."

    "It was only for a few hours, but most power went out late last weekend in Ferenicia and its surrounding areas."
    "The only things that worked were magitech because those weren't connected to the power grid."
    "So far, the government's just said \"civil unrest,\" whatever that means."
    "Online, people in the capital are even saying that they didn't see anything like a protest or riot, so the \"unrest\" is news to them as much as it is to us."
    "It happening during a Residency and a pair of Spec Ops not coming back to campus afterwards have to be connected."
    "But we're not getting any answers."

    vl sue_vl_prefix 2.2
    s "Things will be revealed in time, I'm sure. Everything is under control, and that's what matters, right?"

    "It looks like even Sue doesn't fully buy what she just said."
    "This sure has gotten awkward. There has to be some way I can change the subject to make it less… depressing."
    "What comes to me feels only marginally better."

    a "So, graduation's next month."

    hide naomi with dissolve
    show elio neutral at right_pos
    vl elio_vl_prefix 2
    e "Thanks for the reminder."

    a "What's the plan afterwards? You guys got anything lined up?"
    
    show killian neutral at left_pos
    vl sue_vl_prefix 3.2
    s "Thankfully, I've got a job lined up in Goengyi. So I'll be hopping on an airship a few days after we walk."

    hide elio with dissolve
    show naomi neutral at right_pos
    vl naomi_vl_prefix 2
    n "I'd like to open a little cafe by the sea somewhere. But if it's here or back home in Estary, I don't know yet."

    hide naomi with dissolve
    show elio neutral at right_pos
    vl elio_vl_prefix 3
    e "Probably join a Guild. The military is the other option and yeah, no."

    hide elio with dissolve
    show killian neutral at center_pos
    hide killian with dissolve
    show killian neutral at right_pos
    vl killian_vl_prefix 3.2
    k "If I can get my way, go for a Master's somewhere, maybe?"

    hide killian with dissolve
    show naomi neutral at right_pos
    
    if eval(a.name)[0] == "Alexis":
        vl naomi_vl_prefix 3A
    else:
        vl naomi_vl_prefix 3B
    n "How about you, [a]? Do you know what you want to do?"

    a "What do I want to do?"

    "Yeah, I've put at least a little bit of thought into this over the course of the year."

    #jump route_branch_point_mid

# Changed
#label route_branch_point_mid:
    if chosen_club == "no_clubs":
        a "Going home for now. Shouldn't be terrible to find a job thanks to some family connections and a degree from a place like this."
        a "Maybe see if some Prospera noble needs a new secretary."
        #jump student_council_verabis_cont
    elif chosen_club == "disciplany":
        a "Take some time to myself. I could definitely use a break. See if the family and I can take a vacation."
        a "Then… probably a Master's in public policy or something."
        #jump student_council_verabis_cont
    elif chosen_club == "literature":
        a "Hit the road, if I can. I've learned a lot this year, but there's still plenty I have to sort out about what I want to do with myself."
        #jump student_council_verabis_cont
    elif chosen_club == "anime":
        a "I can probably find an office job back home without much difficulty. At least, I hope so. But I think I'll be fine. It isn't like I'm going at it alone."
        #jump student_council_verabis_cont
    elif chosen_club == "home_ec":
        a "Maybe a librarian? Giving people a place to hang out and, hopefully, a home away from home sounds like it would be nice."
        #jump student_council_verabis_cont
    elif chosen_club == "archery":
        a "Well, I want to go for a Master's degree. I just don't know what or where yet."
        #jump student_council_verabis_cont
    else:
        #TODO: Add dialogue variant for Scouts route
        pass
    
    jump student_council_verabris_cont
    
label student_council_verabris_cont:
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Student Council/Month 8/Reina_Shared_StudentCouncil_Month8_"
    $ goude_vl_prefix = "audio/voices/Supporting-Extra/Isaiah/SC/Isaiah_SC_Month8_"
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Student Council/Month 8/Naomi_SC_Month8_"

    scene bg student_councilroom_afternoon with fade
    
    define left_pos = Position(xpos=0.2, ypos=1.0, xanchor=0.5, yanchor=1.0)
    define center_pos = Position(xpos=0.5, ypos=1.0, xanchor=0.5, yanchor=1.0)  
    define right_pos = Position(xpos=0.8, ypos=1.0, xanchor=0.5, yanchor=1.0)
    
    "The intercom in the room crackles to life and we all snap to attention."

    show naomi happy at center_pos with hpunch
    vl naomi_vl_prefix 4
    n "They're finally starting!"

    hide naomi with dissolve
    "The only reason we all gathered here on an off day."

    vl goude_vl_prefix 1
    h "Good afternoon, everyone. I would like to present to you today your first ever candidates for the Student Council of the Imperial Academy at Huntsdale for the 1027 - 1028 school year."

    "The speeches we hear sound like there's an even split between style and substance."
    "Some candidates for offices like treasurer or secretary actually sound like they have visions for where they'd like to take the school."

    "Then you have some like the first candidate for athletic club representative."
    "All they did was brag about their popularity and how many points they scored during their games."

    "But I guess we'll see if competence or clout matters more when the ballots are cast next month."

    "Towards the end, the candidate I was waiting for comes on."

    show reina neutral at center_pos with dissolve
    vl reina_vl_prefix 1
    r "Good afternoon, everyone. This is Reina Dreyar, candidate for Student Council President, and I'm honored to have this moment to speak with you."

    "Most of the buzz in the room goes silent. Reina's one of few sitting members on the Council that put their name forward."

    "Between that familiarity, her notoriety from earlier in the year, and her throwing her support behind all of the year's reforms when it came time to vote, she's definitely been one to keep an eye on."

    vl reina_vl_prefix 2
    r "In my fourth and final year, I would look towards the future."
    voice sustain
    r "To lift up the ones who will come after me and prepare them so that they may succeed when I am gone."

    vl reina_vl_prefix 3
    r "The next few years for us students will no doubt be turbulent, and a steady hand will be essential to guide us through it."

    "From where she sits, I glimpse Sue nodding out of the corner of my eye."

    vl reina_vl_prefix 4
    #r "Next year, we will not be here at home, but enjoying the island paradise of Apanaʻoha."
    r "Next year, we will not be here at home, but enjoying the hot springs paradise of Ekaska. No doubt, there will be some culture shock."
    #voice sustain
    #r "No doubt, there will be some culture shock."

    vl reina_vl_prefix 5
    r "I have been blessed with the privilege to visit a number of nations around the world."
    voice sustain
    r "My upbringing also required extensive lessons into the intricacies of interpersonal communication."

    vl reina_vl_prefix 6
    r "On the world stage, as we will be next year, I believe you all deserve a president who shan't embarrass you."
    voice sustain
    r "Rather, one whose poise will garner praise and admiration that cascade down to you all, endearing you to our Ekaskan peers by association."

    "She pauses for a moment, probably to take a drink."

    vl reina_vl_prefix 7
    r "There is also the matter of the new Sectors."
    voice sustain
    r "Even if I weren't presently a third-year, I believe I would be a General Education student."

    vl reina_vl_prefix 8
    r "I admit that lack of personal experience limits what I could do for Special Operations and Civic Magic students."
    voice sustain
    r "So I swear to you that I would work readily with and defer to those within the Sectors so that I may better serve them and their fellows."

    vl reina_vl_prefix 9
    r "I wish to be a guiding hand for those who come after me and to help lay the foundation for I.A.H's bright future. Thank you."
    hide reina with dissolve

    "When she ends, the room breaks out into applause. I glance around at the others around me. Will the fourth years be casting votes next month?"
    "Try to leave their mark on the school by trying to influence who makes up its next generation of leaders?"

    "I'm still on the fence myself. While I might not know if I'll roll up on election day, I do know who's won my vote for Student Council President."
    call phillip_overa("Verabris", 27) from _call_phillip_overa