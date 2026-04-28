label swordplay_route_jinus(month, date):
    $ ylva_vl_prefix = "audio/voices/Friends/Ylva/Month 1/Ylva_Month1_"

    call screen calendar(month, date, "Jinus", 27)
    scene bg wright_gymnasium_afternoon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Ylva - \nUctday, Jinus 27, 1027 RD")
    
    "It’s been a few weeks since the school year started, and a few weeks since I first swung by the Swordplay Club. I am not very good. Seeing just how much all the other fresh faces are struggling makes it feel a little less embarrassing, at least."
    "The way some of the others move, there’s no way that the extent of their practice is a few hours after school once a week. These are people that take their swordsmanship seriously."
    "Most of all, Ylva is out of this world. After yet another set of conditioning swings, I’m taking a break when I see her facing down three people at once. They’re some of the more experienced club members, and she’s still making it look easy."
    "Just like during her little match with Said, she’s making use of that trick where her sword and stick become a spear to manipulate the distance between her and her opponents."
    
    a "And she’s the Vice Captain?"
    
    anek2 "I know, right?"
    
    "When her opponents are either disarmed or laid out on the ground, the club members who weren’t busy offer a small round of applause. Ylva’s taking a drink when I go up to her."

    show ylva warm club at center with dissolve
    a "Mind if I give you a whirl? After your break."
    
    vl ylva_vl_prefix 1
    yl "Not at all."
    
    "She screws the cap on her water bottle and picks up her weapons."
    
    a "Hold on—"
    
    stop music fadeout 1.0
    vl ylva_vl_prefix 2
    yl "I’m not tired, if that’s your concern. Come."
    
    play music hatchling8_2 fadein 1.0
    "I follow her back onto the floor, assuming a ready stance mirroring her own. If the genuine blades aren’t dulled, there are guards for them to keep us from maiming each other."
    "Yet the gleaming steel peeking through the thick, tightly bound leather sends my heart into a frenzy. Something I apparently let show in my face."
    
    vl ylva_vl_prefix 3
    yl "Are you sure about this?"
    
    a "Very."
    
    vl ylva_vl_prefix 4
    yl "Then come at me."
    
    "And come at her I do. My assault is unrelenting, but no matter what I do, I just can’t find a gap in her guard. And guard is the only thing she does."
    "I don’t know if Ylva’s going easy on me. I don’t know if I want her to go easy on me. But her being on the defense feels wrong."
    "As I raise my sword to strike again, she jabs me in the side with her stick. In the moment I take to process the sting of the blow, she swats my sword out of my hand, the wooden thing clattering against the gym floor a short distance away."
    stop music fadeout 1.0
    "My leaden arms drop to my side, only a moment before I drop onto my behind."
    play music hatchling1 fadein 1.0

    vl ylva_vl_prefix 5
    yl "You still tire too easily. Practically handed me the match."
    
    "She helps me to my feet and offers me a drink."
    
    a "That explains why you let me have at it."
    
    vl ylva_vl_prefix 6
    yl "Better luck next time."
    
    a "And you are the Vice Captain, right?"
    
    "She nods. I scan the room, but I don’t see anyone that seems half as skilled as her."
    
    a "Then where’s the real deal?"
    
    anek2 "Busy with work, probably."
    
    a "Work? At a school like this?"
    
    "Figures that some people at a school like this would need to work on the side to cover the costs, but…"
    
    anek2 "It’s definitely not what you’re thinking."
    
    vl ylva_vl_prefix 7
    yl "He’s an Overseer Initiate."
    
    a "Come again?"
    
    "Everyone knows Overseer. The All-Seeing Eye badge of the international police is one of the most iconic symbols on Unios. But an Initiate, not a Prospect? That means they already decided this guy was worth bringing on full time."
    
    a "So he’s enough to give even you a run for your money, Ylva?"
    
    vl ylva_vl_prefix 8
    "She and the other person with us both laugh."
    
    vl ylva_vl_prefix 9
    yl "I’ve never beaten him."
    
    a "You don’t seem to mind it much."
    
    vl ylva_vl_prefix 10
    yl "I don’t. It just means that I still have room to improve."
    
    "She glances over at a clock hanging high on the gym’s walls."
    
    vl ylva_vl_prefix 11
    yl "We’re just about out of time."
    
    "She turns to the senior club member with us."
    
    vl ylva_vl_prefix 12
    yl "Could you help me get everyone under control?"
    
    anek2 "No prob. See you around, [a]."
    
    a "Later."
    
    scene bg mainstreet_afternoon with fade

    "I exit The Amity, nibbling on a snickerdoodle. On my way back to House Lychester, I decided to make a quick stop for a snack. And with how good the thing is, it was definitely the right choice."
    "I’m still a long ways away from being able to put names to faces, but several of the people I pass on the street at least tickle my brain in some way. Like I’m close to being able to recognize them, but not there just yet."
    "The long platinum blonde hair of the girl ahead of me, though, is impossible to mistake. I hasten to catch up to her."
    stop music fadeout 1.0
    
    a "Ylva!"
    
    play music hatchling14 fadein 1.0
    show ylva neutral at center with dissolve
    "The look she gives me when she stops and glances over her shoulder stops me cold. None of the warmth I’ve grown used to seeing in her during club is there."
    
    a "…Hey?"
    
    vl ylva_vl_prefix 13
    yl "What do you want?"
    
    "Where did this attitude come from? Did I say something to upset her?"
    
    a "I just wanted to talk."
    
    vl ylva_vl_prefix 14
    yl "And I have somewhere to be."
    
    a "So do I. We could always walk and talk."
    
    vl ylva_vl_prefix 15
    yl "Nor do I have any desire to speak with an imperial."
    hide ylva with dissolve
    
    "She stalks off, not even giving me a chance to reply."
    "\"Imperial\"? And the way she said it was so… cold."
    "I sigh and continue eating my snickerdoodle. Next time I see her, I’m going to have to try and clear that up. Next club meeting, perhaps? Maybe she’ll be in a better mood then."
    stop music fadeout 1.0

    call swordplay_route_dallinus("Jinus", 27) from _call_swordplay_route_dallinus

label swordplay_route_dallinus(month, date):
    $ goude_vl_prefix = "audio/voices/Supporting-Extra/Isaiah/Ylva/Month 2/Isaiah_Ylva_Month2 - _"
    $ ylva_vl_prefix = "audio/voices/Friends/Ylva/Month 2/Ylva_Month2_"

    call screen calendar(month, date, "Dallinus", 9)
    scene bg wright_gymnasium_afternoon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Ylva - \nUctday, Dallinus 9th, 1027 RD")

    show ylva warm club at center with dissolve
    vl ylva_vl_prefix 1
    yl "And that’s that!"

    "It took a little while, but clean up after today’s club meeting is finally over."
    
    anek2 "Alright, time to get out of here. I’m starving."
    
    "Not many of us stuck around to help. The already thin crowd grows even thinner. As someone goes out the door, a pair of people I wasn’t expecting to see come in."
    
    show ylva warm club at character_pos1 with moveinright
    show reina neutral at character_pos4 with dissolve
    vl ylva_vl_prefix 2
    yl "Sir Goude, Lady Reina, welcome. I wasn’t expecting to see the two of you here."
    
    r "Good afternoon, Ylva. And to the rest of you as well."
    
    vl goude_vl_prefix 1
    h "Just doing a quick sweep of the campus, making sure everything is in order. Had another eventful club meeting, Lady Ylva?"
    
    vl ylva_vl_prefix 3
    yl "I think the Mother would denounce her children before the day I find one of our meetings boring!"
    
    a "Um…"
    
    "The three of them turn to me. I have been silent up until this point, so I guess I surprised them."
    
    a "Oh, uh… I just noticed something about Ylva. I don’t think I’ve heard anyone at this school use titles like \"Lord\" or \"Lady,\" other than her."
    
    r "It isn’t just her formality that confuses you, but people saying it back to her, I assume?"
    
    a "Sort of. Just being respectful, maybe?"
    
    vl goude_vl_prefix 2
    h "That’s part of it, but it’s also a statement of fact. House Brandt is very important in Ekaska."
    
    "I turn to Ylva."
    
    a "You’re nobility?"
    
    "The few senior club members still hanging around laugh."
    
    anek2 "Oh, she’s more than just plain old nobility, buddy."
    
    show ylva bashful club
    "Ylva suddenly looks embarrassed."
    
    yl "M-my older brother is the head of King Emil’s personal guard…"
    vl ylva_vl_prefix 4
    
    a "Personal guard? Of the king?"
    
    "There’s another round of laughter."
    
    anek2 "That’s how we all reacted when we found out, too."
    
    "The headmaster checks his watch."
    
    vl goude_vl_prefix 3
    h "Well, we have a quick inspection to do, and don’t want to keep you any longer. Good day, everyone."
    
    scene bg wright_gymnasium_afternoon with dissolve
    stop music fadeout 1.0
    "Most everyone else does leave, but a small group of us remains behind, talking about nothing, while the headmaster and Reina go about their work. When they’re done, I expect them both to leave, but Reina stays behind."
    play music hatchling15 fadein 1.0
    show reina neutral at character_pos6 with dissolve
    show ylva warm club at character_pos3 with dissolve

    "Then I remember how we met. And what Ylva’s wearing. Oh boy."
    "Anticipating the clash to come, the group breaks up into smaller pairs and trios."
    
    r "Ylva, we have been over this. What you’re wearing is a gross violation of the dress code."
    
    show ylva neutral club
    vl ylva_vl_prefix 5
    yl "And this dress code is older than any of us, our parents, or our grandparents. Why should I heed something so ancient?"
    
    r "Because so long as the dress code is part of the school’s official rules, how old it is and how we feel about it mean nothing. We must respect it."
    
    "Ylva crosses her arms. I recognize this look. It’s the same one she gave me last month when I ran into her out on the street."
    
    vl ylva_vl_prefix 6
    yl "Of all the ways to waste your time…"
    
    r "Excuse me?"
    
    vl ylva_vl_prefix 7
    yl "Look at yourself. A Roma, halfway across the world from her home, chastising a girl for her decision to wear slacks over a skirt."
    
    show reina worried
    r "I’m not \"halfway across the world from home.\" Magiana is the only home I’ve ever known. And don’t try to change the subject. My being Roma is irrelevant."
    
    vl ylva_vl_prefix 8
    yl "\"Home,\" she says! Your ancestors abandoned their true home and grew fat on the gifts of a foreign king."
    
    r "We came with naught but the clothes on our backs and were rewarded for loyalty and service to our adopted homeland."
    
    "Reina maintains her composure—evidently with great effort—but she’s more exasperated than I’ve ever seen her."
    
    r "You swing around a massive glaive like a brute, wear slacks and spit all over rules and tradition, and disparage a woman’s family right to her face. You have none of the poise and dignity befitting a lady of your station!"
    
    "That was one of the most hoity-toity insults my ears have had the pleasure of hearing. But with the darkness that’s suddenly settled on Ylva’s face, it clearly struck a nerve I don’t have."
    
    show ylva angry club
    vl ylva_vl_prefix 9
    yl "Nor do you have any of the pride befitting a Roma! Lady Reina, your forefathers ran away from home, and you try to defend it by using sweet words like \"loyalty\" and \"service.\""
    vl ylva_vl_prefix 10
    yl "I suppose I shouldn’t be surprised. You Roma have a habit of running away from home. The Ajak are still waiting for their wayward children to come crawling back."
    
    show reina confused
    "After Ylva’s comment, everyone carrying on their conversations on the periphery of this all fall silent and turn to the two."
    
    anek2 "Oh no."
    
    show reina worried with dissolve
    "Tears suddenly well in Reina’s eyes."
    
    r "How dare you!"
    
    "I’m terrible with history, but even I know Ylva’s gone too far. Oslein, where the Roma are from, is north of Osma. The Ajak tribe in northern Osma say the Roma are some of them that went north centuries ago and struck out on their own."
    "The Osman government stands by that claim, but nowhere else in the world does. And the Roma themselves hate it."
    "Everyone’s stunned into silence, but seeing Reina there, on the verge of tears, I can’t sit on the sidelines any longer. I approach her, deliberately blocking her view of Ylva."
    
    a "Would you like me to walk you outside?"
    
    "She sniffles and nods."
    
    r "That would be much appreciated."

    hide ylva with dissolve
    stop music fadeout 1.0
    scene bg wright_field_afternoon with fade
    play music hatchling10 fadein 1.0
    show reina flustered at center with dissolve
    
    "Once outside, Reina fishes a handkerchief out of her skirt pocket and dabs at her eyes."
    
    r "I am sorry you had to see me lose my composure like that."
    
    a "\"Lose your composure\"? Reina, do you have any idea how composed you looked to me?"
    
    show reina neutral with dissolve
    "The smallest of smiles creeps onto her face."
    
    r "I suppose I don’t."
    
    a "But I’m sorry you had to hear that. I don’t know what came over her."
    
    r "Don’t apologize for her boorish behavior. You didn’t do anything wrong."
    
    "More of the others come outside, offering quick apologies of their own to Reina. They don’t stop to give her a chance and address them, so she just gives them little nods of acknowledgement."
    
    a "Need me to walk you somewhere?"
    
    r "I’ll be fine. But thank you for the offer. Take care, [a]."
    hide reina with dissolve
    
    "She leaves me, and I take a deep breath before heading back inside."

    scene bg wright_gymnasium_afternoon with fade

    show ylva neutral club at center with dissolve
    "Ylva’s engaged in some rather rigorous drills, trying to blow off steam."
    
    a "What in the Abyss was that?"
    
    vl ylva_vl_prefix 11
    yl "She insulted me."
    
    a "After you insulted her family first. What you said was bigoted and wrong, Ylva."
    
    "She stops her drills, turning away from me. That’s about as clear a dismissal as I could get. I sigh and leave her. Right on my way out the door, though, I hear her whisper something to herself."
    
    vl ylva_vl_prefix 12
    yl "Of course I know that…"
    hide ylva with dissolve
    stop music fadeout 1.0

    # jump to main club route dallinus
    $ renpy.call(chosen_club + "_route_dallinus", "Dallinus", 9)
    #jump swordplay_route_dyalt

label swordplay_route_dyalt(month, date):
    $ ylva_vl_prefix = "audio/voices/Friends/Ylva/Month 4/Ylva_Month4_"

    call screen calendar(month, date, "Dyalt", 9)
    scene bg wright_gymnasium_afternoon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Ylva - \nUctday, Dyalt 9th, 1027 RD")

    "I don’t believe I’ve ever gotten a chance to appreciate the rafters of the gym. They’re actually quite nice. And, if it was stay up all night or lay on the floor like I am right now, I could see myself doing the latter. More comfortable than I would’ve imagined."
    
    show ylva warm club at center with dissolve
    vl ylva_vl_prefix 1
    yl "Why are you just lying there?"
    
    "Ylva looms over me, perplexed."
    
    a "Just being dramatic."
    
    "She pulls me to my feet. Once again, I’ve challenged her and lost. Not like I stood a chance, but it still stings a bit. And not just my leg after she smacked it with her stick."
    
    vl ylva_vl_prefix 2
    yl "Keep trying. Maybe you’ll have me beat by year’s end."
    
    a "I hope so. That’s going to be the last chance I have."
    
    "I move off to the side and sit against the wall to catch my breath. Ylva joins me, taking the chance to have some water. We stop by a few of the others, leaning or sitting against the wall."
    
    anek2 "Any news on how prep for the Revolution Festival’s going, Ylva?"
    
    vl ylva_vl_prefix 3
    yl "Splendidly, from what I hear. A fine group of young ladies this time around."
    
    a "Revolution Festival? I thought Ekaska was still a monarchy."
    
    "The member of the club who asked looks down at me."
    
    anek2 "It is. Some sort of big festival they  have in the winter."
    
    vl ylva_vl_prefix 4
    yl "A new year’s festival, to be exact. It all ends with a dance put on by our women and girls."
    
    "She starts to play with her necklace."
    
    vl ylva_vl_prefix 5
    yl "We’re considered adults at 15. We get them throughout our lives, but the Sign of Solaris we get then is extra special. The Revolution Festival is a young woman’s first major social function. Then the women newly engaged, newly married, new mothers…"
    vl ylva_vl_prefix 6
    yl "No matter the phase of her life, a woman is free to participate, but those major milestones are the main ones."
    
    a "Have you ever danced in it, Ylva?"
    
    vl ylva_vl_prefix 7
    yl "Only my first opportunity, after my 15th birthday. But I hope to dance again soon."
    
    anek2 "When you’re back home for the Week of Life?"
    
    vl ylva_vl_prefix 8
    yl "Too out of practice. But maybe for the 1029 Revolution Festival."
    
    anek2 "Man, I’d love to see that. Only if airship tickets weren’t so damn expensive."
    
    "They take up their wooden sword and push off of the wall."
    
    anek2 "I’m getting another round or two in. See you."
    
    "In the silence that follows, Ylva finishes drinking her water. Here we are, in our own little corner of the gym, no one paying any attention to us. I figure she’ll be back to it herself soon."
    stop music fadeout 1.0
    "And if she does, I’d have squandered a perfect chance to have an important talk."
    play music hatchling10 fadein 1.0
    
    a "Hey, Ylva."
    
    vl ylva_vl_prefix 9
    yl "Yes?"
    
    a "About what happened with Reina a few months ago…"
    
    show ylva neutral club
    vl ylva_vl_prefix 10
    yl "What about it?"
    
    a "Do you actually believe the things you said?"
    
    "It takes her a while to answer. That isn’t exactly comforting."
    
    vl ylva_vl_prefix 11
    yl "I stand by what I said about the Dreyar family abandoning their homeland and cozying up to a foreign king."
    
    a "But it isn’t like they don’t care about other Roma. Even if they don’t live in Oslein. The Mortal Coil Foundation’s proof of that."
    
    "She nods."
    
    vl ylva_vl_prefix 12
    yl "Her father’s philanthropy is the thing propping up the respect I do have for them."
    
    a "And the other thing you said?"
    
    "More silence."
    
    vl ylva_vl_prefix 13
    yl "Like I said back then, she insulted me."
    
    a "That’s just an excuse."
    
    voice "<to 2>audio/voices/Friends/Ylva/Month 4/Ylva_Month4_14.ogg"
    yl "I know it is!"
    
    "Up until this point, she’d been standing. She slides down the wall to sit beside me."
    
    voice "<from 2.3>audio/voices/Friends/Ylva/Month 4/Ylva_Month4_14.ogg"
    yl "I was just hurt, and I lost myself in the moment."
    
    "I rack my brain, trying to recall that day and what it was Reina had said to set Ylva off. I remember \"brute\" and \"skirt\"..."
    
    a "Because she was saying you weren’t acting like a lady? That’s what set you off?"
    
    show ylva bashful club
    "She turns away from me, but not quickly enough. I noticed that blush creeping across her cheeks."
    
    a "I… wasn’t expecting that."
    
    vl ylva_vl_prefix 15
    yl "Most people aren’t. But I am a lady, so…"
    
    "I sigh. It is easy to forget Ylva isn’t a fourth-year. But times like this really hammer it home that she’s just a 17-year-old girl, at the end of the day."
    
    a "You don’t hate Reina. I remember you calling her \"Lady,\" even when you were angry."
    
    vl ylva_vl_prefix 16
    yl "How could I hate someone like her?"
    
    a "So when are you planning on apologizing to her?"
    
    vl ylva_vl_prefix 17
    yl "When my heart is ready."
    
    a "And that will be…?"
    
    vl ylva_vl_prefix 18
    yl "When it is ready."
    
    "Again, I sigh. Guess you can’t force these sorts of things. At least she knows it needs to happen. I rise to my feet, ignoring the stinging in my leg."
    
    a "Well, if I’m ever going to beat you, I need to get better. Time to find someone to spar with."
    
    hide ylva with dissolve
    "I wave, but she isn’t looking at me, still turned away to hide her embarrassment. Hopefully I won’t have to play mediator, but only time will tell what’s in store for Ylva and Reina."
    stop music fadeout 1.0

    # jump to main club route dyalt
    $ renpy.call(chosen_club + "_route_dyalt", "Dyalt", 9)
    #jump swordplay_route_neralt

label swordplay_route_neralt(month, date):
    $ ylva_vl_prefix = "audio/voices/Friends/Ylva/Month 5/Ylva_Month5_"

    call screen calendar(month, date, "Neralt", 26)
    scene bg student_councilroom_afternoon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Ylva - \nZynday, Neralt 26th, 1027 RD")

    show sue neutral at character_pos2 with dissolve
    show reina neutral at character_pos5 with dissolve
    "A Student Council meeting wrapped up not too long ago. The only ones remaining in the Council’s room are myself, Reina, and Sue. Reina is seated at her desk, working through a stack of documents. Suddenly, without warning, she rises."
    
    show reina sickly
    r "If you’ll excuse me."
    show reina sickly at right with moveinleft
    s "Of course."
    
    "She takes her bag and crosses over to the door, glancing over her shoulder at us."
    
    show reina sickly at character_pos5 with moveinright
    r "I’ll be heading up to the salon. Would either of you care to join?"
    
    "As much as I’d like to, I have been letting an awful lot of homework pile up. So I guess I’m going to have to—"
    
    s "We’d love to. When we’re done, we’ll meet you upstairs."
    
    show reina neutral
    "A smile creeps onto Reina’s face, and she gives Sue a little nod."
    
    r "I’ll be looking forward to it. But do take your time."
    
    hide reina with dissolve
    show sue neutral at center with move
    "She’s barely closed the door behind her before I speak."
    
    a "\"We\"?"
    
    s "Yes, we. There’s something that needs to be done, and I doubt I can do it alone."
    
    a "You need me for something?"
    
    s "You’re acquainted with Ylva Brandt, yes? At the very least, I’m pretty sure you’re in her club."
    
    "So that’s what this is about."
    
    a "Is something up with Reina?"
    
    s "The quality of her work has been slipping. I’ve heard about what happened between them, and it started around then."
    
    a "Ylva hasn’t apologized yet? That girl…"
    
    "I shake my head."
    
    a "So what’s the plan?"
    
    s "We find Ylva, drag her to the salon, and chaperone her and Reina like the children they are."
    
    "I wince. Even though there was an almost inappropriate lightness to Sue’s tone."
    
    s "Her club isn’t meeting today, but I wouldn’t be surprised if she got in a workout anyway. She’s probably gone to her dorm to rest."
    
    "Sue stands, her work also noticeably incomplete."
    
    a "Getting right to it, are we?"
    
    s "The sooner we get them together the better, right?"
    
    "I can’t argue with her there."

    scene bg mainstreet_afternoon with fade

    "Sue and I wait outside in front of House Sloane. Just as Sue suspected, it’s only a matter of time until Ylva comes by. She perks up when she notices the two of us."

    show sue neutral at character_pos3 with dissolve
    show ylva warm at character_pos6 with dissolve
    
    if eval(a.name)[0] == "Alexis":
        vl ylva_vl_prefix 1.1
    else:
        vl ylva_vl_prefix 1.2
    yl "Lady Sue, [a], it’s good to see you. Funny place to be hanging around."
    
    s "Hanging around without a purpose, yes."
    
    "Sue nods in my direction, and I step forward."
    
    a "Ylva, is your heart ready?"
    
    "For a moment, she’s confused. Then she begins stammering wildly."
    
    show ylva bashful with hpunch
    vl ylva_vl_prefix 2
    yl "I-i-it’s happening already?!"
    
    a "Ylva, it’s been a month since you told me you’d apologize when you’re ready. Well, are you?"
    
    vl ylva_vl_prefix 3
    "Ylva looks behind me to Sue, in some vain attempt to find relief. When it’s clear she won’t find any, she instead steadies herself and takes several deep breaths."
    
    show ylva neutral
    vl ylva_vl_prefix 4
    yl "Not fully, no. But it isn’t like I have much choice, do I? Bring me to her."
    
    scene bg wilson_salon_afternoon with fade

    "Our walk back to the Wilson Building and up to the salon was silent, Ylva trailing behind Sue and I the entire time. I can only imagine what’s going through her head as we make our way."
    "Sue is the first of us to enter the salon."

    show sue neutral at character_pos4 with dissolve
    s "Sorry for the wait, Reina. We’re here."
    
    "Seated by a window with her back to us, a gleeful Reina looks our way, her smile quickly erased at the sight of Ylva. In an instant, her face is composed and dignified."

    show reina neutral at character_pos1 with dissolve
    show ylva neutral at character_pos7 with dissolve
    "Ylva takes a seat directly across from Reina, Sue and I between them. There’s a long moment of silence."
    stop music fadeout 2.0
    with vpunch
    "Then Ylva plants her hands on the table and bows her head so deeply she nearly slams it into the table."
    play music hatchling10 fadein 1.0
    
    show ylva bashful
    show reina confused
    vl ylva_vl_prefix 5
    yl "What I said to you in Dallinus was disgusting and wrong."
    vl ylva_vl_prefix 6
    yl "I will only speak true to you. I have misgivings with how your family came to this nation, but I admire you and your father’s efforts to give back to the Roma of the world."
    vl ylva_vl_prefix 7
    show reina worried
    yl "And I didn’t believe a word of my comment about the Ajak. I said it only because I knew it would hurt. And for that, you have every right to loathe me."
    vl ylva_vl_prefix 8
    yl "I simply want you to know that I am sorry, regret what I said, and owe you an additional apology for not coming to you sooner."
    
    "We are again plunged into silence. My eyes flit between Ylva, her head still bowed, and Reina, who looks down on her impassively. Sue doesn’t share any of my trepidation."
    
    show reina neutral
    r "Raise your head."
    
    "Ylva does as she’s told. Upon seeing the penitent look on her face, Reina’s expression softens."
    
    r "Your apology is accepted. What you said wounded me deeply, but it would be unladylike of me not to commend you for this humility you’ve shown in apologizing."
    
    "She glances at Sue and I."
    
    r "Even if you needed to be escorted."
    
    "Her shoulders slump ever so slightly."
    
    show reina worried
    r "I owe you an apology as well. Saying you’re not acting like a lady because you’re a warrior and not in skirts, honestly."
    
    "Reina sighs and shakes her head."
    
    r "I truly am my father’s daughter."
    
    stop music fadeout 1.0
    "Sue clasps her hands together."
    play music hatchling1 fadein 1.0
    
    show sue happy
    s "And thus, peace was made! To celebrate, how about some drinks and snacks?"
    
    a "Sounds good to me. Ladies?"
    
    vl ylva_vl_prefix 9
    yl "If you’ll have me."
    
    show reina happy
    r "The more the merrier, as they say. Garçon, over here, please."
    
    "A sheepish Ylva quietly nurses her drink once it arrives, not speaking up unless spoken to. We’re able to stay for a few hours, and it’s only when we’re ready to leave that she really starts to open up."
    "By the time we say our goodbyes, she’s able to offer a small wave."
    hide ylva with dissolve
    hide sue with dissolve
    show reina neutral
    "I end up side by side with Reina, since we’re heading to the same place."
    
    show reina neutral at center with moveinleft
    a "How’re you feeling?"
    
    r "A bit better. Thank you. Even if it was just dragging her to the salon."
    
    a "Just glad to know it all worked out."
    
    "At least it seems like a weight has been lifted from both of their shoulders. All’s well that ends well."
    stop music fadeout 1.0

    call student_council_exalt("Neralt", 26) from _call_student_council_exalt_3
    #jump swordplay_route_exalt
    
label swordplay_route_exalt(month, date):
    $ ylva_vl_prefix = "audio/voices/Friends/Ylva/Month 6/Ylva_Month6_"

    call screen calendar(month, date, "Exalt", 21)
    scene bg weaver_library_afternoon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Ylva - \nLenday, Exalt 21st, 1027 RD")

    "The second trimester is just about done. And with it comes exams next week. Just as I thought, the library’s packed with people trying to get in the right headspace to study so they don’t crash and burn once those accursed tests are in front of them."

    scene bg weaver_library_second_location_afternoon with fade
    
    "Thankfully, the deeper into the library I go, the less crowded it is. Most of the little study tables here seat two, but only have one occupant, if they have any at all."
    "It makes the most sense for me to sit at one of the empty ones, but when I spy Ylva, I can’t help but go up to her."
    
    a "Mind if I take a seat?"
    
    "She looks up at me, brow furrowed. A moment later, she shrugs."
    
    show ylva neutral at center with dissolve
    vl ylva_vl_prefix 1
    yl "Feel free."
    
    "I sit and take out my study materials. We pass the time, working on our own things, enjoying the companionable silence. The turning of a page and the sound of pencil on paper are all there is to accompany us."
    "Until I speak up."
    
    a "Winter’s almost over, but it's as cold as ever, huh?"
    
    vl ylva_vl_prefix 2
    yl "Please, this is nothing. You should try a night in Ekaska in the deep winter. Those are bad."
    
    vl ylva_vl_prefix 3
    "She shivers."
    
    a "But the hot springs are supposed to help, right? Ekaska’s famous for them, isn't it?"
    
    show ylva warm
    vl ylva_vl_prefix 4
    yl "Rightfully so. You won’t find better hot springs anywhere on Unios."
    
    a "The most I’ve ever seen of them is postcards. Or the odd video here and there."
    
    vl ylva_vl_prefix 5
    yl "Everyone should try to visit, at least once. The City is a marvel in and of itself, but Brasan has its own unique charm."
    
    a "I’m guessing those are places?"
    
    vl ylva_vl_prefix 6
    yl "We are only one island, so it isn’t like we have many settlements. Brasan is on the western side of the island. It’s the second biggest city."
    
    a "And \"The City\" is the capital?"
    
    vl ylva_vl_prefix 7
    yl "To the rest of the world, it’s \"Säkerhet,\" but to us, it’s just \"The City.\""
    
    a "It’s not just those two, is it? Only two cities is a bit…"
    
    vl ylva_vl_prefix 8
    yl "There’s also Stendamm, in the island’s center. Just a small mining town, though."
    
    "It’s my turn to furrow my brow. The confusion etched into my face gets a laugh out of her."
    
    vl ylva_vl_prefix 9
    yl "Let me guess. \"How could such a tiny island be such an important country?\""
    
    a "Felt a little inappropriate to say out loud, so thanks for doing the hard part for me."
    
    vl ylva_vl_prefix 10
    yl "The fish caught in Ekaskan waters are some of the best in the world. Especially in the summer. Then there’s the fact that anyone that wants to sail across the Western Ocean is going to need somewhere to restock. And did I mention the manite?"
    
    stop music fadeout 1.0
    a "Stendamm?"
    
    show ylva adoration
    "Ylva’s grin widens. She’s absolutely glowing with pride."
    play music hatchling22 fadein 1.0
    
    vl ylva_vl_prefix 11
    yl "Home to one of the oldest manite mines in the world."
    vl ylva_vl_prefix 12
    yl "Oh, and then there’s the animals!"
    
    "As I try to wrap my brain around what could be so great about them, she takes out her phone and scootches her seat a bit closer to mine."
    
    vl ylva_vl_prefix 13
    yl "Here, look."
    
    "She shows me a video, the subject of which makes me flinch at first. A white wolf—the biggest I’ve ever seen, with a bloodied muzzle—comes speeding out of a forest, dashing through the snow."
    "A man is standing, arms outstretched, and begins crying for the creature to stop before it tackles him to the ground."
    "The laughs that suddenly break out are Ylva behind the phone. She calls the wolf to her and it hurries over, nuzzling its head against her hand. She’s saying something about the hearty meal it must’ve had."
    
    vl ylva_vl_prefix 14
    yl "Isn’t my Siggy just the cutest thing?"
    
    "I’m stunned into silence. Frowning at the delay in my affirmation of her beast’s adorability, Ylva draws back."
    
    show ylva neutral
    vl ylva_vl_prefix 15
    yl "You imperials are so weird, with your obsessions with tiny furballs like cats and dogs. If you ever met my little Siggy, it would be love at first sight. So what if he's a giant wolf?"
    
    a "Um, it isn’t like he isn’t cute! I was just caught off guard."
    
    vl ylva_vl_prefix 16
    yl "Sure you were."
    
    l "Everything going alright over here?"
    
    "Lucas pokes his head into our little alcove. He was introduced to me as the temp librarian. Only makes sense that he’d wander around making sure everything was in order."
    
    show ylva neutral at character_pos2 with move
    show lucas neutral at character_pos6 with moveinright
    a "I’m alright. Sorry if we were being loud."
    
    stop music fadeout 1.0
    "I look to Ylva, expecting her to echo the apology, but instead I find her glowering at Lucas."
    play music hatchling15 fadein 1.0
    
    vl ylva_vl_prefix 17
    yl "It isn’t like there’s anyone in this part of the library. Who cares if we’re a little loud?"
    
    show lucas annoyed
    l "Your noise carries farther than you’d think. Even if there aren’t many people here, the ones up front will also hear you."
    l "Not like there being few people back here would justify disturbing them with noise."
    
    vl ylva_vl_prefix 18
    yl "Noted. Now leave."
    
    l "I’m sorry if I disturbed you two."
    
    "He turns to leave."
    
    a "Hold it."
    
    vl ylva_vl_prefix 19
    yl "Don’t \"hold it.\" I want him gone."
    
    a "And that’s exactly why I’m asking him to \"hold it.\" He’s just doing his job. You’re being rude."
    
    stop music fadeout 1.0
    "Ylva grumbles, voice too low to make out anything that I’m saying. She turns her head away from Lucas and I."
    
    show ylva bashful with dissolve
    vl ylva_vl_prefix 20
    yl "I apologize. I’ll be more quiet."
    
    show lucas neutral
    l "And I appreciate your efforts."
    
    hide lucas with moveoutright
    "With a nod, he leaves the two of us."

    show ylva bashful at center with move
    a "Was that really so hard?"
    
    "Ylva doesn’t respond. A sigh escapes me. There’s some small comfort in the fact that she didn’t tell me to leave or leave herself. I let us return to our silent studying, hoping that my presence will be a small comfort to her as she calms down."


    #jump to main club route exalt
    $ renpy.call(chosen_club + "_route_exalt", "Exalt", 21)
    #jump swordplay_route_verabris

label swordplay_route_verabris(month, date):
    $ ylva_vl_prefix = "audio/voices/Friends/Ylva/Month 8/Ylva_Month8_"
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Ylva_s Route/Month 8/Gwynette_Ylva_Month8_"

    call screen calendar(month, date, "Verabris", 18)
    scene bg wright_gymnasium_afternoon with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Ylva - \nUctday, Verabris 18th, 1028 RD")

    "The gym is mostly deserted. Club just wrapped up, and most of the cleaning is done, too. A skeleton crew is all that remains to finish the job."
    "Just a little over a month until graduation. Only four or five club meetings left to go. When did the end of the year get so damn close?"
    
    show ylva neutral club at center with dissolve
    vl ylva_vl_prefix 1
    yl "You seem distracted."
    
    "I jump. When did she get here?"
    
    a "Just contemplating my impending graduation."
    
    vl ylva_vl_prefix 2.1
    yl "Fun."
    
    show ylva neutral club at character_pos1 with move
    show gwynette neutral at character_pos4 with dissolve
    show naomi neutral at character_pos7 with dissolve
    vl ylva_vl_prefix 2.2
    "The scuffing of shoes across the gym floor draws my attention over to the door. Gwynette and Naomi just arrived. Not like I know why. And judging by the high-pitched noise Ylva makes behind me, I doubt she did, either."
    
    vl gwynette_vl_prefix 1
    gw "PT, BB, hey!"
    
    n "Good afternoon, you two."
    
    vl ylva_vl_prefix 3
    yl "W-w-what is Naomi-tensei doing here?!"
    
    n "Gwynette invited me out to spend time with her and a friend. Well, more like \"insisted,\" than invited, really…"
    
    a "Well, the more the merrier, right?"
    hide ylva with moveoutleft

    vl gwynette_vl_prefix 2
    gw "Exactly! Hey, why don’t you come with us, BB? We were going to catch a movie at the mall. Or something."
    
    a "Sign me up. Not like I’m doing anything with the rest of the day. Just need to finish up here."
    
    "There isn’t that much left to do, so the wait isn’t long. Once we’re done, I meet the girls by the gym’s exit. I need to stop by House Lychester to freshen up first, so we decide to split up for a bit and then meet up at the mall."
    show ylva neutral club at character_pos1 with moveinleft
    "We’re about to all head out when I notice Ylva’s not with us. She’s still in the middle of the gym floor. My sudden stop gets the other two’s attention."
    
    stop music fadeout 1.0
    vl gwynette_vl_prefix 3
    gw "PT?"
    play music hatchling10 fadein 1.0
    
    "Her hands are at her sides, balled into fists, and the look on her downturned face is some concoction of guilt and pain."
    
    n "Are you alright?"
    
    vl ylva_vl_prefix 4
    yl "I’m a fool…"
    
    a "Where did this come from?"
    
    "She just barely lifts her gaze to look at the three of us."
    
    vl ylva_vl_prefix 5
    yl "I didn’t want to come to this school. The king and my father decided that I would. That it would help to strengthen our relationship with the empire."
    vl ylva_vl_prefix 6
    yl "Ekaska was all I ever knew. Ekaskans were the only people I’d ever known. To be thrown into a sea of outsiders…"
    
    "Even after nearly two years, I guess she’s still adjusting to the new environment. It makes sense, in a weird way."
    "That look she gave me after club back at the beginning of the year, how nasty she was to Reina for hurting her pride, Lucas asking us to just be quiet in the library damn near setting her off."
    "It isn’t just that Ylva’s a fiery girl. It’s because we’re all imperials: \"outsiders.\""
    
    vl ylva_vl_prefix 7
    yl "But here you are, a Magianan, an Estarese woman, and an Aglean drachkin, all inviting me out to spend the evening with you."
    vl ylva_vl_prefix 8
    yl "I never could’ve imagined such a thing two years ago."
    
    "Gwynette strolls back into the gym, Naomi following her. My brain lags for a second before I join them."
    
    vl gwynette_vl_prefix 4
    gw "Then the powers that be were right, right?"
    
    a "And it’s not just us. You’re getting on better with Reina and Sue too, right?"
    
    n "Um, Ylva?"
    
    "She starts, face going bright red at the mention of her name."
    
    n "I know what it’s like, to move to a new country and struggle to fit in, or make friends. I’m glad that you’re starting to realize you’re not alone here, even so far away from home."
    
    "Ylva opens her mouth to reply, but words fail her."
    
    vl gwynette_vl_prefix 5
    gw "Don’t mind her. She’s just a big fan."
    
    n "Of who? I don’t get it…"
    
    "I place a hand on Ylva’s shoulder."
    
    a "Congrats on learning that we’re not all bad. I can say the same about you."
    
    vl ylva_vl_prefix 9
    yl "Was that supposed to be a compliment?"
    
    a "With some of the things I’ve heard you say this year? I wouldn’t blame people for thinking you’re a rabid she-wolf who’d bite their head off if they looked at you the wrong way."
    
    "She rolls her eyes."
    
    vl ylva_vl_prefix 10
    yl "What an original joke."
    
    a "Point is, under that icy exterior, you’re a girl anyone would be lucky to have as a friend. Like how, apparently, you learned that anyone who isn’t Ekaskan isn’t some two-faced snake."
    
    vl gwynette_vl_prefix 6
    gw "And you can pay me back next year by showing me all the hottest spots on the island."
    
    stop music fadeout 2.0
    n "That might be a bit hard, in a place so cold."
    play music hatchling1 fadein 1.0
    
    vl ylva_vl_prefix 11
    "We share a laugh at Naomi’s little joke. Ylva’s considerably lightened up now."
    
    vl ylva_vl_prefix 12
    yl "I’m sorry. It just seems so simple now."
    vl ylva_vl_prefix 13
    yl "I don’t know why I didn’t notice it earlier."
    
    a "Maybe your heart \"wasn’t ready.\""
    
    "She blushes and turns away from me."
    
    vl ylva_vl_prefix 14
    yl "Don’t you have a shower to go take?"
    
    a "Same to you. Gwynette, Naomi, see you two soon?"
    
    vl gwynette_vl_prefix 7
    gw "Right. We’ll probably be in the food court or something, so just look for the singing drachkin. You’ll find us in no time."
    
    scene bg wright_gymnasium_afternoon with dissolve
    "We go our separate ways. My solitary walk back to House Lychester gives me a bit of time to think. I can’t help but wonder if the Ekaskan king and Ylva’s father were looking out for her."
    "Sure, this would look good as a political move, but on a personal one, it’s paid dividends. Ylva’s gone and made friends with people from all over the world, broadening her horizons in ways that would’ve been impossible if she’d just stayed at home."
    "I’ve got to say, I’m impressed. If only I could thank them myself for giving her this unique opportunity to grow as a person. Maybe one day."
    stop music fadeout 1.0

    call student_council_verabris("Verabris", 18) from _call_student_council_verabris_3
    #jump swordplay_route_overa

label swordplay_route_overa(month, date):
    $ phillip_vl_prefix = "audio/voices/Supporting-Extra/Phillip/Ylva/Phillip_Ylva_Epilogue - _"
    $ elio_vl_prefix = "audio/voices/Love Interests/Elio/Ylvas Route/Elio_Ylva_Epilogue_"
    $ gwynette_vl_prefix = "audio/voices/Friends/Gwynette/Ylva_s Route/Epilogue/Gwynette_Ylva_Epilogue_"
    $ vince_vl_prefix = "audio/voices/Friends/Vince/Vincent_Ylva_Epilogue/Vincent_Ylva_Epilogue_"
    $ ylva_vl_prefix = "audio/voices/Friends/Ylva/Epilogue/Ylva_Epilogue_"
    $ said_vl_prefix = "audio/voices/Friends/Said/Said Ylva Epilogue/Said_Ylva_Epilogue_"

    call screen calendar(month, date, "Overa", 19)
    scene bg confession_tree_night with fade
    play music hatchling1 fadein 1.0

    $ renpy.notify("Ylva - \nLenday, Overa 19th, 1028 RD")

    "I don’t quite know why Ylva invited me out to the park at night, but I didn’t have any sort of reason to deny her. She wanted to meet up at the gazebo, but the small army I found when I got there was not at all what I was expecting."
    "One, two… ten other people? Why?"
    
    a "Oh boy."
    
    show vince neutral at character_pos1 with dissolve
    show gwynette neutral at character_pos4 with dissolve
    show sue neutral at character_pos7 with dissolve
    vl gwynette_vl_prefix 1
    gw "Hey, BB."
    
    a "What’s going on here? Where’s Ylva?"
    
    s "Your guess is as good as ours. Some of us here don’t exactly surprise me, but…"
    
    vl vince_vl_prefix 1
    vin "Don’t look at me. Gwyn dragged me here."

    scene bg confession_tree_night with dissolve
    show killian neutral at character_pos1 with dissolve
    show lucas neutral at character_pos4 with dissolve
    show said neutral at character_pos7 with dissolve
    
    k "Same with me and Lucas."
    
    l "Well, I was allowed a plus-one."
    
    vl said_vl_prefix 1
    sa "Must be big thing Ylva planned."
    
    scene bg confession_tree_night with dissolve
    show naomi neutral at character_pos1 with dissolve
    show elio neutral at character_pos3 with dissolve

    n "You can say that again."
    
    vl elio_vl_prefix 1
    e "Bit rude to be late when she’s the one who called us all here, don’t you think?"
    
    r "There’s a good reason for it, I’m sure. Besides, it’s a beautiful night tonight, isn’t it? We may as well enjoy it."
    
    hide elio
    show phillip neutral eyepatch at character_pos7
    vl phillip_vl_prefix 1
    p "Reina is right. A perfectly mild night like this is one to be appreciated."
    
    scene bg confession_tree_night with dissolve
    "I don’t know how long everyone else has been waiting, but I’m not there for too long before Ylva finally arrives, two bulky bags on either shoulder."

    show ylva neutral at character_pos4 with dissolve
    "She freezes when she sees us, face going red."
    
    vl ylva_vl_prefix 1
    yl "I hope I don’t regret inviting this many people…"
    
    "The prince is the first person to approach her."
    
    show phillip neutral eyepatch at character_pos7 with dissolve
    vl phillip_vl_prefix 2
    p "Do you need any help with your bags?"
    
    vl ylva_vl_prefix 2.1
    yl "Oh. Actually, some help with this one would be nice…"
    
    scene bg confession_tree_night with dissolve

    vl ylva_vl_prefix 2.2
    "The bag in question contains a tent. The prince and a few of the others help to set it up. When it’s ready, Ylva takes a breath and turns to address everyone gathered."
    
    show ylva neutral at character_pos4 with dissolve
    vl ylva_vl_prefix 3
    yl "I’m putting on a show for you all."
    
    show gwynette neutral at character_pos1 with dissolve
    vl gwynette_vl_prefix 2
    gw "So that’s why you sent me that song?"
    
    "Ylva nods."
    
    vl ylva_vl_prefix 4
    yl "I would like to dance in next year’s Revolution Festival, but I still need a lot of practice. I wanted a test audience. You felt appropriate."
    
    hide gwynette with dissolve
    "She looks at Reina and the prince."
    
    show phillip neutral eyepatch at character_pos7 with dissolve
    show reina neutral at character_pos1 with dissolve
    vl ylva_vl_prefix 5
    yl "Since we’ll be in Ekaska next year, the President and Vice President of the Council."
    hide phillip with dissolve
    hide reina with dissolve

    "Then to Lucas, Elio, and Killian."
    
    show killian neutral at character_pos1 with dissolve
    show elio neutral at character_pos7 with dissolve
    vl ylva_vl_prefix 6
    yl "People I may have been rude to, or otherwise have closed my heart to."
    hide killian with dissolve
    hide elio with dissolve

    vl elio_vl_prefix Scoff
    "At that, Elio snorts. Then, Ylva turns to the rest of us."
    
    show gwynette neutral at character_pos1 with dissolve
    show said neutral at character_pos7 with dissolve
    vl ylva_vl_prefix 7
    yl "And all of you who’ve done me the honor of counting me among your friends."
    hide gwynette with dissolve
    hide said with dissolve

    vl ylva_vl_prefix 8
    yl "I’ll be a few minutes."
    hide ylva with dissolve
    
    "She retreats into the tent, leaving us to discuss."
    
    show reina neutral at character_pos2 with dissolve
    show phillip neutral eyepatch at character_pos6 with dissolve
    s "Revolution Festival, a show, music? She’s going to dance for us, then? I believe that’s the centerpiece of the event."
    
    vl phillip_vl_prefix 3
    p "That’s what I’ve heard. I haven’t ever seen it myself, though."
    
    scene bg confession_tree_night with dissolve
    show killian neutral at character_pos1 with dissolve
    show lucas neutral at character_pos4 with dissolve
    show elio neutral at character_pos7 with dissolve

    l "I’m sure this is going to be amazing!"
    
    vl elio_vl_prefix 2
    e "You sure about that? She said she needs practice."
    
    k "It’s the effort that counts?"
    
    scene bg confession_tree_night with dissolve
    show said neutral at character_pos2 with dissolve
    show naomi neutral at character_pos6 with dissolve

    vl said_vl_prefix 3
    sa "She is ready."
    
    n "Let’s settle down, everyone!"
    stop music fadeout 1.0
    
    scene bg confession_tree_night with dissolve

    "A moment before the tent flap actually rustles, we settle down. Then Ylva emerges. As she does, music begins to play from Gwynette’s phone."
    # TODO: Update theme to Ylva's
    play music ylvaTheme fadein 1.0
    "The dress she wears is breathtaking. Its gradient of blues and star-shaped silver accents are faintly reminiscent of the Northern Lights."
    "The grand orchestral piece playing in the background accompanies Ylva’s graceful walk to the center of the gazebo and then the beginning of her dance."
    "Her steps are light and deliberate. Each pirouette and twist of her body speak to how much work a person would have to put into perfecting this dance."
    "Watching her bewitches me. It almost feels like each move she makes is some sort of praise or prayer, and the more precise a person is, the more they exalt the stars above and the powers that put them into motion."
    "None of us speaks, simply following her with our eyes as she moves about the gazebo."
    "She returns to its center and begins to spin. One revolution, two, three, again and again she spins, until the fifteenth."
    "Then, coming out of the final spin, she allows herself to fall to her knees, head raised and arms outstretched, venerating the night sky above us."
    stop music fadeout 1.0
    "The music stops, and Ylva’s labored breaths are the only sound for a brief moment. Then we all begin to clap."
    play music hatchling1 fadein 1.0

    show vince neutral at character_pos1 with dissolve
    show gwynette neutral at character_pos4 with dissolve
    show reina happy at character_pos7 with dissolve
    vl gwynette_vl_prefix 3
    gw "Brava, brava!"
    
    vl vince_vl_prefix 2
    vin "That was… amazing."
    
    r "If that was you out of practice, I can only imagine you at your best."
    
    scene bg confession_tree_night with dissolve

    "The praise keeps getting piled on. Ylva flees back into the tent, getting a laugh out of us. When she reemerges, she’s composed herself."
    
    show ylva neutral at character_pos4 with dissolve
    vl ylva_vl_prefix 9
    yl "Thank you for coming."
    
    a "No, thank you for putting this on for us."
    
    "Again, she goes red."
    
    vl ylva_vl_prefix 10
    yl "I… simply wanted to show my appreciation to you all for being a part of my journey at MIA so far. And to send off those of you who will be graduating next week."
    
    show naomi happy at character_pos1 with dissolve
    n "Thank you, Ylva."
    
    "After the tent’s taken down, there’s another round of thanks and congratulations. Then we begin to disperse. Eventually, we’re the only ones left."

    scene bg confession_tree_night with dissolve
    
    show ylva warm at center with dissolve
    vl ylva_vl_prefix 11
    yl "Thank you."
    
    a "What did I do?"
    
    vl ylva_vl_prefix 12
    yl "How do you not know? You’re practically the only reason Lady Sue, Lady Reina, and Lucas were even here."
    
    "I guess I am, huh? If not for my meddling in those situations, she and Reina would still be beefing. And Lucas probably would’ve stalked off furious at Ylva for making noise in the library."
    
    a "Well, you’re welcome."
    
    vl ylva_vl_prefix 13
    yl "I will miss you, you know."
    
    a "Have mercy. I already only have a week. Don’t make it even harder for me to say goodbye to this place."
    
    "Then she does something I couldn’t have ever imagined her doing. She hugs me."
    
    vl ylva_vl_prefix 14
    yl "Be sure to take care of yourself."
    
    a "I will, don’t worry. See you at the last club meeting?"
    
    vl ylva_vl_prefix 15
    yl "Yes. You can get going. I’d like a moment alone with the Mother."
    
    a "Of course. See you, Ylva."
    
    "I turn and go, not giving in to the temptation to turn back. Even knowing that she’ll always be a call or a text away, something about knowing that it’ll be so much harder to see her makes the thought of saying goodbye all the more agonizing."
    "But I shake off the depressing thoughts and focus on the good I can see. As long as there’s a will for the two of us to reunite, there will be a way."
    stop music fadeout 1.0

    #jump to main club route overa
    $ renpy.call(chosen_club + "_route_overa", "Overa", 19)