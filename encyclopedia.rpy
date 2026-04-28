screen encyclopedia():
    default frame_width = config.screen_width / 2
    default selected_category = None
    default selected_subcategory_index = None
    fixed:
        grid 2 1:
            frame:
                xsize 960
                yfill True
                has vbox
                frame:
                    xfill True
                    xmaximum 960
                    has hbox
                    for i in range(len(encyclopedia_unios)):
                        textbutton encyclopedia_unios[i]["name"]:
                            text_size 30
                            xmaximum 200
                            action [SetScreenVariable("selected_category", encyclopedia_unios[i]["id"]),SetScreenVariable("selected_subcategory_index", None)]
                frame:
                    xfill True
                    has vbox
                    if selected_category != None:
                        $ sub_categories = eval(selected_category)["sub_categories"]
                        python:
                            print(selected_category)
                            print(type(eval(selected_category)))
                        for i in range(len(sub_categories)):
                            textbutton sub_categories[i]["name"]:
                                action SetScreenVariable("selected_subcategory_index", i)
            frame:
                xsize 960
                #yfill True
                background Solid("#fff")
                if selected_subcategory_index != None:
                    use political_entities_info(sub_categories[selected_subcategory_index])

screen political_entities_info(subcategory):
    viewport id "political_entity_vp":
        xsize 960
        draggable True
        has vbox
        for key, value in subcategory.items():
            text "[key]: [value]"

    vbar value YScrollValue("political_entity_vp"):
        xalign 1.0
        at transform:
            on hover:
                alpha 1.0
            on idle:
                linear 0.5 alpha 0.0


define political_entities = {
    "id": "political_entities",
    "name": "Political Entities of Unios",
    "desc": "The world of Unios is governed by a number of bodies that bind its nations in various alliances. In the modern day, the following political entities and sovereign states exist:\n- The Magianan Empire\n- The Holy Queendom of Oslein\n- Allowlucia\n- The Republic of Osma\n- The Culmarean League\n- The Eastern Confederation\n- Apanaʻoha\n- The Oceanic Alliance\n- Unios United",
    "sub_categories": [
        {
            "id": 0,
            "name": "The Magianan Empire",
            "Continent(s)": "Lucio, Voles",
            "Predominant Religion": "Nyrellanism",
            "Date Founded": "718 RD",
            "Capital and Largest City": "Ferenicia",
            "Est. Population": "802.8 Million",
            "desc": "The Magianan Empire is much smaller in scope than some other political entities on Unios. It was designed to give the states of the continent of Lucio a common government, common laws, freer trade, freer travel, and a permanent set of allies. The Sworn Sword and Sword Shield are the right and left hand of the emperor or empress. The title alone is equivalent to that of Colonel in the Imperial Army.",
            "Member States": [
                "Kingdom of Magiana - The homeland of the empire, and one of the most powerful nations in the modern world. The capital city of Ferenicia lies on its western coast and is known as the Jewel of the Empire.",
                "Kingdom of Troara - To the north of Magiana, Troara’s brutal winters have made the people especially reliant on and close knit with their families, their most sure allies when the weather turns against them. Its capital of Alta Maria is situated in a mountain range.",
                "Republic of Aragon - The imperial nation with the most territory, comprised mainly of islands in the southern ocean, Aragon is known for its enthusiastic, lively, and open minded populace. It’s also called the birthplace of modern democracy.",
                "Kingdom of Estary - Becoming a member of the empire towards the end of the ninth century, this far eastern nation boasts a proud populace renowned for their determination and passion. Its capital, Shouryū, was rebuilt after a civil war, and is referred to by some as the Jewel of the East, due to their similar layouts."
            ]
        },
        {
            "id": 1,
            "name": "The Holy Queendom of Oslein",
            "Continent": "Cena",
            "Predominant Religion": "Nyrellanism",
            "Date Founded": "10 RD",
            "Capital": "Civiallow",
            "Largest City": "Romia",
            "Est. Population": "154.1 Million",
            "desc": "The traditional homeland of the elves and the Roma people, Oslein is the birthplace of the planet's most common religion. Outside of Oslein, it is found most often in the Empire and the Culmarean League, though it's practiced everywhere. Once considered the center of civilization, Oslein enjoys a much more subdued presence on the world stage in the modern day. It is one of only three nations—alongside Apanaʻoha and Melstrain—in which a monarch rules with what is tantamount to absolute power in the modern day."
        },
        {
            "id": 2,
            "name": "Allowlucia",
            "Continent": "Cena",
            "Predominant Religion": "Nyrellanism",
            "Date Founded": "10 RD",
            "Est. Population": "6.7 Million",
            "desc": "This small city-state is enclaved within Civiallow, the capital of Oslein. It is the seat of the Nyrellan Church. Its Sovereign, and leader of the Church, is known as the Contact, and is said to have been chosen by the goddess Nyrella Herself to represent the Divines on Unios. Like Oslein, its continued global prominence is largely thanks to the cultural significance the religion of Nyrellanism retains."
        },
        {
            "id": 3,
            "name": "The Republic of Osma",
            "Continent": "Cena",
            "Predominant Religion": "Faith of the Eight",
            "Date Founded": "15 RD",
            "Capital": "Amabula",
            "Largest City": "Cape Crimson",
            "Est. Population": "509.1 Million",
            "desc": "Osma as a nation was united out of necessity during the early days of the Reign of the Divines. When a Nyrellan aspirant to the throne raised an army, the Amansie, Ajak, Eunoto, and Arishem peoples banded together to defeat them, out of fear of the nascent religion displacing the Faith of the Eight. They lived together in a tenuous peace for centuries afterward, with each group's current leader serving as Osma's monarch. In the late 800s, upon its transition to republicanism, it attempted to retain this delicate balance, with each president having three vice presidents from the other three tribes.\nThe capital of the nation changed each time its leader did. While, in theory, that would ensure that all parts of Osma enjoyed the privilege of being the seat of power, during its years as a monarchy, there was no way of knowing if one tribe would dominate for only a few years before its leader died and the rotation would begin again, or half a century. The length of Osma's presidential terms meant that these changes would happen regularly, with this lack of consistency being a persistent cause of tension.\nAmidst growing instability, it was with the assistance of Emperor Gregory Magis of the Magianan Empire in the year 1000 that a permanent administrative capital was established in the long ignored Songwo region of the nation in its geographical center.\nSongwo Province, the administrative center of the nation which is also its geographical center, is notably a predominantly Nyrellan region."
        },
        {
            "id": 4,
            "name": "The Culmarean League",
            "Continent": "Culmar",
            "Predominant Religion": "Nyrellanism",
            "Date Founded": "600s RD",
            "De Facto Capital": "Llyn, Aglea",
            "Largest City": "Brighton",
            "Est. Population": "680.4 Million",
            "desc": "A loose alliance that sees the countries of the Culmarean continent sharing a close economic relationship.",
            "Member States": [
                "Republic of Aglea - Made up of nine clans, each associated with an element, the people of Aglea hold strongly to their democratic traditions, first established after a bitter struggle between the clans for the nation’s throne.",
                "Republic of Eflington - Once the two separate nations of Eforte and Lexington, Eflington’s two halves retain their disparate cultures. Eforte in the west is much more expressive and easygoing while Lexington places much more emphasis on organization and efficiency.",
                "Kingdom of Archos - Third only to Oslein and Allowlucia, Archos has the most devout Nyrellan population on Unios. However, the much larger Magianan Empire has a wider reputation for being a global representative of the faith. The people of Archos, due to their geographical closeness to Terrakai and Cena, are among the most tolerant of foreigners."
            ]
        },
        {
            "id": 5,
            "name": "The Eastern Confederation",
            "Continent(s)": "Terrakai, Voles",
            "Predominant Religion": "Animism",
            "Date Founded": "600s RD",
            "Est. Population": "1.2374 Billion",
            "desc": "Founded in response to the Culmarean League, the Confederation is much larger, being made up of nations from two continents. It is more of a political and military alliance above all else. The economic ties of the League and the more open foreign policy of the empire is generally lacking in the Confederation.",
            "Member States": [
                "Kingdom of Melstrain - The traditional home of the dracomorphs, Melstrain is one of the few non-western Nyrellan nations. The often mild mannered peoples of Melstrain are known for their openness and hospitality, almost more so than their ability to transform into dragons.",
                "Kingdom of Yespela - This southwestern Volesian nation has always been in the shadow of its nation, Otren. Fiercely animist, the farmers and sailors of the nation are known to be some of the most spiritual and passionate, but also the most fearful of the outside world. Even its learned elites are anxious of potential influence from foreigners.",
                "Republic of Gibroar - A close ally of Yespela, the second largest nation of Terrakai acts as a buffer between the animist east and Nyrellan west. Itself a predominantly animist nation, it’s only marginally more moderate than Yespela, and shares a similar fear of its traditions being undermined should Nyrellanism spread.",
                "Republic of Daslea - Daslea is known for being a center of culture in the middle ages, as well as the birthplace of the world’s most popular styles of swordplay, collectively known as the Sixfold Path. Daslea is the youngest republic in the world, only abandoning its monarchy around 1000 RD.",
                "Republic of Acroton - A dominant force on the world stage in the late 800s RD. Defeated in a war instigated by dictator Jeremy Reiner and absorbed into the Confederation. In the modern day, Acroton struggles to remain relevant, and its people live quiet lives.",
                "Republic of Otren - The de facto leader of the Confederation, which rose to prominence in the 900s as the rest of the alliance recovered from Reiner’s War and the so-called Republican Wave of the latter years of the previous century. Led by a strong central government, the nation acts as a bulwark against influence from the empire, with Estary a short distance away.",
                "Republic of Goengyi - An emerging economic powerhouse, and one of the birthplaces of Spiritism, a religion blending Nyrellanism and animism. Once part of Otren, and still sharing a land border with it, the people of the city-state are often fearful that the much larger nation might take some sort of action against them."
            ]
        },
        {
            "id": 6,
            "name": "Apanaʻoha",
            "Predominant Religion": "Pacificanism",
            "Capital and Largest City": "Pahui",
            "Est. Population": "15.8 Million",
            "desc": "Situated in the Western Ocean, this island microstate is the homeland of the seafaring Pacifican people. Its capital, known to Pacificans as simply \"The City,\" but Pahui to foreigners, is one of the foremost seaports in the world. The island is also a key source of manite for militaries and corporations all over the globe."
        },
        {
            "id": 7,
            "name": "The Oceanic Alliance",
            "desc": "The nations of the world most reliant on the sea formed this alliance to govern and regulate the waters of the world.",
            "Member States": [
                "Aragon",
                "Estary",
                "Aglea",
                "Osma",
                "Goengyi",
                "Apanaʻoha"
            ]
        },
        {
            "id": 8,
            "name": "Unios United",
            "desc": "Founded around 1000 RD, Unios United is made up of prominent members from each of the world's political entities. Not all nations are represented, though all alliances are.",
            "Member States": [
                "Magianan Empire, represented by Magiana",
                "Eastern Confederation, represented by Otren",
                "Culmarean League, represented by Aglea",
                "Osma",
                "Oslein",
                "Apanaʻoha",
                "Allowlucia"
            ]
        }
    ]
}

define magic = {
    "id": "magic",
    "name": "Magic",
    "desc": "Magic is broadly defined as the ability to manipulate the natural world. Most peoples of Unios are capable of such a feat, which in some way, shape, or form involves them interacting closely with the following:",
    "sub_categories": [
        {
            "name": "Aer",
            "desc": "Aer is one of the fundamental parts of Unios. It was once thought of as the two distinct substances of \"air\" and \"mana\", until Professors Ralph Wald and Amelia Weathers of the Imperial Institute of Natural Science discovered that the substances people breathed and used to power their magic were one and the same.\n\nAer is made up of six components: fire, water, earth, wind, shadow, and light. When broken up into those components, a small bit is leftover: pure aer, known as void.\n\nPeople draw aer into themselves with a part of their brain called the Aer Cortex, then break it apart into those component pieces. They exhale all of the elements they have no use for, with the ones they retained powering their magic. People born without an Aer Cortex are said to have Aer Cortex Deficiency Disorder (ACDD).\n\nSince ACDD was only recognized as a medical condition in the later 800s RD, until that point, people born incapable of using magic were referred to as \"Dim\" in the Nyrellan world and other non-animist nations. In animist majority nations, people with ACDD were—and still are, in some cases—referred to as \"soulless,\" said to have been abandoned by the spirits that govern the world and are said to bless people with the gift of magic."
        },
        {
            "name": "Manite",
            "desc": "Manite is a mineral found all over Unios. Elves are capable of using magic with their Aer Cortexes alone, though it's more taxing, but humans and drachkin both need to use manite as conduits. Once aer is funneled into a piece of manite, it can then be expelled as what people call \"Magic Arts\".\n\nManite, like aer itself, comes in a number of varieties. Manite of a specific element can only use Magic Arts of that element. The rarest and more valuable, translucent pure manite, can be any sort of magic its wielder desires.\n\nCollectively, all elements of this mineral are known as manite, but each element also has individual names.\n\nEarth - Amber in color, and referred to as Gaeastone.\nWater - Blue in color, and referred to as Veolite.\nFire - Red in color, and referred to as Ambadine.\nWind - Green in color, and referred to as Urald.\nLight - Yellow in color, and referred to as Luxite.\nShadow - Dark purple in color, and referred to as Nixite.\nVoid - Transculent, and referred to as Etherite.\n\nThe four tribes of the drakoni people can only use magic arts of their tribe. For example, Fyr Vyr drachkin can only use fire magic. All manite that isn’t fire or pure would be useless to them.\n\nManite eventually breaks and loses its ability to hold aer. The time until it breaks is determined by its size and how much it is used. Often cut into spherical shapes to be used as power sources, manite comes in four sizes. From smallest to largest, they are referred to as Spheres, Nodes, Orbs, and Globes. Globes are most expensive, but would last the longest before needing to be replaced."
        },
        {
            "name": "Beaststones & Heartstones",
            "desc": "Heartstones are a colloquial term for heart shaped stones. On their own, they don’t do anything, but they are very popular as a vessel for summon spirits. As such, they are often associated with summoning.\n\nBeaststones are effectively fossilized animal souls. They are a popular power source for Arms and magitechnology, though they’re rare and expensive. Being a soul, a person and their Arm often have a relation like that of companions, or even a person and their pet. In Animist nations, they are referred to as Soulstones.\n\nBeaststones are one of the only sources of Ice and Lightning Magic Arts, which do not have corresponding elements of aer or manite.\n\nDifferent species of animals always produce the same beaststone. For example, all lions will produce fire beaststones."
        },
        {
            "name": "Caster Magic",
            "desc": "Caster Magic is the most common branch of magic practiced. When people refer to the ability to manipulate aer and have it produce various effects, they’re referring to Caster Magic.\n\nSummoning\nSummoning is a form of magic that doesn’t quite fall under any umbrella, but is usually associated with Caster Magic. Summon spirits, or Familiars, are ghosts that people are capable of making pacts with. These pacts are just agreements the two beings make, so each bond is highly personal. Once a pact is made, a spirit takes residence in some sort of object the summoner provides. They can then use their Aer Cortex to summon them and use their power. So long as the pact is upheld, they will be able to do this. If one swears to fight for justice, and then acts in a way contrary to their own, or their Familiar’s, sense of justice, whatever magic the Familiar would normally use on their behalf would not work.\n\nCasting Styles\nPeople are capable of using magic just by thinking about the effect that they want to produce. That core concept of \"think and it shall be\" led some to spend more time visualizing the magic they want to cast, resulting in stronger spells. Over time three distinct styles of casting emerged.\n\nThe most common uses no incantations, and it referred to as \"quickcasting\". People simply conjure their spells into existence. It is the quickest way to use magic, but also the weakest and most inefficient. It is often the casting method that most quickly breaks someone's manite.\n\nSome people use short phrases to cast their spells. This \"shortchanting\" gives their magic more power. Them effectively speaking their magic into existence makes it more clear in their minds, and gives them more power.\n\nThe last type of cast is that of \"Incanters.\" These people use full incantations, spending the most time to channel their aer and process it into a pure form. This form of magic use is the most powerful and efficient, but since a person must stand still to focus and cast, it is the longest and leaves them the most vulnerable."
        },
        {
            "name": "Fundamentals of Magic & the Exaotic Window",
            "desc": "This is the study of Magic as an art and a concept. Considered its own field of science, it covers a wide range of topics, including the nature of Aer and its use, the application of Magic, Magitechnology, and the ethics and philosophy regarding magic.\n\nMagical Medicine is considered a sub-discipline of Fundamentals, and examines how magic can be used to heal wounds and treat illnesses.\n\nIn recent years, medical researchers have come to the consensus that magical healing does not alone alter or repair the body, so much as it stimulates the immune system and the body's natural healing process. To many, this explains why it's easy to heal a small cut, while all magic can do for a viral infection or chronic condition is hold off symptoms for a time.\n\nThe Exaotic Window—named for the Divine Exaos—refers to a medical theory centering around the limitations of healing magic. After a time, magic becomes unable to affect the body, but doctors aren't in agreement on what determines when the window closes. A popular example used when debating the window are occasions where, in the heat of the moment, something like a broken bone by be healed incorrectly and have to be broken again by a medical professional to be properly set. The Traumatic Exaotic Window proposes that the bone being broken again dampens the impact magic would have on it, while the Temporal Exaotic Window proposes that, since the initial break, the amount of time that's passed would make magic less effective."
        },
        {
            "name": "Potion Brewing",
            "desc": "Potions are used for various tasks like granting temporary invisibility, accelerated crop growth, and so on. Potion brewing is sometimes called a type of science, but is treated as an entirely different field.\n\nDifferent types of materials are associated with different functions and elements.\n\nThe liquids in a potion are referred to as Bloods, and associated with water. They are the basis for potions, supporting them and giving them life.\nAlcohol used in potions are referred to as Spirits, and associated with wind. They add greater volume and character to a potion, and are the basis for magical potions.\nFungi used in potions are called Bodies, and are associated with earth. They are supportive structures that add body to a potion, and are the basis of physical potions.\nHerbs used in potions are the Nerves, and are associated with void. They befuddle the mind or alter its functions. They are the basis for mental potions.\nAnimal parts added to a potion are its Bones, and are associated with fire. They add greater character and body to potions, amplifying their effects."
        },
        {
            "name": "Magical Theology",
            "desc": "Magical Theology, in a sense, is just the art of praying. Through asking the Gods to do certain things, generally at some sort of cost, people are capable of doing things that they normally aren’t capable of doing. Sometimes special conditions must be met and certain words recited. It is the most niche form of magic because of its limited applications.\n\nIn some academic circles, the field is expanded to include general study on how the religions of the world impact the attitudes their practitioners have towards magic."
        },
        {
            "name": "Overreach",
            "desc": "All people on Unios are born with a gene that gives them the ability to enhance their abilities. This is known as Overreach, and has two different expressions, depending on whether or not someone is born with an Aer Cortex.\n\nThose born with an Aer Cortex, for a limited time, see their magical abilities enhanced. Normally, people don’t use all of their Aer Cortex, and Overreach sees them temporarily breaking their limits. However, it leaves them exhausted afterwards, usually with a bad headache.\n\nFor those without an Aer Cortex, they have access to what is known as Latent Overreach. Due to their lack of magical ability, Latent Overreach instead enhances their physical capabilities. They both perceive the world around them more slowly and move more quickly."
        },
        {
            "name": "Arms",
            "desc": "Arms are weapons that have been enchanted with Beaststones or manite to use some sort of magic. There are all kinds of Arms, from swords to axes to firearms. \"Enhancement Arm\" is a colloquial term for an Arm that compliments magic a person normally uses even when unarmed."
        },
        {
            "name": "The Sixfold Path",
            "desc": "The Sixfold Path is the name given for a school of eastern swordsmanship that came to dominate the world in the late middle ages. Its defining feature is its implementation of magic and magical philosophy into its forms. The school was founded by six Daslean swordsmen who each mastered one of the core elements and incorporated it into their swordsmanship. Each of these is called a Path, which itself has a number of different forms and techniques. Each of the Paths is represented by a certain animal, and it is not uncommon for the Beaststones in Arms of practitioners of a path to be from their path’s associated animal.\n\nFirst Path: Stalwart Sword\nThe First Path, of Earth, is the most defensive of the six paths. Many of its techniques are various forms of counters and parries, allowing practitioners to use their opponent’s attacks against them. The extinct Terra Costa is the animal of the Stalwart Sword. Called \"the world turtle,\" this massive animal was known for being incredibly long lived and hard to kill, though their small population is what eventually led to them dying out.\n\nSecond Path: Flowing Fang\nThe Second path, of Water, is one of the more defensive paths. While not as defensive as the First Path, this path focuses on smooth, flowing movements that make the practitioner hard to keep track of and hit. The Efortian Palatinate is a species of dolphin native to the waters around Eforte. They are so named for their purple color and the telepathy scientists have hypothesized they use for communication, rather than simple echolocation. They are very quick, swift, and elegant in the water, hence their association with this path.\n\nThird Path: Blazing Blade\nThe Third Path, of Fire, is one of the most offensive paths. The path focuses on using the destructive power of fire to overwhelm the practitioner’s opponents and win the fight. The Salamandryx, native to Melstrain, is the animal of the Blazing Sword. They, like the Troaran Stoat, are known to be aggressive, yet aren't as infamously vicious.\n\nFourth Path: Blustering Blade\nThe Fourth Path, of Wind, focuses on swift, successive strikes. Some practitioners focus on using these swift strikes to overwhelm the opposition while others make use of their speed to avoid being hit. The path could be offensive or defensive, depending on what the user wills. The animal of the Fourth Path is the Sylphalcon. Called the Lord of the Skies, this species of falcon is the fastest flying species on all of Unios.\n\nFifth Path: Lightning Sword\nThe Fifth Path, of Lightning, is the most magically inclined. This path combines the range of lightning magic and the user’s skill with swordsmanship. It is among the most versatile because it can be used rather effectively for more close-range and long-range combat. The Thunderbane Dragon is the animal of the Lightning Sword path. As the quintessential creature that is associated with lightning, it was only natural to take this dragon as the path's animal.\n\nSixth Path: Frigid Fang\nThe Sixth Path, of Ice, is like the element on which it is based, and the most fragile. In exchange, it also has the most raw power. This path focuses on overwhelming the opponent and immobilizing them with ice magic. However, this Path’s offensive nature also renders practitioners rather vulnerable if caught off guard. The Troaran Stoat is a small northern mammal native to the frigid Troaran north. They are known for being territorial and aggressive, appropriate symbols for the quick, offensive fighting style."
        }
    ]
}

define lore_cosmology = {
    "id": "lore_cosmology",
    "name": "Lore & Cosmology",
    "desc": "In addition to the religions of the world of Unios, the world is governed by a number of laws that inform how its people go about their lives and think about the supernatural and the afterlife.",
    "sub_categories": [
        {
            "name": "Romanism",
            "desc": "Romanism is the religion of the nomadic Roma, native to Oslein. An ethnic religion, though conversion hasn't been completely unheard of. Worships a deity known as the Creator, called Ors by the Osman government and the Nyrellan Church, with seven aspects related to seven virtues and elements. This one god in seven is said to represent the ideal person.\n\nThe Creator puts specific emphasis on temperance and respect for the world around you. As such, the Roma decided against settling in any one place and overusing its resources, staying for a portion of the year before moving on and allowing an area time to renew the resources they might have used.\n\nThe Creator is said to have dictated to the Roma that they should grow their hair out, at least long enough to braid, for the braid and its complex, interwoven structure symbolized the complex nature and relationship that all things in nature have.\n\nAs a religion, Romanism puts the most focus on the self, and being an ideal person. For being righteous and enlightened in life, Roma are said to become part of the Eternal Coil after death, in which they enjoy life with the Creator. Failure to do so results in banishment to the Void, and the destruction of their soul.\n\nThe virtues that practioners of Romanism are encouraged to aspire to are referred to as \"The Links of Life.\" It shares in common with the Faith of the Eight the following:\nTemperance\nService - To more traditional practitioners of the religion, the Link of Service is gender specific, with men encouraged to take on more active or leadership roles, with women encouraged to support them.\nPiety\n\nThe following Links are unique to the religion:\nHarmony\nSerenity\nIngenuity - Creativity and art are celebrated amongst the Roma, and people are encouraged to think outside of the box and create art.\nAdaptability - Given the nomadic culture of the Roma, it is considered virtuous for a person to be willing and able to adjust to changes in their lives and environment"
        },
        {
            "name": "Faith of the Eight",
            "desc": "The Faith of the Eight is the predominant religion of Osma, and believed to be closely related to that of the Roma. Some Osman scholars suggest that Romanism is an offshoot of the Faith of the Eight. While the Roma beleive that there is a Creator with seven aspects, Osmans believe that a chief God has several subordinates that represent how mortals ought to live. The four tribes of Osma have slightly different beliefs about who this chief deity is, with the local name of the religion being slightly different as a result.\n\nAs a religion, the Faith of the Eight puts the great focus on the self, and being an ideal person. For being righteous and enlightened in life, people are said to open the Gate of Life after death, in which they enjoy life with their God. Failure to do so results in banishment to the Void, and the destruction of their soul.\n\nThe virtues that practioners of the Faith are encouraged to aspire to are referred to as \"Keys.\" It shares in common with Romanism the following:\nTemperance\nService\nPiety\n\nThe following Links are unique to the religion:\nPassion\nResilience\nWisdom - This Key specifically refers to maintaining a healthy curiosity and desire to learn\n\nThe seventh Key differs between Osma's four tribes:\nTo the Amansie, it is Guardianship. This differs from the Nyrellan virtue of the same name. To the Amansie, Guardianship refers to a person's contributions to raising the next generation of their people.\nTo the Eunoto, it is Strength. Strength of body and strength of will are both thought of as virtuous things to have. It's enough for a person to have either-or.\nTo the Ajak, it is Ambition.\nTo the Arishem, it is Tolerance."
        },
        {
            "name": "Pacificanism",
            "desc": "Pacificanism is the religion of the seafaring Pacificans. An ethnic religion, though conversion hasn't been completely unheard of. Worships the goddess of the seas, Pacifica. Given the nature of their beliefs, water is of the utmost importance, and given its importance to life in general, the Pacificans hold a deep reverence for all water and aquatic life. They idolize many traits they attribute to their goddess, such as openness and compassion.\n\nAs a religion, Pacificanism puts a great focus on service to others. The faithful are said to enjoy eternal life with their Goddess after death. Failure to do so results in banishment to the Void (called \"Fono\" in the Pacifican language), and the destruction of their soul."
        },
        {
            "name": "Animism",
            "desc": "Animism as a religion is most common in the far east, with slight variations depending on where it's practiced, animists believe that the world is governed by various spirits, rather than very distinct gods with their own teachings and dogma.\n\nAnimism places great importance in relations. The elderly are said to be more holy, for they are closer to death and joining the Spirits that the living worship. As such, younger people defer to their elders. These elders are usually in more senior positions, so while juniors defer to their seniors, this is often one and the same. The young are to respect their elders so that they protect them and bless them. The old are to respect and treat the young well, so that their descendants will continue to worship them and leave offerings for them, rather than let their souls be forgotten.\n\nThese \"Forgotten Ones\" are said to be people so wicked in life that their children and future descendants elected against honoring them in death. Animism doesn't make distinctions for peculiar spirits like Nyrellanism does, so Spectres, monsters, and fiends are all considered Forgotten Ones.\n\nIn Estarese, \"Shokuromi\" is a term for \"soulless\" people; ones that can't use magic. Basically people with Aer Cortex Deficiency Syndrome. They believe these people have been forsaken by the spirits and the universe, hence why they can't use magic. They're thought of as bad luck for friends and family.\n\nIt is historically a slur, but modern Estarese people have reclaimed it, using it as a term of endearment in their social circles.\n\nThe Estarese term for Forgotten Ones is \"wagami,\" roughly translating to \"evil spirit.\" It's believed that Shokuromi are their favorite hosts."
        },
        {
            "name": "Nyrellanism",
            "desc": "Nyrellanism is the most widely practiced religion on Unios. The Nyrellan Church believes in the Divines. This group of 21 gods are said to be the children of the deities who made the world, and entrusted humans, elves, and drachkin with its governance after rebelling against their parents. A descendant of the Church’s official language is the universal language of the world, and the de facto language of international business and diplomacy.\n\nAs a religion, Nyrellanism puts a great focus on service to others. The Nyrellan afterlife is only temporary, as the religion teaches that the planet only has a finite number of souls that need to be recycled. Whether one is righteous or wicked in life determines if their time between lives is comfortable or not.\n\nThe Nyrellan Church worships the following Gods:\nNyrella - Chief Goddess and namesake of Nyrellanism. Goddess of Wisdom and Justice.\nIstos - God of Lightning\nTolene - Goddess of Wind & Storms\nZybris - God of Water\nZaenar - God of Music & Art\nUctia - God of Fire\nDilene - Goddess of Love & Lust\nIra - Goddess of Magic\nZydis - God of War\nElros - God of Earth\nDaius - Lord of the Underworld\nExaos - God of the Dead\nZyntrx - God of Courage\nJihena - Goddess of Fertility\nAlnera - Goddess of the Moon\nSolus - God of the Sun\nOnir - God of Life\nEsva - Goddess of Vice\nGodall - God of Virtue\nBydall & Esyn - Twin God & Goddess of Balance",
            "sub_items": [
                "name"
            ]
        }
    ]
}

define world_institutions = {
    "id": "world_institutions",
    "name": "World & Institutions",
    "desc": "The landscape of modern Unios is defined by these institutions and organizations, as well as the people that call it home."
}

define history_unios = {
    "id": "history_unios",
    "name": "A Brief History of Unios",
    "desc": "There was a world before Unios, though none of its current inhabitants are aware of its existence. Then it ended, and some of its inhabitants were reborn as the gods who created Unios.\n\nThe first era of the world was the Age of Legends, and has been lost to time. As far as the people of Unios are concerned, the children of these Original Ones, the Titans, were the ones that created the world. The Titans ruled the world for a time. Then their children rebelled against them, as they themselves once did. The period following this second war is what gave rise to the Reign of the Divines."
}

define encyclopedia_unios = [
    political_entities,
    magic,
    lore_cosmology,
    world_institutions,
    history_unios,
]


