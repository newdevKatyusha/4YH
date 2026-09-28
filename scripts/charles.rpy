label scouts_route_jinus(month, date):
    #"EXT. HUNTSDALE MAIN STREET - AFTERNOON"
    scene bg mainstreet_afternoon with fade

    $ renpy.notify("Charles - \nJinus, 1027 RD")

    "School recently just let out for the first weekend of the year. Just like she said, Sue set me up with Charles. So I head into Huntsdale after dropping my bag off to find wherever he and the rest of his Scouts would be."
    "I did a little bit of looking into the Scouts to jog my memory after being reminded of Father’s history with them. Most people stop participating when they’re sixteen."
    "As much as I wonder how I’m supposed to be involved at my age, I’m more worried about the fact that I’m going to stick out like a sore thumb in a group of kids..."
    "I find them all out in front of the Plainfield Mall. It looks like they’re about to get started. A few young stragglers are just arriving when I reach them."
    "All eyes turning towards me is discomforting, to say the least. Not like I can blame them. At least the older kids here aren’t that much younger than I am."

    show charles neutral_scout at character_pos4 with dissolve
    cha "Good, you’re here."
    a "Glad to be here."
    "Charles claps his hands to get the children’s attention. Then he gestures to me."
    cha "I’m going to have a special helper this year. An... \"Assistant Scoutmaster,\" I guess you could say. Be sure to be nice to them, okay?"
    "I give the crowd an awkward wave."
    a "H-hey, everyone, it’s nice to meet you. I’m [a] Blakesley. Hopefully I’ll be able to help you guys out this year."
    "Spurred on by some of the older Scouts, the group offers me a disjointed chorus of greetings."
    cha "Before we get started today, let’s get to know each other a bit better. We’ve got some new friends with us, so have at it. Chat a bit. I’ll be right over here if you guys need some help."
    "He nods towards one of the older Scouts, who wrangles their peers and gets them started on... talking with each other."
    a "This is what you guys do?"
    cha "Gives us an excuse to talk for a bit, doesn’t it?"
    a "I guess it does."
    cha "So, hit me. Why the Scouts? Newcomers don’t usually join on at twenty."
    "Charles’s icebreaking exercise effectively turns into a miniature social mixer. The more experienced among the Scouts, young and old, help their peers if they’re at all shy. Though they were mainly egging on the kids he was with during Orientation."
    a "I just felt something seeing you guys earlier this week. I think it was what I heard when we were leaving. \"Honor, Integrity, and Justice for All.\""
    cha "Words to live by. And I try to help the kids learn their importance, too."
    a "My father was a Scout once."
    "Charles’s eyes go wide at that."
    cha "Really?"
    a "He didn’t talk about it much. I remember my parents laughing about his old uniform not fitting him anymore, but not much else."
    cha "Then I guess scouting’s in the blood. Better late than never for dipping a toe in, right?"
    a "You can say that again."
    #"[Beat]"
    a "...So about this icebreaker."
    cha "Helps them socialize. An important skill we develop in the kids."
    a "And the fact that you’re in front of the mall?"
    "He fishes into the pocket of his uniform pants, coming out with a stack of cards. Wait, those are credit cards, aren’t they?"
    cha "A lesson in budgeting and financial responsibility. They’ll be picking up school supplies that might’ve gotten missed during the summer."
    a "Social skills, finance? I figured the Scouts would’ve been about camping."
    cha "We’ll get to that eventually. So I hope you know how to set up a tent."
    a "I can definitely try."
    cha "And I can’t complain about that. It’s the effort that counts. "
    "He puts the cards away and looks back at the children."
    cha "I’ll take the lead. All you have to do is be a good role model for the kids."
    a "Got it. Though I expect I’m going to have to help a kid understand how tax and credit works today..."
    "Charles whistles to get his troop’s attention."

    show charles excited_scout
    cha "Alright everyone, who’s ready to do some shopping?"
    "They all begin to cheer. Charles grins at that."
    cha "For pencils and composite notebooks?"
    "How suddenly the excitement dies down gets a chuckle out of me. As he explains the purpose of their visit to the mall that day, he hands out all of their cards."
    "He cautions the kids against being wasteful, and to be especially thrifty if they want some leftover funds to buy themselves snacks."
    "I get my own card, if only to, as I’ll apparently be doing all year, lead by example."
    "Barely started my first day, and I already feel like I’ve heard quite a bit. The Scouts are a lot more than camping and fishing, it turns out. I wonder what else the year is going to have in store for me."
    "If this first Nyday is anything to go off of, it’ll be full of surprising revelations like this."

    #TODO: Update with correct timeline
    call phillip_jinus("Jinus", 5) from _call_phillip_jinus_6

label scouts_route_dallinus(month, date):
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Charles/Month 2/Reina_Charles_M2_"

    #"EXT. HUNTSDALE MAIN STREET - AFTERNOON"

    scene bg mainstreet_afternoon with fade

    $ renpy.notify("Charles - \nDallinus, 1027 RD")

    "I know that the first years are going to be busy with... something... during break next week, but I’ll be sticking around Huntsdale. What am I going to do with all of that free time?"
    "Some other local schools might have the week off too, so I wonder if Charles has anything planned for the kids..."

    show charles neutral_scout at center with dissolve
    cha "We’re just here to help enforce rules. Doesn’t mean you have to like them."
    "It doesn’t surprise me to see Charles and his Scouts. What does is that fact that he’s only with the older kids that are in his troop."
    "One of them says something, a bit too quiet for me to hear. Whatever it was, Charles shakes his head at it."
    cha "Don’t give me that. Think of it as a lesson in civic engagement. You don’t change the rules you don’t like if all you do is complain about them. Go on, everyone, you know what to do."
    cha "And take the time you’re working to think on how this all makes you feel and what you can do about situations like these when you run into them later in life."
    "With some grumbling, the group disperses, leaving Charles alone. At least it seems he wasn’t just offering lip service. He looks about as satisfied with whatever it is they’re doing as the kids were."
    a "You guys okay?"
    "He turns towards me, a small smile on his face. There’s something somber about it, almost forced. That’s enough to answer my question."
    cha "Doing a bit of community service, I guess you could say."

    show charles contemplative_scout
    "Suddenly, he gives me an intense look. It takes me aback, but the shock is overpowered by confusion just as suddenly when he takes a small notepad out of his pocket."
    a "What’re you doing?"
    cha "Your necklace. Prohibited accessorization."
    "You have got to be kidding me. My hand flies up to the necklace, protectively clasping its wolf charm."
    a "You’re not on the Disciplinary Committee, are you?"
    cha "No, I’m not."
    a "Then why in the Abyss do you care?"
    "He scribbles something into the notepad. Obviously some mysterious demerit that’ll go on file somewhere. Not like I know what’ll happen when I rack up enough of them, but that’s the second now."
    cha "Because they’re the rules. And the DC’s so understaffed that enforcing them properly’s damn near impossible."
    a "Reina doesn’t have an army of helpers?"
    cha "If she did, I wouldn’t need to help."
    "I hear someone groan in the distance. Another MIA student, being accosted by a teenager in a Scout uniform. There are few other similar interactions happening, now that I’m paying attention."
    a "Hence the \"civic engagement\" line. Why bother helping her with this?"
    cha "Because I wanted to. I don’t need any other reason to help someone else when I see them overwhelmed, right?"
    a "Not usually, no."
    cha "Besides, this week is a special case for Reina."
    a "Really? What’s so special about it?"
    cha "You’ve met Reina before, right?"
    "I nod."
    cha "Did you get her family name then?"
    "I nod again. Though I’m not sure why that’s relevant. Reina Dreyar. Dreyar, Dreyar... Then it hits me."
    "Exist long enough and it’s only a matter of time until you hear the name \"Tobias Dreyar.\" Duke of Centra; CEO of a major imperial defense contractor; chairman of the board of the tech giants Correro and Aquatica both."
    "Only the richest man on the planet. How did I not put the pieces together before? I’m not sure what face I’m making, but the smirk on Charles’s face gives me away."
    cha "So yeah, she’s going to be rather busy next week."
    a "Not sure why you need to step in. Her dad’s the one with all of the work. What’s Reina—"

    show reina neutral at character_pos2 with dissolve
    vl reina_vl_prefix 1
    r "You rang?"

    show charles excited_scout at character_pos7 with move
    "Her sudden appearance at my side makes me jump. It gets a laugh out of Charles, but it makes her look at me like I’ve lost a few marbles."

    vl reina_vl_prefix 2
    r "Are you quite alright?"
    cha "They’ll be fine. Probably."

    show charles neutral_scout

    a "Just... wasn’t expecting to see you. How much did you hear?"

    show reina worried
    vl reina_vl_prefix 3
    r "That you apparently think me some privileged little princess who faffs about and spends her father’s money."

    a "Hey, I never said that!"

    vl reina_vl_prefix 4
    r "But the thought occurred to you?"
    "Well, I can’t exactly deny that it didn’t."
    cha "Dallinus is Orsborn Heritage Month. Events are going on all over the country, but next week Ferenicia’s going to be kicking it up a notch. Helping to plan it all’s been keeping Reina real busy."
    a "You lost me at \"Orsborn.\""

    show reina neutral
    vl reina_vl_prefix 5
    r "Roma Heritage Month. \"Orsborn\" is just one of our names in the old country. I do appreciate that attention to detail, Charles."
    cha "Don’t mention it."
    a "O-oh..."

    vl reina_vl_prefix Laugh
    "Reina giggles at my discomfort. Again, I’m read like a book."

    vl reina_vl_prefix 6
    r "There’s nothing wrong with how you’ve been addressing us. The Orsborn Diaspora took to calling ourselves \"Roma\" long ago."

    vl reina_vl_prefix 7
    r "But Charles is correct. I’ll be rather preoccupied with events in the capital. I haven’t had time for my Disciplinary Committee duties of late."
    a "But that’s no excuse to let rulebreakers off scot-free, right?"
    "Reminded of how this interaction started, I tuck my necklace into my shirt before Reina gets an excuse to write me up herself."

    vl reina_vl_prefix 8
    r "Very. Though we’ve already discussed what you ought to do if you find it absurd; that your necklace counts as a rules infraction."
    "Before I can respond, she turns on Charles and offers a slight curtsy."

    vl reina_vl_prefix 9
    r "I must be going, but thank you again for this, Charles. I’ll be sure to repay you someday."
    cha "...Sure, looking forward to it."

    vl reina_vl_prefix 10
    r "And a good day to you as well, Blakesley."
    hide reina with dissolve

    "She leaves us, presumably to attend some sort of meeting about a big cultural event I only just learned was going on next week."
    "For as much as how much of a stickler for the rules Reina is drives me up the wall, that little talk makes it harder for me to be upset with her. And with Charles, for that matter."
    a "I’m off. Good on you, for lending her a hand when she needed it. "

    show charles contemplative_scout
    cha "...Yeah, thanks."
    "What’s with that weird hesitance? Before I can ask, I’m met with the grin I’ve come to expect from Charles."

    show charles excited_scout
    cha "Unless you want to stay and help—"
    a "I’ll see you at the next Scout meeting."

    scene black with fade

    #TODO: Update with correct timeline
    call student_council_dallinus("Dallinus", 19) from _call_student_council_dallinus_6

label scouts_route_vanus(month, date):
    #"EXT. WRIGHT GYMNASIUM FIELD - NIGHT"
    scene bg wright_field_night with fade

    $ renpy.notify("Charles - \nVanus, 1027 RD")

    a "There... we... go!"
    "For my first time setting up a tent, I didn’t do a bad job. But we are on the school’s field. Probably not as impressive doing this right next to civilization as it would be in the middle of the woods."
    "And in the time it’s taken me to pitch the one tent, Charles has helped the younger Scouts set up half a dozen more."
    "The plan was to go camping eventually, but with the younger kids, Charles decided that it was best to give them a test run. It would’ve been better to do it in the public park, but pitching tents and setting campfires there would’ve ended real bad."

    show charles excited_scout at character_pos4 with dissolve
    cha "Alright, good job on the tents! Who wants to roast some marshmallows?"
    "The troop erupts into cheers. Some of the younger kids were starting to look worn out after the tents, but the promise of sweet, molten goodness invigorated them."
    "Nodding approvingly at their enthusiasm, Charles gestures to a portable fire pit that he brought along with him. "

    show charles neutral_scout
    cha "To roast the marshmallows, we need a fire. Find us some firewood and we’ll be good to go!"
    "He pumps his fist in the air, triggering another wave of cheers from the kids before they scatter. We hid firewood all over the field to give them a chance to practice this sort of foraging safely."
    "Charles walks over to me, watching over the kids as they go to work."
    cha "Pretty nice night, isn’t it?"
    "My eyes drift up towards the stars above us. We’re far enough out from the capital that the stars stand out nicely, even with the light from Huntsdale. The smattering of stars above us makes me look forward to actually going camping with this group some day."
    a "Being out in the woods, that view is going to be so good."
    cha "It’ll be nice to get out of the town. The kids always love it."
    "A moment of silence falls between us. I’ve known Charles for a few months now, but most of that we’ve spent together has been for our Scout work. It feels like an appropriate time to try and learn a little bit more about him while the kids are busy."
    a "How long have you been a Scoutmaster?"
    cha "This is going to be my third year."
    "I shouldn’t be surprised, seeing how close he is to some of the troop’s veterans, but I’m still caught off-guard. The moment he could’ve hung up the uniform, he put it right back on and said \"Hit me with more responsibility! I can handle it!\" "
    a "The Scouts mean a lot to you then."
    cha "That would be one heck of an understatement."
    a "Why Scoutmaster, though?"

    show charles contemplative_scout
    "My eyes are trained on the darkening sky so, after a time, his silence starts to worry me a bit. When I glance over at him, he’s taking in the same view, a weirdly impassive look on his face."
    "Oh no."
    a "Hey, you don’t need to—"
    cha "Just wanted to pay it forward."
    "I leave the space open for him to keep going. Eventually, he does."
    cha "It’s a long story. The short version is that my Scoutmaster did an awful lot for me. So I wanted to help the next generation, just like how she helped me."

    show charles neutral_scout
    cha "I’ll probably tell you about it sometime, but I’ll just leave it at this: \"Charles Liang Ren Wei\" wasn’t a name I went by until she gave me the confidence to."
    "I don’t understand the significance of what he said, but if anyone understands the importance of names, it’s me. And with how Sue called him \"Wei,\" there must be something there, too."
    "One of the younger kids is shouting, barrelling towards us with arms full of twigs."
    cha "Mind getting the skewers and marshmallows?"
    a "This is going to be good!"
    "For as open and personable as Charles is, these small moments of seriousness I’ve seen from him lately are a bit worrying. Maybe there’s nothing serious about it. I hope that there isn’t, anyway."
    "Charles rallies the kids and supervises one of them as they ignite the fire. When the sparks go off and the flames begin to roar, everyone lets out exuberant, almost animalistic roars; people who find fire super cool, for some reason."
    "I trot over with the marshmallows, doing my best to get the kids to orderly line up; a small practice in delayed gratification, I suppose. But I have high hopes for the rest of the evening. And whatever that proper camping trip will have in store."

    scene black with fade
    # TODO: Update with correct timeline
    $ renpy.call(chosen_club2 + "_route_dyalt", "Vanus", 15)

label scouts_route_dyalt(month, date):
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Charles/Month 4/Naomi_Charles_M4_"
    $ vince_vl_prefix = "audio/voices/Friends/Vince/Charles/Month 4/Vincent_Charles_M4_"
    
    #"INT. MAGIS HALL - HOME EC ROOM - MORNING"
    scene bg home_ec_room_stove_noon with fade

    $ renpy.notify("Charles - \nDyalt, 1027 RD")

    "THUD. THUD. THUD."
    "Charles and Vince unload sacks of flour and sugar onto the crowded countertops of the home ec room early Lenday morning. Naomi and Gwynette carry the eggs. I’m left to help the kids with the copious amounts of butter we’d need."
    "Only half of Charles’s Scout troop is with us, but the room was quickly starting to look like a textbook example of \"too many cooks in the kitchen.\""

    show naomi neutral apron at character_pos1 with dissolve
    vl naomi_vl_prefix 1
    n "Okay. That’s all of the ingredients we need. It’s time to bake some cookies!"

    show gwynette neutral at character_pos3 with dissolve
    gw "Cookies!"
    "Gwynette pumps her fist, a cheer the kids were all too eager to pick up. Vincent, leaning against the counter, rolls his eyes. Charles rolls up his sleeves, then roves around the room gathering tools."

    vl naomi_vl_prefix 2
    n "Wei, can you help me get the kids started?"

    show charles neutral_scout at character_pos7 with dissolve
    cha "On it!"

    hide naomi with dissolve
    hide charles with dissolve
    show vince neutral at character_pos6 with dissolve
    "I grab a mixing bowl and join Gwynette and Vince in a corner of the room. With a devious grin on her face, Gwynette has a bag of sugar tipped over a bowl, pouring it for longer than she probably should."

    vl vince_vl_prefix 1
    vin "Are you trying to rot peoples’ teeth?"
    gw "These are sugar cookies, VV. People are going to have to taste the sugar!"
    "I reach over and tip the bag back, ending the cascade."
    a "Everything in moderation. Don’t want them getting sick of the sweetness one or two cookies in, right?"
    gw "I guess not. Then I’ll just go heavy on the butter!"

    vl vince_vl_prefix 2
    vin "First she wants to give them cavities, now she wants to clog their arteries."
    gw "Well it’s not my fault the Divines made so many delicious foods terrible for your health."
    a "I don’t think that’s an excuse to overindulge, Gwynette..."
    "With Vincent watching Gwynette like a hawk to make sure she doesn’t accidentally make a batch of sugar bombs, I work on my own dough."
    "And it’s while I’m working that I think a bit more about what I’m doing. I already knew that Charles wanted the kids to get some sort of experience in the kitchen. The fact that we’re helping Naomi at the same time isn’t surprising, either."
    "But why were Gwynette and Vince there? I just had to ask."
    gw "The chapel’s hosting a bake sale tomorrow. Chuck caught wind of it, offered to help out, roped Naomi into it, and here we are!"

    vl vince_vl_prefix 3
    vin "You really think I’d be here if it wasn’t for Gwyn and her church?"
    "Putting it like that, a grouch like him would prefer watching paint dry to social interaction. Especially with kids around."
    gw "Don’t say that. You’d help out if I asked."

    vl vince_vl_prefix 4
    vin "I-I would not. I’m not that easy."
    a "\"Easy\"? I think that’s just called being a good boyfriend."
    gw "See? BB gets it!"
    "Cheeks flushed, Vince begrudgingly helps to lay out the small balls of prepped dough onto baking sheets and into the home ec room’s ovens."

    hide gwynette with dissolve
    hide vince with dissolve
    "With nothing left to do but wait, we take in the scene of the kids in varying stages of distress, some of them covered in flour and others feverishly picking bits of eggshell out of their dough."
    "Seemingly satisfied with their ability to bake, or at least help each other bake, Charles and Naomi join us."

    show charles excited_scout at character_pos7 with dissolve
    cha "This is going to be a crazy haul."

    show naomi happy apron at character_pos1 with dissolve
    vl naomi_vl_prefix 1
    n "This would’ve taken all day if I had to do it myself. Thank you, everyone."

    show gwynette neutral at character_pos3 with dissolve
    gw "I should be thanking you! Without you and Chuck, I don’t know what I’d do!"

    show charles neutral_scout
    a "You and Charles know each other? You said this is all because he offered you some help, right?"
    gw "That’s right! We met in the chapel my first year. Been pals ever since."
    a "You’re religious, Charles?"
    "He places a hand on his cheek. He’s had a tattoo there the entire time we’ve known each other. I never asked any questions about it, but I haven’t heard anything about Reina giving him grief, either."
    cha "Animist. I just thought it would be interesting to see how the other side lived. So I pop in from time to time. I’ve met a lot of good folks there."

    hide naomi with dissolve
    show vince neutral at left with dissolve
    vin "I’m surprised none of them have tried converting you yet."
    "Gwynette huffs and crosses her arms."
    gw "Anyone is welcome, regardless of faith or lack thereof. Or do you want to remind me of all the times you were turned away at the door, VV?"

    vl vince_vl_prefix 6
    vin "None, but I don’t show up nearly as much as he does."

    hide vince with dissolve
    show naomi neutral apron at character_pos1 with dissolve
    vl naomi_vl_prefix 4
    n "Wouldn’t it be bad that Charles visits more when you, you know..."
    cha "It’s probably best if we don’t poke that bear."
    "A very awkward silence falls between all of us. I latch onto the first thing that comes to mind to try and lighten t he mood."
    a "So! Gwynette calls you \"Chuck.\""
    cha "It’s stupid and funny, so I like it."
    gw "And him having such good taste is why we’re friends."

    hide naomi with dissolve
    hide gwynette with dissolve
    hide charles with dissolve

    "When the baking finishes, the more responsible among us hold back everyone who’s drooling over the cookies while they rest. As a reward for our hard work, Naomi allows us a celebratory cookie once she deems they were well and truly done."
    "With a round of \"CHEERS!\" we all take a hearty bite. The next moment, the room is hit with a wave of satisfied groans. Mission accomplished."
    "Before the cookies can be devoured, Charles and Naomi start everyone on a new task: the Scouts would clean up, and their supervisors store the cookies for tomorrow’s sale."

    scene black with fade
    #TODO: Update with correct timeline
    call student_council_dyalt("Dyalt", 26) from _call_student_council_dyalt_6

label scouts_route_neralt(month, date):
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Charles/Month 5/Killian_Charles_M5_"
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Charles/Month 5/Lucas_Charles_M5_"

    #"INT. HOUSE LYCHESTER - COMMON ROOM - NIGHT"
    scene bg dorm_common_night with fade

    $ renpy.notify("Charles - \nNeralt, 1027 RD")

    "It’s normal for people to gather in the House Lychester common room on Nyday nights to hang out with friends or play games."
    "Sometimes people choose to go out, instead of staying in to be full of energy to spend frolicking about in Huntsdale or Ferenicia on Lenday."
    "Charles asked me to hang out with him a few weeks ago, but even now that the time has come, he’s never explained what we were doing."

    show charles excited at center with dissolve
    cha "It’s going to be a ton of fun. Just trust me."
    show charles neutral

    "That’s all he’d ever say."
    "So I’m not all that surprised when he leads me out into town. The closer we get to the school, however..."
    
    #"EXT. MAGIS HALL - CONTINUOUS"
    scene bg maincastle_night with dissolve

    a "What in the Abyss is going on?"

    show charles excited at center with dissolve
    cha "Just trust me."
    a "Right now that smile of yours is anything but trustworthy..."
    "He walks up to the doors of the school, which should be locked."
    "He pushes them open."
    a "I’m supposed to trust you right now? I feel like I’m being led to my death."

    show charles neutral
    cha "I’m not that cruel. Come on."

    "He waltzes in, as if we weren’t trespassing. Resigning myself to my fate, ready to toss him to the wolves if we run into a faculty member, I follow."
    "We head up to the third floor. My blood runs cold when we hear voices. I’m about to grab Charles and turn him around when I get a bit of a better listen. Those aren’t the voices of anyone working for the school. Too youthful for that."
    "Great, more hooligans like us."
    "Charles pushes into the room. I follow, if only to find out whatever it was he’s been plotting."

    #"INT. MAGIS HALL - ANIME & MANGA ASSOCIATION CLASSROOM - CONTINUOUS"
    scene bg classroom_anime_night with dissolve

    show charles neutral at right with dissolve
    cha "Sorry to keep you guys waiting."

    show killian neutral at left with dissolve
    show lucas neutral at character_pos3 with dissolve

    "Killian and Lucas are waiting for us. A TV is set up, and there’s a case of energy drinks atop one of the desks."
    "Now it makes sense."
    a "You brought me here... to watch anime?"
    cha "Oho! Not just any anime!"
    "He takes a deep breath."
    cha "WE’RE WATCHING ANIME FOR LITTLE GIRLS!"
    a "What."

    show lucas annoyed
    vl lucas_vl_prefix 1
    l "I beg your pardon?"

    vl killian_vl_prefix 1
    k "\"Pretty Magica.\" Just one of the biggest franchises out there."

    vl lucas_vl_prefix 2
    l "A show for little girls...?"

    vl killian_vl_prefix 2
    k "Kids shows have motion, Lucas! The people who lead the world grew up watching these shows."
    voice sustain
    k "Their art is influenced by the art they consumed. And with how many people consumed it, its DNA is everywhere in entertainment."
    "Killian slams one of the desks."

    vl killian_vl_prefix 3
    k "Even the Empress loves the show!"
    "Having spoken to the woman’s son several times now, that’s a weird image to have put into my head."

    vl lucas_vl_prefix 3
    l "Well, I’d be remiss to chastise you for wanting to share a seminal work in a medium you love. But why’d you have to sneak us into the school like thieves in the night?"
    "On cue, Charles drops a bunch of film cases onto another one of the desks."
    a "Six of them. What are these? I thought this was some sort of TV show."
    "Charles clicks his tongue and wags his finger at me."
    cha "Please. We’d barely scratch the surface in just a night if we watched the proper show. So we’re watching compilation movies."
    
    vl killian_vl_prefix 4
    k "Two of the most popular seasons. Three films each."
    a "...And how long are these things?"

    show charles excited
    cha "Two hours a piece!"
    "I sink into the nearest chair. Lucas doesn’t look nearly as surprised."

    show lucas sad
    vl lucas_vl_prefix 4
    l "Well, that explains why you wanted me to bring energy drinks. And your scheme to sneak us into the school. Twelve hours of anime, huh?"

    vl killian_vl_prefix 5
    k "We didn’t \"sneak you in.\" Headmaster signed off on this."

    vl lucas_vl_prefix 5
    l "Of course he did."

    hide killian with dissolve
    hide lucas with dissolve
    hide charles with dissolve

    "Killian sets everything up for us. The last thing he does is hand me an energy drink. If my entire night is going to be spent watching television, it probably isn’t going to be my only one that night."
    "They started us on \"Pretty Magica Crystal.\" For one of the more popular seasons, I didn’t get the hype."
    "I wasn’t a child, but quality kids shows are supposed to have some gold under the surface for parents and older siblings. Instead I got a decent show about a bunch of boys and girls with powers fighting evil."
    "Then it was about the girls fighting evil. Halfway through, the boys became clowns. No real explanation for it, either. Guess the ratings were rough so they needed to switch gears."
    "And six hours later, I’m left very whelmed."

    show lucas tired at character_pos3 with dissolve
    vl lucas_vl_prefix 6
    l "That was one of the popular seasons?"

    show killian neutral at left with dissolve
    vl killian_vl_prefix 6
    k "Not when it came out. But it’ll make sense after this."
    a "After— Did you just make us watch six hours of set up?"

    show charles excited at right with dissolve
    cha "Without it, it’s not like the payoff would really hit, right? Now, onwards!"

    hide killian with dissolve
    hide lucas with dissolve
    hide charles with dissolve

    "\"Pretty Magica Black and White\" is set in the same city. Clearly a sequel of some sort. Probably because the back half of \"Crystal\" pissed people off. I wouldn’t blame them."
    "I thought Charles and Killian were full of it at first. Starting over with a new premise and cast took some time to get used to. Then the familiar names started getting dropped; the faces started to show up."
    "The studio must’ve been paying really close attention to the pulse of the fanbase when they were making this one."
    "There’s as much fanservice as there is new material, but it’s clear they were aiming to deliver more of what the people loved and make up for all of their screw ups."
    "The \"Crystal\" boys most of all."
    "The show was super heavy on friendship. But complex, adult friendships got nearly as much focus as the innocent, foundational relationships of youth, with the returning cast spending a lot of time learning how to reconnect after years apart."
    
    #"INT. MAGIS HALL - ANIME & MANGA ASSOCIATION CLASSROOM - MORNING"
    scene bg classroom_anime_noon with fade

    "A good eleven in, we’re on the final movie. Things are heating up. A big twist saw one of the \"Crystal\" boys come back as a villain. Then, during a lull in the finale, the protagonist of \"Crystal\" says this:"
    "\"We made so many fun memories together when we were kids. I’d love to get a chance to make more of them with you. I know we can, too, even after all of this. My friend’s still in there; I know you’re still a good person deep down. This isn’t black and white.\""
    "I latch onto Charles, who wraps an arm around my shoulder in kind."
    a "She said it! She said the thing!"

    show charles excited at right with dissolve
    cha "Roll credits!"
    hide charles with dissolve

    "\"...We can fix it, go back to how we were—even though it might not be exactly the same—and continue this journey through life side by side, hand in hand."
    "\"So, Hikaru, what do you say? Are you willing to give it another go?\""
    "The movie—\"Pretty Magica Black and White\" as a whole—ends on a hopeful note. But a damn good one too."
    "During the credits (and the beautiful song that accompanied them), we sat in a cathartic silence, letting the workday-and-a-half of content we binged sink in. If I was a kid when I watched these?"
    "I could see myself getting hooked on something like this."

    show lucas neutral at character_pos3 with dissolve
    vl lucas_vl_prefix 7
    l "It makes a bit more sense to me now."

    show killian neutral at left with dissolve
    vl killian_vl_prefix 7
    k "There’s a lot of good stuff they needed to cut for the movies, too. Even better if you watch the show."
    a "But how long would that take? I think I’m all \"twelve hour marathon\"’d out for the next few years."

    show charles neutral at right with dissolve
    cha "We’ve got the rest of the year. That’s plenty of time."
    "Charles stands up from his seat, wobbling a bit as he does."
    cha "Welp, the sun’s up and it’s only a matter of time until the caffeine crash hits, so I think I’m going to head back. Thanks for the watchalong, everyone. It was a fun time."

    vl lucas_vl_prefix 8
    l "Killian’s recommended anime to me before. After this I think I’m going to have to watch a few."

    show killian sad
    vl killian_vl_prefix 8
    k "Wait, you’ve been ignoring my recommendations?!"

    #"EXT. HUNTSDALE - MAIN STREET - CONTINUOUS"
    scene bg mainstreet_late_naming with dissolve

    "We leave after tidying up our cans. Charles and I lean on each other as we walk back to House Lychester, barely clinging onto consciousness despite the liquid caffeine sloshing around inside of us."
    "There’s something oddly appropriate about it. After six movies of the power of friendship being beamed into my brain, I can appreciate the small gesture of helping an exhausted friend walk a lot more than I would’ve just yesterday afternoon."

    scene black with fade
    # TODO: Update with correct timeline
    $ renpy.call(chosen_club2 + "_route_neralt", "Neralt", 16)

label scouts_route_exalt(month, date):
    #"EXT. HUNTSDALE - MAIN STREET - NIGHT"
    scene bg mainstreet_night with fade

    $ renpy.notify("Charles - \nExalt, 1027 RD")

    "The final Student Council meeting of 1027 has finally wrapped up. It isn’t like much happened, though. A good chunk of the council left as soon as school let out to get home for the Week of Life."
    "There’s been a gentle snowfall all day, so by this point, it’s accumulated a fair bit. Nothing so substantial that plows have needed to come by, so much of the ground is covered with a white blanket."
    "I’m most of the way to House Lychester when something catches my eye, stopping me in my tracks. There’s an odd white lump on the ground ahead of me. A very large lump."
    "Hold on..."
    "That’s no lump."
    "I sprint through the snow to the person who’s collapsed in the snow and drop to my knees."
    a "Hey, are you alright?!"

    show charles contemplative_scout at center with dissolve
    "I help them sit up. It’s Charles, and he’s freezing. Shit. The maneuvering is awkward, but I’m eventually able to get Charles onto my back. How in the Abyss did he find himself in this situation anyway?"

    #"INT. HOUSE LYCHESTER - COMMON ROOM - CONTINUOUS"
    scene bg dorm_common_night with dissolve

    show charles contemplative_scout at center with dissolve
    "Charles sits in front of the fireplace in the common room, cradling a mug of hot chocolate, a thick blanket draped around his shoulders. The school’s head nurse just left, making sure that Charles wasn’t struck with a case of hypothermia or anything."
    "He said it was a close call, but as long as Charles stays inside and warm today, he should be fine. I pull a seat up next to him."
    a "You doing alright?"

    show charles neutral_scout
    cha "The chocolate’s good, at least. Think I should be fine."
    "An awkward, almost uncomfortable, silence falls between us as Charles takes a few sips of his drink."
    a "What happened out there?"
    cha "Guess I was just tired."
    a "So tired you collapsed? In winter? What could’ve drained you that much?"

    show charles contemplative_scout
    cha "Let’s see... I helped Gwynette and the chapel prepare for the Week of Life. I’ve been helping one of the Scouts prep for tertiary school entrance exams. I’ve been helping out at an old folk’s home lately."
    cha "There was the winter foraging thing we did with the kids. On my way here tonight, I’d just come from showing someone to the other side of town since they were lost."
    a "You’ve had a busy week. Please don’t tell me that’s what your normal has been..."

    show charles neutral_scout
    "My question is met with another sip of the hot chocolate by Charles."
    a "Don’t ignore me! It’s good that you’ve been helping people, but you can’t push yourself so hard that it makes you drop in the street, Charles."
    "He ignores me again. You’ve got to be kidding me."
    a "Say something. You’re not a kid. You know better than to ignore me because you don’t like what you’re hearing."
    cha "Sorry. But I can’t stop."
    a "And what in the Abyss does that mean?"
    cha "Someone had to help those people. So I did. There are going to be more people that need help. So I will."
    a "Paying it forward again?"

    show charles excited_scout
    "He lets out a little lifeless laugh."
    cha "That obvious, huh?"
    a "I wouldn’t really say obvious. But it is very you."

    show charles neutral_scout
    cha "Well. You’re right. If my Scoutmaster didn’t help me, who would have? Where would I be without her? I don’t want anyone else to be left hanging because I saw them reaching out and didn’t give them a hand."
    a "That is also very you. But it’s okay to slow down."

    show charles contemplative_scout
    "He shoots me a disapproving look. Apparently he thinks I’m just ignoring him."
    a "I know, I know. \"Who’s going to help people if it’s not me?\" Didn’t you ever think about your Scouts?"
    a "You’ve been helping them. They’ve been seeing you want to help other people. The good example of what to do when they see people in need is there."
    a "You wanted to pay it forward, and you have been. Your Scoutmaster was one person, and now how many people have you impacted over the years? And how many people are they going to help?"
    a "If you want to honor her in some way, you don’t have to be the only person carrying that weight."
    "Again, a silence falls between us. One sip at a time, Charles works through his hot chocolate. I keep quiet. I’ve said my piece. And just having someone sit with him is probably what Charles needs right now."
    cha "I hate to say it... but you’re right."
    "Finished with his drink, Charles sets the mug on a nearby side table. Leaning back in his chair, Charles wraps his blanket around himself more tightly."

    show charles neutral_scout
    cha "Thanks for that. I never thought about things that way. I let the kids down, having such little faith in them."
    cha "I’m not going to be able to see them tomorrow, I don’t think. You’ll be able to handle things on your own?"
    a "After all this time? It’ll be easy. You focus on taking it easy, okay?"
    cha "And please, tell them to not make the same mistake I did."
    a "I make no promises. They’ll probably be better off hearing that from you."
    "I rise from my seat, slinging my bag over my shoulder."
    a "Need any help getting to your room?"
    cha "I’m going to hang out for a bit longer. But I should be able to manage that on my own after letting my body warm up some more."
    hide charles with dissolve

    "It does worry me to leave him all by his lonesome. Even if he said he sees what I was trying to say, it would take more than just a few minutes for it to really sink in."
    "And the other side of the coin that is \"help people until the point of collapse\" probably would be \"never ask for help to avoid being a burden.\""
    "But, as I head up the stairs, I decide to have faith in Charles. Whatever he needs to do, whoever he needs to call, he’ll do it if getting to his room isn’t something he can do on his strength alone."

    scene black with fade
    #TODO: Update with correct timeline
    if chosen_club2 == "enseki":
        call enseki_route_exalt2("Exalt", 22) from _call_enseki_route_exalt2_4
    else:
        call phillip_elvera("Exalt", 22) from _call_phillip_elvera_7

label scouts_route_elvera(month, date):
    $ sue_vl_prefix = "audio/voices/Love Interests/Sue/Charles/Month 7/Sue_Charles_M7_"
    $ phillip_vl_prefix = "audio/voices/Supporting-Extra/Phillip/Charles/Month 7/Phillip_Charles_M7_"

    #"INT. WILSON BUILDING - SALON - AFTERNOON"
    scene bg wilson_salon_afternoon with fade

    $ renpy.notify("Charles - \nElvera, 1028 RD")

    "It’s been about two weeks since I found Charles in the snow. From what I’m able to see, he has been serious about being easier on himself."
    "He’s been antsy about missing people out there who need help, but I’ve seen him muttering to himself lately. He’s told me that when he does that, he’s reminding himself of the fact that there are good people out there helping where he isn’t able to."
    "It’s a weekend afternoon, and the two of us are heading to the salon on the third floor of the Wilson Building. We planned to meet up with Sue, but when we get there, she’s nowhere to be seen."

    a "Guess we’re a bit early."

    show charles neutral at right with dissolve
    "Charles nudges me with his elbow."
    cha "Hey, look who it is."
    "He points out Prince Phillip, who’s enjoying some tea by a window."
    a "Do you know the prince, too?"
    cha "I get to say hi every now and then. Like right now."
    "Then he saunters over to the table."
    cha "Hey there, prince. Good to see you."

    show phillip neutral at character_pos2 with dissolve
    vl phillip_vl_prefix 1
    p "Ah, Charles. It’s been a while. And it’s good to see you too, Blakesley."
    a "Hope we weren’t bothering you."

    vl phillip_vl_prefix 2
    p "I was just about to leave, actually, so your timing is quite nice. Only a few minutes from missing each other."
    cha "You spoke to Sue a few months ago about something, right?"

    vl phillip_vl_prefix 3
    p "I did. I’m surprised she told you."
    cha "If it helps you keep your word to her, I might be able to reach out to someone I know in Otren and pass along their contact info."

    vl phillip_vl_prefix 4
    p "Okay..."
    cha "Might take a while until I hear from them, though. Oh, well. If it’s after graduation, I’ll just forward the info to the palace."

    vl phillip_vl_prefix 5
    p "What palace contacts could you have? Wait, that’s not important. What was that about knowing someone in Otren? You don’t really mean someone who could help Sue, do you?"
    cha "That’s the hope, anyway."

    vl phillip_vl_prefix 6
    p "But you knowing someone who actually has that sort of sway... How?"
    cha "We Scouts are all over the world. I don’t know much about the Otren branch, but it definitely exists."

    show phillip contemplative
    vl phillip_vl_prefix 7
    p "But still. What you’re saying is—"
    "The prince suddenly huffs and shakes his head."
    show phillip neutral
    vl phillip_vl_prefix 8
    p  "If you’re able to reach out to someone, the help would be appreciated, thank you."
    cha "Don’t mention it."

    hide phillip with dissolve
    "With a brief, cordial farewell, the prince leaves. Charles assumes a seat nearby, completely unbothered by how surprised the prince was. I don’t even understand what they were saying, but for him to be so shocked, it must’ve been a huge deal."
    a "So what was that?"
    cha "Don’t worry about it. Spirits willing, it’s not a favor I’ll have to call in."
    a "That just leaves me with more questions."
    "But before I’m able to ask any of them, Sue crests the top stair and calls out to us."

    show sue neutral at character_pos2 with dissolve
    vl sue_vl_prefix 1
    s "There you two are. I hope you weren’t waiting too long."
    a "Just got here ourselves. You’re good."
    "We put in some orders for drinks and snacks, chatting about how the start of the new year has been while we wait. Only once the food is here do I find out why we were even invited in the first place."

    vl sue_vl_prefix 2
    s "Animist New Year is next month. Celebrations are going to be held all over Ferenicia."
    cha "Going to be the last time we get to go through one of those parties. Man, I’m going to miss them..."
    a "You two go together?"

    vl sue_vl_prefix 3
    s "Yes! It’s a little tradition of ours to go every year."
    a "So like a date?"
    "The two of them look at me like I’m crazy. Then they turn to each other. The prolonged moment of stillness is broken just as suddenly when they both spin away from the other and begin to gag."

    vl sue_vl_prefix 4
    s "Wei’s like my brother. I could never imagine going on a date with him!"
    cha "Exactly! Just the thought is enough to give me chills..."
    "I’m not sure if I should feel sorry for them or glad the disgust was mutual..."

    vl sue_vl_prefix 5
    s "Ahem! I was wondering if you might want to join Wei and I on that day?"
    a "I can definitely try. When is it?"

    vl sue_vl_prefix 6
    s "It’ll be Nyday, Verabris 21st."
    a "That’s some bad luck. I actually made plans with a friend. We’re going to catch a movie that comes out that day."

    vl sue_vl_prefix 7
    s "Blowing us off for a movie? How rude!"
    a "I know, but if I tried to ditch them on opening day, they’d kill me."
    cha "How about this? We make a promise"
    "He thrusts a fist out over our table."
    cha "One of these years, the three of us’ll be able to tear up the streets of Ferenicia during Animist New Year, good and proper."
    a "I like the sound of that."

    vl sue_vl_prefix 8
    s "That does sound nice. We could invite Naomi and Reina, too."
    "We all bump fists. Then I blink, and my vision is blurry. Ah, that makes sense. I had no idea if I’ll see any of the people I met here after graduation. But here I am, making a promise to spend New Year’s with some of them one day."

    vl sue_vl_prefix 9
    s "Whoa! Are you okay?"
    "I dab away the tears."
    a "I’m fine. Just... really looking forward to when we get that chance."
    "Maybe it’ll be next year. Maybe it’ll be in ten. But whatever small part of me was worried about graduation day being a final goodbye to all of the people I’ve met has been able to calm down, if only a little bit."

    scene black with fade

    call scouts_route_verabris("Elvera", 22) from _call_scouts_route_verabris

label scouts_route_verabris(month, date):
    $ arline_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Arline/Charles/Month 8/Arline_Charles_M8_"
    
    #"INT. HOUSE LYCHESTER - COMMON ROOM - EVENING"
    scene bg dorm_common_night with fade

    $ renpy.notify("Charles - \nVerabris, 1028 RD")

    "I stare at Mother’s contact in my phone. My time here at MIA is almost up. I’m satisfied with the education I’ve gotten, and I’m hopeful that whatever job I’m able to get will help House Blakesley in some way."
    "But it’s not the silver bullet Mother was expecting. And I doubt I’m going to find it before graduation. It’s been nagging at me of late, what might happen if I don’t. What it might do to Mother if her husband’s family loses its status on her watch."
    "Taking a deep breath, I initiate the call, and prepare myself to share what I've been contemplating these past few months with the woman who needs to hear it most."
    "Each of the dial tones I have to sit through spikes my anxiety. Then, I finally hear Mother’s voice."

    vl arline_vl_prefix 1
    arline "Hi, dear. I wasn’t expecting you to call so late. How have you been?"
    a "Oh, you know... I’ve been okay. Just trying to stay on top of things, the closer we get to finals."

    vl arline_vl_prefix 2
    arline "Well, you sound like something’s wrong. It’s okay. You can tell me."
    "I should’ve known it would be useless trying to lie to her. Of course the woman who’s known me my entire life would see right through me."
    "I take another breath."
    a "Do you think it’s really necessary, Mother? Everything we’ve been trying to do this past year, I mean."

    vl arline_vl_prefix 3
    arline "To save House Blakesley?"
    a "Yes. That. It could do more harm than good to worry so much in the long run."

    vl arline_vl_prefix 4
    arline "...Go on."
    "I tell her about what’s been eating away at me. About my concerns not only for myself, but her, Salem, and Skylar."
    "If not for the occasional sound to let me know she was still there, I’d probably be freaking out about the call having somehow dropped."
    a "None of us asked to have the future of an entire lineage placed on our shoulders. It’s exhausting, isn’t it?"

    vl arline_vl_prefix 5
    arline "Exhausting, yes. But it’s our duty. This goes far beyond just us. Our family has a long history. And we can’t sacrifice its future when we have a chance to save it."
    a "That’s House Blakesley. But the Blakesley family? That lives on as long as we do. Just like how it existed before the first one of us even got the name."
    a "We don’t need the title or the property to find love, have kids, any of that. Keeping the House alive shouldn’t mean risking our family."
    "There’s a long moment of silence on the other end. Then, finally, she sighs."

    vl arline_vl_prefix 6
    arline "You do have a point. And I can only imagine that your Father would agree."
    a "You do?"

    vl arline_vl_prefix 7
    arline "If he had to pick between no title or no family, he’d sacrifice the title in a heartbeat. I’ve been treating them as one and the same..."
    a "What’ll we do now, then?"

    vl arline_vl_prefix 8
    arline "Our best, I suppose. Try to hold onto the title if we can. But if we can’t, we can’t. And just live our lives as commoners with our heads held high."

    vl arline_vl_prefix 9
    arline "There are some plans I’ll need to change around, but we can talk when you’re home. Thank you for giving me some things to think on, dear."
    "Hearing her thanks lifts a weight off of my shoulders. I feel lighter than I did when the night began."
    "We talk for a little bit longer, catching each other up on everything that’s happened since I started at MIA last spring. Mother hangs up when it’s time for dinner, and that’s my cue to go on a walk."
    "I think a bit of time outside would do me some good."

    #"EXT. HUNTSDALE - MAIN STREET - CONTINUOUS"
    scene bg mainstreet_night with fade

    "It’s a temperate spring evening, ideal for a walk. My life was turned upside down when Mother said that we were in danger of running out of money and losing our viscounty. This time, I’m the one to have turned both of our lives upside down."
    "There’s a big difference between then and now. The stakes were clear, then. Success meant continuing as we always had, and failure meant ruin. Now, success and ruin are practically one and the same, and the future is a giant black shroud of unknowns."

    show charles neutral at center with dissolve
    cha "Going somewhere?"
    "I was wandering aimlessly, barely paying attention to my surroundings. I jump when I hear Charles, but he’s right in front of me, heading the way I came. My skittishness earns me a raised eyebrow."
    a "Sorry, was just getting some fresh aer. I was lost in thought."
    cha "Clearly. Everything alright?"
    a "I hope it will be, anyway."
    "I give him a brief rundown of the talk I had with Mother. After all, he’s a big part of why I decided to make that plunge."
    cha "That is a lot to have on your mind."
    a "I know, right?"
    cha "Mind if I join you?"
    a "You’re heading back to House Lychester, aren’t you?"
    cha "Yeah, but a detour won’t kill me."
    a "Weren’t you just on your way back from a \"detour\" when you fell into the snow?"
    cha "Hey, I was in helper mode back then. This is friend mode."
    a "Those two are very similar, you know."
    cha "Ah-ah! Similar, but not the same. I’m walking with you for a bit. Don’t worry, I’ll take it easy."
    a "You’d better."
    "Charles turns on his heel and follows me as I continue to walk to nowhere in particular. As much as I wanted to chide him for sticking his neck out for me like that, I appreciate the gesture too much to be bothered by it."
    "Even though we walk in utter silence, just having someone at my side as I contemplate whatever this new course in life might have in store for me and my family turns out to be exactly what I needed."

    scene black with fade

    $ renpy.call(chosen_club2 + "_route_verabris", "Verabris", 9)

label scouts_route_overa(month, date):
    #"EXT. MAGIS HALL - AFTERNOON"
    scene bg maincastle with fade

    $ renpy.notify("Charles - \nOvera, 1028 RD")

    show charles neutral_scout at center with dissolve
    cha "So are you going to tell me what’s going on?"
    "Charles’s time as Scoutmaster officially ended over the weekend, but I’ve hauled him onto campus, again in our Scout uniforms. When he asked me what was going on I said: \"Just trust me.\""
    "He rolled his eyes at that."
    "Only a few days remain until graduation. We’d say goodbye by week’s end. Goodbyes like that were just a part of life, but still bittersweet."
    "But there’s no use crying when I could just be glad about the fact that I got to meet these people in the first place."
    cha "Going onto the field? I remember that camping trial we had here. Poor Kloe—"

    #"EXT. WRIGHT GYMNASIUM - CONTINUOUS"
    scene bg wright_field_afternoon with dissolve

    show charles neutral_scout at center with dissolve
    "When we enter the field, we’re met with a round of cheers and streamers of confetti shot at us by readied party poppers."

    show charles excited_scout
    cha "Whoa!"
    "I leave a stunned Charles to join his Scout troop. Standing side by side, clad in their uniforms, I call them to attention, and all of the children stand straight as an arrow."
    a "Scoutmaster Charles Liang Ren Wei. For three eventful years, you’ve guided these promising young souls through the tumultuous journey of life."
    a "Now, as your path diverges from theirs, and your time amongst them comes to an end, there are some things they wanted to tell you."
    a "SALUTE!"
    "As one, we all give Charles the crispest salutes we can muster. Then, with varied energy, varied volume, and in varied levels of emotional distress, we all shout:"
    a "CONGRATS ON GRADUATING! THANK YOU FOR EVERYTHING, CHARLES!"
    "Some kids call him \"Scoutmaster,\" others \"Charlie,\" or \"Chuck,\" and others still \"Wei.\" I hear a few other special nicknames he’d amassed over the years sprinkled in, too."
    "Still frozen, Charles stares at us, slackjawed. With a small urging from me, the kids rush him, clamoring to say their final goodbyes."
    "It doesn’t take long for the tears to flow as Charles is overcome by the weight of the appreciation his Scouts unleash upon him."
    "It’s not until the sun starts to set that they’re finally done saying goodbye to their beloved Scoutmaster. After a final round of tearful goodbyes, they head off into the sunset, the seniors among them promising to see their peers home safely."

    show charles neutral_scout
    cha "How’d you pull that off?"
    a "Told them that it would be a nice surprise: say goodbye after the \"last time\" so you wouldn’t see it coming."
    cha "It really is setting in that it’s so close to goodbye."
    a "Really snuck up on us, didn’t it?"
    cha "It did. As good a time as any for story time."
    a "Story time?"
    cha "We’ve known each other all year, but I don’t talk about myself much, right?"
    "He’s right. I’m familiar with how friendly he is and how he likes to help people. I’ve seen him gush about his favorite hobbies. Ever since Exalt, I’ve seen him a bit more relaxed and almost contemplative."
    "But through all of that, I barely know anything about him outside of school and the Scouts."
    a "Well, if you don’t mind sharing..."
    cha "Of course I don’t. After all these months?"
    "Charles leads me over to a tree on the field. We take a seat on the grass before he begins to speak."

    show charles contemplative_scout
    cha "My grandfather’s from Otren. Committed some sort of small white collar crime. He never told me what it was."
    "His hand drifts up to his tattoo, brushing it lightly."
    cha "Didn’t get any jail time. Just thrown out of the country. Because of this."
    a "What?"
    cha "To make a very long, messy story short: people with Aer Cortex Deficiency Syndrome like him aren’t treated the best over there. Whatever he did was an easy excuse for the government to get rid of him."
    cha "But he still loved his home, despite what it did to him. I think the exile made him even more intense. I was born and raised here. I’m as Magianan as you are. But if you looked in my house growing up, you’d never guess it."
    cha "Language, food, celebrations, etiquette, every aspect of life crafted to perfectly emulate Otren."
    cha "My parents named me \"Charles,\" but saying the name would make him sick. I say something in Oslenite, the look he’d give me damn near drove me to tears."
    cha "Made me feel like a stranger in the land of my birth. Surrounded by kids who I should relate to on so many things, always feeling like a stranger because he always told me I was."
    a "Charles... I’m sorry."

    show charles neutral_scout
    cha "What’re you apologizing for? It’s not like you did anything."
    a "Maybe not, but..."
    "He waves a hand, dismissing whatever pity party I was about to have."
    cha "You already know how this story ends. It’s not like it’s some tragedy."
    a "Your old Scoutmaster, right?"
    "He nods, leaning back on his hands and looking up at the brilliant carnelian sky as the sun continues its march towards the horizon."

    show charles contemplative_scout
    cha "The family only ever called me \"Wei,\" but outside the home I didn’t let anyone use that name for me. I couldn’t stand it. I was \"Charles Liang\" and nothing else."
    cha "When I was away from them, that was a small way I could try to grasp for a sense of self; something I wanted, instead of something decided for me."
    cha "I joined the Scouts during primary school. It took some time, but my Scoutmaster saved me. Grandfather made me think I was an Otrenite exile living in a strange land. I felt like I didn’t belong in the only home I’d ever known because of it."
    cha "Shit, when I was an angsty preteen, I started to hate being Otrenite because it was pushed so hard at home. I thought of everything about the place as a mark of familial tyranny instead of an important part of who I am."
    a "Your grandfather would say \"This is who you are,\" and you’d say \"No, grandpa, this is who I want to be\"? Something like that?"
    cha "If only. That would mean I knew who I wanted to be then. I didn’t have a damn clue. Was I Magianan? Or was I Otrenite? My Scoutmaster told me that the answer was \"yes.\""
    cha "To my family, I was \"Liang Ren Wei.\" To everyone else, I was \"Charles Liang.\" Which one was the real me? She told me I didn’t have to choose. That I could be both."
    a "And thus was born Charles Liang Ren Wei."

    show charles neutral_scout
    cha "You got it. \"Charles\" and \"Wei\" are both my names, so now I don’t care which one people call me by. They’re both right."
    "Charles stands up, leaning against the tree."
    cha "Thank you. For Exalt. That’s the second time someone’s really pulled my ass out of the fire."
    a "That’s not anything to thank me for. That was just me being a good friend."
    "I join him on my feet, giving him a light punch to the shoulder."
    a "Trying to save you from yourself when you make a stupid mistake."

    if player_gender == "female":
        jump scouts_route_overa_romance
    else:
        $ charles_platonic = True
        jump scouts_route_overa_platonic

label scouts_route_overa_romance:
    "Pushing himself off the tree, Charles takes a breath. Then he levels an uncharacteristically serious look at me. It freaks me out."
    cha "I’m not going to beat around the bush. I want you to be my girlfriend."
    "Wh-WHAT?!"
    cha "I know the timing’s garbage, with graduation right around the corner. But I can’t let you walk out of my life without saying anything."
    cha "I’m not sure how to put it, but... you make me feel seen in a way I haven’t felt in ages."
    cha "So... when we leave in a few days, I don’t want it to be the end of something, but a new beginning."
    
    menu:
        "A new beginning? That sounds nice.":
            $ charles_romance = True
            jump scouts_route_overa_romance_accept
        "It’ll be a new beginning... But not the one you want.":
            $ charles_romance = False
            jump scouts_route_overa_romance_reject

label scouts_route_overa_romance_accept:
    a "A new beginning? That sounds nice."
    cha "Huh?"
    "I can’t help but laugh at that."
    a "You’re the one that asked me out! Didn’t think you’d get this far—?!"
    "The next thing I know, Charles scoops me up under my arms and twirls me around under the tree. Barely a moment after he’s set me down, my head still spinning, he’s peppering my cheeks with kisses. That just gets me to laugh even harder."
    a "Down, boy, down!"
    cha "Sorry! I guess I didn’t think I’d get this far. You caught me off guard."
    jump scouts_route_overa_platonic

label scouts_route_overa_romance_reject:
    a "It’ll be a new beginning... But not the one you want."
    "His shoulders slump, and his expression softens. I can tell he’s disappointed, but his feelings don’t seem hurt. At least not too much."
    a "It just feels like too big a decision to force in only a few days, I’m sorry. But things will be different on the other side of graduation."
    a "I don’t know how our friendship will change when we can’t hang out all the time, but the end of this isn’t the end of everything, right?"
    cha "You’re right. We’ve been good friends, and we can keep on, even after we’re gone here. But Spirits above, it was nice to get that off my chest."
    jump scouts_route_overa_platonic

label scouts_route_overa_platonic:
    cha "Hey."
    a "What’s up?"
    "Turning his eyes towards the ground, Charles goes red. Now what could this be about? It isn’t like him to get embarrassed."
    cha "\"Wei\" is something reserved for people real close to me. Like Sue and the rest of my family. If you want..."
    "I give him a hearty slap on the back. It’s pretty cute to see him get this hung up over something so simple."
    a "Okay, Wei."
    cha "That’s going to take getting used to."
    a "You’re the one that wanted this!"
    cha "I know, I know. So, how about dinner? I need some food in me after this."
    a "Sign me up. And you know what? It’ll be my treat."

    show charles excited_scout
    cha "Careful now. I just might make you regret that!"
    "We playfully jostle each other on the way out of the field, heading into Huntsdale, an arm wrapped around each other’s shoulder. This is one of the last days we’ll be able to do things like this for a while. Best to make the most of it while we can."

    scene black with fade

    #TODO: Update with correct timeline
    call epilogue_graduation("Overa", 24) from _call_epilogue_graduation_15

label epilogue_scouts_route:
    # TODO: FADE IN: SOUNDTRACK 17

    #EXT. MAGIS HALL - CONTINUOUS
    scene bg maincastle_noon with fade

    if chosen_club == "scouts":

        show charles excited at center with dissolve
        cha "Well, look who it is!"

        "An arm is suddenly thrown around my shoulder, and I’m met with Charles’s familiar grin. I shake him off."

        a "Fancy seeing you here. You come here often?"

        cha "Well, this is the third time I’m graduating from somewhere, so maybe."

        "We share a laugh at our attempts at \"jokes.\""

        if charles_platonic:
            jump epilogue_scouts_route_platonic
        elif charles_romance:
            jump epilogue_scouts_route_romance_accept
        else:
            jump epilogue_scouts_route_romance_reject

    else:
        jump epilogue_scouts_route_not_chosen

label epilogue_scouts_route_romance_accept:
    show charles neutral
    cha "So, it’s finally over."

    a "This chapter is over. And another one’s just begun, right?"

    "A rapidly reddening Charles rubs his neck and turns away from me."

    cha "Yeah, I guess it has."

    a "I remember you being the one pulling out the flowery wording. Are you really embarrassed having it thrown back at you?"

    cha "Apparently… But it’s pretty exciting too, right?"

    a "Very. So, what’s in store next for you, Wei?"

    cha "Taking a gap year to help the Scouts around Unios. Not too sure about after that, but we’ll see. You headed back home?"

    a "For now, anyway. But I’ll probably be in Prospera for a while."

    cha "Well, I have a whole year to figure out what I want to do. I know there’s a university or two in Prospera, so maybe…"

    "I roll my eyes at that."

    a "Please don’t pick a school just as an excuse to be in my city. That’s a big deal."

    cha "I know. But it’ll be nice if it turns out to be a good match."

    a "It  would be, yeah."

    cha "Were you up to something when I found you?"

    a "Trying to find my mother and siblings."

    cha "I’ll leave you to it then. Who knows, maybe I’ll get to meet them before heading out of Huntsdale."

    a "We’ll have to see about that. Bye, Wei."

    cha "Goodbye, [a]."

    show scene black with fade
    jump reuinion

label epilogue_scouts_route_romance_reject:
    show charles neutral
    cha "Oh, yeah. I’m going to be having a reunion next year."

    a "You are?"

    cha "Yeah. Five year reunion for my old Scout troop back home. Want an invite?"

    a "I’d be able to go?"

    cha "We get a plus one. And as an honorary Scout, I think it’s only right you get in on the action, you know?"

    a "I guess, but then I’d be like a fraud, wouldn’t I?"

    cha "A Scout’s a Scout, no matter when they join. You’ll be fine. The guys and gals are chill, trust me."

    a "Sounds like it could be a good time. Count me in."

    cha "And you have a year to brush up on your secret Scout handshakes, too. We’re going to have a lot of ground to cover. Remotely. Somehow."

    a "When there's a will, there’s a way, right?"

    cha "How’d you know there was a Will in my troop?!"

    a "Gods, that was bad!"

    cha "Couldn’t help myself. I’ve got to go, but we’ll catch up soon, yeah?"

    a "Sounds like a plan. Be seeing you around, Charles."

    show scene black with fade
    jump reuinion

label epilogue_scouts_route_platonic:
    show charles neutral
    cha "Hold on a second!"

    a "What’s up?"

    cha "You’re from Prospera, right? There are some pretty good camping spots near that city."

    a "And I am very much a city boy."

    cha "One who’s gone camping before!"

    a "Once before."

    cha "Better than nothing. Come on, summer’s right around the corner, and your own backyard’s the perfect place to go. What’s a better way to celebrate our newfound freedom than to live off the land for a few days?"

    a "I can think of several things."

    cha "Just give it some thought. I’ll probably be in Prospera in the next few months to hang out. Maybe we can steal away to the woods for a weekend."

    a "Maybe I’ll come around to the idea by then. We’ll see."

    cha "I guess we will. I’ve got to jet, so talk to you later, right?"

    a "Until next time."

    show scene black with fade
    jump reuinion

label epilogue_scouts_route_not_chosen:
    show charles neutral at center with dissolve
    cha "Hey there. You’re Sue’s friend, right?"

    a "That’s right. You are too, aren’t you? Charles? Or was it Wei?"

    cha "Yes."

    a "How helpful."

    cha "Congrats on making it through the other end."

    a "You too. I’m sure you were busy with your Scout stuff, too."

    cha "I definitely was. Maybe I’ll see you around one of these days. Until next time."

    show scene black with fade
    jump reuinion

label reuinion_scouts_route:
    $ arline_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Arline/Epilogue/Meet Charles/Arline_Epilogue_MeetTheFamily_Charles_"
    $ salem_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Salem/Meeting Charles/Salem_Epilogue_MeetTheFamily_Charles_"
    $ skylar_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Skylar/Meet Charles/Skylar_Epilogue_MeetTheFamily_Charles_"

    show charles neutral at center with dissolve
    "When Charles arrives, he gives the rest of the family a friendly salute."

    cha "Charles Liang Ren Wei. It’s a pleasure to meet you all."

    vl arline_vl_prefix 1
    arline "Arline Blakesley. The pleasure is all mine. Charles, correct?"

    cha "Yes. Or “Wei,” if you’d prefer. Either one works."

    vl salem_vl_prefix 1
    salem "Name’s Salem. Mother told us a little bit she’s heard about you from our sister. You were a Scout?"

    cha "Huntsdale Scoutmaster. The organization’s super important to me."

    vl salem_vl_prefix 2
    salem "She says our Father was in it. Think you’d be able to tell me a bit about them sometime?"

    cha "Anytime. I can give you my number later, so your sister doesn’t have to be a middleman."

    vl salem_vl_prefix 3
    salem "Thanks, man."

    "He turns to Skylar, who’s giving him a weird look."

    cha "Nice to meet you. And you are…?"

    "Her stare lingers."

    vl salem_vl_prefix 4
    salem "Sis, you good?"

    vl arline_vl_prefix 2
    arline "Skylar, it’s not polite to stare."

    vl skylar_vl_prefix 1
    sky "Oh, sorry. Well, Mother already said my name, but I’m Skylar."

    cha "Was there something funny about me?"

    vl skylar_vl_prefix 2
    sky "That tie clip… Is that the Star of Origin?"

    cha "Oho? A fellow “Pretty Magica” disciple? Not many people recognize where my clip’s from."

    vl skylar_vl_prefix 3
    sky "Of course the uncultured masses wouldn’t recognize it. Far too many of them have crap taste."

    vl arline_vl_prefix 3
    arline "Skylar!"

    vl skylar_vl_prefix 4
    sky "Well, it’s true! So many of them look at “PreMa” and dismiss it as some stupid little kids show, but it’s so much more than that!"

    show charles excited
    cha "Exactly! It’s a perfect example of “Don’t judge a book by its cover”!"
    show charles neutral

    a "That’s right. I learned that the hard way."

    vl skylar_vl_prefix 5
    sky "Since when were you into “PreMa”?"

    a "Well, it was a whole thing. Wei kept me up all night w—"

    vl salem_vl_prefix 5
    salem "He did what now?"

    a "What? It’s not like that, you brat. We were in the school w—"

    vl skylar_vl_prefix 6
    sky "I-in the school?! I didn’t know you were such a deviant, dear sister!"

    a "WE WERE WATCHING ANIME!"

    "The twins share a hearty laugh, in a rare moment of sibling unity. All at my expense, of course."

    cha "Sounds like things must be pretty lively at home."

    a "Unfortunately…"

    vl salem_vl_prefix 6
    salem "Come on, you know you love us."

    cha "I think I’m going to have a lot of fun getting to know you folks."

    jump finale