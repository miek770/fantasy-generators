from roll import roll


# Source: http://dndspeak.com/2017/12/100-sea-travel-events/
table = [
    ("A Pod of Dolphins Swims alongside your vessel for 1d4 hours", 1),
    ("An intoxicated Crewmember falls overboard", 1),
    ("A Pod of Plesiosaurs feed off the corpse of a sperm whale in the distance", 1),
    ("A Barrel floats past the ship, it contains a fine wine", 1),
    (
        "The ship passes by a Sea Stack where a sailor, crazed through starvation, begs to be taken aboard",
        1,
    ),
    (
        "A crew member saw a ghost ship during the night. The captain being superstitious changes course to go around the sighting. The takes journey is now 1d4 days longer.",
        1,
    ),
    (
        "A boulder is seen floating past the ship. Upon inspection the boulder is indeed made of stone, but floats inexplicably.",
        1,
    ),
    (
        "A whale emerges from the depths and a nearby ship attempts to attack it, the captain of said ship is constantly rambling about revenge and has a peg-leg. If the characters do not intervene the ship is destroyed and the whale goes back under.",
        1,
    ),
    (
        "A coffin floats past, covered in barnacles. If the players choose to haul it onto the ship they will find the word “CASSIUS” is engraved above the lock. Inside rests a long-forgotten vampire who will attack the crew one-by-one at night if aboard the ship.",
        1,
    ),
    (
        "A ball on a chain floats past. However the ball has been covered in extremely hard barnacles making it sharp, allowing it to be used as a spiked flail.",
        1,
    ),
    ("You catch a member of the crew writing eldritch sigils on the deck in chalk.", 1),
    ("Forty-odd bodies immediately float to the surface, they seem fresh…", 1),
    (
        "A member of the crew has disappeared! The last person to see him says he took a rowboat in the middle of the night and abandoned ship…",
        1,
    ),
    (
        "The ship passes through a school of pink, octopoid-like creatures. They are harmless, but exude a very slippery oil.",
        1,
    ),
    (
        "The carcass of a dragon turtle, bloated with decomposition gases, floats on the surface. The sickening stench is notable a half-mile away.",
        1,
    ),
    (
        "A small longboat with sails furled, crewed by around ten, scuds by in the night. They do not hail or acknowledge the PC’s boat in any way.",
        1,
    ),
    ("A warm rain falls – the water is pinkish in color but otherwise normal.", 1),
    (
        "A sea elf surfaces and hails the ship with a series of broad hand motions, obviously some type of code. No reply seems to make sense them and they leave after a minute.",
        1,
    ),
    (
        "A lump of Grey goop floats by. If collected, it proves to be the precious ambergris.",
        1,
    ),
    (
        "During the night, ball lightning dances among the sails, creating a frightening show. It does no damage.",
        1,
    ),
    (
        "At night, a fog covers the area, blocking the ability to see the stars, but the crew spots three glowing green orbs floating off the port bow. The players can try to use the orbs as a point of reference to navigate, investigate the orbs, or wait till morning.",
        1,
    ),
    (
        "Your ship is immersed in giant tentacles and is unable to move. A giant kraken head emerges and tells you that it’s lonely and just wants to talk.",
        1,
    ),
    (
        "The first mate of the ship you’re on finds excess cargo from their last trip, and shares the contents with the group. (Spices, alcohol, etc.)",
        1,
    ),
    ("The travelers meet a traveling brothel ship titled “The Lusty Crustacean”.", 1),
    (
        "Two crew members are playing chess on the top deck. The ship shifts, causing one of the king pieces to slide off the side of the ship.",
        1,
    ),
    (
        "A large sea beast follows the ship for 1d4 days. It does not appear threatening, and dives to the depths if attacked.",
        1,
    ),
    (
        "A storm hits in the night, and one of the crew claims to hear it speaking/singing to them.",
        1,
    ),
    (
        "You find a small, unmapped island. If the crew disembarks to investigate, it is revealed that the island is actually debris collected on the shell of an enormous turtle.",
        1,
    ),
    (
        "The captain makes a detour to a small, rocky island, shrouded in fog. He goes to the island for 1d4 days before returning with no explanation. None of the crew seem to be bothered by this.",
        1,
    ),
    (
        "The ghostly residents of a long sunken city walk above the waves where the city streets and buildings once were. As your ship approaches, they all stop and watch you.",
        1,
    ),
    (
        "As you approach a large island, all of the water pulls from its shore to reveal a sunken ship surrounded gold and artifacts that have spilled from its belly. But the water that has been pulled from shore is now a tsunami, and you have a time limit to do what you will.",
        1,
    ),
    (
        "A massive spire of stone erupts from the ocean. There appears to be someone at the top, looking down upon your vessel.",
        1,
    ),
    (
        "While inside of a bay a squall hits and temporarily your boat sits on dry land. Eventually, the waters return and the boat sails onward.",
        1,
    ),
    (
        "A ship manned by terrifying beasts passes by. Your sailors are terrified, but the monsters keep their distance. They pass swiftly, as if on a mission.",
        1,
    ),
    (
        "As noon approaches in the vast expanse of ocean, you see a ship that looks exactly like yours approaching. As the ship passes by, you see yourselves on the other ship, watching you with the same confused expressions that you have yourselves.",
        1,
    ),
    (
        "In the dead of night, a panicked bell toll rings. A massive beast is striding in the ocean. It appears the ocean depth only reaches up to its hip.",
        1,
    ),
    (
        "You find a rusted anchor covered in runes, when you use the anchor the entire ship sinks nearly instantly to the bottom of the sea. The occupants of the ship are now under the effect of the breathe underwater spell.",
        1,
    ),
    (
        "An iceberg floats by, when sunlight shines through it you see the ship frozen inside.",
        1,
    ),
    (
        "You can’t believe your eyes, a gold obelisk just sitting in the water surrounded by a jagged sharp reef.",
        1,
    ),
    (
        "During the journey, an occasional bump is noticed against the ship’s hull. But as the days go by, the bump becomes a thump, then a bang, and suddenly a crash that rocks the ship.",
        1,
    ),
    (
        "An old woman appears on deck. She says a toll must be paid to pass beyond this point, and seems to have the power to enforce it. But she doesn’t want money. She wants something from each of you that you can’t bear living without.",
        1,
    ),
    (
        "A beautiful mermaid is spotted approaching your ship by a number of crew. Shortly after they spot her, they suddenly sink into madness, ravenously gnawing on their fingers and rambling in an unknown language. All the while, she is getting closer.",
        1,
    ),
    (
        "A small bird begins circling your ship, then two, then a thousand, then an innumerable flock.",
        1,
    ),
    (
        "As you walk the deck, you notice a board is missing. A few days later, you notice another. Then more parts begin to go missing, including boards from the hull.",
        1,
    ),
    (
        "A small trickle of water is seen coming into the ship. It seems like it’s not an issue, but when someone goes to plug it, the hole opens up and devours them.",
        1,
    ),
    (
        "You walk across the deck as the ship’s nose lifts up. The ship has left water and is now floating above the ocean and directly into the sky.",
        1,
    ),
    (
        "A fire erupts from the captain’s quarters, he runs out burning and screaming for everyone to run before collapsing on the deck.",
        1,
    ),
    (
        "As the first lantern is lit during sundown, a constant stream of fish begin to jump out of the water and onto the deck, followed by a deep rumbling sound from below the ship.",
        1,
    ),
    (
        "An empty rowboat is sighted. When the ship gets close to it, it vanishes in a wet mist.",
        1,
    ),
    (
        "You pass by a hermit living on a self sufficient fishing platform. They chuck rotten fish at your ship if you get too close.",
        1,
    ),
    (
        "The ship is followed for several hours by fins extruding from the water. The water appears dark grey, and nothing beneath the surface can be seen. If anyone goes swimming in the water, they can’t see more than a foot in front of them. After several hours, the fins water gradually turns back to normal color and the fins dip beneath, disappearing.",
        1,
    ),
    (
        "You find a man adrift at sea in a bloodied life boat. He claims to be the survivor of a shipwreck.",
        1,
    ),
    (
        "A Naga is found floating on a piece of driftwood. She begs to come aboard and appears to have been starving.",
        1,
    ),
    (
        "A crew member that was dumping waste off the side of the boat yells for help. You go the deck to see the crew member being beaten by a humanoid fish creature. The creature jumps back into the sea and swims away when it sees you.",
        1,
    ),
    (
        "You see a dolphin happily follow the ship. You see that dolphin gets eaten by a shark.",
        1,
    ),
    (
        "A hooded figure appears at night and approaches 1 character and says “a danger beyond your mortal understanding is lurking within these waters” if a character goes looking for the figure they will be unable to find it.",
        1,
    ),
    (
        "You see a crew-member slip on the deck. Upon closer inspection, the spot is covered with ice. The water is still liquid, but the ship is slowly freezing.",
        1,
    ),
    (
        "A huge storm approaches, making it difficult to see. The sound of rushing water alerts you to a whirlpool forming ahead, threatening to pull the ship in or damage it if you don’t think fast!",
        1,
    ),
    (
        "A flock of birds appears to be circling bits of driftwood. Upon closer inspection there is blood in the water and the birds are glowing faintly red. There might be something valuable still floating around if you’re willing to risk it…",
        1,
    ),
    (
        "A crew member or crew members disappear for 1d4 hours and come back seemingly out of thin air if investigated its found to be a stow away Doppelgagger who merely wanted passage to your destination you must decide now what to do the. the crew member is still alive just hidden somewhere that only the Doppelgagger knows.",
        1,
    ),
    (
        "You casually walk below deck when you notice water coming up between two of the floor boards.",
        1,
    ),
    (
        "One night, the sea is calm and quiet as a small life boat approaches the ship head on. Your ship steers to avoid destroying it. As you pass it you see a wirey old man with white hair and mustache rowing hypnotically. He’s facing backward with wide eyes, staring off into the distance, and with a shiver in his voice he repeats “the black…. the black”.",
        1,
    ),
    (
        "Enormous bubbles surface frequently throughout the day, they smell horrible when they pop and a faint green/yellow gas can be briefly seen. “Whale farts.” the captain explains, covering his nose and mouth with his handkerchief. Fortitude/Constitution save or be sickened for 1d4 days.",
        1,
    ),
    (
        "A man is spotted on top of a volcanic rock formation, it is clear he has no food or shelter save his clothing and a spare bit of half a row boat. He try’s to get there attention by lighting a fire, but will only board the ship if the players say they are going further south.",
        1,
    ),
    (
        "The captain gets too drunk and in the process he steers the ship gets off course.",
        1,
    ),
    (
        "A large object bumps against the hull of the ship. After hauling it aboard, the crew discovers it is a huge glass bottle the size of a person, with an equally large scroll inside. On it is a beautiful poem written in Giant.",
        1,
    ),
    (
        "The navigator is found to be a fraud- he has no idea where the ship is or where it is going. Neither does anyone else on the ship.",
        1,
    ),
    (
        "The ship passes over a coral reef inhabited by aquatic fairies- the fairies play pranks on and try to mislead the crew, accidentally causing one crewmember to fall off the mast to his death.",
        1,
    ),
    (
        "The captain calls everyone aboard and announces that someone or something has been stealing food- there is only 1d4 days worth of rations left.",
        1,
    ),
    (
        "A giant is seen walking through an ocean that only reaches his belly, in the distance.",
        1,
    ),
    (
        "A sailor spots a glimmer under the water—further investigation reveals it is the very top of a huge underwater statue made of gold.",
        1,
    ),
    (
        "The ship cook has concocted the foulest, sickest looking meal, even by his standards. It’s also his birthday, and no one wants his feelings to get hurt.",
        1,
    ),
    (
        "Huge manta rays fly over the ship. Each of the manta rays could feed the crew for days, and some are even rumoured to have precious pearls within. However, if the party does manage to get one, they find the skeleton of a human child within.",
        1,
    ),
    (
        "Everything. I mean EVERYTHING. Smells like fish. Horrible, stinky, rotting fish. Clothes, shoes, your own body, and even food that doesn’t contain fish. Oddly enough, fish smells like strawberries.",
        1,
    ),
    (
        "The crew’s amusements of dares have prompted one member to drink the ocean’s water. To his amazement, it is not salty, but sweet.",
        1,
    ),
    ("Shadows appear under the water that must be fish, but look like large birds…", 1),
    (
        "Shipworms have weakened the hull. Carpenters must spend a day repairing the damage.",
        1,
    ),
    (
        "Fruit you brought to combat scurvy has slowly been going missing. An investigation reveals a few crew members secretly attempting to brew alcohol.",
        1,
    ),
    (
        "Celebrations on deck for a cabin boy’s first catch at sea go sour when a drunken deckhand confronts the boy to tell him nasty facts about his heritage.",
        1,
    ),
    (
        "The ship comes across a fairly large merchant vessel named “The Seaside Exstravaganza”. The merchant who runs the ship, a stern but fair old woman named Gellie, deals in merchandise from faraway countries. She quickly becomes fond of one of the party and offers them a spot among her crew.",
        1,
    ),
    (
        "The ship approaches a collection of rocky outcroppings surrounded by abnormally quick-moving water. A ship-sized geyser in the center of the outcroppings acts as a portal to the Elemental Plane of Water during the day.",
        1,
    ),
    (
        "The ship comes across a fairly large merchant vessel named “The Seaside Exstravaganza”. The merchant who runs the ship, a stern but fair old woman named Gellie, deals in merchandise from faraway countries. She quickly becomes fond of one of the party and offers them a spot among her crew.",
        1,
    ),
    (
        "A castaway named Sinan is found on board. He swears up and down he can read the stars, seas, and winds just by shooting a crossbow into the air.",
        1,
    ),
    (
        "You pass by an island, across the beaches you can see an entire pirate crew crucified and bleeding by the neck.",
        1,
    ),
    (
        "You pass a ship in the water, a crowd of satisfied soldiers celebrating a victory, unaware of the bulky headless pirate climbing up the side of the ship.",
        1,
    ),
    (
        "A small rowboat floats next to you, a husband begrudgingly asks for directions as his wife cajoles him to have a better attitude.",
        1,
    ),
    (
        "A humanoid manta-man surfaces, his strength is immense and his intentions are unknown.",
        1,
    ),
    (
        "You observe a rather small island in the distance, being no bigger than the size of a small courtyard. Upon closer inspection, you notice that there is table in the center of the island, surrounded by 10 or so chairs. The table is set for what seems to be a grand feast, displaying all sorts of exotic food and drink, completely fresh. However, there is no mention of this island on any map, and you find no indication that anyone else has been there recently.",
        1,
    ),
    (
        "The fluke of a large sea monster is seen in the distance, seemingly headed towards the ship, only for the maw of a much large monster envelop it from below, breaking the surface and quickly sinking back down.",
        1,
    ),
    (
        "Off in the distance, a sunburned, unclean, lone figure on a lifeboat shoots off a flare, and desperately cries for help. The figure is a pirate who escaped from an encounter with the authorities by abandoning their crew. Upon landing, if he/she is turned in to the proper authorities, the party may claim their bounty, or, if kept free, the pirate may come in handy as a contact, as the pirate knows of hidden ports all across the sea.",
        1,
    ),
    (
        "Off in the distance, a sunburned, unclean, lone figure on a lifeboat shoots off a flare, and desperately cries for help. The figure is the final survivor of a terrible shipwreck. This person is a simple fisherman. Should the party take the survivor aboard, they will refuse to go below deck, regardless of the circumstances. If asked, all they will say is “My friends were below deck.”",
        1,
    ),
    (
        "Off in the distance, a sunburned, unclean, lone figure on a lifeboat shoots off a flare, and desperately cries for help. The figure is an arrogant cleric, surviving off of magically created food and water. This person is doing fairly well, all things considered. If rescued and delivered to their temple, this cleric will give the party a small favor, but will consider the party a small part in the cleric’s survival.",
        1,
    ),
    (
        "Off in the distance, a sunburned, unclean, lone figure on a lifeboat shoots off a flare, and desperately cries for help. The figure is a doppleganger, feigning being stranded at Sea, after destroying a ship and eating her crew. If allowed on board, the doppleganger will continue their antics, attempting to kill the crew before they reach shore.",
        1,
    ),
    ("A fishing net brings aboard a treasure chest that turns out to be a mimic.", 1),
    ("A giant squid is seen off the port side of the ship.", 1),
    ("A group of rats get into the food!", 1),
    ("Something huge and solid scrapes against the bottom of the ship.", 1),
    ("Hundreds of manta rays are migrating under the ship.", 1),
    ("Below the water, someone on the ship notices an enourmous sunken city.", 1),
    ("An orc scout ship is seen in the distance, traveling fast towards the ship.", 1),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {roll(table)}\n")


if __name__ == "__main__":
    main()
