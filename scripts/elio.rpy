label archery_route_jinus(month, date):
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Jinus/Elio_Own_Month1_"
    $ clubmember1_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Club Member 1/Elio Month 1/ClubMember1_Elio_Month1_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Elio/Month 1/" + player_voice_prefix + "_Elio_Month1_"

    call screen calendar(month, date, "Jinus", 8)
    scene bg wright_field_afternoon with fade
    play music hatchling14 fadein 1.0

    $ renpy.notify("Elio - The Arrowhead\nToleday, Jinus 8th, 1027 RD")

    "Once upon a time, I thought I liked archery, but now - leg muscles burning and chest on fire - I'm starting to reconsider."
    "At this point, I'm genuinely concerned if my perception of archery has been wrong my entire life, because in all my lessons, I don't remember having to run laps."

    "On the other end of the field, those who have finished their run are sent straight to the target range."
    "Weak-kneed and wobbly, they struggle to aim their bows."

    show elio neutral at right with dissolve
    vl elio_vl_prefix 1
    e "Your form's off. Fix your stance."

    "The poor singled-out club member lets out a sad, whimpering groan."
    "Every gaze on the field softens with pity, except one."
    "The overlord. The tyrant. The club president himself: Elio."

    show elio confused at center with dissolve
    vl elio_vl_prefix 2
    e "What? Would you rather end up dead?"

    "If anything, that only attracts more dissent in the ranks."
    "The club members glance at each other, until one brave soul steps forward, brow knitted in a frown."

    vl clubmember1_vl_prefix 1
    aek "Captain... We appreciate that you take archery seriously, but this is a school club. For fun."
    voice sustain
    aek "No one here is going off to fight an army."

    show elio surprised with hpunch
    vl elio_vl_prefix 3
    "Elio laughs - a short, harsh sound."
    vl elio_vl_prefix 4
    e "Then quit."

    "I stiffen as he glances over the rest of the group, dark eyes piercing."

    vl elio_vl_prefix 5
    e "If you don't like it, then quit. No one's stopping you."

    "Silently, the club member retreats back into the crowd, and Elio resumes his corrections as if nothing happened."
    #a "You have got to be kidding me."
    "You have got to be kidding me."

    vl alexis_vl_prefix 1
    a "Hey!"
    "Elio fixes his icy gaze on me. Jackass wants a fight, he's going to get one."
    "What sort of club president tells people to just quit?"

    show elio neutral with dissolve
    vl elio_vl_prefix 6
    e "It's not time for a break. Back to your drills."

    vl alexis_vl_prefix 2
    a "Abyss take you and your drills. This is a school club, not a boot camp."

    vl elio_vl_prefix 7
    e "If you're not up to the task, then you know what to do. You heard me, didn't you?"

    vl alexis_vl_prefix 3
    a "Yeah, quit."
    "I turn towards the rest of the club's members, transfixed by our clash."

    vl alexis_vl_prefix 4
    a "And I bet I wouldn't be the only one doing that, right?"
    "It takes a second, but some of the others begin nodding or murmuring their intent to follow me if I did walk."

    vl alexis_vl_prefix 5
    a "You really don't want to be the reason half your club up and leaves, right? What kind of club president does that?"

    show elio confused with dissolve
    "Elio doesn't look angry, but if looks could kill, his piercing eyes would've put half a dozen holes in me already."
    stop music fadeout 1.0

    show elio embarrassed with dissolve
    vl elio_vl_prefix 8
    e "We're done for the day. All of you, out of my sight."

    "He doesn't have to tell people twice. Bows are tossed to the ground and people start grabbing their things."
    "As the members of the club abandon him, Elio looks oddly defeated."

    "And even though he was just being an insufferable jackass, it makes me feel bad for the guy."
    #a "Gods, I'm such a bleeding heart."
    "Gods, I'm such a bleeding heart."

    "I should walk away with the others, but instead, I find myself helping him pick up the discarded bows and putting everything away."
    "We don't say a thing the entire time. When we're done, I leave without a word or getting any semblance of a thank you."

    scene black with fade
    #a "This is going to be a long year, isn't it?"
    "This is going to be a long year, isn't it?"
    
    # jump to phillip jinus
    call phillip_jinus("Jinus", 8) from _call_phillip_jinus
    #jump archery_route_dallinus

label archery_route_dallinus(month, date):
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Dallinus/Elio_Own_Month2_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Elio/Month 2/" + player_voice_prefix + "_Elio_Month2_"

    call screen calendar(month, date, "Dallinus", 15)
    scene bg wilson_salon_afternoon with fade
    play music hatchling4 fadein 1.0

    $ renpy.notify("Elio - The Man With a Known Name\nZynday, Dallinus 15th, 1027 RD")

    "Sue told me about a salon on the third floor of the Wilson Building."
    "Unless you're nobility or a club president, you need to tag along with someone who is."

    "I leave Sue in the Student Council room after one of our meetings and head up to the salon myself."
    "I never expected to flaunt my family's status like this."
    "The server who greets me hands me a menu and shows me to a table."

    show elio neutral at right with dissolve
    "Most of the people in the salon are strangers to me, but one familiar face does stick out."
    "I ask to be seated near them, and the server obliges me."

    vl alexis_vl_prefix 1
    a "So... hey."

    show elio confused at center with dissolve
    "Elio looks up from his phone and glowers at me."

    vl elio_vl_prefix 1
    e "What do you want?"

    vl alexis_vl_prefix 2
    a "To talk?"
    "Jackass. I don't wait for him to invite me, and take the other seat at his table."

    vl alexis_vl_prefix 3
    a "Good job loosening up. I can already tell that the others are enjoying the club more."
    
    show elio neutral with dissolve
    vl elio_vl_prefix 2
    e "Sure."

    vl alexis_vl_prefix 4
    a "About the way you run things—"

    show elio confused with hpunch
    vl elio_vl_prefix 3
    e "What're you even doing here?"

    "I roll my eyes."

    vl alexis_vl_prefix 5
    a "Do you want people to hate you?"
    "A faint blush creeps onto his face. It would be almost cute, if he wasn't so rude."

    show elio embarrassed with dissolve
    vl elio_vl_prefix 4
    e "I meant the salon."

    vl alexis_vl_prefix 5.7
    a "That? I'm a viscount's kid. Figured I may as well check the place out."

    show elio surprised with dissolve
    vl elio_vl_prefix 5
    e "So you're nobility, too, huh?"

    vl alexis_vl_prefix 6
    a "Too?"

    show elio neutral with dissolve
    vl elio_vl_prefix 6
    e "Never mind."

    vl alexis_vl_prefix 7
    a "Come on, don't leave me hanging like that. Maybe I've heard of your family before."

    show elio confused with dissolve
    vl elio_vl_prefix 7
    e "Sure you have."

    "I keep my eyes trained on him, which makes him go even redder."

    show elio embarrassed with hpunch
    vl elio_vl_prefix 8
    e "W-what's with you?"

    vl alexis_vl_prefix 8
    a "I haven't heard it yet. Come on, let's see if I don't know."

    show elio confused with dissolve
    vl elio_vl_prefix 9
    e "Gods, you're annoying."
    vl elio_vl_prefix 10
    "He sighs."
    voice sustain
    show elio neutral with dissolve
    e "Ever heard of House Natale?"

    "Have I? I'm not sure if I have."

    show elio happy with dissolve
    vl elio_vl_prefix 11
    e "That's what I thought."

    vl alexis_vl_prefix 9
    a "You got me there. Hold on, what language is that name?"

    show elio neutral with dissolve
    vl elio_vl_prefix 12
    e "Troaran."

    vl alexis_vl_prefix 10
    a "Well that's no fair. You expected me to recognize a noble family from another country?"

    show elio happy with dissolve
    vl elio_vl_prefix 13
    e "You're the one who asked."

    "He's got me there. But there's still something about the name that bugs me."

    vl alexis_vl_prefix 11
    a "Maybe I have heard the name... Some sort of military family, right?"

    show elio surprised with dissolve
    vl elio_vl_prefix 14
    e "Lucky guess."

    vl alexis_vl_prefix 12
    a "I might be terrible with history, but my military history isn't all that bad."
    voice sustain
    a "Sort of comes with the territory when a guy doing good in the army is the only reason your family got their title."

    show elio neutral with dissolve
    vl elio_vl_prefix 15
    e "Really?"

    vl alexis_vl_prefix 13
    a "Ever heard of the Black Wolf of Estary?"
    "My shoulders slump after the protracted silence following my question."

    show elio confused with dissolve
    vl elio_vl_prefix 16
    e "Sorry?"

    vl alexis_vl_prefix 14
    a "Nah, it's fine..."

    show elio confused with dissolve
    vl elio_vl_prefix 17
    e "Hold on, this all started because you came here and started bugging me."
    voice sustain
    e "I didn't come here to chat. Leave me alone."
    
    "No words come to me when I open my mouth to respond. He is right, after all. I stand up."

    vl alexis_vl_prefix 15
    a "Talk to you later?"

    show elio neutral with dissolve
    vl elio_vl_prefix 18
    e "And why would I want that?"

    vl alexis_vl_prefix 16
    a "Because we're in the same club?"
    "Then it's his turn to be silent."

    "A smirk creeps onto my face at the annoyance written plainly on his."
    "I leave him to his brooding, and while I got a little bit of something out of him, I don't know what to expect the next time we talk."
    stop music fadeout 1.0
    "Assuming he doesn't avoid me until graduation."

    scene black with fade
    call student_council_dallinus("Dallinus", 15) from _call_student_council_dallinus

label archery_route_vanus(month, date):
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Vanus/Elio_Own_Month3_"
    $ clubmember1_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Club Member 1/Elio Month 3/ClubMember1_Elio_Month3_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Elio/Month 3/" + player_voice_prefix + "_Elio_Month3_"

    call screen calendar(month, date, "Vanus", 28)
    scene bg wright_field_afternoon with fade
    play music hatchling14 fadein 1.0

    $ renpy.notify("Elio - One Tsun-y Day\nToleday, Vanus 28th, 1027 RD")

    "Most of the archery club is underclassmen. Guess Drill Sergeant Elio scared off most of the upperclassmen."
    "It serves him right. But it’s a bit sad at the same time."

    "There is no vice president of the archery club, and even though it isn’t official or anything,"
    "I think I accidentally ended up in the role for being one of the very few people in the club that puts any effort into talking to him."

    "He still wants us to run, and I’ve just about seen him pop a blood vessel trying to keep himself from yelling at someone for a screw-up."
    "The fact that he’s definitely trying, though? I respect it."

    show elio neutral at center with dissolve
    vl elio_vl_prefix 1
    e "You there, hold it! Your form’s off!"

    "The student he called out freezes, a look of pure terror on their face."
    "Elio’s tried to mellow out, but the fear of being raked over the coal for an honest mistake still lingers."

    vl elio_vl_prefix 2
    e "You’re going to hurt yourself at this rate. Need me to show you the ropes?"

    vl clubmember1_vl_prefix 1
    aek "Yes please?"

    "More than a few people stop and watch. There’s an uncharacteristic tenderness to his instruction."
    "Who is this guy, and what has he done with Elio? He goes red when he notices all of the people staring."

    show elio flustered
    vl elio_vl_prefix 3
    e "No gawking! B-back to your drills!"

    "The others do, but not before getting some laughs in at his embarrassment."

    "When he leaves the struggling underclassman, they’re doing noticeably better."
    "Elio returns to the spot he left, which just so happens to be near me."
    "Before he can get back to his own shooting, he catches my eye."

    show elio neutral
    vl elio_vl_prefix 4
    e "What?"

    vl alexis_vl_prefix 1
    a "You’re a better teacher than I thought you’d be."

    show elio annoyed
    vl elio_vl_prefix 5
    e "Yeah, whatever."

    vl alexis_vl_prefix 2
    a "Why didn’t you pull that out at the beginning of the year?"

    "He ignores me. So I try a different approach."

    vl alexis_vl_prefix 3
    a "Where’d you learn how to teach like that? No way it was all natural talent."

    show elio neutral
    vl elio_vl_prefix 6
    e "After you have to stop your brother from shooting your sister enough times, it becomes second nature."

    vl alexis_vl_prefix 4
    a "Oh, you have siblings?"

    pause 0.5

    vl alexis_vl_prefix 5
    a "Are they the reason you know how to actually teach people archery without being a hardass?"

    show elio annoyed
    vl elio_vl_prefix 7
    e "It isn’t important."
    stop music fadeout 1.0

    "Gods, he must not have any friends. Why act so hostile after an innocent question?"
    "How’d he make it through the past three years? Maybe he’d be willing to open up more if he knew he wasn’t alone."

    "I feel like I was getting through to him a little bit in the salon before he shut me down."

    vl alexis_vl_prefix 6
    a "I’ve had to help my younger siblings plenty of times before."
    "Not the same as archery, but it definitely helps when you need to help out just about anyone."

    show elio angry
    vl elio_vl_prefix 8
    e "Don't care. Didn't. Ask."

    vl alexis_vl_prefix 7
    a "You didn't have to."

    show elio annoyed
    vl elio_vl_prefix 9
    e "Just get back to your archery. The meeting isn’t over yet."

    "He ignores me and any other attempt I make to strike up conversation."
    "When the meeting’s over, he doesn’t stay behind long enough for anyone else to approach him."

    hide elio annoyed
    vl alexis_vl_prefix 8
    a "I just don’t get that guy."

    "One of these days, he’ll actually open up. I mean, this is his last year,"
    "and even he must want to end his time at the school with a friend or two."

    scene black with fade
    
    # jump to second club route dyalt
    $ renpy.call(chosen_club2 + "_route_dyalt", "Vanus", 28)
    #jump archery_route_dyalt

label archery_route_dyalt(month, date):
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Dyalt/Elio_Own_Month4_"
    $ val_vl_prefix = "audio/voices/Supporting-Extra/Val/Elio/Val_Elio_Month4_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Elio/Month 4/" + player_voice_prefix + "_Elio_Month4_"

    call screen calendar(month, date, "Dyalt", 19)
    scene bg weaver_library_afternoon with fade

    $ renpy.notify("Elio - An Echoey Salon Spitoon\nNyday, Dyalt 19th, 1027 RD")

    "The library is a great place to do homework. When I'm cooped up in my room, it's too tempting to lay in bed and scroll mindlessly on my phone."
    "Here, it's much easier to focus on what I need to do."

    "A change in environment does wonders for putting me in a productive mood. The only real downside is that it's easy to lose track of time while I work."

    "I stretch, noticing the sun is already setting. Damn, where did the time go? Sure, it's winter now, but I didn't expect so much time had passed."

    "Well, I made good progress, so it's about time that I—"
    play music hatchling14 fadein 1.0

    vl elio_vl_prefix 1
    e "Don't you think you should cool it, Val?"

    vl val_vl_prefix 1
    v "What're you talking about?"

    "At a nearby table, I see Elio sitting with someone I don't recognize. He hasn't noticed me yet. That's probably good. Seeing my face would put him in a bad mood."

    show elio neutral at right with dissolve 
    vl elio_vl_prefix 2
    e "I hear you tore Dreyar a new one a few weeks back."

    vl val_vl_prefix 2
    v "The bitch deserved it."

    vl elio_vl_prefix 3
    "Elio groans."
    voice sustain
    e "That's what I mean. Ever thought about being less of a dick?"

    vl val_vl_prefix 3
    v "Why should I? People don't hate me!"

    "Someone shushes them. Elio chuckles."

    show elio happy at center with dissolve
    vl elio_vl_prefix 4
    e "Right, how about that guy just now?"

    vl val_vl_prefix 4
    v "They can piss off."

    show elio neutral with dissolve
    vl elio_vl_prefix 5
    e "And saying stuff like that would make them hate you. For good reason. People don't like shit-talkers."

    vl val_vl_prefix 5
    v "It isn't like I'm talking trash about my friends."

    vl elio_vl_prefix 6
    e "As far as they know. You see what I mean?"

    vl val_vl_prefix 6
    v "What do you mean?"

    vl elio_vl_prefix 7
    e "Let's say you didn't tear Reina a new one in public. That you two are friends, even."

    vl val_vl_prefix 7
    v "Gross."

    "Elio waves a hand, as if to say 'Exactly my point.'"

    vl elio_vl_prefix 8
    e "Civil in public, critical in private. For all you know, no one actually trusts you because they've seen how you run your mouth."

    vl val_vl_prefix 8
    v "N-no! That's not..."

    vl elio_vl_prefix 9
    e "'If that's what they say with people around, what do they say behind closed doors? How can I know they're not saying worse about me?'"

    vl val_vl_prefix 9
    v "You're one to talk. What makes you think you can lecture me? You're just as bad!"

    vl elio_vl_prefix 10
    e "And when was the last time I humiliated someone because they annoyed me? For doing their job?"

    vl val_vl_prefix 10
    v "Don't think I don't hear about how you run your club—"

    vl elio_vl_prefix 11
    e "Oh no, someone doing their job. I'm there to make sure they're doing things right. Screw ups like that'll get them killed."

    vl val_vl_prefix 11
    v "You're no drill sergeant, so why do you care?"

    vl elio_vl_prefix 12
    e "You know why. Military family, remember? And outside of that, ever hear anyone complain about me?"

    vl val_vl_prefix 12
    v "Not really, no..."

    vl elio_vl_prefix 13
    e "What's your excuse? How do you justify being ready to shout at people all the damn time?"
    voice sustain
    e "No one's going to think 'Ah, they mean well.' They're going to think you're an annoying little shit."

    "Val buries their head in their hands and Elio does something I couldn’t imagine him doing before: he places a comforting hand on their shoulder."
    stop music fadeout 1.0

    vl elio_vl_prefix 14
    e "Don't worry about it too much. You're still young. Always time to turn it around."

    vl val_vl_prefix 13
    v "You make it sound easy."

    vl elio_vl_prefix 15
    e "Trust me, it isn't."

    "After the initial shock, the gesture does make sense. Elio let slip that he’s an older brother. I doubt this is the first of these talks he’s had to have."
    "Is this really the same guy from back in Jinus who was trying to break his own club members?"

    vl elio_vl_prefix 16
    e "Baby steps and all that, yeah?"

    vl val_vl_prefix 14
    v "I guess so. But what do I even do?"

    vl elio_vl_prefix 17
    e "Try to keep your temper in check, for one."

    "Val rises, offers a small farewell, and Elio doesn’t try to stop them when they leave. His eyes follow them on the way out. He glances in my direction, and our eyes meet. Aw, nuts."
    
    vl elio_vl_prefix 18
    e "Enjoy the show?"

    vl alexis_vl_prefix 1
    a "H-hey..."

    "He isn't angry? That's odd..."

    vl elio_vl_prefix 19
    e "Guess you heard that, huh? Do me a favor and forget you did, alright?"

    vl alexis_vl_prefix 2
    a "Y-yeah, sure... See you later, I guess."

    "My business at the library was done, so when I leave, it's natural. But the talk I overheard is so unlike Elio that it'll be tough to forget."
    "I just hope I'm not thinking about it for too long."

    scene black with fade
    call student_council_dyalt("Dyalt", 19) from _call_student_council_dyalt

label archery_route_neralt(month, date):
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Neralt/Elio_Own_Month5_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Elio/Month 5/" + player_voice_prefix + "_Elio_Month5_"

    call screen calendar(month, date, "Neralt", 15)
    scene bg wilson_salon_afternoon with fade
    play music hatchling4 fadein 1.0

    $ renpy.notify("Elio - In Desperate Need of Intuition\nToleday, Neralt 15th, 1027 RD")

    "What is happening?"

    show elio neutral with dissolve
    vl elio_vl_prefix 1
    e "Just a cup of black coffee for me."

    "How did I end up here?"

    show elio confused with dissolve
    vl elio_vl_prefix 2
    e "Why are you looking at me like that? Is there something on my face?"

    "I sit across from Elio in the salon, on his invitation. After club practice today, he walked up to me and asked–no, declared–that I go somewhere with him."
    "It felt so out of character that all I could do was nod and follow him."

    vl alexis_vl_prefix 1
    a "It’s just… You want to talk to me?"

    show elio embarrassed with dissolve
    vl elio_vl_prefix 3
    e "Don't  make it weird."

    vl alexis_vl_prefix 2
    a "Every time I’ve tried to interact with you, you give me a death glare."

    show elio neutral with dissolve
    vl elio_vl_prefix 4
    e "Shit."

    vl alexis_vl_prefix 3
    a "So…"

    stop music fadeout 1.0
    "As uncomfortable as this all is, there has to be a reason behind his sudden invitation, so I may as well figure out what it is."

    vl alexis_vl_prefix 4
    a "What’s up?"

    vl elio_vl_prefix 5
    e "Right."

    "He rubs the back of his neck, groaning."
    "Obviously, it’s not out of any sort of discomfort but because he’s as bothered by whatever he’s about to say as I am his sudden interest in me."

    vl elio_vl_prefix 6
    e "I need relationship advice."

    vl alexis_vl_prefix 5
    a "What?"

    "He quickly goes red. Very red."
    play music hatchling12 fadein 1.0

    show elio embarrassed with dissolve
    vl elio_vl_prefix 7
    e "N-not for me!"

    vl alexis_vl_prefix 6
    a "Then for who?"

    show elio neutral with dissolve
    vl elio_vl_prefix 8
    e "My sister."

    vl alexis_vl_prefix 7
    a "Oh. Well, I’m very flattered, but I’d have to at least meet the girl…"

    vl elio_vl_prefix 9
    e "She’s fifteen."

    vl alexis_vl_prefix 8
    a "I take it all back."

    "I clear my throat, praying that my shoddy attempt at humor is quickly forgotten."

    vl elio_vl_prefix 10
    e "Relax. It's for my sister."

    vl alexis_vl_prefix 9
    a "And you think I can give your sister relationship advice because…?"

    vl elio_vl_prefix 11
    e "I figure you’ve done it before. You’re an older sibling, too, aren’t you?"

    "Well, this is awkward. Technically, I have given advice, but it’s definitely not the type he’s looking for."

    vl alexis_vl_prefix 10
    a "Best I’ve got is comforting the guys my sister rejects."

    "Elio blinks at me."

    show elio surprised with hpunch
    vl elio_vl_prefix 12
    e "You what?"

    vl alexis_vl_prefix 11
    a "Some poor boy comes up to me or my younger brother, asks what he can do to get our sister to notice him, we say \"Quit while you’re ahead,\" and then when they crash and burn, we help to pick up the pieces."

    "I sigh and shake my head."

    vl alexis_vl_prefix 12
    a "Maybe I can help your sister accept the possibility of being rejected, but that’s about it."

    show elio neutral with dissolve
    vl elio_vl_prefix 13
    e "So you’re telling me your brother and sister have never come to you about a crush?"

    vl alexis_vl_prefix 13
    a "Nope. I don’t even know if Skylar has crushes…"

    vl elio_vl_prefix 14
    e "That you know of?"

    "There was one time Salem was smitten with a secondary school friend of mine. Suffice it to say, it didn’t work out."

    vl alexis_vl_prefix 14
    a "What advice does your sister even need?"

    vl elio_vl_prefix 15
    e "How to get a guy to notice her."

    "Really, that’s it? This shouldn’t be hard at all, then."

    vl alexis_vl_prefix 15
    a "She could go up to him and ask him out."

    "Again, Elio looks dumbfounded. You’ve got to be kidding me."

    show elio confused with dissolve
    vl alexis_vl_prefix 16
    a "What, you didn’t think of that yourself?"

    vl elio_vl_prefix 16
    e "No way it’s that easy."

    vl alexis_vl_prefix 17
    a "My brother had a crush on a friend. I told him to tell her."

    vl elio_vl_prefix 17
    e "And?"

    vl alexis_vl_prefix 18
    a "She turned him down."

    vl elio_vl_prefix 18
    e "And that’s supposed to help?"

    vl alexis_vl_prefix 19
    a "There was a chance of it working out, and that’s the important part. What if the guy doesn’t already have his eyes on your sister?"

    vl alexis_vl_prefix 20
    a "There’s no chance of anything happening if she sits on her thumbs all day."
    voice sustain
    a "She lets him know he has a chance, maybe it’s the start of something beautiful."

    show elio neutral with dissolve
    vl elio_vl_prefix 19
    e "Anything else? I doubt that’s going to work."

    vl alexis_vl_prefix 21
    a "Well, why not?"

    vl elio_vl_prefix 20
    e "My family…"
    stop music fadeout 1.0

    "He trails off, but I think I get what he’s trying to say. Maybe my parents were just more forward-thinking about this sort of thing."
    "Or maybe a viscount’s family doesn’t have to worry too much about reputation and propriety."

    "I don’t know how high up Elio’s family is, but it isn’t like it’s harder to have a more prestigious title than ours."

    vl alexis_vl_prefix 22
    a "Wouldn’t stand their daughter making the first move?"

    vl elio_vl_prefix 21
    e "Right."

    vl alexis_vl_prefix 23
    a "I say screw them. This is between your sister and her crush. Who cares what your parents think?"

    vl elio_vl_prefix 22
    e "Well, they—"

    vl alexis_vl_prefix 24
    a "How do you feel about it? Would it bug you?"

    "He averts his gaze."
    play music hatchling14 fadein 1.0

    show elio embarrassed with dissolve
    vl elio_vl_prefix 23
    e "Something like this? Trust me, I don’t care one bit."

    vl alexis_vl_prefix 25
    a "And you’re heir, aren’t you? That’s got to count for something."
    voice sustain
    a "You’re going to be in charge some day, and you’ll have the power to say, \"If the lady wants to approach the gentleman, let her.\" Why not let your sister be the start of that?"

    show elio neutral with dissolve
    vl elio_vl_prefix 24
    e "I guess so. But I’d have to convince Alessia to go through with it too…"

    "He sighs."

    vl elio_vl_prefix 25
    e "But like you said, there’s at least a chance of it working out if she does…"

    vl alexis_vl_prefix 26
    a "And next to no chance if she doesn’t. She’s the one that came to you."
    voice sustain
    a "If you bring that up to her, she’ll have to at least consider."

    "Again, he sighs."
    vl elio_vl_prefix 26
    e "And even if she doesn’t, at least there was the chance she would."

    vl alexis_vl_prefix 27
    a "You catch on quickly."

    "The drinks we ordered arrive, longer than the waits I’ve had usually are. Elio picks up his cup of coffee, grimacing at it."

    vl alexis_vl_prefix 28
    a "Something wrong with the drink?"

    vl elio_vl_prefix 27
    e "Just wishing there was some booze in this."

    "I see what he means. Trying to convince a teenager raised in a traditional noble family to toss out traditional roles of courtship might be easier said than done."
    "Not to mention the traditional noble parents that raised that same kid."

    "He’s going to have to hope and pray they don’t clutch their pearls and catch a touch of the vapors at the thought of their daughter doing something other than fluttering her eyelashes at a guy."

    "But just how old-fashioned can Elio’s family really be if he’s that worried?"
    stop music fadeout 1.0

    scene black with fade

    # jump to second club route neralt
    $ renpy.call(chosen_club2 + "_route_neralt", "Neralt", 15)
    #jump student_council_exalt

label archery_route_exalt(month, date):
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Exalt/Elio_Own_Month6_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Elio/Month 6/" + player_voice_prefix + "_Elio_Month6_"

    call screen calendar(month, date, "Exalt", 22)
    scene bg wright_field_night with fade
    play music hatchling14 fadein 1.0

    $ renpy.notify("Elio - United in Grief\nZaeday, Exalt 22nd, 1027 RD")

    "What is someone doing out on the field this late? And in this weather?"
    "I mean, the fact that I’m out and about on a winter evening is peculiar, too, but at least I’m not doing archery in this biting cold."

    "Turning a corner, I find the very person I should’ve expected to find out here."

    show elio neutral with dissolve
    vl alexis_vl_prefix 1
    a "Elio, hey."

    "He looses an arrow and then turns to me, right as it strikes the bullseye."

    #scene bg wright_field_night with hpunch
    with vpunch
    show elio neutral
    vl elio_vl_prefix 1
    e "Hey."

    vl alexis_vl_prefix 2
    a "What’re you doing out in this cold?"

    vl elio_vl_prefix 2
    e "Thinking."

    "Back to being the stellar conversationalist he was earlier in the year, I see. Not like I can blame him."
    "This time of year has a way of getting into a person’s head."

    vl alexis_vl_prefix 3
    a "About family?"

    "He nocks another arrow and trains it on the distant target."

    vl elio_vl_prefix 3
    e "My grandfather."

    "I stand at his side, whistling when this next arrow also strikes the bullseye, sinking itself into the target right next to its twin."

    #scene bg wright_field_night with hpunch
    with vpunch
    show elio neutral
    vl elio_vl_prefix 4
    e "Old man practically raised me. He’s the reason I’m here. Always preferred a bow to a gun for his hunting."

    vl alexis_vl_prefix 4
    a "He must’ve had a crazy good eye."

    vl elio_vl_prefix 5
    e "One of the best sharpshooters the Leon Dragoons has ever seen, he used to tell me."

    vl alexis_vl_prefix 5
    a "Leon?"

    vl elio_vl_prefix 6
    e "House Natale di Leon. It’s a suburb of Alta Maria and the territory we were given to lord over. Grandfather loved that city."

    "He hasn’t yet nocked another arrow, just looks down at it in his palm."

    vl elio_vl_prefix 7
    e "It feels a bit like everything changed when he died."

    vl alexis_vl_prefix 6
    a "Yeah. I think I get what you mean."

    vl elio_vl_prefix 8
    e "You lose someone, too?"

    vl alexis_vl_prefix 7
    a "My father. Nearly eight years ago now."

    "Silently, he fires another arrow, then lets the bow fall to his side."

    #scene bg wright_field_night with hpunch
    with vpunch
    stop music fadeout 1.0

    show elio neutral
    vl elio_vl_prefix 9
    e "A bit like the seam holding everything together finally snaps."
    vl elio_vl_prefix 10
    e "You know, I don’t really give a damn what the Church says."
    voice sustain
    e "But we’re just a few days away from one of the holiest times of year, and I’m getting all sentimental."

    vl alexis_vl_prefix 8
    a "The Week of Life will definitely do that to you. Going home?"

    vl elio_vl_prefix 11
    e "Airship leaves in the morning. Think it’s been long enough since I’ve seen the kids."

    vl alexis_vl_prefix 9
    a "I’m sure they’ll be glad to have their big brother around."

    vl elio_vl_prefix 12
    e "Right."

    "For a few excruciatingly long minutes, we stand in the cold, staring across the field at the target he left out for his own little personal practice session."
    play music hatchling10 fadein 1.0
    "Elio's finally starting to open up, after all this time. Maybe, if I did the same, he’d listen and not just clam up."

    vl alexis_vl_prefix 10
    a "I used to call myself Nyrellan."

    vl elio_vl_prefix 13
    e "And your father’s death changed that?"

    vl alexis_vl_prefix 11
    a "It just felt wrong. That the Divines would let such a good man die such a meaningless death."
    voice sustain
    a "They say the Gods don’t want to get mixed up in mortal affairs anymore, but at that point, why even call them Gods?"

    vl elio_vl_prefix 14
    e "Great question. Wish I had an answer."

    "Another minute passes, then Elio exhales."
    stop music fadeout 1.0

    vl elio_vl_prefix 15
    e "I’ve got some news. Not as depressing."

    vl alexis_vl_prefix 12
    a "Let’s hear it."

    show elio embarrassed with dissolve
    vl elio_vl_prefix 16
    e "Got Alessia to give it a shot."

    vl alexis_vl_prefix 13
    a "And?"

    show elio neutral with dissolve
    "He shakes his head."

    vl elio_vl_prefix 17
    e "Didn’t work. But she’s happy. Says it did a lot for her to get the feelings off her chest."

    vl alexis_vl_prefix 14
    a "Good to know she didn’t blow up at you or anything."

    vl elio_vl_prefix 18
    e "All she did was swear that I’ll buy her all the ice cream she wants while I’m home. If anyone’s going to blow up, it’s Father."

    vl alexis_vl_prefix 15
    a "Good luck with him."

    vl elio_vl_prefix 19
    e "Here’s hoping I won’t need it."
    vl elio_vl_prefix Sneeze
    pause 0.4
    show elio neutral with hpunch
    voice sustain
    "A sudden, violent sneeze racks him."

    vl alexis_vl_prefix 16
    a "Think you’ve spent enough time out in the cold."

    vl elio_vl_prefix 20
    e "Oh really? What gave that away?"

    vl alexis_vl_prefix 17
    a "To the salon?"

    vl elio_vl_prefix 21
    e "Lead the way."

    "We don’t say much on the walk there. But after what we spoke about in the field, I don’t mind it."
    "I guess the fact that he didn’t turn down my invitation makes the silence more than tolerable."

    "I’m sure we’ll have more to say when we’re seating and nursing some nice, warm drinks."

    hide elio with fade
    scene black with dissolve
    
    if chosen_club2 == "enseki":
        call enseki_route_exalt2("Exalt", 22) from _call_enseki_route_exalt2
    else:
        call phillip_elvera("Exalt", 22) from _call_phillip_elvera

label archery_route_elvera(month, date):
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Elvera/Elio_Own_Month7_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Elio/Month 7/" + player_voice_prefix + "_Elio_Month7_"

    call screen calendar(month, date, "Elvera", 30)
    scene bg wright_field_night with fade

    $ renpy.notify("Elio - Why We Do It\nIstday, Elvera 30th, 1028 RD")

    "I yawn, dabbing at the corners of my eyes where they went watery. It’s too early for me to be yearning for sleep now. There’s work to be done."

    "When I asked my teachers if I could do extra credit, I wasn’t quite sure what I was expecting, but I was pleasantly surprised when most of them had something to throw my way."

    "Seeing how damned hard these assignments would be… Well, that was less pleasant. I guess it makes sense, since they’re outside of the regular curriculum, but have mercy…"

    "And, of course, the history assignment is the most unpleasant of all. How in the Abyss am I supposed to know the rationale behind the Great Ennobling? I don’t even know what that is!"

    vl elio_vl_prefix 1
    e "It was a power move."

    "I jump. My head whips around, finding Elio standing at my shoulder. Instead of greeting me, he just taps my worksheet."

    show elio neutral at center with dissolve
    vl elio_vl_prefix 2
    e "Have a big, strong gentry, and no one would mess with the new Empire. That was the idea."

    vl alexis_vl_prefix 1
    a "Thanks…"

    vl elio_vl_prefix 3
    e "Probably want to add that it was a big carrot, too. The land, money, and privilege that came with the titles was the central government's way of saying,"
    voice sustain
    e "\"We did good by you, so defend us if we’re ever embroiled in war.\""

    "I furiously jot down the things he’s saying, a massive weight lifted off of my shoulders."
    play music hatchling14 fadein 1.0

    vl alexis_vl_prefix 2
    a "Man, you saved me. The books I was looking through didn’t say anything about that. Just that it happened, really."

    vl elio_vl_prefix 4
    e "The most important parts of history aren’t in the textbooks. That should be obvious."

    vl alexis_vl_prefix 3
    a "I didn’t know you were a history buff."

    vl elio_vl_prefix 5
    e "I’m not. It’s just my family’s history, so of course I know it."

    "He drops himself into a seat at my side."

    vl elio_vl_prefix 6
    e "You missed a meeting. Again."

    vl alexis_vl_prefix 4
    a "It’s that time of the week already? Sorry about that."
    
    vl elio_vl_prefix 7
    e "What’s up? Trying to not fail?"

    vl alexis_vl_prefix 5
    a "No. More like trying to stand out. My grades aren’t terrible, but they’re not good enough."

    show elio confused with dissolve
    vl elio_vl_prefix 8
    e "Not good enough for what?"

    "Not good enough for what indeed? How do I explain it? The gears in my head start grinding, trying to figure out some way to put it into words."

    "Nothing comes to me, in the end. So I keep it short and simple. It’s mostly the truth, anyhow."

    vl alexis_vl_prefix 6
    a "Better grades, better university, better job, more money."

    vl elio_vl_prefix 9
    e "What do you need money for? Your family should be set, shouldn’t they?"

    "I don’t answer right away, which is all he needs."

    vl elio_vl_prefix 10
    e "Not trying to be a dick, but you sure it was a good idea to come to this school if your family has money troubles?"

    vl alexis_vl_prefix 7
    a "It wouldn’t be much of an issue if I had stuck to my mother’s plan…"

    show elio neutral with dissolve
    vl elio_vl_prefix 11
    e "Oh, yeah? What was this plan?"

    "Again, I fall silent. This is going to sound terrible, isn’t it? I sigh. May as well rip off the bandage and tell him."

    vl alexis_vl_prefix 8
    a "Seduce someone well-off."

    "His eyes widen, utter bafflement written plainly on his face."

    show elio surprised with hpunch
    vl elio_vl_prefix 12
    e "You? Seduce someone?"

    vl alexis_vl_prefix 9
    a "Little harsh, don’t you think?"

    vl elio_vl_prefix 13
    e "Not as harsh as your mother wanting you to use someone for their money."

    "The bluntness of his words make me wince. He’s completely right, after all."

    show elio neutral with dissolve
    vl elio_vl_prefix 14
    e "So, now that we’re only a few months to graduation, and you’re  as single as you started, you’re trying to pivot?"

    # TODO: Missing voice line in Elio Month 7
    #vl alexis_vl_prefix 10
    a "At a school like this, I have options. If the romance route is a bust, then I’ll just take advantage of the school’s reputation to work my way up. It’ll work out. It has to."

    "Enough time passes with us sitting in silence that I get back to my work. My eyes flit over to Elio from time to time."
    "He’s not saying anything, but he hasn’t left me either. Why is that?"

    "I don’t know how much time passes until he next speaks, but when he does, it catches me off guard."

    vl elio_vl_prefix 15
    e "No promises, but I might have an idea."

    vl alexis_vl_prefix 11
    a "What is it?"

    vl elio_vl_prefix 16
    e "Ever consider being a tutor?"

    vl alexis_vl_prefix 12
    a "Come again?"

    vl elio_vl_prefix 17
    e "My two younger siblings."
    voice sustain
    e "I expect my father wouldn’t be as generous as if it was some famous academic, but he’d still pay well for someone to make sure his kids get good grades."

    vl elio_vl_prefix 18
    e "Might help that you’re a noble yourself. He’d probably think he’s offending you if the offer was too low."

    vl alexis_vl_prefix 13
    a "How good are we talking?"

    vl elio_vl_prefix 19
    e "How much money do you think a marquess has to throw around?"

    "A marquess? Elio’s family is more important than I thought. And he’s really offering to help me out like this?"
    
    vl alexis_vl_prefix 14
    a "I’m sure it’s a lot, but…"

    vl elio_vl_prefix 20
    e "Nowhere near enough for what you’re hoping to do? Then… maybe I can refer you to some of the family accountants."
    voice sustain
    e "They might help you and your parents get the finances in order."

    vl alexis_vl_prefix 15
    a "You’re really willing to do all of this for me?"

    "He chuckles."

    vl elio_vl_prefix 21
    e "Trying to worm your way into someone’s heart isn’t the only way to get their help. Friends help each other, don’t they?"

    "I look back down at my work, tapping the sheet with my pencil. At the sound of the chair being pushed back, I glance up at him."

    vl elio_vl_prefix 22
    e "Just think it over, alright?"

    vl alexis_vl_prefix 16
    a "I will. Thanks…"

    vl elio_vl_prefix 23
    e "And try not to skip club next time."

    "With a casual wave, he leaves me in the library. Again, I yawn. Maybe I’ve done enough today."
    "Besides, after that conversation, I’m not sure I’d be able to properly focus on all of this work anyway."

    "I’ll pack up and head back to House Lychester. But maybe after a short nap."
    stop music fadeout 1.0

    scene black with dissolve
    call archery_route_verabris("Elvera", 30) from _call_archery_route_verabris

label archery_route_verabris(month, date):
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Verabris/Elio_Own_Month8_"
    $ noble_lady_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Noble Lady/NobleLady_Elio_Month8_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Elio/Month 8/" + player_voice_prefix + "_Elio_Month8_"

    call screen calendar(month, date, "Verabris", 8)
    scene bg chapel_day with fade
    play music hatchling21 fadein 1.0

    $ renpy.notify("Elio - Out\nLenday, Verabris 8th, 1028 RD")

    "Of all the places I expected to find myself with Elio, this was last on the list."
    "I sit beside him in the pews, the building empty save for us and the presiding priest, working in his office."

    "Elio looks up at the various depictions of the Divines in the stained glass windows."

    show elio neutral at center with dissolve
    vl alexis_vl_prefix 1
    a "And here I thought you weren’t religious."

    vl elio_vl_prefix 1
    e "I’m not."

    "I expected some sort of annoyance in response to my little jab, but nothing. His voice is practically void of any emotion."

    vl elio_vl_prefix 2
    e "There’s just something about places like this that…"

    "He trails off, but I understand him. Father’s death might’ve made it impossible for me to fully believe in the Divines, but I wasn’t left with any animosity towards the Church."
    "Just indifference."

    vl alexis_vl_prefix 2
    a "If you were drawn to it, I’m guessing there’s something on your mind?"

    vl elio_vl_prefix 3
    e "You could say that."

    "He takes a letter out of his pocket and hands it to me. While I’m a bit confused, I take it and begin to read."

    vl noble_lady_vl_prefix 1
    "\"My dearest Elio, I hope you are doing well. I struggle to believe that it’s been a mere two months since we met."
    voice sustain
    "It feels like it’s been so much longer, which only serves to make our time apart more agonizing."
    
    vl noble_lady_vl_prefix 2
    "\"You will be returning to Leon for break at the end of the month, yes? My heart leaps with joy at the thought of seeing you again."
    voice sustain
    "If I may be so bold, I’ve put much thought into what we can do, in the limited time you are here."

    vl noble_lady_vl_prefix 3
    "\"I hope you’ll do me the honor of spending some time with me, when you are able.\""

    "It goes on, but I stop there. Seems like it starts going into more of what the sender’s been up to lately, and I don’t want to pry. My eyes go to the bottom of the page."
    "That is definitely a lady’s name."

    vl alexis_vl_prefix 3
    a "You have a girlfriend?"

    "Or would \"betrothed\" be the better word, for a marquess’s son?"

    vl elio_vl_prefix 4
    e "Not willingly. Father sprung her on me when I went home at the end of last year."

    vl alexis_vl_prefix 4
    a "What, you don’t like her? Sure, a letter’s a little old-fashioned, but she seems sweet."

    "I’m taken aback by the cascade of emotion that parade across his face. Uncertainty, discomfort, anxiety."

    show elio embarrassed with dissolve
    vl elio_vl_prefix 5
    e "I like her, but I don’t like her. We’re incompatible in the most fundamental sense of the word."

    "Well, that would explain why he felt the need to come to church."

    vl alexis_vl_prefix 5
    a "There’s no harm in breaking things off, is there? Surely she and your family would understand."

    show elio neutral with dissolve
    vl elio_vl_prefix 6
    e "They would, but…"

    vl alexis_vl_prefix 6
    a "But?"

    vl elio_vl_prefix 7
    e "It’s not in the cards. Not for me. Maybe if I were my brother, but I’m not."

    vl alexis_vl_prefix 7
    a "You lost me."

    vl elio_vl_prefix 8
    e "I thought you’d understand. After all, you’re the one at this school and not one of your siblings, aren’t you?"

    stop music fadeout 1.0
    "His words cut me to the bone. A duty to serve the family and ensure its future."
    "A duty almost uniquely placed upon the shoulders of whoever had the misfortune of being born first."

    vl alexis_vl_prefix 8
    a "Come on, that’s insane. You don’t have to do that."

    vl elio_vl_prefix 9
    e "The first-born child of House Natale’s always been the one to inherit the title. And they’re always sure to produce an heir so the line remains unbroken."

    vl alexis_vl_prefix 9
    a "And you’re determined to make sure that doesn’t end with you?"

    "He falls silent."

    vl alexis_vl_prefix 10
    a "That isn’t what you want, is it?"

    vl elio_vl_prefix 10.1
    e "It doesn’t matter what I want. What matters is what’s right by my family."

    vl alexis_vl_prefix 11
    a "And this is it?"

    vl elio_vl_prefix 11
    e "What else is? This is the responsibility I was born with. I can’t just abandon it."

    "For all my insistence that I don’t care about the Gods, I hesitate to say what I’m about to say in a house of worship."

    "But if Elio’s convinced himself he needs to marry a girl he just met and could never love out of some twisted sense of duty, I have to say it."

    vl alexis_vl_prefix 12
    a "Imagine yourself in bed with this girl. And I don’t just mean sleeping together."

    "He blanches, and for a second I damn near think he’s going to gag."

    vl alexis_vl_prefix 13
    a "Do you want to do that to her? To yourself?"

    vl elio_vl_prefix 12
    e "I…"

    vl alexis_vl_prefix 14
    a "Do you really want your children’s parents to be nothing more than roommates? And that’s the best case scenario."
    voice sustain
    a "You think that’s the best thing for your family?"

    vl alexis_vl_prefix 15
    a "The whispers about your loveless marriage? Your dead bedroom? The affairs that would no doubt happen?"

    "He hunches over, clasping his hands together. It almost looks like he’s praying."

    "I don’t say any more, but it doesn’t look like I have to. We sit in the serene silence of the chapel while Elio sorts the things I said."
    "When he finally sits up, he sighs."

    vl elio_vl_prefix 13
    e "I don’t exactly like the idea of breaking a lady’s heart."

    vl ("<to 4.9>" + alexis_vl_prefix) 16
    a "Better to make it quick and dirty than drawn-out and agonizing."

    "I pause, thinking of something to say that will hopefully put him at ease."

    vl ("<from 5.1>" + alexis_vl_prefix) 16
    a "Sure, popping out an heir’s one way to serve your family, but there are others, too."
    voice sustain
    a "What did all the other younger siblings do? What are your younger siblings going to do?"
    vl alexis_vl_prefix 17
    a "Don’t beat yourself up over something like this."

    vl elio_vl_prefix 14
    e "Right. Right…"

    "We don’t say anything else after that, passing the rest of the morning in each other’s company."
    "It’s the awkward growl of a stomach that brings us back down to Unios and out of the chapel, en route to a restaurant in town."

    "The biggest hurdle in Elio’s path is himself. Today, he overcame it, but I hope that was a true victory and won’t come back to trip him up later."

    scene black with dissolve
    
    #jump to second clubd route verabris
    $ renpy.call(chosen_club2 + "_route_verabris", "Verabris", 8)
    #jump student_council_verabis

label archery_route_overa(month, date):
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Elio Epilogue/Elio_Own_Epilogue_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Elio/Epilogue/" + player_voice_prefix + "_Elio_Epilogue_"

    call screen calendar(month, date, "Overa", 24)
    scene bg wright_field_noon with fade
    play music hatchling14 fadein 1.0

    $ renpy.notify("Elio - Epilogue\nToleday, Overa 24th, 1028 RD")

    "The final archery club meeting of the year just wrapped up. Everyone else is long gone, but Elio and I remained behind on the field, shooting in silence."

    "I only got to enjoy this for a single year. So, if this is my last time on the field, I may as well make the most of it, right?"

    "Across the field, the sound of Elio’s shooting stops. I’m able to fire a few more arrows of my own before he speaks."

    show elio neutral at center with dissolve
    vl elio_vl_prefix 1
    e "Hey."

    "I lower my bow."

    vl alexis_vl_prefix 1
    a "What’s up?"

    vl elio_vl_prefix 2
    e "Thanks for this year."
    stop music fadeout 1.0

    vl alexis_vl_prefix 2
    a "What did I do?"

    vl elio_vl_prefix 3
    e "Being my friend, obviously. It might surprise you, but I didn’t have many."

    "Thinking back to his behavior our first month, I let out a wry laugh."

    vl alexis_vl_prefix 3
    a "I’m super surprised."
    play music hatchling10 fadein 1.0

    show elio happy with dissolve
    vl elio_vl_prefix 4
    e "It’s weird. I wasn’t expecting to meet someone who… gets me so well. There was always a chasm between me and other people because my life is so…"

    vl alexis_vl_prefix 4
    a "Extraordinary?"
    
    show elio neutral with dissolve
    vl elio_vl_prefix 5
    e "In a sense."

    "The firstborn of a noble family with some sort of storied military tradition. Quite a few crossroads there."

    "And even though plenty of people tick off one or two of those boxes at this school, I guess it is rare that someone would tick off all of them and then cross paths with Elio like I did."

    vl alexis_vl_prefix 5
    a "Well, you’re welcome. You’re not a bad guy, after I got past that prickly outer layer."

    vl elio_vl_prefix 6
    e "Did you just call me prickly?"

    vl alexis_vl_prefix 6
    a "Don’t try to deny it."

    vl elio_vl_prefix 7
    e "Ass."

    vl alexis_vl_prefix 7
    a "I could say the same about how you were at the start."

    "I’m starting to run out of arrows myself."

    vl alexis_vl_prefix 8
    a "How about we clean up and get out of here? I could go for some dinner."
    stop music fadeout 1.0

    jump archery_route_overa_choice

label archery_route_overa_choice:
    if player_gender == "female":
        $ elio_platonic = True
        jump archery_route_overa_platonic
    else:
        jump archery_route_overa_romance

label archery_route_overa_platonic:
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Elio Epilogue/Platonic/Elio_Own_Epilogue_Platonic_"

    show elio neutral at center with dissolve
    vl elio_vl_prefix 1
    e "Let’s. My treat, too."

    a "You spoil me, my good sir."

    vl elio_vl_prefix 2
    e "Probably the least I can do to make up for how I started the year."

    "A night out with a friend doesn’t seem like a bad way to end the year. Not at all."
    "I just hope that the future will present us plenty more chances to do this again."

    scene black  with dissolve
    call epilogue_graduation("Overa", 24) from _call_epilogue_graduation

label archery_route_overa_romance:
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Elio Epilogue/Romantic/Elio_Own_Epilogue_Romantic_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Elio/Epilogue/" + player_voice_prefix + "_Elio_Epilogue_"

    "He turns away from me, mulling something over. When he turns back to me, the look in his eyes sends a chill down my spine."

    show elio embarrassed with dissolve
    vl elio_vl_prefix 1
    e "Before that, there’s something I want to say."

    vl alexis_vl_prefix 9
    a "Y-yes?"

    "Again, he falls silent, trying to find the words."

    vl elio_vl_prefix 2
    e "It’s hard to find anyone who really understands me the way you do."
    voice sustain
    e "Even harder to find a guy who does… Things are just easier without having to explain everything about how my world works all the damn time."

    vl alexis_vl_prefix 10
    a "I get what you mean."

    vl elio_vl_prefix 3
    e "It’s getting harder and harder to imagine my life without you in my corner, so…"

    "Words fail him. So it’ll be up to me to fill the gap."

    $ elio_romance = None

    menu:
        "Accept Elio's confession":
            $ elio_romance = True
            jump archery_route_overa_romance_accept

        "Reject Elio's confession":
            $ elio_romance = False
            jump archery_route_overa_romance_reject

label archery_route_overa_romance_accept:
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Elio Epilogue/Romantic/Acceptance/Elio_Own_Epilogue_Romantic_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Elio/Epilogue/" + player_voice_prefix + "_Elio_Epilogue_"

    vl alexis_vl_prefix 11
    a "Then I’ll stick around. Your corner’s pretty damn cozy anyway."

    "He smiles."
    play music hatchling10 fadein 1.0

    show elio happy at center with dissolve
    vl elio_vl_prefix 4
    e "Could you be more corny?"

    vl alexis_vl_prefix 12
    a "Do you want me to try?"

    vl elio_vl_prefix 5
    e "Please don’t."

    "He approaches, gingerly taking my free hand in his."

    vl elio_vl_prefix 6
    e "I’ve been scared, you know."

    vl alexis_vl_prefix 13
    a "Of?"

    vl elio_vl_prefix 7
    e "Breaking off that engagement. But now I can’t wait to bust down the door and tell my father, \"I’ve found the one I want to be with!\""

    "The thought of him doing that makes me laugh."

    vl alexis_vl_prefix 14
    a "Damn, I want to be there to see that."

    vl elio_vl_prefix 8
    e "Could you be? It would be easier to do it, if I weren’t alone."

    vl alexis_vl_prefix 15
    a "Of course. Just tell me when, and I’ll buy the first airship ticket I can find."

    "Which, in all likelihood, is going to be soon, with the summer right around the corner."
    "The idea of meeting Elio’s family so soon, and in those circumstances, is nerve-wracking and exciting all at the same time."

    "We share a moment of blissful silence then resume cleaning up."
    "For as nice as the weather is this time of year, better to enjoy each other’s company over some nice food and not standing on a track by the gymnasium."

    "As we set out, I have a feeling this dinner is going to be one of the nicest I’ve ever had. And this is just the beginning."
    "I can only imagine all of the things more grand than a simple dinner that we’ll be able to share in the future."
    stop music fadeout 1.0

    scene black with dissolve
    call epilogue_graduation("Overa", 24) from _call_epilogue_graduation_1

label archery_route_overa_romance_reject:
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Elio Route/Elio Epilogue/Romantic/Rejection/Elio_Own_Epilogue_Romantic_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Elio/Epilogue/" + player_voice_prefix + "_Elio_Epilogue_"

    vl alexis_vl_prefix 16
    a "I’m on your side, but not in the way you think."

    show elio neutral with dissolve
    vl elio_vl_prefix 9
    e "Is that so?"

    "He begins marching towards his target."

    vl alexis_vl_prefix 17
    a "Elio, wait!"
    play music hatchling10 fadein 1.0

    show elio confused with dissolve
    vl elio_vl_prefix 10
    e "You said we should clean up and get food. What’s the hold up?"

    vl alexis_vl_prefix 18
    a "Maybe it came out wrong. Listen—"

    show elio angry with dissolve
    vl elio_vl_prefix 11
    e "Forget it."

    vl alexis_vl_prefix 19
    a "Just listen to me for a second!"

    "The force in my voice stuns him."

    vl alexis_vl_prefix 20
    a "You are a dear friend to me. I could go on and on about how amazing it’s been to get to know you this year."
    voice sustain
    a "I just can’t return these feelings, and for that, I’m sorry."
    
    vl alexis_vl_prefix 21
    a "But that doesn’t mean I won’t fully support you in the future, no matter what gets thrown your way."

    "His expression does soften, at least a bit. I go on."

    vl alexis_vl_prefix 22
    a "I’m sure the best man spot at your wedding’s reserved for your brother, but let me get a spot as one of your groomsmen, alright?"

    "He looks confused, and that confuses me in turn."

    vl alexis_vl_prefix 23
    a "What, you think you’re not going to find someone else?"
    vl alexis_vl_prefix 24
    a "Elio, there are billions of people on the planet. There’s someone out there for you. You just haven’t met them yet."

    show elio confused with dissolve
    vl elio_vl_prefix 12
    e "I… it’s just fresh, you know?"

    vl alexis_vl_prefix 25
    a "Yeah."

    "And because it is, it’s probably best if I gave him space."

    show elio neutral with dissolve
    vl alexis_vl_prefix 26
    a "Mind if I go on ahead? If you still wanted dinner…"

    vl elio_vl_prefix 13
    e "I’m the president, so it’s my job to clean up anyway. I’ll let you know about dinner."

    vl alexis_vl_prefix 27
    a "Talk to you later, then?"

    vl elio_vl_prefix 14
    e "Yeah, later."

    "I leave him, my heart still heavy. He said it himself last month, and I find that I agree. I’m no fan of breaking hearts."
    "I just hope he heard me when I said he was important to me, even if not in that way."

    "I doubt dinner’s happening. But hopefully it will some other day. This disappointment doesn’t overwrite everything else Elio and I have been through together this year."
    "All I can do is wait and see if he sees that simple truth the same way I do."
    stop music fadeout 1.0
    
    scene black with dissolve
    call epilogue_graduation("Overa", 24) from _call_epilogue_graduation_2

label epilogue_archery_route:

    scene bg maincastle with fade 

    "I finally make it to the park. Unfortunately, there are a few more people around than I’d like. Now where are they…?"
    jump epilogue_elio_choice

label epilogue_elio_choice:
    if chosen_club == "archery":
        if elio_romance:
            jump epilogue_archery_route_romance_accept
        elif elio_platonic:
            jump epilogue_archery_route_platonic
        else: 
            jump epilogue_archery_route_romance_reject
    else:
        jump epilogue_archery_route_not_chosen

label epilogue_archery_route_romance_accept:
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Shared Epilogue/Epilogue/Confession Accepted/Elio_Shared_Epilogue_ConfessionAccepted_"

    show elio neutral with dissolve
    if eval(a.name)[0] == "Alexis":
        vl elio_vl_prefix 1A
    else:
        vl elio_vl_prefix 1B
    e "Hey, [a]."

    a "Elio, hey! Congrats on graduating."

    vl elio_vl_prefix 2
    e "Same to you. What’s up?"

    a "Looking for my family."

    "I hesitate, then ask the question that popped into my head the moment I answered his."

    a "Is your family around?"

    vl elio_vl_prefix 3
    e "They’re here. And so is she…"

    a "She is?"

    show elio embarrassed
    vl elio_vl_prefix 4
    e "I’m going to be meeting up with her later. I’ll try to tell her then."
    voice sustain
    e "If the mood is right. Sure, it’s my big day, but it isn’t like she wasn’t looking forward to it, too."

    a "Good luck. I don’t know her, but I don’t think she’ll be upset."

    vl elio_vl_prefix 5
    e "I know she won’t. I just hope she doesn’t feel guilty."

    a "And, after that…"

    show elio neutral with dissolve
    vl elio_vl_prefix 6
    e "We get you on a flight north. Soon."

    a "Soon."

    vl elio_vl_prefix 7
    e "Don’t want to keep your family waiting too long, right? You should get back to looking for them."

    a "You’re right. I’ll talk to you soon, Elio."

    #show scene black with fade
    #jump reuinion
    jump epilogue_scouts_route

label epilogue_archery_route_romance_reject:
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Shared Epilogue/Epilogue/Confession Rejected/Elio_Shared_Epilogue_ConfessionRejected_"

    show elio neutral at center with dissolve
    if eval(a.name)[0] == "Alexis":
        vl elio_vl_prefix 1A
    else:
        vl elio_vl_prefix 1B
    e "Hey, [a]."

    a "Elio, hey! Congrats on graduating."

    vl elio_vl_prefix 2
    e "Same to you. What’s up?"

    a "Looking for my family."

    vl elio_vl_prefix ThroatClear
    "There’s a moment of silence, then Elio clears his throat."

    show elio embarrassed
    vl elio_vl_prefix 3
    e "I’m sorry about dinner."

    "He never did show up that night, just like I expected."

    a "Don’t worry about it. Not very surprising, considering everything."

    vl elio_vl_prefix 4
    e "Make it up to you sometime soon?"

    a "I like the sound of that. Might not get a chance to do that anytime soon, though."

    show elio neutral with dissolve
    vl elio_vl_prefix 5
    e "Then you get to lord it over me until we do."

    a "Don’t mind if I do, then."

    vl elio_vl_prefix 6
    e "Don’t want to keep your family waiting too long, right? You should get back to looking for them."

    a "You’re right. I’ll talk to you later, Elio."
    
    #scene black with fade
    #jump reuinion
    jump epilogue_scouts_route

label epilogue_archery_route_platonic: 
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Shared Epilogue/Epilogue/No Confession/Elio_Shared_Epilogue_NoConfession_"

    show elio neutral at center with dissolve
    if eval(a.name)[0] == "Alexis":
        vl elio_vl_prefix 1A
    else:
        vl elio_vl_prefix 1B
    e "Hey, [a]."

    a "Elio, hey! Congrats on graduating."

    vl elio_vl_prefix 2
    e "Same to you. What’s up?"

    a "Looking for my family."

    "I’m reminded of a talk we had a while ago. It completely slipped my mind, and here we are, already graduated."

    a "Think you could hook us up with that accountant you mentioned?"

    vl elio_vl_prefix 3
    e "No problem. I’ll talk them into giving you a discount, too."

    a "That would mean a lot."

    vl elio_vl_prefix 4
    e "And good luck with that degree you said you wanted to get. Crazy to think you want to go back to school."

    a "Well, duty calls."

    vl elio_vl_prefix 5
    e "Ain’t that the truth."
    vl elio_vl_prefix 6
    e "Don’t want to keep your family waiting too long, right? You should get back to looking for them."

    a "You’re right. I’ll talk to you soon, Elio."

    #scene black with fade
    #jump reuinion
    jump epilogue_scouts_route

label epilogue_archery_route_not_chosen: 
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Shared Epilogue/Epilogue/Route Not Chosen/Elio_Shared_Epilogue_RouteNotChosen_"

    "I bump into someone. Again. I’m cursed, aren’t I?"

    show elio neutral at center with dissolve
    a "So sorry about that."

    vl elio_vl_prefix 1
    e "Yeah, sure. Oh, it’s you."

    a "Yeah, it’s me."

    vl elio_vl_prefix 2
    e "Congrats."

    a "Congratulations to you too."

    "A small, awkward moment of silence passes between us. Then, with a nod, he leaves me."

    #scene black with fade
    #jump reuinion
    jump epilogue_scouts_route

label reuinion_archery_route:
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Shared Epilogue/Epilogue/Meet the Family/Elio_Shared_Epilogue_MeetTheFamily_"
    $ arline_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Arline/Epilogue/Meet Elio/Arline_Epilogue_MeetElio_"
    $ skylar_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Skylar/Meet Elio/Skylar_Epilogue_MeetElio_"
    $ salem_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Salem/Meeting Elio/Salem_Epilogue_MeetElio_"

    $ renpy.notify("Elio - Meeting the Family\nNyday, Overa 25, 1028 RD")

    show elio neutral at center with dissolve
    "When Elio arrives, Skylar starts."

    vl skylar_vl_prefix 1
    sky "How did you pull him?"

    a "Gee, thanks."

    vl salem_vl_prefix 1
    salem "Ha!"

    vl arline_vl_prefix 1
    arline "Skylar, that’s rude!"

    vl skylar_vl_prefix 2
    sky "I-I’m sorry, I just…"

    "She flushes and falls silent."

    show elio confused with dissolve
    vl elio_vl_prefix 1
    e "Nice to meet you guys?"

    vl arline_vl_prefix 2
    arline "Forgive my daughter. I wasn’t expecting that out of her."

    vl salem_vl_prefix 2
    salem "Well, I sure did."

    vl skylar_vl_prefix 3
    sky "And what is that supposed to mean, jackass?"

    vl arline_vl_prefix 3
    arline "Skylar!"

    vl salem_vl_prefix Snicker
    "Salem snickers."

    vl salem_vl_prefix 3
    salem "\"How vulgar.\""

    vl skylar_vl_prefix 4
    sky "Curse you for using my words against me!"

    vl arline_vl_prefix ClearThroat
    "Mother clears her throat. Several times."

    vl arline_vl_prefix 4
    arline "Ignore them. Elio, I take it you’re Marquess Leon’s son?"

    show elio neutral with dissolve
    vl elio_vl_prefix 2
    e "That’s right, ma’am."

    vl arline_vl_prefix 5
    arline "If I’m not wrong, a Natale fought alongside the progenitor of our house in Estary."

    vl elio_vl_prefix 3
    e "\"Blakesly,\" right? I think I’ve heard a bit about a \"Black Wolf\" from around then."

    vl arline_vl_prefix 6
    arline "Yes, that would be him!"

    hide elio with fade
    "As Elio and Mother talk, I go over to the twins."

    a "Are you alright, Skylar? Wasn’t expecting to see you so riled up."

    vl skylar_vl_prefix 5
    sky "Your boyfriend’s hot. Can you blame me?"

    vl salem_vl_prefix 4
    salem "Careful now, she might try to steal him from you."

    vl skylar_vl_prefix 6
    sky "Give me some credit. I’m not that evil."

    a "Wouldn’t work, anyway. We’ve talked about this."

    vl salem_vl_prefix 5
    salem "You what now?"

    vl skylar_vl_prefix 7
    sky "And why did you two talk about me stealing him?"

    a "Not you specifically! Just… never mind."

    "Skylar keeps to herself until Elio leaves, while Salem seems interested in his archery prowess."
    "Mother seems to find it amusing that, after well over a century, the Blakesley and Natale families have been brought together again in some fashion."

    "I don’t know what I expected when I called Elio, but it definitely wasn’t this. When he leaves, though, he’s smiling. So at least I know it wasn’t all bad."
    jump finale