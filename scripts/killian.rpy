label anime_route_jinus(month, date):
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Killan_Own_Month1_"
    $ clubregular1_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Club Regular 1/Killian Month 1/ClubRegular1_Killian_Month1_"
    $ clubregular2_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Club Regular 2/Killian Month 1/ClubRegular2_Killian_Month1_"

    call screen calendar(month, date, "Jinus", 1)
    scene bg dorm_common_noon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Killian - Gates Open\nToleday, Jinus 1st, 1027 RD")

    "So many people in such little time. I can barely remember faces, never mind their names. It all feels like the bends and I'm in dire need to decompress."
    #a "Now, I could just lie down and fling my body clock out the window with a quick three-hour nap..."
    "Now, I could just lie down and fling my body clock out the window with a quick three-hour nap but it’s my first week at MIA."
    "There’ll be other times to snooze but making sure that my first impressions impress the right people won’t come again during my time as a fourth-year."
    stop music fadeout 1.0

    call screen calendar("Jinus", 1, "Jinus", 2)
    scene bg classroom_anime_afternoon with fade
    play music hatchling22 fadein 1.0

    $ renpy.notify("Killian - Gates Open\nNyday, Jinus 2nd, 1027 RD")

    "This place has plenty of clubs, I'd think that there'd at least be one that was quiet..."
    "...In times like these, I start to envy Dad. At least you get some peace and quiet for a bit when they bury you."

    "Eventually, I rock up to classroom 3-3. Initially, I was looking for whatever classroom was baking cookies but I ended up opening the wrong door."

    show killian happy at center:
        zoom 1.1
    
    vl killian_vl_prefix 1.1    
    k "Greetings, don't be shy! Welcome to Magiana Imperial's very own abode for special artistic interests!"
    voice sustain
    k "Yes, the very nice, very quaint Anime and Manga Association! Or AMA, for short."
    vl killian_vl_prefix 2.1
    k "Oh! And yours truly, President Killian Moto."
    
    show killian surprised with dissolve
    vl killian_vl_prefix 3.1
    k "Hold up! I know you... You're the secret first-year from earlier..."

    "President Moto eyes me like he did before, only from a swivel chair now."

    show killian neutral with dissolve
    a "In the flesh. Blakesley. [a] Blakesley. And I'm not a first-year. Just a transfer student."

    show killian happy with dissolve
    vl killian_vl_prefix 4.1
    k "I knew it! That banal quirk never ceases to fail me."
    
    stop music fadeout 1.0
    show killian angry with dissolve
    "Killian backs up but looks me up and down from his chair more suspicious than before."
    play music hatchling2 fadein 1.0

    vl killian_vl_prefix 5.1
    k "Why are you here, Mx. Blakesley? Come to poach from our free manga library, hm? Did the IAH send you?"

    "I look around and see a few awkward first and second year students are watching quietly across the room."
    "The projector shows a super-powered fisherman beating up a feathery naval officer while a tiny bear cub in a bowler hat keeps crying."

    a "What? No and no. I mean, why not? I come in peace."

    show killian neutral with dissolve
    "Killian gets up from his chair and straightens his posture, looking even taller than before."
    stop music fadeout 1.0
    "I honestly get the impression that he's got some sort of beef with me."
    show killian disgust with dissolve
    "I can hear him breathing intensely through his nose and it reminds me of a bull who's about to charge."

    "While I'm still trying to tell whether or not this is how this person intimidates people, I'm struggling to fight back a laugh as his straight face is getting to me."

    vl clubregular1_vl_prefix 1
    anek "You're doing great! They do this bit with everyone!"
    play music hatchling12 fadein 1.0

    show killian embarrassed with dissolve
    "The room relaxes with some much needed chuckles and laughs."
    "The president's intensity melts away into something much more natural and, quite frankly, much dorkier."

    show killian sad
    vl killian_vl_prefix 6.1
    k "Damn it all, it's tradition!"

    vl clubregular2_vl_prefix 1
    anek2 "Shut up with your tradition already! Rikki's hitting top gear against Vapes!"

    show killian happy with dissolve
    "Killian relents and finally reveals a warm smile and kind eyes behind those glasses of his."

    vl killian_vl_prefix 7.1
    k "Sorry about that, I just needed to know if you came here with good intent or intended to denigrate the organization."
    voice sustain
    k "Though, I should've suspected the former. Most trolls don't show up in person."
    voice sustain
    k "Please, feel free to grab a seat."

    "And from there, he tells me a bit about the Anime Club and how he joined as a first-year, later inheriting the organization after the previous president."
    "And then growing the org's attendance average by 75\% (attendants before: 1; attendants now: 4)."

    show killian neutral with dissolve
    vl killian_vl_prefix 8.1
    k "Anyway, enough exposition. Can I be honest with you about something?"

    a "Uh, sure?"
    "I really hope he doesn't make shit weirder already..."

    show killian sad with dissolve
    vl killian_vl_prefix 9.1
    k "My intuition has often guided me throughout life by pointing out friends from foes."
    voice sustain
    k "You strike me as one of the former."

    a "Good to know?"

    show killian embarrassed with dissolve
    vl killian_vl_prefix 10.1
    k "What I'm trying to get at here is that I never thought that you were the type to take interest in anime and manga."

    a "Oh? And what makes you say that?"

    show killian surprised with hpunch
    vl killian_vl_prefix 11.1
    k "I mean... You look normal."

    a "...What's that supposed to mean?"

    show killian fear with dissolve
    vl killian_vl_prefix 12.1
    k "Like... You know... It's not like... I'm not trying to..."

    a "Stereotype?"

    show killian happy with dissolve
    vl killian_vl_prefix 13.1
    k "Exactly!"
    show killian fear with dissolve
    vl killian_vl_prefix 14.1
    k "...Wait, I meant, like, not trying to stereotype you because that'd be messed up and we just met."
    voice sustain
    k "Not that I'd start after we ge-"

    a "Wow. Just wow."
    "Quite the tongue for an elected official. It's kinda cute really. Y'know, until he actually starts feeling bad about himself."

    show killian sad with dissolve
    a "Relax, I'm messing with you."

    show killian sad with dissolve
    vl killian_vl_prefix 15.1
    k "Oh, thank the gods!"
    stop music fadeout 1.0

    scene black with fade
    "All in all, despite the way things started, I'm glad I got a chance to get to know President Moto."
    "And maybe I'll get to know more about him during the next club meeting."
    
    #Jump to phillip jinus
    call phillip_jinus("Jinus", 2) from _call_phillip_jinus_1
    #jump anime_route_dallinus

label anime_route_dallinus(month, date): 
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Killan_Own_Month2_"
    $ clubregular1_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Club Regular 1/Killian Month 2/ClubRegular1_Killian_Month2_"
    $ clubregular2_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Club Regular 2/Killian Month 2/ClubRegular2_Killian_Month2_"

    call screen calendar(month, date, "Dallinus", 19)
    scene bg classroom_anime_afternoon with fade
    play music hatchling22 fadein 1.0

    $ renpy.notify("Killian - Trash Tastes\nNyday, Dallinus 19th, 1027 RD")

    a "If there's anything to say about MIA's Anime and Manga Association, it's definitely an interesting time."
    a "I guess watching nerds argue about fiction in person is its own sort of live show."

    show killian angry at center with dissolve:
        zoom 1.1
    
    vl killian_vl_prefix 1.1
    k "...Rikki is a terrorist."
    "And, thankfully, it's better than theater. At least when Killian's on a roll with his hot takes."

    show killian angry with vpunch
    vl killian_vl_prefix 2.2
    k "He's a freedom fighter in the most honorable sense of the word!"
    voice sustain
    k "They're literally fighting a corrupt one-world government led by their top sailors!"
    voice sustain
    k "He's literally fighting the navy and motherfuckers keep telling me Blue Meridian's not political?!"

    "I'd probably be cracking up like everyone else in the room if I watched Blue Meridian—or anime in general."
    "Killian's been trying to win me over with them but he's yet to break me in that regard."
    "Still, out of context, it's certainly one of the opinions of all time."

    show killian happy at center
    vl killian_vl_prefix 3.1
    k "Say, Mx. Blakesley! What do you think?"

    a "Huh?"
    "One of the regulars mumbles something under their breath. Probably something about me being a 'normie'."
    
    show killian sad at center
    "Killian gives me a strained but sympathetic look."

    show killian neutral with dissolve
    vl killian_vl_prefix 4.1
    k "Never mind them. Here, let's switch topics so you can partake in the discourse."
    "Thank the Gods. It's good to know that this guy isn't completely a single-interest personality."

    show killian happy with dissolve
    vl killian_vl_prefix 5.1
    k "Have you watched Hidden Village of the Iron Chambers?"
    voice sustain
    k "It's a popular anime that the general public seems to latch onto nowadays."
    "...Well, that's what I get for getting my hopes up. At least he's trying to accommodate for my sake."

    a "Can't say I have..."

    show killian neutral with dissolve
    vl killian_vl_prefix 6.2
    k "No need to worry, no need to worry. Though, I will shamelessly promote it if you're into all things action-y."
    
    show killian happy with dissolve
    vl killian_vl_prefix 7.1
    k "I've asked this hypothetical to just about everyone in here back when new manga chapters were still coming out:"
    vl killian_vl_prefix 8.1
    k "The story centers around this guy, Larips Alstrom, and he was abandoned by the whole town just because he was supposedly cursed by his ancestors."
    vl killian_vl_prefix 9.1
    k "BUT once he's older and learned how to fend for himself, despite everyone shunning him for something he can't control..."
    voice sustain
    k "...he ends up saving them from destruction and protecting them from a world war."
    
    show killian neutral with dissolve
    vl killian_vl_prefix 10.1
    k "So, with all of that known, I ended up asking if that was a realistic premise for an action series."
    voice sustain
    k "Is a child abandoned by their village able to overcome that neglect or is that unrealistic?"

    a "Damn, a whole village?"
    #"[Beat.]"
    a "I'm sorry."
    a "Um... Yes. I wouldn't rule it out completely."

    show killian angry with dissolve
    vl killian_vl_prefix 11.1
    k "That includes their family, friends, and strangers hating you, thinking you're some supernatural freak, and that's all you've grown up knowing."

    a "It might be hard but everyone's able to come out of hardship."
    a "That Larips guy probably knew that those labels the village gave him from day one weren't what defined him at the end of the day."
    a "He understood that he could be anything and that he was his own person."

    show killian happy with hpunch
    "Killian suddenly jumps up excitedly and speaks emphatically with their hands."
    stop music fadeout 1.0

    vl killian_vl_prefix 12.1
    k "ACTUAL OPINIONS. REAL DISCUSSION. THANK YOU."
    play music hatchling22 fadein 1.0
    vl killian_vl_prefix 13.1
    k "I have been telling these drones to not be afraid of what other people think and speak their minds for years!"
    voice sustain
    k "But noooooo, it's nothing but regurgitated safe statements everyone sees online!"

    vl clubregular1_vl_prefix 1
    anek "Brother, we can still fucking hear you on the other side of the room."

    show killian happy with dissolve
    vl killian_vl_prefix 14.1
    k "On a more serious note: you really must see the show."
    
    show killian surprised with dissolve
    voice sustain
    k "OH! Better yet, better yet... We should watch 'In His Heaven' sometime."
    voice sustain
    k "It's a bit old but a pivotal show in the mecha genre canon."

    vl clubregular2_vl_prefix 1
    anek2 "The last two episodes are a mindfuck!"

    show killian happy with dissolve
    vl killian_vl_prefix 15.1
    k "When are you free, Mx. Blakesley? I will make time for you."
    voice sustain
    k "I've been starved of quality conversation for so long."
    "The guy's almost puppy-eyed, I swear."

    a "Tell me where I can watch it. We can circle back here once I'm done bingeing it."

    show killian happy with dissolve
    vl killian_vl_prefix 16.1
    k "Of course! Just let me check where it's available..."
    
    show killian neutral with dissolve
    "As he pulls up his phone, I realize in that moment that I've finally got the answer to my question asking if Killian's a complete loon."

    "Awkward? Definitely. Lonely? More than likely. But crazy? He might be a bit borderline—but I think I'm okay with that."
    "At least this dork bathes regularly and knows how to put a decent fit together."

    show killian happy with dissolve
    "Maybe the normie in me can get this shut-in to touch grass in due time?"
    stop music fadeout 1.0

    scene black with fade
    call student_council_dallinus("Dallinus", 19) from _call_student_council_dallinus_1

label anime_route_vanus(month, date):
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Killan_Own_Month3_"
    
    call screen calendar(month, date, "Vanus", 15)
    scene bg classroom_anime_afternoon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Killian - Down With the Sickness\nNyday, Vanus 15th, 1027 RD")

    "Ever since wandering into 3-3, it's been a time getting familiar with the AMA even if there isn't much to do."
    "It's an odd club for sure but odd doesn't necessarily mean bad in my book. Honestly, I think I have to thank the club's president for that."
    "Sure, he's a bit over the top and he has his hot takes but it isn't like he's hurting anyone."
    "He's a bit cringe at times but such is life. He lives life unafraid which is more than what most people can say about themselves."

    show killian neutral at center with dissolve
    "Things have gotten to the point now that we both feel comfortable having lunch together (even though he doesn't seem to eat much aside from milk and some forms of noodles)."
    "I eventually found out that we share a class together somehow... Calculus, I believe."
    "Once we both found that out, he keeps mentioning about an upcoming test we have that he's absolutely scared shitless about."
    stop music fadeout 2.0
    "Poor guy looks like he's been living at the library for the past few days I've seen him..."
    play music hatchling22 fadein 1.0
    "But, ever the stalwart leader he believes himself to be, he still makes time to hold weekly meetings in 3-3."

    show killian happy at center
    "This week, everyone's crunching to get caught up with watching Blue Meridian."
    "Apparently it's been on air for close to 30 years and counting!"
    "It kinda makes you wonder if there's really any treasure at The One Peak if they've been searching for the place that long..."

    show killian neutral
    "As I'm contemplating all of this, I hear Killian coughing in the back of the room, trying to stifle the noise."

    a "Everything alright back here?"

    show killian neutral
    vl killian_vl_prefix 1
    k "Everything's quite alright, Mx. Blakesley. Just a little tickle in the throat."

    show killian sick
    "As I get a better look at him, he looks clammy and his breathing is off."
    "I go and pad his forehead with the back of my hand just to verify what I'm seeing."

    a "Your temperature says otherwise..."

    show killian sick
    vl killian_vl_prefix 2
    k "Please... A little bit of fatigue isn't going to stop me from doing my due diligence."

    a "That's noble and all but... What about retreating and living to fight another day?"

    # TODO: Add Killian sneeze effect
    show killian sick
    vl killian_vl_prefix 3
    k "I'd rather {w=0.9}di- {w=0.9}di- {w=0.7}d-– {w=0.3}ACHOO!{w=0.3}– !!!"
    stop music fadeout 1.0

    hide killian sick with fade
    "Right in my face. Gross."
    "In war, even metaphorical ones, there are always casualties and, today, I am one of them."

    a "Gross... Can somebody get me a tissue ple- BY THE GODS."
    play music hatchling21 fadein 1.0

    show killian sick at center with vpunch
    vl killian_vl_prefix 4.2
    "Suddenly, Killian's on the floor, groaning."
    voice sustain
    "The regulars quickly notice, quickly close up shop, and get him to the infirmary."

    "According to some of them, he always had a tendency to overwork himself."
    "They tell me he's got the attitude of an Estarese salaryman willing to live at the office if you give him the chance."

    scene bg dorm_common_noon with fade
    "As for me, after that unfortunate incident, I had to take a few days off and play catch-up after Killian's germs got to me."
    "Once I got better though, I wanted to check up on Killian in the infirmary but that was against MIA policy for some reason."
    "One of the downsides to having a house system, I guess."

    scene black with fade
    "Gods, I hope the geek's alright."
    stop music fadeout 1.0

    # jump to second club route dyalt
    $ renpy.call(chosen_club2 + "_route_dyalt", "Vanus", 15)
    #jump anime_route_dyalt

label anime_route_dyalt(month, date):
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Killan_Own_Month4_"
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Killians Route/Month 4/Naomi_Killian_Month4_"

    call screen calendar(month, date, "Dyalt", 26)
    scene bg maincastle with fade
    play music hatchling4 fadein 1.0

    $ renpy.notify("Killian - Out of Contrology\nNyday, Dyalt 26th, 1027 RD")
    
    "Gods bless the MIA kitchen staff! At least I know we're all getting our money's worth."
    "Still, I noticed that Killian hasn't been in the dining hall ever since checking out of the infirmary. Word around campus is that he sustained a head injury when he had that pratfall after succumbing to his flu and fatigue."
    "It would've been nice to check up on how he's holding up in House Crowlin but sadly that's against academy rules."
    
    pause 1.0
    
    "Maybe I should get some fresh air, there's no use in worrying over that dork this bad. Besides, it's so crowded inside. Most of the people here are good company as far as I know but sometimes just being where everyone is can sap the spirit, y'know?"
    stop music fadeout 1.0
    
    scene bg wright_field_afternoon with fade
    
    vl killian_vl_prefix 1
    unknown "Unf... Unf... Unf...!"
    voice sustain
    "...What the..."
    voice sustain
    unknown "Unf... Unf...!"
    voice sustain
    play audio "audio/voices/Love Interests/Naomi/Killians Route/Month 4/Naomi_Killian_Month4_1.ogg"
    unknown "Don't stop! Keep going!"
    voice sustain
    unknown "Unf... UGH!"
    voice sustain
    "Damn. I'm not one to stick my nose into other people's business—wait, I meant to say that I'm not the nosy type. Who in this academy is doing... Whatever—on school grounds out in the open? And in the middle of winter?!"
    voice sustain
    "I follow the grunting and other sounds before turning a corner into a secluded part of the field, finding the source of the noise."
    voice sustain
    show killian sad at character_pos2 with moveinright
    show naomi embarrassed at character_pos6 with moveinright
    vl killian_vl_prefix 2
    k "UGH! No more! I can't keep up!"
    
    vl naomi_vl_prefix 2
    n "You're doing fine. Here, have some of my meat."
    
    "...Ahem."

    with hpunch
    show killian neutral
    show naomi embarrassed
    
    "The two class presidents turn around. And while ego's nowhere present, something else died in that terribly heavy moment of silence."
    
    # TODO: Add textbox for multiple characters talking at teh same time
    # TODO: Add voice channel for saying different voice lines at the same time
    vl killian_vl_prefix 3
    play sound ["<silence .5>", "audio/voices/Love Interests/Naomi/Killians Route/Month 4/Naomi_Killian_Month4_3.ogg"]
    call screen multiple_say(k, "We can explain.", n, "We can explain.")
    
    
    
    stop music fadeout 1.0
    a "Please do."
    play music hatchling22 fadein 1.0
    
    "Naomi whips out a comically large cured sausage from out of nowhere and holds it out in front of me. The damn thing could easily be a murder weapon if you swung it at someone's head hard enough."
    
    a "...What is that?"

    show killian sad:
        xpos 0.2
        yalign 1.0
    show naomi neutral:
        xpos 0.8
        yalign 1.0
    with dissolve
    
    vl naomi_vl_prefix 4
    n "...My meat. Mateba sausage, Estarese style. It took me a week to dry it properly..."
    
    "Killian gets to his feet, chest bare, uniform top and blazer hanging on a nearby tree branch (for reasons I can't explain—medical professionals would probably refer to this phenomenon as 'shock'—I can only picture him with all of it on)."
    
    a "So I take it you're all better then? After those long nights alone in the infirmary? Finally getting enough sleep between study sessions?"
    
    show killian fear
    vl killian_vl_prefix 4
    k "Mx. Blakesley, I swear that this isn't what it looks like!"
    
    a "Oh, really? Out with it then. I'd love to see where this soap opera goes."
    
    pause 1.0
    
    show killian neutral
    show naomi neutral
    vl killian_vl_prefix 5
    k "Well... I've been working out to get stronger."
    
    show naomi happy
    vl naomi_vl_prefix 5
    n "It's true! I've been watching him outside of the Home Ec room's window! He's been at it for a while now, you'd think he'd get better after some time!"
    
    vl killian_vl_prefix 6
    k "Naomi's been acting as my nutritionist ever since I started."
    
    show killian neutral:
        linear .25 alpha 0.75
    show naomi neutral
    vl naomi_vl_prefix 6
    n "Don't tell him but I just needed to empty out the back of the freezer before the end of the month."
    
    show killian neutral :
        linear .25 alpha 1.0
    vl killian_vl_prefix 7
    k "After overworking myself and getting you sick, I wanted to invest some time in tending to my physical health."
    
    pause 1.0
    
    vl killian_vl_prefix 8
    k "I read online that contrology was a good way to improve oneself without any heavy lifting equipment... So I started doing that..."
    stop music fadeout 1.0
    
    pause 1.0
    
    show killian fear
    vl killian_vl_prefix 9
    k "Why aren't you saying anything?"
    
    a "You do realize that I haven't seen you in several weeks, right?"
    
    show killian sad
    "The dork looks down, shoegazing."
    
    show killian neutral
    vl killian_vl_prefix 10
    k "...I figured nobody would notice, if I'm being quite honest. Really, I didn't mean anything by it."
    
    pause 1.0
    
    vl killian_vl_prefix 11
    k "You noticed?"
    
    a "Why wouldn't I?"
    
    "This whole time I thought we were... He's just being dense now, right?"
    
    a "Naomi."
    
    show naomi surprised
    vl naomi_vl_prefix 7
    n "Eep!"
    
    a "Did you know that Killian was in the infirmary a while ago?"
    
    vl naomi_vl_prefix 8
    n "N-no... Is that true, Killian?"
    
    show killian neutral
    vl killian_vl_prefix 12.1
    k "It is, Ms. Kuzuma."
    vl killian_vl_prefix 13
    k "I-... I really should've said something. I know that now, Mx. Blakesley."
    
    show killian sad
    "Killian looks back down again, getting dressed. I suppose he had a reason to assume the worst based on his own personal history even after we've gotten to know each other for a while now."
    "Not a long time, but a long enough time to chat regularly with someone—we weren't acquaintances to each other is what I'm trying to say here."
    "Now, I only hope he knows that I had my own reasons to reciprocate given the... Really fucking odd circumstances, I'm not even gonna lie. But despite all of that, I feel some sort of relief."
    "Though, there's now a new concern I have with Naomi giving almost out-of-date food like that but, then again, it could've been way worse."
    "Maybe I should've just stayed inside and finished my lunch today..."

    call student_council_dyalt("Dyalt", 26) from _call_student_council_dyalt_1

label anime_route_neralt(month, date):
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Killan_Own_Month5_"

    call screen calendar(month, date, "Neralt", 16)
    scene bg classroom_anime_afternoon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Killian - Arcade Parts\nNyday, Neralt 16th, 1027 RD")

    "We haven’t spoken to each other since the weird contrology-sausage incident."
    "I see him occasionally during passing time and sometimes our eyes lock but never any words or any attempt to approach."

    "At least it looks like the workouts are paying off for him."

    "Despite the awkward tension, I still find myself in his club even if I still haven’t found the nerve to say something."
    "At least to tell him that I wasn’t mad when he and Naomi told me what was really going on."

    show killian neutral at center with dissolve
    vl killian_vl_prefix 1
    k "Okay… In the coming weeks, we’ll have an online poll thrown up in the AMA server to vote for the next Watch-a-thon…"
    voice sustain
    k "I believe it’s a toss up between \"Shouryū Walkers\" and \"Present Day//Time\"."

    show killian disgust
    vl killian_vl_prefix 2
    k "I’d also like to remind everyone, for future reference, that we still cannot stream anime such as \"AfterSchool Special X\" on academy grounds without breaking several rules."
    voice sustain
    k "With all that said, please vote before the Involvement Fest."

    show killian neutral
    vl killian_vl_prefix 3
    k "Speaking of which… Involvement Fest! The Anime and Manga Association will be setting up a booth next weekend in order to help raise funds and raise awareness of our existence on school grounds."
    vl killian_vl_prefix 4
    k "If you all enjoy coming here and want to show your support, please let me know as soon as possible and we can work something out."
    vl killian_vl_prefix 5
    k "Does anyone have questions before I adjourn this meeting? Speak now or forever hold your peace?"

    "Nope. May peace be forever held with this Blakesley."

    vl killian_vl_prefix 6
    k "Alright. Consider this meeting adjourned. Thanks for coming and see you all next week."

    "Once the regulars leave, much to my surprise, Killian pulls me over to the side."
    stop music fadeout 1.0

    vl killian_vl_prefix 7
    k "Mx. Blakesley, do you mind if I have a moment with you?"

    a "Um… Sure. What’s up?"

    vl killian_vl_prefix 8.2
    k "We both know \"what’s up.\" I’ve assumed that you, much like myself and Ms. Kuzuma, weren’t feeling like our miscommunication situation near the gymnasium field found proper closure."
    vl killian_vl_prefix 9
    k "And so, because I’ve yet to find such a thing, I’ve come bearing an alternative to you: I want to formally apologize."

    a "Thanks for the formality… But I’m not sure there’s a need to do that… It should be me apologizing but I’ve been… squirrely after the last time we spoke with each other."

    a "I wonder if this school has a counselor on-site…"

    vl killian_vl_prefix 10
    k "Come again?"

    a "Nothing! You were saying?"

    vl killian_vl_prefix 11
    k "Ah, yes. I guess that makes us both fools and cowards for different reasons. But that also makes us even in my book."

    a "I’m glad. A balanced book sounds good to me."

    "It seems that we’ve both overcome this hurdle through the power of mature conversation."
    "But, as I turn to head out of 3-3, Killian has a strange look on his face—the one a kid might have while struggling to hold their piss in."
    play music hatchling22 fadein 1.0

    a "Is there something wrong?"

    show killian angry
    vl killian_vl_prefix 12
    k "Yes! I mean, no! Argh, well… I don’t know!"

    show killian neutral
    vl killian_vl_prefix 13
    k "I had this whole thing prepared. I was gonna… Take you out somewhere."

    show killian surprised
    vl killian_vl_prefix 14
    k "TO STRICTLY MAKE THINGS UP TO YOU!"

    a "You were gonna take me out somewhere?"

    vl killian_vl_prefix 15
    k "Y-yeah! Wanna walk with me and see where?"

    #FADE TO:
    scene bg mainstreet_afternoon with fade

    "Before I know it, we’re both standing in front of an arcade but closed off to the public for renovations."

    show killian angry
    vl killian_vl_prefix 16
    k "Oh, what the fuck?! The afternoon’s ruined!"

    a "There’s no need to get too worked up. They’re probably just repainting the place."

    show killian sad
    vl killian_vl_prefix 17
    k "But it would’ve been so cool!"
    voice sustain
    k "We would’ve had fun and laughed and we’d remember this afternoon at this place I’ve known since I was a kid and it would’ve been a grand old time… "
    vl killian_vl_prefix 18
    k "The gods are cruel and crave misery from me, I suppose."

    a "Why don’t we just head back and watch some anime instead? Maybe the next time we swing by here, they’ll be back up with a whole new look!"

    vl killian_vl_prefix 19
    k "…I’m sorry."

    a "Seriously, there’s nothing to be sorry about. I can handle a bumpy road but not an empty car so let’s get going."

    "Kindness for kindness’ sake has always felt good to me—but seeing it bring calm to another feels even better."
    "And for some reason, with Killian, that feeling seems to grow warmer and warmer when he comes around to living life for himself…"

    scene black with fade
    "…Or maybe those last two episodes of \"In His Heaven\" just really left an impression on me."
    stop music fadeout 1.0
    
    # jump to second club route neralt
    $ renpy.call(chosen_club2 + "_route_neralt", "Neralt", 16)
    #jump student_council_exalt

label anime_route_exalt(month, date):
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Killan_Own_Month6_"
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Killian/Month6/Reina_Killian_Month6_"
    $ sue_vl_prefix = "audio/voices/Love Interests/Sue/Killian/SueDaengQan_Killian/SueDaengQan_Killian_"
    $ phillip_vl_prefix = "audio/voices/Supporting-Extra/Phillip/Killian/Phillip_Killian_Month6_"

    call screen calendar(month, date, "Exalt", 22)
    scene bg maincastle with fade
    play music hatchling12 fadein 1.0

    $ renpy.notify("Killian - Club is War (Or the Involvement Festival Incident)\nZaeday, Exalt 22nd, 1027 RD")

    "It feels strange to see all of MIA out and about during the weekend."
    "Maybe it's because of all the crowding or maybe the snow but everything here seems oddly competitive with everyone's booths outside of Magis Hall."
    "I can smell whatever Naomi's cooking during her demonstration and the smoke coming off the grill can't help but make everything feel like a summer day's sunset."
    "Lucas has got a freestyle poetry thing going on, inviting people to throw topics at him and he'll bang something out on his ancient typewriter for people to take home."
    "Regardless of whether the writing's good or not, folks seem entertained."
    "Sue, Reina, and the Prince himself have taken a more straightforward approach with the formal handshakes, pamphlets, and buttons."
    "I think Reina threw in a pull-up bar for the less policy-savvy individuals to play around with."
    "And it looks like someone from the Archery Club managed to convince Elio to organize something for Involvement Fest, just a little carnival-style shooting range with toy bows and suction cup arrows."
    "As for the Anime & Manga Association… Killian's moving stereo speakers next to the selected manga volumes and steelbooks of anime."

    show killian neutral at center with dissolve

    a "Sooo… What are we doing here exactly?"

    vl killian_vl_prefix 1
    k "We… Are going… To meet… Our quota."

    a "And what is the \"quota\" exactly?"

    vl killian_vl_prefix 2
    k "Ever since I became the AMA's president in my second year, it came with a myriad of responsibilities, of which includes the matters of upkeep and expansion."

    "Now he tells me…"

    vl killian_vl_prefix 3
    k "I'm aware that the club hasn't exactly been the \"fan favorite\" org that students have been clamoring for but I haven't given up yet."
    stop music fadeout 2.0
    vl killian_vl_prefix 4
    k "In short: I've devised a surefire way to attract the required amount of members and the funds for annual dues."
    play music hatchling22 fadein 1.0

    show killian happy
    vl killian_vl_prefix 5
    k "I'm going to sing a song to attract the masses!"

    a "Since when do you know how to sing?"

    vl killian_vl_prefix 6
    k "That's the funny thing! I don't!"
    vl killian_vl_prefix 7
    k "While I do have some musical ability, I've never tested my vocal cords like that."

    "That sounds like such a bad idea."

    a "This sounds like such a bad idea."

    show killian neutral
    vl killian_vl_prefix 8
    k "Desperate times call for wild swings. Keep faith in me though, Mx. Blakesley."
    voice sustain
    k "We can celebrate with a night out into town after we've won this war of attrition and annual fees!"

    "It doesn't take long for everyone to notice the speakers once they're plugged in and screech feedback until we readjust them."
    "One of the regulars helping us quickly hands Killian a microphone."

    show killian fear
    "I turn to find Killian white-knuckling the microphone in their hand, staring off into the sea of people who are waiting for something to happen."

    hide killian fear with fade
    "And just like that, when his club needs him the most, Killian… Vanishes?"
    stop music fadeout 1.0
    "The next time I turn to find the AMA president, he's disappeared and the live mic rests on the grass."
    "Damn it all…"
    "I reluctantly pick up the mic and let the metaphorical spirit of altruism and true friendship take the wheel."

    a "The, Uh, welcome everyone… To MIA's…"

    "Killian, what the fuck?"

    "I try to think of something on the fly and come to a viable emergency option."
    "I hope he'll forgive me for what I'm about to say…"
    play music hatchling22 fadein 1.0

    #[Beat.]

    "(Nah, but seriously, what the fuck, Killian; why have you run off like a cannon's aiming for you?)"

    a "To MIA's Open Library Auction… Brought to you by the Anime and Manga Association! Come spend some cash and sign up to learn more about the club!"

    "The next hour or so become a blur to me. I do my best bid caller impression, yapping away at a mile a minute, successfully encouraging bidding wars for weeb shit."
    "Thankfully for us, a few folks actually do!"
    "By the time I stopped and let my voice rest, almost all of our impromptu wares were with new owners."
    "I then find the nearest chair and claim my well-earned sit like the hero I know I am."
    "I take the liberty of counting and sending everything up to on-site IAH officials, earnings and sign-ups, once I replenish some energy and watch as all the clubs pack up and bring down their stands."
    stop music fadeout 1.0

    show killian surprised at center with dissolve
    vl killian_vl_prefix 9
    k "…Have they all left?"

    a "Mr. President, what the fuck?! Where have you been?"

    "Almost immediately, Killian sighs, looking defeated, before bawling."
    play music hatchling21 fadein 1.0

    show killian sad
    vl killian_vl_prefix 10
    k "Thank you so much, Mx. Blakesley… I tried so hard, I really did but I couldn't, I really couldn't… My voice wouldn't-"

    a "Look, it's alright, we can talk about this later if you want. Just calm down and catch your breath."

    "Killian takes a moment to recollect himself."

    vl killian_vl_prefix 11
    k "Mx. Blakesley, may I hug you? And maybe buy you dinner tonight? It's the least I can do to thank you really."

    a "Oh, well, sure. It's-"

    stop music fadeout 2.0
    "As Killian awkwardly embraces me, off in the distance, I can see the big three approaching our booth for some reason."
    play music hatchling3 fadein 1.0

    show killian surprised at left_pos
    show sue neutral at center_pos
    show phillip neutral at right_pos
    with dissolve
    
    vl sue_vl_prefix 1.2
    s "I do apologize. Am I interrupting?"

    a "Huh? No, no, we're just… Wait, why are you here?"

    vl sue_vl_prefix 2.2
    s "There's no need to worry. We come bearing good news."

    vl killian_vl_prefix 12
    k "Really?"

    hide sue
    show reina neutral at center_pos
    with dissolve
    vl reina_vl_prefix 1
    r "Really. Following Blakesley's most recent deposit and submission, it looks like the Anime club lives to see another year."

    vl killian_vl_prefix 13
    k "Oh my… That was so quick."

    a "It helps when the student council's accounts manager doing your totals hates to procrastinate."

    show reina happy
    vl reina_vl_prefix 2
    r "You should be glad. Your friend over here is the only reason why your organization will remain when you're gone from this place."

    hide reina
    show phillip neutral at center_pos with dissolve
    vl phillip_vl_prefix 1
    p "Now, there's no need for that. We should be glad! The school's going to reap the rewards at the end of the day anyway, right?"

    hide phillip
    show reina neutral at center_pos with dissolve
    vl reina_vl_prefix 3
    r "Be that as it may, it doesn't change the fact that Mr. Moto's found a way to avoid death yet again."

    show killian disgust at left_pos
    vl killian_vl_prefix 14
    k "That's the goal. Every time."

    hide reina
    show phillip tired at center_pos with dissolve
    vl phillip_vl_prefix 2
    p "Alright, alright, we're all probably a bit tired. It's late and we just figured everyone here wanted to hear the good news."

    "The prince reaches out to shake Killian's hand like a mayor running for office would."

    show phillip neutral
    show killian surprised at left_pos
    vl phillip_vl_prefix 3
    p "Congratulations, Dylan. I'm happy for you. Truly."

    vl killian_vl_prefix 15
    k "Um, actually, it's-"

    show phillip excited
    vl phillip_vl_prefix 4
    p "Who's hungry?!"

    "As the student council heads departed, Killian and I couldn't help but be a little happier about ourselves."
    "The AMA had a much needed win for the future which is quite alright in my book."
    stop music fadeout 1.0

    if chosen_club2 == "enseki":
        call enseki_route_exalt2("Exalt", 22) from _call_enseki_route_exalt2_1
    else:
        call phillip_elvera("Exalt", 22) from _call_phillip_elvera_1

label anime_route_elvera(month, date):
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Killan_Own_Month7_"
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Killians Route/Killian/Elio_Killian_EoE_"
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Killian/Month 7/Reina_Killian_Month7_"
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Killians Route/Month 7/Naomi_Killian_Month7_"

    call screen calendar(month, date, "Elvera", 18)
    scene bg maincastle with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Killian - End of Everything\nNyday, Elvera 18th, 1028 RD")

    "It’s occurred to me that, after the Involvement Festival, that means that I’m more than halfway through the year here at MIA."
    "With grades passing, friends being made, and being the hero of someone else’s story, I’d say that I’m having a grand time so far."
    "Not unlike Killian who, during lunch, hasn’t been so inconspicuous about something by the way he’s been muttering to himself like a madman."

    show killian angry with dissolve 
    a "Are you alright?"

    vl killian_vl_prefix 1
    k "Huh? What? Of course I’m alright. I’m all left, all up, and all down too."

    a "Okay… Just checking to make sure…"

    vl killian_vl_prefix 2
    k "How can she be so cruel with the way she speaks? Just because you’re the disciplinary head doesn’t mean you have to wave the title in peoples’ faces like a hammer!"

    a "What are you talking about?"

    show killian disgust
    vl killian_vl_prefix 3
    k "Reina Dreyar. Let’s just say that I don’t appreciate the way that she spoke at me."

    a "Is it really worth getting this worked up about it though?"

    show killian neutral
    vl killian_vl_prefix 4
    k "I understand that the AMA has had its ups and downs behind closed doors but… Sometimes it takes a while for the underdog to find their bearings, right?"

    #[Beat.]
    vl killian_vl_prefix 5
    k "Why can’t she respect every representative of the Student Council? I’m there for a reason too!"
    voice sustain
    k "People put me in the position I am today because they saw something in me when I couldn’t."

    a "So, I won’t deny any of that. But, from what I know about the club’s financial history…"
    a "She’s got good reason to be a bit testy with you when it comes to this sort of thing."

    vl killian_vl_prefix 6
    k "Well, I-"
    #voice sustain
    stop music fadeout 1.0
    #show killian fear with hpunch
    with hpunch
    "Killian’s phone pings and he chokes on the carton of milk he’s been sipping."

    a "Okay, what was that? What happened?"

    show killian surprised
    vl killian_vl_prefix 7
    k "Nothing… Milk went down funny…"

    "Thankfully, him nearly choking on dairy manages to knock him out of his heated ramble. I don’t really pay too much mind. A good vent ought to do him some good."
    "But then I couldn't help but notice as we leave the cafeteria that something in his eyes faltered…"

    hide killian surprised
    #FADE TO:

    scene bg classroom_anime_afternoon with fade

    "It’s like the abyss itself has done everything in its power to try and rain everything out. Thank the Gods it’s warm in the Anime Club room."

    "We’ve reached the holiday-themed anime episode for whatever series is playing on the projector."
    "I look around and everyone seems to be in high spirits except the club president."

    vl killian_vl_prefix 8
    "He flashes smiles and puffs light laughter but I think that… I don’t know… Killian just seems detached from it all…"

    show killian neutral with dissolve 
    a "Hey there! Is everything alright?"

    vl killian_vl_prefix 9
    k "…Hm? Oh. Yeah, everything’s alright."

    "Liar. You’d be a terrible gambler, Killian. Just tell me what’s going on."

    vl killian_vl_prefix 10
    k "Is there something wrong?"

    a "No. Well… You tell me."

    vl killian_vl_prefix 11
    k "…It’s nothing that you should worry about. Have you been outside? You look like you’ve been shivering."

    a "It’ll make you feel better if you talk it out with someone. Whatever’s bothering you, you don’t have to deal with it alone."

    vl killian_vl_prefix 12
    k "It’s official Student Council business. Even if I wanted to, I’m not permitted to disclose such details."

    a "That doesn’t make sense, I’m a council aide. Student council business is my business too."

    vl killian_vl_prefix 13
    k "Well, it’s on a need to know basis and you don’t need to know."

    a "…Killian, just tell me what’s wrong and I’ll leave you and this fucking Anime Club alone."

    show killian surprised
    vl killian_vl_prefix 14
    k "What’d you say?"

    show killian disgust
    "He immediately straightens his posture and I practically swallow my tongue at that moment."

    vl killian_vl_prefix 15
    k "What do you want me to say? You wanna feel sorry for me? You wanna give a little sympathy to the crazy little shut-in dork with the hobby nobody gives two shits about?"
    voice sustain
    k "It’ll make you feel good, right?"

    "I stand speechless, regretting I ever asked anything. Needless to say, there’s definitely something wrong and it’s taking a massive toll on his head and heart."

    show killian angry
    vl killian_vl_prefix 16
    k "Right?!"

    "I look around the classroom and everyone’s looking at the two of us. It doesn’t take long until everyone slowly starts streaming out of the classroom."
    "This is a first for me, seeing Killian like this—and I think that he realizes this too. Quickly, his frustration subsides."
    "He palms his face and takes his glasses off before looking down, disgusted by his own actions."

    show killian fear
    vl killian_vl_prefix 17
    k "…I’m truly sorry for… Raising my voice…"

    a "I really shouldn’t have word- I mean, I didn’t mean to-"

    vl killian_vl_prefix 18
    k "It’s fine. I know you didn’t mean it. Besides, I’ve heard worse."

    "The silence between us is harsher than the wind blowing outside."

    show killian disgust
    vl killian_vl_prefix 19
    k "Please leave."

    "I comply with his request with an awful feeling in my stomach. I pressed too hard. And then we ended up scaring the newbies (and the regulars)."
    "I guess giving space is the best option for the time being."
    "But there’s that part in me that won’t let this go. I’m worried for him and I’ll be damned if I let him suffer alone."

    hide killian with fade
    #FADE TO:

    call screen calendar("Elvera", da18te, "Elvera", 21)
    scene bg home_ec_room_door_afternoon with fade

    $ renpy.notify("Killian - End of Everything\nZynday, Elvera 21st, 1028 RD")

    "Now, I’m no sleuth but in a situation like this it doesn’t hurt to kick some tires to get to the bottom of things (at least, I don’t think)."
    "My first person of interest in this case: Naomi Kuzuma."
    "I’m greeted with the heavenly scent of a kringle fresh out of the oven wafting through an open classroom door and the back of a home ec president carefully piping icing on top of the pastry."
    play music hatchling3 fadein 1.0

    show naomi neutral apron with dissolve
    vl naomi_vl_prefix 1
    n "Who is it?"

    a "It’s… [a]. You could tell when someone’s coming into the room like that?"

    vl naomi_vl_prefix 2
    n "It’s not like I’m psychic or anything like that. Our uniform shoes aren’t exactly the sneakiest of sneakers. Was there something you needed from me?"

    a "Yes, actually. I was wondering if you knew anything about Killian?"

    show naomi thinking apron
    vl naomi_vl_prefix 3
    n "Oh, well, I’m not one for Estarese cartoons so I can’t really offer much about that. As far as I know, Killian’s cool. A bit quiet but who am I to judge?"

    a "Oh, no, you see, he’s been a bit on edge. There was a bit of an incident at the Anime Club the other day and-"

    show naomi neutral apron
    vl naomi_vl_prefix 4
    n "Don’t worry, I heard."

    a "Wait, what? Who told you?"

    vl naomi_vl_prefix 5
    n "Nobody. I heard the echoes of some sort of squabble down the hall."

    "This isn’t getting me anywhere unfortunately. And that kringle is coming along nicely, it’s making my stomach growl."

    show naomi thinking apron
    vl naomi_vl_prefix 6
    n "Don’t give me that look. I can feel it when people are looking at me funny."

    a "Sorry, I didn’t mean to. Look, I just wanted to ask if something might’ve happened with him or the club?"
    a "Maybe something happened after the last meeting that I don’t know about?"

    show naomi neutral apron
    vl naomi_vl_prefix 7
    n "Hmm… I can’t exactly speak on what’s happening behind closed doors amongst student council presidents."
    vl naomi_vl_prefix 8
    n "But, if you’re so concerned, you might want to try asking Reina or Sue."
    voice sustain
    n "There’s no guarantee that they’ll tell you anything but it’s worth a shot to try, right?"

    a "Right. Thanks, Naomi."

    vl naomi_vl_prefix 9
    n "No worries. Oh, and just because you’re here…"

    "Naomi raises her hand to reveal a knife—which she uses to start chopping up the kringle. She hands me a fork and a plate."

    vl naomi_vl_prefix 10
    n "Care to try? At least take it with you. Or else I’m gonna end up with way too many leftovers."
    stop music fadeout 1.0
    hide naomi with fade
    #FADE TO:

    scene bg maincastle with fade 

    "As much as I’d like to take time and catch my breath, I need to hurry up and get to the bottom of this."
    "Almost everyone’s gone home and only a handful of students are walking around MIA."
    "Thankfully, I catch Reina and Elio talking to one another—or rather, I stumble on Reina lecturing Elio…"

    show reina worried at character_pos2
    show elio neutral at character_pos6
    
    vl reina_vl_prefix 1
    r "As club president, your behavior reflects back on the council."

    vl elio_vl_prefix 1
    e "Get off it, will ya? So what if I buy clothes at the soup store in my personal time? You don’t hear me barking at you when you’re all by your lonesome, eh?"

    a "Hey! Sorry, excuse me, I was wondering if I could ask the two of you a few questions real quick?"

    vl reina_vl_prefix 2
    r "I must be going. I've devoted enough time here already."

    vl elio_vl_prefix 2
    e "Whatever."

    a "Please! If you want to get technical about it, it does concern the wellbeing of a key member of the student council."

    vl elio_vl_prefix 3
    e "You’re gonna ask about Killian, right?"

    "We all stop for a moment. Reina simply scowls at Elio and me."

    vl reina_vl_prefix 3
    r "We did all we could. He should be thankful knowing that he’s still going to be there at the end of it all."
    hide reina worried with dissolve

    "After that, Reina storms off."

    a "What’s she talking about?"

    show elio confused
    vl elio_vl_prefix 4
    e "You really don’t know, huh?"

    "Elio takes his phone out, pulls up a message, and begins to read."
    play music hatchling15 fadein 1.0

    show elio neutral
    vl elio_vl_prefix 5
    e "\"This update is to inform all student organization leaders of a recent change in the coming year by IAH’s school board.\""
    vl elio_vl_prefix 6
    e "\"While the main goal of IAH's Involvement Fest has been to attract freshmen students to get involved in extracurricular activity,"
    voice sustain
    e "it has also been a flagship event for club fundraising with school board approval and regular financial upkeep.\""
    vl elio_vl_prefix 7
    e "\"One club in particular that goes by the Anime and Manga Association has been deemed a liability by the school board.\""
    vl elio_vl_prefix 8
    e "\"With that said, despite their best efforts and their recent success at attracting the necessary funds and sign-ups at Involvement Fest, the organization is marked for upcoming termination.\""

    pause 1.0
    stop music fadeout 1.0

    vl elio_vl_prefix 9
    e "Kinda makes you wonder if Killian’s upset or not, doesn’t it?"
    hide elio neutral with dissolve
    pause 1.0

    call screen calendar("Elvera", 21, "Elvera", 22)
    scene bg classroom_anime_afternoon with fade
    play music hatchling10 fadein 1.0

    $ renpy.notify("Killian - End of Everything\nUctday, Elvera 22nd, 1028 RD")

    "I try to meet with Killian the day after Elio told me what was happening with the AMA."
    "I keep an eye out for him that whole day but it looks like he’s taken a day for himself."
    "Even 3-3 is barren—I guess I don’t have to imagine what this place will look like in the future. I pull up a seat for myself and just sit in silence for a moment."
    "I guess it’s kind of like paying my respects to the place. Or asking it for forgiveness."
    "But not long after that, my nose catches the smell of something warm and homey. Naomi must be baking her ass off for an upcoming afterschool sale."
    "It’s a pleasant surprise to the senses but then I notice the scent getting stronger and stronger."
    "Out of general curiosity, I step outside of 3-3 and bump into Naomi carrying a decorated woven basket like one you’d hear about in a fairy tale."

    show naomi neutral with dissolve
    vl naomi_vl_prefix 11
    n "Oh! Funny seeing you here again. Were you able to find anything with your investigation?"

    a "I did actually and it’s kind of depressing if I’m being honest."

    pause 1.0

    a "Say, how come you didn’t tell me anything about the school board?"

    show naomi worried
    vl naomi_vl_prefix 12
    n "I didn’t mean anything by it, truly. I’ve been busy with doing my share of work readying elections for Home Ec, studying for finals coming up, and organizing stuff with my family for graduation."

    show naomi embarrassed
    vl naomi_vl_prefix 13
    n "I hadn’t checked my messages until last evening. So, I do apologize for not knowing as soon as the others caught wind."
    voice sustain
    n "But I mean, I have my own life to live and it doesn’t exclusively revolve around the club as much as I fight for it."

    "By the look of the basket, at least she isn’t half-assing anything."

    a "Special delivery, I take it?"

    show naomi neutral
    vl naomi_vl_prefix 14
    n "It is, actually. I’m taking this to the chapel just past Main Street."

    a "I didn’t exactly strike you as religious."

    show naomi thinking
    vl naomi_vl_prefix 15
    n "I wouldn’t say that… I treat it like salt. Not too much but a little bit can go a long way."

    show naomi happy
    vl naomi_vl_prefix 16
    n "Actually, do you mind keeping me company? Maybe a walk into town can help ease yourself."

    "I take one last look back at 3-3 before closing the door behind me."

    a "Sure. Why not?"

    stop music fadeout 1.0
    hide naomi happy with dissolve
    scene bg chapel_day with fade

    "The rain’s always so harsh this time of year, I can only take it in small portions."
    "Naomi and I eventually find ourselves in front of a plain but visibly aged chapel."
    "I hold open the door and we both quickly head in for a brief respite from the springtime showers."
    "As I turn from the door, I’m met with stillness in the room. Similar to what the silence in 3-3 brought except I can’t help but feel like I’m being watched."
    "I guess with places like these, that’s the whole point so I try to shake off the feeling as best as I can."

    show naomi neutral with dissolve
    vl naomi_vl_prefix 17
    n "I’ll just be a moment now."

    "Naomi scurries off down the middle aisle past the plain wooden benches, each step echoing throughout the entire building, before turning back around halfway once she notices a lone figure sitting alone along the outer end of one of the front pews."
    "She quickly motions me to hurry over, I roll my eyes, and walk on over. Turns out it was for a good reason. I immediately recognize the charms hanging off of the person’s uniform lapels."

    vl naomi_vl_prefix 18
    n "…I’m gonna drop these off and let the two of you work things out."

    "Naomi exits and I carefully slide down the pew where Killian is sitting."
    
    hide naomi neutral with fade
    play music hatchling21 fadein 1.0
    pause 1.0
    show killian neutral with dissolve 
    vl killian_vl_prefix 20
    k "…How’d you find me?"

    a "Naomi. Reina and Elio told me about the school board. Mostly Elio."

    #[Beat.]
    vl killian_vl_prefix 21
    k "They sent out the message a few days ago. Everything still feels fresh."

    a "I’m sorry that everything turned out like this."

    vl killian_vl_prefix 22
    k "After all our efforts. After all the work I put into, after being a good soldier, I have nothing."

    a "…Well, think about it like this: we’re still going to graduate and we’ll still have fond memories with th-"

    show killian disgust
    vl killian_vl_prefix 23
    k "You know… That's the thing that I loathe about everyone in this school."
    vl killian_vl_prefix 24
    k "\"oH, wHy dO yOu cArE? yOu'Ll bE gRaDuAtiNg SoO-\" That's not the point!"

    show killian angry
    vl killian_vl_prefix 25
    k "People were depending on me to care!"
    vl killian_vl_prefix 26
    k "Sure, it may not be a full house but the people in it were at home. People like…"
    voice sustain
    "Killian sighs."

    show killian neutral
    vl killian_vl_prefix 27
    k "Those people became my responsibility when I became the AMA’s president. I took that oath with the best of intentions and I failed in the end."
    vl killian_vl_prefix 28
    k "Now look at me. A nobody in a burning house waiting for the roof to fall. I’m nothing."

    pause 1.0 

    a "Nobody’s nothing, you know."

    a "Take a man. He can be many things. A warrior. A poet. A husband. A father. He can live as plainly as possible but he’ll never be a nobody."

    vl killian_vl_prefix 29
    k "Those are all titles given to them by other people throughout their life. Without them, they’re nothing."

    a "They simply know the man as they know them. They’re just reflections, and everything reflects who we are at the end of the day."

    vl killian_vl_prefix 30
    k "Everything has dictated what I supposedly am since as far as I can remember."

    show killian disgust
    vl killian_vl_prefix 31
    k "Exes. Enemies. Bullies. Family. Society."
    vl killian_vl_prefix 32
    k "I know it. Whether I wanted it or not, people simply knew me the way I am now. It was predestined."

    a "So the Anime Club… You weren’t always a leader were you?"

    vl killian_vl_prefix 33
    k "No. But I wanted to be. So what does that tell you?"
    vl killian_vl_prefix 34
    k "Whatever mirror I wanted to look at in front of me—what I wanted to see there—is gone."
    stop music fadeout 1.0

    pause 1.0

    show killian angry with dissolve
    vl killian_vl_prefix 35
    k "[a], I don’t want to go back to being that hermit with no direction that people use as a warning."

    a "You know it doesn’t have to be that way, right?"

    vl killian_vl_prefix 36
    k "I guess but… I don’t even know what to do now."

    show killian sad with dissolve
    vl killian_vl_prefix 37
    k "I don’t know who I am! "
    vl killian_vl_prefix 38
    k "If fate isn’t going to let me look up to a better self and I don’t want to revert to my past self, then what am I now?!"
    vl killian_vl_prefix 39
    k "What do I do now?!"

    pause 1.0

    a "You do what everyone else does every day. You do the best you can."

    "Killian breaks down and huddles close to me for comfort. I embrace him and the two of us don’t say anything further."
    "Just two people looking back at each other’s reflections, trying to understand ourselves and what the future might bear."
    hide killian sad with fade
    pause 1.0
    
    call anime_route_verabris("Elvera", 22) from _call_anime_route_verabris

label anime_route_verabris(month, date):
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Killan_Own_Month8_"

    call screen calendar(month, date, "Verabris", 9)
    scene bg classroom_anime_afternoon with fade

    $ renpy.notify("Killian - Secret Talent\nZeday, Verabris 9th, 1028 RD")

    "I can’t help but keep thinking about that afternoon in the chapel. Killian seems to be fine but, even still, he also seems different now."
    "On the bright side, I’m able to see him again at least, even if he doesn’t say much."
    "Come to think of it, I can’t remember if he’s ever spent time with anyone else from the club…"
    "I swing by 3-3 one last time just to check up on him. When I get there, I’m greeted by a melody and a near empty room."
    "Once I walk through the door, however, the melody stops. Killian, holding an ocarina in his hands, almost seizes up when he sees me."
    play music hatchling10 fadein 1.0

    show killian surprised with hpunch
    vl killian_vl_prefix 1
    k "M-mx. Blakesley! I didn’t know you’d be stopping by."

    a "Well, I’ve been coming through almost every week this year. Why would this week be any different?"

    "Killian tries to put the instrument away."

    a "Where’d you learn to play?"

    show killian neutral with dissolve
    vl killian_vl_prefix 2
    k "M-my grandfather. It’s his actually."

    a "The instrument or the song?"

    show killian surprised with hpunch
    vl killian_vl_prefix 3
    k "W-what?"

    a "Is it your grandfather’s ocarina or were you playing a tune your grandfather wrote?"

    show killian neutral with dissolve
    vl killian_vl_prefix 4
    k "Oh. It’s his. The instrument I mean. I… Sorry…"

    a "What are you apologizing for?"

    vl killian_vl_prefix 5
    k "It’s just… I wasn’t exactly expecting anyone to show up today."

    a "I see. So, you’ve told them?"

    vl killian_vl_prefix 6
    k "Yeah. It’s just a room now. Plus, I didn’t feel in the mood to watch anything so I figured I’d just prac-"

    a "How come you never played for the club?"

    vl killian_vl_prefix 7
    k "…I’m not really fond of crowds all that much if I’m being quite honest. Or audiences, for that matter."

    "That makes two of us."

    vl killian_vl_prefix 8
    k "Hey, [a]."
    voice sustain
    a "Hmm?"
    voice sustain
    k "Do you know what you’re gonna do? When all of this is over, I mean."

    a "It’s hard to say. I’ll be working and sending money back to the family, I know that much."

    vl killian_vl_prefix 9
    k "And what will you do when the work is done?"

    a "I… Don’t know. I never thought about that, honestly. Any recommendations?"

    show killian happy with dissolve
    vl killian_vl_prefix 10
    k "Catch up on some stories, learn an instrument. Something to pass the time, stave off the agony of being, y’know?"

    vl killian_vl_prefix 11
    "We share a laugh and the next thing I know, I pull up a seat next to him."

    "His body language is still tense but, after just sitting there in silence almost like we were in that church pew from before, he relaxes."

    "Pupils contracting, shoulders sliding down back at a casual level, breathing becoming regular again."

    a "Can I stay?"

    "He caresses my hand with both of his and gives me a nervous smile."

    "Then he starts playing his tune again until the sun sets on MIA."

    scene black with fade
    "No more thoughts about what’s next. Just us in the present."
    stop music fadeout 1.0
    #hide killian happy with fade
    

    #jump to second clubd route verabris
    $ renpy.call(chosen_club2 + "_route_verabris", "Verabris", 9)
    #jump student_council_verabis

label anime_route_overa(month, date):
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Killan_Own_Month9_"

    call screen calendar(month, date, "Overa", 24)
    scene bg maincastle with fade
    play music hatchling10 fadein 1.0

    $ renpy.notify("Killian - Call Me Killian\nToleday, Overa 24th, 1028 RD")

    "Dad never said much when I knew him."
    "I don’t know how much of that was him working all the time, and I was too young to realize it then, but I sometimes wonder how much of that was just him."
    "I don’t know how he felt wearing more than one hat—as a father, a husband, a breadwinner—or if he even knew that when he was alive."
    "I just hope that he never felt restricted to only those titles in life."
    "And maybe, because I can never ask him myself, that’s why he’s been on my mind lately."
    "Needless to say, the end of the year has me thinking more introspectively than usual. A lot’s happened. But soon, all of that will be behind me."
    "And all I’ll be able to do from then on is look back."
    "Everything must end. Whether it be on our own terms or life throws a wrench at your head, nothing lasts forever."
    "Sue’s held the last Student Council meeting recently, and I don’t know if it’s just me but the meeting has made everything feel more {b}real{/b}."

    #[Beat.]

    "I figured, since it’s worked in times like these this year, I’d go for a walk."
    stop music fadeout 1.0

    scene bg mainstreet_afternoon with fade 
    play music hatchling1 fadein 1.0

    "Everyone’s in a hurry on Main Street. Everyone knows where to go and I envy them all."
    "The future’s inevitable and I don’t know how to feel about that."
    "It’s kinda like that old saying: \"Forever’s never long until you’re in it.\" The only problem I find with that statement is that it never mentions the space between now and the rest of your life."
    "I guess the only way to fight the feeling is to step out of that and stick to the present. Count blessings, keep growing, and check in with the homies."
    stop music fadeout 1.0

    #[Beat.]

    "I eventually bring myself back down to reality and I find myself staring at a glass pane X’d out with caution tape for construction."
    "Inside, I can see ancient gaming cabinets that look like they’ve been collecting dust for however long they’ve been there."
    "But then I refocus my eyes and see that the flowers just over at the roundabout are in bloom."
    "What I fail to notice though is a familiar body hauling ass towards me in the distance."

    vl killian_vl_prefix 1.1
    k "MX. BLAKESLEY! MX. BLAKESLEY!"

    a "LOOK OUT!"

    with hpunch
    "A convertible almost sweeps his legs Killian but he clumsily avoids being isekai’d before catching up to me but not before trying to catch his breath."
    play music hatchling12 fadein 1.0

    show killian fear with hpunch 
    vl killian_vl_prefix 2.1
    k "Mx. Blakesley… Ah, Abyss take me, gimme a moment…"

    #[Beat.]
    vl killian_vl_prefix 3.1
    k "I’ve got good news… I wanted to tell you…"

    a "Oh. Well, that’s great and all but you already have my number, you could’v-"

    show killian surprised with dissolve
    vl killian_vl_prefix 4.1
    k "News this big deserves an in-person delivery! Like business deals and pregnancy announcements!"

    a "Okay then. What’s up? Oh wait! Were you actually able to save the AMA?"

    show killian happy with dissolve
    vl killian_vl_prefix 5.1
    k "Gods no! That would’ve been really cool but no. I wanted to let you know that I know what I want to do after we all graduate."

    a "Oh… Okay. I’m glad you’ve got your life sorted ou-"

    show killian sad with hpunch
    vl killian_vl_prefix 6.1
    k "PLEASE LET ME BE WITH YOU!"

    a "Wh-... What?"
    stop music fadeout 1.0

    show killian neutral with dissolve
    if eval(a.name)[0] == "Alexis":
        vl killian_vl_prefix 7.2    
    else:
        vl killian_vl_prefix 7.1
    k "Only if you’ll have me. [a]."
    
    play music hatchling10 fadein 1.0
    "We look at each other after that, not knowing how to proceed with this interaction that should honestly be a lot more serious than how it’s currently going down."
    "Then, Killian shuffles around for something in his lapel pockets and proceeds to pull out fucking index cards."

    if eval(a.name)[0] == "Alexis":
        vl killian_vl_prefix 8.2
    else:
        vl killian_vl_prefix 8.1
    k "\"To [a]...\""
    vl killian_vl_prefix 9.1
    k "\"I hope you can forgive me for confessing in this manner but I knew I wouldn’t be able to get the words out because of my racing heart.\""
    vl killian_vl_prefix 10.1
    k "\"When you walked through the door earlier in the year, I never knew that I would be met with a force of nature.\""
    vl killian_vl_prefix 11.1
    k "\"Because of you, I am able to realize that while I may consider myself to just be a singular entity in this world I am actually many.\""
    vl killian_vl_prefix 12.1
    k "\"That is to say that, as stupid as it sounds, had you not helped me realize that nobody can truly understand me and look out for me but me,"
    voice sustain
    k "I wouldn’t have been able to learn how to take care of myself.\""
    vl killian_vl_prefix 13.1
    k "\"So I wanted to ultimately thank you for everything that you’ve done for me. And if you’d be interested, I humbly ask you to let me be with you."
    voice sustain
    k "So that we can one day understand ourselves well enough to take care of one another.\""
    stop music fadeout 1.0

    jump anime_route_overa_choice

label anime_route_overa_choice:

    if player_gender == "male":
        $ killian_platonic = True
        jump anime_route_overa_platonic
    else:
        menu:
            "Accept Killian's confession":
                $ killian_romance = True
                jump anime_route_overa_romance_accept

            "Reject Killian's confession":
                $ killian_romance = False
                jump anime_route_overa_romance_reject
            
label anime_route_overa_romance_accept:

    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Killan_Own_ConfessionAccepted_"

    scene bg mainstreet_afternoon with fade 
    show killian fear at center

    a "Okay."

    hide killian fear with fade
    "Killian takes a step back and looks at me like he’s seeing a ghost before running off in a hurry."
    "I run after him and eventually find him under the shade of a tree, out of breath, hand over his mouth, trying to stifle back tears of joy."
    play music hatchling10 fadein 1.0

    show killian sad with dissolve
    a "…Hey. Are you okay?"

    vl killian_vl_prefix 1.1
    k "I’m sorry you have to see me like this… I didn’t actually expect this to happen… I wasn’t ready for all of… This…"

    #[Beat.]

    vl killian_vl_prefix 2.1
    k "Even after reading and watching so many rom-coms, it wasn’t enough to prepare me for the way I feel—the way I’m feeling for you—right now…"

    #[Beat.]

    vl killian_vl_prefix 3.1
    k "I’m sorry for being so weird."

    a "…I don’t care that you’re weird, you know."

    a "Everyone’s weird in their own way. There is no \"normal\". You need to know that."
    a "So there’s no reason to distance yourself from the rest of the world because of that."

    "I stand him up straight and embrace him."

    a "Don’t worry. I’m here with you."

    "The feeling behind those glasses of his can’t help but pour over. But we’re both at ease, finally resting in each other’s bubbles."
    "Our foreheads bump into each other as he tries to lower himself to my height, flashing a smile after rubbing the pain away."

    show killian happy with dissolve
    vl killian_vl_prefix 4.1
    k "Thanks for putting up with me."

    stop music fadeout 2.0
    a "Thanks for letting me in."

    call epilogue_graduation("Overa", 24) from _call_epilogue_graduation_3

label anime_route_overa_romance_reject:
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Killan_Own_ConfessionRejected_"

    scene bg mainstreet_afternoon with fade

    #[Beat.]
    vl killian_vl_prefix 1.1
    k "…Thank you for being honest. And for everything from before."
    vl killian_vl_prefix 2.1
    k "I’m glad to see you this one last time. Even if things didn’t really pan out exactly how it went in my head…"
    vl killian_vl_prefix 3.1
    k "I guess I need to lay off the rom-coms for a bit… I’ll be leaving forever now."
    hide killian sad with fade

    "Killian calmly walks off without another word. I do feel bad but there’s simply nothing there for me. Because the love I have for him isn’t the kind he’s seeking."

    "After a few solemn minutes, I find Killian alone on a patch of green, sitting under the shade of a tree, hugging his knees together like a scared boy."

    show killian neutral with dissolve
    a "…H-hey."

    vl killian_vl_prefix 4.1
    k "Oh. Hey…"

    a "I’m sorry."

    vl killian_vl_prefix 5.1
    k "Don’t be. There’s no need to worry about me. These sorts of situations are only like this for a little bit."
    vl killian_vl_prefix 6.1
    k "And I have nothing against you. It's just… It always hurts when someone says they don’t want you, y’know?"

    a "It’s not that. I just…"

    a "I can’t… It’s not there for me. I’m sorry but I just can’t. I still feel for you but not in that way."

    vl killian_vl_prefix 7.1
    k "Just… Let me be for a while… "
    vl killian_vl_prefix 8.1
    k "I’ll get over it… "
    vl killian_vl_prefix 9.1
    k "I always do…"
    call epilogue_graduation("Overa", 24) from _call_epilogue_graduation_4

label anime_route_overa_platonic:
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Killan_Own_PlatonicReaction_"

    #$ killian_platonic = True

    scene bg mainstreet_afternoon with fade 

    a "…Were we not doing that already?"

    vl killian_vl_prefix 1.1
    k "I… I suppose you’re not wrong."
    vl killian_vl_prefix 2.1
    k "But wait, how long have you felt that way?"

    a "Since we first met. Though, I’ll admit, I was a bit skeptical at first, all reservations were brushed aside once we really got to know each other."

    show killian surprised with hpunch
    vl killian_vl_prefix 3.1
    k "WAIT, WHAT?! THAT WAS SO LONG AGO, OH MY GOODNESS!"

    a "I mean, yeah. Everyone’s gotta make friends somehow."
    play music hatchling10 fadein 1.0

    show killian fear with dissolve
    vl killian_vl_prefix 4.1
    k "Make… Friends… Right."

    a "Are you alright?"

    vl killian_vl_prefix 5.1
    k "Hm? Oh, yeah. Just need to catch my breath again."

    "I go over and pull him in for a hug since he’s trying to be vague and mysterious again. One of these days, that act’s gonna reel someone in for him."

    a "Have you had anything to eat? Why don’t we go find some ramen around here? We gotta celebrate graduation somehow, right?"

    show killian neutral with dissolve
    vl killian_vl_prefix 6.1
    k "Right."

    #[Beat.]
    if eval(a.name)[0] == "Alexis":
        vl killian_vl_prefix 7.1
    else:
        vl killian_vl_prefix 7.2
    k "Um… [a]?"

    a "Yeah, Killian?"

    vl killian_vl_prefix 8.1
    k "Thanks for being there for me. Even when I couldn’t be there for me."

    a "Of course. What else are good friends for?"

    show killian happy with dissolve
    vl killian_vl_prefix 9.1
    k "Yeah, yeah…"

    #[Beat.]

    show killian neutral with dissolve
    if eval(a.name)[0] == "Alexis":
        vl killian_vl_prefix 10.2
    else:
        vl killian_vl_prefix 10.1
    k "Hey, [a]."

    a "Yeah?"

    vl killian_vl_prefix 11.1
    k "Do you really think that everything’s gonna be alright? Today and tomorrow and every other tomorrow?"

    a "I hope so. If not, at least I know I’ve got back up on my side, right?"

    vl killian_vl_prefix 12.1
    k "I’ll do my best, my liege."
    stop music fadeout 1.0
    scene black with fade
    
    call epilogue_graduation("Overa", 24) from _call_epilogue_graduation_5

label epilogue_anime_route:

    scene bg maincastle with fade 

    "I start weaving my way through the crowd of celebrants, trying to get out of the congestion"
    "There can’t be that much longer until I’m free."
    jump epilogue_killian_choice
 
label epilogue_killian_choice:
    if chosen_club == "anime":
        if killian_romance:
            jump epilogue_anime_route_romance_accept
        elif killian_platonic:
            jump epilogue_anime_route_platonic
        else: 
            jump epilogue_anime_route_romance_reject
    else:
        jump epilogue_anime_route_not_chosen
    
label epilogue_anime_route_romance_accept:
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Shared Epilogue/Killian_Epilogue_GoodbyeToKillian_"

    "As I make my way, I spy a familiar face. Someone’s just left him, so it looks like he’s free, anyway…"

    show killian happy at center with dissolve
    a "Killian!"

    if eval(a.name)[0] == "Alexis":
        vl killian_vl_prefix 1.1
    else:
        vl killian_vl_prefix 1.7
    k "Mx. Blakesley— wait, no. [a]. There you are. What’s up?"

    a "Trying to get out of the crowd to go meet up with my family."

    show killian neutral
    vl killian_vl_prefix 2.2
    k "Same. My dad and I were going to go out to eat after this."

    a "Whatever’s on the menu, I hope it’s  delicious."

    vl killian_vl_prefix 3.1
    k "Right. Listen, do you have many plans for the summer?"

    a "I shouldn’t, anyway."

    vl killian_vl_prefix 4.1
    k "Good. Prospera Mitsuri’s in a few months, and even after this year, you desperately need more anime exposure."

    a "There’s an anime convention in Prospera?"

    vl killian_vl_prefix 5.1
    "He groans."
    voice sustain
    show killian disgust with dissolve
    k "And that’s exactly my point. That one first, then I’m going to have to find out what other cons to drag you to."

    a "Just the two of us?"

    "He blinks."
    
    show killian surprised with hpunch
    vl killian_vl_prefix 6.1
    k "I… didn’t think that far ahead. Yeah, I guess it would be."

    a "Then I’ll look forward to it."

    show killian happy with dissolve
    vl killian_vl_prefix 7.1
    k "Yeah. Me too."

    #[Beat.]

    show killian neutral
    vl killian_vl_prefix 8.1
    k "Well, we both have family to find, so…"

    "I can’t help but laugh with his cheeks flushing so fast."

    a "Talk to you later."

    scene black with fade
    jump epilogue_home_ec_route

label epilogue_anime_route_romance_reject:
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Shared Epilogue/Killian_Epilogue_GoodbyeToKillian_"

    "Soon it’s my turn to bump into someone. Thankfully, it doesn’t look like I made them drop anything."

    a "I’m sorry about that…"

    show killian neutral at center with dissolve
    "Killian looks down at me. For a moment, his face is a stone wall, whatever’s going through his head impossible to read."
    "Then a small smile creeps onto his face."

    vl killian_vl_prefix 9.2
    k "Mx. Blakesley. Don’t worry about it, not with the crowd."

    a "So, um…"

    show killian happy with dissolve
    vl killian_vl_prefix 10.2
    k "Congratulations on making it out the other end."

    a "Oh! Same to you, too."

    show killian neutral
    vl killian_vl_prefix 11.2
    k "I have to go meet up with my dad, so I’ve got to run. Talk to you sometime later?"

    a "Yeah, definitely."

    "With a small nod, he leaves me. I have places to be myself, but there’s a lingering worry that he didn’t have to leave that quickly."

    "Maybe it’s still too soon. When we do get to talk later, I just hope we’ll be able to go back to some semblance of how we were before."

    scene black with fade
    jump epilogue_home_ec_route

label epilogue_anime_route_platonic:
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Shared Epilogue/Killian_Epilogue_GoodbyeToKillian_"

    "As I make my way, I spy a familiar face. Someone’s just left him, so it looks like he’s free, anyway…"

    show killian neutral at center with dissolve
    a "Killian!"

    vl killian_vl_prefix 12.1
    k "Mr. Blakesley, there you are. What’s up?"

    a "Trying to get out of the crowd to go meet up with my family."

    vl killian_vl_prefix 13.1
    k "Same. My dad and I were going to go out to eat after this."

    a "Whatever’s on the menu, I hope it’s delicious."

    vl killian_vl_prefix 14.2
    k "Right."

    "His face sets, and when he next speaks, the gravity of his words sends a shiver down my spine."

    vl killian_vl_prefix 15.2
    k "Before we both head home, there’s something I have to warn you about."

    a "D-did something happen?"

    vl killian_vl_prefix 16.1
    k "I…"

    a "You? What’re you going to do, Killian?"

    show killian happy with dissolve
    vl killian_vl_prefix 17.2
    k "…Am going to absolutely blow your phone up with seasonal anime you should be checking out."

    vl killian_vl_prefix 18
    "The silence lasts for a good thirty seconds before he bursts out laughing."

    a "You are so lame, man."

    vl killian_vl_prefix 19.1
    k "Can you blame me? I can’t have you reverting back to your normie ways."

    a "What? So you’re trying to corrupt me?"

    "He starts whistling."

    show killian neutral with dissolve
    a "Okay, Killian."

    vl killian_vl_prefix 20.2
    k "We’ve both got family to find, don’t we?"

    a "You’re right. Don’t want to keep them waiting too long. Talk to you later."

    "With a final wave he heads off, leaving me to continue on my way. But the thought of him blowing up my phone…"
    "For as goofy as it is, it’s oddly worrying in its own way."

    scene black with fade
    jump epilogue_home_ec_route

label epilogue_anime_route_not_chosen:
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Shared Epilogue/Killian_Epilogue_GoodbyeToKillian_"

    "Soon it’s my turn to bump into someone. Thankfully, it doesn’t look like I made them drop anything."

    show killian neutral at center with dissolve
    a "I’m sorry about that…"

    "Killian—I’m pretty sure that was his name—looks down at me."

    vl killian_vl_prefix 21.2
    k "Oh, the not-first-year. Looks like you survived."

    a "That’s how you remember me?"

    vl killian_vl_prefix 22.1
    k "Good on you for making it out the other end."

    a "Same to you."

    vl killian_vl_prefix 23.1
    k "I have to go meet up with someone, so I’ve got to run. Take care out there."

    scene black with fade
    jump epilogue_home_ec_route

label reuinion_anime_route:
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Shared Epilogue/Killian_Epilogue_MeetTheFamily_"
    $ arline_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Arline/Epilogue/Meet Killian/Arline_Epilogue_MeetKillian_"
    $ skylar_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Skylar/Meet Killian/Skylar_Epilogue_MeetKillian_"
    $ salem_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Salem/Meeting Killian/Salem_Epilogue_MeetKillian_"

    $ renpy.notify("Killian - Meeting the Family\nNyday, Overa 25, 1028 RD")

    "When Killian arrives, he takes my mother’s hand in his and places a delicate kiss upon it."

    show killian happy at center with dissolve
    vl killian_vl_prefix 1.1
    k "Blessed am I to have this opportunity to meet the Mother of Worlds; my world, and gaze upon the radiance of the one who brought forth my beloved."

    a "What."

    if eval(a.name)[0] == "Alexis":
        vl arline_vl_prefix 1-A
    else:
        vl arline_vl_prefix 1-N
    arline "Ah, a gentleman and a poet. You’ve found yourself a keeper, [a]."

    vl skylar_vl_prefix 1
    sky "…Was that a \"Lightning Strikes Red Thread\" reference?"

    "Killian perks up at the sound of the title. It sounds familiar to me too, for some reason. But where did I hear it?"

    vl killian_vl_prefix 2.1
    k "You’ve seen it?"

    vl skylar_vl_prefix 2
    sky "Huh?"

    a "Do you not realize you said that out loud?"

    vl salem_vl_prefix 1
    salem "That’s that one romance movie I caught you watching, right?"

    show killian neutral with dissolve
    vl killian_vl_prefix 3.1
    k "Movie? That scene was from episode seventy-six."

    vl salem_vl_prefix 2
    salem "Whoa."

    vl skylar_vl_prefix 3
    sky "W-well, it was a compilation movie, so-!"

    a "They crammed over seventy episodes into a single movie?"

    vl salem_vl_prefix 3
    salem "Damn. Nearly a hundred episodes all for a love story, huh? Wasn’t expecting you to be into something so girly."

    vl skylar_vl_prefix 4
    sky "I-I’m not, I swear…!"

    vl arline_vl_prefix 2
    arline "I don’t know what’s happening, but this seems like quite the spirited conversation."

    a "You’re right about that."

    vl killian_vl_prefix 4.1
    k "Not like it’s anything to be ashamed of. The show was revolutionary when it came out."
    voice sustain
    k "There’s a reason people still recommend it years later."

    vl skylar_vl_prefix 5
    sky "I just stumbled across it online. That’s all."

    vl salem_vl_prefix 4
    salem "Whatever helps you sleep at night."

    "There’s a brief moment of silence. Then, Salem leans over to Skylar."

    vl salem_vl_prefix 5
    salem "Totally looking it up later."

    vl skylar_vl_prefix 6
    sky "I will end you!"

    show killian happy with dissolve
    vl killian_vl_prefix 5.1
    k "Well, I’ve made a mess."

    a "They’re just like this. It’ll be fine. Probably."

    vl arline_vl_prefix 3
    arline "Why do I feel so old?"

    jump finale