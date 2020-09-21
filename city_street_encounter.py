from roll import roll


# Source: http://dndspeak.com/2020/01/100-city-street-encounters/
table = [
    (
        "A homeless urchin approaches the party and claims that he used to be a great magician. He says that if the party were to give him a gold piece, he could make one of them disappear. The urchin has a teleportation sigil on the ground in front of him that is incredibly difficult to see and only activates with his command word, which happens to be ‘PRESTO!’. The character standing on the sigil is teleported to an alleyway 3 blocks down the road, into a trash pile.",
        1,
    ),
    (
        "Three semi-attractive ladies boldly harass a PC saying that s/he slept with all three of them. Creating a diversion for a pickpocket to snag the purse of the PC’s while they are distracted by the ladies. Once the pickpocket is gone, they apologize and say that the PC looks like someone they know.",
        1,
    ),
    (
        "Down the street, a person is being chased by the city guard. The guard are yelling for the thief to stop. As the thief gets close a 2nd thief causes a distraction to the guard such as overturning a wagon full of manure. The pair of thieves around the corner close to the PCs. what do the PC’s do?",
        1,
    ),
    (
        "As you pass an alleyway, a male goblin rushes out frantically and flags down your group. “Help, help, my wife is giving birth! Please, someone help us!” You look past him into the alley, and sure enough, there is a pregnant goblin grimacing and bracing herself against a crate. You get to name their firstborn if you help out, and the father will buy your party a round of drinks at the tavern he works at.",
        1,
    ),
    (
        "A charlatan offers to give a party member some fancy jewelry to advertise their business. Little did they know this jewelry has a scrying enchantment and will be used to see where the party is staying and how well defended, they are and rob them that night.",
        1,
    ),
    (
        "Roll a DC 15 Dexterity check to not get hit with the contents of an emptied chamber pot. If anyone in the party fails the check, the party rolls all Charisma checks at a disadvantage until the unlucky ones take a proper bath.",
        1,
    ),
    (
        "You see an older man yelling at his apprentice for making some mistake. The apprentice seems near tears because he’s trying to explain himself but can’t get a word in edgewise.",
        1,
    ),
    (
        "You are walking down the street when you are bumped violently aside, but when you look for the perpetrator all you see is a stray cat which seems to part the crowd wherever it goes (It’s actually a dragon casting major illusion to better mingle).",
        1,
    ),
    (
        "A child with an obvious injury begging for money pleads to the party for money. Later that day the party sees the same kid running around playing tag.",
        1,
    ),
    (
        "A shopper in the market starts going mad trying to bite the other patrons. Minutes later the shopper collapses with no memory of what happened. (In my game the person had been possessed by an animal spirit)",
        1,
    ),
    (
        "The party comes upon an ongoing street performance of a popular play. It’s an enjoyable show, until the actors start looking for members in the audience to call on stage (whether that’s because they’re malicious or they pick the most socially awkward member of the part)",
        1,
    ),
    (
        "A group of miners are protesting outside of a noble’s estate over poor working conditions",
        1,
    ),
    (
        "A gaggle of students run up to the party and demand that the oddball (genasi, orc, kenku, etc…) come back to the university with them so they can win the scavenger hunt they’re competing in.",
        1,
    ),
    (
        "You come across 4 old men sitting and playing cards. If you want to join, they let you, but because this is what they do with their lives, they are very good.",
        1,
    ),
    (
        "You see a man/woman locked away in a prison carriage, they beckon to you they are innocent and will compensate you handsomely should you aid in their escape.",
        1,
    ),
    (
        "A street performer is making music, hoping that people will pay him. If he’s very good, there’s a large crowd. If he’s bad, people walk by, averting their eyes. If the party is musical, he’s happy to perform together and split the take. He may not be honest about the split, though.",
        1,
    ),
    (
        "A friendly looking man in light brown robes approaches the party. He is surrounded by 7 golden birds. He offers to read the fortune of the party in exchange for enough coin to buy a meal and bed for the night (I usually use 5 GP). If they acquiesce, he asks them to ask a question and he answers using the Divination spell. A successful perception check (DC 15, ARC skill of +5 or higher automatically succeeds) will reveal that he hasn’t actually cast any spell, but his answers are always truthful. Once he is out of sight of the party, he disappears.",
        1,
    ),
    (
        "A homeless man/woman approaches begging for food and or shelter for the evening. Party agrees, they’ll wake up and a large sum of money sits by them but he or she is gone. If they refuse, then days later they hear in the news a man shown kindness in a person’s time of need. Billionaire gives man money.",
        1,
    ),
    (
        "A raving madwoman stops everyone she sees, telling the story of how she was the mistress of the Mayor or King. Her mind is broken, and her speech is rambling, but the stories she tells are very consistent and convincing.",
        1,
    ),
    (
        "A voice calls out from a darkened alleyway, it sounds in distress, but is quickly muffled.",
        1,
    ),
    (
        "The cobble pavement collapses in a major street revealing a dungeon (or unknown sewer beneath. In a short period of time a large portion of the city guard will come to inspect and clear crowds. A single old crippled man will climb from within the hole and collapse once he reaches the light.",
        1,
    ),
    ("A parade blocks traffic while many people stop what they are doing to watch.", 1),
    (
        "A circus strongman flexes and struts in a chalk ring. A halfling barker stands on a soap box, challenging anyone walking by to test their mettle against the steel thews of Kourteous the Mighty, Terror of the Ring! Best out of three clinches wins.",
        1,
    ),
    (
        "A very large wild animal calmly walks down the street. People run away and shout, but the beast seems uninterested in them.",
        1,
    ),
    (
        "A merchant offers the exact same items the party already owns, but if they buy anything, they will find the exact object missing from there bag. If confronted about it, the merchant will flee leaving the party with all the items, but their bags are empty (they have one of each item again). The players can buy and keep two of any item by taking it out of there backpack and holding it while buying the duplicate.",
        1,
    ),
    (
        "Several acrobats occupy a part of the street and display great skill and dexterity in their movements and contortions.",
        1,
    ),
    (
        "A tower full of boiling molasses/oil/etc. groans and collapses from atop the roof of a local apothecary/wizard. Any caught in the rushing wave of scorching liquid stand to have the flesh melted from their very bones!",
        1,
    ),
    (
        "The doors to a brewery explode open and thousands of gallons of beer rush out and swamp the streets. Many townsfolk quickly gather buckets, pitchers, and other containers and start scooping up what they can.",
        1,
    ),
    (
        "Two gentlemen or women surrounded by guards seem to be getting into a bit of a fight. They’re yelling loudly and making convincing swings at each other. They position themselves, and as one swings with all his/her might, the other ducks, and they manage to knock over one of the guards, dashing out of the circle as quickly as possible. As they pass your party, one of them tosses you a mysterious object as they pass. Along with the object is a hastily scribbled note that reads, ‘MIDNIGHT, , MEET’.",
        1,
    ),
    (
        "Two merchants stand nose to nose screaming at each other, their carts are intertwined, and they are blocking traffic. Their horses seem to be nonplussed and nibble at nearby grass.",
        1,
    ),
    (
        "You find a potion seller that had all the labels to his potions torn of in the middle of the night by a trickster rouge that has been terrorizing the city in recent weeks. To make matters worse, due to the ‘discrete’ nature his clientele, all of the potions have been bewitched so they are immune to the use of an Identify spell. He is desperately trying to sell the rest of his unusable stock at a discount to anybody passing by. Each potion is 20gp or comes in bulk packs of 12 for 200gp.",
        1,
    ),
    (
        "A man runs by, screaming, seemingly battling a large octopus that has latched itself to his head and is spraying ink everywhere. No one recognizes the man, and fewer know where one could find a large octopus.",
        1,
    ),
    (
        "You bump into a figure in a sharp traveler’s cloak. The figure either places a magic item in your pocket that is being hunted by the town guards or the figure steals a magic item from you and runs. Upon finding the figure either way you come to learn they are a royalty among the criminal underworld and want to hire you for their next big score.",
        1,
    ),
    (
        "A skilled bard is performing in a local noble’s garden. The sounds can be heard clearly outside and a small crowd of passersby has stopped to appreciate. The Noble’s guards are debating if they can/should disperse the crowd.",
        1,
    ),
    (
        "The party hears an alarm bell ringing loudly a few blocks out of sight, which is quickly picked up other alarm bells around the city. Large flagpoles around the party’s section of the city of quickly raise up orange flags, and a general call of ‘code orange’ is taken up by everyone nearby as citizens rapidly pack up stalls and evacuate the streets with practiced ease. The ground begins to tremble by the time all nearby citizens are tucked into alleys or taking shelter indoors, and within seconds of the street clearing, a stampede of brightly colored oxen around a corner and barrel down the party’s street. If the party has taken shelter, they are trapped where they are for the next 30 seconds as the small flood of animals passes by them, after which the locals quickly go about setting up shop as if nothing had happened. If the party is in the path of the oxen, they take 3d6 bludgeoning damage and are dragged 40 feet in the direction of the stampede for each turn that they remain in it, with the stampede counting as difficult terrain in any area it occupies. If the party manage to get someone to explain the situation, it is revealed a powerful but unstable sorcerer named Wizbo often conducts strange ‘experiments’ in his ‘wizard tower’, and that the particular section of the city he belongs to has adapted and developed a warning system to alert the locals to incoming magical shenanigans. In this case, a code orange indicates actual potential danger and advises citizens to clear the streets and take shelter indoors until the alarm has passed.",
        1,
    ),
    (
        "A local baker has created a new type of baked good and is giving samples to everyone. From the sounds of appreciation, it is quite good and there is already a line to both try the food and to enter the store.",
        1,
    ),
    (
        "Some of the citizens are exchanging messages in thieves cant. Messages like “it begins in 30 minutes” and “get in position”. 50% chance it’s a daring heist and 50% chance it’s a flash mob.",
        1,
    ),
    (
        "A horse, saddled and with a large pack slowly ambles down the street, the stays and ties having clearly been broken. Surely the owner will want it back.",
        1,
    ),
    (
        "The Laughing Prince, a controversial thief, has been captured. Half of the populace think he’s a hero of the people; the other half think he’s a ruthless cutthroat. His public execution is scheduled for midday in the town square, and the crowd on both sides is getting increasingly reckless and ugly…",
        1,
    ),
    (
        "Several guardsmen can be seen checking strangers to see if they paid their gate tax or if they are residents. Most people seem to have a piece of paper indicating one or the other.",
        1,
    ),
    (
        "A fire has broken out in the Market District and is growing fast. The party can work to put out the fire, can try to alleviate the panic, or perhaps try to pick up some abandoned items for a *substantial* discount…",
        1,
    ),
    (
        "A well-dressed man accompanied by two rough looking guards is politely inquiring if anyone has paid the Thieves’ Guild Tax and if they need to renew their licenses. As soon as he spots the party, he smiles widely and approaches.",
        1,
    ),
    (
        "It’s the Regent’s/Mayor’s birthday and the streets are awash with celebrations. An amiable man wearing the city colors and crest persuades (DC15 CHAR) the party to go on a discounted city tour (subsidized by the city council) of some of its less famous sites with his colleague sat in the box-seat of an elegant carriage. It is in fact a dodgy scheme to eek money out of travelers. The coachman venerates the cities beautiful attractions, recklessly hurtling the rig through the foot traffic. He deposits you at the first stop. A temple. Here a weaselly monk attempts to persuade (DC10 CHAR) the party to generously donate to the temple and depart with earthly possessions. The coachman will be very encouraging and optimistic about the next stop being enticing and is according to the coachman a renowned tailor. In the dingy shop a short scowling man will stalk the players as they browse the store, seizing any opportunity to try and convince them to buy his garments. At this point the players will have little sense of where they are without some means of navigation. The coachman is adamant that the last stop will make it all worth it. The final stop from the outside appears to be a theatre with elaborate decorations and promotions. An attractive host receives them at the doors, and leads them down a dimly lit hall, through another set of doors and into an empty auditorium. She tells them to take a seat at the front by the stage before retreating to the double doors and locking them. (2d8+3) thugs rise from the concessions stands with loaded crossbows aimed at the players heads, and the amiable man strides out on to the stage. He demands the party’s valuables in exchange for their lives.",
        1,
    ),
    (
        "One of the PCs trips over something in the street. Reaching down they find a coin purse, heavy and clinking. Just then an angry voice bellows, ‘My money! I’ve been robbed!’ The crowd steps back and a well-dressed noble point to the party and screams, ‘Thieves!’",
        1,
    ),
    (
        "A frail looking stray cat follows you no matter where you go in town, the cat seemingly following you with intent.",
        1,
    ),
    (
        "A cloaked figure ask’s where the local library is. You can hear the muffled sounds of chewing paper while he talks. And in his wake, he leaves shreds of pages.",
        1,
    ),
    (
        "A loud, colorful troupe of dwarves enter the city square; they pitch a tent and within a few hours, they announce that the traveling unarmed fight championship will be held – all who deem themselves worthy can try and earn a goblet full of gems and honor, for a small fee. Inside, a large, wooden octagonal platform sits on the center stage… but there is a trick: it stands a few feet above the ground, balancing and tilting on a stout pole on its center, and a ring-out is an immediate disqualification. The tricky dwarven fighters have specialized on pushing off opponents as soon as they enter, and those who are hardier and can hold their ground and reach the finals find that the surface starts to spin, using centrifugal force to slide them off (the champion, of course, doesn’t even try to fight and just holds to the post)",
        1,
    ),
    (
        "A group of city guards are clustered around the entrance to an alleyway. They look concerned and serious. One guard exits the alleyway, and abruptly bends over and vomits with gusto all over the pavement. If any approach, they are waved away — ‘Nothing to see here. Go about your business.’",
        1,
    ),
    (
        "A sign outside a shop selling manuscripts is crooked and jutting out into your path. If straightened or moved, a shelf of books falls over, knocking over another shelf of small paintings. Four servant boys appear in fresh finery. In the distance, the wail of a siren.",
        1,
    ),
    (
        "In a nearby back alley, an observant party member spots a lone cur, that whimpers and withdraws deeper into shadow. With skill checks, a player approaches to find: A hungry stray grateful for a bite, that reveals a secret tunnel it uses to navigate the city. Or the hungry ‘cur’ is companion to a Ranger, judging by the collar he wears. Another Ranger can communicate with him, following him to an injured/dead/captured fellow ranger. The ‘cur’ is a formidable hound badly treated by his owner. It might be a wealthy arrogant merchant, an animal handler in a traveling circus, etc. The hound can become a follower/familiar/companion.",
        1,
    ),
    (
        "A nearby building explodes, and trees rapidly grow from the rubble. Bystanders explain that this is the third attack like this in a month, and that they are the work of an anarchist collective of druids that believe cities are blasphemy upon nature.",
        1,
    ),
    (
        "Near the wizard’s college is a stand selling ice cream. Occasionally, the bound elemental keeping it cool will try to break free, causing the cart to shake. The bored teenage girl running the stand takes no notice of this.",
        1,
    ),
    (
        "A miniature stage is set up on the side of a street, within it, small illusions tell the story of great adventures slaying a beast like a magical puppet show. A crowd of children sit on the floor in front of this and adults stand a little further behind. When it ends, all the kids run off to wherever they’re going, and a member of the party feels their purse get a little lighter in the commotion.",
        1,
    ),
    (
        "A child runs up to you and tries to sneakily stab you. Her eyes pierce through her long black hair that covers her face. This little girl stares at you. You can feel an evil and malicious presence.",
        1,
    ),
    (
        "A doll or easel falls from a nearby multi-story building and nearly lands on the head of someone in the party! Anyone who looks at it feels a faint sense of unease, but it also looks expensive and valuable. You can hear an argument from the loft whose window it seemed to have dropped out of, and soon enough someone will lean out of it and ask the party if they can bring it upstairs, since they aren’t finished with their artwork. If pressed, the artist says that he has other matters to attend to and can’t come downstairs, but it’s urgent that he get that piece back and soon. Is he just rude and bad at interacting with other people? Is he afraid of the outside? Is he in danger, or is he luring the party into some kind of trap? Will he even reward the party for giving him his work back? It’s up to the DM.",
        1,
    ),
    (
        "1d4+1 Students of the nearby wizarding academy try out their newly learned spells in the alleyway and accidentally a firebolt hits the party members.",
        1,
    ),
    (
        "A man with a strange accent whose clothes incorporates the bones of animals is convincing nearby townsfolk to join him on a hunt on the morrow. Given the way that people are talking about him, he seems to be very convincing and jovial. He’s just finished talking to a couple down the street, and he’s eyed your party. He seems to be headed your way!",
        1,
    ),
    (
        "2d6 of friendly drunken hobbits ask the party to join their celebration of their newborn family member. They offer good ale and raspberry flavored tobacco",
        1,
    ),
    (
        "A bald man in robes is busy eating from a plate while also kickboxing a couple of brawny-looking folks in the regalia of the city guard. He seems to be making a fool of them. Given the crowd of onlookers, you’re not sure if this is some kind of performance or just a hilariously failed attempt by the guard to arrest this man.",
        1,
    ),
    (
        "3d6 of spectral butterflies briefly circle around a party member with the highest wisdom and then fly away. People say it brings good luck, but no one knows.",
        1,
    ),
    (
        "A famous, beloved explorer will be delivering new relics to the local museum or gallery and wants to unveil them all in a brand-new wing of the building in a few days. One of the menial guilds has backed out on contract, though, so she’s short on manpower to actually set everything up and guard the exhibition until opening day. If you’re interested, she’s hiring- and she’ll pay handsomely. Suspiciously handsomely, for menial work.",
        1,
    ),
    (
        "Random friendly dog happily brings a leather pouch containing 1d6 silver pieces and 1d4 human fingers.",
        1,
    ),
    (
        "You come across several guardsmen hoisting a large battering ram so they can heave it against a gate. It seems the city official whose mansion is behind that gate is unwilling to leave- not only are the gates barred, but the window drapes are drawn down, and the doors are bolted shut. They were supposed to show up for an important meeting yesterday, and were going to make a speech today, but no one’s heard anything from anyone inside. Most of the locals are worried- though some seem to be happy about it.",
        1,
    ),
    (
        "The players hear humming coming from underneath a manhole cover. If they open said manhole cover, they find a male gnome with a monocle and a top hat. He explains that he was trapped down there in a storm and that the manhole cover is a portal to a different realm. If the players walk into it, they end up in limbo.",
        1,
    ),
    (
        "A man in beggars robes appears. 7 tiny canaries with him. He asks the players to spare some food or coin. He is actually Bahamut in human form. If they help him, he grants them his blessing. They have advantage on WIS rolls for the next hour. If they don’t, he moves along. If they attack the canaries become Wyvern. After players are subdued Bahamut gives them a lecture on justice and charity.",
        1,
    ),
    (
        "A city-guard is busy giving a lecture to a newbie. They use the players as an example, either positively or negatively, depending on their status in the city’s eyes. For example: ‘Stop and Frisk’ if the party are scofflaws, or ‘Soliciting Bribe’ if the setting is somewhat fascist or corrupt. If the city views the players positively, the interaction is along the lines of ‘Did you see that ludicrous display last night? (Sports)’ or ‘Good day, Squire’ or something germaine to the overall plot. (‘You be safe out there; I hear the masked bandit has struck again!’) It could also be used as a way for the guards to deliver a message/invitation to the players: ‘Stop by the Station, the Lieutenant would like a word with ye’. In an espionage campaign, the Player-Guard interaction may be used to communicate with the team secretly; falsely arresting and then slipping a message or dragging in to talk in a theatrical manner. It could also be used as an intimidation tactic by a well-connected political figure who controls the guards and has made enemies of the players… (‘This is a message! *smash!*’)",
        1,
    ),
    (
        "A gaggle of urchins hurries through the crowd city streets towards the party. One of them makes eye contact, before hurrying past and heading around a corner. The city guard pushes their way forward asking everyone if they saw which way the kids went.",
        1,
    ),
    (
        "The noonday bells only chimes twice before the rope holding the bell snaps and it plummets down the steeple, landing with a resounding gong, blowing the temples door open, and making many townsfolk believe there is devilry afoot.",
        1,
    ),
    (
        "While walking by the stocks, one of the prisoners recognizes someone from the party, and asks a favor. Could be something as simple as scratching an itch they can’t reach themselves, or perhaps something more involved.",
        1,
    ),
    (
        "An intelligent huge mimic on a sturdy roof top of a one-story building with other several buildings snug down on both sides. The mimic mainly stays on the edge of the roof draping a part of itself down the side of the tight alley side outside wall. It forms itself as a wet metal ladder. As an added incentive the mimic drops coins from pervious victims a few at a time to bait its ladder. When someone grasp hold of the ladder (both hands and a foot hold), the mimic exudes its adhesive and grapples by rolling up its ladder/self at the same time. The mimic eats atop the roof.",
        1,
    ),
    (
        "A woman is being attacked by thugs. If you ignore her cries for help, she gets taken away. If you help her, she takes you to her home where she and her sisters reveal themselves as succubi and try to kill you.",
        1,
    ),
    (
        "You see a drunkard stumbling about. He greets your PCs in a friendly if overly affectionate manner before shuffling off singing at the top of his lungs.",
        1,
    ),
    (
        "There is a striped carriage with the number 53 on the side that is someone moving uncontrollably without any houses (or driver for more modern RPG).",
        1,
    ),
    (
        "A War-priest with a flaming sword steps in your way. He’s limping and looks beaten up but holds himself proudly. ‘So here it ends.’ he speaks as a bewildered look slowly enters his face. ‘You’re not them. I’m very sorry, please go along.’",
        1,
    ),
    (
        "A small critter (of the DM’s choice) appears to be causing chaos, as everywhere it scampers people flee in horror.",
        1,
    ),
    (
        "You stumble upon an alleyway chat and discover one stall in a nearby busy market is rigged to detonate in a Fireball when a specific noble approaches.",
        1,
    ),
    (
        "You step in some viscous green goo… and it slithers away from you into a nearby sewer grate. The ground rumbles.",
        1,
    ),
    (
        "The street is literally alive. This part of the city was built over a large Earth Elemental, but it doesn’t seem bothered to carry people to their destinations. However, it decides to block the adventurers from entering the street.",
        1,
    ),
    (
        "A bird plummets from the sky right on a party member’s head (1d4 physical). There is an arrow right through it… and a missive attached to its back. Someone didn’t want this getting to its destination.",
        1,
    ),
    (
        "A street magician decides to turn your party’s most anger-prone member into a joke. He uses prestidigitation to cover them in slick oil, change the color of their hair, and untie their shoelaces, all while mocking them.",
        1,
    ),
    (
        "A piano crashes down 1d4 meters away from a party member. It must have been pushed off the balcony of that nearby building. But who would toss a piano out of a balcony?",
        1,
    ),
    (
        "A person explodes in a gout of fire. Then 2 more nearby. A creature is possessing these victims before they ignite. Then the creature turns on the players! It could be that the victims (or at least one of them) are connected somehow. Are there more victims throughout the city? It’s clear that the heroes must find this out before it happens again!",
        1,
    ),
    (
        "Household ‘Otto-Servant’ warforged automatons have recently become a trend among the well to do. Their inventor sends a message to the players asking for help using an unassuming middleman as a messenger. It seems the inventor fears for their life, as they narrowly escaped a lethal attack by one of their inventions! Tales of similar attacks spread like wildfire the following days – copycat attacks seem to be happening! Can the players protect the life of the inventor, and discover the conspiracy behind the attacks?",
        1,
    ),
    (
        "A rag-picker with his towering cart of discards rushes into your path. They stumble on a cobblestone, bringing the entire trolley crashing down on the street. You see glints amongst the strewn linen and furs …",
        1,
    ),
    (
        "A promoter catches sight of the party and seizes the opportunity. Each player must take a DC 10 CHA check or have a wristband for the all new bar ‘The Whore’s Shoe’.",
        1,
    ),
    (
        "A throng of protestors block the road, bearing banners with slogans such as ‘Ditch the Witch’ and ‘The hag’s a hack’. The leaders of the group, a human druid in an impressive headdress, and a dwarf Bard with a powerful voice are getting the frustrated crowd riled up with a powerful speech about the decadence, intransigence and failures of the powers that be.",
        1,
    ),
    (
        "A few guards march past with a scrawny street urchin in tow. The child is manacled and clearly in pain.",
        1,
    ),
    (
        "An unkempt mage is staring at a lamppost, seemingly transfixed. He stands with a relaxed posture and smells of ozone",
        1,
    ),
    (
        "You spot a fruit seller dragging a cart through a solid wall and vanish. Inspecting the wall, it appears to just be the solid outer wall of a general store",
        1,
    ),
    (
        "A street artist is making portraits for a reasonable price. The images seem to have a life of their own, with the faces smiling and winking at passersby. Some complete examples on the flagstones around him showing detailed backgrounds and activity but no actual muse. None the less the frames have the ‘depicted’ individuals name painted in gold letters.",
        1,
    ),
    (
        "3 drunk students from the mage’s college are causing a ruckus in the street, causing hijinks and hilarity with their cantrips. One of them takes issue with the PCs, mistaking them for a reviled enemy. The gang tries to assert their dominance and challenges the enemy and their ‘minions’ to a fight.",
        1,
    ),
    (
        "A pack of (2d4 +2) rabid dogs bursts from an alley, directly in the path of the party.",
        1,
    ),
    (
        "A chieftain born aloft on his vast shield by the shoulders of four tattooed warriors is rushed through the crowd, tailed by a Dwarf with a winged helm and a Goliath in striped pantaloons.",
        1,
    ),
    (
        "A man in long white stockings with a glamorous golden quiff and accompanied by a small white dog disturbs the party to ask them if a hairy man with a black beard wearing a tricorne hat has been through here. Apparently, the man has stolen something very dear to him and must be found at once.",
        1,
    ),
    (
        "A masked figure in a billowing black cloak leaps across the street from one rooftop to another. Their polished black mail gleams in the light. A smaller figure in a colorful leather jerkin with a quarterstaff strapped to their back jumps after him.",
        1,
    ),
    (
        "You walk past an elite’s compound as an angsty looking teenager emerges from a side-gate. They glance at the players and slouches off. After a minute or so banshee like screams emerge from the building…",
        1,
    ),
    (
        "A building is being demolished on the street. The wrecking crew are on a break.",
        1,
    ),
    (
        "A panicked crowd stampedes down the street. In the havoc you see innocents stumble and be crushed by the terrified crowd. Through the wails and screams you can hear one word: Giant.",
        1,
    ),
    (
        "A sewer collapses into a sinkhole during heavy rains. Half of a neighborhood is now thirty feet underground. In a poor one: many people may be trapped beneath the rubble and possibly drowning. but only a few heroes care enough to try and save the victims. Will those greedy land-developers get their way and clear out those dirty poor people once and for all? Was this part of a planned attack? In a wealthier neighborhood: a few gold-pieces and trinkets hint that the sinkhole may hide a treasure cache; a wealthy noble might mourn the loss of their precious object-d’art and pay the heroes to delve the hole to retrieve it. Anywhere: a small horde of 3d6 low-level semi-intelligent sewer monsters emerge, shouting abuse at the ‘sky-demons’ who just invaded their home; swarms of vermin; slip-and-slides; and a labyrinthian network of secret tunnels!",
        1,
    ),
    (
        "A drug addict pleads for money from the players. He is suffering from the shakes, with his eyes darting in separate directions. He stammers unintelligibly in a hoarse voice, wringing his hands desperately. If the players don’t help him out, it is revealed the addict is possessed by a Shadow Demon. He has the same stats as a commoner with +2 to DEX, INT, and CHA. He has the same resistances, immunities, vulnerabilities and abilities as a Shadow, and knows the spell Deeper Darkness and Shadow Evocation.",
        1,
    ),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {roll(table)}\n")


if __name__ == "__main__":
    main()
