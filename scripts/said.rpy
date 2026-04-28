label enseki_route_jinus(month, date):
    $ said_vl_prefix = "audio/voices/Friends/Said/Said 1/Said_Month1_"

    call screen calendar(month, date, "Jinus", 23)
    scene bg dorm_common_noon with fade

    $ renpy.notify("Said - Day One\nNyday, Jinus 23rd, 1027 RD")

    "As I watch the leaves fall outside from my quarters, I’m compelled to get off my ass and fight off the emotional whirlpool known as “nostalgia”..."
    "…I’m sure that people can relate to that, right?"

    scene bg wright_gymnasium_afternoon with fade
    play music hatchling22 fadein 1.0

    "As I try to kill time, I’m quickly learning that MIA takes their extracurricular programs very seriously. The Enseki Club in particular, to me, looks like its own school nested within the academy."
    "And by how uniform the shouts are from the club’s class, the Enseki Club seems to be thriving inside the gym."
    "Pacing back and forth, sweat bleeding through their two-piece uniform and wearing a red and white belt, I recognize the person yelling commands at the white, yellow, green, blue, and brown belt students."
    "Despite this assumption, I wait until the guy wraps up with his coaching duties before approaching him while he’s sitting down, wiping himself off."

    a "Hey! You’re Said, right?"
    
    show said neutral enseki at center with dissolve
    vl said_vl_prefix 1
    sa "This is true. Who are you?"
    
    a "[a] Blakesley. Sue and I bumped into you and your friend not too long ago."
    
    vl said_vl_prefix 2
    sa "Hmm."
    
    "…I guess he’s more of a strong silent type?"
    "That’s not to say that he isn’t observant though."
    
    vl said_vl_prefix 3
    sa "Can I help you, Blakesley?"
    
    a "Me? Oh, no, I just wanted to say hi because I was… Wandering around the neighborhood, y’know?"
    
    vl said_vl_prefix 4
    sa "Ah. Yes. The school is very big, no?"
    
    "I mean, he isn’t wrong…"
    
    sa "..."
    
    a "..."
    
    sa "..."
    
    "…Gods damn, this guy’s really comfortable with silence. He’s just fucking looking at me like I’m supposed to press a button to move the conversation along."
    
    a "So… How long have you been attending MIA."
    
    vl said_vl_prefix 5
    sa "I’m transfer from Yvaratan. Second year student but I’m not been here long."
    vl said_vl_prefix 6
    sa "You like sport?"
    
    a "Do I like sports? I mean, they’re oka-"
    
    vl said_vl_prefix 7
    sa "You want train Enseki here?"
    
    "Through his nonchalant tone of voice, I can tell that the invitation is well-meaning. However, the wear and tear from many years of Enseki worn across his face and probably the rest of his body has nearly triggered my fight-or-flight response."
    "But then again, that funny feeling of coming off rude takes my tongue in a different direction."
    
    a "Sure…"
    
    "Said rises, tightens the belt around his waist, and motions me over to a padded portion of the gym floor. As for me, I gulp down whatever reluctance I have and try to mentally prep myself for an impending ass-whooping."
    
    stop music fadeout 2.0
    vl said_vl_prefix 8
    sa "Try to take me down, eh? Promise, I won’t kill you, let’s go. "
    play music hatchling15 fadein 1.0
    
    "At first, it almost feels like the starting position of an awkward waltz."
    "As we draw closer, I posture up using one of my hands, reaching for one of his shoulders."
    "Said, without blinking, does not perceive this as any sort of threat at all so I attempt to advance—but that’s when he grabs the wrist of my extended arm and wraps a hand behind my head."
    "I struggle to get out of his hold but his grip and strength is comically elite. I feel like I’d accidentally gotten my head stuck in a hole in the wall and Said just seems detached by the look in his eyes—like he’s watching himself toy with a child."
    "With each second, he continues to apply pressure with the hand wrapped behind the nape of my neck, lowering himself until I’ve flattened out. "
    "He then calmly climbs on to my back, pressing my back with stone-like knees, grabs on and rolls us over, and locks his arms around my windpipe. "
    stop music fadeout 1.0
    "I immediately tap, he acknowledges the submission with a grunt, gets up, and then offers a hand to me while I’m still coughing and catching my breath."
    play music hatchling22 fadein 1.0

    vl said_vl_prefix 9
    sa "Newbie, eh?"
    
    a "Buh… What?"
    
    vl said_vl_prefix 10
    sa "You never train before, yes?"
    
    "I shake my head no."
    
    vl said_vl_prefix 11
    sa "You should come train. Come next week. Is good for… Breathing."
    
    a "Good to know."
    
    "I take his hand, he brushes off the dust off my shoulders and makes sure that I’m standing straight."
    
    vl said_vl_prefix 12
    sa "You want to compete? I can teach you."
    
    a "Oh… No, I’m not much of a fighter really…"
    
    vl said_vl_prefix 13
    sa "Ah. Still. You should come train. Even if you’re not wanting to compete. You have to stay strong."
    
    a "I appreciate the concern."
    
    vl said_vl_prefix 14
    sa "You will be okay. Is not like how my father teach me. No animals allowed."
    
    a "…I’m sorry, what did you say?"
    
    vl said_vl_prefix 15
    sa "When I was small, my father made me train with cubs. You know, the bear cubs? And we spend weekend grappling."
    
    a "Um…"
    
    vl said_vl_prefix 16
    sa "Their name is Avdol."
    
    a "Your father’s name is Avdol?"
    
    vl said_vl_prefix 17
    sa "This is the bear’s name, bratha."
    
    "He studies my look of visible confusion carefully."
    
    vl said_vl_prefix 18
    sa "I know this is not normal for, ah… The MIA. But this is how my family raise me in Yvaratan."
    
    a "..."
    
    sa "..."
    
    a "..."
    
    vl said_vl_prefix 19
    sa "You okay?"
    
    a "I’ll be fine, thanks."
    
    vl said_vl_prefix 20
    sa "You think about training. It’s good, it’s good."
    
    "He exits the conversation soon after and, as I’m still tending to my sore spots, he’s gone and grabbed some cleaning supplies to wipe down the areas where the Enseki Club was training. "
    "I notice the quiet look on his face. It tells me that he’s lived a lot of life in such a brief time. "
    stop music fadeout 1.0
    scene black with fade
    "Now, I don’t know if I’m exactly sold on the idea of becoming some street fighter with the martial arts here but I am interested in learning more about what makes this guy tick."
    
    call enseki_route_dallinus("Jinus", 23) from _call_enseki_route_dallinus

label enseki_route_dallinus(month, date):
    $ said_vl_prefix = "audio/voices/Friends/Said/Said 2/Said_Month2_"

    call screen calendar(month, date, "Dallinus", 12)
    scene bg wright_gymnasium_afternoon with fade
    play music hatchling1 fadein 1.0
    
    $ renpy.notify("Said - Coffee Hour\nNyday, Dallinus 12th, 1027 RD")
    
    "Frequenting the Enseki Club ever since I got to MIA has been an eye-opening experience. I am becoming more in tune with the mechanics of aer and how all of that can be used to cover my ass if I ever need some self-defense. "
    "Even more interesting to me is Said’s method of working around it all. I have my suspicions as to why this might be but I’ve yet to ask him why he insists on toiling with the wrestling, striking, and submission holds."
    "Luckily, for me, we’ve gotten along well with one another in that brief time. Though I will admit that he’s quite the taskmaster whenever he’s commandeering the front of the class but it's mostly been pleasantries once everything’s wrapped up."
    "It’s been great. He even texted me and asked if I wanted to grab a coffee with him sometime. Granted, I really wish he’d get some sleep so my phone doesn’t go off before the weekend sun comes up but that’s minor in the grand scheme of life."

    call screen calendar("Dallinus", 12, "Dallinus", 14)
    scene bg mainstreet_noon with fade
    play music hatchling22 fadein 1.0

    $ renpy.notify("Said - Coffee Hour\nZaeday, Dallinus 14th, 1027 RD")
    
    "By the time I meet up with him, he’s already sitting down and catches me walking through the door. He motions me to come over and it looks like he’s already helped himself to a hot cup of tea."
    
    show said happy at center with dissolve
    vl said_vl_prefix 1
    sa "Blakesley! How are you, bratha? Please, come, come."
    
    "I don’t waste time and sit across from the table where he’s at. It doesn’t take long for a server to come by and take my order."
    
    show said neutral
    vl said_vl_prefix 2
    sa "You like coffee?"
    
    a "Huh? Oh, yeah, that’d be great."
    
    "Once the drink order gets sent in, there’s nothing but the awkward silence between me and Said (again)."
    
    a "So, uh… What’s up?"
    
    vl said_vl_prefix 3
    sa "Hmm?"
    
    a "…Did you want to talk about something in particular?"
    
    "Keeping in mind that neither of us share any classes together—that I knew of, at least—I’m really confused as to why he wanted to meet one on one."
    
    vl said_vl_prefix 4
    sa "Oh? I wanted to, ah… You know… The icebreaker?"
    
    a "Icebreaker? Seriously?"
    
    vl said_vl_prefix 5
    sa "Yes, bratha. You’re only student who talk to me in Enseki."
    
    a "Oh, I see!"
    
    vl said_vl_prefix 6
    sa "Yes, yes! I wanted to see if Amity was all hype or not, eh?"
    
    a "Yeah? What’d you get?"
    
    vl said_vl_prefix 7
    sa "Breakfast tea, straight breakfast tea. Simple because of the training."
    
    a "Training? Do you compete at all or do you just teach and practice?"
    
    stop music fadeout 1.0
    vl said_vl_prefix Sip
    "Said nods as he takes a sip from his cup before setting it down to answer my question."
    play music hatchling21 fadein 1.0
    
    vl said_vl_prefix 8
    sa "I compete since I was 12. From there, all my life."
    
    a "Huh. If you don’t mind me asking then, how come you never, uh…?"
    
    vl said_vl_prefix 9
    sa "Never use magic? I’m, ah… How do you say this? I’m “soulless”. Ever since I was small, no magic."
    
    "“Soulless”. I guess that means he has Aer Cortex Deficiency Disorder. But, based on what I’ve seen from him, he seems to be doing fine for himself despite the setback…"
    
    vl said_vl_prefix 10
    sa "But in Yvaratan, when you’re young, boy or girl, everyone fight. Doesn’t matter. And, my mother tells me this when I was kid, like, five, six, seven."
    vl said_vl_prefix 11
    sa "When I fight in street and come back, she never asked me “Why you fight?”, my mother always asked me “You lose or win?”"
    vl said_vl_prefix 12
    sa "Because she don’t like hurt people but she knows street is street—you have to show your heart, magic or no magic, when you go to the street because they don’t have referee, no rules."
    vl said_vl_prefix 13
    sa "You have to protect yourself all the time, bratha. She always say “Never come home if you lose”."
    
    a "…So, did you ever lose a fight? Is that why you’re at MIA?"
    
    vl said_vl_prefix 14
    sa "Oh, no, no, no… I don’t remember this with Enseki. I come to MIA in Ferenicia to learn, to get the red-black belt in Enseki, and opportunity to bring money back to Yvaratan."
    stop music fadeout 1.0
    
    a "What about that spar with Ylva about a month ago?"
    
    vl said_vl_prefix 15
    sa "This is just sparring, bratha. You spar to learn, to practice."
    vl said_vl_prefix 16
    sa "But that’s why I’m training Enseki even now."
    vl said_vl_prefix 17
    sa "It was my father’s last wish."
    
    a "I’m sorry, I didn-"
    
    vl said_vl_prefix 18
    sa "No, no, no, is okay, is okay, bratha."
    play music hatchling25_2 fadein 1.0
    vl said_vl_prefix 19
    sa "My father… He give me everything. Like tools to get here. Even when he get sick. "
    vl said_vl_prefix 20
    sa "He was like father figure to all children in Yvaratan. Because he keep them out of trouble, you know."
    vl said_vl_prefix 21
    sa " Everything I do is because of him."
    
    a "…So… You mentioned bringing money back to Yvaratan. Do you plan to go into the military or something?"
    
    vl said_vl_prefix 22
    sa "I will compete in True Strike Grand Prix. Fifteen million dominion for prize money."
    
    a "Don’t you have to fight a lot of people with a short turnaround time?"
    
    "One person every week once the tournament starts to be exact."
    
    vl said_vl_prefix 23
    sa "Yes, but this is no problem for me. I beat plenty of Enseki fighters from Gibroar and Acroton. Magiana fighters are like nothing."
    
    a "Well, you do seem to know what you’re doing…"
    
    vl said_vl_prefix 24
    sa "That’s why they give me red-white belt, bratha!"
    
    a "Lemme know when the tournament starts. I’d love to come by and support you during one of your matches."
    
    vl said_vl_prefix 25
    sa "This idea I like, I will let you know. Just don’t skip training, yeah?"
    stop music fadeout 1.0

    # jump to main club route dallinus
    $ renpy.call(chosen_club + "_route_dallinus", "Dallinus", 14)
    #jump enseki_route_dyalt

label enseki_route_dyalt(month, date):
    $ val_vl_prefix = "audio/voices/Supporting-Extra/Val/Said/Val_Said Route_Month 4_SkySantacruz - _"
    $ said_vl_prefix = "audio/voices/Friends/Said/Said 4/Said_Month4_"

    call screen calendar(month, date, "Dyalt", 5)
    scene bg wright_gymnasium_afternoon with fade
    play music hatchling15 fadein 1.0

    $ renpy.notify("Said - The Grappling… Is Zero\nNyday, Dyalt 5th, 1027 RD")

    "Even as the winter winds start blowing through MIA, I am dying of heat and thirst…"
    "It’s been several months since beginning the whole Enseki thing. Seeing a flatter stomach in the mirror and being able to breathe a lot better has been nice. I don’t necessarily feel like I’m a worldbeater but I never intended to become such a thing."
    "With the True Strike Grand Prix beginning in a few weeks, Said’s been locking in. He’s got no time to worry about the Student Council’s update for dress codes. "
    "Sometimes I can hear him striking trees at dawn, sometimes I see him just sitting on a patch of land meditating to himself…"
    "All of the tournament training and preparation has extended to how he runs the classroom. This particular week, he has the floor—and the floors are coated in wringed sweat. "
    "And, just for fun, the actual president of the club and the other black and red belts have conveniently missed the memo (most of them as far as I know at least)."
    "Thankfully, I survive a session of basic but intense pummeling drills. I begin to feel my peripherals blur and I immediately fall and crawl to where I think my bottle of water was. "
    "A few other students including the higher ranking yellow, orange, green, purple, brown, and black belts soon follow suit. The only one standing in their pool of sweat is Said. "
    "He has a look on his face—one of disappointment and annoyance—like someone cut him off in traffic."
    stop music fadeout 1.0
    
    show said neutral enseki at center with dissolve
    vl said_vl_prefix 1
    sa "Quickly: who thinks that they can fight professionally? Stand up so I can see."
    vl said_vl_prefix 2
    sa "Tell me. Who wants to fight?"
    
    "A few of the black belts rise and Said studies them. Everyone sitting down looks around to see who rises. Honestly, I’m thinking that Said’s about to ask them to spar with him all at once but I know that he’s no gym bully."
    
    vl said_vl_prefix 3
    sa "If you are doing Enseki for this long, you have to be ready, okay? Has anyone competed before?"
    
    "Nobody answers."
    
    vl said_vl_prefix 4
    sa "If you all want, come talk to me and the Enseki president when they are here. We can arrange fights if you want."
    vl said_vl_prefix 5
    sa "It won’t be like amateur, this is real competition. For this, you have to be ready."
    vl said_vl_prefix 6
    sa "You must be prepared or else you will have bad time. The most important thing is don’t skip training. It’s only one day out of the week."
    vl said_vl_prefix 7
    sa "You must train, you must compete. When you win, you will know how you will improve."
    
    "In the middle of all this, some poor bastard tightening their green belt quickly files into the drenched crowd with the stench of tardiness on them."
    
    vl said_vl_prefix 8
    sa "Not like Solan. One week of training and then disappear. Probably get lost in mountains."
    vl said_vl_prefix 9
    sa "Don’t sit down. Stand up when I’m speaking to you."
    
    "The student nervously rises, struggling to maintain eye contact with Said. Said never breaks his gaze focused on the student."
    
    vl said_vl_prefix 10
    sa "How many weeks did you skip training? More than half! You don’t think I don’t know this, eh?"
    
    "Said turns his gaze and, to my surprise, locks on to me."
    
    vl said_vl_prefix 11
    sa "You have to decide for yourself. Who are you? Are you a fighter or you working somewhere? Do you even make money? How can you support your family?"
    vl said_vl_prefix 12
    sa "You have everything here, eh? Decide! Otherwise, you waste time and body here."
    
    "As intense as his words are and I feel their stoic sting against parts of my ego, I also feel a sickening heat around the nape of my neck."
    "I begin to see smudgy images through my tired haze and the indoor heat continues to do me no favors…"
    "I grab my water bottle and expose myself from the room to die in a better climate outside in the hallway…"

    scene bg dorm_common_noon with fade

    "The sound of footsteps echo from one side of the hallway but I don’t know which one. The heels of uniform shoes click and grow louder in volume with each passing moment, slowing until there is a complete halt. "
    "I look up and recognize a somewhat familiar face."
    play music hatchling14 fadein 1.0
    
    vl val_vl_prefix 1
    v "Damn, Blakesley! You look like shit!"
    
    a "Good afternoon to you too, Val…"
    
    "Val looks down at me with a self-important grin, hands in their pockets, ignorant of my bubble of personal space. They look back at the doors to the gym in front of me before turning back to me."
    
    vl val_vl_prefix 2
    v "You know, if you wanted something more… Stimulating—y’know, for your brain—you should try reading instead."
    
    vl val_vl_prefix 3
    v "What are you doing playing battle mage anyhow?"
    
    a "Why do you care? You trying to expand your horizons this winter?"
    
    vl val_vl_prefix 4
    v "Perhaps. For more useful things."
    
    "Val turns to see the ruckus that’s happening through the gym door’s glass. By the muffled volume of Said’s lecture, people are still being chewed out."
    
    vl val_vl_prefix 5
    v "He’s a bit of a brute, isn’t he?"
    
    a "This is just another day for him. I’m just a humble tourist."
    
    vl val_vl_prefix 6
    v "Ech… Sounds so needlessly strenuous. But then again, I suppose he’s just living the only way he knows. Not much to do in that shithole bordertown so you can’t really blame him, right?"
    
    "I muster enough strength in my fatigued state to raise my head so I can look Val in the eyes when I judge them. Alas, I can’t think of anything to say… "
    "Thankfully, I don’t have to."
    stop music
    pause 1.0
    show said neutral at center with dissolve
    "Somehow, during this brief interaction, Said makes his way into the hallway and is currently standing behind Val."
    
    vl val_vl_prefix 7
    v "What? Speechless? I’ll take your silence as an admission of me being correct."
    
    "Val turns and finds today’s instructor with his arms crossed and an unbothered expression across his face."
    "Almost immediately, Val makes a swift exit with flushed cheeks. Said and I glance as he runs off as if he’s seen a bear in his bedroom."
    play music hatchling10 fadein 1.0
    
    vl said_vl_prefix 13
    sa "Blakesley. How are you? Already leaving?"
    
    a "Just catching my breath. You?"
    
    vl said_vl_prefix 14
    sa "My breathing is fine, bratha. Here."
    
    "Said reaches out and offers a hand to me. I grab hold and I’m reminded of the awesome strength he possesses as he pulls me up thanks to the discipline and dedication he has for his craft. "
    "Something about it is almost electric, taxing, and horrific all at once. "
    "But I’m reminded by the calmness written across his face that he’s looking out for me and everyone else learning from him at the end of the day."
    "I stumble as Said props me up with his broad shoulders."
    
    vl said_vl_prefix 15
    sa "You want doctor or Lychester House?"
    stop music fadeout 2.0

    # jump to main club route dyalt
    $ renpy.call(chosen_club + "_route_dyalt", "Dyalt", 5)
    #jump enseki_route_neralt

label enseki_route_neralt(month, date):
    $ said_vl_prefix = "audio/voices/Friends/Said/Said 5/Said_Month5_"

    call screen calendar(month, date, "Neralt", 21)
    scene bg wright_gymnasium_afternoon with fade
    play music hatchling15 fadein 1.0

    $ renpy.notify("Said - Poking the Lion\nIstday, Neralt 21st, 1027 RD")

    "Another month gone by, the same remains as it’s been."
    "Not long after almost passing away from Said’s intensity in the Enseki Club, Said has been testing his might in the True Strike Grand Prix."
    "I was surprised to hear the doors to House Lychester unlock in the middle of the night only a few hours after Said left for the event in the first place. "
    "He eventually told me the next morning that he’d “mauled” a “very nice guy” using the Stalwart Sword variation of Enseki (he called it “World Turtle Style”). All that said, beginning things off at 1-0 sounded like a pretty good start to me. "
    "And, based on the clip he showed me of the post-fight interview where he insisted on telling the interviewer in the ring that he’d be able to go again in 30 minutes, I feel even less worried about my friend and teacher."
    "With all of this said, even for the average layman, the “fight game” is always open to the dangers of sports celebrity—at least I think so (thank you, Brocky films)—corrupting many before and many to come."
    "In the case of Said, his success, even before True Strike, attracts jealousy and opportunists looking to go into business for themselves by any means necessary."
    "Much to everyone’s chagrin, as I enter the gym for another training session, I am met with bedlam."
    "Hard mats for grappling are torn and cut to shreds, sand is everywhere from punctured heavy bags, broken wooden dummies scattered across the floor. Dripping in red paint across the gym are two halves of an intimidation message…"
    "“Return lost animal to No Man’s Land”—the text is accompanied by a crude drawing of what I think is Said with a big emphasis on the mark on his chest."
    show said neutral at center with dissolve
    "Said stands alone, looking at the debris with a surprisingly unbothered look across his face…"
    
    a "What happened here?"
    
    vl said_vl_prefix 1
    sa "Break-in."
    
    a "Geez…"
    
    vl said_vl_prefix 2
    sa "You lucky, bratha. No training for today because of break-in. Come."
    stop music fadeout 1.0
    
    "Said walks over to a section of the gym where cleaning equipment is kept. He carries over a dusty broom and rolls a big vacuum over to me."
    
    vl said_vl_prefix 3
    sa "We can clean mess and then go eat, eh?"
    
    a "Shouldn’t we report this to someone?"
    
    vl said_vl_prefix 4
    sa "…Yes, if you like. We clean mess first."
    
    "That befuddled look across his face is only a bit concerning to me but thankfully, he doesn’t fight me on reporting the incident to IAH officials. If anything, he just seemed bored when we pulled up to their office."
    
    scene bg mainstreet_night with fade
    
    "Most of the time we spent cleaning up the chaos back at the gym was spent in relative silence—the powerful whirring of that ancient vacuum cleaner made it impossible for any sort of small talk to be had then (not that I think Said minded at least)."
    "Thankfully, we made up for lost time in that regard on our way to dinner."

    play music hatchling12 fadein 1.0
    show said neutral at center with dissolve
    
    a "So that’s why you were pouting at the office?"
    
    vl said_vl_prefix 5
    sa "Bratha, I don’t make face in the office. Because in Yvaratan, we don’t do this?"
    
    a "No police out there?"
    
    vl said_vl_prefix 6
    sa "No, no police. You have problem? You either talk or you send location."
    
    a "I see…"
    
    vl said_vl_prefix 7
    sa "See, Blakesley, I don’t know why people can do this, eh? People can talk shit and don’t get hurt in Magiana…"
    
    a "…I think it’s like a freedom of speech thing but yeah I think I see what you’re saying."
    
    vl said_vl_prefix 8
    sa "Because it’s better, eh?"
    
    a "Is it better? Yeah, I’d say so."
    
    vl said_vl_prefix 9
    sa "No, like, better for you. Not good for me but I stay calm for this."
    
    "As we arrive at our destination, the two of us hear a ruckus building up from behind us. It sounds like a mob."
    stop music fadeout 1.0
    
    "Unknown Asshole" "OY! Look, look, it’s the mud rat! It’s that hairy ape from across the world!"
    play music hatchling2 fadein 1.0
    "I turn around and see that six large individuals are hyping each other up for some reason. There’s a wildness to the biggest one of the group. He’s dressed in sweats from head to toe and it’s the same case for his cronies."
    
    "Unknown Asshole" "You’re dead just like your father, you know that, mud rat?! You’ll fit in with the other facedown corpses on that wartorn ghetto between Gibroar and Acroton, yeah?!"
    
    "The lead asshole is also carrying something with visible weight—an ax handle. Once Said and I make eye contact with the lot of them, they start to run up on us before the leader chucks the damn thing."
    
    with hpunch
    "Unknown Asshole" "I’m right here, you fucking slime! Right in front of you and you aren’t gonna do a damn thing, are ye?!"
    
    with hpunch
    "A shop window is obliterated and blood starts to trickle from the top of Said’s head but he remains unfazed. The pack of hyenas scurry away like delinquents pussying away after some ding-dong-ditch prank."
    
    "Unknown Asshole" "I hope your mother has a strong back! She’ll need it to bury you next to your useless pawn of a father and the rest of your inbred siblings!"
    
    a "Said! Are you alright?"
    
    stop music fadeout 1.0
    "I take a moment to take in the current situation in real time and all it does is parallel the chaos back at the gym unfortunately."
    "Said doesn’t say a thing and doesn’t do much other than brush off the broken glass off of his school uniform. "
    "I stop what I’m doing and try to help tend to his wound by asking whoever’s at the front of the store with the newly broken glass for some sort of towel or bandage which they do."
    
    a "Gods, talk to me Said, I need to know how you’re doing? Are you hurt? Do we need to get to the infirmary?"
    
    vl said_vl_prefix 10
    sa "Eh, they just wanna send me message. "
    
    a "What? What are you talking about?"
    
    vl said_vl_prefix 11
    sa "The talking chicken who threw ax handle. From True Strike."
    vl said_vl_prefix 12
    sa "Is okay. It is what it is, bratha."
    play music hatchling15 fadein 1.0
    
    "I make eye contact and notice him almost vibrate, a grin seems to form. But behind Said’s eyes, something sinister and feral struggles to settle down…"
    
    vl said_vl_prefix 13
    sa "He can only do that because of group. Of course, they do this before with many opponent, they get scared when they see lot of people gonna cause trouble…"
    vl said_vl_prefix 14
    sa "All they need is just send me location. I will come. I promise. But they never tell, only bark like small dog. Throwing bullshit like zoo animals."
    vl said_vl_prefix 15
    sa "Just come to me. If they wanna send me message, send location or wait for tournament. I'm gonna come. I no care for this, bratha. Wherever they are, doesn't matter—Gibroar, Yespela, Huntsdale, or Prospera."
    vl said_vl_prefix 16
    sa "All they need is to tell me where."
    stop music fadeout 1.0
    
    call student_council_exalt("Neralt", 21) from _call_student_council_exalt_1
    #jump enseki_route_exalt
    
label enseki_route_exalt(month, date):
    $ said_vl_prefix = "audio/voices/Friends/Said/Said 6/Said_Month6_"

    call screen calendar(month, date, "Exalt", 21)
    scene bg dorm_common_morning with fade
    play music hatchling15 fadein 1.0

    $ renpy.notify("Said - Any Time, Any Place, Without Security\nLenday, Exalt 21st, 1027 RD")

    "Everyone calls fighting the loneliest sport in the world—and through Said, I can see why."
    "Since the incident back in Huntsdale, it seems to me that it’s only done nothing but attract unwanted camera crews acting on behalf of the True Strike organization."
    "Said has been doing well for himself though. He continues to go on with his regular schedule of waking, praying, training, attending class, training again, and then somehow eating and sleeping sometime in between all of that. "
    "By the look of the production assistants and gaffers trying to get up in everyone’s business by sticking a microphone in front of their face and calling that an “interview”, none were too happy about Said living simply…"
    stop music fadeout 1.0
    
    scene bg mainstreet_afternoon with fade
    play music hatchling14 fadein 1.0
    show said neutral at character_pos2 with dissolve
    "A press conference is held three days before fight night to promote the event. News of the attack on Said and I has trended and circulated across Magiana news stations bringing only hype to the event. "
    "In order to avoid any further issues with Magianan authorities, the press conference has only brought in reporters and fighter affiliates (thanks for pulling strings to make me a part of your corner, Said). "
    "The balding True Strike promoter’s look of greed is apparent and seems to rub Said the wrong way but, as he’s told me in the lead-up to all of this, that’s his job."
    "Though, due to the absence of the other half of the main event, after being 30 minutes over the expected start time, the promoter officially introduces the event and stalls."

    stop music fadeout 1.0
    "Eventually, Said’s opponent arrives—striding to the fanfare of the audience and his team of 20 behind him."
    play music hatchling2 fadein 1.0

    "We also get the name of our attacker, recognizing the abrasive voice through the very enthusiastic (probably more relieved) promoter introducing him: “Prince” Finn Staten—a tall, lanky but well-toned, brute of a man who’s several years Said’s senior."
    "Finn sports tinted sunglasses, chews his gum emphatically, and waves to the crowd. His theatrical gait is led by his damn crotch which draws far too much attention to itself thanks to Finn wearing business formal clothing one size too small."
    "The two sit across from each other with the True Strike promoter standing in between them, yelling into a mic attached to a podium. He officially introduces the event now that the two fighters have arrived."
    "Said is dressed plainly, not even out of his MIA uniform. He is introduced to the general public as Said “The Lion of Yvaratan” Abdullaev. He simply nods and looks at the promoter as if to say “get on with it please”."
    "Meanwhile, I notice that Finn hasn’t even taken a seat yet. He’s just glaring at Said with a shit-eating grin, chewing away, saying something to him that eventually gets Said to stand up from his seat and face him."
    "The promoter, with a freakish smile across his face too, spreads his bony arms out wide to separate them but neither of them are too pressed to mush the weaker person out of the way."
    stop music fadeout 1.0
    
    promoter "Thank you all for coming! Who has the first question?"
    
    "At the front of stage are a string of sports journalists and personalities, some of which have lined up behind a designated microphone stand. A pink-suited fast-talker with literal rose-tinted glasses starts things off."
    
    "Punch Palooka" "Hey, y’all, how ya doin’? It’s Punch Palooka from Palooka Press, I’m glad to be here. "
    "Punch Palooka" "It seems like despite the success of the True Strike promotion and all of the revenue coming in, many fighters young and old are still raising the issue of appropriate payment. "
    "Punch Palooka" "What’s it going to take to get you to not only legitimize these warriors not just with the brand of the organization but with decent earnings and maybe some pay-per-view points? Get that going at the end of summer? Early fall? "
    "Punch Palooka" "A lot of the top names wanna see it and so do the people—and when I say “the people”, I mean Punch Palooka. What do you think?"
    
    "The balding promoter looks at Punch as the crowd gives a noticeable wave of affirming woos."
    
    promoter "Who the hell are you?! What the fuck just happened?"
    
    "The impressionable audience then laughs with the promoter."
    
    promoter "Not gonna happen, Palooka. Next question!"
    
    "A portly but more appropriately dressed reporter comes up to the mic stand and pipes up."
    
    "Reporter #1" "First question for Finn: of course, the talk of the town has been you throwing an ax handle at your opponent an-"
    
    promoter "Okay, security, get this clown out of here!"
    
    finn "It’s called promoting a fight, sonny. I am a student of war and I am slowly chipping away at the psyche of this bomb shelter baby! He got punked then and he’s scared now."
    
    vl said_vl_prefix 1
    sa "…Who said this, eh? You think I’m scared? I don’t feel nothing. Why would I be scared of chicken?"
    
    "It doesn’t take long for the two to start verbally going at each other."
    
    #TODO: Text box for characters talking at the same time
    vl said_vl_prefix 2
    call screen multiple_say(sa, "You really think I’m scared of you? I never feel nothing, bratha. You think you can win like this? Title can only go to tournament winner.", finn, "The only reason why anybody’s giving a shit about us is because of me. Don’t show lip to your senior. Try learning how to speak proper, yeah? You fuckin’ bridge troll.")
    
    "The promoter raises his hands up, ready to hold each fighter back, but his attention lingers just a bit more on Said as he’s trying to calm both of the hotheads. "
    "However, the precaution comes less from a place of concern and safety but to simply protect his bag. He’s but one of many opportunistic hypocrites in the fight business."
    
    finn "If you were there, you could see in that moment when the glass broke behind him, he shit himself like a lost toddler in an open field. "
    finn "So come this weekend, I will give him two for flinching when I rain a storm he won’t be able to weather."
    
    "Despite his jabbering jaw, Finn himself was no slouch in Enseki. "
    "He’d accrued experience and made a name for himself as a sort of sports personality prior to entering the Grand Prix with a 10-2 record under the organization."
    "So, to be meeting with Said at this point in the tournament meant that he too added three additional wins under his belt."
    
    finn "The fanboy has a glass jaw—and he’s been opening it for far too long, so if you want to see more glass shatter, tune in this weekend and enjoy the show!"
    
    "The promoter lets out a nervous laugh (probably anxious from a legal standpoint due to the broken glass remark). Everything is dead silent until Said speaks."
    
    vl said_vl_prefix 3
    sa "I don’t know what you are talking about. Are you drinking?"
    
    finn "Wouldn’t you like to know, you bloody crotch-sniffer?"
    
    vl said_vl_prefix 4
    call screen multiple_say(sa, "Why do you say this, eh? Be like professional. You’re not going to do nothing. I’m going to maul you, bratha. I’m going to drown you, you will feel this. I promise you.", finn, "Ooh, I’m so scared! The ring hugger, the dirt kisser, is going to majority decision me to death. REMEMBER THAT I PULLED UP AND YOU DID NOTHING. YOU DID FUCKING NOTHING. You and your nobody acquaintance were frozen in fear. You fucking mushroom.", True)
    
    "A lull in the commotion set invites a reporter to try and redirect things."
    
    "Reporter #2" "Finn, fill in the blank here: “This weekend, Finn Staten will blank Said when you meet each other.”"
    
    finn "STOMP ON HIS HEAD WHILE HE’S UNCONSCIOUS!"
    
    #"[Beat.]"
    
    "…Who the fuck are these guys? They’re just clowns under an odd big-top it seems."
    "This annoying cycle of soft-balling questions and then letting two people bark at each other goes on for close to half an hour until the promoter disconnects the mic and finally has the two face off before they officially meet each other in battle."
    "The entire time, I see Finn try to press himself into Said’s personal bubble. But like an awkward but good-willed uncle babysitting their two estranged nephews, the True Strike Promoter uses his hands as guard rails."
    "Finn just chews away, talking at Said, and Said simply nods and smiles at his adversary’s empty threats. "
    "Once the photographers get their shots in, the two face the crowd again but not until the promoter shoves a mic in each of their faces for closing remarks."
    
    promoter "Finn, before we leave, I have to ask for the people: how will this change the course of your career?"
    
    finn "This is just another day in the office for me. It’s just business and business is gonna be booming for the both of us, I promise you that. Your promotion will go under if that primitive knee-scraper squeaks a decision over me."
    finn "But even then, even then, hey, I don’t count decision losses. If he’s a real fighter or even half the man his grunt father was, he’ll try to actually fight me then."
    
    promoter "Very strong words from Prince Finn! Good luck to you, young man. See you at the weigh-ins."
    
    "The promoter turns to Said once Finn’s left the stage."
    
    promoter "Said. What does this fight in the Grand Prix finals mean to you against Finn Staten?"
    
    vl said_vl_prefix 5
    sa "First I want to thank my father and the spirits above me, they give me everything. They give me everything. I know the people don’t like this because it sounds, eh, corny."
    vl said_vl_prefix 6
    sa "But soon, I’m going to smash your boy’s face. In three days, gods willing, I’m going to smash your boy! Because this is easiest fight in tournament. "
    vl said_vl_prefix 7
    sa "Thank you to everyone who going to watch, without you, none of this is possible. Thank you, everybody."
    
    "The promoter’s eyes indicate that he might have shat himself. But, being the professional that he is, he wraps things up and finally ends the event."
    "Now, with media just about done, Said’s biggest challenge lies before him: making weight."
    
    scene bg wright_gymnasium_night with fade
    play music hatchling15 fadein 1.0
    
    "Said’s corner consists of a fraction of whatever mob Finn has. The president of the Enseki Club at MIA plus their closest confidant and I have come to the aid of Said during this tumultuous two-day period."
    "The goal here is to drain out as much water from Said without killing him. If we do that for the next 48 hours, it’ll be just enough to have him qualify for fight night."
    "Everyone has been living in the gym to monitor Said. The fighter in question wears an uncomfortable compression suit made for the exact purpose of drawing out moisture from his body. "
    "The thermostat reads a temperature that would be fit for a tropical jungle. "
    "And Said, in the aforementioned suit, has been cycling, jogging, or brooding—all of that, without food or water, since we got back to MIA from the press conference."
    "I see him but I’m afraid to talk to him. His entire face is sunken and almost looks like a walking skeleton compared to his usual look."
    "Both of us know that this pain is temporary but only one of us seems comfortable enough with the experience."
    "All I can do now is watch and maybe pray that Said doesn’t kill himself as he makes his final push before actual competition…"

    if chosen_club == "anime" or chosen_club == "archery" or chosen_club == "home_ec":
        $ renpy.call(chosen_club + "_route_exalt", "Exalt", 21)

    else:
        call enseki_route_exalt2("Exalt", 21) from _call_enseki_route_exalt2_3
    
label enseki_route_exalt2(month, date):
    $ said_vl_prefix = "audio/voices/Friends/Said/Said 6/Said_Month6_"

    call screen calendar(month, date, "Exalt", 24)

    stop music fadeout 1.0
    scene mainstreet_night with fade
    play music hatchling2 fadein 1.0

    $ renpy.notify("Said - Any Time, Any Place, Without Security\nUctday, Exalt 24th, 1027 RD RD")

    "Ring Announcer" "…AAAAAAAAAND NOW!!! THE MAIN EVENT OF THE EVENING!!!"
    
    "The heat of the lights, the roar of the crowd, the quiet in the locker rooms. A hard cut to the climax of Said’s story."

    show said neutral enseki at character_pos2 with dissolve
    "Making weight was ultimately a success. No need for towel pulling and stripping butt-naked unlike Finn just to win the scale over. It was nice to finally get human essentials into Said. By the time we’re at the venue, he almost seems normal again."
    "I stand behind the caged off ring where Said and Finn face opposite of one another. Said turns to me as the ring announcer belts Said and Finn’s names into his microphone."
    
    vl said_vl_prefix 8
    sa "How you feel right now, Blakesley?!"
    
    a "I’d rather not talk about it honestly!"
    
    vl said_vl_prefix 9
    sa "Don’t worry, bratha! We’ll go get tea afterwards!"
    
    "The referee of the event waves the two to come to the center before the starting bell rings."
    
    show said neutral enseki at character_pos3 with move
    "Referee" "Gentlemen. We’ve been over the rules. Protect yourselves at all times. Follow my instructions. Keep this fight clean. Touch gloves if you wish to. Any questions before we begin?"
    
    finn "Is the lion scared?"
    
    "Referee" "No questions like that."
    
    "The referee sends them back to their corners but Said replies before the bell rings."
    
    show said neutral enseki at character_pos2 with move
    vl said_vl_prefix 10
    sa "Just remember: there is nobody between us now."
    
    stop music fadeout 3.0
    "I feel a small collective moment of brevity before that bell is rung. But before I know it, the first of five rounds has begun."

    play music hatchling2 fadein 1.0
    show said neutral enseki at character_pos3 with move
    "Said, in his neutral stance, gallops to the center of the ring to get in range of Finn. Finn, on the other hand, attempts to aura farm. "
    "He approaches Said with his hands down, staring him down with a cocky but sinister look on his face before landing a piercing lead hand jab to Said’s forehead. It almost looks like a piston from where I’m standing but Said remains unfazed."
    "Said throws a blind jab which is evaded and countered by an air punch from Finn, this time stunning Said just for a moment. Before Finn can find their rhythm from an outer distance, Said suddenly bursts and shoots for Finn’s waist."
    "Finn snakes his way out of Said’s hold but falls off-balance as Said grabs hold of one of his ankles. After having had the chance to spar Said, I know how much of an anchor he can be when he’s only using 50\% of his strength to get a hold on you."
    "As they wrestle, there’s an odd scramble which sees Finn twirling around, hopping on one foot, as he tries to mush Said’s head off of his leg with Blustering Blade techniques."
    "However, once Said is able to stabilize his target, he plows him into one of the sides of the cage and sits Finn down on the ground."
    "Frustrated and eager to get back to his feet, Finn starts to smack anything that looks like free real estate to him—this is to say that he starts elbowing Said in the back of the head (which is illegal)."
    "The referee, who is middle-aged and visibly slow (both physically and, honestly, mentally), simply stares at Finn as he lands about four illegal shots onto my friend."
    
    "Referee" "Don’t strike the back of the head!"
    
    "It’s about fucking time you said something, molass-hat…"
    "Finn finally ceases after the verbal warning and, for the rest of the round, the crowd hails in a storm of boos due to Said keeping the Enseki match on the ground with him smothering Finn with his weight on top."
    "The bell rings and the round ends but not before Said throws a ground-and-pound punch that lands just as the bell rings."
    stop music fadeout 1.0
    show said neutral enseki at character_pos2 with move
    "The two rise and make their way to their corners. Finn smiles and says something to Said on his way back to the corner that makes him look over his shoulder."
    
    finn "Still warming up, yeah? How do I smell down there? That’s what a real fighter smells like!"
    
    "I rush to bring Said a bottle of water. Said stands and listens to what the Enseki president has to say to him, Finn sits on a wooden stool while getting rubbed down with bags of ice."
    "The bell rings again. Here comes round two."

    show said neutral enseki at character_pos3 with move
    "The opening seconds almost mirror the first moments of the previous round, only this time, Finn throws and misses a front kick aimed at Said’s abdomen. "
    "Shoulders down and no respect from Finn, and an attentive Said looking for another moment to employ his grappling-heavy style of Enseki."
    "Finn continues to prod, poke, and jab from the outside, forcing Said to move laterally with him closest to the walls of the fighting platform. Finn throws a flashy set of kicks but makes no contact onto Said."
    "Then, Said acts quick to deploy a trap. He feints at waist level which Finn reacts to—Finn leans ever so slightly to catch and sprawl another takedown attempt. "
    "However, he’s quickly met with a sickening pop of leather as Said lands a flush overhand blow to his chin which sends him stumbling backwards."
    with hpunch
    "Not wanting to prolong the battle, Said sprints forward and charges with a wild knee strike—which he misses, glancing off of one of Finn’s shoulders before Finn ties him up and pushes Said against the nearest cage wall. "
    "Said quickly finds his footing, turns them both around so Finn is fighting further away from the center, and relaxes his pace to continue his onslaught."
    "The two trade blows—Finn throwing out of instinct, Said trying to close the distance or possibly end the fight. "
    "Surprisingly, Finn makes more contact but Said seems to be dealing more damage with the few round punches he manages to throw based on the bruising around the ribcage of Finn and the swelling forming on one of his eyebrows."
    "Soon, Said charges like a bull yet again, imposing his will and pressing his shoulder against the damaged core of Finn. "
    "Unlike before though, I can hear Said grunt as if he’s deadlifting and carries Finn over one of his shoulders before walking over to our corner and slamming him onto the ground. "
    "That sequence pauses once Said ties up Finn’s lower body with his own legs, slowly climbing on top to a more dominant top position with more ground-and-pound blows. With three long minutes remaining in the round, I can hear Said’s voice…"
    
    vl said_vl_prefix 11
    sa "Eh? Talk now."
    
    "Said holds Finn down, almost like how a schoolyard bully would, and crashes an elbow across his opponent’s cheek."
    
    with hpunch
    vl said_vl_prefix 12
    sa "What happened?! Talk! Let’s talk now! Come on!"
    
    with hpunch
    "Another wild hook lands for Said."
    
    with vpunch
    vl said_vl_prefix 13
    sa "Talk now, eh!"
    
    "I’m met with what 100\% of Said’s capabilities look like and, for a moment, I almost pity Finn."
    "The rest of the round was spent on the ground with Said comfortably pummelling Finn in an attempt to live up to his personal promise of rearranging his face."
    "The second round bell rings. The two rise, Said shoots up and gets in Finn’s face before the referee gets in between them."
    
    vl said_vl_prefix 14
    sa "I’m here now! Let’s talk!"
    
    finn "…It’s only business, mate…"
    
    play music hatchling15 fadein 1.0
    show said neutral enseki at character_pos1 with move
    "Said stops and rests his hands at the top of the cage wall once he gets back to our corner. The president of the Enseki Club immediately goes to coaching mode with Said’s back facing Finn. He leans on the side of the cage, trying to catch his breath."
    "I go to look over Finn and I see his cornermen press swelling steels across his newly formed welts and bottle feed him his water."
    
    a "Said! Look!"
    
    "Said turns and looks at me, panting heavily."
    
    a "He’s dying on his stool, Said! Look!"
    
    "His eyes widen almost with some sort of anger, gently pushing the Enseki president away so he can get a straight look at his opponent."
    "Almost naturally, Said starts walking to the center of the ring before the referee stops him and tells him to return to his corner."
    
    vl said_vl_prefix 15
    sa "Say something, eh? Fucking bitch…"
    
    "The time for rest ends yet again. To the third round we go."

    show said neutral enseki at character_pos3 with move
    "The ref holds both hands out at each of the combatants. Each of the combatants are still breathing hard—then the bell rings and they’re off to best each other again."
    "Finn immediately tries to hone in on the reach advantage he has over the stockier fighter, trying to repeat the beginning successes of the first two rounds. "
    "Said, however, as if possessed by a spirit, casually marches forward despite eating pinging knuckles to the forehead, compressed air blasts to the gut, and push kicks to the legs. "

    show said with hpunch
    "Finn throws them so quickly that they almost seem to create smoke trails. Said manages to mix in his own offense as well, primarily to the body and to the head. "
    "A particular sequence sees Said weaving out of harm's way from a rising strike from Finn in order to land an audible roundhouse slap to one of Finn’s ears. I turn to ask the Enseki president if that was indeed a slap and he confirms."
    "Said’s wrathful tenacity quickly makes the momentum of round three a constantly swinging pendulum. "
    "Finn chins Said with clean punches and kicks, but Said is still standing and pounces to return a few of his own combos and trips."
    "Finn takes a hard impact after the first few wrestling trips but is still able to get to his feet quickly albeit practically running away from Said to do so. "
    "I assume that the judges’ eyes are scoring the round favorably for Said as a result of these impacts but they can still be easily swayed by Finn’s crowd-pleasing style of Enseki. "
    "Then, digging deep, Said drops to waist level again to shoot for a takedown and succeeds. And in that moment, I can hear Said talk to Finn again."
    stop music fadeout 1.0
    
    vl said_vl_prefix 16
    sa "I told you. I’m gonna drown you."
    
    "Finn squirms and tries to wriggle out of Said’s legs which have constricted and bound the taller man’s lower limbs, making his escape attempts futile. His stamina drops drastically in real time and his morale follows."
    "At some point with half of the round left to go, Finn manages to roll onto his side and, for a moment, it looks like he’s about to finally get back up to his feet but instead gets jumped again by Said."
    "Said quickly takes his back, uses one of his knees to flatten him out until he can wrap his burly arms around the neck of Finn and lock them in. "
    "Finn, panicking but still trying to fight back, tucks his chin down in an attempt to reduce the likelihood of being put to sleep by Said. Unfortunately, this does nothing for him."
    "Said hugs and squeezes his arms tight, no gradual increase, just complete intensity with intent to pop his head open or cave his jaw in with torque and force."
    "Then I see Finn’s hand rise and swat something on his shoulder. Finn raises his hand again and begins to tap. The referee yells and has to forcibly unclasp Said’s hands loose."
    "Finn immediately coughs and gasps for air as he falls over before sitting up against the cage. Said is sent in a rage."
    
    vl said_vl_prefix 17
    sa "I killed you! I killed you!"
    
    "Said hawks phlegm at his loudmouthed adversary. Weeks of harassment, instigation, and insults far beyond the line of decency finally reach their boiling point here."

    show said neutral enseki at character_pos2 with move
    "My eyes widen, unsure of what to do. The referee pushes Said away and Said starts barking at one of Finn’s cornermen who, in the corner of my eye, is egging him on to do something."
    "Said pulls out his mouthguard and chucks the bloody thing at the cornerman."
    
    vl said_vl_prefix 18
    sa "I kill all of you!"
    
    "Finn's Cornerman" "You’re easy work for me, pussy! I fucking dare you."
    
    hide said with dissolve
    "Said then proceeds to hop the cage fence and divebomb himself right into Finn’s cornermen, immediately throwing hands at the bold one among the bunch—then the rest of Finn’s wolf pack. "
    "Event staff and security clumsily stumble and rush over to break everything up."
    "The Enseki president makes a beeline for Said and tries to pull him away but not before instructing me and Said’s cutman to get in the ring as chaos builds outside of it. "
    "We open the cage door and come in alongside more event staff. The crowd roars simply just by bearing witness to this fiasco in real time."
    "Then I notice some familiar faces jumping the fence to get into the ring—the same assholes who were there when the ax handle was thrown."
    "One of them bum rushes the cutman and the other sucker punches me. "
    with hpunch
    "I immediately feel red pouring out of my nose but I immediately push him off of me. Before I can return fire, some rotund event staff member peels me away from the conflict. "
    "Thankfully, as the large person hauls me to a different part of the ring, another staff member has peeled the other asshole off of the cutman. Thank the gods for that."
    "This is… Crazy. This isn’t professionalism by any means but this is still somehow the nature of the business. No class, no glory—only bread and circus riles up the audience."
    "It takes a while but eventually both fighters are back in the ring, cronies from opposing camps are back in their corners, and it’s finally time for the official announcement of the bout—but not quite."
    "The fight promoter of True Strike, alongside an army of guards, has gotten into the ring and carefully makes sure that his pet project Finn is okay and unharmed. Meanwhile, Said is still heated."
    
    show said neutral enseki at center with hpunch
    vl said_vl_prefix 19
    sa "No way! This is number one bullshit! Where is my belt?! Where is my money?! I am the champion! Where is promoter, eh?"
    
    "Like clockwork, the high-and-mighty promoter of True Strike arrives with a stern look on his face and no tournament belt in sight."
    
    vl said_vl_prefix 20
    sa "Hey! Where is my belt? I earned this, bratha! Give me my belt!"
    
    promoter "Just shush for a moment, okay? I don’t have your belt!"
    
    vl said_vl_prefix 21
    sa "Why?!"
    
    promoter "I don’t have it with me right now because—and this is what I believe—if I put that belt on you right now, people are gonna start throwing shit into the ring!"
    
    vl said_vl_prefix 22
    sa "Bratha, I’m ready for this!"
    
    a "Said!"
    
    vl said_vl_prefix 23
    sa "What?"
    
    a "You have to think straight here. People could get hurt."
    
    "Said takes one last look at Finn—and he’s finally quiet. He looks over to me and I see the beast inside of him disappear. A look of guilt starts to form and he uses one of his sweat towels to cover his face up."

    hide said with dissolve
    "Much to the chagrin of Said, we all comply with the promoter’s proposition and are escorted back to the locker rooms by security. The crowd cheers at the sight. "
    "The promoter won’t be handing Said the grand prix trophy. The promoter will be withholding half of his fight purse to make up for property damages and possible legal settlements for any of the front row audience members looking to complain."
    "The well-connected promoter also mentioned that if he didn’t take that deal, Said would be banned from practicing, teaching, and/or competing in Enseki on the continent for life (a favor from the Magianan sports commission would do just that)."
    "And so our team watches silently from the locker room at the televised coverage of the event."
    
    scene black with fade

    "Ring Announcer" "Ladies and gentlemen, the referee has called a stop to this contest in the third round! "
    "Ring Announcer" "Declaring the winner by submission via a neck crank and the NEW TRUE STRIKE GRAND PRIX WINNER: SAID “THE LION OF YVARATAN” ABDULLAEV!"

    #jump to main club route exalt
    if chosen_club == "disciplinary" or chosen_club == "literature" or chosen_club == "no_clubs":
        $ renpy.call(chosen_club + "_route_exalt", "Exalt", 24)
    else:
        call phillip_elvera("Exalt", 24) from _call_phillip_elvera_6
    #jump enseki_route_verabris

label enseki_route_verabris(month, date):
    $ said_vl_prefix = "audio/voices/Friends/Said/Said 8/Said_Month8_"

    call screen calendar(month, date, "Verabris", 16)
    scene bg dorm_common_morning with fade

    $ renpy.notify("Said - The Loneliest Sport in the World\nZaeday, Verabris 16th, 1028 RD")

    "The morning after the grand prix finals is quiet. After sleeping in for a few, I wake to an empty floor and a bit of soreness from my nose thanks to last night. Maybe everyone’s gone off into town before the week begins…"
    "However, when I look outside my window, I stumble upon a quiet sight…"

    scene bg maincastle_noon with fade

    "I put on my slippers and a robe and make my way outside, carefully sidling up on Said."
    "Said is on a flattened mat of some sort, kneeling on a clean patch of grass, facing towards the sun. "
    "He speaks in a tongue I can’t understand but, based on the tranquil environment and his solemn tone, I know that the words coming out of him are of reverence and worship—prayers."
    "I kneel behind him and patiently wait for him to finish his prayer. When he finally rises to his bare but cleaned feet, he notices that I’m there."
    
    show said neutral at center with dissolve
    vl said_vl_prefix 1
    sa "Blakesley! What are you doing here, eh?"
    
    a "Sorry, I didn’t mean to intrude… I just wanted to check up on you, that’s all."
    
    "A rare look of sorrow overtakes him. He closes his eyes tight before opening them up to me."
    
    vl said_vl_prefix 2
    sa "Come. We’ll talk inside."
    
    scene bg dorm_common_morning with fade

    "Said prepares and pours out two cups of breakfast tea for ourselves and we sit opposite in the middle of Lychester’s common room."
    
    show said neutral at center with dissolve
    vl said_vl_prefix 3
    sa "…You know, my father… This was always his dream for me…"
    
    a "Yeah, the tournament…"
    
    vl said_vl_prefix 4
    sa "Not True Strike. For better life. Better life for me and my mother. That’s why he train me so hard before he passed."
    vl said_vl_prefix 5
    sa "I miss him. In Yvaratan, in our culture, it’s very hard to say this. Because when you grow up, it’s like… Plenty of people will say “Oh, love makes your heart weak”."
    vl said_vl_prefix 6
    sa "You not agree with this, Blakesley?"
    
    a "I don’t actually. I don’t. Why else would you go this far to fulfill his dream then, whatever that may be?"
    
    "Said looks down his teacup and smiles for just a moment."
    play music hatchling21 fadein 1.0
    
    vl said_vl_prefix 7
    sa "He was my only real friend there. You remind me of him, Blakesley."
    vl said_vl_prefix 8
    sa "For last night, I feel embarrassed. Because… This is not who I am. I know who I am. "
    vl said_vl_prefix 9
    sa "But in Yvaratan, you cannot talk about someone country, you cannot talk about someone family. I think even here you cannot talk about that without getting hurt."
    
    a "Said, I completely understand. I definitely wouldn’t condone stuff like that in the future but I understand. Remember, I was caught up in the crossfire."
    
    vl said_vl_prefix 10
    sa "I get too emotional and I hurt people. Audience. My friends. I’m sorry for this, Blakesley."
    
    a "It’s fine."
    
    vl said_vl_prefix 11
    sa "…This was not what my father wanted. I put dirt on his name so, this morning, I turn towards the Cornerstone—my father teach me when I was small—and pray. I pray for forgiveness, that’s all I want now."
    
    a "…What’ll you do now that everything’s done?"
    
    "Said downs the rest of his tea and looks down at his cup before looking at me."
    
    vl said_vl_prefix 12
    sa "I don’t know… I don’t know. Maybe this evening, I will pray again for guidance."
    
    stop music fadeout 1.0
    vl said_vl_prefix 13
    sa "But right now, I only ask you for forgiveness."

    call student_council_verabris("Verabris", 16) from _call_student_council_verabris_1
    #jump enseki_route_overa

label enseki_route_overa(month, date):
    $ said_vl_prefix = "audio/voices/Friends/Said/Said Epilogue/Said_Epilogue_"

    call screen calendar(month, date, "Overa", 20)
    scene bg maincastle with fade
    play music hatchling25_2 fadein 1.0

    $ renpy.notify("Said - Epilogue\nZaeday, Overa 20th, 1028 RD")

    "Over the course of one school year, despite never feeling it in the present, I think I’ve grown a bit—mostly thanks to Said."
    "Following the tournament, he went on with life as it was before all the ugliness got involved."
    "We didn’t talk as much towards the end of the school year as I mentally prepared myself to get ready for the “real world” and he spent most of his time in offices trying to sort out continental visas and other documents."
    "While I don’t know all the details, it seems that Said’s got his new plan of attack with returning to Yvaratan for holiday. For him, there's nothing going into Said’s plan other than to do it. "
    "Now, despite becoming a villain and quickly immortalized as a sort of antihero (casual fight fans are finicky with their emotions towards fighters like that), he wants nothing to do with any of the drama. "
    "Despite losing a significant amount of life-changing money, he still plans to return home to figure out what he can actually do with the remainder of his winnings. "
    "And despite all that we’ve been through together as friends, he still treats me a bit like a stranger and… "
    stop music fadeout 1.0
    "I don’t know… I just hope he knows that someone was looking out for him throughout all of the strife and throughout the drama. Even if I wasn’t able to do much, I only hope that he knows that I’ve had his back since day one."
    "In this moment of celebration and reflection, I try to keep my head on the lighter side. "
    "Thankfully, it feels just a bit lighter when I see a familiar face come up to me from behind (which honestly feels scary because I’m met with a familiar power holding me in the air for a moment)."
    play music hatchling17 fadein 1.0
    
    show said happy at center with dissolve
    vl said_vl_prefix 1
    sa "Blakesley!"
    
    a "Said… I didn’t know… You’d be coming…"
    
    "Said puts me down and reaches for his phone to show me something."
    
    vl said_vl_prefix 2
    sa "You sent text message. I don’t know when but you sent text, bratha."
    
    a "Right! I, uh, wasn’t expecting you to show up honestly."
    
    vl said_vl_prefix 3
    sa "Eh? How come?"
    
    a "You know after the tournament and-"
    
    vl said_vl_prefix 4
    sa "None of that matters, bratha. It’s past."
    
    a "No, I get that. It just seemed like you wanted to be left alone…"
    
    vl said_vl_prefix 5
    sa "Okay… How you know?"
    
    a "You were distant. I just wanted to give you space, y’know?"
    
    vl said_vl_prefix 6
    sa "I was working, bratha. And I don’t wanna talk about personal problem like that. I tell you them already. And I don’t have any personal problem after True Strike."
    
    "I look in his eyes to try and find the truth behind the words…"
    
    a "You’re sure about that?"
    
    vl said_vl_prefix 7
    sa "Yes, I am sure about this, bratha."
    
    a "…Okay. Well, what do you plan on doing once school’s out?"
    
    vl said_vl_prefix 8
    sa "Maybe I go see my mother and father. Tell them what happen."
    
    a "What are you gonna do with the money?"
    
    vl said_vl_prefix 9
    sa "I will see if I can use to fix my father’s gym. Might not be enough, but maybe I skip repaint."
    
    "I give him a smile and he returns in kind."
    
    a "Best of luck then, Said. You’ve taught me a lot."
    
    vl said_vl_prefix 10
    sa "Bratha, don’t stop. Keep training, keep growing, get stronger for your family."
    
    a "I’ll do that."
    
    "Probably more in a metaphorical or philosophical sense but I suppose a daily walk wouldn’t hurt in the long run."
    
    a "Enjoy your break and get home safe!"
    
    vl said_vl_prefix 11
    sa "May the spirits will it! Be safe, bratha."
    stop music fadeout 1.0

    #jump to main club route overa
    $ renpy.call(chosen_club + "_route_overa", "Overa", 20)