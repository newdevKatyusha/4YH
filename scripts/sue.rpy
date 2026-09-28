label no_clubs_route_jinus(month, date):
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Sue/Reina_Sue_Month1_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Sue/Month 1/" + player_voice_prefix + "_Sue_Month1_"

    call screen calendar(month, date, "Jinus", 19)
    scene bg student_councilroom_afternoon with fade

    $ renpy.notify("Sue\nZynday, Jinus 19th, 1027 RD")

    "I wasn't exactly sure what it would mean to be Sue's aide. Apparently, it makes me her gopher."
    "She has me running all over the Wilson Building, and sometimes the entire town, doing things for her."
    "At least it helps me to get my steps in."

    "The first few weeks of the school year go by like this."
    "I'm starting to get used to it, and return from one of my errands, when I see Sue at her desk, surrounded by documents."
    "She usually is, but the pile looks larger than normal."

    show reina neutral at right with dissolve
    "Reina sits in the corner at her desk, acknowledging my existence with a nod."

    vl alexis_vl_prefix 1
    a "What's that?"

    show sue neutral at center with dissolve
    "She barely spares me a glance before going back to work."
    s "Budget proposals for clubs that the treasurer put together."
    s "I have to go through them, approving them or requesting adjustments."

    vl alexis_vl_prefix 2
    a "For every club?"

    show sue neutral
    s "For everything their presidents say they'd like to do this year, too."
    "That sounds like a lot of numbers. And she's already been in school all day."
    "How long is she going to be stuck here mulling over these things?"

    vl alexis_vl_prefix 3
    a "Want some help?"

    show sue neutral
    s "Thank you, but I'll be alright."

    vl alexis_vl_prefix 4
    a "Are you sure? That's a lot of paper."

    show sue happy
    s "It's nothing I'm not used to."

    vl alexis_vl_prefix 5
    a "But that doesn't mean help won't make it go by more quickly."
    
    "No response to that. I smile to myself. So she sees the sense in that part, at least."

    vl alexis_vl_prefix 6
    a "Besides, I'm actually pretty decent with numbers."
    voice sustain
    a "Math is one of my better subjects. Even took an accounting class my second year of tertiary school."

    show sue neutral
    s "Of tertiary— Oh, I forgot you imperials do that."

    show reina happy
    vl reina_vl_prefix 1
    r "I'm afraid I can't say the same about Sue, so you'd be quite the help."

    show sue embarrassed with hpunch
    vl reina_vl_prefix Giggle
    "Sue clears her throat, and I can't help but smirk when Reina lets out a little laugh."

    show sue neutral
    s "I don't suppose it'll kill me to let you lend me a hand."
    s "Worst case scenario, I guess the treasurer scolds me and it's back to square one."
    s "At least for some of them. Just your opinion on them should be enough. Here, take these."

    "I was hoping for half of them. Instead I get a quarter. Oh well, it's a start."
    "The documents aren't too complicated. For each club, the events are listed, along with associated costs."
    "Or estimates of them, at least."

    "The treasurer's given them all a budget, based on how much the school's set aside for clubs in general."
    "And it's up to Sue to either approve or reject, based on if they're too close to, or even over, how much money they have."

    vl alexis_vl_prefix 7
    a "Gods. Anime Ironburke is how much?"

    show sue melancholic
    s "So Killian went and did it anyway. I told him Ferenicia V-Con would be cheaper since they wouldn't need hotels."

    show reina neutral
    vl reina_vl_prefix 2
    r "Or the airship tickets. But I suppose he is one for extravagance."
    hide reina with dissolve

    "It wasn't over budget, somehow, but it was cutting it really close."
    "So for a comment I just wrote, 'Don't bring the entire club or consider a local convention instead.'"

    "That was the most egregious of them. The Troaran Culture Club came in a very close second."
    "The president wants to bring them to a ski resort during the Week of Life at the end of the year."

    "At least all the athletic clubs requested was new equipment, some of them more than others."
    "The cultural club's expenses were all dwarfed by Killian's, so those were much easier to simply say 'Should be accepted' for."

    "When I was done, I set the stack I was given on Sue's desk. She stares at it."

    show sue neutral
    s "That was quick."

    vl alexis_vl_prefix 8
    a "It's like someone only gave me a fourth of the work."

    show sue happy
    s "Ha. I guess that is true."
    "She hands me another stack."

    show sue neutral
    s "There. The other half of your half. Satisfied?"

    vl alexis_vl_prefix 9
    a "Very."

    "We continue our work in relative silence, with little more than the ruffling of paper to keep us company."
    "Eventually, Reina packs up her things and leaves us."

    show sue happy at center with dissolve
    "Sue's done with her half slightly before I am with mine."
    "She gives my work a quick look-over, and then offers a satisfied nod."
    s "Good work."

    vl alexis_vl_prefix 10
    a "I try."

    show sue neutral
    s "It's... much earlier than I expected it to be when I finished."

    vl alexis_vl_prefix 11
    a "You're welcome."

    show sue neutral
    "Rising from her desk, Sue shoulders her bag."
    s "Thank you, [a]. Good work today. You're dismissed."

    vl alexis_vl_prefix 12
    a "Got it. Be seeing you."

    "We leave the Student Council Room, heading in opposite directions."
    "While I head for the elevator, I spy Sue heading for a staircase leading up to the third floor."
    "I wonder what's up there? I'll have to ask her about it sometime."

    scene black with fade
    
    # jump to phillip jinus
    call phillip_jinus("Jinus", 19) from _call_phillip_jinus_5
    #jump no_clubs_route_dallinus

label no_clubs_route_dallinus(month, date): 
    $ student1_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Student 1/Student1_Sue_Month2_"
    $ student2_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Student 2/Student2_Sue_Month2_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Sue/Month 2/" + player_voice_prefix + "_Sue_Month2_"

    call screen calendar(month, date, "Dallinus", 18)
    scene bg wilson_salon_afternoon with fade

    $ renpy.notify("Sue - \nToleday, Dallinus 18th, 1027 RD")

    "There's a salon on the Wilson Building's third floor. Not a hair salon."
    "Sue tells me the name comes from fancy gatherings high society people would have a few centuries back in Troara and Eforte."

    "Today, the Student Council isn't meeting, but she's dragged me along anyway. Just so we could go there."

    vl alexis_vl_prefix 1
    a "Why don't I ever hear about this place?"

    show sue neutral
    s "It's barred to anyone but nobility, club presidents, and their plus-ones."

    vl alexis_vl_prefix 2
    a "I'm a viscount's kid. I could've come up here whenever I wanted?"

    s "That's right."

    "Upon us cresting the stairs to the third floor, a server in finely pressed livery greets us and leads us to a table by a window overlooking Huntsdale."

    "We take a cursory glance at a menu they hand us, ordering drinks and some light snacks. With a bow, they leave us."

    show sue happy
    s "How are you enjoying MIA so far?"

    vl alexis_vl_prefix 3
    a "I can see why it's so renowned. It's one fancy-ass school. Wasn't Huntsdale built just to be its campus?"

    s "That's right. You can thank the Premier for that one."

    "I stare at her."

    show sue embarrassed
    s "Do you… not know who that is?"

    vl alexis_vl_prefix 4
    a "Is it bad that I don't?"

    s "No…"

    "So it is bad."

    show sue neutral
    s "Lucius Magis, the first emperor. He founded the school."

    "So just one of the most important guys in imperial history and I didn't know his nickname. Great."

    vl alexis_vl_prefix 5
    a "Hold on. The emperor founded the school?"

    s "Why else did you think Prince Phillip was here? A Magis not attending this school is basically unheard of."

    vl alexis_vl_prefix 6
    a "They're like the final boss of legacy admissions."

    "She chuckles at that."

    show sue happy
    s "I suppose they are."

    "Someone approaches our table."

    vl student1_vl_prefix 1
    s11 "President Daeng Qan, it's good to see you."

    "A bit formal, aren't we? And hold on a second… haven't I seen this person before?"

    show sue neutral
    s "Likewise. Did you need something?"

    vl student1_vl_prefix 2
    s11 "I was wondering if you'd heard about that new Goengyi restaurant that opened in the capital?"
    voice sustain
    s11 "I hear it's divine. Would you like to accompany me sometime? My treat, of course."

    s "That's very generous of you. I am with a guest, so I can't answer right now, but I'll consider it."

    "She gestures to me, and only then do they acknowledge my existence."

    vl student1_vl_prefix 3
    s11 "Oh, I'm sorry. Well, if you'll excuse me…"

    "They slink away, right before the things we ordered arrive. Just some tea and miniature lemon tarts."

    "There's something about what that person said that's bugging me."

    vl alexis_vl_prefix 7
    a "You have a bit of an accent."

    show sue happy
    s "Very observant of you. Well done."

    vl alexis_vl_prefix 8
    a "Guess that did sound pretty stupid. The thing is—"

    show sue neutral
    s "Yes, I am from Goengyi. And them inviting me to a restaurant serving Goengyi cuisine was very much on purpose."

    vl alexis_vl_prefix 9
    a "But why—"

    vl student2_vl_prefix 1
    s22 "Sue, hey!"

    "Son of a bitch."

    vl student2_vl_prefix 2
    s22 "Did you have any plans for Verabris break next year?"

    s "Not right now."

    vl student2_vl_prefix 3
    s22 "Great. Some friends and I were heading down to Platinum Bay for the week. Think you'd want to join?"

    s "Very tempting. Can I have some time to think it over? That is six months out, after all."

    vl student2_vl_prefix 4
    s22 "Yeah, sure. Just wanted you to know the offer was there."

    "They walk off. I don't think they even noticed that I was here."

    show sue happy
    s "Your turn."

    vl alexis_vl_prefix 10
    a "What?"

    show sue neutral
    s "You just found out I'm from Goengyi. How about you?"

    vl alexis_vl_prefix 11
    a "Nothing too fancy. Just Prospera."

    show sue happy
    s "I'd still call the Old Capital quite fancy. A place any history fan has to visit at least once. There's just so much of it!"

    vl alexis_vl_prefix 12
    a "And, unfortunately, a history fan I'm not."

    "I'm sure Sue wanted us to have a nice little after school snack together, but several more people interrupt us."
    "And just like the first two, they don't say so much as a word to me. After the umpteenth one leaves, I have to say it."

    vl alexis_vl_prefix 13
    a "I didn't know you were so popular."

    show sue neutral
    s "I'm not."

    vl alexis_vl_prefix 14
    a "With all of this attention you're getting?"

    "She smiles and leans across the table."

    show sue happy
    s "I'm not. Didn't you recognize a few of them?"

    vl alexis_vl_prefix 15
    a "Well, I thought I did."

    show sue neutral
    s "The first one was the president of the Troaran Culture Club."

    "Then it clicks. The greetings, the friendliness, the fact that most of them invited her to dinner or to spend break with their friends."

    vl alexis_vl_prefix 16
    a "They were trying to bribe you?"

    s "It comes with the territory."

    "She takes a sip of her tea and speaks from behind the cup."

    show sue embarrassed
    s "I hope you didn't mind me using you."

    vl alexis_vl_prefix 17
    a "Not at all."

    "If it gave her an excuse to cut those conversations short, she's not going to hear me complaining."
    "Sue pointing it out is the only way I was able to piece together what happened."
    "And that's after seeing all of them fail in real time. But she could smell them from a mile away and wasn't having any of it."
    "Abyss, she even let them walk off thinking they had a chance. I doubt I'd be able to pull off something like that."

    vl alexis_vl_prefix 18
    a "Didn't you want to say yes to some of them?"

    show sue melancholic
    s "Of course. But it's my job to serve everyone. Not just the ones that pay me. Speaking of, I have somewhere I need to be."

    "She rises."

    show sue neutral
    s "Take care. Enjoy the rest of the tarts for me."

    hide sue

    "I do. And with each one I shove in my mouth, I think about what I'd do if I were in her shoes."

    "I ask myself if I'd be able to turn down every offer I was given today, and be able to do that every time I come to the salon, and probably even outside of it. I'm not able to say that I would."

    "So the fact that Sue can? She says she isn't popular, but I think she just earned herself a fan."
    call student_council_dallinus("Dallinus", 18) from _call_student_council_dallinus_5

label no_clubs_route_vanus(month, date):
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Sue/Month 3/" + player_voice_prefix + "_Sue_Month3_"

    call screen calendar(month, date, "Vanus", 23)
    scene bg weaver_library_afternoon with fade

    $ renpy.notify("Sue - \nLenday, Vanus 23rd, 1027 RD")

    show sue neutral
    "Sue agreed to help me with a history assignment I was struggling with. She's my boss, so I'm grateful that she agreed to do something like this."

    "We're in the library, poring over books about recent imperial history." 

    "I'm reading through an account of the empire's involvement in a civil war Estary had over a hundred years ago when I see it."

    "If not for the involvement of the government of Goengyi, it's very likely the recently war-weary Otren and Estary would have clashed."

    "Historians still debate what would've happened if the Eastern Confederation and Magianan Empire went to blows over the far eastern nation."

    vl alexis_vl_prefix 1
    a "Sue?"

    s "Yes?"

    "It takes me a minute to gather myself."

    vl alexis_vl_prefix 2
    a "I didn't know much about Goengyi until recently. Really recently. Like, after the salon recently."

    "I expect her to be disappointed. But the look of scorn I was anticipating never comes."

    s "And you wouldn't be alone in that."

    vl alexis_vl_prefix 3
    a "I wouldn't be?"

    s "We're just a little city-state. Most people don't have much reason to think of us."

    vl alexis_vl_prefix 4
    #TODO: Update dialog
    #a "But what about Apanaʻoha and Allowlucia? I hear about those two."
    a "But what about Ekaska and Allowlucia? I hear about those two."

    show sue melancholic
    s "The maritime hub of Unios and the seat of the Nyrellan Church are both much more important than the \"armpit of Otren.\""

    "Vitriol I didn't know Sue was capable of bled into the final three words she spoke."

    "But her words bring to the forefront of my mind terribly vague memories I'd all but forgotten."
    "News bulletins or hushed conversations my parents had with friends about the \"Goengyi Problem."

    "It's part of the Eastern Confederation, but it's friendly with Estary, which is part of the Empire."
    "A bit too friendly, according to the other Confederate states."

    vl alexis_vl_prefix 5
    a "…And didn't religion have something to do with it?"

    show sue neutral at center with dissolve
    s "It did."

    vl alexis_vl_prefix 6
    a "Shit. Didn't know I said that out loud."

    s "You've at least heard about Spiritism?"

    vl alexis_vl_prefix 7
    a "I'm not super religious, but it's some type of Nyrellan thing, right?"

    s "A denomination of it, yes. It's the lovechild of Nyrellanism and the animism Estary's people practiced for centuries before the empire got involved in their affairs."

    s "It only came about to calm people down when they worried the Nyrellan Empire would trample all over their traditions."

    "I think back to the passage from my book."

    vl alexis_vl_prefix 8
    a "And Goengyi gave it a try as a show of goodwill?"

    s "Exactly. Even though the Narrow Sea separates Estary and mainland Voles, the rest of the Confederation got nervous."
    s "And when it came to the mainland through Goengyi?"

    vl alexis_vl_prefix 9
    a "They got scared?"

    show sue melancholic
    s "Very. So Otren's been rattling its saber and bullying us ever since. We were a province of theirs once, and—I'm sorry."
    show sue embarrassed
    s "I'm supposed to be helping you with homework, not lecturing you."

    "I don't say anything; there's nothing for me to say. She just told me her country's wrapped up in generations of geopolitical bullshit."
    "And I didn't know the first thing about any of it."

    "Even when I finally do have words to say, I'm sure as sin they aren't the right ones."

    vl alexis_vl_prefix 10
    a "Did you run away? Wait, no! I mean, with… all of that… Did it have anything to do with why you decided to go to a foreign school?"

    "Again, I expect her to be angry with me, but she isn't. This woman has the patience of a saint."

    show sue neutral
    s "It is the reason I'm here, yes. Did I run away, no."

    "She crosses her arms and her eyes drift off to the corner of our table."

    show sue melancholic

    vl alexis_vl_prefix 11
    a "Is something wrong?"

    s "Not exactly. It's just that the idea of me running away will probably make more sense than the truth."

    vl alexis_vl_prefix 12
    a "And what is that truth?" 

    "She remains silent for a minute before taking a breath to compose herself."

    show sue neutral
    s "There is someone I was hoping to meet. Someone who, I believe, will be able to help strengthen my nation's delicate position." 
    s "Give it strong allies it desperately needs to deter any aggression from the rest of the Confederation."
    s "I've been waiting three years for them."

    vl alexis_vl_prefix 13
    a "Three whole years?"

    "Who in the Abyss could she have been waiting that long for? And someone with the potential to shift the balance in international affairs?"

    "It couldn't have been someone on staff. They would've been here when she first showed up."
    "And it isn't like she'd have been able to know who would be hired after she started."

    "So a student, then? But they'd have to have a big enough profile for someone all the way in Goengyi to plan this around when they would start here."
    "What student…"

    vl alexis_vl_prefix 14
    a "You mean the prince."

    "I guess he does have the empress on speed dial. And he must have dinner with the prime minister regularly. Is that what she was hoping for?"
    "To have someone to speak up for Goengyi here in the empire?"

    s "That's right."

    show sue melancholic 
    "She laughs, but there's no joy behind it."

    s "You must think I'm crazy."
    s "Going to a school on the other side of the planet and waiting years just for a chance to speak to someone who won't have the power to make direct decisions for decades."

    "She's right. It was crazy. But it isn't like I'm any better. My mother sent me here to find someone rich to marry to save our soon-to-be-bankrupt family."

    "And if not that, it would be damn near the same thing as her. Talking to someone with connections just hoping they'd be able to help get us out of this rough patch."

    "The only difference is that Sue's problem makes mine seem like a walk in the park."

    show sue neutral

    vl alexis_vl_prefix 15
    a "No. I don't think you're crazy at all."

    "She doesn't say anything in response to that, and we get back to my history assignment."
    
    # jump to second club route dyalt
    $ renpy.call(chosen_club2 + "_route_dyalt", "Vanus", 23)
    #jump no_clubs_route_dyalt

label no_clubs_route_dyalt(month, date):
    $ goude_vl_prefix = "audio/voices/Supporting-Extra/Isaiah/Sue/Isaiah_Sue_Month4_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Sue/Month 4/" + player_voice_prefix + "_Sue_Month4_"

    call screen calendar(month, date, "Dyalt", 24)
    scene bg student_councilroom_noon with fade

    $ renpy.notify("Sue - \nIstday, Dyalt 24th, 1027 RD")

    show sue neutral

    "Like what usually ends up being the case, Sue and I are the last ones in the Student Council Room, long after everyone else has gone home for the day."

    "It only makes sense for the president to have the most work. So it only makes sense her aide stays behind in case she needs anything."

    "I'm brewing Sue a cup of coffee, the coffee maker the source of the only noise in the room. The silence is suddenly broken by the door opening."

    vl goude_vl_prefix 1
    h "Ah, Sue, there you are."

    show sue happy
    "She laughs."

    s "Did you expect to find me anywhere else at this time of day?"

    vl goude_vl_prefix 2
    h "I guess not."

    show sue neutral at center with dissolve
    "The headmaster nods in my direction as me makes his way to the table dominating the center of the room."

    vl goude_vl_prefix 3
    h "You and the Council did a good job earlier this month."

    vl alexis_vl_prefix 1
    a "I still find it wild that people just ignored the rules on the books for so long."

    "I bring Sue's coffee over to her."

    vl goude_vl_prefix 4
    h "When I was on the Council, I didn't think too much about that. Though it only makes sense that it would reach a tipping point eventually."

    vl alexis_vl_prefix 2
    a "Would you like some, Headmaster?"

    vl goude_vl_prefix 5
    h "Yes, please."

    "As I make my way back to the coffee maker, the headmaster places his hands on the table and laces his fingers, settling his eyes on Sue."

    vl goude_vl_prefix 6
    h "But I hear that your business is only starting. The prince wants to revisit the charter?"

    s "He does. And his plans just so happen to line up with your own, Headmaster."

    vl goude_vl_prefix 7
    h "Do they? How curious."

    s "But I'm sorry to say that it won't be easy for any such reforms to pass. When you put the idea forward, you must've known they'd be controversial."

    vl goude_vl_prefix 8
    h "I certainly had an idea."

    "Once the headmaster has his coffee, I lean against the counter near the coffee maker."

    s "Did the Board of Directors not object? The cost of this must give them pause."

    vl goude_vl_prefix 9
    h "The only things they care about are making money and gaining the school more prestige."

    vl alexis_vl_prefix 3
    a "And they think that'll happen?"

    vl goude_vl_prefix 10
    h "The Sectors set us apart from the other imperial academies and universities."

    s "And so would being able to spend the next three years boasting that students get to travel the world as part of the curriculum."

    vl goude_vl_prefix 11
    h "Exactly."

    show sue melancholic
    s "Most of the Council is more worried about the costs of this all than the bragging rights they'd earn."

    vl goude_vl_prefix 12
    h "I'm aware. That's why I'm here. You'd be able to assuage their fears, wouldn't you?"

    "Did I hear that right? Is the headmaster trying to get something out of Sue now?"

    show sue neutral
    s "We both know that's not my job, Headmaster."

    vl goude_vl_prefix 13
    h "Is it now?"

    s "You were in this chair once. You know it's our duty to serve the student body, not our own interests, or anyone else's."

    vl goude_vl_prefix 14
    h "And you do that by being perpetually neutral? Little more than a watcher with a gavel? Besides, isn't that what you'd be doing by putting your support behind my initiatives?"

    s "Would I be?"

    vl goude_vl_prefix 15
    h "This isn't black and white, Sue. I recognize that there's good and bad to my ideas. So it's up to you to decide if the answer to that question is yes or no."

    s "And if my answer is \"no?\""

    vl goude_vl_prefix Chuckle
    "He chuckles."

    vl goude_vl_prefix 16
    h "I have an odd feeling that won't be the case. But if it is, I'll admit defeat and go back to the drawing board."

    "The headmaster quickly finishes his coffee and stands up."

    vl goude_vl_prefix 17
    h "Thank you for the coffee, [a]."

    voice sustain
    h "And remember the power your office grants you, Sue. I trust you'll use it to do the right thing." 
    voice sustain
    h "For your peers, the school… yourself. A good evening to you both."

    show sue melancholic
    "He leaves us in an awkward silence where Sue spends an uncomfortable amount of time contemplating her coffee."

    s "He does have a point."

    vl alexis_vl_prefix 4
    a "About what?"

    s "I could make or break this new charter, couldn't I?"

    vl alexis_vl_prefix 5
    a "Probably. But what was that thing he said about doing the right thing for yourself? Seems pretty ominous, if you ask me."

    s "I'm still trying to make sense of that."

    "Obviously, the purpose of his visit was to try and get Sue to put her weight behind his plans."
    "Yet he just up and left without her yielding even an inch. What's his game here?"

    vl alexis_vl_prefix 6
    a "Would your answer be no? About this being in the best interest of the school."

    s "My thoughts are more complex than a single word could convey."

    vl alexis_vl_prefix 7
    a "So you're somewhere in the middle."

    s "You could say that. My problem is the Sectors and the study abroad being a package deal. But I imagine they're going to stay that way."

    show sue embarrassed
    "Sue groans and buries her face in her hands."

    s "Could you leave me? I need time to think."

    show sue melancholic
    "I grab my bag and make my way to the door. With my hand hovering over the doorknob, I take a moment to reconsider."
    "I don't have anything else to do, and whatever the headmaster could've possibly meant is weighing on Sue's mind."

    "But my gut is telling me that leaving her alone isn't the right thing to do. If Sue wants to think, that means she needs some peace and quiet."
    "And it isn't like she can't have that while I'm still here."

    "So I turn around and take the seat nearest to the door. At the sound of me settling back down, Sue peaks through her fingers and sighs, but she doesn't rebuke me."

    "I might be sitting here for a while, but if the company puts her at ease even a little bit, future me will be able to forgive a few lost hours."
    call student_council_dyalt("Dyalt", 24) from _call_student_council_dyalt_5

label no_clubs_route_neralt(month, date):
    $ phillip_vl_prefix = "audio/voices/Supporting-Extra/Phillip/Sue/Phillip_Sue_Month5_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Sue/Month 5/" + player_voice_prefix + "_Sue_Month5_"
    
    call screen calendar(month, date, "Neralt", 11)
    scene bg wilson_salon_afternoon with fade

    $ renpy.notify("Sue - \nZaeday, Neralt 11th, 1027 RD")

    show sue neutral

    "It's been a while since I was last in the salon. There's never much reason for me to go. Usually, the only times I'm around is when Sue drags me up."
    "And today is one of those days. On a weekend too, no less. I guess she wants to have brunch?"
    "At Sue's request, the server that greets us leads us to a table in a corner, which is about as private as you can get in this already exclusive establishment."
    "We put in an order for tea and an assortment of fruit tarts and then are left alone."
    
    vl alexis_vl_prefix 1
    a "You said you were waiting for someone?"

    s "That's right."

    vl alexis_vl_prefix 2
    a "And you wanted your aide around?"

    show sue happy
    s "You're off the clock today. Say it's more like asking a friend for moral support."

    vl alexis_vl_prefix 3
    a "Moral support?"

    show sue neutral at center with dissolve
    "Our things arrive a lot more quickly than I thought they would. Guess that, even though it's a weekend, we're here early enough that most of their clientele is still asleep."

    "As we breakfast, Sue passes the time by asking me how school's been. It's subtle, but I can almost feel the slightest bit of anxiety coming off of her. Who is she waiting for?"

    show sue neutral:
        xpos 0.2
        yalign 1.0
    show phillip neutral:
        xpos 0.5
        yalign 1.0
    with dissolve
    vl phillip_vl_prefix 1
    p "Good morning, Sue. I see [a] is with you too."

    "The prince is led over to our table. Instinctively, I shoot up, eyes pinned on him."

    vl alexis_vl_prefix 4
    a "He's who you were meeting? Are you two sure you want me to stick around, then?"

    show phillip happy:
        xpos 0.5
        yalign 1.0
    vl phillip_vl_prefix 2
    p "I wouldn't mind one bit. It isn't like you're a total stranger."

    "There's a light tug on my sleeve. I peel my eyes off of the prince to turn towards Sue, who's looking up at me."

    s "If you wouldn't mind, I'd like you to stay."

    "\"Moral support,\" right. If I want to run, she must want to, too. The server brings over another chair and I set it next to Sue."
    "The prince sits down and, at Sue's invitation, helps himself to some of our tea and tarts."

    show phillip neutral:
        xpos 0.5
        yalign 1.0
    vl phillip_vl_prefix 3
    p "So, what did you want to talk about?"

    show sue melancholic:
        xpos 0.2
        yalign 1.0
    "Sue clasps her hands together, lips pursed. She takes a deep breath before speaking."

    show sue neutral:
        xpos 0.2
        yalign 1.0
    s "How much do you know about Goengyi, Your Highness?"

    "Of course she wanted to speak to the prince. This very moment is the only reason she came to this school. And she wants me to be here for it?"

    vl phillip_vl_prefix 4
    p "Not much, if I'm being honest. It's part of the Confederation, right by Estary, mostly Spiritist. That's about it."

    "She gives him the same primer she gave me. He sits in silence, nodding from time to time, never once looking like he felt a fool for not already knowing all of this."

    s "Getting a chance to speak with you about Goengyi is why I came to this school."

    "Tart halfway to his mouth, the prince freezes. He sets it down."

    vl phillip_vl_prefix 5
    p "Really? You must know there's not much I can do."

    s "No, but you do have the ear of some very powerful people. Your father's commander-in-chief of the Imperial Armed Forces."
    "Your mother's one of the most famous philanthropists in the world, not to mention the prestige her blood grants her."

    s "And you've had a chance to personally speak to multiple government ministers, haven't you?"

    show sue melancholic:
        xpos 0.2
        yalign 1.0
    show phillip contemplative:
        xpos 0.5
        yalign 1.0
    "The prince silently eats a few tarts. He's no doubt weighing everything Sue just told him, but the longer he goes without speaking, the more worried I get."
    "Sue looks calm, but I can only imagine how fast her heart must be beating."

    show sue neutral:
        xpos 0.2
        yalign 1.0
    "Again, Sue takes a breath, and leans forward."

    s "This new charter of yours faces an uphill battle. Plenty of people have plenty of reasons not to want it to pass."

    s "Some of these people are agreeable, and could be willing to change their minds, with the right arguments. From the right person."

    "And I have a feeling she isn't talking about the royal in this situation. All this time, Sue has insisted that it was her job to remain neutral."

    "The moment she did something that might have seemed as a challenge to one side of this argument, she diffused it to keep Anti-Sectorists from getting any ideas."

    "She must really be desperate to get him to say yes."

    show phillip neutral:
        xpos 0.5
        yalign 1.0
    vl phillip_vl_prefix 6
    p "Quid pro quo, from you? I'm surprised.  I thought that wasn't your style."

    s "Not normally, no. Does it disturb you? This political dealing?"

    vl phillip_vl_prefix 7
    p "As a matter of principle, I don't like it."

    s "So you'll decline my offer?"

    show sue melancholic:
        xpos 0.2
        yalign 1.0
    show phillip contemplative:
        xpos 0.5
        yalign 1.0
    "He doesn't answer. For the third time, Sue takes a breath. Then her tone takes a grave turn."

    s "I admire that about you, Prince Phillip. But there's much more at stake here than your principles."
    s "Goengyi is home to nearly 14 million. All I'm asking of you is to talk to people."
    s "For that, your conscience will be able to forgive a little bit of tit-for-tat, won't it?"

    "He frowns, and in that moment, my anxiety spikes."

    show phillip neutral:
        xpos 0.5
        yalign 1.0
    vl phillip_vl_prefix 8
    p "When you put it like that, it probably can. Then when you call, I'll bring your concerns right to them. But you're alright with them not acting?"

    show sue neutral:
        xpos 0.2
        yalign 1.0
    s "If you do, they might act, and they might not. I don't know. What I do know is that if you never act, nor will they. So what is there to lose?"

    "The two exchange contact information. Then the prince stands up, extending a hand."

    show phillip happy:
        xpos 0.5
        yalign 1.0
    vl phillip_vl_prefix 9
    p "Then I guess we're done here. Hopefully we'll both get what we want out of this."

    "Sue stands and takes his hand, giving it a firm shake."

    s "Enjoy the rest of your day, Your Highness."

    hide phillip with dissolve
    show sue happy at center with dissolve
    "When he's gone, she falls into her chair, leaning back and letting out a long sigh."

    vl alexis_vl_prefix 5
    a "So, um… did the moral support work? I didn't do anything."

    s "No, you did great. I don't know if I would've been able to do that alone. Thank you for staying with me. It means more than you know."

    "She reaches for one of the tarts."

    s "Now, how about we finish these off? Wouldn't want them to go to waste."

    vl alexis_vl_prefix 6
    a "You don't have to tell me twice."

    "When we're done, we take our leave of the salon. Sue's noticeably more chipper as we do, even humming a little tune to herself."
    "Not like I can blame her. Three and a half years of anticipation, and it's finally paid off. Partially."
    "I just hope that, when the chips are down, this talk will actually pay off for her and the people of Goengyi."
    
    # jump to second club route neralt
    $ renpy.call(chosen_club2 + "_route_neralt", "Neralt", 11)
    #jump student_council_exalt

label no_clubs_route_exalt(month, date):
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Sue/Month 6/" + player_voice_prefix + "_Sue_Month6_"
    
    call screen calendar(month, date, "Exalt", 29)
    scene bg mainstreet_night with fade

    $ renpy.notify("Sue - \nZaeday, Exalt 29th, 1027 RD")

    "Already, the end of the year. The back half of it went by so quickly. Where did the time go?"

    "I don't care much for these cold winter nights, but there is something oddly beautiful about how still and quiet they tend to be, with so many people staying inside to keep warm."

    "The town's chapel has never really stood out to me. I've walked by it plenty of times, but never had a reason to go inside."
    "I haven't had a reason to go into a house of worship for years now."

    "Seeing Sue head inside as I approach tonight, though, is definitely reason enough."

    scene bg chapel_night with fade 
    show sue neutral

    "The chapel, unsurprisingly, is silent. There are a fair number of people gathered in its pews, heads bowed silently in prayer."
    "It only makes sense. This week is the Week of Life, after all."

    "Something about that thought compels me. I don't know nor care if the Divines—or anyone else for that matter—is listening, but I bow my head."

    "Father, wherever your soul is now, I hope you're happy. I miss you."

    s "[a]?"

    "Sue's voice is hushed, but with how quiet the chapel is, she's still easy to hear."
    "She's beckoning for me to join her on a pew by the entrance, and I take her up on the offer."

    "When I'm at her side, I lean over and whisper."

    vl alexis_vl_prefix 1
    a "Week of Life is basically the same in Goengyi?"

    s "Bigger, actually, because of how important taking care of our loved ones' souls is in animism. Those roots are still strong."

    "We pass a moment in peaceful silence."

    show sue melancholic
    s "You know, I had an older brother. His name was Joeng, and he was a soldier."
    s "I always make sure to pray for him at this time of year."

    vl alexis_vl_prefix 2
    a "I'm sorry for your loss."

    s "I didn't really get it before he died. But when I lost him, it all started to make sense to me."

    "I reach for my necklace. Ever since the new dress code passed, I haven't had a reason to hide it."
    "It's been part of my daily routine for so long that I barely think about it anymore. It's almost like it just is part of me."

    vl alexis_vl_prefix 3
    a "This is a memento. Of my father. He… was at the wrong place at the wrong time. This upcoming spring will be eight years."

    show sue embarrassed
    s "I'm… sorry."

    "I glance over at her. The pensive sorrow that was in her voice when she was speaking about her brother's been replaced with what I can only describe as guilt."
    "But over what?"

    s "I'm so sorry."

    vl alexis_vl_prefix 4
    a "What're you apologizing for?"

    s "Six months we've known each other, and I didn't know anything."

    vl alexis_vl_prefix 5
    a "W-well, that can be forgiven. It isn't like I ever mentioned him before."

    "She shakes her head."

    s "I mean your entire family. I don't know anything about them. I never bothered to ask, and it's been half a year. How careless of me."

    "I open my mouth to try and comfort her, tell her that it's not her fault, since it isn't like talking about our families is relevant to our jobs."
    "In the end, I decide against it, and go for something else entirely."

    show sue neutral at center with dissolve

    vl alexis_vl_prefix 6
    a "I have two younger siblings. A brother named Salem and a sister named Skylar. They're twins. Just started tertiary school this year."

    show sue happy
    s "Those are lovely names."

    vl alexis_vl_prefix 7
    a "I'll have to tell my mother that you said that. She put a lot of thought into our names."

    s "Did she?"

    show sue neutral

    vl alexis_vl_prefix 8
    a "She really did. She hoped that Skylar would get into some top school and make a groundbreaking discovery in some renowned field."
    voice sustain
    a "Salem's supposed to be a guy people can rely on and feel safe around. He has his moments, but he's a good kid."

    s "And what about your name?"

    #This will differ slightly based on if the player kept the name \"Alexis\" or not.

    if temp_name == "Alexis":
        #1 - ALEXIS
        vl alexis_vl_prefix 9
        a "\"Helper.\""

        s "Oh."

        show sue happy
        "She smirks and covers her mouth, like she's giggling into it and doesn't want me to see."

        s "That makes a lot of sense."
    else:
        #2 - PLAYER INPUTTED NAME
        vl alexis_vl_prefix 10
        a "[temp_name]? My parents told me it means \"Black Wolf.\" It was a nickname the founder of our house had when he was in the military."

        s "Black Wolf… I like that name. They must've been strong."

    #CONTINUE
    show sue neutral
    s "Would you mind telling me a little bit more about your family? I feel like there's a lot of lost time to make up for."

    vl alexis_vl_prefix 11
    a "Sure. Let's see… One time, when we went to Troara, my father pissed off a stoat and it got into his clothes…"

    "We pass the time, sitting in the corner of the chapel, whispering in hushed tones."
    "Sue occasionally chimes in, but just like she said, she wants to hear about my family, and she lets me talk."

    "I stop after telling a few stories from when Father was still alive. Then we just sit there for a time, side by side, not saying a word."

    show sue melancholic
    "It took Sue yawning to bring us back to reality."

    vl alexis_vl_prefix 12
    a "We might not have anything to do this week, but I guess that's not an excuse to stay out all night, huh?"

    show sue neutral
    s "I wanted to use this week to get caught up on sleep. I should really go and do that."

    "Outside of the chapel, we say goodbye and part ways, heading back to our respective dorms. I don't know what I was expecting, when I followed her into the chapel."

    "Spending hours recalling things that happened so long ago, during simpler, happier times wasn't anywhere near the top of the list."

    "I feel oddly… lighter. Whatever the rest of this week has in store for me, I've got a feeling it's going to be a good way to ring out this year."
    call phillip_elvera("Exalt", 29) from _call_phillip_elvera_5

label no_clubs_route_elvera(month, date):
    #this is sad so maybe add special music for sunofes ? alexis cries so 
    $ sterling_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Sterling/Sterling_Sue_Month7_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Sue/Month 7/" + player_voice_prefix + "_Sue_Month7_"

    call screen calendar(month, date, "Elvera", 27)
    scene bg mainstreet_night with fade

    $ renpy.notify("Sue - \nUctday, Elvera 27th, 1028 RD")

    "Sue and I exit the Plainfield Mall, fresh off of a new movie that just came out. Yet another adaptation of that famous play, Scarlet Blade under a Violet Moon."

    "I've seen bits of it here and there over the years, but tonight was my first time seeing any of it in full."

    show sue happy

    s "What an amazing movie."

    "Sue dabs at her eyes with a sleeve."

    show sue melancholic

    vl alexis_vl_prefix 1
    a "Still feeling emotional?"

    s "Can you blame me?"

    "Not really. I knew that the original play was a tragedy, and I could hear sniffles from more people than just Sue during the movie."

    s "What, that wasn't enough to make you cry?"

    "I shrug."

    show sue neutral at center with dissolve

    vl alexis_vl_prefix 2
    a "I mean, it was definitely heartfelt, but I'm not sure I'd call it tear-worthy."
    voice sustain
    a "Besides, I'm just not that much of a crying person."

    s "Oh. Well, I suppose that's fair."

    "There's no more discussion of the movie after that. The two of us walk around Huntsdale, enjoying the growing warmth of the night that's starting to come with spring and the new year."
    "I'm not going to miss winter, that's for sure."

    hide sue

    "But the coming of the new year means that the school year is right on the cusp of ending."
    "It's going to be weird, having to say goodbye to this town and all the people I've met so soon. I'm going to miss them."

    "There's no doubt that people have made lifelong friends here;"
    "they won't have to worry about falling out of touch just because they've walked across the stage and are moving on to the next chapter in their lives."

    "After just one year, have I forged any bonds that strong?"

    "When Sue stops walking, I'm brought back down to Unios. We're in a local park. I didn't even notice we were heading in this direction."
    "At this time of the day, there aren't many people about. Maybe just the odd jogger."

    show sue neutral

    s "Up for a little break?"

    vl alexis_vl_prefix 3
    a "Sure."

    "We take a seat on a bench, and then I'm suddenly hit with a wave of unease. Why the park, and why this break?"

    show sue melancholic

    s "I'm guessing the last time you cried was when your father died?"

    vl alexis_vl_prefix 4
    a "That's…"

    "…right? It only makes sense. You'd cry no matter how old you are when you lose a loved one, and I was only twelve."
    "Of course I cried when Father died. So why don't I remember it?"

    "When she asked the question, Sue didn't look at me, but my silence makes her turn, and the look in her eyes breaks my heart."

    s "So you didn't?"

    vl alexis_vl_prefix 5
    a "I don't think so. At least, I don't remember it. When he died, I threw myself into making sure the rest of the family was alright."

    show sue neutral at center with dissolve

    s "So you comforted your mother instead of her comforting you? That's so… shitty of her."

    vl alexis_vl_prefix 6
    a "It isn't like that. She tried. I just didn't let her. I wanted to be the one to make her feel better."
    voice sustain
    a "Not the other way around."

    #"Additional line if the player kept the name Alexis."

    #BRANCH
    if temp_name == "Alexis":
        s "Because you were that focused on being the \"Helper.\""

        vl alexis_vl_prefix 7
        a "That's right."

    #CONTINUE

    s "Does that mean you never had a chance to properly grieve?"

    vl alexis_vl_prefix 8
    a "I guess not?"

    "I shrug for the second time tonight."

    vl alexis_vl_prefix 9
    a "But it's not that big a deal, right?"

    show sue melancholic

    "We fall silent after that. In the minutes that pass, I become uncomfortably aware of how sweaty my palms have become."
    "What's the problem with what I said? Father died nearly eight years ago. I've been fine."

    "Why would it be such a big deal if I haven't cried about it? Why isn't Sue saying anything?"

    "When was the last time silence put me on edge like this?"

    s "Let's say that you died."

    "And that's how the silence is broken?"

    s "It's only natural that your mother would want to make sure Salem and Skylar are okay, right?"

    "I nod."

    s "How would you feel if she was so focused on them that she never allowed herself a moment to cry and grieve her own child?"

    "And that breaks my heart into even tinier fragments."
    "The idea of Mother suffering in silence just because she's the caretaker, and meant to be strong for the children that rely on her."

    vl alexis_vl_prefix 10
    a "I wouldn't like it. Just because she's looking after the other two doesn't mean she should bottle up… Oh."

    show sue neutral

    s "Don't you think that's exactly how your father feels? Has felt, for years now? Some people just don't cry very much."
    s "If you're that type of person, that's fine. If you don't cry again afterwards, that's fine."

    show sue melancholic

    s "But, just once, don't you think your father would want you to properly let it all out with him gone?"

    "I reach for my necklace, the final gift I ever received from Father."
    "Taking it in hand reminds me of something he would tell me when I was younger, whenever I refused to take a break helping around the house."

    vl sterling_vl_prefix 1
    ster "Seeing you help people makes me so proud. But please don't forget to help yourself from time to time, okay?"

    "My heart's ground to a fine dust, and with it, the dam I had constructed in my mind after his death."

    "The emotions I'd held at bay so I could put on a strong face for my younger siblings who had just lost their loving father, and a mother who had lost the man she'd loved longer than I'd been alive, are finally free to rush forth."

    "My sobs wrack me, and I'm returned to that day. The officers from the Prospera Police Department coming to the house and speaking with my mother in private."

    "Her bringing me and the twins into the drawing room and forcing herself to repeat the news that her husband was dead."
    "All three of them breaking down in that moment."

    "The only thought in my mind then was to wrap my arms around the twins and hold them."

    "Not to think about how I'd never see my father's radiant smile again, feel his arms around me, hear his boisterous laugh, have him help me with my homework or praise me when I did a good job."

    "He would never see me graduate from secondary school or from university, or get married, or have children."
    "So many milestones we should've been able to share together, forever lost."

    "And I never let myself dwell on those thoughts. There were more important things to worry about, I said."

    vl alexis_vl_prefix 11
    "As I cry, Sue wraps an arm around me. That only makes me cry harder. Being comforted in the same way I did for others for so long."

    "Eventually, the tears run dry. My voice is hoarse when I next speak."

    vl alexis_vl_prefix 12
    a "I'm sorry for going on for so long. And for crying all over your uniform."

    show sue happy

    s "Silly, don't apologize for that."

    "She stands, and helps me up."

    show sue neutral

    s "Would you like me to walk you back?"

    vl alexis_vl_prefix 13
    a "Yeah, I think I'd like that."

    "I do feel much better now. Lighter than I've felt in ages. I could definitely make my way through the quiet streets of Huntsdale on my own."
    "But why pass up on the chance to spend even a little bit more time with Sue?"
    
    call no_clubs_route_verabris("Elvera", 27) from _call_no_clubs_route_verabris

label no_clubs_route_verabris(month, date):
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Sue/Month 8/" + player_voice_prefix + "_Sue_Month8_"

    call screen calendar(month, date, "Verabris", 3)
    scene bg student_councilroom_afternoon with fade

    $ renpy.notify("Sue - \nZynday, Verabris 3rd, 1028 RD")

    "I'm the first to arrive in the Student Council room after Sue. There's still a bit more time until the others start trickling in for our routine meeting."
    "When I enter, she's seated at her desk, enraptured by some piece of paper."

    show sue neutral
    "She usually greets the people that enter, or at least looks up from whatever she's working on, but not today."

    show sue neutral

    vl alexis_vl_prefix 1
    a "Hey, Sue."

    "She jumps. Clearly, she didn't even notice that someone had come in. When she looks at me, the light in her eyes stops me dead in my tracks."
    "Then the next thing I know, her arms are wrapped around me. I don't think I've ever seen her like this."
    show sue happy

    vl alexis_vl_prefix 2
    a "Who are you and what have you done with Sue? What is that piece of paper?"

    s "An offer of employment! I have a job for when I get home!"

    vl alexis_vl_prefix 3
    a "That's great! What's the job?"

    s "The Goengyi Presidential Office. I'll be an aide, just like you."

    "She laughs."

    s "Oh, how the tables turn. Now it's going to be my job to fetch someone's coffee!"

    vl alexis_vl_prefix 4
    a "Ha ha. Very funny."

    "But it sounds like the first step towards a career in politics, and it wouldn't surprise me if those were the sorts of ambitions she had."

    s "But if getting coffee for the person running my country helps give them the energy to make the important decisions, I'm more than happy to serve."
    s "I couldn't have asked for anything better."

    "Her smile falters. Her contagious elation at the news of the new job is pierced by a sudden onslaught of what I can only describe as fear."

    show sue melancholic

    vl alexis_vl_prefix 5
    a "Are you alright?"

    s "I feel so small and helpless. I want to help Goengyi—I want to help my home—but what can someone like me do against a behemoth?"

    "I place a hand on her shoulder and gently squeeze."

    vl alexis_vl_prefix 6
    a "Come on, don't think like that. Focus on the things you've already done."

    s "Like what?"

    vl alexis_vl_prefix 7
    a "You worked hard to get into the school, for one. The prince gave you his word to speak up for Goengyi to the powers that be here at home."

    s "And now you've got a government job."

    s "But that isn't enough to keep everyone safe."

    vl alexis_vl_prefix 8
    a "It might not seem that way, but think about it like this."

    "I think back to her conversation with the prince. May as well try something she used on him back then."

    vl alexis_vl_prefix 9
    a "You're one person. Otren's a country of, what, nearly 300 million?"
    voice sustain
    a "If you're thinking that it's you against all of that, of course you're going to feel hopeless."
    voice sustain
    a "But for just one person, you're doing good, making connections you're going to need to deal with it all."
    voice sustain
    a "You're not alone in this. You've got me, your parents, the prince, your future co-workers… That should make you feel powerful, not powerless."

    "She leans against the table, letting my words sink in."

    show sue neutral at center with dissolve
    s "You're right. I don't have to be Goengyi's sole savior. I can't be. For years, I've had it all wrong. Thank you."

    vl alexis_vl_prefix 10
    a "It's what I'm here for."

    show sue embarrassed
    s "And… you meant that earlier? That you were on my side, too?"

    vl alexis_vl_prefix 11
    a "Of course! \"Moral support\" and all."

    "She laughs."

    show sue happy
    s "Again, thank you."

    "She clears her throat."

    show sue neutral
    s "The others will be here soon. Let's act natural, shall we?"

    "Then it's my turn to laugh."

    vl alexis_vl_prefix 12
    a "As natural as the day I was born."

    show sue embarrassed
    s "As natural—that's disgusting."

    "But she laughed all the same."
    
    show sue happy
    "We settle into our usual routine, and by the time the others begin filing in, they're none the wiser to the moment she shared just a few minutes ago."
    
    #jump to second clubd route verabris
    $ renpy.call(chosen_club2 + "_route_verabris", "Verabris", 3)
    #jump student_council_verabis

label no_clubs_route_overa(month, date):
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Sue/Epilogue/" + player_voice_prefix + "_Sue_Epilogue_"

    call screen calendar(month, date, "Overa", 23)
    scene bg student_councilroom_afternoon with fade

    $ renpy.notify("Sue - \nIstday, Overa 23rd, 1028 RD")

    "It's over. The Student Council just wrapped its final meeting for the year."
    "Well, to call it a Student Council meeting would be a bit of a stretch. After the election, the rising Council started taking charge, to give them a bit of a test run."

    "But this last week, we gave up. Everyone already had exams to deal with, and it wasn't like anything the Council really needed to do was going to crop up at the eleventh hour, so people just stopped by, ate snacks, and played games."

    "I'm a bit surprised we were able to get away with it."

    show sue neutral
    "Sue is walking around the room, taking it in for one final time."
    "Saying goodbye to the place is going to be weird for me, but I can't even imagine what it must be like for her, after all the time she's spent here."

    s "We did good this year, didn't we?"

    show sue neutral

    vl alexis_vl_prefix 1
    a "Definitely. I just wish I could be around to see how everyone benefits from all this."

    s "Right."

    "I was expecting some sort of nostalgic melancholy, but she seems oddly detached."
    "Her voice is barely a whisper, and after overseeing a year as transformative as this, I figure she would've had more to say than just \"Right.\""

    show sue melancholic
    s "There have been times when I think back to people who used to go here, who used to be on the Council with me."
    "Of things I wanted to say to them, but never did, for one reason or another. And now they're gone."

    s "With my peers, I could always just wait until we got back from summer break, but that's not an option anymore."
    s "The things I don't say now may very well stay unsaid forever."

    vl alexis_vl_prefix 2
    a "And you'd regret that? You do regret the times it's already happened?"

    s "Perhaps. But if this is to be a final goodbye, it's better to make sure that things aren't left unsaid, right?"

    show sue neutral at center with dissolve

    vl alexis_vl_prefix 3
    a "I think so, yeah."

    "She completes a lap of the room, taking a seat next to me at the table. Then she's silent."

    "This… has to do with me, right? I mean, why else would she be talking about regretting things she didn't say to people right before graduation?"

    vl alexis_vl_prefix 4
    a "Um… Sue?"

    "She clears her throat, a faint blush blooming across her face."

    show sue embarrassed
    "Oh Gods."

    s "Ever since I've been at this school—no, ever since Joeng died—I've been like an island."
    "Tackling the world alone, because I thought that was what it took to achieve my goals."

    "She doesn't look at me as she speaks, eyes turned down towards the table instead."

    show sue melancholic
    s "It all started with something so small: you insisting on helping me with the budget. Looking over numbers for hours, but that toppled the first stone."
    s "I… don't think I knew that I could rely on someone to always be at my side, helping me like that."

    "A nervous little laugh breaks out of her."

    s "I mean, it is your job, but it's not just that. You want to help, just because you like easing peoples' burdens."
    s "I admire that. A lot."

    "She finally looks at me, a steely coolness in her eyes. Not cold, but not especially warm, either."
    "I can tell her heart must be pounding—like mine is right now—but she's… at ease. Like she's comfortable with however this is going to go."

    show sue neutral
    "Because I know what's about to happen even before she takes my hands in hers."

    s "With my return to Goengyi so soon, and everything that awaits me, it's gotten harder and harder to imagine facing the challenges that life throws at me without you, [a]."
    s "Would you be willing to face them with me, standing side by side?"

    "She didn't say the exact words, but the message is loud and clear."

    vl alexis_vl_prefix 5
    a "Sue..."
    
    menu:
        "Accept Sue's confession":
            $ sue_romance = True
            jump no_clubs_route_overa_romance_accept
        "Reject Sue's confession":
            $ sue_romance = False
            jump no_clubs_route_overa_romance_reject

label no_clubs_route_overa_romance_accept:

    show sue neutral

    vl alexis_vl_prefix 6
    a "I'd be more than willing."

    "Sue blinks at me."

    s "Come again?"

    "I can't help but laugh at that."

    vl alexis_vl_prefix 7
    a "I said that I'd be happy to face the world with you, Sue. Besides, it isn't like I'm the only one that's helped you."

    "If not for her, I'd still be bottling up all of the grief that came with Father's death."

    "I barely have time to meditate on that appreciation before she just about tackles me out of my chair with an embrace."

    show sue happy

    vl alexis_vl_prefix 8
    a "Whoa, easy there!"

    "She releases me, maintaining a firm grip on my hands."

    s "I'm sorry. I just didn't think you'd feel the same. It makes me so happy."

    "Then, just like last month, her joy falters."

    show sue melancholic

    vl alexis_vl_prefix 9
    a "What's wrong?"

    s "Even for you, I can't abandon Goengyi."

    vl alexis_vl_prefix 10
    a "And I wouldn't want you to, either. Besides, I could probably talk the family into making the move."
    voice sustain
    a "Someday. I think they'd like the change of pace."

    s "You'd do that? But uprooting your entire family—"

    vl alexis_vl_prefix 11
    a "If I have to go without them, I will. Just after I make sure they'll be taken care of here."
    voice sustain
    a "I'd just like to keep them close, is all."

    "Then something hits me, which makes the idea of a move more appealing."

    show sue neutral

    vl alexis_vl_prefix 12
    a "And the Dominion's stronger than the Confederate Dollar, so it'd be a boost to the bank accounts."

    "Sue laughs."

    show sue happy
    s "How pragmatic of you."

    vl alexis_vl_prefix 13
    a "I'll do my best here at home, so you do your best back in Goengyi, alright?"

    show sue neutral
    s "I wouldn't think of giving any less."

    vl alexis_vl_prefix 14
    a "Good. And then, someday, we'll be able to give it our all together, without the oceans keeping us apart."

    show sue happy
    s "I like the sound of that. I really do."

    "We sit there for a time, hand in hand, letting an oddly companionable silence wash over us."

    "I don't quite know what the future will have in store, but what I do know is that I have to brush up on my long term planning skills, because coordinating everything to make this all work out is going to take a long time."

    "But I'm in it for the long haul, and I have no doubt Sue is, too."
    call epilogue_graduation("Overa", 23) from _call_epilogue_graduation_13

label no_clubs_route_overa_romance_reject: 

    show sue neutral

    vl alexis_vl_prefix 15
    a "I'm sorry, but I don't think I can."

    show sue melancholic
    s "Oh."

    "She drops my hands."

    vl alexis_vl_prefix 16
    a "I do like you, but not in that way. And… my family needs me here in Magiana."
    voice sustain
    a "Dropping it all for Goengyi isn't something I'd be able to do."

    s "That I figured."

    vl alexis_vl_prefix 17
    a "I really am sorry."

    show sue neutral
    s "Don't be."

    "She rises from her seat."

    s "Matters of the heart are messy. I already knew this might happen."
    s "I just didn't want the feelings to go unshared before I left."

    vl alexis_vl_prefix 18
    a "Right."

    s "But thank you again, for everything. You're probably the best aide I could've asked for this year."
    s "And just as good a friend."

    vl alexis_vl_prefix 19
    a "And I don't think I could've asked for a better boss."

    "She walks over to her desk, inspecting the area behind it. Her back is turned to me when she speaks."

    show sue melancholic
    s "You don't have to wait up for me."

    vl alexis_vl_prefix 20
    a "Right."

    "I collect my things and head for the door. Again, her unspoken message is crystal clear."

    vl alexis_vl_prefix 21
    a "See you later."

    s "Until next time."

    "I linger on the other side of the door for a time. That was about as good as this could've gone, all things considered, but it still feels wrong."
    "Within a few days, or maybe weeks, we should be back to normal, right? That's what I hope, anyway."
    call epilogue_graduation("Overa", 23) from _call_epilogue_graduation_14

label epilogue_no_clubs_route:
    scene bg maincastle with fade 

    show sue neutral at center with dissolve
    s "Ah, [a], there you are."

    "Sue appears, seemingly from nowhere, giving me a pat on the back."

    show sue happy
    s "Made it to the end of the road. Congratulations on making it out the other side."

    a "Thanks, Sue."
    jump epilogue_sue_choice
    
label epilogue_sue_choice: 
    if chosen_club == "no_clubs":
        if sue_romance:
            jump epilogue_no_clubs_route_romance_accept
        else: 
            jump epilogue_no_clubs_route_romance_reject
    else:
        jump epilogue_no_clubs_route_not_chose

label epilogue_no_clubs_route_romance_accept:

    show sue neutral at center with dissolve
    s "I just got off the phone with my parents. They were watching the ceremony online."

    a "Really? Isn't it the middle of the night over there?"

    "She laughs."

    show sue happy
    s "It is. But they wouldn't miss this for the world."

    "She flushes, diverting her eyes for a moment."

    show sue embarrassed
    s "So… I told them about you."

    a "You did?!"

    s "They were surprised, but happy for me. …For us."

    "I feel my face burning. I wasn't expecting this to be so embarrassing."
    "My brain scrambles to find some way to make things less awkward, but I'm not quite sure I hit the mark."

    show sue neutral
    a "My family's somewhere here. I'm looking for them. Do you want to…"

    "Sue's become a tomato. Only then do I realize what I said."

    show sue embarrassed
    s "M-meeting the family already?! Don't you think that's a bit early?"

    a "Um. Probably not the right words."

    s "Maybe your brother and sister. I'm not sure I'd survive meeting your mother so soon."

    a "Right…"

    "We settle into an awkward silence, broken only when someone calls Sue's name. It's some of her other friends."

    show sue neutral
    s "Guess it's time for me to be going, then. Talk to you soon?"

    a "Yeah. Real soon."
    jump epilogue_disciplinary_route

label epilogue_no_clubs_route_romance_reject:

    show sue neutral at center with dissolve
    s "I just got off the phone with my parents. They were watching the ceremony online."

    a "Really? Isn't it the middle of the night over there?"

    "She laughs."
    show sue happy
    s "It is. But they wouldn't miss this for the world."

    "An awkward moment passes. Then Sue clears her throat."

    show sue neutral
    s "Well, I wish you the best of luck with your endeavors after this."

    a "Same to you. Let me know when you're back in Goengyi?"

    s "I will. Though it will be very late over here."

    a "Eh, it's fine. Might take some time getting used to the difference, but we'll make it work."

    "I scan the crowd. Still no sign of them."

    a "I was on the lookout for my family. Not sure where they are in the crowd."

    s "Then I won't keep you. Until next time, [a]."
    jump epilogue_disciplinary_route

label epilogue_no_clubs_route_not_chose:

    show sue neutral at center with dissolve
    s "I just got off the phone with my parents. They were watching the ceremony online."

    a "Really? Isn't it the middle of the night over there?"

    "She laughs."

    show sue happy
    s "It is. But they wouldn't miss this for the world."

    "An awkward moment passes. Then Sue clears her throat."

    show sue neutral
    s "Well, I wish you the best of luck with your endeavors after this."

    a "Same to you."

    "I scan the crowd. Still no sign of them."

    a "I was on the lookout for my family. Not sure where they are in the crowd."

    s "Then I won't keep you. Until next time, [a]."
    jump epilogue_disciplinary_route

label reunion_no_clubs_route:
    $ sue_vl_prefix = "audio/voices/Love Interests/Sue/Shared Epilogue/SueDaengQan_MeetingtheFamilySue/SueDaengQan_MeetingtheFamilySue_"
    $ arline_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Arline/Epilogue/Meet Sue/Arline_Epilogue_MeetSue_"
    $ skylar_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Skylar/Meet Sue/Skylar_Epilogue_MeetSue_"
    $ salem_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Salem/Meeting Sue/Salem_Epilogue_MeetSue_"

    $ renpy.notify("Sue - Meeting the Family\nNyday, Overa 25, 1028 RD")

    "When Sue arrives, she freezes at the sight of my mother."
    show sue embarrassed at center with hpunch
    vl sue_vl_prefix 1.2
    s "Eep!"
    "She runs to my side and takes my arm."
    
    vl sue_vl_prefix 2.1
    s "You didn't mention your mother would be here! I said it was too soon."

    vl salem_vl_prefix 1
    salem "Ah, look at them, all over each other already."

    vl skylar_vl_prefix 1
    sky "Wasn't she your boss on the Council? Scandalous."

    vl arline_vl_prefix 1
    arline "Now that they're graduated she isn't, so it should be fine, right?"

    vl sue_vl_prefix 3.1
    "Sue clears her throat. Multiple times."
    show sue neutral with dissolve
    vl sue_vl_prefix 4.1
    s "It's nice to meet you all. My name is Sue. Though I suppose this is a bit awkward, since I'll be on a flight soon."

    vl arline_vl_prefix 2
    arline "You were an international student?"

    vl sue_vl_prefix 5.1
    s "That's right, ma'am. From Goengyi."
    
    vl skylar_vl_prefix 2
    sky "Well that's far. I don't envy the flight you're going to have to sit through."

    show sue melancholic with dissolve
    vl sue_vl_prefix 6.1
    s "I've gotten used to it. It's a good time to get through a book or two, too."

    vl salem_vl_prefix 2
    salem "But that would mean reading. I'd rather sleep."
    
    show sue happy with dissolve
    vl sue_vl_prefix 7.1
    "Sue laughs."
    voice sustain
    s "That's also an option."

    vl arline_vl_prefix 3
    arline "You two are grown, so I trust you to make the right decisions. I'll support you both however I can."

    if player_gender == "female":
        vl salem_vl_prefix 3FemaleMC
        salem "Same. Want to know what's going on in my sister's head, I'm your guy. Place is mostly empty, though."
    else:
        vl salem_vl_prefix 3MaleMC
        salem "Same. Want to know what's going on in my brother's head, I'm your guy. Place is mostly empty, though."

    a "Quiet, you."
    show sue neutral with dissolve
    "For all of her nerves earlier, Sue seems quite at ease with my family."
    show sue melancholic
    "She eventually excuses herself to return to her dorm to make doubly sure that all of her things were packed for her trip."
    hide sue with dissolve
    jump finale