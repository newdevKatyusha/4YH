#notes 
#in lit club exalt - choice depending on whether name alexis chosen or not 
#fix once coded that in the beginning 
#in no club elvera or verabis branch 

define a = Character(
    "[temp_name]",
    color="#343668",
)

define p = Character("Prince Phillip", color="#4caf50")
define s = Character("Sue", color="#7b1fa2")
define r = Character("Reina", color="#f57f17")
define l = Character("Lucas", color="#ad1457")
define k = Character("Killian", color="#e65100")
define n = Character("Naomi", color="#00838f")
define e = Character("Elio", color="#c62828")
define gw = Character("Gwynette")
define sa = Character("Said", color="#6e6e6e")
define vin = Character("Vince")
define yl = Character("Ylva", color="#dbd360")

define lb = Character("Lost Boy", color="#6d4c41")
define h = Character("Headmaster Goude", color="#455a64")
define unknown = Character("???", color="#424242")
define hek = Character("Club Member", color="#5d4037")
define anek = Character("Club Member", color="#3e2723")
define anek2 = Character("Simon", color="#37474f")
define lek = Character("Club Member", color="#263238")
define lek2 = Character("Simon", color="#424242")
define v = Character("Val", color="#4e342e")
define aek = Character("Club Member", color="#3c3c3c")
define s1 = Character("Club Member", color="#512da8")
define s2 = Character("Club Member 2", color="#303f9f")
define s11 = Character("Student 1", color="#512da8")
define s22 = Character("Student 2", color="#303f9f")
define h1 = Character("Heckler 1", color="#ad1457")
define h2 = Character("Heckler 2", color="#6a1b9a")
define ster = Character("Sterling", color="#2e7d32")
define h3 = Character("Hugo", color="#bf360c")
define sky = Character("Skylar", color="#1565c0")
define orib = Character("Oribe", color="#7b1fa2")
define ymv = Character("Young Man's Voice", color="#5d4037")
define arline = Character("Arline", color="#424242")
define salem = Character("Salem", color="#37474f")
define promoter = Character("True Strike Promoter")
define finn = Character("Finn")

default chosen_club = None
default chosen_club2 = None

init:    
    #Vars
    $ lucas_romance = None
    $ naomi_romance = None
    $ sue_romance = None
    $ reina_romance = None
    $ elio_romance = None
    $ killian_romance = None
    $ lucas_platonic = None
    $ naomi_platonic = None
    $ sue_platonic = None
    $ reina_platonic = None
    $ elio_platonic = None
    $ killian_platonic = None


    # Hatchling Sounds
    define audio.hatchling1 = "audio/Music/Days of Our Lives… In Huntsdale.mp3"
    define audio.hatchling2 = "audio/Music/Blackout.mp3"
    define audio.hatchling3 = "audio/Music/Romance of the East.mp3"
    define audio.hatchling4 = "audio/Music/Chair Waltz.mp3"
    define audio.hatchling8_2 = "audio/Music/On the Verge of a Breakthrough.mp3"
    define audio.hatchling10 = "audio/Music/Hello, Or Goodbye.mp3"
    define audio.hatchling12 = "audio/Music/4th Year Hatchling (Overture).mp3"
    define audio.hatchling14 = "audio/Music/Troaran Horse.mp3"
    define audio.hatchling15 = "audio/Music/Ruthless Regression.mp3"
    define audio.hatchling21 = "audio/Music/Meditations.mp3"
    define audio.hatchling22 = "audio/Music/...A Rotten Egg.mp3"
    define audio.hatchling25_2 = "audio/Music/Ocean’s Embrace.mp3"
    define audio.hatchling17 = "audio/Music/Heralding a New Day.mp3"
    define audio.reinaTheme = "audio/Music/Reina2#Min.mp3"
    define audio.lucasTheme = "audio/Music/Lucas#2.mp3"
    define audio.ylvaTheme = "audio/Music/Cana.mp3"
    define audio.sueTheme = "audio/Music/Sue.mp3"
    define audio.gwynetteTheme = "audio/Music/Gwynette.mp3"

    $ preferences.set_mixer("music", 0.8)

label start:
    $ Alexis = "Alexis"  # Default name
    
    scene black with dissolve
    
    # Show character creation screen
    call screen name_input
    if _return.strip() == "":
        $ temp_name = "Alexis"
        "We will call you Alexis."

    else:
        $ temp_name = _return

    call screen gender_selection
    $ player_gender = _return
    
    jump prologue

label prologue:
    $ killian_vl_prefix = "audio/voices/Love Interests/Killian/Prologue/Killian_Prologue_MeetingKillian_"
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Prologue/Elio_Shared_Prologue_"
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Prologue/Reina_Prologue_"
    $ sue_vl_prefix = "audio/voices/Love Interests/Sue/Prologue/SueDaengQan_Prologue_MeetingNaomi/SueDaengQan_Prologue_MeetingNaomi_"
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Prologue/Lucas_Prologue_MeetLucas_"
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Prologue/Naomi_Prologue_MeetNaomi_"
    $ goude_vl_prefix = "audio/voices/Supporting-Extra/Isaiah/Prologue/Isaiah_Prologue_MeetKillian_"
    $ arline_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Arline/Prologue/Arline_Prologue_Introduction_"
    $ phillip_vl_prefix = "audio/voices/Supporting-Extra/Phillip/Prologue/Phillip_Prologue_MeetPhillip_"
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Prologue/Gwynette_Prologue_"
    $ vince_vl_prefix = "audio/voices/Friends/Vince/Vincent_Prologue_MeetGwyn&Vince/Vincent_Prologue_MeetGwyn&Vince_"
    $ ylva_vl_prefix = "audio/voices/Friends/Ylva/Prologue/Meeting Ylva Said/Ylva_Prologue_MeetingYlvaSaid_"
    $ said_vl_prefix = "audio/voices/Friends/Said/Said Prologue MeetYlvaSaid/Said_Prologue_MeetYlvaSaid_"
    
    scene bg mainstreet_afternoon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Prologue - Welcome to Magiana\nZynday, Esynce 26th, 1027 RD")
    
    a "Abyss take me, I'm tired..."
    
    "I'm barely off of the bus, one of the only souls heading north out of Ferenicia. The airship from Prospera was overnight, but of course I didn't get a wink of sleep."
    "The Huntsdale Bus Terminal is a pretty plain looking building. The rest of the town—my home for the next year—looks cute from where I'm standing, but nothing to write home about."
    "The building over there looks like a mall. That… castle? Is that a damned castle? Gods, I really am tired. The school building? I know it's one of the oldest buildings around. But that’s not where I needed to go, right? Where {b}was I{/b} supposed to go?"
    "Standing around isn’t going to do me any favors, so I take up my bag and suitcase and start walking. The castle—I swear that can’t be right—seems like a good start."
    "There are a few others wearing the same uniform I am. None of them give me so much as a second glance."
    "The luggage should make me stand out, but for all they knew, I was some fourth-year they'd never met coming back after summer break."
    "Not someone who had the bright idea of starting at a new school right before graduation."
    "Here I am, about half a year removed from the point of no return, and a part of me is still wondering how I let Mother send me on this fool's errand."
    
    scene black with fade
    vl arline_vl_prefix 1
    arline "This will be your last year of school, so please don't stress, and just try to enjoy yourself."
    scene bg mainstreet_afternoon with fade
    
    "I can try, but it's going to be hard to forget just how badly the family needs money right now..."
    "A boy standing on a corner catches my eye. Whatever worries I might've had puff away, and all I can focus on is the way he's staring up at the street signs like he's never had to read one a day in his life."
    "It isn’t like I know where I’m going either, but I’ve definitely read street signs before. Maybe I’ll be able to help him out. The closer I get, the more I feel like I’ve seen him somewhere before."

    show phillip neutral:
        xpos 0.6
        yalign 1.0
    with dissolve
    a "Excuse me? Do you need any help there?"
    
    show phillip excited at center with move
    "He jumps a bit when I speak. I didn't mean to sneak up on the poor kid. When he turns to me, the weird sense that I've definitely seen him before grows stronger."
    
    vl phillip_vl_prefix 1
    lb "Oh, I'm alright, thank you."
    show phillip contemplative
    "He raises a brow at me."
    vl phillip_vl_prefix 2
    lb "I'm sorry, but we haven't met before, have we?"
    
    "I've heard that accent of his before. Fancy dinners. Tailored suits and flowing dresses. Parlors when Mother and Father called on their noble friends."
    "This was a rich people accent. And I {b}had{/b} seen this boy before. Rich was an understatement with this one. How did I forget about him?"
    
    a "Prince Phillip? Your Highness, it is you! I'm Blakesley, [a] Blakesley. We met in Prospera a while ago when your family visited!"
    
    show phillip neutral
    "The prince blinks at me a few times, but I can tell that the dots aren't connecting in his head."
    
    vl phillip_vl_prefix 3
    p "Blakesley... Blakesley... I'm sorry, the name doesn't ring a bell. I didn't know you went to this school. I would have assumed that you'd stay down south."
    
    a "So did I. This is my first time in Huntsdale."
    
    vl phillip_vl_prefix 4
    p "First time?"
    
    "He looks me up and down."
    
    vl phillip_vl_prefix 5
    p "I could've sworn you were older than me."

    "And there it is. I knew this was going to happen as soon as I found out I got accepted. May as well get used to telling the story."
    
    a "Yeah, I'm new, but I'm a fourth-year."
    
    show phillip excited
    vl phillip_vl_prefix 6
    p "O-oh, really? Well, you missed the Welcome Gala, so... maybe the Wilson Building?"
    
    "He points off in the distance. It was a short distance away from the castle I'd been heading towards."
    
    if eval(a.name)[0] == "Alexis":
        vl phillip_vl_prefix 7A
    else:
        vl phillip_vl_prefix 7B
    p "That's the school's administrative building. Someone should be able to help you there. Take care, [a]."

    a "Thanks… I nearly forgot! Happy belated sixteenth birthday, Your Highness."

    "Only last month, too. One of the youngest first years, if not the youngest, but the most famous at the same time. I wonder how that feels."
    
    vl phillip_vl_prefix 8
    p "T-thank you. I wasn’t expecting that this long after the day. Well, I’m sure I’ll be seeing you around. Until then."

    hide phillip with dissolve
    "He perked up a bit at what I said, but the joy I feel in seeing the look on his face is short lived."

    "I meant to help him, but it's only after he's gone that I realize he helped me. What a fantastic way to start my new school career."
    
    scene bg student_councilroom_afternoon with fade
    "The Wilson Building is one of the taller ones in town, so with the prince's directions, it's actually pretty easy to find."
    
    "I explain my situation to a secretary and she points me to the Student Council Room up on the second floor of all places."
    
    "When I get there, I knock."

    $ sue_vl_prefix = "audio/voices/Love Interests/Sue/Prologue/SueDaengQan_Prologue_MeetingSue/SueDaengQan_Prologue_MeetingSue_"
    
    vl sue_vl_prefix 1.1
    "Student Council President" "Come in."
    
    show sue neutral with dissolve
    "The door opens easily and I take a step inside. The room is empty, save for a sole young woman sitting at a desk in the back, a gavel resting next to a stack of documents. She’s looking over one of them when I first come in."

    "If she has a desk all to herself, she’s obviously important. The president, maybe?"
    
    vl sue_vl_prefix 2.3
    "Student Council President" "You can leave your things by the table, if you'd like."
    
    "I take her up on her offer and drop my bag. There isn't that much in it, but it's nice to have the weight off my shoulders."
    
    "When she's finished scanning the document she was reading when I came in, the president gets up and walks over to me."
    
    vl sue_vl_prefix 3.2
    "Student Council President" "My name is Sue Daeng Qan, Student Council President. It's nice to meet you."
    
    a "[a] Blakesley. Same to you, Sue."
    
    vl sue_vl_prefix 4.1
    s "So you're the Fourth Year Hatchling the headmaster's told me about. Worry not, it's my job today to help you get a lay of the land, so you're not completely lost your entire first week here at MIA."
    
    a "That would be a {b}huge{/b} help."
    
    show sue happy
    vl sue_vl_prefix 5.1
    s "Haha, I know. You can leave your things here. We'll be coming back eventually. Now let me show you our wonderful little corner of Magiana, Huntsdale."
    
    "Sue heads towards the door. Only then my brain registers something she just said."
    
    a "MIA?"
    
    show sue neutral
    vl sue_vl_prefix 6.1
    s "I suppose you wouldn't know. 'Magiana Imperial Academy.' It was the school's old name, until about a century ago. We still like to call it 'MIA,' though. It sounds better than 'I.A.H,' doesn't it? Now, let's get on with that tour."
    
    scene bg mainstreet_noon with fade

    show reina neutral:
        xpos 0.2
        yalign 1.0
    show sue neutral:
        xpos 0.5
        yalign 1.0
    with dissolve

    "On our way outside, Sue and I bump into someone. She gives Sue a small curtsy, and then her eyes fall on me."
    "She looks me up and down, which makes me feel more self conscious than I thought it would. Hold on, something about her is familiar too..."

    vl reina_vl_prefix 1
    "Formal Girl" "That's a demerit."
    
    a "I'm sorry?"
    
    "She has the same rich people accent as the prince. I guess it only makes sense for all sorts of nobles to go to the same school as him."
    
    vl reina_vl_prefix 2
    r "The academy's dress code expressly prohibits accessorization and uniform modification. Yet I can see a necklace as plain as day. There are exceptions for religious reasons, but in your case, I don't believe that applies."
    
    "Dress code? What in the Abyss is she going on about?"
    
    "She produces a notepad and pen from a pocket in her skirt. She wasn't really about to write me up for wearing a damned necklace, was she?"
    
    if player_gender == "female":
        s "Hold on a second, Reina. She just got here. I told you about that new fourth-year, didn't I?"
    else:
        s "Hold on a second, Reina. He just got here. I told you about that new fourth-year, didn't I?"
    
    show reina worried
    vl reina_vl_prefix 3
    r "So that's who they are. I am sorry, but new students aren't exempt from the rules. You should know that, Sue."
    
    show sue melancholic with dissolve
    "Sue sighs, and then gestures to the girl."
    show sue embarrassed_closed
    s "This is Reina Dreyar. She's the head of the Student Council's Disciplinary Committee. Forgive her. This sort of thing is literally her job."
    
    a "But for a necklace?"
    
    "And who cares if it's not a religious symbol? With the memories packed into this thing, it may as well be for me..."
    
    a "Don't you think that's a little unreasonable? What, did you go writing up all the new first years who didn't know any better?"
    
    show reina happy
    "She just smiles at me."
    
    a "You've got to be kidding me."
    
    show reina neutral
    vl reina_vl_prefix 4
    r "I am simply doing my duty. You've already met the President of the Student Council. If you take issue with the official rules of the school, you're more than free to take them up with your representative."
    
    "She again curtsies."
    
    vl reina_vl_prefix 5
    r "Now, if you'll excuse me, I had some business in the Wilson Building. A good day to you both."
    
    hide reina with dissolve
    "Once she's through the doors, I turn on Sue."
    
    a "\"Official rules\"? No way she's right."
    
    show sue neutral at center with moveinright
    s "She is."
    
    a "That's insane."
    
    s "That's what everyone else said. Which is why we started ignoring them at some point."
    
    "She glances towards the door and then back to me."
    
    s "I know that wasn't a particularly good first impression, but try not to hold it against Reina. She is just trying to do her job. Though I will admit she could stand to be a bit more relaxed sometimes."
    
    show sue embarrassed
    "What she says next she whispers to herself, but just loud enough that I can still make it out."
    
    s "She definitely needs a girlfriend to help her mellow out."
    
    show sue neutral
    "Sue clears her throat."
    
    s "Let's keep going?"
    
    a "Let's."
    
    "Sue shows me around Huntsdale, pointing out various shops and hangout spots that students frequent. She tells me that a cafe called The Amity and the Plainfield Mall are probably the most popular in Huntsdale itself."
    
    "For a lot of other things, people just catch a bus and head down to Ferenicia for the day."
    
    "Eventually, we stop in front of a cute little library. The Weaver Library, it was called."
    
    s "It isn't officially affiliated with MIA, but this library's been here since the town was founded. It's the unofficial official library we students rely on."
    
    scene bg weaver_library_afternoon with fade

    show sue neutral at character_pos2 with dissolve
    "It might be because classes haven't properly started, or maybe it's because libraries are dying, but the library is deserted. Mostly. I can hear someone snoring softly from somewhere deeper in."
    "The grand desk I'd expect to see a librarian behind is deserted, too. Maybe the person in charge of the place is catching some shut eye."
    
    show lucas neutral at character_pos6 with easeinright
    "A boy in glasses pops his head out from behind a bookshelf. He starts to speed walk towards us."
    
    vl lucas_vl_prefix 1
    "Bespectacled Boy" "Sue, could you help me hunt down some overdue books? A few are from locals, but most are from students. Some taken out before summer, no less."
    
    s "If you can put together a list, I'll hand it off to Reina. She'll be able to get your books back."

    show lucas happy
    vl lucas_vl_prefix 2
    "Bespectacled Boy" "Thank you."
    show lucas neutral

    "Then he finally notices me."

    vl lucas_vl_prefix 3
    "Bespectacled Boy" "Who is this?"
    
    s "[a] Blakesley. They just transferred in. A bit of a rare case, since they're a fourth year like us. And this is Lucas. He's the president of the literature club. And the temp librarian, if the normal librarian is ever absent."
    
    vl lucas_vl_prefix 4
    l "Transferring in at the start of your fourth year? Look, I get it might be overwhelming, but if you ever need help with anything in class or in the library, I'd be willing to help you out. Just ask around for Lucas."
    
    a "Thanks for the offer. Definitely think I'm going to have to take you up on that sometime."
    
    vl lucas_vl_prefix 5
    l "If you're showing them around, Sue, you might want to go see Naomi. She's probably cooking something right now for all the first years. Maybe our new arrival will be able to get their hands on something before they're all gone."
    
    s "Good idea! Magis Hall was next on the list anyway."
    
    vl lucas_vl_prefix 6
    l "I've got to keep looking through the ledgers to see if there are any other missing books. I'll get a list to the Student Council when I can. Nice meeting you, Blakesley."
    
    scene bg maincastle with fade
    "Before long, we finally come to the castle I saw from the bus terminal. A stream of students are coming and going. Probably on little tours of their own ahead of classes starting later this week."

    "Seeing it up close, it isn’t quite a castle, but it’s pretty damn close. It’s definitely big, fancy, and {b}old{/b}."
    
    a "Whoa..."
    
    show sue happy at character_pos6 with dissolve
    s "This is Magis Hall. Where most of the magic happens. Haha, impressive, isn't it?"
    
    a "This thing must be older than my entire family."
    
    show sue neutral
    s "Older than your...? Well, yes, actually. This building's—"
    
    show killian neutral at character_pos2 with dissolve

    stop music fadeout 0.5
    vl killian_vl_prefix 1.1
    "Tall Boy" "Hey, Sue."

    play music hatchling22 fadein 0.5
    
    "A tall guy saunters over to the two of us, apparently none the wiser to the fact that he butt into our conversation. He points a thumb at me as he talks to Sue."
    
    vl killian_vl_prefix 2.2
    "Tall Boy" "Where'd this one come from?"
    
    show sue embarrassed_closed
    s "They're a new student. I'm giving them a tour."
    
    vl killian_vl_prefix 3.2
    "Tall Boy" "New... Student?"
    
    "He turns his attention to me, slouching and squinting hard through his circle lenses. I shrink a little under his gaze."
    
    a "Can I help you?"
    
    vl killian_vl_prefix 4.1
    "Tall Boy" "You look old for a first-year student. You don't have as much hope and wonderment gleaming in your eyes as the others."
    
    a "...Thank you?"
    
    show sue neutral
    s "There are some extenuating circumstances, but they are new, Killian. Of that, I can assure you."
    
    play sound "audio/sfx/phone_notification.ogg"
    "He opens his mouth to speak, but then a song starts playing. It's a peppy, upbeat song. Familiar and slightly muffled."

    "I think I recognize the language, too. Estarese, I think?"

    "Killian takes his phone out of his pocket to dismiss their alarm, but takes a  closer look and gasps."
    
    show killian surprised
    show sue neutral

    vl killian_vl_prefix 5.1
    k "{b}Shit{/b}! The {b}Blue Meridian{/b} Watch-a-thon's supposed to start soon!"
    
    "The tall boy straightens up a bit and gives both of us one last look and a wry grin."
    
    show killian happy
    show sue neutral

    vl killian_vl_prefix 6.1
    k "Lend me your energy. I'll need it for what's to come. Hang on, Rikki, I'm coming!"
    stop music fadeout 1.0
    
    hide killian with easeoutleft
    "Without another look at the two of us, he tears off towards Magis Hall, nearly crashing into several people on the way."
    pause 1.0
    
    a "What was that about?"
    
    show sue melancholic_closed
    s "That's just Killian. He's the anime club's president."
    
    "An odd introduction with the way he stared me down, but I've definitely seen people give worse first impressions."
    
    play music hatchling1 fadein 0.5

    show sue neutral
    s "Where was I? Oh, right. Magis Hall was built with the rest of the school, in the 8th century. There are plenty of noble titles younger than that."
    
    a "Gods. How many times have they ripped its guts out to keep up with the times?"
    
    s "My guess is at least twelve. Come on, let's go inside."
    
    "We're barely inside the building before someone else approaches us. He isn't old, but judging by the suit he's wearing, he clearly isn't a student, either. And what’s with that shoulder cape he’s wearing? It was certainly a choice."
    
    if eval(a.name)[0] == "Alexis":
        vl goude_vl_prefix 1A
    else:
        vl goude_vl_prefix 1B
    h "Ah, you're [a] Blakesley, I assume?"
    
    a "Yes. It's nice to meet you."
    
    vl goude_vl_prefix 2
    h "Likewise. My name is Isaiah Goude. I'm the headmaster of the Imperial Academy at Huntsdale. I'm sorry I wasn't able to give you the tour myself, but I couldn't find the time."
    
    a "Don't sweat it. Can't be easy running a school like this."
    
    "Especially the year that royalty comes to campus."
    
    vl goude_vl_prefix 3
    h "And I'm going to have to inconvenience you again. Sue, could you come with me for a minute?"
    
    "Sue turns to me."

    s "Feel free to walk around by yourself. Magis Hall isn't {b}that{/b} complicated, really. We'll meet out here later, alright?"
    
    a "Yeah, sure."
    
    hide sue with dissolve
    "The two of them head off, and I crane my neck to look at the building. Just a bunch of hallways and classrooms. I'll be able to survive that much."
    
    # Start Gwynette & Vince
    scene bg music_hall_afternoon with fade
    
    "On the bright side, Sue was right. It isn't that complicated. The issue is that the floors feel like they were copy-pasted during construction."
    "I can barely tell most of the rooms on the first floor apart from the second."
    "It's still going to take some time just memorizing where my classes are to make sure I don't accidentally wander into Language Arts when I have History."
    "I peek my head into another one of the classrooms, expecting it to look the same as the rest of them. Instead, I’m met with a peculiar sight."
    "Several of the desks have been pushed up against the wall, and in their space, is a… loveseat? With a drachkin sprawled out on it."
    "Right when I wonder why this girl’s turned a classroom into her personal lounge, I notice the elf seated behind a canvas, sketching her."
    "That makes a lot more sense than… whatever it is I was thinking."
    "I lock eyes with the drachkin, and she beams."

    show gwynette neutral at character_pos2 with dissolve
    vl gwynette_vl_prefix 1
    "Drachkin girl" "Welcome in, welcome in!"

    "She hops off of the couch and hurries across the room. Judging by that groan, the elf’s none too happy about it."

    show vince annoyed at character_pos6 with dissolve
    vl vince_vl_prefix 1
    "Elf boy" "Dammit, Gwyn, I told you not to move!"

    vl gwynette_vl_prefix 2
    "\"Gwyn\"" "What, and leave our guest hanging? No way, VV."

    "Gwyn turns to me, the radiant smile she flashes making me feel right at home."

    vl gwynette_vl_prefix 3
    "\"Gwyn\"" "Nice to meetcha! I’m Gwynette, Gwynette Ellis. I don’t recognize you. You one of the first… years?"

    "Her joy quickly gives way to utter confusion. A moment after smiling at me, she looks as if she’s been told a riddle she doesn’t know the answer to. And in a way, I guess I am."

    "The elf joins us, looking like he’d rather be anywhere else than in our company."
    
    show vince neutral with dissolve
    vl vince_vl_prefix 2
    "\"VV\"" "Looks too old to be a first-year."

    a "Again, really?"

    vl gwynette_vl_prefix 4
    gw "Again?"

    "I tell them about my recent run in with Killian. After, they share a knowing look."

    vl gwynette_vl_prefix 5
    gw "Definitely sounds like Killian to me."
    vl gwynette_vl_prefix 6
    gw "And before I forget, this is my boyfriend, VV."

    vl vince_vl_prefix 3
    "\"VV\"" "Vincent Ziani. Or \"Vince.\" Call me \"VV,\" and we’re going to have problems."

    a "I wasn’t going to, I assure you."

    "I look back to the easel and the couch."

    a "So this is an art room?"

    vl vince_vl_prefix 4
    vin "Art Club meets here, yeah."

    vl gwynette_vl_prefix 7
    gw "You should totally stop by sometime. VV’s art is {b}so{/b} good!"

    show vince flustered
    vl vince_vl_prefix 5
    vin "Gwyn!"

    "Yet he’s gone red all the same."

    a "Are you in the club too, Gwynette?"
    vl gwynette_vl_prefix 8
    gw "Nope. Can’t draw to save my life. The Music Club is where I let myself fly free. I just bug VV here sometimes because, you know."

    "There’s a brief lull in conversation, and it really lets me get a good look at Gwynette. Dyed hair, piercings galore, practically drowning in necklaces and bracelets, absolutely covered in tattoos..."

    a "Reina must be your worst nightmare."

    vl gwynette_vl_prefix 9
    gw "So you’ve met her?"

    a "Wrote me up damn near first thing. For a necklace."

    show vince neutral
    vl vince_vl_prefix 6
    vin "Sounds about right."

    a "How do you handle her?"

    vl gwynette_vl_prefix 10
    gw "Oh, I don’t have to worry about her one bit. Well, maybe a bit, but not much."

    a "How do you manage that?"

    "Before she can answer, Vince takes her hand."

    vl vince_vl_prefix 7
    vin "Alright, break’s over."

    vl gwynette_vl_prefix 11
    gw "‘Kay. Where are my manners? I never asked your name."

    a "[a] Blakesley."

    vl gwynette_vl_prefix 12
    gw "Well, BB, it’s nice to meetcha! …Again."

    vl vince_vl_prefix 8
    vin "\"BB\"? Lame."

    "Gwynette waves at me as she lets Vincent lead her back to the loveseat. She throws herself on it and resumes her pose so he can get back to work."
    "For how disinterested he seemed a moment ago, I can tell just by looking at his sketch that he cares an awful lot about his subject."
    scene black with fade
    "Smiling to myself, I leave the young couple to what they were doing, closing the door on my way out."
    
    scene bg home_ec_room_door_afternoon with fade
    "From there, I go up to the third floor, expecting to see more of the same identical classroom."
    "It turns out, the classes on the third floor were the exception. I knew that schools like MIA were special since they baked magic into the curriculum, but it didn’t quite sink in until I saw the classrooms they were taught in."
    "Most of them, anyway, had unique layouts. I peaked in one of the few that just had lines of desks and saw what was definitely a priest of the Nyrellan Church chatting up some people, so I don’t know what to make of that one."
    "When I've seen enough, I start heading down to wait for Sue outside. On the first floor, some succulent smell hits my nostrils. I make my way towards it, coming across a room with its doorway crowded by people idly munching on something."
    "They make way for me as I approach. And those are most certainly rice balls. And this is definitely a home ec room."

    show naomi neutral apron at center with dissolve
    "There's a lone girl within, tending to a pot. She's faintly humming to herself. She notices me out of the corner of her eyes and stops."
    
    vl naomi_vl_prefix 1
    "Girl in apron" "Why, hello. Are you here for a rice ball, too?"
    
    a "Oh, just passing the time, really..."
    
    "I scan the room again. No one else is around."
    
    a "You're by yourself?"
    
    vl naomi_vl_prefix 2
    "Girl in apron" "Oh, it's no trouble."
    
    a "Maybe I could help you out? I'm not doing anything right now anyway."

    "If Sue got whisked away by the headmaster of all people, surely she must still be busy, right?"
    
    "The girl takes a moment to consider my offer, then she gives a slight bow."
    
    show naomi happy apron
    vl naomi_vl_prefix 3
    "Girl in apron" "If you wouldn't mind. My name is Naomi. Naomi Kuzuma. I'm lucky enough to serve as the president of the school's Home Ec Club."
    
    a "That I figured. Name's [a] Blakesley, by the way."
    
    "I roll up my sleeves."
    
    a "So what do you have for me?"
    
    "She has me wash my hands before showing me to the rice cooker, where she spoons its contents into an equally large bowl. A few moments later, she brings me sheets of seaweed, a knife, a roll of plastic wrap, and a bowl of water."
    
    vl naomi_vl_prefix 4
    n "Have you ever made rice balls before?"

    "I shake my head."

    vl naomi_vl_prefix 5
    n "They’re super simple. Watch closely."

    "She forms one, and then two, wrapping them up and setting them aside. When she steps back to let me take over, I feel mostly confident that I won’t completely screw things up."

    "A few stop by Naomi, over by her pot, and strike up a conversation. I lose count of how many people come in, but no matter who it is, Naomi is able to talk with them as if they were old friends."
    
    "Even the first years meeting her for the first time seem right at home after exchanging only a few words."

    "The group hanging around outside ended up being fans of hers, or something. The only reason they stuck around was so they could talk to her every once in a while."

    "I’m focused on the rice balls, so I don’t pick up many specific details of her talks, but on more than a few occasions I hear an honorific tacked onto her name. At some point I heard \"Naomi-tensei,\" even. Wasn’t that one supposed to be a big deal?"

    show naomi neutral apron at character_pos2 with moveinright
    show sue neutral at character_pos6 with moveinright
    #vl sue_vl_prefix 1.2
    s "There you are."
    
    "I jump when I hear Sue beside me. She's holding one of my rice balls up to the light, inspecting my handiwork."
    
    #vl sue_vl_prefix 2.2
    s "Not bad. Are you ready to get going? We're almost done."
    
    "I call over to Naomi and ask if she still needs me around."

    show naomi happy apron
    vl naomi_vl_prefix 6
    n "I should be alright now. Thank you for the help."

    "Sue hands me a rice ball, waves to Naomi, and heads for the door. I follow."

    vl naomi_vl_prefix 7
    n "Just a second!"

    "She catches up to us, offering me a small cup of some steaming liquid. It must’ve been from that pot of hers."

    vl naomi_vl_prefix 8
    n "If you ever need a quiet place, you’re welcome here. I always make too much food anyway."
    
    scene bg maincastle with fade
    stop music fadeout 2.0
    "I sip on the cup Naomi gave me as I follow Sue out of Magis Hall. It's a spicy soup, but oddly comforting. I could definitely imagine sipping a bowl of this on a cold winter’s night."
    
    scene bg wright_gymnasium_afternoon with fade
    play music hatchling14 fadein 1.0
    show sue neutral at center with dissolve
    s "And this is where phys ed will happen. And where most of the sports clubs meet."
    s "In fact, there should be a little something going on right now. Let’s go inside."

    "Sue leads me into the gymnasium. And she was very right. It’s full of people. The sounds of grunts and wood clashing against wood—and even a bit of what sounds like steel on steel?—reverberate throughout the building."

    "In the center of the gym floor, there’s a crowd gathered."

    a "What’s that about?"

    show sue happy
    s "A match we don’t want to miss, probably."

    "It takes a bit to get through enough of the crowd to actually see what’s going on. We get stuck in the middle of the spectators, but I’m able to make out the pair that drew so much attention."
    hide sue with dissolve

    show ylva neutral club at character_pos2 with dissolve
    show said neutral enseki at character_pos6 with dissolve
    "A boy and a girl circle each other. Prominent on the boy’s face is an intricate tattoo inked in black."
    "The girl’s hair is so light in color it damn near reflects the lights of the gymnasium. I’m able to spy glimpses of her icy blue eyes and a tiny tattoo of the same color underneath her eye, too. I haven’t seen many Ekaskans in person, but her features are unmistakable."
    "It’s only after those striking details are processed that I pay attention to the rest of what they’re doing."
    "The boy’s wearing martial arts robes, but firmly grasps a sword in one of his hands. As for the girl, she definitely looks ready for physical activity, but definitely no sport I’ve ever heard of. On top of a shortsword, she’s holding a stick?"

    show sue neutral at center with dissolve
    s "Ah, Ylva and Said. No wonder they were so excited."
    hide sue with dissolve

    "The girl—I assume she’s Ylva—steps forward, swinging with her stick,  but the blow is deftly blocked. Dual wielding the way she was, I expected her to easily come out on top, but Said was quick, both on his feet and with his hands."
    "He didn’t have a chance to go on the attack, but his defense was incredible. Said jumps back, putting some space between himself and Ylva. It looks like he’s about to make his move, but the match ends before I know it."
    "Almost as soon as he was out of arm’s reach, Ylva brought her sword and stick together, locking the stick into the base of her sword’s handle."
    "She let her newly formed spear slide through her hands, gripping it close to the base and used the additional reach to sweep Said right off his feet."
    "The sound of him landing hard on his back is drowned out by the chorus of winces and groans from their viewers."
    "Ylva helps Said to his feet and then faces the crowd."

    show ylva warm club with dissolve
    vl ylva_vl_prefix 1
    yl "That’s enough of a show. Go on and have fun."

    "The crowd disperses. Where Sue and I were lost in the small sea of people a moment ago, we were now awfully exposed. When Ylva sees us, she smiles and comes our way, Said on her heels."
    "Seeing them side by side, Ylva’s a bit taller than he is. And now that she’s not fighting, I see the necklace and rings she’s weaning."
    
    vl ylva_vl_prefix 2
    yl "Lady Sue, it’s nice of you to visit us."

    show ylva warm club at character_pos1 with moveinright
    show said neutral enseki at character_pos4 with moveinright
    show sue neutral at character_pos7 with dissolve
    s "And it’s good to see you too, Lady Ylva. Said, you did a good job, too."

    vl said_vl_prefix 1
    sa "Thank you."

    a "What was that all about?"

    s "The Swordplay Club and Enseki Club both use the gym, so they decided to have a little exhibition day today."

    a "Guess that explains the robes and the sword."

    "When Ylva turns to me, there’s a surprised look in her eye, as if she hadn’t noticed me until just now."

    vl ylva_vl_prefix 3
    yl "Welcome, stranger. Ylva Brandt, Vice Captain of the Swordplay Club. If you ever come by, I look forward to seeing what you can do with a blade."

    a "Name’s [a] Blakesley. So you’re the vice captain? Must mean you’re pretty good in a fight."

    vl said_vl_prefix 2
    sa "This is very true."

    a "Sue mentioned that you were… Said, right?"

    vl said_vl_prefix 3
    sa "Said Ramzanovich Abdullaev."

    "Ylva’s tattoo is plain as day, and I think I see a bit of ink on Said’s chest peeking just past his robes. That seems…"

    a "Hey, Sue?"

    s "What is it?"

    a "How does Reina deal with…"

    "I gesture towards Ylva and Said."

    vl said_vl_prefix 4
    sa "This is not important for me."

    show ylva neutral club
    vl ylva_vl_prefix 4
    yl "Nor are my Kiss or Solaria any concern of hers."

    "The tattoo and jewelry, if I had to take a guess. If they have special names, no wonder Reina doesn’t touch them. Must have some crazy cultural significance."

    a "That explains the tattoos, and Said’s robes make sense, but Ylva, you—"

    vl ylva_vl_prefix 5
    yl "Lady Reina can grouse all she wants about the clothes I wear to my club. I will not change them."

    a "Fair enough."

    vl said_vl_prefix 5
    sa "Is that soup? "

    "I’d completely forgotten about it. The cup’s almost empty at this point, but there’s still a bit left. Should’ve known others would be able to smell it. Hope it didn’t make anyone here too hungry."

    a "Got it from Naomi not that long ago. In the Home Ec room."

    show ylva adoration club with vpunch
    vl ylva_vl_prefix 6
    yl "Naomi-tensei made that for you?!"

    a "Yeah, she was making a big pot of—"

    hide ylva with moveoutleft
    show sue happy
    "Ylva, spear still in hand, rushes away from our little group. Sue lets out a little laugh, while Said just shakes his head."

    vl said_vl_prefix 6
    sa "I forget this is second-year student."

    show sue neutral
    s "I know, right? Anyway, I was showing [a] around. Just about done, so we’re going to head out."

    vl said_vl_prefix 7
    sa "Peace be with you, Blakesley."
    stop music fadeout 1.0

    # Start Elio

    scene bg wright_gymnasium_noon with fade
    play music hatchling1 fadein 0.5
    "The outside, while still warm, feels pleasantly cool compared to the gym, packed full of bodies. What else could Sue want to show me out here, though?"

    show sue neutral at character_pos6 with dissolve
    s "So that’s the gym itself. Last up is the field. If the weather’s good, class happens over here. Some clubs meet outside instead of inside, too."

    "I hear a small thud off in the distance."
    
    s "Speak of the Fiend. Sounds like the president of the Archery Club is here. Let's go say hello."
    
    show elio neutral at character_pos2 with dissolve
    "A few targets are set up. Across the field, someone's shooting at them. Even when we reach him, he just nocks another arrow."
    
    s "How's your practice going, Elio?"
    
    play sound "audio/sfx/arrow_release.ogg"
    with vpunch
    "He fires the arrow. Just barely misses the bullseye."
    
    vl elio_vl_prefix 1
    e "Fine."
    
    "Another arrow gets nocked."
    
    s "I'm showing a new student around. This is [a] Blakesley."
    
    a "Nice to meet you, Elio."
    
    play sound "audio/sfx/arrow_release.ogg"
    with vpunch
    "Another shot, and another near miss."
    
    show elio annoyed
    vl elio_vl_prefix 2
    e "I'm trying to focus."
    
    s "Right. Be seeing you."
    
    hide elio with dissolve
    "He's barely out of earshot before I open my mouth."
    
    a "What's his problem?"
    
    s "Oh, he's just not much of a people person. It isn't anything you should take personally. That should be everything, though. Let's get back to the Wilson Building."

    stop music fadeout 1.0
    
    scene bg student_councilroom_afternoon with fade
    "When we're finally back, I sink into the seat next to where I left my things. I barely noticed how tired my legs had gotten. Sue settles in at her desk at the back of the room."
    
    show sue neutral at center with dissolve
    s "I hope that proved useful."
    
    a "Very."
    
    s "Good."
    
    "She pauses. Just for long enough to put me on edge."
    
    show sue embarrassed
    s "When the headmaster called me away, he suggested something. Concerning you."
    
    "I sit up, trying not to look too nervous. Even though my mind is racing. I just got here, and all I said to the guy was \"hello.\" There’s no way I already pissed him off somehow."
    
    s "He suggested that I take you on as my aide for the year."
    
    "I let myself deflate, falling back in the chair and letting out the breath I had been holding."
    
    a "You had me scared for a second there."
    
    s "Sorry. It's just unorthodox. Student Council Presidents don't usually have aides. I didn't last year. But he believes it'll be useful for you, considering."
    
    a "Then I'll be the best aide that ever aided, boss."
    
    show sue happy
    s "Careful now. Don't want to set my expectations too high, do you?"
    
    #"Another pause."
    pause 1.0
    
    show sue neutral
    s "If you are going to be my aide, there are some things I need to tell you. This year is... special."
    
    a "Special how?"
    
    s "Let's see... The pins. Did you notice anything about the first years?"
    
    "I look down at my blazer. Pinned to my left lapel is a small charm representing House Lychester, the dorm I was assigned to. Everyone was wearing them."

    "Thinking back to the few first-years I saw, they had {b}two{/b} pins. The prince, too."
    
    s "Starting this year, new students will be placed into one of three 'Sectors': Special Operations, Civic Magic, and General Education."
    
    a "Alright. What's that about?"
    
    s "Students graduate and then go on to do all sorts of things. But being expected to ace all your history tests isn't going to be the most useful if you want to join Overseer or become a doctor."
    
    a "No, I guess not."
    
    s "They’re there to help students gain real world experience while in school. If they want to go down one of those paths."
    
    s "As for the second thing... in a few years, the school turns three hundred years old."
    
    a "No shot, really?"
    
    "I offer a small applause."
    
    a "Happy early birthday to MIA, then!"
    
    s "And to celebrate, Headmaster Goude thinks it would be valuable to pack up and leave."
    
    "My clapping stops."
    
    a "I'm sorry?"
    
    s "Next year, all school operations would take place {b}outside{/b} the empire. And the year after that. And one more time after that."

    "Leaving the country the school was founded in was certainly one way to celebrate the anniversary of its founding."
    
    a "And all of that concerns the Student Council how?"
    
    show sue melancholic_closed
    s "Money."
    
    a "Oh."
    
    "I don’t know about these \"Sectors\" Sue mentioned, but going worldwide three years in a row? With all of these students? The thought of that price tag alone makes me shudder."

    "Yeah, maybe the body representing the students should weigh in on something like that."

    show sue neutral
    s "Before I send you home for the day, most people join a club or two while they're here. Any catch your eye? It's your only year here, so you may as well make the most of it, right?"
    
    jump choose_club2

label choose_club2:
    menu:
        "Art Club":
            $ chosen_club2 = "art"
            jump art_club
        "Music Club":
            $ chosen_club2 = "music"
            jump music_club
        "Enseki Club":
            $ chosen_club2 = "enseki"
            jump enseki_club
        "Swordplay Club":
            $ chosen_club2 = "swordplay"
            jump swordplay_club

label choose_club:
    show sue neutral at center
    s "Any other clubs? Like I said, it isn’t uncommon for people to pick up a second. Sometimes people try to fit in three or four and rotate them, if they’re adventurous."

    menu:
        "A second club, eh? Is there anything else I’d want to do?"
        "No clubs":
            $ chosen_club = "no_clubs"
            jump no_clubs
        "Disciplinary Committee":
            $ chosen_club = "disciplinary"
            jump disciplinary_committee
        "Literature Club":
            $ chosen_club = "literature"
            jump literature_club
        "Anime Club":
            $ chosen_club = "anime"
            jump anime_club
        "Home Ec Club":
            $ chosen_club = "home_ec"
            jump home_ec_club
        "Archery Club":
            $ chosen_club = "archery"
            jump archery_club

label art_club:
    s "Art? You draw?"

    a "A little bit here and there. Not as much as when I was younger, though. Besides, it sounds like it would be fun to have a place to practice and meet other artists."

    s "Indeed it does."

    jump choose_club

label music_club:
    s "You sing?"

    a "I doubt you’d like to hear it, but every now and then."

    show sue happy
    s "I’m going to have to request a private concert one of these days."

    a "No, that’s too embarrassing."

    show sue neutral
    s "So are you going to never sing in front of the other club members?"

    a "…I’ll cross that bridge when I get to it."

    jump choose_club

label enseki_club:
    s "I didn’t take you for much of a martial artist."

    a "Because I’m not. Not yet, anyway. But I have to start somewhere, right?"

    s "Right you are. Good luck. I hear Said’s a good teacher."

    jump choose_club

label swordplay_club:
    s "Oddly appropriate."

    a "It is?"

    s "A nobleman’s child wielding a sword?"

    a "When you put it like that…"

    show sue happy
    s "You’ll be like a dashing knight right out of the middle ages!"

    a "Don’t know if a newbie like me could be called \"dashing,\" Sue."

    jump choose_club

label no_clubs:
    show sue neutral at center with dissolve
    s "Really? No other clubs?"
    
    a "Not really. Sure, I could try and have fun, but with only one year left, I may as well not tie myself down, you know? Besides, I've already got this new gig as your aide."
    
    show sue melancholic at center
    s "I suppose so. Well, that was all I had to say today. You’re free to go."

    jump prologue_end

label disciplinary_committee:
    show sue neutral at center with dissolve
    s "The Disciplinary Committee?"
    
    a "Yeah, why not? What was it Reina said earlier? Something about going through the Student Council after the necklace thing? Trying to make change from the inside. What better way than through the Disciplinary Committee?"
    
    show sue melancholic at center
    s "I don't think that's what she meant. No matter, I can let her know your intentions. I don't see any reason for her to object to you joining her."
    
    a "Sweet."
    
    show sue neutral at center
    s "Well, that was all I had to say today. You're free to go."
    jump prologue_end

label literature_club:
    show sue neutral at center with dissolve
    s "The Literature Club's a good choice. I wouldn't have thought you were much of a reader."
    
    a "I can only imagine how many classics must be in the libraries of a place this old. How could I stay away?"
    
    show sue happy at center
    s "I'm sure Lucas would be thrilled to hear that."
    
    show sue neutral at center
    s "I don't think there's anything else that needs to be done right now. You can get going."
    jump prologue_end

label anime_club:
    show sue neutral at center with dissolve
    s "A very popular choice, that one."
    
    a "I wonder why."
    
    show sue happy at center
    s "From what I hear, you'll be in good hands with Killian. He really knows his stuff."
    
    a "I'd hope so."
    
    show sue neutral at center
    s "Well, that was all I had to say today. You're free to go."
    jump prologue_end

label home_ec_club:
    show sue happy at center with dissolve
    s "Naomi won you over, didn't she?"
    
    a "I think she won over {b}most{/b} people who walked into that room."
    
    s "You're not wrong about that. She'll take good care of you. I've heard nothing but good things from people in her club."
    
    show sue neutral at center
    s "I don't think there's anything else that needs to be done right now. You can get going."
    jump prologue_end

label archery_club:
    show sue neutral at center with dissolve
    s "So Elio didn't put you off earlier?"
    
    a "Don't get me wrong, he's a real piece of work. But I like archery."
    
    show sue happy at center
    s "I guess that is how it would go. Well, you'll get used to him in time."
    
    a "I sure as sin hope so."
    
    show sue neutral at center
    s "I don't think there's anything else that needs to be done right now. You can get going."
    jump prologue_end

label prologue_end:
    "I take up my bag and my suitcase again. Sitting for a little bit did me some good."

    show sue neutral at center with dissolve
    s "Zynday, Istday, and Nyday are when the Student Council meets. So just come here after school on those days, alright?"
    
    a "You got it, boss. See you later."
    
    hide sue with dissolve
    scene bg dorm_common_noon with fade
    "Damn, that took most of the day. Wonder who my roommates are? Eh, not like that matters. All I care about right now is getting some sleep."
    
    "I met enough people today, and have more to think about than I thought. The last thing I need is to try and make small talk like that. With the way I feel right now, I'll be out as soon as I hit the mattress."
    
    scene black with dissolve
    "Here's hoping that when I wake up, I'm ready to face this new school life of mine."

    $ renpy.call(chosen_club + "_route_jinus", "Esynce", 26)
    
label route_branch_point:
    if chosen_club == "no_clubs":
        jump no_clubs_route_jinus
    elif chosen_club == "disciplinary":
        jump disciplinary_route_jinus
    elif chosen_club == "literature":
        jump literature_route_jinus
    elif chosen_club == "anime":
        jump anime_route_jinus
    elif chosen_club == "home_ec":
        jump home_ec_route_jinus
    elif chosen_club == "archery":
        jump archery_route_jinus



label route_branch_point4:
    if chosen_club == "no_clubs":
        jump no_clubs_route_exalt
    elif chosen_club == "disciplinary":
        jump disciplinary_route_exalt
    elif chosen_club == "literature":
        jump literature_route_exalt
    elif chosen_club == "anime":
        jump anime_route_exalt
    elif chosen_club == "home_ec":
        jump home_ec_route_exalt
    else:
        jump archery_route_exalt



label epilogue_graduation(month, date):
    $ goude_vl_prefix = "audio/voices/Supporting-Extra/Isaiah/Epilogue/Isaiah_Epilogue_Graduation_"
    scene bg maincastle with fade 
    play music hatchling17

    call screen calendar(month, date, "Overa", 25)
    $ renpy.notify("Graduation\nNyday, Overa 25, 1028 RD")

    vl goude_vl_prefix 1
    h "We’ve come to the end of a long road."

    "The day has finally come. I’m seated with the rest of the fourth years in front of Magis Hall."
    "The headmaster stands behind a podium, giving us the speech we all expected before we get our diplomas."

    vl goude_vl_prefix 2
    h "You’ve walked it, side by side with your peers, heads held high. And when you saw one of your fellows lagging behind, you would pick them up and help them along."

    vl goude_vl_prefix 3
    h "While myself and the rest of your Instructors have guided you along these last four years, we were merely assistants."
    voice sustain
    h "All of your victories, and the momentous achievement of making it to this day, were the result of your hard work and determination."

    vl goude_vl_prefix 4
    h "And for that, I must commend you all. Now, before awarding your diplomas, I’d like to invite the valedictorian to say a few words…"

    "Someone I’ve had maybe one conversation with takes the stand and goes on about everything we’ve gone through as a class and the potential we hold as a group to change the empire, and the world, for the better."

    "When they’re done, our names are called in alphabetical order."
    "We cross the school’s yard, take our diplomas, shake the headmaster’s hand, and return to our seats."

    "People around me talk with the others around them, but anyone I’ve come to even remotely consider a friend is nowhere near me."
    "Curse you, alphabetization."

    "At the end of the ceremony, the headmaster says a few parting words."

    vl goude_vl_prefix 5
    h "Today marks the end of one chapter of your lives and the beginning of another."
    voice sustain
    h "As you say your final goodbyes today, don’t forget that you will always have a home, not only here in Huntsdale, but among those with whom you shared these hallowed halls."

    vl goude_vl_prefix 6
    h "In all your endeavors, take heart and be brave. Just as you overcame these four years, I’m sure you’ll be able to overcome whatever life has to throw at you."
    voice sustain
    h "Thank you all, for allowing me the honor of being your headmaster."

    "Everyone’s been doing a good job keeping quiet, but at these words, we erupt into applause."
    "Now that we’ve been officially dismissed, people begin to mill about, forming small clusters."

    "Our families are across the street. When both groups begin to bleed together, I quickly find myself lost in a sea of bodies."

    "I know my family was here today. But where in the Abyss are they?"
    jump epilogue_no_clubs_route

label epilogue_intermission:
    $ skylar_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Skylar/Intermission/Skylar_Epilogue_Intermission_"

    scene bg maincastle with fade 

    "When I’m finally alone again, I make the call to Skylar. I just hope we’ll be able to hear each other over all of the yapping."

    vl skylar_vl_prefix 1
    sky "Well hello there, graduate."

    a "Haha, thanks. Where are you guys? I’m having trouble finding you in the crowd."

    vl skylar_vl_prefix 2
    sky "We stopped by a local park. Mother didn’t mind the crowd during the ceremony but tires of it now."

    a "I’ll head over there, then. See you guys soon."

    "The park, huh? That makes sense. I just hope not too many families got the same idea."
    jump epilogue_anime_route

label reuinion:
    $ arline_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Arline/Epilogue/Reunion/Arline_Epilogue_Reunion_"
    $ skylar_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Skylar/Reunion/Skylar_Epilogue_Reunion_"
    $ salem_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Salem/Reunion/Salem_Epilogue_Reunion_"

    scene bg mainstreet_afternoon with fade

    "Now that I’m alone again, I throw myself back into looking for the others. If only there were fewer people around…"

    vl salem_vl_prefix 1
    ymv "Yo, over here!"

    "I’d recognize that voice anywhere. Salem is waving at me. Mother’s seated on a bench, and Skylar’s standing at her side."
    "I rush over to them."

    a "There you are."

    "Mother rises from the bench, drawing me into an embrace."

    if eval(a.name)[0] == "Alexis":
        vl arline_vl_prefix 1-A
    else:
        vl arline_vl_prefix 1-N
    arline "Congratulations. I’m so proud of you, [a]. My baby, graduating from MIA of all schools."

    "When she releases me, Skylar and—with great reluctance on his part—Salem give me hugs of their own."

    vl skylar_vl_prefix 1
    sky "With only one year, too. I’m definitely going to need your help with my summer homework."

    vl salem_vl_prefix 2
    salem "What, can’t do it yourself?"

    vl skylar_vl_prefix 2
    sky "At least I do it."

    vl arline_vl_prefix 2
    arline "Salem? You are doing your homework, right?"

    vl salem_vl_prefix 3
    salem "She’s just talking out her ass, mom."

    vl skylar_vl_prefix 3
    sky "How vulgar."

    a "Same as always, huh?"

    vl arline_vl_prefix 3
    arline "I got us reservations for a restaurant in the capital. It’s later tonight, but I thought we could tour the city a bit."

    a "Really?"

    "I take a step closer so I can whisper into her ear."

    a "Are you sure? The accounts…"

    vl arline_vl_prefix 4
    arline "For your graduation, a little splurging is worth it. We’ll figure it out."

    vl salem_vl_prefix 4
    salem "Keeping secrets, are we?"

    a "Don’t worry about it."

    #"This section of the finale only happens if: 1) The player was on a route where they could be confessed to (Alexis-F on Killian, Alexis-M on Elio, etc), and 2) they didn’t reject it."
    #"Otherwise, skip to the end, where they leave."

    if sue_romance or reina_romance or lucas_romance or killian_romance or naomi_romance or elio_romance:
        "Now that I think about it, before we head out, there’s something I should probably do…"

        a "Actually, there’s someone I want you guys to meet. I need to make a call. Wait here a minute."

        $ renpy.jump("reuinion_" + chosen_club + "_route")
    else:
        jump finale
    #jump route_branch_point7

label route_branch_point7:
    if sue_romance:
        jump reunion_no_clubs_route
    elif reina_romance:
        jump reuinion_disciplinary_route
    elif lucas_romance:
        jump reuinion_literature_route
    elif killian_romance:
        jump reuinion_anime_route
    elif naomi_romance:
        jump reuinion_home_ec_route
    elif elio_romance:
        jump reuinion_archery_route
    else: 
        jump finale 



label finale:
    $ arline_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Arline/Epilogue/Finale/Arline_Epilogue_Finale_"

    "We talk for a while longer. Then Mother urges us to get a move on so we can spend at least a little time touring the capital before dinner like she wanted us to."

    "The few suitcases I brought with me go with us on the bus down south."
    "A small part of me was hoping that we’d have to come back up to grab my things, but they’ll be sitting in a hotel room until we head back home."

    "So the view of Huntsdale as the bus pulls away is the last one I see of the town. At the very least, the last one I’ll see for a long time."

    vl arline_vl_prefix 1
    arline "I’m sure you’ll get a chance to see everyone again someday."

    a "You’re right. Just still stings a bit to say goodbye."

    "For all his teasing, Salem puts a comforting hand on my shoulder. Skylar, seated on my other side, takes my hand. My breath hitches in my throat."

    a "But this does make it a little bit easier."

    "Like the headmaster said, one chapter of my life has ended, and another has begun."
    "But even with the changes that will come starting tomorrow, at least I know that the people who helped me out this year will still be there for me, and me for them."
    call screen end_screen

return