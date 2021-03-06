from roll import roll


# Source: http://dndspeak.com/2018/01/04/100-gods-and-goddesses/
table = [
    ("The Allfather – Ruler of the gods and creator of humans and other races.", 1),
    (
        "Război – One of two gods of war. Although often seen as bloodthirsty, he actually hates war. He encourages brutality so that people will fear war and try to avoid it.",
        1,
    ),
    (
        "Erou – One of two gods of war. Generally the more worshipped of the two, being seen as the goddess of honorable war. Loves the thrill of battle and she appreciates it most when her worshippers fight battles in her name.",
        1,
    ),
    (
        "Nälij – Goddess of knowledge. Legend says she lives in an eternal archive with the knowledge of all that does, has, or will exist.",
        1,
    ),
    (
        "Rymat Samiar – Demigod of bridges, ferryboats, and fjords. Samiar was born a mortal who later achieved great renown for his swordplay, trickery, and legendary ability to escape from the most secure prisons in the multiverse. His most famous exploit was escaping from the afterlife by transforming into a frog and swimming back across the Stream of Life. He tricked the Servitor of Death sent to retrieve him to make a bargain that he would protect others from mishaps when fording the Stream if he could remain free. Now he is invoked by those wishing a safe crossing across rivers and streams. He usually appears as a rapier-wielding bipedal frog.",
        1,
    ),
    (
        "Ismaros – God of stalking. The hooded figure looks a bit like the grim reaper, but without being a skeleton. He is not very popular, but he is always there, always watching everyone and everything. If you wish to make a deal with him for information, it will come at a great price.",
        1,
    ),
    (
        "Edrun-Of-Far-Places – God of the unknown and the wanderer, dressed in a traveler’s cloak patterned with stars. He has no realm in the Astral Plane and instead is believed to wander the mortal realm.",
        1,
    ),
    (
        "Talichtoli – God of Murder, justified or unjustified. Talichtoli’s symbol is a simple bone knife, and they gives their aid to any who truly wants someone dead.",
        1,
    ),
    (
        "Pocaba, Lady of Islands – Goddess of sailors, fishermen and any who lives away from the mainland.",
        1,
    ),
    (
        "Hornfels – Dwarven god of home and hearth. It is common for members of any faith to keep a statue of Hornfels on the mantle. This god demands no worship, no tradition. Warming yourself by his protected hearth or eating food cooked at his hearth offers a kind of boon over the years. A request for home and safety can be made. Locate an outcrop of rock and, using soot from a campfire, draw a door-frame on the stone or boulder. The door-handle is drawn with a special rune. If done correctly and by the right person the door will materialize and a hearth and bed will be waiting inside the stone.",
        1,
    ),
    (
        "Fýsi – Goddess of the reclaiming wilds. When disaster strikes a town and buildings or lives are lost, that is the work of Fýsi, she takes back the man-made. Followers of Fýsi are nomadic and travel between villages on the outskirts of the wilds. Followers of Fýsi are not so much protected by her, or sent by her for specific bidding, but rather understand that Fýsi will act and it is a question of disaster, or a safe offering. They understand that Fýsi acts to protect nature and her disasters are akin to the lashing out of a scared animal, when her home is encroached by mankind. Followers are often offered respite in abandoned buildings in the village. Often, disaster can be warded off when followers arrive at the village and suggest safe homes and objects to offer to nature, so that disaster can be averted. Rangers and hunters will seek out these followers for blessing to avoid animal attacks and other dangers of the wild. A common ward is a packet of seeds kept in a cloth pouch with dry earth from their village. As long as the traveler keeps the soil dry, they will be safe.",
        1,
    ),
    (
        "Calais – God of vigilance and domesticity. Domain: Life/Light Calais is not the most powerful or well-known god, but among the pantheons he is the most well-loved. Keeper of homesteads and of vigils he comforts the wives whose husbands have gone off to war and keeps hope alive in the hearts of men who are in far off and possibly dark places. Although his representation among clergy has diminished over time, he keeps the hearth alive and warm for all mankind.",
        1,
    ),
    (
        "Noklaji – The Construction god, representing the expansion of cities and towns. This gnomish god is a deep gray all over and always carries a wooden plank with a nail in it as his weapon. Protects buildings and the people inside.",
        1,
    ),
    (
        "Vigo – Faceless Prince, Master of Lies, Patron God of Actors and Charlatans. Shapeshifter, Facechanger, the Great Mimic. Has no temples but a yearly festival where a parade of masked worshippers marches through cities. His holy symbol is a plain gold coin with two eyeholes, but any mask can be used to depict him.",
        1,
    ),
    (
        "The Crone – Goddess of Mists, Magic and Prophecy. Worshipped primarily by the river halfling nomads, she is a little known deity and very mysterious. It is said these Halflings read the cards each morning to determine her will for them, and that her chosen on this earth (often an elderly female seer), is imparted with some of her divine manifestation.",
        1,
    ),
    (
        "Samuqan – God of the Desert, Sun and Stars. He is known as a god of little mercy because of what he did to the land, but also as a guide for people, using the stars to help travellers find their way and tell their history.",
        1,
    ),
    (
        "Sangasu – God of Storms, known as a destructive force of nature, but necessary for renewal. It is believed he kidnapped [Goddess] and forced her to help him make monsters.",
        1,
    ),
    (
        "Naphistim – God of the Sea and Sand, people worship him when they need to travel through harsh and unforgiving places. They often give thanks to him by way of sacrifice as a reminder of their mortality, but also their strength.",
        1,
    ),
    (
        "Mezizi – God of Time and Death. All things turn to dust and sand, many are burnt in funeral pyres to honour him as it is he who allows life even in the harsh climes of the deserts and wastes.",
        1,
    ),
    (
        "Lugalme – Goddess of War and Fire. This goddess is the heat of passion and bloodlust, embodied literally as fire, she is prayed to in times of tragedy but also renewal, consummation and of course, before war.",
        1,
    ),
    (
        "Amarazen – God of Protection and Life, she is said to be the one that guided [city’s founder] to the oasis that made [Desert city] possible. Those who anger her are given visions of water that isn’t real. Most claim her essence rests in the oasis and so the largest temple belongs to to her as she allowed them to live at the oasis’ side. Thus all who wish to take from the waters must pay tithes to the temple. She is secretly the goddess of secrets and sacred knowledge.",
        1,
    ),
    (
        "Elutil – Goddess of Monsters, Madness and Evil. Often depicted as an elderly woman, Elutil is cursed and hated by the people as the mother of Hags. Thought to have created most of the monsters in the world, it is hate and fear that strengthens her.",
        1,
    ),
    (
        "Delondra – Goddess of Woe and False hope, but at the centre of her machinations is the promise of something greater. She is a fickle Goddess, known to test mortals, sometimes out of sadistic humor and sometimes from a desire to help. She is also a Goddess of Hope and Risk.",
        1,
    ),
    (
        "Toitel – God of Travel, Wandering and Beasts. It is said he walks the world and has no domain other than where he stops to rest each night. He carries a shell on his back that looks like a rock to hide from people. Those who find him, he blesses with luck.",
        1,
    ),
    (
        "Caileon Le Corre – God of Protection, Music and Joy. He was sad to be a human who saved thousands from disaster and so was worshipped by them. He is depicted with a ring of swords and a lute. In times of revelry, some say they can hear his voice, keeping the party alive.",
        1,
    ),
    (
        "Prophet of Harvest – All who wish for a plenty to befall them pray. A god of Hunting, Harvest, Wellness, Livestock and Famine A skeleton god, with a complete digestive system, the ribcage being filled by a beehive. Offerings are made with fresh meat, honey and pommegranites.",
        1,
    ),
    (
        "Michizane – patron god of learning. Often students will pray or provide offering ahead of a major exam. He is known to be fond of poetry, plums and oxen. Legend tells of the time a nobleman closed down a library, to expand his palace. Misfortune had befallen the nobleman and his family, until they reopened the library and built a shrine in his honor. His holy symbol resembles a plum tree.",
        1,
    ),
    (
        "Molac – God of Flame, Red Dawn, Flame Tyrant. The god of the primal wild nature of fire. He represents chaos, and that is passionate (love, art, war. etc…). He appears as a being made from flame bearing a mask made of blackened wood. He represents things that are all consuming and destructive.",
        1,
    ),
    (
        "Tempsdule: God of time – Born out of the fragmentation of Relatitus, former Deity of The Singularity, Temspdule lives in a temple on the Moon, guarding and manipulating the Universal Hourglass, that controls all time in the Multiverse.",
        1,
    ),
    (
        "Metria – Goddess of space – Also born from Relatitus, Metria dwells on a mile-high tower on the Sun, which she moves and protects, using it to coordinate the movement of the planes.",
        1,
    ),
    (
        "Decepscher – God of illusion – Worshipped by illusion mages, Decepscher is often depicted as an artist, using a canvas and paint to shape the perception of reality. It’s said he lives in a personal semi-plane, where all normal concepts of space and time are irrelevant.",
        1,
    ),
    (
        "Aveli – Deity of birds – Once a majestic winged creature that soared through the skies of the old world, it created all the bird species, and sacrificed it’s own flying abilities in favor of it’s creation. Penguins and emus are a question Aveli refuses to answer it’s followers.",
        1,
    ),
    (
        "Falkorta – Goddess of luck – Ironically, she’s worshipped by strategists and leaders, who believe chance plays a huge role in any important event. She decides who to give her blessings, and does so to anyone, just to make it look like she’s neutral, even though she prefers to bring luck to those who never give up. Usually takes the form of a small pink dragon.",
        1,
    ),
    (
        "Icholese – The Lady of the Lake, the Teal Stream. Godess of lakes, rivers, and all inland waters. She protects the health of her people by granting them pure water and healings. She can take the form of a great predatory fish or a willow. Her fidels often throw offerings in ponds and ritualistically drown sacrifices",
        1,
    ),
    (
        "Doran – The God of the Forge. He is a Dwarf with a mighty hammer in hand and towers even Orcs in size. It is said that the unique weapons that Dwarves use come from Doran telling them how to make it when they sleep. These same legends say the weapons are to have a greater purpose in the future against an unknown enemy.",
        1,
    ),
    ("Bob – God of the mundane.", 1),
    (
        "Peolai – Goddess of luck. Big on irony, she tends to make life chaotic for those people most staunchly committed to our ability to control our own destiny. On the other hand, for those who rely upon luck and appease her, their good fortune becomes almost predictable.",
        1,
    ),
    (
        "Lelia – One of the twin druid gods, Lelia is the opposite of Vadaszat. Called the Mother of Nature, the owl-headed goddess represents life and balance in nature. She and Vadaszat select a shared mortal champion from among their druids, called the Skinwalker.",
        1,
    ),
    (
        "Vadaszat – The second of the twin druid gods, Vadaszat the Huntmaster is the brutality and ruthlessness of nature made manifest. Appearing as a man with a deer head, he stalks the world’s forests at night hunting prey for sport.",
        1,
    ),
    (
        "Aussiria – Goddess to Kobolds, Dragonborn, and other races with draconic heritage. It is said she was born a pure white color, and emanated a powerful good aura unlike her brothers and sisters. Unlike other chromatic dragons, she values kindness and well being over power and hatred. Draconic societies that worship her are therefore very welcoming with their hospitality to outsiders, though they are not against using claw and breath to maintain the sanctity of their homes.",
        1,
    ),
    (
        "God of the Forgotten – you know how sometimes you wash your laundry and sometimes you end up missing a few socks? They’re his now. Orphanages hold a special place in his heart, and any legends, stories, or prophecies lost to time are his to know.",
        1,
    ),
    (
        "God of Belief – If an “AllFather” or “God of Creation”, or “King of Gods” had an origin story, it would be because of this god. Following through on superstitions (like knocking on wood, or throwing salt over your left shoulder) is worship to him, and as this God is of Belief, he is able to create new Gods–which may or may not be properly thankful for their creation (e.g. “Oh hero, it is because of your belief that I am alive! Here is a boon.”). His true form cannot be seen by anyone, as anyone who sees him sees what they believe he looks like.",
        1,
    ),
    (
        "Goddess of Choices – Much like her sister the Goddess of Luck, this goddess is more on the “cosmic” scale of things. Able to see other outcomes for different choices–and depending on the outcome of the choice and whether or not you are in her favor, she may let you choose the more fortunate path. Alternatively, if you piss her off, she may send you down the more destructive path–even if it seemingly looks like the best path, at the moment. She is fond of games that require logic or math.",
        1,
    ),
    (
        "Goddess of Elements – not just of water, nor solely of fire, air, or earth–and certainly not “mother nature”. “Element” golems worship her, as it is she who grants them life. She has a particular fondness of fire and lava–or, really, any of the “heated” elements. Being a high priest in her temple means remaining virginal–she rewards loyalty with immunities.",
        1,
    ),
    (
        "The Gray God – A solitary genderless god, half pure evil and half pure good, both sides are eternally in pain from the others’ existence. Worship at their feet means relief of pain from it’s existence, and with relief brings information that Good can use against Evil–as well as information Evil can use against good (both pieces of information are given at the same time to the one worshiping). Also could be considered a god of wealth, the Gray God also finds pain relief in donations of silver coins (melted in sacrifice). The larger the donation, the more your alignment slides towards True Neutral.",
        1,
    ),
    (
        "Goddess of the Gift – any time something is given selflessly, or out of good will to another is worship to her. Fun fact: any version of “Santa Claus” on any version of reality is her champion. Usually “appears” to those who have great potential but are in dire straits–she isn’t ever actually seen, mind you, but something draws her target to whatever gift she’s left behind. Typically, her gift is contextual in nature.",
        1,
    ),
    (
        "The Write/ReWrite God – authors/bards pray to him, their worship is books/songs, his temples are libraries/music halls. This god looks like… well, like a shut-in middle-aged male with a pencil on his ear, glasses down his nose, and rumpled up dark-brown hair with silver streaks on either side. If your adventure, your quest, whatever mission you’re on, is not going well… you pray to this god, and hope he doesn’t find your story exciting. If your downturn of events makes for a good book, he will ignore you, and may even possibly send more challenges your way; but if you seem unjustly getting the wrong end of the stick (so to speak), he will erase what’s happened, and re-write it so you come out better.",
        1,
    ),
    ("Spencer – God of storytelling and beards.", 1),
    (
        "Vance – the god of deceit, mischief, and insanity. Represented by a smiling gray mask. He blesses those who worship him with insanity and power. On the occasion that he comes to the material world, or a follower gains his spirit, he tends to go to casinos and bet everything he has on him. When losing, he burns the place to the ground. He is known to take any bet, whatever the chances.",
        1,
    ),
    (
        "Judrod – Goddess of lost causes. Taking the form of a brief spark of light, this goddess is known to appear when all seems lost. A flash in the eyes of a sickly child just before a miraculous recovery, a glint off a rock that momentarily blinds an executioner, a meteor in the sky that leads a starving man out of the forest: all these are manifestations of her brief favor. Impossible to prove from mere coincidence, her boons are nonetheless real.",
        1,
    ),
    (
        "Paxe – the god of peaceful passings. Taking the form of a kindly stranger, this god will appear at the side of those dying in pain or in fear and will comfort them until they claimed by Death. Paxe will grant blessings on those that nurse the sick or comfort the troubled. Necromancers and torturers earn the god’s wrath, as Paxe will reveal in harsh detail to them how they will die.",
        1,
    ),
    (
        "Fortuna – goddess of luck and gambling that celebrates fair play. She will never alter the outcome of a game of chance, but will often grant boons to those that willingly risk everything. Appearing as a smiling beauty with fire red hair, she might gift a gracious loser at a casino with a priceless ruby or a winner at a card game with a passionate kiss. Those that cheat at games of chance, though, earn her wrath and instead see her moments before meeting a grusome end in a random accident.",
        1,
    ),
    (
        "Azuiar – Secret god of preservation. On the surface, Azuiar is a god of evil, the proverbial devil on your shoulder convincing you to do bad things. In reality he chose to adopt the mantle of the evil god out of fear that the world was changing too drastically toward good. Azuiar is the god of all who wish to corrupt and do evil for its own sake.",
        1,
    ),
    (
        "Entaros – God of the Soil- A massive giant ridden with dirt, grass, and plant life. Many say he is made of stone himself, with a heart of diamond. Legend has it, the most rich soil is that which clings to his back, and that those who worship him will be granted with the ability to grow all plants in any location. He rests in the earth, appearing to be a huge overgrown mountain. Many druids and those who respect nature are his followers.",
        1,
    ),
    (
        "Knaben – God of archeologists and ruins, he guides those who seek lost knowledge. Mostly invoked to protect graves and monuments from grave robbers, buildings blessed by him are immune to the wear of the elements, at least until someone recovers their secrets.",
        1,
    ),
    (
        "Ub’took – God of Aliens: A disliked loner of a god that has taken an interest in mindflayers, beholders, and other aberrant creatures. Most aberrations stick don’t worship him or even acknowledge his existence but Ub’took does have a small following. He is also a patron of all mortals who study alien lore and magic.",
        1,
    ),
    (
        "Nurggle – God of the unclean. Nurggle thrives on the rot and decay of all things as he and his followers see it being the common denominator of everything. Nurggles avatar is the form of a Giant/Orc hybrid with the broken antlers of an elk. He wishes for the decay of not just physical entities but also society, love/purity in relationships, and advancement. His followers often douse townsfolk with their chamberpots and exhume corpses in the name of Nurggle. Nurggle only appears to mortals when they have destroyed or desecrated something of great sentimental worth, when he reveals himself he will complete one task for a mortal so long as it is vile and distasteful. No Lawful or good alignments would worship this deity.",
        1,
    ),
    (
        "Mamcho – Humanoid woman, solid gold eyes, long curly hair, light brown skin, radiates a warm light. Dressed in white robes. Goddess of hospitals, harvests, the home, and family. Patron goddess of parents, doctors, and patrolmen. Described as being very warm and friendly. Symbol: The shield, can be found carved into the cornerstones of fortresses and above the entrances of homes.",
        1,
    ),
    (
        "Masnach – Humanoid man, jet black skin with piercing blue eyes. Dressed in rags and carrying a shepherd’s staff. God of travel, shipping, and trade. Ship launchings involve a prayer to Masnach. Patron god of sailors, pilgrims, and the lost. Associated with lambs and sheep. Most likely to visit mortals. Described as kind, quiet. Symbol: The face of a lamb, can be found on all coins.",
        1,
    ),
    (
        "Nador – A very large black owl with eyes like spotlights. God of dreams, science, investigation, research, and above all else: the truth. Patron god of wizards, teachers, detectives, and fortune tellers. Associated with books and learning. Often appears in dreams. Never speaks. Symbol: The eye, can be found at most libraries. “None can hide from the eye of Nador”",
        1,
    ),
    (
        "Rhyfedel – A giant skeleton covered in black resin, the skull above the mouth and jaw is a large brain. God of madness, manipulation, and torment. Patron god of none. Very rarely seen, supposedly he never stops screaming. Symbol: His own face.",
        1,
    ),
    (
        "Yunni – Genderless humanoid, described as a bald monk dressed in orange robes with 8 arms. Its body appears to be made of pure white light and it speaks in thousands of voices at once. God of balance, control, and grace. Patron god of martial artists, sculptors, and dancers. Associated with fire and lightning. Appears only to those who reach true inner harmony, tends to be very direct but patient. Symbol: The scales.",
        1,
    ),
    (
        "Gwallus – Has never been seen or heard. God of lies, conspiracy, and secrets. Patron god of spies and saboteurs. Natural enemy of Nador. Symbol: A circle with three dots in the middle.",
        1,
    ),
    (
        "Perthor – A semi-humanoid man in ragged clothes and a wide-brimmed hat. 17 feet tall and extremely thin, his body appears to be made of very old wood and he is covered in moss and other plant life. His head is a ball of shadows with two glowing yellow eyes. God of life, death and the natural order, patron to all druids and enemy of all necromancers. He is totally unwavering and infalible, acting as gatekeeper to the underworld and as a symbol of the inevitability and finality of death. He has appeared exactly 3 times, each time rising from the ground, grabbing a mighty necromancer by the throat and dragging them to the underworld. Symbol: A metal gate. “None shall pass.”",
        1,
    ),
    (
        "Yera – A giant white stag, may sometimes take the form of a human. God of change, the seasons, and time. Patron god of farmers and animals. Rarely seen. Symbol: The stag.",
        1,
    ),
    (
        "Pydros – the patron god of oaths and of friendship – Pydros is often thought to be the defining link between the gods and mortals for the basis of worship of any gods. Pydros is prayed to before every legal hearing in the land, and between those who share a close bond friendship and honor.",
        1,
    ),
    (
        "Araknev – scorpion god of darkness, trickery and deceit. Araknev is an ageless alien entity drawn by great shifts in power or promising evil presences in the multiverse. He is charismatic and manipulative, and seeks to shape all reality in his fiendish, twisted image. His followers turn on their former allied overnight, betraying their way to power and wealth.",
        1,
    ),
    (
        "Israfiel – God of Angels. A former Solar, Israfiel generated enough of a following on his own to be revered as a god among angels. While not particularly well-known on the material plane, Israfiel’s domains include the upper planes and ascension, making him the patron of those who wish to serve in the heavens when they die. He is a paragon of lawful good to such an extent that he’s seen by those that know him as a metaphysical constant that helps define what it means to be ‘good’.",
        1,
    ),
    (
        "Jack – God of Deals. ‘Jack’ goes by many names to many different people but most often introduces himself as ‘Jack’ to people meeting him for the first time. While he is a devil god of immense power, Jack is bound by only being able to effect what others allow him to. He authors and abides by countless deals and contracts with mortals in order to spread his influence and power and open up more avenues to actually exert his strength. For a devil, he is surprisingly open about his motives and speaks plainly about what he offers to others and why. He appears to mortals as an unassuming-looking human or elven man wearing impeccable clothing and is courteous, often greeting people with the line, “Pleased to meet you,” and describing himself as, “A man of wealth and taste.” Lawful evil.",
        1,
    ),
    (
        "Myshta – God of X Forest. A lesser god, not even truly considered one by some scholars, Myshta is a god whose domain is local to and entirely contained within a single forest. Within her forest, she is an intellectus (localized omniscience) and can see, hear and understand that state of anything that calls her forest home. She wills her forest to grow and spread and doesn’t take issue with creatures living within her forest but can be aggressive and vengeful towards those who threaten the lives of the plants and creatures that make up her domain. True neutral.",
        1,
    ),
    (
        "Sedyne – God of Brawlers. An ascended mortal of ages past, Sedyne was well-known for being a remarkable fighter long before her ascension to godhood. Now she encourages aggression, violence and combativeness among her followers. She is that patron that pit fighters and brawlers will pray to for the stamina to go one more round or the strength to deliver a debilitating blow. Chaotic, impartial to good/evil.",
        1,
    ),
    (
        "Audalma – The Coming Dusk: Goddess of the Setting Sun – Audalma is the third aspect of the Cycle of Night and Day. Garbed in thick cloaks made from the subtle colors of sunset, she embodies the spirit of closure and change; a belief that something’s end is what gives it meaning, and that with every end there is a new beginning. As the The Coming Dusk, Auphaela has a silver-gray bun that glimmers with various reds, pinks, and oranges, and a quiet smile perpetually on her elderly face. She is comforting and accepting while also being nostalgic and wistful, always advising due consideration and reflection in nearly all situations, which can make her seem indifferently removed when dealing with other gods or even mortals. Followers of The Coming Dusk are much like the aspect herself in their contemplative attitude and behavior, and often Seek fulfillment through change and repeated meditation. The Coming Dusk is prayed to whenever someone is going through a change or reaching a conclusion to something meaningful, whether it is a way of life, a relationship, or something else that is comparably meaningful. Those who worship this aspect find themselves more tranquil and clear minded when going through tough transitions or experiences, and those that dedicate themselves entirely to it have the possibility of being able to channel her divine powers of finality and change.",
        1,
    ),
    (
        "Augelva, The Hidden Pinnacle – Goddess of the Midnight Sun – Augelva is the fourth and final aspect of the Cycle of Night and Day. Garbed in a veils made from the velevet inky darkness of midnight, she embodies the spirit of improvement and drive; a belief that there is always room to improve, no matter the presence or absence of adversity. As the The Hidden Pinnacle, Augelva has brilliant white braids specked with blonde spots resembling stars, and a determined smirk perpetually on her mature face. She is persistent, focused, and motivating, always advocating for improvement and the chance to better oneself in nearly any situation, which can lead to her appearing unrelentingly single minded when dealing with other gods or even mortals. Followers of The Hidden Pinnacle are much like the aspect herself in their ambitious attitude and behavior, and consistently seek to make a name for themselves in whatever they decide to do. The Hidden Pinnacle is prayed to whenever someone is attempting to improve themself or pursue a goal that requires dedication, whether it is a work project, trying to learn a skill, or another form of concentrated pursuit. Those who worship this aspect find themselves improving at a faster rate when dedicating themselves to something, and those that dedicate themselves entirely to it have the possibility of being able to channel her divine powers of growth and improvement.",
        1,
    ),
    (
        "Auphaela, The Breaking Dawn – Goddess of the Rising Sun – Auphaela is the first aspect of the Cycle of Night and Day. Garbed in robes made from the soft golden glow of dawn, she embodies the spirit of renewal and rebirth; a belief that something beautiful will always come, no matter the bleakness of what comes before. As the The Breaking Dawn, Auphaela has pale golden locks that are almost white, and an inspiring grin perpetually on her youthful face. She is gentle, warm, and encouraging, always advocating for forgiveness and the chance to repent in nearly every circumstance, which can lead to her appearing naively optimistic when dealing with other gods or even mortals. Followers of The Breaking Dawn are much like the aspect herself in their welcoming attitude and behavior, and often participate in charity of all sorts in order to help others out of their misfortune. The Breaking Dawn is prayed to whenever someone is about to embark on something new, whether it is an experience, a friendship, or a similarly momentous occasion. Those who worship this aspect find themselves more fortunate when starting something, and those that dedicate themselves entirely to it have the possibility of being able to channel her divine powers of rejuvination.",
        1,
    ),
    (
        "Auchelda, The Brilliant Zenith – Goddess of the Peaking Sun – Auchelda is the second aspect of the Cycle of Night and Day. Garbed in a gown made from the harsh yellow glare of midday, she embodies the spirit of potential, ability and triumph; a belief that through there is no better time than now, and that those who strive harder can always achieve victory. As the The Brilliant Zenith, Auchelda has luscious blonde locks that shine powerfully with a light of their own, and a confident look of amusement and confidence on her mature face. She is proud and stern, yet pleasant, always standing by deserved achievement and making the most of what there is, which inevitably leads to her appearing dominant and proud to an almost overbearing degree when dealing with other gods or even mortals. Followers of The Brilliant Zenith are much like the aspect herself in their motivated attitude and behavior, and often engage in competitions of all kinds to prove their competence when they aren’t training for perfection. The Brilliant Zenith is prayed to whenever someone is faced with or completes a challenge of some sort, whether it is a fight, a flash of inspiration, a moment of temporary genius, or a similarly important appearance of success. Those who worship this aspect find themselves with increased prosperity when reaching to go farther, and those that dedicate themselves entirely to it have the possibility of being able to channel her divine powers of strength and superiority.",
        1,
    ),
    (
        "Issha, who stands against the storm – Despite being a storm deity, Issha does not control the storm. The force of weather is a force too massive and too chaotic to be controlled. Rather, it is Issha’s job to fight and hold back the destructive power of the storm, because left unchecked, it would render the world barren and uninhabitable. Issha is a lawful good tempest deity. Followers of Issha understand the power of the storm, and work to ensure that it doesn’t wreck chaos. They can be found rebuilding towns ravaged by tornadoes or hurricanes, or designing storm proof shelters or walls for cities.",
        1,
    ),
    (
        "Callatti – Goddess of rebirth and forgiveness. Prayed to by those who wish to repent their transgressions and seek a path to redemption.",
        1,
    ),
    (
        "Illuri – Goddess of fertility. Infertile couples place the first sprouts of the harvest at her altar.",
        1,
    ),
    (
        "Matala and Nasheth – Maker of the world/God of Decay. Brought from far travelers that came from the south, Matala is the goddess who shaped the world from nothingness and imbued it with life. The barren places of the world are said to be the work of Nasheth who, in his jealousy for what Matala created, seeks to add blight to her creation out of spite. Nasheth is worshiped by necromancers and those who use magic to spread death and decay.",
        1,
    ),
    (
        "Ignotus – God of the unknown. Everything about him is unknown, he has no face and appears with a straw hat.",
        1,
    ),
    (
        "Yehven – Goddess of four petal flowers. She has the ability to control and create four petalled flowers.",
        1,
    ),
    (
        "Salandros – God of debauchery and drunkenness. Worshipped by brewers, brothel workers, and lovers. Salandros is genderless, appearing as male, female, or androgynous at their whim, but always devastatingly beautiful. People pray to them for good wine, a fun night, and pleasurable company. Essentially Tyrion Lannister’s God of Tits and Wine.",
        1,
    ),
    (
        "Gaelin – God of Idiocy and Eccentricity. He’s known to wander the Earth making non-sense jokes and preforming acts befitting his title. He has the ability to cause even the stupidest course of action to end successfully.",
        1,
    ),
    (
        "Nais – Goddess of trickery and epic poetry. She is the weaver of stories and the main reason why the mythologies surrounding other gods can be so confusing, as she makes up stories about other deities a lot. She plays pranks on other deities a lot and inspires her clerics to do likewise. She is seen as a patron of chance encounters–which always make for a good story.",
        1,
    ),
    (
        "Palakis – God of magic. Actually a warlock who used a powerful spell to take control of his patron.",
        1,
    ),
    (
        "Lord Tenticonia – One of many insane gods invented by the kuo-toa. Unfortunately, it’s just a mind flayer.",
        1,
    ),
    (
        "The Traveler – Patron diety of wanderers, nomads, and sailors. Depicted as a faceless figure in a hooded traveling cloak with a walking stick. Praying to the Traveler helps guide people to their destination, be it a physical place or a goal. The Traveler’s holy symbol is a compass, but instead north, south, east, and west, the cardinal points are the Hearth (for those traveling home), the Throne (for those traveling for a goal/ambition), the Heart (for those traveling for love), and the Unknown (for those traveling for discovery or adventure).",
        1,
    ),
    (
        "Lairon – God of Rest. Worshiped equally by those in leisure and those collapsing after a day of work, people pray to them for the ability to better appreciate their rest. Prayers are long, repetitive, and thought, not spoken.",
        1,
    ),
    (
        "Regaia – goddess of Enchantment. A wizard who destroyed her body and chose to live on in the minds of mortals. As long as someone somewhere knows she exists or believes in her, she’ll live. What better way to make people know about you than convincing them you are a god? Able to take control of her high priests to speak with her worshippers.",
        1,
    ),
    (
        "Viel – the god of Trickery and betrayal, represented by a green dragon coiling around a dagger.",
        1,
    ),
    (
        "The Tainted One – Child of unknown parents, supposed to have been born from an ‘unholy union’, whatever that might entail in the different societies. They are a symbol of fighting and winning against all odds; a disgrace to their family and marked as one who should not be, they still rose to godhood – although they aren’t exactly held in high esteem. Patron of bastards, half-bloods and children of criminals or likewise.",
        1,
    ),
    (
        "Remira – the God of Light burns all unworthy to his eye with his magnificent gaze. Those worthy of his regard are heroes of virtue, beings of honour and glory. The worthiest are his Paladins and those giving their life to protect the innocent, the righteous and honorable!",
        1,
    ),
    (
        "Olkath and Althok – the Twins of Life and Death; one wrapped in blooming vines and accompanied by merry laughter, the other always halfway hidden in shadows and killing everything he touches. The brothers are as contrary as fire and water, black and white, light and dark; their clergies split as well, although Life is meaningless without Death and Death is not without Life.",
        1,
    ),
    (
        "Kinfal – Daughter of Smoke, Mistress of Flame, Goddess of Fire. She is chaotic and merciless, gives and takes life in equal measure. She is said to favour smiths even above her own clergy and sailors use her name when cursing enemy ships and crews.",
        1,
    ),
    (
        "Plera – the Black Elk: Goddess of the Forest, gracious to those who respect her domains and creations, patron of hunters, druids and rangers. Might bless one by appearing in the form of a black moose on a forest clearing; one will be granted safe passage through her domain without needing to worry for food and water.",
        1,
    ),
    (
        "Natuno – God of Mistakes. Her goal is to keep everyone just out of reach of their full potential. For every missed note a bard plays, every hunt a ranger loses track of, and every botched experiment a wizard creates, Natuno is there watching and guiding them away from success.",
        1,
    ),
    (
        "Zobober – god of spirits and spirits. An orc who ascended to godhood, the priesthood’s practices and philosophies include a lot of communion with nature spirits, self-improvement, and regular intoxication through rigorous alcohol consumption.",
        1,
    ),
    (
        "Bleigusblonde – a vampire god of nurturing. He grants strength and wisdom to vampire children who worship him by carrying a beige string and a small pebble in their pockets",
        1,
    ),
    (
        "Toam’aron – God of tactics and battlefield strategy. He helps his followers see into the tactics of their enemy and place themselves to fight the easier battle. Encourages laziness and letting the enemy overwork themselves to fight you rather than go to fight the enemy, making the fight more unfair.",
        1,
    ),
    (
        "Seva – goddess of the sands. She takes the form of a large serpent, spends her days sleeping under the sand dunes and the nights rearranging her expansive deserts.",
        1,
    ),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {roll(table)}\n")


if __name__ == "__main__":
    main()
