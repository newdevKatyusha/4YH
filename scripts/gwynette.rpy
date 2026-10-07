label music_route_jinus(month, date):
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Own/Month 1/Gwynette_Month1_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Gwynette/Month 1/" + player_voice_prefix + "_Gwynette_Month1_"

    call screen calendar(month, date, "Jinus", 26)
    scene bg music_hall_noon with fade

    $ renpy.notify("Gwynette - \nZynday, Jinus 26th, 1027 RD")

    play music hatchling1 fadein 1.0

    "The first month of school’s already almost come and gone. Where did the time go? It took a few weeks, but I finally have time to give some other clubs a look."
    "I’ve never been good at singing or playing instruments, but hearing that the school had a music club, my interest was piqued. It was easy enough to ask around and locate the club room."
    "As I approach after school one day, I can hear music drifting from the club room long before I’m out in front of it. It's an interesting cacophony that meets my ears."
    "Some club members have been playing instruments for most of their lives, while others hadn’t picked one up until this month."
    "I’ve barely crossed the threshold into the room before I make eye contact with someone. A drachkin girl—wide, gleaming smile on her face—hurries over to me."
    
    show gwynette neutral at center with dissolve
    vl gwynette_vl_prefix 1
    "Drachkin Girl" "Hey! Glad you were able to make it."
    
    vl alexis_vl_prefix 1
    a "Y-yeah. Been busy this past month, but finally had a chance to stop by."
    
    "Have I seen this girl before? That greeting felt a little too familiar…"
    
    vl gwynette_vl_prefix 2
    "Drachkin Girl" "Eh, it happens. Let me show you around the club."
    
    "She turns and begins to walk away."
    
    vl alexis_vl_prefix 2
    a "Um, I’m sorry, but… have we met before?"
    
    "Turning back, the girl crosses her arm and tilts her head."
    
    vl gwynette_vl_prefix 3
    "Drachkin Girl" "You don’t remember me?"
    
    vl alexis_vl_prefix 3
    a "Sorry…"
    
    vl gwynette_vl_prefix 4
    "Drachkin Girl" "Well, I guess it has been a while since we met. BB, it’s me, Gwynette!"
    
    "First it’s \"BB\" that jogs my memory. Then the name \"Gwynette\" hits me. We have met before but…"
    
    vl alexis_vl_prefix 4
    a "What happened to you?! I mean…"
    
    vl gwynette_vl_prefix Laugh
    "She looks confused, but after a moment, she starts to laugh."
    
    vl gwynette_vl_prefix 5
    gw "Oh, that? My piercings are clip-ons, and my tattoos are temporary."
    
    vl alexis_vl_prefix 5
    a "But… why?"
    
    vl gwynette_vl_prefix ClearThroat
    "She straightens her back and clears her throat, a satisfied look on her face."
    
    vl gwynette_vl_prefix 6
    gw "\"We are born bare, with not a blemish upon our flesh. As we would not deface a temple with obscene markings, nor bore holes into its walls for unnecessary decoration, let us not do the same to the bodies the Divines have gifted us.\""
    
    vl alexis_vl_prefix 6
    a "Were you quoting someone?"
    
    vl gwynette_vl_prefix 7
    gw "Contact Alexius I. From the Middle Ages."
    
    "Boy, this girl is {b}religious{/b}. It’s one thing to cite a leader of the Church to explain away… how much her look’s changed, but one I’ve never heard of from the middle of the millennium?"
    
    vl alexis_vl_prefix 7
    a "That’s… very interesting."
    
    vl gwynette_vl_prefix 8
    gw "It’s alright if you think I’m crazy. You wouldn’t be the first."
    vl gwynette_vl_prefix 9
    gw "So, how about that tour?"
    
    vl alexis_vl_prefix 8
    a "Oh, right."
    
    "Gwynette takes me around the room, pointing out the various instruments and introducing me to some of the other club members."
    "I’m, frankly, distracted throughout most of the tour, still trying to wrap my mind around this awkward reunion."
    
    vl gwynette_vl_prefix 10
    gw "So, hit me."
    
    vl alexis_vl_prefix 9
    a "Huh?"
    
    "We’ve stopped in a corner of the club room, away from most of the others."
    
    vl gwynette_vl_prefix 11
    gw "Sing a little something for me. Your pick."
    
    vl alexis_vl_prefix 10
    a "Oh, um…"
    
    "I came to a music club. Why is it just hitting me that I’d have to sing in front of people?"
    
    vl gwynette_vl_prefix 12
    gw "No pressure. We have the entire year ahead of us. You could always try next time."
    
    vl alexis_vl_prefix 11
    a "I think I’ll just listen today, yeah."
    
    vl gwynette_vl_prefix 13
    gw "Well then, my dear BB, allow me to serenade you!"
    
    "What starts as Gwynette singing just to me quickly becomes an impromptu, club-wide a cappella concert. As Gwynette’s voice rises, she begins marching around, stealing people away from whatever they were doing to join her."
    "I sit on the sidelines, enjoying the show, until I finally become aware of the time that’s passed. Club’s set to end soon. Even if it wasn’t, I’ve got homework to do."
    "I take up my bag and head for the door. Gwynette stops me before I head out."
    
    vl gwynette_vl_prefix 14
    gw "Sorry! Didn’t mean to ignore you there."
    
    vl alexis_vl_prefix 12
    a "Don’t worry about it. I got a damn good show."
    
    vl gwynette_vl_prefix 15
    gw "If you really don’t mind, how about you return the favor next time?"
    
    vl alexis_vl_prefix 13
    a "I’ll try practicing in the shower so I don’t embarrass myself."
    
    vl gwynette_vl_prefix 16
    gw "Looking forward to it. See ya later, BB!"
    
    scene black with fade
    "For how little I actually did, I’ve got to say, Music Club left a pretty good first impression. I can’t help but wonder, what kind of miniature concert am I in for  next week?"

    stop music fadeout 1.0

    call music_route_dallinus("Jinus", 26) from _call_music_route_dallinus

label music_route_dallinus(month, date):
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Own/Month 2/Gwynette_Month2_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Gwynette/Month 2/" + player_voice_prefix + "_Gwynette_Month2_"

    call screen calendar(month, date, "Dallinus", 5)
    scene bg mainstreet_afternoon with fade

    $ renpy.notify("Gwynette - \nNyday, Dallinus 5th, 1027 RD")

    play music hatchling1 fadein 1.0

    "Sue and I were busy after this latest Student Council Meeting. It ended hours ago, but I’m only now able to head back to my dorm. And that was with my help. I shudder to think how long she would’ve been held up without me."

    scene bg bus_terminal with fade
    "I pass by a bus stop, then stop. I look over my shoulder. A drachkin girl in MIA’s uniform sits on the bench, head downturned. It takes me a second to recognize her."
    
    vl alexis_vl_prefix 1
    a "Gwynette?"
    
    show gwynette neutral
    "She looks up at me and smiles, though it’s devoid of the joy I’m used to."
    
    vl gwynette_vl_prefix 1
    gw "BB, hey."
    
    vl alexis_vl_prefix 2
    a "Bit of an odd place to take a load off, don’t you think?"
    
    vl gwynette_vl_prefix 2
    gw "I guess it is."
    
    "She hops to her feet."
    
    vl gwynette_vl_prefix 3
    gw "So, what’s up?"
    
    vl alexis_vl_prefix 3
    a "Wrapped up some work for the Student Council. On my way back to House Lychester."
    
    stop music fadeout 1.0
    vl gwynette_vl_prefix 4
    gw "The SC? I do think I remember hearing that you were Susu’s assistant."

    play music hatchling22 fadein 1.0
    
    vl alexis_vl_prefix 4
    a "Isn’t the point of a nickname to be {b}shorter{/b} than someone’s actual name?"
    
    vl gwynette_vl_prefix 5
    gw "Nuh-uh! The point is to be cuter."
    
    vl alexis_vl_prefix 5
    a "How is \"Dick\" cuter than \"Richard\"?"
    
    vl gwynette_vl_prefix 6
    gw "I could think of a cute Dick or two if I try hard enough."
    
    #"[Beat.]"
    
    vl gwynette_vl_prefix 7
    gw "Oh."
    
    vl gwynette_vl_prefix Laugh
    "She bursts out laughing. I can’t help but join in."
    
    vl alexis_vl_prefix 6
    a "Excellent choice of words."
    
    "When I calm down, I’m reminded of how this little interaction started."
    
    vl alexis_vl_prefix 7
    a "What were you doing out here anyway?"
    
    vl gwynette_vl_prefix 8
    gw "Oh, right."
    
    "Gwynette’s shoulders slump as she comes back down to Unios."
    
    vl gwynette_vl_prefix 9
    gw "I was waiting for VV."
    
    vl alexis_vl_prefix 8
    a "He’s running late?"
    
    vl gwynette_vl_prefix 10
    gw "{b}Very{/b} late."
    
    "So the poor girl got stood up."
    
    vl alexis_vl_prefix 9
    a "Well, how about a drink, on me?"
    
    vl gwynette_vl_prefix 11
    gw "Are you sure? I wouldn’t want to bother you."
    
    vl alexis_vl_prefix 10
    a "Not at all. Come on, follow me."
    
    scene black with fade

    "So back to the Wilson Building I go, Gwynette by my side. Surely that salon on the third floor is still open, right?"

    scene bg wilson_salon_afternoon with fade
    
    show gwynette neutral at center with dissolve
    vl gwynette_vl_prefix 12
    gw "Ah, what a cute little place!"
    
    "There are still a few people left in the salon. At Gwynette’s excited outburst, they give us a brief look before returning to their drinks and conversations."
    "A server leans us to a vacant table and leaves us with a pair of menus. Gwynette wastes no time flipping through hers."
    
    vl gwynette_vl_prefix 13
    gw "It’s like The Amity, but fancier."
    
    vl alexis_vl_prefix 11
    a "Figure that’s the point. So all the fancy people can feel the part."
    
    vl gwynette_vl_prefix 14
    gw "I never knew about this place."
    
    vl alexis_vl_prefix 12
    a "Only found out about it recently from Reina. Nobles and club presidents only."
    
    vl gwynette_vl_prefix 15
    gw "And I’m guessing the new kid didn’t start a new club just to get an invite?"
    
    vl alexis_vl_prefix 13
    a "That’s right."
    
    "There’s a moment of silence. Then I realize there was a second question hidden in what she said."
    
    vl alexis_vl_prefix 14
    a "I’m from a viscount’s family down south. We live in Prospera."
    
    vl gwynette_vl_prefix 16
    gw "Just a viscount? Darn. I was hoping I was rubbing elbows with a dukeling."
    
    vl alexis_vl_prefix 15
    a "My most sincere apologies for not being blue-blooded enough, my lady."
    
    vl gwynette_vl_prefix 17
    gw "Hmm… I fear that apology won’t suffice. Please grovel before me in recompense."
    
    vl gwynette_vl_prefix Laugh2
    "We share another laugh."
    
    vl alexis_vl_prefix 16
    a "Feeling any better?"
    
    vl gwynette_vl_prefix 18
    gw "A bit, thanks. Some time with a friend is exactly what I needed."
    
    vl alexis_vl_prefix 17
    a "I’m just glad I passed by that bus stop when I did. Thank the Divines I had so much work to do, huh?"
    
    vl gwynette_vl_prefix 19
    gw "\"Thank the Divines,\" indeed."
    
    "It was meant to just be a common turn of phrase, but now that I think about it, those three words must’ve meant a lot more to her than they did me."
    
    vl alexis_vl_prefix 18
    a "Do you… actually think the Divines bogged me down with work so I would run into you when I did?"
    
    vl gwynette_vl_prefix 20
    gw "Not directly, no. They don’t do that anymore. But, I do believe one of Them might’ve subtly nudged you to take the route you did. If you were just one street over, I’d still be sitting alone in the dark."
    
    "The server returned to take our orders, withdrawing shortly afterwards with the menus in hand."
    
    vl gwynette_vl_prefix 21
    gw "Hold on a second…"
    
    vl alexis_vl_prefix 19
    a "What’s up?"
    
    vl gwynette_vl_prefix 22
    gw "I know this song. I love it!"
    
    "I haven’t paid much attention to it, but there is a jazz song playing softly from the speakers. Fitting."
    "Even more fitting, Gwynette breaks out into song."

    show gwynette singing with dissolve
    "Like when we first arrived, people turn and stare. But Gwynette’s impromptu karaoke draws more unambiguous adoration than mild annoyance."
    "Listening to her dulcet tones makes me momentarily forget that I’m the one who tried to cheer {b}her{/b} up."
    "This soothing song is just the sort of thing that I’d put on when I was having a bad day and needed something to put me at ease."
    "She’s doing a great job with it."
    
    show gwynette neutral with dissolve
    "When Gwynette falls silent, people begin to applaud. She even earns herself a few standing ovations. At that, she giggles."
    
    vl gwynette_vl_prefix 23
    gw "Thank you, thank you! You were a wonderful audience."
    
    "With impeccable timing, our drinks arrive right as the song’s finished."
    
    vl gwynette_vl_prefix 24
    gw "Aw, one of my adoring fans bought me a drink. That’s so sweet of them."
    
    "I roll my eyes."
    
    vl alexis_vl_prefix 20
    a "Ha ha. Very funny."
    
    vl gwynette_vl_prefix 25
    gw "Thank you."

    scene black with fade
    stop music fadeout 2.0
    "As we drink, Gwynette gives me a history lesson. By the time we leave, I know more about the song she sang, who wrote it, and how they wrote it, than everyone else  in the salon combined. Save Gwynette, of course."
    
    scene bg mainstreet_night with fade
    play music hatchling1 fadein 1.0
    show gwynette neutral at center with dissolve
    vl gwynette_vl_prefix 26
    gw "I’m off to the chapel for a little bit. Later, BB. Thanks for tonight, too."
    
    vl alexis_vl_prefix 21
    a "Don’t mention it. See you later."
    
    "As we part ways, Gwynette and I get into a waving match, determined to be the last one left waving. My arm gives out before hers, and she turns with a satisfied little smile on her face."
    
    scene black with fade
    "Endless fount of optimism, that one. I don’t know how she does it. Maybe the Divines really are up there, looking out for her."

    stop music fadeout 2.0
    "Not like I have any way of knowing one way or the other."

    # jump to main club route dallinus
    $ renpy.call(chosen_club + "_route_dallinus", "Dallinus", 5)
    #jump music_route_dyalt

label music_route_dyalt(month, date):
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Own/Month 4/Gwynette_Month4_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Gwynette/Month 4/" + player_voice_prefix + "_Gwynette_Month4_"

    call screen calendar(month, date, "Dyalt", 6)
    scene bg mainstreet_noon with fade

    $ renpy.notify("Gwynette - \nLenday, Dyalt 6th, 1027 RD")

    play music hatchling1 fadein 1.0
    "I know shopping malls are going the way of the terra costa, but there’s just something about them. Maybe it’s because of how long it’s been since I was at a mall."
    "It’s been a little while since I last got a chance to hang out with Gwynette. Outside of Music Club, anyway. So we’re here to remedy that. At least for a little while."
    
    show gwynette neutral with dissolve
    vl gwynette_vl_prefix 1
    gw "Ooh, look, Variance Comics! Wanna go inside?"
    
    vl alexis_vl_prefix 1
    a "You read comics?"
    
    vl gwynette_vl_prefix 2
    gw "Nope! But the merch they’ve got is always super cool!"
    
    "Can’t argue with that."
    
    vl alexis_vl_prefix 2
    a "Lead the way."
    
    "Comic Books are only a fraction of what Variance carries. Trading Cards, model kits, miniatures, hats, tees, CDs, all manner of things."
    "I don’t think I’ve ever read a comic book, but I could easily find myself wandering into this place whenever I come to the mall or see it in the wild."
    "Gwynette stops by a shelf and gasps."
    
    vl gwynette_vl_prefix 3
    gw "\"In His Heaven\"? I didn’t know this had a manga. I thought it was an anime original…"
    
    "She picks it up and begins feverishly flipping through the pages."
    
    vl alexis_vl_prefix 3
    a "You’re a fan?"
    
    vl gwynette_vl_prefix 4
    gw "Just casual. But it’s wild. So much Nyrellan imagery, you can’t help but wonder what it all means."
    
    vl alexis_vl_prefix 4
    a "Sounds deep."
    
    vl gwynette_vl_prefix 5
    gw "People have been debating for decades whether it’s all because the director just thought it was cool."
    
    vl alexis_vl_prefix 5
    a "…I don’t know if I should be offended by that."
    
    vl gwynette_vl_prefix 6
    gw "I know, right?!"
    
    "Abruptly, she puts the volume down and picks up another one."
    
    vl gwynette_vl_prefix 7
    gw "Then there’s all the other things it inspired. There’s an old game that apparently does the whole \"religion\" thing a lot better."
    vl gwynette_vl_prefix 8
    gw "Never been much of a gamer, but maybe I should try it out one of these days."
    
    vl alexis_vl_prefix 6
    a "Is that a rabbit hole you want to go down?"
    
    vl gwynette_vl_prefix 9
    gw "Why not? Sounds like it would be fun."
    
    "She sets the volume down and continues to walk."
    
    vl gwynette_vl_prefix 10
    gw "I’ve lost count of how many times I’ve come in here over the years."
    
    vl alexis_vl_prefix 7
    a "Oh yeah? And how much have you bought?"
    
    "She winks at me."
    
    vl alexis_vl_prefix 8
    a "Serial loiterer."
    
    vl gwynette_vl_prefix 11
    gw "I prefer \"serial window shopper.\""
    
    vl alexis_vl_prefix 9
    a "If it helps you sleep at night."
    
    vl gwynette_vl_prefix 12
    gw "It does!"
    
    "And, true to her loitering ways, we leave without Gwynette buying anything."
    
    vl gwynette_vl_prefix 13
    gw "Do you like animals?"
    
    vl alexis_vl_prefix 10
    a "Depends on the animal. But, if it isn’t trying to kill me, why not?"
    
    vl gwynette_vl_prefix 14
    gw "Then off to the pet shop with us!"
    
    "She marches ahead, and I obediently follow."
    
    vl gwynette_vl_prefix 15
    gw "You know, I brought Ylva here last year. She was pretty icy, but after seeing some furry friends, she warmed up real quick."
    
    "I wouldn’t have expected that from what little I’ve seen of her. Guess that’s another reminder not to judge a book by its cover."
    "When we get to the pet shop, it hits me that I’ve never been in one of these, either. Squawks, meows, barks, and all manner of noises assault my ears."
    
    vl gwynette_vl_prefix 16
    gw "To the ferrets we go!"
    
    "Despite her declaration, I takemy leave of Gwynette. A trio of kittens caught my eye, and I can’t stay away."
    "Two, one black and one orange, are wrestling with each other while a third, fur white as snow and eyes as deep and blue as the sea, rests and watches them from a distance."
    "If not for the fact that I live in a dorm, I just might have taken all three."
    "The store has fewer animals than I expected. I find puppies playing like the kittens, rabbits idly munching hay, lizards perched on rocks underneath heat lamps. A bird dancing along to the store’s soft background music is a personal favorite."
    "True to her word, Gwynette is by the ferrets. She’s cradling one like a child when I arrive while a store employee keeps a watchful eye over her."
    
    vl gwynette_vl_prefix 17
    gw "Just the cutest little thing, isn’t he?"
    
    vl alexis_vl_prefix 11
    a "You’re right. Always thought I was a cat or dog person, but this little one’s an amazing salesferret."
    stop music fadeout 1.0
    pause 1.0
    play music hatchling21 fadein 1.0
    
    vl gwynette_vl_prefix 18
    gw "So, who do you think they were?"
    
    "I blink at her. Ignoring my confusion, she sets the ferret down onto a waiting play mat and picks up a wand toy. She waves it before the small animal, which begins dashing this way and that to catch it."
    
    vl gwynette_vl_prefix 19
    gw "A beloved grandmother surrounded by loved ones at the end? A vile villain who gave up the ghost in a prison cell? Maybe even someone else’s pet come again?"
    
    "Ah, so that’s what she means. Reincarnation is a core Nyrellan belief, so it only makes sense that Gwynette would bring it up."
    
    vl alexis_vl_prefix 12
    a "{b}Does{/b} it work the same for animals? I mean, a person being reborn as a ferret? Or a ferret as a person?"
    
    vl gwynette_vl_prefix 20
    gw "I guess it depends. Do you think souls are created? Or recycled?"
    
    vl alexis_vl_prefix 13
    a "Way to put me on the spot. But if there’s only so many to go around, I guess they {b}have{/b} to be included."
    
    "The ferret gets a hold of the wand and begins to roll around the mat with it clutched in its jaws."
    
    vl alexis_vl_prefix 14
    a "Seems a bit unfair for a \"vile villain\" to enjoy playing with people gushing over their cuteness."
    
    vl gwynette_vl_prefix 21
    gw "But it would be fair to the forlorn who died prematurely or bound to their sickbeds to have this newfound freedom, no?"
    
    "I imagine a parent telling a little child mourning a grandparent that they aren’t gone forever-just taking a short rest alongside the Divines before they come back down and live a new life"
    "I can even see a parent getting that same kid a pet and telling them it’s their grandparent come again to help lift their spirits."
    stop music fadeout 1.0
    "And, if it brings that child comfort, who am I to complain?"
    play music hatchling1 fadein 1.0
    "Gwynette gasps, then hurriedly says goodbye to the ferret and the pet store employee who was supervising her. She pats herself down and takes out her phone as she heads for the entrance."
    
    vl alexis_vl_prefix 15
    a "Run out of time?"
    
    vl gwynette_vl_prefix 22
    gw "Yeah, VV’s waiting for me. We’re taking a bus down to the capital for the rest of the day."
    
    vl alexis_vl_prefix 16
    a "Nice to hear you two made up."
    
    "Her only response is a nervous little laugh. Alright, then…"
    
    vl gwynette_vl_prefix 23
    gw "See ya later, BB."
    hide gwynette with dissolve
    
    "I see her off, but we don’t have a wave-off like she usually insists on. I really shouldn’t have gone ahead and assumed everything was perfect with her and Vincent."
    "But if it isn’t, why does she do it? How much is there to the guy I don’t get to see? Because, from what I’ve seen, it’s not looking good for him."

    scene black with fade
    stop music fadeout 2.0
    "Sighing, I start heading back to House Lychester. Their relationship is their business. Unless Gwynette comes to me in tears or something, best to give them space and respect their privacy."

    # jump to main club route dyalt
    $ renpy.call(chosen_club + "_route_dyalt", "Dyalt", 6)
    #jump music_route_neralt

label music_route_neralt(month, date):
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Own/Month 5/Gwynette_Month5_"
    $ ylva_vl_prefix = "audio/voices/Friends/Ylva/Gwynette/Month 5/Ylva_Gwynette_Month5_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Gwynette/Month 5/" + player_voice_prefix + "_Gwynette_Month5_"

    call screen calendar(month, date, "Neralt", 25)
    scene bg chapel_night with fade

    $ renpy.notify("Gwynette - \nZaeday, Neralt 25th, 1027 RD")
    
    play music hatchling21 fadein 1.0
    "I burst into the chapel, throwing the doors open far more forcefully than would ever be appropriate for a house of worship, but I’m not in the mood to care about propriety right now."
    "Scrolling the internet without a care in the world, only to get a random call from a crying Gwynette asking me to come here."
    "What happened to her?"

    show gwynette neutral at character_pos3 with dissolve
    show ylva neutral at character_pos5 with dissolve
    vl gwynette_vl_prefix Sob
    "The small sobs are what ultimately lead me to her. I let out a sigh of relief when I see Ylva sitting at her side, an arm wrapped around her."
    
    vl alexis_vl_prefix 1
    a "Gwynette, there you are. I was worried."
    
    vl gwynette_vl_prefix 1
    gw "S-sorry. Guess the call was kinda cryptic, huh?"
    
    if player_gender == "female":
        vl ylva_vl_prefix 1.2
        yl "That’s why I offered to talk to her for you."
    else:
        vl ylva_vl_prefix 1.1
        yl "That’s why I offered to talk to him for you."
    
    "I take a seat on a pew on Gwynette’s other side. I’m about to ask what happened, then it hits me. A crying Gwynette flanked by people, and neither one of them is her boyfriend."
    
    vl alexis_vl_prefix 2
    a "Dammit, Ziani…"
    
    "Ylva glances over at me."
    
    vl ylva_vl_prefix 2
    yl "Gwynette was asked to perform a hymn for the church this morning. She’s been looking forward to it all week."
    
    "And she no doubt told him as soon as she found out, only to look out into the pews and not see his face."
    
    vl alexis_vl_prefix 3
    a "What a piece of work."
    
    "Sputtering through her tears, Gwynette shakes her head."
    
    vl gwynette_vl_prefix 2
    gw "Don’t say that about him."
    
    vl ylva_vl_prefix 3
    yl "Maybe \"inconsiderate jackass\" would be more fitting."
    
    vl gwynette_vl_prefix 3
    gw "Stop that! He’s just… stressed."
    
    vl ylva_vl_prefix 4
    yl "No amount of stress justifies skipping this. It isn’t like you were asking much of him, and he couldn’t do even that?"
    
    vl alexis_vl_prefix 4
    a "\"Come to church a single morning to hear me sing, it means a lot to me.\" Such an easy assignment."
    
    vl gwynette_vl_prefix 4
    gw "Stop that, both of you."
    
    "Gwynette wipes her tears."
    
    vl gwynette_vl_prefix 5
    gw "I know you’re upset. And I know you think venting will make me feel better, because it’s putting down someone who hurt me, but he doesn’t deserve that."
    
    vl ylva_vl_prefix 5
    yl "And why doesn’t he? If my brother knew a boy was treating me like this, he’d—"
    
    "She falls silent and clears her throat."
    
    vl gwynette_vl_prefix 6
    gw "VV isn’t from Magiana. He’s from Archos. He’s here, all alone, and he doesn’t even want to be."
    
    "She glances at Ylva."
    
    vl gwynette_vl_prefix 7
    gw "You understand, don’t you? Being dumped in another country even when you insist you want to stay at home?"
    
    "The guilty silence that hits her gets a little smile out of Gwynette."
    
    vl alexis_vl_prefix 5
    a "Even if he’s a tragic figure, it doesn’t justify dragging someone down because he’s homesick or whatever."
    voice sustain
    a "You deserve better than him, Gwynette."
    
    vl gwynette_vl_prefix 8
    gw "I \"deserve better\"? Funny. That’s what VV said earlier when he…"
    
    vl alexis_vl_prefix 6
    a "Why did you do it, Gwynette?"
    
    vl gwynette_vl_prefix 9
    gw "Do what?"
    
    vl alexis_vl_prefix 7
    a "Even when it came to breaking it off, he had to do it. You were going to keep soldiering on, weren’t you? How could you put up with all of it?"
    
    "A moment of silence passes as she gathers her thoughts. Gwynette lets out a breath and begins to speak."
    
    vl gwynette_vl_prefix 10
    gw "Because I think it’s right. To be kind and extend a hand to him, even if he might slap it away."
    vl gwynette_vl_prefix 11
    gw "I’m an optimist to a fault, if you hadn’t already noticed."
    vl gwynette_vl_prefix 12
    gw "I try to not let things outside of his control affect how I see him. That isn’t fair."
    vl gwynette_vl_prefix 13
    gw "Letting resentment fester and consume me isn’t how I work, either. \"Forgive and forget\" is one of my mottos."
    vl gwynette_vl_prefix 14
    gw "Because I want to protect him from what might happen if he’s left all alone with everything he’s shouldering."
    vl gwynette_vl_prefix 15
    gw "Because I feel like, no matter how bad this is, I can bounce back and face the world stronger than I was before."
    vl gwynette_vl_prefix 16
    gw "And no matter how badly the bridge may get damaged, I’d rather repair it than let it fall apart, you know?"
    
    "It takes a bit of time to absorb everything she did. The more I do, the more radiant Gwynette becomes."
    "Grace, Mirthfulness, Empathy, Forgiveness, Guardianship, Tenacity, Harmony."
    
    vl alexis_vl_prefix 8
    a "You are… perfect."
    
    "She smiles at that, and I can’t help but smile back. If that small gesture boosted her spirits, I’m glad."
    
    vl alexis_vl_prefix 9
    a "Sorry, that’s not what I meant. I mean… that’s all {b}seven{/B} of the Divine Virtues."
    
    vl ylva_vl_prefix 6
    yl "And what does that mean?"
    
    a "That you’re sitting with the future Saint Gwynette of the Nyrellan Church."
    
    "Gwynette covers her mouth to suppress a laugh."
    
    vl gwynette_vl_prefix 17
    gw "Don’t say that. I’m not going to get canonized."
    
    vl alexis_vl_prefix 10
    a "Too late. I’ve already canonized you in my heart."
    
    "Ylva rolls her eyes."
    
    vl ylva_vl_prefix 7
    yl "Couldn’t you at least wait a few days before trying to seduce her?"
    
    vl alexis_vl_prefix 11
    a "I’m not trying to seduce her."
    
    "Although… That is a good point. Vincent did call it off. One day, Gwynette’s going to have to start thinking about this sort of thing again."
    
    vl alexis_vl_prefix 12
    a "You should let go, I think. Like you said, \"forgive and forget.\" But don’t expect him to make up for this, either."
    
    vl ylva_vl_prefix 8
    yl "I agree. If he does, good. But you shouldn’t torture yourself waiting for a day that may never come."
    
    vl gwynette_vl_prefix 18
    gw "You’re right, I shouldn’t."
    
    vl ylva_vl_prefix 9
    yl "It’s late. Let me walk you back to House Bryne?"
    
    "Gwynette nods, and Ylva helps her to rise."
    
    vl gwynette_vl_prefix 19
    gw "Thanks for stopping by, BB. Sorry if I made you panic."
    
    vl alexis_vl_prefix 13
    a "Don’t mention it. That’s what friends are for, right?"
    stop music fadeout 1.0
    
    scene mainstreet_night with fade
    show gwynette neutral at character_pos2
    show ylva neutral at character_pos5
    play music hatchling1 fadein 1.0
    "Outside of the chapel, I see the two off, watching them go for a time before turning and making my own way back to House Lychester."
    
    hide ylva with dissolve
    hide gwynette with dissolve
    "That certainly wasn’t how I expected to spend my night, but when I heard Gwynette in distress, what else was there to do?"
    "A part of me curses my traitorous mind for the thought that bubbles up. If I could drop everything to hear out Gwynette, why couldn’t Vincent spare an hour or two to drop by the chapel for her?"
    stop music fadeout 2.0
    "Whether they get back together or not, I hope Gwynette will be alright."
    
    call student_council_exalt("Neralt", 25) from _call_student_council_exalt
    #jump music_route_exalt

label music_route_exalt(month, date):
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Own/Month 6/Gwynette_Month6_"
    $ vince_vl_prefix = "audio/voices/Friends/Vince/Vincent_Gwynette_Month6/Vincent_Gwynette_Month6_"
    $ ylva_vl_prefix = "audio/voices/Friends/Ylva/Gwynette/Month 6/Ylva_Gwynette_Month6_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Gwynette/Month 6/" + player_voice_prefix + "_Gwynette_Month6_"

    call screen calendar(month, date, "Exalt", 22)
    scene bg chapel_day with fade

    $ renpy.notify("Gwynette - \nZaeday, Exalt 22nd, 1027 RD")

    play music hatchling21 fadein 1.0
    s "Over here!"
    
    "I enter the chapel to find it packed. Only makes sense on the Zaeday that’s kicking off the Week of Life, I guess. Sue’s waving over at me from her seat towards the front of the room. I make my way over to her. She isn’t alone, either."
    
    show sue neutral at character_pos1 with dissolve
    show reina neutral at character_pos4 with dissolve
    show ylva neutral at character_pos7 with dissolve
    r "Good morning, [a]."
    
    vl ylva_vl_prefix 1
    yl "Glad you could join us."
    
    vl alexis_vl_prefix 1
    a "Wouldn’t miss this for the world."
    
    "This time around, Gwynette extended an invitation to me to hear her perform at the chapel. Telling her I’d be there right on time was a no brainer."
    
    vl vince_vl_prefix 1
    vin "Shit. What are you doing here?"
    
    "I glance over my shoulder to see Vince standing there, holding a small gift box."
    
    hide sue with dissolve
    show vince neutral at character_pos1 with dissolve
    show reina worried
    show ylva neutral

    vl alexis_vl_prefix 2
    a "Funny, I was wondering the same thing."
    
    r "Such language in a church, really…"
    
    vl ylva_vl_prefix 2
    yl "Finally learned your lesson?"
    
    vl vince_vl_prefix 2
    vin "Guess you could say that. Move over, I’m sitting with you guys."
    
    "Vince and I take our seats. We end up next to each other, so I lean over and whisper to him."
    
    vl alexis_vl_prefix 3
    a "Gwynette tell you about this one, too?"
    
    vl vince_vl_prefix 3
    vin "If I didn’t think she’d want me here on {b}today{/b} of all days, I’m a lost cause."
    
    "Smart. Maybe there is some hope for him."
    
    vl ylva_vl_prefix 3
    yl "If seeing you throws Gwynette off, so help me Mother…"
    
    "Vince leans forward to get a look at Reina, who remains silent."
    
    vl vince_vl_prefix 4
    vin "So I can’t cuss, but she can swear by another god that she’s going to kill me?"
    
    vl ylva_vl_prefix 4
    yl "I never said that."
    
    r "And you’re quite the boor, so I understand her frustration."
    
    "He rolls his eyes and leans back, arms crossed."

    scene bg chapel_day with dissolve
    "When a priest finally does arrive, I do a double take. Just as suddenly, I scold myself for being so dumb. The first time I saw Instructor Wilson, I clocked him as a priest. Of course he’s the one who does sermons in this town."
    "I’m not one for church, I doubt Vince is, and it’s clear Ylva’s not Nyrellan, at least. Sue and Reina, though, might be a bit disappointed if they knew I {b}completely{/b} zoned out while Instructor Wilson spoke."
    "It isn’t until I hear him mention Gwynette’s name that I start paying attention. After introducing her, he steps away from the pulpit and allows her to be the sole figure at the front of the chapel."

    show gwynette singing with dissolve
    "She looks right at us and waves. When her eyes fall on Vincent, I notice tears welling up at the corner of her eyes."
    
    vl gwynette_vl_prefix 1
    gw "Good morning, everyone. Thank you all for joining us here today, on this sacred day, at the beginning of this sacred week."
    vl gwynette_vl_prefix 2
    gw "No doubt, all of us are going to feel all sorts of things during this week as we spend time with our loved ones and reflect on everything we’ve lost."
    vl gwynette_vl_prefix 3
    gw "So please, allow me to sing you a song that’s near and dear to my heart."
    
    "Then she begins to sing the Nyrellan Hymn."
    "I haven’t heard this song in {b}years{/b}."
    "The last time, my grieving mother had sung it as a final farewell to her beloved husband when he was laid to rest."
    "But then memories of a simpler time come flooding back to me. Of Mother, Father, Salem, Skylar and me, huddled together on the couch, watching movies late into the night."
    "Salem as a young boy, crying about the dark, and his precocious sister scolding him for needing  comfort when he should be the comforter."
    "Being lulled to sleep by one of my parents singing this song to me, while they held me like I was the most precious thing in the world."

    if chosen_club != "no_clubs":
        "Something tickles my cheek. I touch it, the tip of my finger coming away wet. A tear? I haven’t shed a tear since my father's funeral. That was so long ago now."
    
    "Louder sobs break out throughout the chapel. Out of the corner of my eye, I notice Sue and Reina wiping away tears, too."
    "When Gwynette ends her song, she takes a knee, hands clasped together. Even as her audience gives a standing ovation, she doesn’t hear them, absorbed in her own little communion with the Divines."

    hide gwynette
    "Vince rises, going to Gwynette’s side. When she opens her eyes, he’s the first thing she sees. He helps her up and escorts her over to us. They sit hand in hand for the rest of the service."
    "Later, once it’s over, most people remain to talk with friends. We’re no different."
    
    show sue happy at character_pos1 with dissolve
    show reina happy at character_pos4 with dissolve
    show ylva warm at character_pos7 with dissolve
    r "That was absolutely wonderful. You did a fantastic job."
    
    s "I haven’t heard such a beautiful rendition of the Hymn in years. Not since Sadachi released her cover, I don’t think."
    
    vl ylva_vl_prefix 5
    yl "I didn’t quite get it, but the song {b}was{/b} incredibly moving."
    
    hide reina
    show gwynette neutral at character_pos4
    vl gwynette_vl_prefix 4
    gw "Heehee, keep heaping on the praise!"
    
    hide sue
    show vince neutral at character_pos1
    vl vince_vl_prefix 5
    vin "Please don’t. It’ll go to her head."
    
    "Sue checks her phone."
    
    hide vince
    show sue neutral at character_pos1
    s "As much as I would like to, I do have to go."
    hide sue with dissolve
    show vince neutral at character_pos1 with dissolve
    
    hide gwynette with dissolve
    show reina neutral at character_pos4 with dissolve
    r "So do I. There are other things for me to attend to. Good day."
    hide reina with dissolve
    show gwynette neutral at character_pos4 with dissolve
    
    vl gwynette_vl_prefix 5
    gw "And then there was one."
    
    vl ylva_vl_prefix 6
    yl "One what?"
    
    vl gwynette_vl_prefix 6
    gw "Nyrellan. I don’t know about BB, but Ylva’s a Wayfarer, and VV’s a nullifidian."
    
    vl vince_vl_prefix 6
    vin "What did you just call me?"
    
    vl alexis_vl_prefix 4
    a "It’s true that I’m not big on religion. Not the end of the world though, right?"
    
    vl gwynette_vl_prefix 7
    gw "Nope! It’s sweet that you guys showed up for me."
    
    "All of a sudden, a look of profound sadness comes to her, though her smile remains."
    
    vl gwynette_vl_prefix 8
    gw "If only you could see me now, Slink."
    
    vl vince_vl_prefix 7
    vin "You have come a long way, huh?"
    
    vl alexis_vl_prefix 5
    a "Slink? Is that a person?"
    
    "Gwynette shakes her head."
    
    vl gwynette_vl_prefix 9
    gw "I had a real hard time making friends when I first moved here. Slink was my first. A {b}ferret{/b} I loved more than anyone else in the world."
    vl gwynette_vl_prefix 10
    gw "You know, his death is what started it all."
    
    "She looks towards the front of the chapel, where she stood before us all just a short while ago."
    
    vl gwynette_vl_prefix 11
    gw "If not for him, none of this would’ve ever happened. Look at me, my entire faith is based on a ferret."
    
    vl ylva_vl_prefix 7
    yl "I don’t see anything wrong with it. He was obviously important to you, so…"
    
    vl gwynette_vl_prefix 12
    gw "I’m just being dramatic. It’s nothing I’m ashamed of. I never could be. Not of him."
    
    "A line to try and lighten the mood comes to me."
    
    vl alexis_vl_prefix 6
    a "How does it feel to be second place to a ferret, Vince?"
    
    vl vince_vl_prefix 8
    vin "I made peace with that a long time ago. The issue is being, like, 19th. How many Divines are there again?"
    
    vl gwynette_vl_prefix 13
    gw "Hey, I don’t love all of them more than you."
    
    vl ylva_vl_prefix 8
    yl "But there are some that you do?"
    
    vl gwynette_vl_prefix Whistle
    "Gwynette begins to whistle."
    
    vl vince_vl_prefix 9
    vin "Shame. And just when I was about to invite you out to the most expensive restaurant in Ferenicia."
    
    vl gwynette_vl_prefix 14
    gw "My five-star lunch, no!"
    
    "This isn’t over. They have a long, hard talk to have. But still…"
    
    vl alexis_vl_prefix 7
    a "It’s nice to see you two getting along."
    
    "Their eyes meet, and a blushing Vince looks away from Gwynette. Even Ylva appears at ease, watching the two of them."
    
    vl ylva_vl_prefix 9
    yl "Enjoy your surprise date, you two."
    
    vl alexis_vl_prefix 8
    a "I want to hear all about it."
    
    vl gwynette_vl_prefix 15
    gw "Oh, you’ll hear all about it alright."
    
    vl alexis_vl_prefix 9
    a "Excuse me?"
    
    vl ylva_vl_prefix 10
    yl "W-what?!"
    
    vl vince_vl_prefix 10
    vin "H-hey, don’t go putting ideas in their heads!"
    
    "He glares at us, face burning with embarrassment."
    
    vl vince_vl_prefix 11
    vin "She’s just getting a rise outta you two! Ignore her!"
    
    hide vince with dissolve
    hide gwynette with dissolve
    "He takes her hand and drags a giggling Gwynette out of the chapel. Looking over her shoulder, she waves at us. Ylva breaks the awkward silence that follows."
    
    vl ylva_vl_prefix 11
    yl "I’ll be going now."
    
    vl alexis_vl_prefix 10
    a "Right. Sounds good."
    
    hide ylva with dissolve
    "I’m the last one of our little group left in the chapel. For just a moment, I let myself appreciate the place. I might not care for the Church now, but places like this have a way of putting me at ease."
    stop music fadeout 3.0
    "For someone like Gwynette, I’m sure today is going to make places like this all the more precious. And I’m really happy for her."

    #jump to main club route exalt
    $ renpy.call(chosen_club + "_route_exalt", "Exalt", 22)
    #jump music_route_verabris

label music_route_verabris(month, date):
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Own/Month 8/Gwynette_Month8_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Gwynette/Month 7/" + player_voice_prefix + "_Gwynette_Month7_"

    call screen calendar(month, date, "Verabris", 22)
    scene bg mainstreet_noon with fade

    $ renpy.notify("Gwynette - \nLenday, Verabris 22nd, 1028 RD")
    
    play music hatchling1 fadein 1.0
    "I’m on my way back from catching a movie when I notice someone on the sidewalk ahead of me. It’s been a little while since I’ve seen them, too."
    
    vl alexis_vl_prefix 1
    a "Well, look who it is. Gwynette Ellis, is that you?"
    
    "She turns, and instead of smiling, she looks confused."
    
    show gwynette neutral at center with dissolve
    vl gwynette_vl_prefix 1
    gw "Did you have to pull out the full name? You made me worry I was in trouble."
    
    vl alexis_vl_prefix 2
    a "You are in trouble, young lady. You’ve just about ignored me the last two months."
    
    "In true \"honeymoon phase\" fashion, as soon as she and Vincent had made up, she disappeared. Outside of club meetings, I barely saw her."
    
    vl gwynette_vl_prefix NervousLaugh
    "She offers no defense, just a nervous laugh acknowledging her guilt."
    
    vl alexis_vl_prefix 3
    a "So, how’ve you been?"
    
    vl gwynette_vl_prefix 2
    gw "For the most part, pretty great. Just had a nasty cry, though…"
    stop music fadeout 2.0
    
    "My anxiety spikes. I’m ready to blame Vincent for messing up again, but her behavior so far must mean he’s innocent. What else would’ve done that to her, then?"
    
    play music hatchling22 fadein 1.0
    vl gwynette_vl_prefix 3
    gw "Remember that ferret from the pet store a few months back?"
    
    vl alexis_vl_prefix 4
    a "When you randomly hit me with the \"Do you think animals are reincarnated the same as men\" thing?"
    
    vl gwynette_vl_prefix 4
    gw "Yeah, that! Little guy went and got adopted."
    
    vl alexis_vl_prefix 5
    a "And that made you… cry?"
    
    vl gwynette_vl_prefix 5
    gw "How could it not? I thought I had a real connection with the little guy."
    vl gwynette_vl_prefix 6
    gw "Mark my words, when I have my own ferret-friendly place, I’m getting another one. No, {b}two{/b} of them!"
    
    vl alexis_vl_prefix 6
    a "What a noble goal."
    
    vl gwynette_vl_prefix 7
    gw "And I even have the perfect names for them."
    
    vl alexis_vl_prefix 7
    a "Oh, really? Hit me."
    
    vl gwynette_vl_prefix 8
    gw "Little Ferret and Big Ferret."
    
    #"[Beat.]"
    
    vl alexis_vl_prefix 8
    a "{b}That’s{/b} the best you could do?"
    
    vl gwynette_vl_prefix 9
    gw "What? I like them. And as their future owner, isn’t that what’s important?"
    
    vl alexis_vl_prefix 9
    a "I think there’s a lot more to it than that, but go off, I guess."
    stop music fadeout 1.0
    pause 0.5
    play music hatchling1 fadein 1.0

    vl alexis_vl_prefix 10
    a "Things with Vince going alright?"
    
    vl gwynette_vl_prefix 10
    gw "Just peachy. I’m getting him to go outside more and find other ways to appreciate his life and the world around him than {b}just{/b} art."
    vl gwynette_vl_prefix 11
    gw "I figure that would help him feel a bit more at home here, if he’s stuck."
    
    vl alexis_vl_prefix 11
    a "And make it less likely he’ll blow you off?"
    
    vl gwynette_vl_prefix 12
    gw "That, too. Actually, I was on my way to meet up with some friends."
    vl gwynette_vl_prefix 13
    gw "I haven’t been the best at that lately, so I’m trying to make up for it. We can definitely hang out soon, though."
    
    vl alexis_vl_prefix 12
    a "I’d like that. And make sure to answer my texts this time."
    
    vl gwynette_vl_prefix 14
    gw "I will, I will. See ya later, BB."
    hide gwynette with dissolve
    
    "And off she goes. Only when she’s gone do I realize how close that was. Graduation is next month. If not for this chance meeting, I’m not even sure if I’d be able to say a proper goodbye."
    stop music fadeout 3.0
    "We’re going to have a lot of lost time to make up for. Both what could’ve been since the new year, and what can’t be after I’m gone."

    call student_council_verabris("Verabris", 22) from _call_student_council_verabris
    #jump music_route_overa

label music_route_overa(month, date):
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Own/Epilogue/Gwynette_Epilogue_"
    $ alexis_vl_prefix = "audio/voices/Alexis/" + player_voice + "/Gwynette/Month 9/" + player_voice_prefix + "_Gwynette_Month9_"

    call screen calendar(month, date, "Overa", 21)
    scene bg music_hall_afternoon with fade

    $ renpy.notify("Gwynette - \nZynday, Overa 21st, 1028 RD")

    play music gwynetteTheme fadein 1.0
    "What has happened to the club room?"
    "Normally it’s people and instruments strewn about, consumed in their own little worlds, but today, there’s a sense of order to where everything is placed."
    "At the center of the room, directing people, is Gwynette."
    
    show gwynette neutral at center with dissolve
    vl gwynette_vl_prefix 1
    gw "BB, hey!"
    
    vl alexis_vl_prefix 1
    a "Hey. What’s going on here?"
    
    vl gwynette_vl_prefix 2
    gw "We’re putting on a concert. For you!"
    
    "I point at myself, wondering what I could’ve possibly done to deserve such an honor. Gwynette answers me by gesturing around the room."
    
    vl gwynette_vl_prefix 3
    gw "You and everyone else graduating at the end of the week. It’s our last chance to send you guys off, after all."
    
    vl alexis_vl_prefix 2
    a "You’re right about that…"
    
    vl gwynette_vl_prefix 4
    gw "So just kick back, relax, and enjoy the music, alright?"
    
    vl alexis_vl_prefix 3
    a "Yeah, sure."
    
    "I recognize some of the other seated fourth-years, so striking up conversations isn’t the most awkward thing in the world."
    "Gwynette remains conductor of the underclassmen, directing people to where they need to be and making sure all is in order for this final show for the soon-to-be graduates."
    "When all of the instruments are manned, Gwynette places a microphone stand before us all and adjusts its height."
    
    vl gwynette_vl_prefix 5
    gw "Alright, let’s not waste any time and get this party started. Sit back and enjoy the show, folks!"
    vl gwynette_vl_prefix 6
    gw "First off, since graduation is both a happy and a sad day, I wanted to start with a happy and a sad song. This one’s real important to me and a lot of us here."
    
    "A bit of an odd inaugural song, Gwynette and her band start off with the Nyrellan Hymn. Might not exactly fit the mood, but I get what she’s going for thematically."
    "From there, the songs get more upbeat. The members of the club play around with instrumentation and vocals. There’s little in the way of genre consistency, but no one seems to care."
    "Eventually, Gwynette’s back on the mic."
    
    vl gwynette_vl_prefix 7
    gw "Time for another favorite of mine. Bit of an older song, so if this is your first time hearing it, I hope you enjoy."
    
    "I’m reminded of all the way back in Dallinus, when we went to The Amity. She sings the same smooth, jazzy song as she did then. It sounds better to me now that she’s properly singing it and not just trying to match soft ambient music in a cafe."
    "There are a handful of disappointed groans when Gwynette’s song ends and she hands off the microphone,but it’s not long before they’re back on their feet, jamming out with the rest of us."
    "I don’t know how much time has passed, or if a teacher’s going to pop their head in and yell at us to clean up, when Gwynette takes the mic for a third time."
    
    vl gwynette_vl_prefix 8
    gw "Time for one last song, folks! This one’s actually one I wrote myself, so…"
    
    "The crowd breaks out into cheers. Gwynette goes red."
    
    vl gwynette_vl_prefix 9
    gw "You flatter me. But let’s hold onto the cheers until after I’ve actually sung the song. Be sure you like it before you go wild. Let’s do this thing!"
    
    "And the song that she performs is very uniquely \"Gwynette,\" in both the music itself and the lyrics. It sounds so much like her, and not just because she’s the one singing it."
    "The positivity and energy of the song fits the bubbly girl I’ve known the last year to a T."
    "The end of the song marks the end of the meeting, and the Music Club for the year. No one leaves, though."
    "People stand to give their friends well-deserved pats on the back for their hard work. Gwynette is swarmed by people, some of them asking for her autograph."
    "I wait my turn on the edge of the crowd. It takes a while, but it eventually disperses."
    
    vl gwynette_vl_prefix 10
    gw "If I make it big and one of those guys sells something I signed, I’m coming after them for a cut."
    
    vl alexis_vl_prefix 4
    a "{b}When{/b} you make it big, you mean."
    
    vl gwynette_vl_prefix 11
    gw "Please. Even my ego can only take so much inflating."
    
    vl alexis_vl_prefix 5
    a "But it’s deserved. You did a great job."
    
    "She practically glows at the praise."
    
    if eval(a.name)[0] == "Alexis":
        vl gwynette_vl_prefix 12A
        gw "Thank you, [a]."
    else:
        vl gwynette_vl_prefix 12B
        gw "Thank you, BB."
    
    "She takes my hand in both of hers."
    
    vl gwynette_vl_prefix 13
    gw "Thank you for being my friend this past year."
    
    vl alexis_vl_prefix 6
    a "I should be thanking you, honestly."
    
    vl gwynette_vl_prefix 14
    gw "Graduation definitely isn’t the end! Promise!"
    
    vl alexis_vl_prefix 7
    a "It’s not the end. I promise."
    
    "She pulls me into a quick hug. When it breaks, she looks at me less like a girl seeing off a friend and more a proud mother, or something."
    
    vl gwynette_vl_prefix 15
    gw "I’ll be seeing you around."
    
    vl alexis_vl_prefix 8
    a "Definitely."
    
    scene black with fade
    "Gwynette sees me off with one more hug. I leave her, still taking charge and helping to wrangle everyone together to clean up."
    "What a girl, that Gwynette. I’m not sure there’s a better friend I could’ve made this year."
    stop music fadeout 3.0
    "I’m not one for prayer, but as I make my way out of Magis Hall, on behalf of both of us, I offer up a little plea to the Divines to make sure we stay friends for a long time to come"

    #jump to main club route overa
    $ renpy.call(chosen_club + "_route_overa", "Overa", 21)