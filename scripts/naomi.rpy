label home_ec_route_jinus(month, date):
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Month 1/Naomi_Month1_"
    $ clubmember1_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Club Member 1/Naomi Month 1/ClubMember1_Naomi_Month1_"

    call screen calendar(month, date, "Jinus", 6)
    scene bg home_ec_room_door_afternoon with fade

    $ renpy.notify("Naomi - A Place at the Table\nUctday, Jinus 6th, 1027 RD")
    
    "It's my first official club meeting, and I'm already five minutes late."
    "The Home Ec Clubroom is easy to find this time - just follow the sound of laughter and the faint smell of something sweet and eggy."
    "The door's propped open, and I slip inside."

    "The place is packed. There's a group of students crowded around the main table, all eyes on Naomi as she cracks eggs into a bowl with practiced ease."
    scene bg home_ec_room_stove_afternoon with fade
    "She's got her sleeves rolled up again, hair pinned back with that same plum-blossom hairpin."
    "She's humming something under her breath, and somehow, even with all the chaos, she looks completely at home."

    show naomi neutral apron at center with dissolve
    vl naomi_vl_prefix 1
    n "Alright, everyone. If you want your omelets fluffy, you have to be gentle. No whisking like you're mad at the eggs."

    "A couple of first-years giggle."

    vl clubmember1_vl_prefix 1
    hek "Naomi-shi, can you check mine?"
    
    show naomi happy apron at center
    "Naomi steps over, glancing at the pan, and gives an approving nod."

    vl naomi_vl_prefix 2
    n "Looks perfect, Kira. Just a little more patience, and you'll have it."

    "I linger at the edge of the group, not sure where to start. Naomi spots me and waves me over."

    if eval(a.name)[0] == "Alexis":
        vl naomi_vl_prefix 3A
    else:
        vl naomi_vl_prefix 3B
    n "[a]! Glad you made it. Want to give it a try?"

    a "Sure. Though, fair warning, I've never made anything more complicated than toast."

    show naomi thinking apron at center
    vl naomi_vl_prefix 4
    n "That's alright. We all start somewhere. Here."
    
    "She hands me a bowl and a pair of chopsticks."

    show naomi neutral apron at center
    vl naomi_vl_prefix 5
    n "Just beat the eggs until they're pale yellow. Like this."
    
    "Her demonstration is quick, but careful. I try to copy her, but my wrist gets tired halfway through."

    vl naomi_vl_prefix 6
    n "You'll get used to it. The trick is not to overthink it."
    
    "She pours the eggs into a pan, tilts it, and lets the omelet set before rolling it up with a pair of chopsticks. It looks easy when she does it."
    "When she lets me try, my first attempt comes out lumpy and a little burnt."

    a "Uh... is it supposed to look like that?"

    show naomi happy apron at center
    vl naomi_vl_prefix 7
    n "It's alright, everyone burns the rice at least once. My little brother still does."
    
    "She nudges my shoulder."

    vl naomi_vl_prefix 8
    n "Want to try again?"
    "I nod, and she helps guide my hands the second time. It goes better, though it's still not perfect."

    show bg home_ec_room_door_afternoon with dissolve
    "Around us, the club is buzzing. People call Naomi over for help, ask her to taste their food, or just want her opinion on how much soy sauce is too much."
    "She answers every question, remembers everyone's name, and even jokes with a couple of upperclassmen about last year's 'omelet disaster.'"

    vl clubmember1_vl_prefix 2
    hek "Naomi, you're seriously the heart of this club."

    show naomi embarrassed apron at center with dissolve
    "Naomi laughs, but her cheeks turn a little pink."

    vl naomi_vl_prefix 9
    n "You're all too kind. I just like feeding people."

    show bg home_ec_room_door_afternoon with dissolve
    "The meeting winds down. Plates are cleared, and people start drifting out, waving goodbye to Naomi as they go. I hang back, stacking dishes by the sink."

    a "Need a hand?"

    show naomi neutral apron at center with dissolve
    vl naomi_vl_prefix 10
    n "If you don't mind. It goes faster with two."

    "We fall into a rhythm. She washes, I dry."
    "The kitchen is quiet except for the clinking of dishes and the faint sound of someone practicing piano in the music room next door."

    show naomi thinking apron at center
    if eval(a.name)[0] == "Alexis":
        vl naomi_vl_prefix 11A
    else:
        vl naomi_vl_prefix 11B
    n "So, [a], what's your favorite food?"
    
    "She glances over, genuinely curious."
    
    vl naomi_vl_prefix 12
    n "Or is that too hard a question?"

    a "Honestly? I think it's just anything warm. My mom used to make this soup when I was sick. I haven't had it in years, but I still remember how it smelled."

    show naomi happy apron at center
    "She smiles, a wistful look to her eyes."

    vl naomi_vl_prefix 13
    n "I know what you mean. Food is memory, sometimes."
    
    "She pauses, then holds up her wrist, showing me a delicate bracelet with small charms."
    
    vl naomi_vl_prefix 14
    n "My family's far away, but I keep them close in small ways."

    a "Oh? You're not from around here?"
    show naomi neutral apron at center
    "Naomi shakes her head and smiles, but it doesn't reach her eyes."

    vl naomi_vl_prefix 15
    n "I'm from Tokuen, but I moved here because of my father's job."

    a "Tokuen? I don't think I've heard of that."

    show naomi thinking apron at center
    vl naomi_vl_prefix 16
    n "Sorry, I grew up calling it that. It's what we call Estary in our language."
    
    "She lets the bracelet drop, then changes the subject. I decide not to prod further."

    show naomi happy apron at center
    vl naomi_vl_prefix 17
    n "Next week, I'll show you how to make miso soup. It's easier than it looks, I promise."

    a "Looking forward to it."
    
    "I pause, thinking over it."
    
    a "You're a good teacher, you know."

    show naomi embarrassed apron at center
    "She blushes, a flustered look coming about her."

    vl naomi_vl_prefix 18
    n "Thank you. I just... like seeing people enjoy themselves."
    
    show naomi happy apron at center
    
    "She laughs, shaking her head."
    
    vl naomi_vl_prefix 19
    n "Besides, you survived your first omelet. That's worth celebrating."

    show bg home_ec_room_door_night with dissolve
    "We finish up, and Naomi wipes her hands on her apron."

    show naomi neutral apron at center with dissolve
    if eval(a.name)[0] == "Alexis":
        vl naomi_vl_prefix 20A
    else:
        vl naomi_vl_prefix 20B
    n "Thanks for the help, [a]. You didn't have to stay, you know."

    a "Old habits, I guess. I don't like leaving things half-done."

    show naomi happy apron at center
    "Naomi smiles at me, her eyes crinkling at the edges."

    vl naomi_vl_prefix 21
    n "I hope you'll come back."

    a "Yeah. I think I will."

    hide naomi with dissolve
    scene black with fade

    # jump to phillip jinus
    call phillip_jinus("Jinus", 6) from _call_phillip_jinus_3
    #jump home_ec_route_dallinus

label home_ec_route_dallinus(month, date):
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Month 2/Naomi_Month2_"
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Naomi/Lucas_Naomi_M2_"
    $ clubmember1_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Club Member 1/Naomi Month 2/ClubMember1_Naomi_Month2_"
    $ clubmember2_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Club Member 2/Naomi Month 2/ClubMember2_Naomi_Month2_"
    
    call screen calendar(month, date, "Dallinus", 16)
    scene bg home_ec_room_door_noon with fade

    $ renpy.notify("Naomi - Festival Nights\nUctday, Dallinus 16th, 1027 RD")

    "If last month's meeting was busy, this is chaos."
    "The Harvest Festival is coming up, and the Home Ec Clubroom is packed with people and noise. There's the constant sound of chopping, sizzling, and the occasional shout when someone nearly drops a pan."
    "The air smells like fried batter and something sweet, maybe caramelizing sugar."

    scene bg home_ec_room_stove_noon with fade
    "Naomi is everywhere at once. She's tasting batter, checking on a tray of buns in the oven, and giving advice to a first-year who's panicking about their mochi being too sticky."

    vl clubmember1_vl_prefix 1
    hek "Naomi, is this supposed to look like glue?"
    show naomi neutral apron at center with dissolve
    "She smiles gently, her eyes crinkling at the corners."

    vl naomi_vl_prefix 1
    n "That means you're on the right track. Mochi's always a little stubborn. Here, let me show you."
    
    "She steps in, hands deft, and the first-year's shoulders relax."
    "I watch her for a while, moving from group to group, answering questions, calming nerves."
    "She's got this way of making everyone feel like they're doing fine, even when they're not."
    "I try to help where I can, but mostly I just try not to get in the way."
    "Someone hands me a bowl of strawberries to slice. I focus on the task, listening to the chatter around me."

    vl clubmember2_vl_prefix 1
    "Club Member 2" "Naomi, can you taste this? I think I messed up the filling."
    
    "She tastes it, nodding approvingly."
    
    vl naomi_vl_prefix 2
    n "It's perfect. Maybe a touch more sugar, but only if you want it sweeter."

    show naomi happy apron at center
    "She glances my way and gives a quick wave. Even with all the chaos, she notices."

    scene bg home_ec_room_stove_night with dissolve
    "Hours pass. The sun sets outside, and most of the club filters out, taking trays of sweets and snacks with them."
    "I'm left washing bowls at the sink, and when I turn around, the room is almost empty."

    show naomi thinking apron at center with dissolve
    "Except for Naomi, sitting at the corner table, folding tiny squares of paper into cranes."
    "Her hair's come loose from her braid, and she looks tired in a way she didn't during the meeting."

    "I dry my hands and walk over."

    a "You know, I think this is the quietest I've seen this room since I got here."
    show naomi neutral apron at center
    "She smiles, not looking up from her crane."

    vl naomi_vl_prefix 3
    n "It's my favorite part of the day. When it's just... serene."
    "She finishes a crane and sets it gently on the table. There's a little flock of them already—blue, pink, gold, all folded perfectly."

    show naomi happy apron at center
    vl naomi_vl_prefix 4
    n "Here."

    "She offers me one, a pale blue crane."

    vl naomi_vl_prefix 5
    n "These are for luck. I make them when I need to keep my hands busy."

    a "You must have a lot of luck saved up by now."
    
    "She laughs softly, like twinkling bells ringing across the room."

    vl naomi_vl_prefix 6
    n "Maybe. Or maybe I just get nervous before big events."
    
    "I turn the crane over in my hands. The paper is soft, edges crisp."

    a "It's funny. Back home, I always thought I'd do anything for a little peace and quiet."
    a "But now, I'd give anything to hear my siblings fighting over the last piece of cake."

    vl naomi_vl_prefix 7
    n "You get it, then. It's not just the place you miss. It's the mess, the noise, the people."

    a "Yeah. The mess is the best part, sometimes."
    
    "We share a quiet laugh, the kind that comes from knowing you're not alone in missing something you can't get back."

    "I pause, wondering if I should ask this. But curiosity eventually wins out."

    a "Do you ever get tired of being in charge of all this?"
    
    show naomi thinking apron at center
    "Naomi pauses thoughtfully, the silence stretching out between us."

    vl naomi_vl_prefix 8
    n "Sometimes. But I like seeing everyone together."
    
    "She glances at the cranes."

    vl naomi_vl_prefix 9
    n "It reminds me of home, a little. Festivals in Tokuen were always noisy. Music, food, my siblings running everywhere."
    
    "Her voice goes a little quiet."

    vl naomi_vl_prefix 10
    n "Sometimes, I miss the noise of my family more than anything. But cooking helps. It's like sending a letter home, even if no one reads it."
    
    show naomi embarrassed apron at center
    "She looks up, catching herself, and gives a small, apologetic smile."

    vl naomi_vl_prefix 11
    n "Sorry. I get sentimental when I'm tired."
    
    show naomi happy apron at center
    "She brightens, nudging a plate of sweets toward me."

    vl naomi_vl_prefix 12
    n "Here, try these. They're for the festival, but I won't tell if you have one early."
    "I take a bite. It's soft, sweet, and a little floral."

    a "This is incredible. Did you make these?"
    
    show naomi neutral apron at center
    vl naomi_vl_prefix 13
    n "Most of it's a team effort. But I do have a secret recipe or two."

    "We sit in companionable silence for a while, sharing sweets and watching the moonlight spill through the window."

    a "Thanks for letting me help tonight."
    
    show naomi happy apron at center
    vl naomi_vl_prefix 14
    n "I'm glad you stayed. It's nice, having someone to talk to after everyone's gone."

    "She starts folding another crane, and I watch her hands move; steady, practiced, gentle."
    "For a moment, the world outside the clubroom feels far away."

    hide naomi with dissolve
    scene black with fade
    pause 1.0

    call screen calendar("Dallinus", 16, "Dallinus", 17)
    scene bg weaver_library_night with fade
    $ renpy.notify("Naomi - Festival Nights\nIstday, Dallinus 17th, 1027 RD")

    "The storm outside rattles the old windows of the Weaver Library. Most students have already retreated to their dorms, but the lamps are still burning in the reading room."
    "I spot Naomi curled in a window seat, a thick cookbook open on her knees and a stack of battered Estarese folk tales beside her."
    "Lucas is shelving books nearby, humming softly to himself."

    a "Didn’t expect to find you here after hours."

    show naomi happy at center with dissolve
    "Naomi smiles, a little sheepish."

    vl naomi_vl_prefix 15
    n "It’s quieter than the dorms. Sometimes I come here when I need to think, or when I’m searching for new ideas."

    "She taps the cookbook."

    show naomi neutral
    vl naomi_vl_prefix 16
    n "I found a recipe for honey cakes in here. I think I’ll try it for the next club meeting."

    show naomi happy at character_pos2 with moveinright
    show lucas neutral at character_pos6 with easeinright
    "Lucas perks up, wandering over with a book in hand."

    vl lucas_vl_prefix 1
    l "If you’re looking for inspiration, you should read this one."

    "He holds up a collection of Estary legends."

    vl lucas_vl_prefix 2
    l "There’s a whole chapter about a chef who could charm the wind with her pastries."

    vl naomi_vl_prefix 17
    n "Did she ever burn anything?"

    vl lucas_vl_prefix 3
    l "Only once. The story says the whole village smelled like caramel for a week."

    "Naomi and I exchange a glance, both grinning."

    vl naomi_vl_prefix 18
    n "I wish my disasters were that poetic."

    a "What about you, Lucas? Any culinary disasters?"
    
    show lucas sad
    vl lucas_vl_prefix 4
    l "I once tried to make tea and set off the fire alarm."
    show lucas neutral

    "He shrugs, unbothered."
    "Naomi turns to me, eyes bright."

    if eval(a.name)[0] == "Alexis":
        vl naomi_vl_prefix 19A
    else:
        vl naomi_vl_prefix 19B
    n "What about you, [a]? Did you have a favorite story as a kid?"

    "I think for a moment, surprised by how easily the question brings back old memories."

    a "My grandmother used to tell me a story about a fox who outsmarted a merchant. I always liked that the fox won in the end."

    "Lucas grins."

    vl lucas_vl_prefix 5
    l "Classic. I’ll have to find you the illustrated edition."

    "Naomi hugs her cookbook to her chest."

    vl naomi_vl_prefix 20
    n "Sometimes I think I keep coming back to these stories and recipes because they’re the only things that haven’t changed."

    "I grin."

    a "And they don’t argue with you about curfew or whose turn it is to do dishes."

    vl naomi_vl_prefix 21
    n "Exactly. They’re easier than siblings."

    a "But not as much fun."

    "Our laughter echoes softly in the quiet library, and for a moment, the world feels a little less lonely."
    "The three of us settle into the easy hush of the library, swapping stories and laughter as the storm rolls on outside. Naomi seems lighter here, her usual worries softened by the quiet and the company."

    call student_council_dallinus("Dallinus", 17) from _call_student_council_dallinus_3

label home_ec_route_vanus(month, date):
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Month 3/Naomi_Month3_"

    call screen calendar(month, date, "Vanus", 12)
    scene bg home_ec_room_door_night with fade

    $ renpy.notify("Naomi - Midnight Kitchen\nUctday, Vanus 12th, 1027 RD")
    
    "The festival rush is over, but the clubroom still feels lived-in: a faint scent of sugar in the air, a few stray crumbs on the counter, and the echo of laughter long since faded."
    "It's well past curfew, but the world outside is quiet, just the steady hush of rain against the windows and the soft hum of distant thunder."
    
    show naomi neutral apron with dissolve
    "I'm stacking the last of the trays when Naomi appears at my side, rolling her shoulders and letting out a breath."
    
    vl naomi_vl_prefix 1
    n "I think we survived. Barely."
    
    a "If you call this surviving, I'm not sure I could handle a real emergency."
    
    show naomi happy apron
    "Naomi smiles, tiredness seeping into the edges."
    
    vl naomi_vl_prefix 2
    n "You'd be surprised what you can handle when you have to."
    
    show naomi thinking apron
    "She glances at the clock, then at the empty kitchen. For a second, I think she's about to send me home. Instead, she opens a cupboard and pulls out a battered tin."
    
    show naomi happy apron
    vl naomi_vl_prefix 3
    n "You know... it's still early by festival standards. Want to bake something? Just for us."
    
    a "I would never say no to cookies."
    
    show naomi neutral apron
    "We move around the kitchen in a kind of sleepy rhythm, measuring flour and sugar by the glow of the under-cabinet lights. Naomi's hair is coming loose from her braid, and she doesn't bother fixing it."
    "She hums as she works, something soft and low, almost blending with the rain."
    "It's strange how different the clubroom feels at night. No crowd, no noise, just the two of us and the rain. It's easy to forget about tomorrow, about homework, about anything except the smell of butter and sugar."
    
    vl naomi_vl_prefix 4
    n "Have you ever made cookies from scratch before?"
    
    a "Not unless you count the kind that come out of a tube."
    
    show naomi happy apron
    vl naomi_vl_prefix 5
    n "That's a start. My dad and I used to try new recipes every winter."
    
    "She shakes her head, amused."
    
    vl naomi_vl_prefix 6
    n "We had a running competition for 'worst kitchen disaster.' He once made a cake so hard, we used it as a doorstop for a week."
    
    a "That's impressive. I think my worst was burning instant noodles. Twice. In one night."
    
    show naomi happy apron
    vl naomi_vl_prefix 7
    n "That's a special talent."
    
    show naomi neutral apron
    "We shape the dough into little rounds, pressing them flat. Naomi's hands are quick and sure, but she lets me take my time."
    
    a "You always seem so... together. Even when things are falling apart."
    
    show naomi thinking apron
    vl naomi_vl_prefix 8
    n "It's easier to look calm when you're busy."

    "She glances at me, her voice softer."
    
    vl naomi_vl_prefix 9
    n "Sometimes I wonder what it'd be like to just... let someone else handle things for once."
    
    a "Do you ever wish you could?"
    
    show naomi neutral apron
    vl naomi_vl_prefix 10
    n "Maybe. But I think I'd feel even more lost. Taking care of others... It's how I remember who I am."
    
    "She shrugs, then leans against the counter, watching the oven."
    "There's something honest about the way she says it. Like she's not looking for pity, just telling the truth."
    
    vl naomi_vl_prefix 11
    n "You know, I always thought grown-ups had everything figured out."
    
    "She grins, a little sheepish."
    
    show naomi happy apron
    vl naomi_vl_prefix 12
    n "But here I am, hiding in the kitchen at midnight, hoping the rain will drown out my singing."
    
    a "I won't tell if you sing. I might even join in."
    
    show naomi embarrassed apron
    vl naomi_vl_prefix 13
    n "Deal. But only if you promise not to judge my taste in lullabies."
    
    a "You know, I think I get it. At home, I was always the one making sure everyone else had what they needed. Sometimes I forget how to just... let someone else take care of things."
    
    show naomi thinking apron
    vl naomi_vl_prefix 14
    n "Maybe we're both overdue for a break."
    
    a "Or at least a cookie."
    
    show naomi happy apron
    "*DING* The timer dings."
    "Naomi pulls the cookies from the oven, golden and just a little uneven."
    
    show naomi neutral apron
    "We settle by the window, legs tucked up, sharing the first warm bites while the rain paints streaks down the glass."
    
    a "These are perfect."
    
    show naomi happy apron
    vl naomi_vl_prefix 15
    n "They taste better at midnight. It's a rule."
    
    show naomi neutral apron
    "We sit in comfortable silence, the only sounds the rain and the occasional crunch of a cookie."
    
    a "Thanks for inviting me to stay. I didn't realize how much I needed a night like this."
    
    show naomi happy apron
    "Naomi smiles slightly to herself."
    
    vl naomi_vl_prefix 16
    n "Me too."
    
    "She glances sideways at me, her expression softer than I've ever seen."
    "It's nice, not having to fill every silence."
    "For the first time since I came to MIA, I feel like I belong. Not because I did anything special, but just because I'm here, in this moment, with her, no responsibilities hanging over our heads."
    "We finish the cookies, and for a while, we just watch the rain, letting the quiet comfort settle between us."
    
    # jump to second club route dyalt
    $ renpy.call(chosen_club2 + "_route_dyalt", "Vanus", 12)
    #jump home_ec_route_dyalt1

label home_ec_route_dyalt(month, date):
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Month 4/Naomi_Month4_"

    call screen calendar(month, date, "Dyalt", 23)
    scene bg home_ec_room_door_afternoon with fade

    $ renpy.notify("Naomi - Involvement Festival: Secret Recipe\nUctday, Dyalt 23rd, 1027 RD")

    "The clubroom is a mess of flour, handwritten lists, and the kind of nervous energy that only comes before a big event."
    
    show naomi neutral apron with dissolve
    "Naomi is at the stove, sleeves rolled, a bit of flour on her cheek."
    "I'm helping her chop scallions, though I'm mostly just trying not to get in the way."

    vl naomi_vl_prefix 1
    n "Could you hand me the ginger? The fresh one, not the powder."

    a "You got it."

    show naomi happy apron
    "I pass her the ginger, and she grates it straight into the pan, the smell immediately brightening the room."
    "Naomi smiles, a little distracted."

    vl naomi_vl_prefix 2
    n "Thanks. Sorry if I'm a little... all over the place tonight."

    a "You're fine. I think everyone's a little on edge."

    show naomi thinking apron
    "I glance at the whiteboard, which is covered in crossed-out ideas and last-minute notes."

    vl naomi_vl_prefix 3
    n "This one's special. My mom used to make it for birthdays, or when someone had a bad day."
    voice sustain
    n "It's an Estary thing, I guess, food for every feeling."

    show naomi neutral apron
    "She stirs quietly for a moment."

    vl naomi_vl_prefix 4
    n "I hope it tastes right... Sometimes I wonder if I remember it the way it really was, or just the way I want to."

    a "I think that's how it goes with family recipes. They're half memory, half magic."

    show naomi happy apron
    "Naomi laughs, a little sheepish."

    vl naomi_vl_prefix 5
    n "If it flops, we'll just say it's... 'experimental fusion cuisine.' That's trendy, right?"

    a "If anyone can sell it, it's you."

    show killian happy at right with moveinright
    show naomi neutral apron
    "The door bangs open and Killian pokes his head in, waving a stack of flyers."

    k "Naomi! Can I borrow your colored markers? The Anime Club's booth sign is a disaster."

    vl naomi_vl_prefix 6
    n "Here. Try not to get them sticky this time."

    k "No promises."
    
    "He grins at me, then disappears as quickly as he came."
    hide killian with moveoutright
    show naomi neutral apron

    show naomi thinking apron
    vl naomi_vl_prefix 7
    n "I think he's more nervous than I am."

    a "He's not the one cooking for half the school."

    show naomi happy apron
    vl naomi_vl_prefix 8
    n "Fair point."
    
    "She glances at me, softer now."

    vl naomi_vl_prefix 9
    n "Thanks for sticking around for all these late nights. I know you could've bailed."

    a "I like it. It's nice, seeing how everyone comes together."

    show naomi neutral apron
    "I watch her as she tastes the sauce, eyes closed."

    vl naomi_vl_prefix 10
    n "You know, my little brother used to sneak into the kitchen when I made this. He'd always try to steal a bite before it was done."
    
    show naomi happy apron
    "She laughs, shaking her head."

    vl naomi_vl_prefix 11
    n "He'd say, 'If it's good now, it'll be even better later.'"

    a "Did you ever let him?"

    show naomi happy apron
    vl naomi_vl_prefix 12
    n "Every time."
    
    show naomi thinking apron
    "She looks up, a little wistful."

    vl naomi_vl_prefix 13
    n "I miss that. The noise, the mess. Cooking here helps, though. It's like... sending a letter home, even if no one reads it."

    a "I think they'd be proud."

    show naomi embarrassed apron
    "She blushes, but doesn't argue."

    a "You know, I have a similar story. I tried to make my mom's plum cake once. It turned out... well, let's just say even the birds wouldn't eat it."

    show naomi happy apron
    "Naomi laughs, a little relieved."

    vl naomi_vl_prefix 14
    n "That bad?"

    a "Worse. But it still made the house smell like home, so I guess it worked."

    show naomi happy apron
    vl naomi_vl_prefix 15
    n "That's what matters, isn't it? The trying."

    a "Maybe you're right."

    show naomi neutral apron
    "She sighs, soft and quiet."

    vl naomi_vl_prefix 16
    n "Alright. Taste test?"
    "We try the dish together. It's rich, a little sweet, with a kick of ginger. Naomi's face lights up."

    show naomi happy apron
    vl naomi_vl_prefix 17
    n "That's it. That's the taste I remember."

    jump home_ec_route_dyalt2

label home_ec_route_dyalt2:
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Month 4/Naomi_Month4_"

    call screen calendar("Dyalt", 23, "Dyalt", 30)
    scene bg home_ec_room_door_afternoon with fade

    $ renpy.notify("Naomi - Involvement Festival: Secret Recipe\nUctday, Dyalt 30th, 1027 RD")

    "The clubroom is transformed."
    "Banners, paper lanterns, and a line out the door."
    
    show naomi neutral apron with dissolve
    "Naomi is in her element, but I can see the nerves in the way she smooths her apron and checks the trays."

    show sue neutral at right with moveinright
    show naomi neutral apron
    "Sue stops by, clipboard in hand."

    s "Everything running smoothly?"

    show naomi thinking apron
    "Naomi nods, a little breathless."

    vl naomi_vl_prefix 18
    n "I hope so. We're about to start serving."

    show sue happy
    "Sue smiles softly."

    s "If anyone can pull this off, it's you."

    show naomi happy apron
    hide sue with moveoutright
    "Naomi gives a grateful nod."
    "The first plates go out. Soon, people are coming back for seconds, asking for the recipe, complimenting the flavors."
    "Naomi relaxes, her smile growing with every 'thank you.'"

    scene bg home_ec_room_door_night with fade
    show naomi happy apron with dissolve
    "By the end of the day, the special dish is gone."
    "Naomi finally sits, folding a piece of blue paper into a crane."

    vl naomi_vl_prefix 19
    n "Here."
    
    "She hands me the crane, her fingers brushing mine."

    vl naomi_vl_prefix 20
    n "For luck. Or just... to remember today."

    a "I'll keep it."
    
    "I turn the crane over, then glance at her."

    a "You know, you make it look easy. But I saw how much work you put in."

    show naomi happy apron
    vl naomi_vl_prefix 21
    n "It's worth it. Especially when I don't have to do it alone."

    "We sit together as the sun sets, sharing the last of the festival sweets, the quiet between us comfortable and full."

    call student_council_dyalt("Dyalt", 30) from _call_student_council_dyalt_3

label home_ec_route_neralt(month, date):
    $ reina_vl_prefix = "audio/voices/Love Interests/Reina/Naomi/Reina_Naomi_Month5_"
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Month 5/Naomi_Month5_"

    call screen calendar(month, date, "Neralt", 13)
    scene bg home_ec_room_stove_afternoon with fade 

    $ renpy.notify("Naomi - Whispers and Wishes\nUctday, Neralt 13th, 1027 RD")

    "The last of the club members filters out, their chatter echoing down the hallway. I stay behind, stacking plates and running water over the mixing bowls."
    "The fluorescent lights hum softly overhead, and for once, the clubroom feels too big. Too empty."

    show naomi neutral apron with dissolve
    "Naomi is still here, moving quietly as she wipes down the counters. She keeps glancing at her phone, then at the door, like she's waiting for something, or maybe dreading it."

    "The festival's barely over, but the mood on campus has shifted. I've heard my name whispered in the halls, always paired with Naomi's."
    "It's not mean, exactly, but it's there; curiosity, speculation, the kind of talk that makes you feel like you're under a microscope. I wonder if she's noticed. I wonder if she cares."
    "I finish rinsing the last plate and set it on the rack. Naomi stands by the window, arms folded, watching the rain streak down the glass."

    a "You want me to take out the trash, or...?"

    show naomi thinking apron
    "She shakes her head, not quite meeting my eyes."

    vl naomi_vl_prefix 1
    n "No, it's alright. I'll handle it."

    "The silence stretches. I dry my hands on a towel, waiting."

    a "You've been quiet tonight."

    "Naomi pauses, her gaze still not meeting mine."

    vl naomi_vl_prefix 2
    n "I guess I have."

    show naomi neutral apron
    "She finally turns, her expression carefully neutral, but I can see the tension in her shoulders."

    vl naomi_vl_prefix 3
    n "I heard some things today. About... us."

    show naomi thinking apron
    "She laughs, but there's no humor in it."

    vl naomi_vl_prefix 4
    n "It's funny. I used to think if I just worked hard enough, people would only see the good things."
    voice sustain
    n "That if I was useful, I'd be safe from this kind of thing."

    a "People are always going to talk. Doesn't mean they know anything real."

    vl naomi_vl_prefix 5
    n "Maybe not."

    show naomi neutral apron
    "She leans back against the counter, fiddling with the charm on her bracelet."

    vl naomi_vl_prefix 6
    n "But sometimes I wonder if that's all there is. Just... what people expect from me."

    show naomi thinking apron
    "Her voice drops, almost a whisper."

    vl naomi_vl_prefix 7
    n "Do you ever wonder if people like you for who you are, or just for what you do for them? Sometimes I'm not sure I know the difference."

    "She's always been the one holding things together."
    "The mom friend, the club president, the one who remembers everyone's favorite snack. I never thought about how heavy that might get, or how lonely it could be."
    "I step closer, lowering my voice."

    a "I think... the people who matter, they see you. Not just what you do, but who you are when nobody's looking."

    "I hesitate, mulling the words over in my head."

    a "And I like being here with you, Naomi. In this club. I like how you care about people, and I also like who you are when you're too tired to try."

    show naomi embarrassed apron
    "She blinks, surprised, and for a moment she looks so young, like she's just a kid, trying to figure out how to fit in."

    "Naomi smiles, small and real."

    vl naomi_vl_prefix 8
    n "Thank you."

    show naomi neutral apron
    "She lets out a shaky breath."

    vl naomi_vl_prefix 9
    n "I'm not always sure how to... believe that. Sometimes, I wonder if people just like me for what I do for them. It's hard to tell the difference."

    "She looks at me, her eyes searching for something."

    vl naomi_vl_prefix 10
    n "But I'm trying."

    a "You don't have to do it alone."

    show naomi happy apron
    "She looks at me, eyes shining a little in the harsh kitchen light. The rain outside is louder now, a steady rhythm against the glass."

    vl naomi_vl_prefix 11
    n "Sometimes I wish I could just... not care. Not worry about what everyone thinks."

    show naomi thinking apron
    "She gives a soft, self-deprecating laugh."

    vl naomi_vl_prefix 12
    n "But if I stopped, I don't know who I'd be."

    a "Maybe you'd just be Naomi. And that'd be enough."

    show naomi happy apron
    "She's quiet for a while, then pushes off the counter and grabs a dish towel, standing next to me at the sink."

    vl naomi_vl_prefix 13
    n "You know, when I first got here, I was so scared of messing up. Of being the weird new girl from Estary who only knew how to cook."

    "She glances at me, a little embarrassed."

    vl naomi_vl_prefix 14
    n "I still get scared. But it's easier, with you around."

    "We dry the last dishes together, working in silence that feels more comfortable now. When we finish, Naomi lingers, hands resting on the counter."

    vl naomi_vl_prefix 15
    n "Thanks for staying late."

    "She looks up at me, her voice softer than before."

    vl naomi_vl_prefix 16
    n "And for listening. I don't say that enough."

    a "Anytime. Really."

    show naomi happy apron
    "She smiles, and it's the kind of smile that makes the whole room feel warmer, even with the rain outside."

    vl naomi_vl_prefix 17
    n "Next time, I'll save you the last rice cracker."

    "She bumps my shoulder gently, a little of her old playfulness returning."

    vl naomi_vl_prefix 18
    n "But you have to promise not to let me eat all the leftovers by myself."

    a "Deal."

    "For a moment, it feels like the rumors and the whispers can't touch us here. Just the two of us, sharing the quiet, wishing for something simple and true."
    scene bg student_councilroom_afternoon with fade 

    "The afternoon sky is heavy with clouds, but the rain hasn't started yet."
    "Naomi and I duck into the Student Council Room after a club meeting, hoping to snag a quiet spot to decompress before heading back to the dorms."

    show reina neutral at left_pos
    show sue neutral at center_pos
    with dissolve
    "Sue is at her desk, scribbling on a stack of forms, while Reina is sorting files with her usual laser focus."
    "The room is filled with the low hum of paperwork and the faint smell of tea."

    show naomi neutral at right_pos
    with dissolve
    "Naomi sets her bag down and glances around, a little hesitant."

    vl naomi_vl_prefix 19
    n "Think they'll mind if we hide out here for a bit?"

    a "If we're quiet, I doubt they'll even notice."

    show naomi happy
    "Naomi grins and pulls out a small pouch, producing a handful of crackers and dried fruit."

    vl naomi_vl_prefix 20
    n "Emergency provisions. I always come prepared."

    "We settle on the window ledge, sharing snacks and watching the clouds drift by. Sue glances up, pen still moving."

    show sue happy
    s "If you're going to eat in here, don't drop any crumbs. Reina will have my head."

    show reina thinking
    vl reina_vl_prefix 1
    r "I heard that."

    "She doesn't look up."

    vl reina_vl_prefix 2
    r "And she's right."

    show naomi happy
    "Naomi stifles a giggle, passing me a cracker. The room feels different with the council here, less like a meeting and more like a safe little corner of the world, just for now."

    "I'm used to seeing Naomi in charge, but here, tucked in the corner, she's just another student taking a breather. It's oddly comforting."
    "Sue and Reina start bickering about next year's club budgets, Reina's voice clipped and precise, Sue's a little more exasperated."

    show sue neutral
    s "You know, sometimes I think you actually enjoy being the bad guy."

    show reina happy
    vl reina_vl_prefix 3
    r "Oh, absolutely. I get up every morning just to ruin everyone's fun."

    show sue happy
    s "See? You're doing it now. You can't help but bicker."

    show reina neutral
    vl reina_vl_prefix 4
    r "It's called keeping everyone in line. Someone's got to do it."

    show naomi neutral
    "Naomi leans closer, voice low."

    vl naomi_vl_prefix 21
    n "I like seeing them like this. It's... reassuring. Even the people in charge are just people."

    show reina thinking
    vl reina_vl_prefix 5
    r "Well, someone has to be the bad guy. People just have to suck it up and deal with it."

    show sue happy
    s "And we do appreciate you, even if we don't always say it."

    show naomi happy
    "Naomi smiles, a little shy, and the clouds outside begin to break, sunlight slanting through the windows."

    "We gather our things, Sue waving us off with a distracted \"Don't get locked in,\" and step out into the fresh, bright air."

    "For a moment, I wonder if I'll ever see this room the same way again."
    
    # jump to second club route neralt
    $ renpy.call(chosen_club2 + "_route_neralt", "Neralt", 13)
    #jump student_council_exalt

label home_ec_route_exalt(month, date):
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Month 6/Naomi_Month6_"
    $ lucas_vl_prefix = "audio/voices/Love Interests/Lucas/Naomi/Lucas_Naomi_M6_"

    call screen calendar(month, date, "Exalt", 24)
    scene bg home_ec_room_door_afternoon with fade

    $ renpy.notify("Naomi - Rainy Day Window\nUctday, Exalt 24th, 1027 RD")

    "The snow started before lunch and hasn't let up. By the time the club lets out, the windows are fogged and the world outside is just a blur of white."
    "Most of the Home Ec members have already scattered, some to the dorms, some to the library, a few just standing in the hallway, debating whether it's worth sprinting through the snow."

    show naomi neutral apron with dissolve
    "I'm about to pack up when Naomi waves me over, a quiet smile on her face."

    if eval(a.name)[0] == "Alexis":
        vl naomi_vl_prefix 1A
    else:
        vl naomi_vl_prefix 1B
    n "Hey, [a]."

    "She nods toward the far end of the room, where a wide window seat is half-hidden by a curtain."

    vl naomi_vl_prefix 2
    n "Come sit for a bit? I made too many rice crackers again."

    a "I mean, if you insist."

    show naomi happy apron
    "I follow her to the window. The rain outside is steady, almost hypnotic. Naomi settles in, legs tucked up, offering me a small plate of snacks."
    "Her braid's more loose than usual today, a little frizzy from the humidity, and there's a softness to her that matches the weather."
    "It's strange how the world feels smaller on rainy days. Like everything beyond this room is on pause, waiting for the sun to come back."
    "We sit in companionable silence for a while, watching the drops race each other down the glass. Naomi breaks the quiet, her voice softer than usual."

    show naomi thinking apron
    vl naomi_vl_prefix 3
    n "Rain always makes me think of home."

    show naomi happy apron
    "She smiles a little, looking out at the storm."

    vl naomi_vl_prefix 4
    n "My siblings and I would watch storms together, all crammed under one blanket. We'd make a game of guessing which raindrop would reach the bottom first."

    show naomi embarrassed apron
    "She laughs, a little embarrassed."

    vl naomi_vl_prefix 5
    n "I miss that. The noise, the mess. Even the arguments."

    a "I used to do that too, actually. My brother always cheated, though. He'd tap the glass to make his raindrop win."

    show naomi happy apron
    "Naomi laughs, her eyes lighting up."

    vl naomi_vl_prefix 6
    n "That's genius. I wish I'd thought of that."

    show lucas neutral at character_pos7 with easeinright
    show naomi neutral apron
    "The door creaks open, and Lucas pokes his head in, a book clutched to his chest."

    vl lucas_vl_prefix 1
    l "Naomi, did you—oh, sorry. Didn't mean to interrupt."

    show naomi happy apron
    "Naomi smiles, waving him in."

    vl naomi_vl_prefix 7
    n "It's fine, Lucas. We're just hiding from the rain."

    "Lucas glances at the window, then at the plate of rice crackers."

    vl lucas_vl_prefix 2
    l "You always have the best snacks."

    "He gives me a nod."

    if eval(a.name)[0] == "Alexis":
        vl lucas_vl_prefix 3A
    else:
        vl lucas_vl_prefix 3B
    l "Mind if I borrow her for a minute, [a]?"

    show naomi happy apron
    vl naomi_vl_prefix 8
    n "You can have a rice cracker, but you can't steal me away."

    "She grins, handing him one, then moves to a nearby table, pulling out a scrap of paper and a pen."

    vl naomi_vl_prefix 9
    n "What is it?"

    vl lucas_vl_prefix 4
    l "Just wanted to check if you had the recipe for those sesame buns from last week. The Literature Club keeps asking for them."

    show naomi neutral apron
    "Naomi starts jotting down the recipe, her movements quick and practiced."

    vl naomi_vl_prefix 10
    n "I'll write it down for you before you go."

    show naomi happy apron
    "She glances at me with a reassuring smile."

    vl naomi_vl_prefix 11
    n "Sorry. I get sentimental when it rains."

    "She offers the plate of rice crackers to me again while continuing to write."

    vl naomi_vl_prefix 12
    n "Would you like another rice cracker?"

    a "If you're sure you don't mind sharing."

    vl naomi_vl_prefix 13
    n "I always make too much."

    hide lucas with moveoutright
    show naomi neutral apron
    "Once she hands the recipe to Lucas, he thanks her and disappears as quietly as he came, leaving us alone again with the rain."

    show naomi thinking apron
    "Naomi leans back, exhaling slowly. She smiles, but her gaze is distant for a moment."

    vl naomi_vl_prefix 14
    n "I guess I'm still learning how to fill the silence."

    show naomi happy apron
    "She glances at me, her voice almost a whisper."

    vl naomi_vl_prefix 15
    n "You make it a little easier."

    "There's something different about today. The way she lets her guard down, the way she doesn't rush to fill every quiet moment with chatter or jokes."
    "It feels like trust, even if she doesn't say it out loud."
    "We sit together, listening to the rain, sharing snacks and stories, some silly, some small, all of them ours."
    "The world outside fades away, and for a little while, it's just the two of us, warm and safe behind the glass."

    if chosen_club2 == "enseki":
        call enseki_route_exalt2("Exalt", 24) from _call_enseki_route_exalt2_2
    else:
        call phillip_elvera("Exalt", 24) from _call_phillip_elvera_3

label home_ec_route_elvera(month, date):
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Month 7/Naomi_Month7_"

    call screen calendar(month, date, "Elvera", 19)
    scene bg home_ec_room_door_night with fade
    
    $ renpy.notify("Naomi - A Place Just for Us\nLenday, Elvera 19th, 1028 RD")

    "The clubroom is transformed. Paper lanterns cast a soft, golden glow, and the usual clutter has vanished."
    "There's a small table set for two, dishes arranged with care. Outside, the campus is hushed and dark, rain tapping quietly at the windows."

    show naomi neutral with dissolve
    "I pause in the doorway, feeling like I've stumbled into someone else's dream. Naomi stands by the table, adjusting a napkin, her hair pinned up with her favorite plum-blossom clip."
    "She looks up, her smile a little shy."

    vl naomi_vl_prefix 1
    n "Hey. You made it."

    show naomi happy
    "She gestures to the table."

    vl naomi_vl_prefix 2
    n "I, um… hope you're hungry. I might have gone overboard."

    a "If this is overboard, I'm not sure I could survive a regular dinner at your place."

    show naomi embarrassed
    "Naomi laughs, a little embarrassed."

    vl naomi_vl_prefix 3
    n "You'd have to fight my siblings for the last dumpling."

    show naomi neutral
    "We sit. The food is beautiful, steamed buns, pickled vegetables, a delicate soup."
    "Naomi pours tea, her hands steady but her eyes flicking up to meet mine, then away again."
    "For a while, we talk about nothing in particular. Naomi tells a story about her little brother's disastrous attempt at making pancakes."
    "I tease her about her \"experimental fusion cuisine,\" and she rolls her eyes, but her laughter is genuine."

    show naomi happy
    "It's easy, being here with her. The world outside feels far away, no rumors, no expectations, just the quiet clink of teacups and the warmth of her smile."

    show naomi thinking
    "Naomi sets her chopsticks down, tracing the rim of her teacup with her finger."

    vl naomi_vl_prefix 4
    n "You know…"

    "She hesitates, searching for the right words."

    vl naomi_vl_prefix 5
    n "Sometimes I wonder what it would be like to just…"

    show naomi embarrassed
    "She trails off, then shakes her head, a little sheepish."

    vl naomi_vl_prefix 6
    n "Sorry, that sounded dramatic."

    a "No, really, what were you going to say?"

    show naomi neutral
    "Naomi takes a breath, her voice softer but steady."

    vl naomi_vl_prefix 7
    n "I think… sometimes I just want to be seen. Not just for how much I can help, or what I do for everyone else, but for… well, me."

    show naomi happy
    "She looks up, meeting my eyes, a little nervous, but not turning away."

    vl naomi_vl_prefix 8
    n "And when I'm with you, I feel like I am. Not because you need me, but because you get it."
    voice sustain
    n "You know what it's like to be the one holding things together, and you still notice the person underneath."

    show naomi neutral
    "She glances away, busying herself with the teapot, but her words linger in the space between us."

    vl naomi_vl_prefix 9
    n "Sorry. That probably sounds silly."

    a "It doesn't."

    "I pause, searching for the right words."

    a "I think… I know what you mean. It's easy for people to see what you do, but not always who you are."
    a "I like that you care so much about everyone, but even if you ever stopped, I'd still want to be here with you."

    show naomi happy
    "Naomi's smile is small, but real."

    vl naomi_vl_prefix 10
    n "I appreciate that. And you know, I notice things about you, too."

    "She looks at me, more open now."

    vl naomi_vl_prefix 11
    n "I see how you always try to make things easier for other people, even when you think no one's watching."
    voice sustain
    n "I see how you remember the little things, like who likes what snack or who's having a hard week."

    show naomi happy
    "She grins."

    vl naomi_vl_prefix 12
    n "And I see how you always manage to burn toast, even when you're trying not to."

    "We both laugh, the tension easing."

    vl naomi_vl_prefix 13
    n "I guess I just wanted you to know I notice. And I'm glad you're here."

    show naomi neutral
    "For a moment, we just sit there, the silence gentle and full. It's the kind of quiet that feels comfortable."

    vl naomi_vl_prefix 14
    n "So…"

    show naomi happy
    "She finally lets out a breath, her voice lighter."

    vl naomi_vl_prefix 15
    n "Ready for dessert? I promise it's not \"experimental\" this time."

    a "I'll believe it when I taste it."

    show naomi happy
    vl naomi_vl_prefix Laugh
    "She laughs, and the world feels simple again. We share dessert, sweet, sticky, and a little messy, trading stories about family kitchen disasters and laughing when I nearly drop a piece in my lap."
    "The night stretches on, soft and golden, and for a while, it feels like we're both exactly where we're meant to be."
    
    call home_ec_route_verabris("Elvera", 19) from _call_home_ec_route_verabris

label home_ec_route_verabris(month, date):
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Month 8/Naomi_Month8_"

    call screen calendar(month, date, "Verabris", 14)
    scene bg wright_field_afternoon with fade

    $ renpy.notify("Naomi - Home is a Person\nNyday, Verabris 14th, 1028 RD")

    "The sun is setting, painting the sky in streaks of rose and gold."
    "The air is crisp, almost sharp, and every breath feels like it's filled with the promise of something ending and something new just beginning."
    "The campus is quieter than usual, most students are at last club meetings or packing up their rooms."
    "Here, in the fields, it feels like the world has slowed down just for us."

    show naomi neutral

    "Naomi walks beside me, hands tucked into her cardigan sleeves, her hair loose and catching the last light."
    "We meander along the winding gravel path, shoes crunching softly with every step. The scent of damp earth and late-blooming flowers lingers in the air."
    "I keep thinking that I should feel different, more excited, more nervous, more… something. But mostly, I just feel present. Aware of everything around me."

    show naomi thinking

    "Naomi slows as we pass under a willow, its branches trailing like curtains. She stops, looking out at the little pond where the water catches the fading light."

    vl naomi_vl_prefix 1
    n "It's colder than I expected."

    "She hugs her arms a little tighter, but she's smiling."

    show naomi happy
    vl naomi_vl_prefix 2
    n "But I like it. It makes everything feel clearer, somehow."

    a "It's like the world's holding its breath."

    show naomi neutral

    "She glances at me, eyes bright in the twilight."

    vl naomi_vl_prefix 3
    n "Yeah. Like it's waiting for us to decide what comes next."

    "We sit on a low stone bench, half-hidden by ivy. Naomi leans forward, elbows on her knees, gaze fixed on the ripples in the pond."

    show naomi thinking
    vl naomi_vl_prefix 4
    n "You know, I used to think \"home\" was a place."

    "Her voice is soft, almost lost in the hush of evening."

    vl naomi_vl_prefix 5
    n "I worry sometimes… that I'll forget the sound of the ocean back home, or my little sister's laugh echoing down the hall."

    "She twists her bracelet absently."

    show naomi neutral
    vl naomi_vl_prefix 6
    n "But then I remember, home isn't just a place. It's the people you share your life with."

    "A breeze stirs, sending a few petals tumbling across the path. Naomi watches them, thoughtful."

    show naomi happy
    if eval(a.name)[0] == "Alexis":
        vl naomi_vl_prefix 7A
    else:
        vl naomi_vl_prefix 7B
    n "I think I found a little bit of that here, with you."
    voice sustain
    n "Not just because of what we do for everyone else, but because you actually see me, [a]."
    vl naomi_vl_prefix 8
    n "And I see you, too, how you quietly look out for everyone, even when you think no one notices."
    voice sustain
    n "I'm glad you're here."

    a "Just a little bit of home, huh?"

    "I nudge her gently with my shoulder, and she laughs, the sound soft and real."

    vl naomi_vl_prefix 9
    n "Maybe more than a little."

    "She bumps me back, her eyes shining."

    show naomi neutral
    vl naomi_vl_prefix 10
    n "Besides, if you ever get tired of my cooking, you're legally required to tell me. I promise, I won't be offended. Probably."

    a "I'll take my chances. But honestly, I think I'd miss it too much."
    a "And not just the food, the way you make everyone feel like they belong. Even me, when I was new and didn't know anyone."

    show naomi embarrassed
    vl naomi_vl_prefix 11
    n "That's what my dad always said, but I'm pretty sure he just didn't want to hurt my feelings."

    "We both laugh, the sound mingling with the distant calls of birds settling in for the night."

    show naomi happy

    "Naomi leans back, looking up as the first stars appear in the deepening blue."
    vl naomi_vl_prefix 12
    n "Do you ever wonder what comes next?"

    "She glances at me, her voice hopeful but a little uncertain."

    vl naomi_vl_prefix 13
    n "Not just after graduation, but… everything?"

    a "All the time."

    "I pause, thinking it over."

    a "But I think, as long as you have the right people with you, it doesn't matter where you end up."
    a "And… I'm glad you're one of mine."

    show naomi embarrassed

    "Naomi's smile is a little shy, but there's a steadiness in her gaze."

    vl naomi_vl_prefix 14
    n "I think I'd like that."

    "We sit together, letting the silence settle around us, the sky growing darker and the air cooler."
    "For the first time, the future feels close enough to touch, and not so scary after all."

    call screen calendar("Verabris", 14, "Verabris", 15)
    scene bg home_ec_room_stove_afternoon with fade

    $ renpy.notify("Naomi - Home is a Person\nLenday, Verabris 15th, 1028 RD")

    "The clubroom is quieter than usual, sunlight streaming through the windows and catching on the flour-dusted counters and stacks of recipe cards."
    "The festival banners are gone, but traces of the year linger in every corner."
    "Naomi and I are sorting through leftover club supplies, old flyers, and a box of lost-and-found treasures."

    show naomi neutral apron

    "I always thought cleaning up would feel like a countdown to freedom."
    "But now, every little thing I pack away feels like tucking away a piece of this year, a year that somehow became home."
    "Naomi picks up a folded scrap of paper, the edges worn soft."

    vl naomi_vl_prefix 15
    n "You still have this?"

    show naomi happy apron

    "I know what it is before she even opens it: the note she slipped me during my first week, when I was still finding my way around."
    "The handwriting is a little messy, the ink smudged where she'd pressed too hard."
    "\"Don't forget: the best snacks are in the Home Ec room. If you ever need a friend, you know where to find me. — Naomi\""

    a "Of course I kept it."

    "I take it from her, smoothing the creases."

    a "It was the first time I felt like maybe I'd made the right choice coming here."

    show naomi embarrassed apron

    "Naomi smiles, a little embarrassed, but her eyes are warm."

    vl naomi_vl_prefix 16
    n "I almost forgot I wrote that."

    "She laughs softly."

    vl naomi_vl_prefix 17
    n "I was so nervous you'd think I was weird."

    a "I did."

    "I grin."

    a "But in a good way. The kind of weird that makes everything better."

    show naomi happy apron

    "She nudges me with her shoulder, shaking her head."

    vl naomi_vl_prefix 18
    n "You're hopeless."

    "We fall into an easy rhythm, packing away club aprons and sorting through a pile of mismatched chopsticks."
    "Naomi finds a crumpled festival ticket from the night we got caught in the rain, and we both start laughing at the memory."

    a "I still can't believe you convinced me to run across campus in a thunderstorm for fried noodles."

    show naomi neutral apron
    vl naomi_vl_prefix 19
    n "Worth it, though. You have to admit, they tasted better after all that effort."

    a "I'll give you that."

    "It's funny, the things that end up mattering most. Not the grades or the big events, but the little notes, the inside jokes, the quiet moments that nobody else saw."

    show naomi happy apron

    "Naomi rummages in a supply box and pulls out a small, neatly wrapped snack, setting it on the counter beside me."

    vl naomi_vl_prefix 20
    n "For the road."

    "Her voice is gentle, a little wistful."

    vl naomi_vl_prefix 21
    n "Just in case you get hungry before you even leave campus."

    a "I'll save it for when I miss the club. Or, you know, when I burn dinner."

    show naomi neutral apron

    "She sits back, looking around the room one last time."

    vl naomi_vl_prefix 22
    n "I'm glad I got to be part of your mess."

    show naomi happy apron

    "She bumps my arm, her smile soft."

    vl naomi_vl_prefix 23
    n "And I expect updates. Or at least pictures of your next culinary disaster."

    a "Deal. But only if you promise to send me recipes. And updates on your next adventure."

    vl naomi_vl_prefix 24
    n "It's a promise."

    "We finish the last box, and Naomi squeezes my hand before she leaves, her touch warm and steady."

    hide naomi with dissolve

    "As the door closes softly behind her, I realize it's not the clubroom or the school I'll miss most, it's this."

    "The feeling that, for a little while, I truly belonged, and that someone else saw the real me, too."
    
    #jump to second clubd route verabris
    $ renpy.call(chosen_club2 + "_route_verabris", "Verabris", 15)
    #jump student_council_verabis

label home_ec_route_overa(month, date):
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Epilogue/Confession/Naomi_Epilogue_"

    call screen calendar(month, date, "Overa", 22)
    scene bg wright_field_afternoon with fade

    $ renpy.notify("Naomi - Confession\nUctday, Overa 22nd, 1028 RD")

    "The field is quiet, golden light spilling through the leaves. The air is still, carrying the faint scent of grass and summer's end."

    show naomi neutral
    "Naomi waits on a small spot beneath a flowering tree, a bento box in her lap. She looks up as I approach, her smile soft but nervous."
    "Naomi pats the bench beside her. I sit, feeling the hush of the world around us, just the two of us, the day slipping toward dusk."

    show naomi embarrassed
    vl naomi_vl_prefix 1
    n "I, um… made this for you."

    "She opens the bento, each dish arranged with care."

    show naomi happy
    vl naomi_vl_prefix 2
    n "Every recipe means something. My mom's pickled plums, my little brother's favorite rice balls…"

    show naomi embarrassed
    "She glances at me, a little shy."

    vl naomi_vl_prefix 3
    n "I wanted to share this with you. Not just the food, but… all the pieces of where I come from."
    voice sustain
    n "You're the first person I've wanted to share it all with."

    show naomi neutral
    "We eat together, the silence comfortable, each bite a small act of trust. Naomi laughs as I struggle with a stubborn piece of omelet."

    show naomi happy
    vl naomi_vl_prefix 4
    n "You'd think after all this time, you'd have mastered chopsticks."

    a "Some things are just meant to be mysterious."

    "She grins, but then her expression grows serious again."

    show naomi thinking
    vl naomi_vl_prefix 5
    n "I've spent so long being the one who keeps things running, who's steady and dependable."
    voice sustain
    n "But with you, I feel like I can be all the parts of myself, even the ones that aren't so put-together."

    show naomi neutral
    if eval(a.name)[0] == "Alexis":
        vl naomi_vl_prefix 6A
    else:
        vl naomi_vl_prefix 6B
    n "You see me, [a]. Not just the \"mom friend,\" or the girl who cooks, but… me."
    vl naomi_vl_prefix 7
    n "And I see you, too. I know how much you carry for your family, how you always look out for everyone, even when you think no one notices."
    voice sustain
    n "You make me feel safe enough to be a little lost sometimes."

    show naomi happy

    "She looks at me, eyes shimmering in the golden light."

    vl naomi_vl_prefix 8
    n "I don't know what the future holds, but I want to face it with you. Not because I need you, but because I choose you."

    show naomi embarrassed

    "She waits, breath held, heart open."
    jump home_ec_route_overa_choice

label home_ec_route_overa_choice:
    if player_gender == "female":
        $ naomi_platonic = True
        jump home_ec_route_overa_platonic
    else:

        menu:
            "Accept Naomi's confession":
                $ naomi_romance = True
                jump home_ec_route_overa_romance_accept

            "Reject Naomi's confession":
                $ naomi_romance = False
                jump home_ec_route_overa_romance_reject

label home_ec_route_overa_romance_accept: 
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Epilogue/Confession/Accepted/Naomi_Epilogue_Accepted_"
    
    show naomi neutral
    
    a "Naomi…"

    "I reach for her hand, warmth blooming between us."

    show naomi happy

    a "I see you. All of you. And I want that future too."
    a "I care about all of it, Naomi. The way you look out for everyone, the way you make people feel at home that's part of you."

    a "But even if you needed to take a break, or let someone else take care of things for once, I'd still want to be here with you."
    a "I like you for all of it, for who you are, and for how you care. Not just one or the other."

    show naomi embarrassed

    "Her shoulders relax, a real, radiant smile breaking through. She squeezes my hand, her thumb tracing gentle circles on my skin."

    vl naomi_vl_prefix 1
    n "Thank you."

    show naomi happy

    "She laughs, a little shaky with relief."

    vl naomi_vl_prefix 2
    n "I was so sure I'd mess this up."

    a "You couldn't, even if you tried."

    "We finish the meal slowly, savoring the food and the moment."
    "We talk about dreams, her seaside café, places we want to travel, the kind of life we could build together."

    show naomi neutral

    "As the sun dips below the horizon, Naomi leans in, her forehead resting lightly against mine."

    vl naomi_vl_prefix 3
    n "Whatever comes next… let's face it together."

    "I nod, and for the first time, the future feels not just possible, but bright."
    call epilogue_graduation("Overa", 22) from _call_epilogue_graduation_8

label home_ec_route_overa_romance_reject:
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Epilogue/Confession/Rejected/Naomi_Epilogue_Rejected_"

    show naomi neutral

    a "Naomi…"

    "I reach for her hand, holding it gently."

    show naomi thinking

    a "You mean so much to me. I hope you know that."

    "I pause, searching for the right words."

    a "But I don't think I can be what you're looking for. Not right now. I'm sorry."

    show naomi happy

    "Naomi's expression softens, a bittersweet smile touching her lips. She squeezes my hand once before letting go."

    vl naomi_vl_prefix 1
    n "Thank you for being honest with me."

    show naomi neutral

    "She gently folds the cloth around the bento, her voice warm but tinged with wistfulness."

    vl naomi_vl_prefix 2
    n "You'll always have a seat at my table, and probably more food than you can eat. That won't change."

    "There's sadness, but also relief. The bond between us is still there, different, maybe, but strong."
    "We sit together in the fading light, the world quiet around us."

    show naomi happy
    "Naomi's strength shines through, and I know our friendship will endure, even as we step into whatever comes next."
    
    call epilogue_graduation("Overa", 22) from _call_epilogue_graduation_9

label home_ec_route_overa_platonic:
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Own Route/Epilogue/Platonic/Naomi_Epilogue_Platonic_"

    scene bg wright_field_afternoon with fade
    show naomi neutral
    "The field is quiet, golden light spilling across the grass and painting everything in warm, fading color."
    "Naomi waits beneath a flowering tree at the edge of the field, a bento box in her lap. She looks up as I approach, her smile soft, nervous, but real."
    "It feels strange, seeing the field so empty. All year, it's been a place of noise and movement, but now it's just us and the hush of the evening."
    "I wonder if Naomi feels the same sense of ending and beginning tangled together."
    "I settle down beside her, the grass cool beneath my hands."

    show naomi happy
    "Naomi unwraps the bento, laying it out between us, a careful arrangement of rice balls, pickled vegetables, and sweet egg, each piece tucked in with care."

    vl naomi_vl_prefix 1
    n "I thought we could have one last meal out here."

    show naomi embarrassed
    "She glances at me, a little shy."

    vl naomi_vl_prefix 2
    n "You know, for luck. Or just… to say thank you."
    voice sustain
    n "Every recipe means something to me, my mom's pickled plums, my brother's favorite rice balls, my own favorite sweet egg."
    voice sustain
    n "I wanted to share them with you, because you've become part of those memories now, too."

    a "You didn't have to, but I'm glad you did."

    show naomi neutral

    "We eat together, the silence companionable. The world feels far away, just the soft hum of insects and the distant call of a bird."

    show naomi happy

    "Naomi laughs as I struggle with a particularly stubborn piece of omelet."

    vl naomi_vl_prefix 3
    n "You'd think after all this time, you'd have mastered chopsticks."

    a "Some things are just meant to be mysterious."

    "She grins, and for a moment, all the worries about the future fade away."

    show naomi thinking
    vl naomi_vl_prefix 4
    n "I was thinking earlier…"

    "She looks out over the field, voice quiet."

    vl naomi_vl_prefix 5
    n "It's funny how places can feel like home, but it's really the people that matter."

    show naomi happy

    "She nudges me gently with her shoulder."

    if eval(a.name)[0] == "Alexis":
        vl naomi_vl_prefix 6A
    else:
        vl naomi_vl_prefix 6B
    n "Thanks for being my person this year. I don't think I could've gotten through it without you."
    voice sustain
    n "I don't just mean the club, or the cooking, or the chaos. I mean… you saw me, [a]. Not just the \"mom friend,\" but the person underneath."
    voice sustain
    n "And I hope you know I see you, too."

    "There's a lump in my throat I didn't expect. I want to say something big, but all that comes out is the truth."

    a "Right back at you. I don't think I'll ever forget this year. Or you."
    a "You made this place feel like home, Naomi. And not just for me."

    show naomi embarrassed
    "Naomi smiles, a little misty-eyed, but she doesn't look away."

    vl naomi_vl_prefix 7
    n "Promise me we'll keep in touch? Even if it's just texts here and there. Or recipes."

    a "You'll be getting so many texts you'll beg me to stop."

    show naomi happy
    "She laughs, and the sound is bright and easy."

    vl naomi_vl_prefix 8
    n "Good. I'd miss you otherwise."

    show naomi neutral
    "We sit together as the sun slips lower, the field bathed in gold. Naomi stands, brushing grass from her skirt, and offers me her hand."

    vl naomi_vl_prefix 
    n "Come on. Let's walk back before it gets dark."

    "I take her hand, and we head across the field together, the world wide open in front of us."
    "Whatever comes next, I know we'll carry this year, and each other, wherever we go."
    
    call epilogue_graduation("Overa", 22) from _call_epilogue_graduation_10

label epilogue_home_ec_route:
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Epilogue/Goodbye to Naomi/Naomi_Shared_Epilogue_Goodbye_"
    $ oribe_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Oribe/Goodbye to Naomi/Oribe_Epilogue_Goodbye_"

    scene bg maincastle with fade

    "The crowd is finally thinning. The rest of Huntsdale is spreading out before me."
    "It's only a matter of time until I find the others."

    show naomi neutral at center with hpunch
    vl naomi_vl_prefix 1
    n "Oribe, be careful! Look where you're going-!"

    "Yet another person crashes into me. I don't feel much of an impact."
    "I turn, and find a little boy on his rear end. Naomi is right on his heels."

    vl naomi_vl_prefix 2
    n "And that's what happens when you don't. You're not hurt, are you?"

    "She helps him up and pats him down."

    vl oribe_vl_prefix 1
    orib "I'm okay, seisei."

    vl naomi_vl_prefix 3
    n "Good. Now what do we do when we bump into people like that?"

    "He turns to me and bows."

    vl oribe_vl_prefix 2
    orib "I'm sorry for bumping into you."

    a "It's alright. I'm just glad that you're okay."

    "Only when I speak does Naomi seem to notice me."
    jump epilogue_naomi_choice

label epilogue_naomi_choice:
    if chosen_club == "home_ec":
        if naomi_romance:
            jump epilogue_home_ec_route_romance_accept
        elif naomi_platonic:
            jump epilogue_home_ec_route_platonic
        else: 
            jump epilogue_home_ec_route_romance_reject
    else:
        jump epilogue_home_ec_route_not_chosen

label epilogue_home_ec_route_romance_accept:
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Epilogue/Goodbye to Naomi/Accepted/Naomi_Shared_Epilogue_GoodbyeAccepted_"
    $ salem_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Oribe/Goodbye to Naomi/Confession Accepted/Oribe_Epilogue_GoodbyeAccepted_"

    show naomi neutral at center
    vl naomi_vl_prefix 1
    n "Oh!"

    "She pats the boy on the shoulder."

    vl naomi_vl_prefix 2
    n "You'll be able to find your way back to the others?"

    "He nods."

    vl naomi_vl_prefix 3
    n "Good. I'll be right behind you."

    "He runs off, screaming at the top of his lungs."

    vl oribe_vl_prefix 1
    orib "Mira, Iguro, I found seisei's boyfriend!"

    show naomi embarrassed

    "When he's gone, I look to Naomi, who's gone red as a beet."

    a "Do they know?"

    vl naomi_vl_prefix 4
    n "No, n-not yet. He's just teasing."

    a "Coming from someone else with a younger brother, he's going to live it up when he finds out he was right."

    vl naomi_vl_prefix 5
    n "I know…"

    show naomi happy

    a "So the rest of your family flew over?"

    vl naomi_vl_prefix 6
    n "They did! It was a surprise, too. It made me so happy. It's just for a little while now, but someday…"

    a "It'll be for good."

    show naomi neutral
    vl naomi_vl_prefix 7
    n "I don't know when that will happen, or what will happen in the days leading up to it, but it does make it a bit less scary knowing I won't have to face it alone."

    a "You're right, you won't be."

    "I look in the direction her brother ran."

    a "I don't want to keep you from your family, with how long it's been since you've see them."

    vl naomi_vl_prefix 8
    n "Thank you. I'll talk to you as soon as I can. That might be a little while, though…"

    a "That's fine. Go to them."

    show naomi happy
    "She hesitates for a moment. Then she pulls me into a quick hug and hurries off in the same direction her brother did."
    
    jump epilogue_archery_route

label epilogue_home_ec_route_romance_reject:
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Epilogue/Goodbye to Naomi/Rejected/Naomi_Shared_Epilogue_GoodbyeRejected_"
    $ salem_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Oribe/Goodbye to Naomi/Confession Rejected/Oribe_Epilogue_GoodbyeRejected_"

    show naomi neutral at center
    vl naomi_vl_prefix 1
    n "Oh!"

    "She pats the boy on the shoulder."

    vl naomi_vl_prefix 2
    n "You'll be able to find your way back to the others?"

    "He nods."

    vl naomi_vl_prefix 3
    n "Good. I'll be right behind you."

    "He runs off, screaming at the top of his lungs."

    vl oribe_vl_prefix 1
    orib "Mira, Iguro, I found seisei's boyfriend!"

    show naomi embarrassed

    "When he's gone, I look to Naomi, who's gone red as a beet."

    vl naomi_vl_prefix 4
    n "Don't mind him."

    a "Eh, he's a kid. Let him have his fun. That your brother?"

    show naomi happy
    vl naomi_vl_prefix 5
    n "He is. An energetic boy, isn't he?"

    a "If your family came all this way, I don't want to keep you from them."

    vl naomi_vl_prefix 6
    n "That's very thoughtful of you. Before I go, I was wondering…"

    a "What's up?"

    vl naomi_vl_prefix 7
    n "When my cafe opens, you'll visit, won't you?"

    a "Of course."

    show naomi happy

    "She lights up at that."

    vl naomi_vl_prefix 8
    n "I'll be sure to let you know where it is when I can get it up and running. I'll… be going, then."

    a "Take care, Naomi."

    "She bows and turns, running off after her brother."
    jump epilogue_archery_route

label epilogue_home_ec_route_platonic:
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Epilogue/Goodbye to Naomi/None/Naomi_Shared_Epilogue_GoodbyeNone_"
    $ salem_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Oribe/Goodbye to Naomi/No Confession/Oribe_Epilogue_GoodbyeNone_"
    
    show naomi neutral at center
    vl naomi_vl_prefix 1
    n "Oh!"

    "She pats the boy on the shoulder."

    vl naomi_vl_prefix 2
    n "You'll be able to find your way back to the others?"

    "He nods."

    vl naomi_vl_prefix 3
    n "Good. I'll be right behind you."

    "He runs off, screaming at the top of his lungs."

    vl oribe_vl_prefix 1
    orib "Iguro, seisei's friend is super pretty! Come talk to her!"

    vl naomi_vl_prefix 4
    n "Don't mind him."

    a "Trying to set me up with your brother, eh?"

    show naomi thinking
    vl naomi_vl_prefix 5
    n "I swear, if Iguro comes over here…"

    a "But think about it. Me and your brother would mean we might be sisters some day. Doesn't that sound fun?"

    show naomi happy

    "At that, she laughs"

    vl naomi_vl_prefix 6
    n "Now isn't that a bit extreme? Besides, you don't need to be my sister-in-law to be an important part of my life."

    a "You're right about that. Wait, if your family's here, I shouldn't keep you. It's been ages, right?"

    vl naomi_vl_prefix 7
    n "Well, yes, but—"

    a "We can always talk later. I'm only a text away. Now go and have some fun."

    show naomi happy

    if eval(a.name)[0] == "Alexis":
        vl naomi_vl_prefix 8A
    else:
        vl naomi_vl_prefix 8B
    n "R-right! I'll talk to you later, then. Bye, [a]."

    "She bows and turns, running off after her brother."
    
    jump epilogue_archery_route

label epilogue_home_ec_route_not_chosen:
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Epilogue/Goodbye to Naomi/Not Chosen/Naomi_Shared_Epilogue_GoodbyeNotChosen_"

    show naomi neutral at center
    vl naomi_vl_prefix 1
    n "Sorry for the interruption. [a], was it?"

    a "That's right. I'm surprised you remember."

    vl naomi_vl_prefix 2
    n "Oh, it's nothing too special. Congratulations on graduating. It was nice getting a chance to meet you."

    a "Same to you."

    vl naomi_vl_prefix 3
    n "Let's get going, Oribe."

    "Leading the little boy by the hand, he and Naomi head back into the crowd."
    jump epilogue_archery_route

label reuinion_home_ec_route:
    $ naomi_vl_prefix = "audio/voices/Love Interests/Naomi/Epilogue/Meet the Family/Naomi_Shared_Epilogue_MeetFamily_"
    $ arline_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Arline/Epilogue/Meet Naomi/Arline_Epilogue_MeetNaomi_"
    $ skylar_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Skylar/Meet Naomi/Skylar_Epilogue_MeetNaomi_"
    $ salem_vl_prefix = "audio/voices/Supporting-Extra/Extra Voices/Salem/Meeting Naomi/Salem_Epilogue_MeetNaomi_"

    scene bg mainstreet_afternoon with dissolve
    show naomi neutral at center with dissolve

    $ renpy.notify("Naomi - Meeting the Family\nNyday, Overa 25, 1028 RD")

    "When Naomi arrives, I’m a bit surprised to see that she’s alone."

    show naomi thinking with dissolve
    a "No one else from your family wanted to come?"

    show naomi neutral
    vl naomi_vl_prefix 1
    n "I talked them out of it. Just feels like it would’ve been embarrassing."

    a "So, Mother, Salem, Skylar, this is Naomi."

    show naomi happy
    vl naomi_vl_prefix 2
    n "Naomi Kuzuma. It's a pleasure to meet you all."

    vl skylar_vl_prefix 1
    sky "She's so cute…"

    show naomi embarrassed
    vl naomi_vl_prefix 3
    n "T-thank you!"

    vl salem_vl_prefix 1
    salem "So you're here without your family?"
    voice sustain
    salem "Guess I can't blame you for leaving them behind, but sounds like it would've been fun to meet them all."

    show naomi happy
    vl naomi_vl_prefix 4
    n "I'm sure there will be a chance someday. My younger brother was especially sad when I said he had to stay behind."

    vl skylar_vl_prefix 2
    sky "You were president of the Home Ec Club? My brother mentioned something like that while we were waiting."

    vl naomi_vl_prefix 5
    n "That's right. Cooking's really become a passion of mine these past few years. I wanted to share the joy of it with the other students."

    vl salem_vl_prefix 2
    salem "I'd love to take a class sometime."

    vl skylar_vl_prefix 3
    sky "So would I. If you wouldn't mind."

    vl naomi_vl_prefix 6
    n "Not at all. I'd be happy to!"

    "I notice Mother looking Naomi up and down. In fact, she's been silent this entire time."

    a "Mother?"

    vl arline_vl_prefix 1
    arline "Sweet as sugar, family-oriented, a whiz in the kitchen, and as cute as a button."
    voice sustain
    arline "Dear, you couldn't have found me a better daughter-in-law if you tried!"

    show naomi embarrassed with dissolve
    vl naomi_vl_prefix 7
    n "A better what?"

    a "Mom…! Do you have any idea how embarrassing that is?!"

    sky "Pfft…! Hahahahaha!"

    vl skylar_vl_prefix Laughter
    "Skylar doubles over in her laughter while Salem looks at me as if I were nothing more than a lowly insect."

    vl salem_vl_prefix 3
    salem "Bro… that is the lamest thing you have ever said."

    vl arline_vl_prefix 2
    arline "Just a bit of playful teasing. That's for the two of you to decide."
    voice sustain
    arline "And even then, a discussion that shouldn't happen for a long, long time."

    a "Yes, that's very right."

    vl arline_vl_prefix 3
    arline "Actually, Naomi, there was something I wanted to ask you about Estarese cuisine…"

    "Skylar excuses herself to take a seat on the bench and recover from her laughing fit."
    "Mother and Salem ask Naomi about food, with me offering some assistance, based on what I learned over the year cooking with her."

    hide naomi
    jump finale