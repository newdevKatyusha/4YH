label literature_route_jinus(month, date):
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Own Route/Month 1/Lucas_M1_"
    $ val_vl_prefix = "audio/voices/Supporting-Extra/Val/Lucas/Month 1/Val_Lucas_Month1_"

    call screen calendar(month, date, "Jinus", 8)
    scene bg classroom_lit_afternoon with fade 

    $ renpy.notify("Lucas - Discourse\nToleday, Jinus 8th, 1027 RD")

    vl val_vl_prefix 1
    lek "You have got to be kidding me! How'd you get that out of the text?"

    show lucas neutral with dissolve
    vl lucas_vl_prefix 1
    l "Well, it's quite simple, dear Val. I read it."

    "I wasn't expecting the Literature Club to be so… exciting. I grew up watching Mother and her book club friends getting together at the house from time to time."
    "They always sounded like they were having fun, but this is different."
    "It's part book club, part literature-focused debate club and, for a bunch of bookworms, the debate part is pretty godsdamned entertaining."
    "For the most part, I've been able to be a fly on the wall, which is nice. I read the novel they're discussing today, but since it's the fourth in a series I haven't touched, I'm very glad to be ignored."

    vl val_vl_prefix 2
    v "Come on, really? Alonzo and Sofia nearly burn down Articia and you're trying to tell me 'Violet Strands' isn't meant to warn against immature, short-sighted love?"

    show lucas tired with dissolve
    vl lucas_vl_prefix 2
    l "You could easily say that, but I don't believe it's what the author was trying to say, no."

    "He's holding a copy of the book we're covering right now and flips through it for a minute trying to find a certain passage."

    show lucas neutral with dissolve
    vl lucas_vl_prefix 3
    l "'I love Alonzo,' Sofia said, vision blurred by tears, 'and I will do anything to help him achieve his dreams, Divines be damned!"
    voice sustain
    l "I won't repeat my mother's mistake and abandon him in the name of 'duty.'"

    vl val_vl_prefix 3
    v "Exactly. She's next in line to run the city, and she's throwing it away for a guy?"
    voice sustain
    v "Then, of course, there's the fact that she's about to drug the entire garrison so he can rob the cathedral. What else can you get out of that?"

    show lucas happy with dissolve
    vl lucas_vl_prefix 4
    l "She said it quite plainly."

    "Lucas turns to me, and I freeze. Please don't…"

    vl lucas_vl_prefix 5
    l "Would you like to share your opinion, [a]?"

    "Ah, nuts."

    a "I didn't read the original trilogy, so I'm sure I'm missing some context…"

    vl val_vl_prefix 4
    v "Of course you didn't read it."

    show lucas neutral at center with dissolve
    if eval(a.name)[0] == "Alexis":
        vl lucas_vl_prefix 6A
    else:
        vl lucas_vl_prefix 6B
    l "Hush now. That's alright, [a]. You don't need to know Scarlet Blade Under a Violet Moon to understand the message here."
    voice sustain
    l "Think about what it was Sofia did."

    "She sabotaged her own city so a thief and his pals could rob the Church. I get what Val's saying."
    "That's incredibly irresponsible, especially since it allows other criminals to run wild until the garrison's back up and running."
    "But, in the world of the book, the church is also super corrupt and doing more harm than good."

    #[Beat]
    vl val_vl_prefix 5
    v "Hello? Anyone home?"

    show lucas annoyed with dissolve
    vl lucas_vl_prefix 7
    l "Oh, dear, I'm afraid we've lost them."

    "Crap! How long was I just sitting there staring into space?"

    a "The road to the Abyss is paved with good intentions. Sofia loves Alonzo, so she wants to help him achieve his goals. And dealing a blow to the Church is a good thing for the people of her city."

    vl val_vl_prefix 6
    v "But it led to a night of lawlessness and chaos!"

    show lucas happy with dissolve
    vl lucas_vl_prefix 8
    l "And that is precisely my point. The choice Sofia made out of love, both for Alonzo and Atricia, was not black and white."
    voice sustain
    l "Yet they both came from the same noble source. Who can say definitively which matters more, Sofia's actions or their results?"

    "Several of the gathered club members nod in agreement to what Lucas and I said. Val, on the other hand, seems a bit less convinced."

    vl val_vl_prefix 7
    v "Yeah, yeah, whatever. I still say it's telling people to be worried about loving someone without really getting to know them."

    show lucas neutral with dissolve
    if eval(a.name)[0] == "Alexis":
        vl lucas_vl_prefix 9A
    else:
        vl lucas_vl_prefix 9B
    l "And I appreciate your input, Val. Same to you, [a]."

    a "Yeah, sure. I just hope next time I'll have more to offer."

    "We move on from that topic, but the rest of the meeting is spent discussing other parts of the same book, its themes, its characters, etc."
    "Thankfully, I don't have to say too much."
    "The more we talk, the more references to previous events and characters go right over my head. I hope this doesn't become a trend this year, or else I just might sink."
    
    # jump to phillip jinus
    call phillip_jinus("Jinus", 8) from _call_phillip_jinus_2
    #jump literature_route_dallinus

label literature_route_dallinus(month, date):
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Own Route/Month 2/Lucas_M2_"
    $ goude_vl_prefix = "audio/voices/Supporting-Extra/Isaiah/Lucas/Month 2/Isaiah_Lucas_Month2_"

    call screen calendar(month, date, "Dallinus", 17)
    scene bg wilson_salon_afternoon with fade

    $ renpy.notify("Lucas - Antecedent Relationships\nIstday, Dallinus 17th, 1027 RD")

    "Lucas invited me to the salon on the third floor of the Wilson Building."
    "I barely knew about this place. It's a nice little place, like a fancy, private cafe."
    "We sip on coffee, discussing the next books that the club might cover."

    show lucas tired with dissolve
    "He tells me it's part of his routine as the club's president, to talk to new members one-on-one to get a better sense of their taste in books and how they might fit into the club."

    vl lucas_vl_prefix 1
    l "I was thinking about 'The Golden Price.' How do you feel about that?"

    a "Don't know about that one. My mother's a big fan. I've read it once. It's big."

    show lucas tired with dissolve
    vl lucas_vl_prefix 2
    l "That's the biggest issue here. It's so good, but it feels like too much to ask everyone to read on top of their homework."
    voice sustain
    l "Maybe just the first book, but that's barely scratching the surface."

    "\"Barely scratching the surface\" is putting it mildly."
    "The series spans a man's entire life, until he has great-grandchildren, but the first book only covers his relatively uneventful childhood."
    "At best, it might pique someone's interest, but at worst, it could bore them to tears."

    a "Maybe 'The Blackwater Bastion'? I haven't read it, but I know it's a lot shorter."

    show lucas happy with dissolve
    vl lucas_vl_prefix 3
    l "It just might work. Like all spin-offs, you won't glean as much if you haven't read the main series, but it's a much more friendly starting point."

    vl goude_vl_prefix 1
    h "Blakesley, Flores, it's good to see you two."
    "The headmaster walks up to our table, a folio tucked under his arm."

    a "Good afternoon, Headmaster. Looking for a break after finishing up some work?"

    vl goude_vl_prefix 2
    h "Oh, no. The salon is for you students. I'll probably go somewhere in town."
    voice sustain
    h "Just doing the rounds and seeing how everyone's doing."
    voice sustain
    h "I believe I heard 'The Blackwater Bastion' a moment ago?"

    show lucas neutral at center with dissolve
    vl lucas_vl_prefix 4
    l "Have you read it, sir?"

    vl goude_vl_prefix 3
    h "Read it? It's one of my favorites. First discovered it when I was in the Literature Club myself."

    a "You were in the same club as us? Small world."

    show lucas happy with dissolve
    vl lucas_vl_prefix 5
    l "How many years ago, if you don't mind me asking?"

    vl goude_vl_prefix 4
    h "First joined in my first year, so nine years ago now."

    show lucas neutral with dissolve
    vl lucas_vl_prefix 6
    l "Then you knew Hugo?"

    vl goude_vl_prefix 5
    h "I did. My condolences."

    "I steal a glance at Lucas out of the corner of my eye. There is a small, sad smile on his face."
    "I feel dirty, like I shouldn't have heard what I just did."

    show lucas sad with dissolve
    vl lucas_vl_prefix 7
    l "Thank you."

    vl goude_vl_prefix 6
    h "He was a very passionate person. I'm sure you looked up to him a lot."

    voice "<to 2.5>audio/voices/Love Interests/Lucas/Own Route/Month 2/Lucas_M2_8"
    l "I did, greatly."

    vl goude_vl_prefix ThroatClear
    "The headmaster clears his throat."

    vl goude_vl_prefix 7
    h "My apologies, I must be ruining the mood."

    show lucas neutral with dissolve
    vl lucas_vl_prefix 9
    l "No need. I mentioned him first. It's nice to meet one of my brother's old friends."

    vl goude_vl_prefix 8
    h "I wouldn't mind sharing some stories about our school days, if you like."

    show lucas happy with dissolve
    vl lucas_vl_prefix 10
    l "That would be splendid. Thank you."

    "The headmaster leaves us, and Lucas goes back to drinking his coffee in silence."
    "I could always just offer my own sympathies, but if the headmaster was a student that long ago, what point would there be in me doing it now?"

    a "...How long ago was it?"

    show lucas sad with dissolve
    vl lucas_vl_prefix 11
    l "Seven years."
    
    "What a morbid coincidence."

    a "That's the year I lost my father, too."

    vl lucas_vl_prefix 12
    l "Ah."

    "A moment of silence passes between us."

    show lucas tired with dissolve
    vl lucas_vl_prefix 13
    l "It is oddly... pleasant to know that you understand this sense of loss I feel."
    voice sustain
    l "Though I suppose it's callous of me to say."

    a "I don't think so. It's nice to know you're not alone in your grief and all."

    show lucas neutral with dissolve
    vl lucas_vl_prefix 14
    l "Perhaps we present the club with a literary treatise on grief. There must be a few good options I can find."

    a "What a light and airy club discussion that's going to be."

    show lucas happy with dissolve
    vl lucas_vl_prefix 15
    l "You're right, too depressing. Then back to the drawing board we go."

    scene bg wilson_salon_night with dissolve
    "It takes some time for us to get back into the swing of things, but before long, we're swapping suggestions again."
    "Even with all of the titles we name, come sunset and our departure, I'm not sure we're any closer to making a decision."
    "Oh, well. Just being able to talk to Lucas like that was its own reward."

    scene black with fade
    call student_council_dallinus("Dallinus", 17) from _call_student_council_dallinus_2

label literature_route_vanus(month, date):
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Own Route/Month 3/Lucas_M3_"

    call screen calendar(month, date, "Vanus", 17)
    scene bg weaver_library_night with fade

    $ renpy.notify("Lucas - Alumnus Proxima\nZaeday, Vanus 17th, 1027 RD")

    "I desperately need to go shopping. My last pencil and, somehow, I forget it."
    "So here I am going back to the library in the dead of night. I worry that it'll be closed but, to my surprise, the door is unlocked."
    "Huntsdale itself has a serene beauty to it at night, but the library? Not too much."
    "The dearth of light in the building unnerves me. The light on my phone is my only guide as I retrace my steps to where I sat earlier in the day."
    "My pencil is there, just as I expected it to be. Picking it up, I notice a light emanating from deeper in the library."
    "Following it, I find Lucas seated at a table in the back, surrounded by a stack of tomes."
    "He's pointing his own phone at one as he flips through it, consumed by the words on the page."

    show lucas neutral with dissolve
    a "Lucas?"

    "He ignores me. I walk up to the table, knocking on its wood. Judging by how high he jumps, he didn't even know that I was there."

    show lucas annoyed with hpunch
    a "Good evening."

    show lucas neutral
    vl lucas_vl_prefix 1
    l "Ah, hello."

    a "A bit late to be here at the library, don't you think? Isn't it after hours?"

    show lucas tired
    vl lucas_vl_prefix 2
    l "I suppose I just forgot to lock up."

    a "With you inside?"

    "I take the opportunity to take a look at some of the books around him."
    "\"A History of Magic Control Laws,\" \"The Tyrannical Enlightenment,\" \"The Arts of Man and the Arts of Gods,\" \"Magicks of the Titanic Era.\""

    show lucas neutral
    vl lucas_vl_prefix 3
    l "What brings you here at this hour?"

    "I waggle my pencil at him by way of an answer."

    show lucas happy
    vl lucas_vl_prefix 4
    l "Ah. A pencil."

    "He's distracted. Like he'd rather be back in his books than talking to me."

    show lucas neutral
    a "Clearly, I interrupted you. Some sort of homework?"

    show lucas sad
    "His eyes drift down, darting between all of the books."

    vl lucas_vl_prefix 5
    l "No, not quite..."

    a "Is it anything I can help you with?"

    show lucas annoyed
    vl lucas_vl_prefix 6
    l "No..."

    show lucas tired
    "Suddenly, he stands up, taking several of the books in hand. He begins putting them back on the shelves."

    show lucas happy
    vl lucas_vl_prefix 7
    l "Nothing for you to worry about. Sorry you had to see that."

    a "You don't have to stop because of me."

    show lucas sad
    vl lucas_vl_prefix 8
    l "I wasn't going to make any progress tonight anyhow."

    "Is that it? It's almost like he's trying to hide something."
    "The chance of me finding these books by myself is slim to none, so if that's his plan, it would definitely work. But what does he have to hide?"

    a "Is everything alright?"

    show lucas annoyed with dissolve
    "He freezes, a book halfway placed back on the shelf. He slides it in, hand resting on the spine, back turned to me."

    vl lucas_vl_prefix 9
    l "I was simply searching for something."

    a "In a bunch of books about how the world was hundreds of years ago? Over a thousand?"

    show lucas happy with dissolve
    "He turns to me, a warm smile on his face."
    "It doesn't reach his eyes."

    vl lucas_vl_prefix 10
    l "It's nothing to worry about. I can always just try again another day."
    voice sustain
    l "Like you said, the library should be closed now. I'll close up in just a minute. You can wait for me outside, if you'd like."

    scene bg mainstreet_night with fade

    "It would be easy to head back to House Lychester on my own, but it doesn't feel right to just leave him."
    "So I wait outside in the chill of the late autumn evening."
    "When he comes out and locks the door, the smile he flashes me still feels false."

    show lucas neutral at right with dissolve
    vl lucas_vl_prefix 11
    l "Thank you for waiting. Shall we walk together for a moment? Our dorms are in the same general direction."

    a "Of course."
    show lucas neutral at center 
    "We aren't together for long, but while we are, we don't say a word."
    "Part of me finds it awkward not to press Lucas on what he was doing so late by himself in the dark."
    "Another, larger, part of me thinks it's better to offer him the silent company than turn our walk into an interrogation. So that's what I do."

    scene black with fade
    
    # jump to second club route dyalt
    $ renpy.call(chosen_club2 + "_route_dyalt", "Vanus", 17)
    #jump literature_route_dyalt

label literature_route_dyalt(month, date):
    $ val_vl_prefix = "audio/voices/Supporting-Extra/Val/Lucas/Month 4/Val_Lucas_Month4_"
    $ clubregular1_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Club Regular 1/Lucas Month 4/ClubRegular1_Lucas_Month4_"
    $ clubmember2_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Club Member 2/Lucas Month 4/ClubMember2_Lucas_Month4_"

    call screen calendar(month, date, "Dyalt", 25)
    scene bg classroom_lit_afternoon with fade

    $ renpy.notify("Lucas - A Reasonable Takeover\nToleday, Dyalt 25th, 1027 RD")

    "Lucas isn't here. Again."
    "The Literature Club's meeting started half an hour ago, but its President never showed up."
    "Most members sit around, scrolling on phones or talking rather than discussing literature."

    "There was no mention of him being busy last meeting. He just... flaked."

    vl val_vl_prefix 1
    v "This is ridiculous. He's pulling this shit again?"

    a "This isn't usual of him, is it?"

    vl val_vl_prefix 2
    v "Ha!"

    a "That doesn't sound good."

    vl val_vl_prefix 3
    v "You're lucky he lasted as long as he did before ditching us. Three months is a record."
    vl val_vl_prefix 4
    v "If he's going to cut his own club, why is he even president? How'd the jackass get the job?"

    vl clubmember2_vl_prefix 1
    lek2 "I hear his older brother was in the Literature Club with the Headmaster, years back. He was president too."

    vl val_vl_prefix 5
    v "Great, so it is nepotism!"

    vl clubregular1_vl_prefix 1
    lek "Is it, though? Lucas was president before the Headmaster was, well, the headmaster."

    vl val_vl_prefix 6
    v "And before him, it was his grandpa. Probably whispered to let his pal's brother take over. Rotten, the whole lot."

    a "Don't you think you're being a little unfair?"

    vl val_vl_prefix 7
    v "Unfair? Isn't it more unfair for the president to not show up without warning?"

    a "Instead of trashing someone who isn't here, how about we do what we came for?"

    "Val strides to the center, looking at everyone slacking off."

    vl val_vl_prefix 8
    v "Phones away! We didn't come here to lounge. You all did today's reading, right?"

    "Val takes control. At first there's reluctance, but soon everyone joins the discussion."
    "The tension remains. Many glance at the door, expecting Lucas to appear."
    "He never does."
    "When the meeting ends, Val sees everyone off, assigning the next reading."
    "I leave them in the club room, arms crossed and face scrunched in frustration."
    "Even behind the closed door, their desk slam is audible. That can't be a good omen."
    "I fear there may be a storm on the horizon."

    scene black with fade
    call student_council_dyalt("Dyalt", 25) from _call_student_council_dyalt_2

label literature_route_neralt(month, date):
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Own Route/Month 5/Lucas_M5_"
    $ val_vl_prefix = "audio/voices/Supporting-Extra/Val/Lucas/Month 5/Val_Lucas_Month5_"
    
    call screen calendar(month, date, "Neralt", 15)
    scene bg classroom_lit_afternoon with fade

    $ renpy.notify("Lucas - The Power of Healthy Acquaintanceship\nToleday, Neralt 15th, 1027 RD")

    "Lucas isn't here. Again."
    "There was no mention of him being busy last meeting, like I would've expected. He just… flaked."
    "Hold on a second. This is… familiar."
    "Val makes a sound that I can only describe as some sort of low growl."

    vl val_vl_prefix 1
    v "I swear, the next time I see four-eyes—"

    "As if summoned, Lucas walks through the door, letting out a hefty sigh."

    show lucas tired with dissolve
    vl lucas_vl_prefix 1
    l "My apologies for the tardiness."

    vl val_vl_prefix 2
    v "Save it."

    "Lucas has only just barely closed the door behind him when Val shoots to their feet. If their eyes could shoot daggers, Lucas would be skewered."

    vl val_vl_prefix 3
    v "What is wrong with you? You've only been to, what, half of our meetings these past two months? Or is that being too generous?"

    show lucas neutral
    vl lucas_vl_prefix 2
    l "I've been busy—"

    vl val_vl_prefix 4
    v "Yeah, and so have the rest of us. Don't see us skipping club. Least not nearly as often as you."

    "Val marches over to Lucas. The eyes of the rest of the club members follow."

    vl val_vl_prefix 5
    v "You don't care about this club, do you? Not anymore."

    show lucas annoyed
    vl lucas_vl_prefix 3
    l "That's preposterous! This club is my passion."

    vl val_vl_prefix 6
    v "Bullshit. You know, I thought you were an alright guy at first. Really pulled the wool over my eyes."

    "They turn their back on Lucas and shove their hand into their pockets."

    vl val_vl_prefix 7
    v "Do us all a favor and hand the job off to someone else. Someone who'll actually take it seriously."

    "Only now does Lucas get his bearings. He takes a step forward."

    show lucas neutral
    vl lucas_vl_prefix 4
    l "I'll do no such thing. I've led this club capably, and I'll continue to do so until I graduate."

    vl val_vl_prefix 8
    v "You really think you're the best for the job?"

    show lucas annoyed
    vl lucas_vl_prefix 5
    l "Do you disagree?"


    vl val_vl_prefix 9
    v "As a matter of fact, I do, nepo baby."

    "Lucas furrows his brow, confused by the label suddenly injected into their conversation."

    vl lucas_vl_prefix 6
    l "Excuse me?"

    "I get out of my seat, striding over to Val."

    a "He's here now, isn't he? Let's just move on. We can deal with everything else later."

    vl val_vl_prefix 10
    v "What, so he can slink off with his tail between his legs and start avoiding us again? This happens now or never."

    show lucas neutral
    vl lucas_vl_prefix 7
    l "Where did this charge of nepotism come from?"

    vl val_vl_prefix 11
    v "Isn't it obvious? Your brother knew the headmaster."

    vl lucas_vl_prefix 8
    l "That doesn't mean anything."

    vl val_vl_prefix 12
    v "Does it? Thought you blue bloods were all about getting handed shit just for existing. Par for the course for you and your ilk."

    show lucas annoyed
    vl lucas_vl_prefix 9
    l "That has nothing to do with any of this."

    vl val_vl_prefix 13
    v "Really? One noble kid's Lit Club president and cozies up with the headmaster's grandson."
    voice sustain
    v "He ends up as headmaster himself, and the noble kid's younger brother gets the same job."

    show lucas neutral
    vl lucas_vl_prefix 10
    l "That doesn't mean I'm not qualified—"

    vl val_vl_prefix 14
    v "Sure as sin doesn't mean you are qualified, either."

    a "Alright, that's enough."

    "Val turns on me."

    vl val_vl_prefix 15
    v "You stay out of this!"

    a "You're the one ruining the club meeting with your grievances. This could've been a private discussion."

    "I motion to the rest of the club, our silent, enraptured audience."

    a "Or you could've gone to a faculty member directly with your concerns. But no."
    a "Your first instinct was to start a scene. Are you sure you're qualified to be Literature Club President?"

    "My words weren't meant to be a tongue lashing, but Val shrinks all the same. Lucas relaxes a bit, but then I look at him."
    "Val started things today, but it was still only a reaction."

    show lucas sad
    a "And you, Lucas. The least you can do is tell us when you're not going to be here."

    vl lucas_vl_prefix 11
    l "You're right. I've been distracted lately—"

    "He sighs."

    show lucas tired
    vl lucas_vl_prefix 12
    l "No, that's just an excuse. My apologies, everyone. I've been terribly unfair to you these last two months."

    "He turns to Val and inclines his head."

    show lucas neutral
    vl lucas_vl_prefix 13
    l "I understand you've been leading the pack in my absence. You have my thanks."

    "Val goes red at the sudden gesture and begins tripping over their words."
    "It takes a little while before they're able to string together a coherent response."

    vl val_vl_prefix 16
    v "Y-you're welcome…"

    show lucas happy
    vl lucas_vl_prefix 14
    l "Alas, I fear the mood has been spoiled for the day. So, let us depart and start anew at our next meeting?"

    "No one complains about the excuse to leave early. Eventually, the only people left in the room are myself, Lucas, and Val."
    "For all their bluster earlier, Val shifts about on their feet, avoiding our eyes like a scolded child."

    vl val_vl_prefix 17
    v "Sorry about that. Might've been a bit out of line."

    show lucas neutral
    vl lucas_vl_prefix 15
    l "But you were right. I have been… lacking as of late. I will do better, but it is nice to know that there's someone here I can rely on to run things."

    "Val perks up at that, then quickly smothers whatever pride they felt with feigned annoyance."

    vl val_vl_prefix 18
    v "I never should've had to do it in the first place. Don't ditch us again, four-eyes."

    "They leave, not giving Lucas a chance to respond. He shrugs."

    a "What have you been doing these past two months anyway?"

    "Since I found him in the library at night, I hadn't mentioned the encounter. But if there was ever a time to do it…"

    a "Are you still searching through those books?"

    show lucas tired
    vl lucas_vl_prefix 16
    l "So you remember that night, do you?"

    a "If you'd rather not talk about it, that's alright."

    show lucas neutral
    vl lucas_vl_prefix 17
    l "No, it's fine. There's a certain Magic Art I'm searching for."

    a "Magic? Couldn't you just ask some of our teachers?"

    show lucas sad
    vl lucas_vl_prefix 18
    l "I tried, in my first year. They all rebuffed me. So, I'm left to search all by my lonesome."

    a "What spell are you looking for?"

    show lucas neutral
    vl lucas_vl_prefix 19
    l "I do not know. But I know what I need it to do."

    "He pauses, growing visibly uncomfortable."

    show lucas annoyed
    a "We don't have to talk about it if you don't want to. Really."

    show lucas neutral
    vl lucas_vl_prefix 20
    l "Right. Thank you. You can leave without me. I have to make sure the club room is secured before I depart."

    a "I wouldn't mind waiting."

    show lucas tired
    vl lucas_vl_prefix 21
    l "Please, I insist."

    "As much as I want to argue the point, I don't. Poor guy's probably been through enough this afternoon."
    "It's for the good of the club if he's more attentive and stops doing… whatever it is he's doing if it means neglecting his duties."
    "But I'm not naive enough to think he'll stop searching. I just hope he doesn't burn himself out trying to do everything all at once."
    
    # jump to second club route neralt
    $ renpy.call(chosen_club2 + "_route_neralt", "Neralt", 15)
    #jump student_council_exalt

label literature_route_exalt(month, date):
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Own Route/Month 6/Lucas_M6_"
    $ val_vl_prefix = "audio/voices/Supporting-Extra/Val/Lucas/Month 6/Val_Lucas_Month6_"
    $ goude_vl_prefix = "audio/voices/Supporting-Extra/Isaiah/Lucas/Month 6/Isaiah_Lucas_Month6_"

    call screen calendar(month, date, "Exalt", 26)
    scene bg classroom_lit_afternoon with fade

    $ renpy.notify("Lucas - Peak of Obsession\nToleday, Exalt 26th, 1027 RD")

    "Val looks furious. And for good reason. The Literature Club just wrapped up its final meeting of the calendar year, right before the Week of Life."
    "And Lucas was absent, with no warning."

    vl val_vl_prefix 1
    v "The bastard said he wouldn't do this again."

    a "It doesn't seem like him to break his word like that, though."

    vl val_vl_prefix 2
    v "I'm going to Instructor Windsor about this. He'll kick four-eyes out. Or, at the very least, he'll talk some sense into him."

    a "You go do that. I'm going to see if I can't find him."

    "In fact, I don't remember seeing Lucas at all today. He didn't skip school, did he?"
    "Val and I part ways. I start by asking some of the other fourth-years if they've seen him. Then some of our teachers."
    "I even make the trek over to his dorm to ask if any of them have seen him around today."
    "He's gone missing."
    "Well, maybe \"missing\" isn't the right word. But if he's not in the one place I can think of, that's going to be a problem."

    scene bg weaver_library_afternoon with fade 

    "The only person in the library is the regular librarian. Right on the cusp of a week-long break, it isn't like anyone has school work to do right now."
    "The old man who normally mans the library did in fact see Lucas. He tried to get him to leave, only to be ignored."
    "I don't need him to point me to the back."
    "Again, I find Lucas surrounded by a pile of books, so absorbed that he hasn't noticed someone joining him. Just from where I'm standing, something feels wrong."

    show lucas tired
    a "Lucas."

    "He glances up at me, dark circles underneath his bloodshot eyes. The haggard young man blinks at me a few times, then frantically checks his phone."

    show lucas annoyed
    vl lucas_vl_prefix 1
    l "Oh, dear, I lost track of the time."

    a "Lost track of time? Lucas, you skipped school."

    show lucas sad
    vl lucas_vl_prefix 2
    l "I did? I only meant to be here for a short while…"

    a "You need to rest."

    "I approach the table, pushing the books away from him. As I reach for the one he's currently reading, he yanks it off of the table."

    a "Come on, don't do this."

    show lucas annoyed
    vl lucas_vl_prefix 3
    l "N-no, I need to keep searching."

    a "What in the Abyss could be so important that it's worth doing this to yourself? You've been obsessing over them for months."

    "Maybe even years, if what Val said was right."
    "His eyes start flitting about the table, trying to settle anywhere else other than me, from the looks of it."
    "Last time, I didn't press the issue, but I can't just walk away because I worry he might be uncomfortable. Not now. I take a seat across from him."

    a "Talk to me, Lucas. This is worrying."

    "He sets the book down and buries his head in his hands. A long moment passes before he looks up, though not at me."
    "In the silence, I swear I hear the door to the library opening."

    show lucas sad
    vl lucas_vl_prefix 4
    l "Fifteen years. That's how long my father's been asleep."

    a "So you're searching for some sort of super spell, because medicine and magic both have failed him?"

    "All he can manage as a response is a nod."

    a "Why didn't you tell anyone? Someone could've helped you look so you didn't have to run yourself ragged like this."

    "A weak, lifeless laugh escapes him."

    show lucas tired
    vl lucas_vl_prefix 5
    l "I already told you, the teachers turned me down. Why would the students be any different?"

    a "If it's this important to you…"

    "I stop short of offering him my help. For, as important as this obviously is to him, I'm not quite sure what  would be best:"
    "helping him search or talking him out of this altogether before it consumes him."
    "He meets my eyes and voices the thought I couldn't bring myself to say."

    show lucas neutral
    vl lucas_vl_prefix 6
    l "Would you be willing to help me?"

    "My mouth hangs ajar, but words fail me."

    vl goude_vl_prefix 1
    h "So, here you were."

    "The headmaster appears, a surprisingly stern look on his face."

    vl goude_vl_prefix 2
    h "Arthur tells me that Moreno came to him absolutely livid."

    show lucas sad
    vl lucas_vl_prefix 7
    l "I have been lacking as a club president of late, I know."

    vl goude_vl_prefix 3
    h "A matter for another time. It's time you stopped."

    "With a snap of his fingers, I feel a gentle breeze."
    "The books gathered on the table begin to levitate, flying themselves back to the bookshelves and slotting themselves into any empty spaces they find."
    "A weary Lucas raises himself to his feet."

    show lucas annoyed
    vl lucas_vl_prefix 8
    l "My apologies, Headmaster, but you don't understand—"

    vl goude_vl_prefix 4
    h "Silence. And take your seat."

    "Lucas spends a long moment just staring at the school's head instructor. This moment is the most authoritative—the most like a teacher—I've ever seen Goude."
    "I put a hand on Lucas's arm to bring him back to reality."

    vl goude_vl_prefix 5
    h "You're playing with dangerous forces, Flores. Stop now while you're ahead."

    show lucas neutral
    vl lucas_vl_prefix 9
    l "With all due respect, sir, I have to do this…"

    vl goude_vl_prefix 6
    h "Hugo said the same thing."

    "There's not a hint of sympathy in his voice. The edge in it cuts Lucas to his core, sobering him in an instant."

    show lucas sad
    vl lucas_vl_prefix 10
    l "My brother?"

    vl goude_vl_prefix 7
    h "Surely you weren't so foolish as to think he went his entire time here without trying to find a way to wake your father."

    show lucas annoyed
    vl lucas_vl_prefix 11
    l "You don't mean…"

    vl goude_vl_prefix 8
    h "There's no way to know for certain, but someone I trust greatly believes it's what killed him."

    show lucas sad
    vl lucas_vl_prefix 12
    l "W-well, who is this source of yours?"

    vl goude_vl_prefix 9
    h "Gabriel. I'd trust his word on this over my own any day."

    "That would be Gabriel Wilson, the priest I saw on my first day and the instructor for Magical Theology:"
    "the study of how various religions around the world interact with the magical beliefs and practices of their followers."

    a "If the Magical Theology teacher's the one you went to, what does that mean? A God killed him?"

    show lucas annoyed
    vl lucas_vl_prefix 13
    l "That's preposterous."
    
    vl goude_vl_prefix 10
    h "Yet that's what he tells me. The Divines don't like men trying to break the rules."

    vl lucas_vl_prefix 14
    l "Yet they let us stitch ourselves back together with magic."

    vl goude_vl_prefix 11
    h "In the ways they allow. We can heal injuries, to a point; alleviate the symptoms of an illness, but not eradicate it."

    a "I'm guessing that waking someone up from a coma would be breaking the rules?"

    vl goude_vl_prefix 12
    h "And the Divines don't think highly of rule-breakers."

    show lucas neutral
    vl lucas_vl_prefix 15
    l "Surely you must see how I find this hard to believe."

    vl goude_vl_prefix 13
    h "This is just conjecture on Gabriel's part, but he imagines it went something like this:"

    vl goude_vl_prefix 14
    h "Hugo found an Art that might work. And when his course was set, he drew the ire of one of the Divines."
    voice sustain
    h "They appeared to him and said:"

    vl goude_vl_prefix 15
    h "\"Your father's time is near. Do not interfere with this matter.\" But he insisted, and when he did, he was told,"
    voice sustain
    h "\"Then, so that your father's soul may yet remain on this mortal coil, as is your desire, let us take yours as recompense.\""

    "Save for the ticking of the clock, and the occasional cough from the old librarian, we were plunged into silence."
    "Lucas hangs his head, and the headmaster's expression has yet to soften. I place a hand on Lucas's shoulder and break the silence."

    show lucas sad
    a "Then it's best to leave it."

    vl lucas_vl_prefix 16
    l "You want me to give up on my father, too?"

    "His voice is small and weak. It makes my next words stick in my throat, but I manage to force them out."

    a "When he wakes up, do you want him to find out he's lost both sons?"

    "And if Instructor Wilson's theory was right, it would only make things worse."
    "A comatose man on the verge of death, forced to carry on for years, and all because one of his sons was desperate to save him." 
    "Lucas could die and only extend his father's sleep with no hope for closure for anyone."
    "It's far too tragic a possibility to be worth the risk."

    vl goude_vl_prefix 16
    h "It's over, Flores. You might not be able to return home with a cure for your father, but you can be there to be at his side and ring in the new year with him."
    voice sustain
    h "Surely that's something he'd appreciate."

    a "The headmaster's right. Being there for him next week is something that you can do."

    vl goude_vl_prefix 17
    h "Blakesley, take him back to House Bryne. I sent the nurse ahead of you. He'll be waiting to make sure Flores is alright."

    "I help Lucas to his feet and let him lean on my shoulder. We pass by the headmaster, leaving Lucas's little alcove of obsession behind."

    vl goude_vl_prefix 18
    h "One more thing."

    "There's a small rustling sound, and then an envelope appears at the corner of my eye."

    show lucas neutral
    vl goude_vl_prefix 19
    h "It's from Hugo. I can only assume it's meant for you."

    vl lucas_vl_prefix 17
    l "My brother? Where did you…?"

    "The headmaster sighs, guilt settling onto his face."

    vl goude_vl_prefix 20
    h "My desk. Grandfather stored it away after… the end. In the years since, I suppose he forgot. I found it not too long ago."

    "Lucas takes the envelope and struggles to put it into a pocket on his blazer."
    "I walk Lucas back to his dorm as instructed. We don't speak the entire way there."
    "Upon our arrival, the nurse comes to collect him, assuring me that he'll make sure Lucas is in good shape and gets enough rest today."
    "For a time, I linger out in front of House Bryne, wondering what will become of my friend. His dreams dashed, his spirits crushed, homebound right after it all."
    "If I was superstitious, I'd wholeheartedly believe that this obsessive, crestfallen Lucas would die with the year, and a new one would be reborn with the coming of the next."
    "But, the truth is, I don't know."
    "And I won't until after break. It's supposed to be a time of rest and relaxation, but I anticipate nothing but anxiety and trepidation."
    "I just hope he'll be okay."
    
    call phillip_elvera("Exalt", 26) from _call_phillip_elvera_2

label literature_route_elvera(month, date):
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Own Route/Month 7/Lucas_M7_"
    $ hugo_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Hugo/Hugo_Lucas_Month7_"

    call screen calendar(month, date, "Elvera", 24)
    scene bg classroom_lit_afternoon with fade

    $ renpy.notify("Lucas - Denouement\nToleday, Elvera 24th, 1028 RD")

    "Lucas and I are the only ones left in the club room. He was there, but he wasn't quite… present."
    "Val and I needed to do most of the running of the club today. It's been this way the entire month."
    "I didn't tell Val the details, but even they could tell that Lucas is rattled. So they've been going easy on him."

    show lucas tired

    a "How are you doing?"

    vl lucas_vl_prefix 1
    l "Would you believe me if I said \"perfectly alright?\""

    a "No."

    show lucas sad
    vl lucas_vl_prefix 2
    l "Then there you have it."

    a "Think talking about it might help?"

    "I pat the desk next to where I'm sitting. It takes a minute, but he accepts the invitation."

    show lucas sad
    vl lucas_vl_prefix 3
    l "It's like I lost him all over again. Both of them, really."

    a "I see how it might feel that way. But, this is how it has to be."

    vl lucas_vl_prefix 4
    l "Yes, I know. That small hope of being able to wake my father up with some sort of Art has kept me going for years."
    voice sustain
    l "And just like that, it was snuffed out. I feel so… lost."

    a "I was like that once. You could say my father was the glue that held my family together. Losing him was hard."

    show lucas neutral
    vl lucas_vl_prefix 5
    l "How did you get through it?"

    "How did I? I wouldn't exactly say it came naturally to me, but it's been so long that I can hardly remember."

    a "Well, I just pushed right through it, I think. In hindsight, probably not the healthiest approach, but it's what I needed to do."
    a "The world wasn't going to wait for me, so I couldn't let myself get bogged down by the grief."
    a "My family needed me, so even when it was hard, I gave every day my all. And it just got easier and easier with time."

    vl lucas_vl_prefix 6
    l "And it took longer than a month to see the results?"

    a "Much longer. And even then, could you say you're giving it your all right now?"

    "He gives me a small nod, but his forlorn expression remains."

    a "These things take time, though, so don't beat yourself up about it too much, alright? It's different for everyone."

    show lucas tired
    vl lucas_vl_prefix 7
    l "You're right, I shouldn't."

    "He drums his fingers on the desk, lips pursed."

    a "Is there something on your mind?"

    "Out of his pocket, he produces an envelope and lays it on the desk between us."

    show lucas neutral
    a "Is that…?"

    vl lucas_vl_prefix 8
    l "My brother's letter, yes."

    a "It looks unopened."

    show lucas sad
    vl lucas_vl_prefix 9
    l "I haven't had the strength to face it."

    "I place a hand on his arm."

    a "Then, please, take some of mine."

    "Lucas takes a deep breath and opens the envelope, taking out the letter within, and begins to read."

    show lucas neutral
    vl hugo_vl_prefix 1
    h3 "\"My dear brother, by the time you read this, I am gone. I have found that which I sought: a means through which to wake our father."
    voice sustain
    h3 "Alas, this wondrous discovery has invoked the ire of Gods. I was visited in my sleep by the Gods of Life and Death."

    vl hugo_vl_prefix 2
    h3 "\"They beseeched me to reconsider, but in my damnable stubbornness, I could not."
    voice sustain
    h3 "I will not condemn our father by denying him this succor due to threats, even if it's from beings to whom I am but an insect."

    vl hugo_vl_prefix 3
    h3 "\"And so, they have deemed me worthy of punishment for this arrogance. I shall not live to see  the morning."
    voice sustain
    h3 "They did, however, allow me a chance to write this final letter. And I chose you, Lucas. I am sorry for leaving you this way."

    show lucas sad
    vl hugo_vl_prefix 4
    h3 "\"For how much you respected me, it's regrettable that my own ego is the thing that shall tear me away from you."
    voice sustain
    h3 "I pray you will one day forgive my selfishness. In this loneliness, I imagine you may follow in my footsteps. I beg you, do not."

    vl hugo_vl_prefix 5
    h3 "\"Do not repeat my mistake. Do not leave our father with no sons to see him awake, and do not damn our mother to have no one left but her husband, locked in a vegetative state by the whims of fate."

    vl hugo_vl_prefix 6
    h3 "\"They both deserve better, and that, I believe, is you. Live your life well, for Father, for me and, most importantly, for yourself."
    voice sustain   
    h3 "I do, and always will, love you dearly, my little brother.\""

    vl lucas_vl_prefix Sobbing
    "Lucas kept himself together while reading, but at the final words, he drops the paper and begins to sob. Silently, I put an arm around him and let him grieve."
    voice sustain
    "We sit in silence for a long while. When he falls silent, he takes off his glasses and smacks his cheeks."

    a "Lucas?!"

    show lucas tired
    vl lucas_vl_prefix 10
    l "Leave it to my older brother to know me so well. Thank you for staying here with me."

    a "Of course."

    "He extricates himself from me and stands."

    show lucas neutral
    vl lucas_vl_prefix 11
    l "Give each day my utmost, was it? I suppose I'll have to do just that. I might have to lean on you, though, from time to time."

    a "If it'll make it easier on you, please do."

    show lucas happy
    if eval(a.name)[0] == "Alexis":
        vl lucas_vl_prefix 12A
    else:
        vl lucas_vl_prefix 12B
    l "There's someone I need to go see. This, I believe I'll be able to manage on my own, though. I'll be seeing you, [a]."

    hide lucas with dissolve

    "I help him lock up, and then we go our separate ways. I can't help but look over my shoulder a few times."
    "He seems in much better spirits and determined to move on from the shock of last month, but this is a marathon, not a sprint."
    "I hope Lucas is able to keep pace."
    
    call literature_route_verabris("Elvera", 24) from _call_literature_route_verabris

label literature_route_verabris(month, date):
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Own Route/Month 8/Lucas_M8_"
    $ val_vl_prefix = "audio/voices/Supporting-Extra/Val/Lucas/Month 8/Val_Lucas_Month8_"
    $ clubregular2_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Club Regular 2/Lucas Month 8/ClubRegular2_Lucas_Month8_"

    call screen calendar(month, date, "Verabris", 7)
    scene bg classroom_lit_afternoon with fade

    $ renpy.notify("Lucas - Crossover Episodes\nNyday, Verabris 7th, 1028 RD")

    "The Literature Club is watching anime today."
    "It and the Anime Club—or \"Anime and Manga Association,\" as the president insists—meet on different days, but for this week, we arranged a back-to-back mixed meeting arrangement–"
    "- that doesn't have us reading a single word."
    "Instead, we've been watching an anime called \"Lighting Strikes Red Thread.\" Mostly. The first day had a few first episodes, but once we started that last show, we stuck to it."
    "For the most part, people have been having fun."

    vl val_vl_prefix 1
    v "Have to leave it to four-eyes, this was a good plan."

    a "What?"

    vl val_vl_prefix 2
    v "You'll see in a second."

    "After we finished what I think is episode six, Killian pauses."

    k "We're just about out of time. Before we head out, though, Lucas wants to say something."

    show lucas neutral
    vl lucas_vl_prefix 1
    l "Thank you, Killian, and everyone in the AMA for humoring me these last two days. And to our AMA friends who weren't already fans of the show, did you have fun?"

    "There are a few shouts to the affirmative from the crowd."

    show lucas happy
    vl lucas_vl_prefix 2
    l "Fantastic. Well, I wanted to let you know there's much more where that came from."

    lek "No duh. Do you know how long this show is?"

    "Lucas smirks and adjusts his glasses, the light of the room making them flash a brilliant white for a moment."

    vl lucas_vl_prefix 3
    l "That's not what I'm referring to."

    "He reaches into his backpack and produces a book. On the cover is a character I now recognize."
    "After all, I just saw her on screen. A few people in the crowd seem intrigued by what he's holding."

    show lucas neutral
    vl lucas_vl_prefix 4
    l "\"Lighting Strikes Red Thread\" is based on a series of novels. Killian tells me there's quite a bit they needed to cut for the adaptation, so there's content you can only get on the page."

    k "It's more than that. The anime caught up to the novels at some point and split off. The later volumes are their own thing."

    show lucas happy
    vl lucas_vl_prefix 5
    l "Of course, this is probably just the most well-known example, but there are countless others."
    voice sustain
    l "Familiar stories you can see in a new light and tales not unlike what you're used to that only exist in the form of books."
    vl lucas_vl_prefix 6
    l "And discussing these very stories is all that the Literature Club is about. We'd be more than happy to have you if you wanted to explore these worlds with us."

    "I can barely make out the things people say when they talk over each other, but a few promises to stop by next week do stand out to me."
    "Killian dismisses the club, and before long, me, Val, and the two presidents are the only ones remaining."

    show lucas neutral
    k "Looks like it worked. I didn't think about using each other's clubs for cross-promotion."

    vl lucas_vl_prefix 7
    l "A brief moment of inspiration was all I needed. Before then, I never thought to do this, either."

    vl val_vl_prefix 3
    v "Good one, four-eyes. I'm impressed."

    a "High praise, coming from you."

    vl val_vl_prefix 4
    v "Can it."

    show lucas happy
    vl lucas_vl_prefix 8
    l "It's quite fortuitous that you decided to stay behind, Val."

    vl val_vl_prefix 5
    v "What?"

    vl lucas_vl_prefix 9
    l "Of course, I graduate next month, as does my dear friend here. So, as far as people I'd trust the Literature Club to…"

    vl val_vl_prefix 6
    v "H-hold on a second!"

    a "What's the problem? You're the one that came for this job a few months ago."

    vl lucas_vl_prefix 10
    l "I'd be honored if you took over my role as Literature Club President next year."
    voice sustain
    l "If all goes well, this little stunt will have gained you a fresh crop of interested new members too."

    "Val's face goes red."

    vl val_vl_prefix 7
    v "You… you…!"

    "They grow even redder, then turn and flee the room."

    show lucas neutral
    k "Not often does one encounter a tsundere in the wild. Fits the trope to a tee."

    vl lucas_vl_prefix 11
    l "I suppose they do, don't they?"

    "Why do I feel like I'm being watched?"

    vl lucas_vl_prefix 12
    l "Well, we borrowed your club today. Do you need any help tidying up?"

    k "I'll be fine. See you later."

    "We leave Killian in his club room and begin to head out of Magis Hall."

    show lucas neutral
    a "You're doing better."

    vl lucas_vl_prefix 13
    l "I'm trying, at least. With how poor of a president I've been, it only felt right to try and inject some new life into the club for after I'm gone."

    a "And Val?"

    show lucas happy
    vl lucas_vl_prefix 14
    l "Their passion inspired me. And it's my way of apologizing after causing them so much trouble."

    "When we're on the first floor, Lucas again produces the novel from earlier."

    show lucas neutral
    vl lucas_vl_prefix 15
    l "I have to return this to the library. So, I'll be seeing you."

    hide lucas with dissolve

    "This time, when we part ways, I'm much more optimistic about how he's doing than I was last month."
    "I have to hand it to him, he's done a mighty fine job bouncing back."
    "As far as I can tell, I've helped him with that, but I don't think he'll need me for much longer. For better or worse."
    
    #jump to second clubd route verabris
    $ renpy.call(chosen_club2 + "_route_verabris", "Verabris", 7)
    #jump student_council_verabis

label literature_route_overa(month, date):
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Own Route/Month 8/Lucas_M9_"

    call screen calendar(month, date, "Overa", 22)
    play music lucasTheme fadein 1.0
    scene bg weaver_library_afternoon with fade

    $ renpy.notify("Lucas - \nUctday, Overa 22nd, 1028 RD")

    "In his capacity as substitute librarian, Lucas has found himself helping to sort recently returned books, a bit like the day we first met."
    "Graduation is right around the corner, so it is a bit sad that he's doing this instead of enjoying his final days at the school with friends."
    "Not wanting him to be alone, I offered to help. So we find ourselves in the back of the library, out of view of anyone who might come in, surrounded by books that need to be put back where they belong."

    show lucas neutral
    a "Any overdue books to worry about this time?"

    vl lucas_vl_prefix 1
    l "There will always be overdue books. The librarian's going to have to chase them by himself, though."

    a "Best of luck to him."

    "For a moment, we stack books in silence. Then I'm reminded of something."

    a "You weren't there when we listened to the campaign speeches. What happened?"

    show lucas tired
    vl lucas_vl_prefix 2
    l "I was feverishly putting together application materials."

    a "For?"

    show lucas neutral
    vl lucas_vl_prefix 3
    l "Graduate school. Outside of the empire. Seeing the world will do me some good."

    a "Kept you that busy?"

    show lucas sad
    vl lucas_vl_prefix 4
    l "It did. …You know, I was originally planning on dropping out this year."

    "The sudden revelation stuns me into silence. Lucas takes that opportunity to go on."

    vl lucas_vl_prefix 5
    l "Seek the Art I was looking for elsewhere. Other places in Magiana, the empire, the world. In the end, I couldn't."

    "He slides a book into the bookshelf and then turns to me."

    show lucas neutral
    vl lucas_vl_prefix 6
    l "Because of you."

    a "Me?"

    vl lucas_vl_prefix 7
    l "At the thought of leaving, I asked myself what I would miss, and what I'd be sacrificing in pursuit of my goal."
    voice sustain
    l "If it meant looking for ways to wake my father, I didn't expect anything to give me pause, but you did."
    vl lucas_vl_prefix 8
    l "I wasn't sure why, at first. A gut feeling. I didn't want our time together to end, not so soon."
    voice sustain
    l "Then just a few short months later, you proved my gut right, that night in Exalt."

    "Gods. If that was his plan, who knows what would've happened if he had left? The thought of him meeting the same fate as his brother sends chills down my spine."

    show lucas happy
    vl lucas_vl_prefix 9
    l "One could say  that you saved my life. And that, now, I must place my life in your hands as recompense. If you would have me, of course."

    "I open my mouth, but no words come out. It takes a few more false starts for my brain to process what he just said to me."

    menu:
        "Accept Lucas's confession":
            $ lucas_romance = True
            jump literature_route_overa_romance_accept
        "Reject Lucas's confession":
            $ lucas_romance = False
            jump literature_route_overa_romance_reject

label literature_route_overa_romance_accept:

    show lucas neutral
    a "I'll be sure to take good care of you, don't worry."

    "It's Lucas's turn to have words fail him. He just smiles at me and gets back to his work."

    show lucas happy
    vl lucas_vl_prefix 10
    l "Regarding my study abroad…"

    a "If you think it's for the best, I don't see any reason not to do it. Sounds like it could be a lot of fun."

    show lucas neutral
    vl lucas_vl_prefix 11
    l "If I'm accepted."

    a "Please. I have no doubt you will be."

    "Before long, our work is done."

    a "Okay! Now that that's out of the way—"

    show lucas happy
    "My breath hitches in my throat when Lucas caresses my cheek. Turning to him, and seeing the soft, relaxed look in his amber eyes, my face heats up."
    "When he closes his eyes and begins to lean in, the world begins moving in slow motion. At least, that's what I tell myself."
    "With my brain going haywire, I can't think of any other way I could've thought to close my eyes and await the kiss."
    "My first kiss, and my treasonous brain's thoughts go from Lucas right to my family."
    "I can almost imagine them: my mother looking on proudly, a bashful Skylar hiding behind her like a little girl, overwhelmed by the quiet, romantic scenery of the library, and Salem teasing us about choosing clichéd location for this important moment."
    "When Lucas and I break away, I'm not sure if I'm smiling because of what just happened or because of how stupid that would be."

    show lucas neutral
    vl lucas_vl_prefix 12
    l "If I might leave you, I didn't want to say goodbye without having done that."

    a "One of the best ideas you've ever had."

    "At the sound of the library's door opening, I jump back. Even out of view like this, the boldness of kissing someone here of all places finally settles in."

    a "Why the library and not my room or something?"

    "Hold on a second."

    show lucas happy
    vl lucas_vl_prefix 13
    l "Oh, your room, you say?"

    a "Wait wait wait, no-!"

    vl lucas_vl_prefix Laugh
    "He laughs, surprisingly mindful of the library's quiet policy."

    show lucas neutral
    vl lucas_vl_prefix 14
    l "But now that our job is done… Lunch?"

    a "Yes, please. How about The Amity? I'd love to eat there one last time."

    hide lucas with dissolve

    "We leave the library hand in hand. The thought of Lucas leaving for yet more school does sadden me, but I put it out of my mind."
    "There's always the reunion afterwards to look forward to and the blissful now to just bask in and enjoy."
    
    call epilogue_graduation("Overa", 22) from _call_epilogue_graduation_6

label literature_route_overa_romance_reject:

    show lucas sad
    a "Your life is yours to live, Lucas."

    vl lucas_vl_prefix 15
    l "Yes, I suppose you're right."

    "He sighs."

    show lucas neutral
    vl lucas_vl_prefix 16
    l "At least I got that off my chest."

    "We get back to work in silence, and, before long, we're done."

    show lucas happy
    vl lucas_vl_prefix 17
    l "Just so you know, the memories we made this year are something I'll always cherish."

    a "So will I."

    show lucas neutral
    vl lucas_vl_prefix 18
    l "Since we won't have the chance while I'm away, how about one last lunch together, as friends?"

    a "Yes, please. How about The Amity? I'd love to eat there one last time."

    hide lucas with dissolve

    "When we leave the library, the idea of Lucas going to some other part of Unios is oddly disheartening."
    "Everyone may be going their separate ways, but to a completely different continent? He'd be even further out of reach than my other MIA friends."
    "But I put it out of my mind. Rather than dwell on the time apart, I think ahead to a future reunion."
    "No matter how long he may be away or how far he goes, when we see each other again, I fully expect him to grill me about all the new books I've read."
    "And that's something I'm very much looking forward to."

    call epilogue_graduation("Overa", 22) from _call_epilogue_graduation_7

label epilogue_literature_route:
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Shared Epilogue/Goodbye Lucas/Lucas_Epilogue_GoodbyeLucas_"

    scene bg maincastle with fade 

    "When Reina's gone, I make to call… Skylar, probably. She's most likely to pick up."

    show lucas happy at center
    vl lucas_vl_prefix 1
    l "Well, look who it is. What a pleasant surprise."

    "I lower my phone. So close, but calling can wait a little bit longer, right?"

    a "Lucas, hey!"
    
    jump epilogue_lucas_choice

label epilogue_lucas_choice:
    if lucas_romance:
        jump epilogue_literature_route_romance_accept
    else: 
        jump epilogue_literature_route_romance_accept

label epilogue_literature_route_romance_accept:
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Shared Epilogue/Goodbye Lucas/Lucas_Epilogue_GoodbyeLucas_Accepted_"

    show lucas neutral at center
    vl lucas_vl_prefix 1
    l "So our journey is finally at its end. Bittersweet, isn't it?"

    a "It is. I think I'm going to miss this place."

    vl lucas_vl_prefix 2
    l "But life must go on, and we have little choice but to march to its relentless rhythm."

    a "Speaking of, when will you hear about your study abroad application?"

    show lucas happy
    vl lucas_vl_prefix 3
    l "I've been waiting to tell you. I'll be starting a Master's in Creative Writing and Literature at the University of Brighton after the summer."

    a "Really, Brighton? Lucky."

    "He laughs."

    vl lucas_vl_prefix 4
    l "I'm the lucky one? I thought I heard you wanted to travel the world, too."

    a "That's right. Need to clear my head a bit. Maybe I try going to Brighton myself…?"

    vl lucas_vl_prefix 5
    l "Can't bear the thought of being away from me, can you? I like the thought, our own little world tour."

    show lucas neutral
    a "Not just the underclassmen."

    vl lucas_vl_prefix 6
    l "Poetic, isn't it? The study abroad is for them, yet here we are, defying fate to reap the reward in our own  way."

    "His eyes dart to my phone."

    vl lucas_vl_prefix 7
    l "Were you busy?"

    a "Just about to call my sister."

    show lucas happy
    vl lucas_vl_prefix 8
    l "Then don't let me keep you. I was just about to head over to the library anyhow. We'll speak soon again, dear. Take care."
    hide lucas with dissolve

    jump epilogue_intermission

label epilogue_literature_route_romance_reject:
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Shared Epilogue/Goodbye Lucas/Lucas_Epilogue_GoodbyeLucas_Rejected_"

    show lucas neutral:
        xpos 0.7 yalign 1.0

    vl lucas_vl_prefix 1
    l "Congratulations on making it to the end of this story, dear."

    a "Same to you."

    vl lucas_vl_prefix 2
    l "I've heard through the grapevine that you wanted to travel, now that you're free from your academic obligations?"

    a "Just doesn't seem like a bad idea to see the world and think a bit more about what I want to do."

    show lucas happy
    vl lucas_vl_prefix 3
    l "Would you write to me? I'll be sure to write to you. Might be nice to have a pen pal, especially in our world of modern technology."

    a "Of course. Hold on, have I ever written a letter before?"

    vl lucas_vl_prefix 4
    l "Exactly my point. I'm sure it'll be fun."

    "His eyes dart to my phone."

    show lucas neutral
    vl lucas_vl_prefix 5
    l "Were you busy?"

    a "Just about to call my sister."

    show lucas happy
    vl lucas_vl_prefix 6
    l "Then don't let me keep you. I was just about to head over to the library anyhow. We'll speak soon again, dear. Take care."
    hide lucas with dissolve

    jump epilogue_intermission

label reuinion_literature_route:
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Shared Epilogue/Meet The Family/Lucas_Epilogue_MeetTheFamily_Lucas_"
    $ arline_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Arline/Epilogue/Meet Lucas/Arline_Epilogue_MeetLucas_"
    $ skylar_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Skylar/Meet Lucas/Skylar_Epilogue_MeetLucas_"
    $ salem_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Salem/Meeting Lucas/Salem_Epilogue_MeetLucas_"

    $ renpy.notify("Lucas - Meeting the Family\nNyday, Overa 25, 1028 RD")

    "When Lucas arrives, Mother's off to the races before I've got half a word out."

    show lucas neutral at center with dissolve

    vl arline_vl_prefix 1
    arline "Lucas, is it? I hear you were the school's Literature Club president."

    vl lucas_vl_prefix 1
    l "That's right."

    vl arline_vl_prefix 2
    arline "Are you familiar with \"The Golden Price,\" by chance?"

    show lucas happy with dissolve
    vl lucas_vl_prefix 2
    l "Familiar? How could I not be familiar with one of the finest pieces of historical fiction ever published?"
    voice sustain
    l "The better question would be how many times I've read it."

    vl arline_vl_prefix 3
    arline "I know, right? You just can't help but devour the series from book one all over again after you finish!"

    vl lucas_vl_prefix 3
    l "After you recover from the heartbreak of the final chapter, anyhow."

    vl arline_vl_prefix 4
    arline "Oh, yes, I need a good week grieving before I can pick it up again."

    vl lucas_vl_prefix 4
    l "Actually, if you're a fan, I must know, do you have a favorite passage?"

    vl arline_vl_prefix 5
    arline "Far and away, the \"Roar of the Lightning Dragon.\""

    show lucas neutral with dissolve
    vl lucas_vl_prefix 5
    l "That is a fantastic choice. Though I've always been partial to the \"Blackwater Address.\""

    a "Look at them go. I can't get a word in edgewise."

    vl salem_vl_prefix 1
    salem "This is one of the nerdiest conversations I've ever had the displeasure of hearing."

    vl skylar_vl_prefix 1
    sky "What? You loved the show!"

    vl salem_vl_prefix 2
    salem "Yeah, that's the thing. The show."
    hide lucas 

    "As the twins bicker, and Lucas and Mother continue their impassioned discussion, I can't help but wonder one thing."

    a "I'm introducing my boyfriend to them and I'm the fifth wheel. How did this happen?"
    
    jump finale