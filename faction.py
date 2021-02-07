from roll import roll


# Source: http://dndspeak.com/2018/02/14/100-factions/
table = [
    (
        "The Old Lord’s Watch – A group of retired combatants that protect a small village from evil threats. They put up the disguise of an old man/woman, but they haven’t forgotten their training.",
        1,
    ),
    (
        "The Wayfarers – a band of pirates who pilot the seas off Waterdeep. They offer peace with pirates who run the Wayfarer flag. The High Wayfarer is an illithid pirate.",
        1,
    ),
    (
        "Compassion Conclave – A conclave of Lawful Good Warlocks who work to promote being kind, helping others.",
        1,
    ),
    (
        "My Eyes are Down Here – Gnomes, Halfings, Duergar, Kobolds, small races of all kinds grouping together for awareness of Shorter races and delivering speechs and information on how to talk to those of shorter stature.",
        1,
    ),
    (
        "The Unchained – Mercenary band comprised of former slaves and prisoners. Make use of scavenged or improvised weapons. Often found fighting in rebellions. Have a very loose command structure and usually exist in smaller groups.",
        1,
    ),
    (
        "Society for the Protection of Nature – Various Druids, Monks, Paladins and Cleric of natural domains. Fighting against pollution of natural habitats, deforestation, industrialisation etc.",
        1,
    ),
    (
        "RSPD – The Royal Society for the Protection of Dungeons. A group of fanatics who believe that dungeons are to be preserved and not delved in for treasure or glory, or even to sort out the kobold problem.",
        1,
    ),
    (
        "The Legion of the Faceless – a nebulus organization that practices intense anonimity, always wearing masks when in combat or public settings. They claim to be everywhere and to hear everything, making them excellent at political blackmail and manipulation.",
        1,
    ),
    (
        "The Cult of the Clear-Eyed Mind – a small group of dwarves that have sworn off alcohol. They boast of fantastic powers, such as remembering what happened last night.",
        1,
    ),
    (
        "The Jötunn Valkyries – Half giant and half Aasimar these armored shield maidens inspire both dreadful fear and fierce loyalty. Their hair dyed red with blood and their eyes burning with a rage only a fool would ignore sets the tone on the battlefield.",
        1,
    ),
    (
        "The Banner of Pine Needles – A warband of elfish archers known for hunting goblins and orcs. They show no mercy and offer no quarter.",
        1,
    ),
    (
        "The Glürgil Tinkerocracy – A Gnomish scientific community that believes wild and dangerous progress for the sake of progress is still progress…only faster.",
        1,
    ),
    (
        "Lords of the Gyre Mountains – Dwarven emissaries, traders, warriors, smiths, and diplomats. Powerful and rich families comprise this clan. Their ancient walls have never been breached.",
        1,
    ),
    (
        "The Scale – Lizardfolk, Dragonborn, and Tortles known for their ambushes and their proclivity to bed in the sewers of large cities.",
        1,
    ),
    (
        "Morg Trigal – An abnormally large war band of goblins, orcs, and worgs. The large column of torches and smoke often gets them confused with a fire wurm. A war chief and shaman priestess leads the horde.",
        1,
    ),
    (
        "The Ivory Jacks – Led by the large, mustachioed Rupert Quakesly, the Ivory Jacks are the city’s premier white collar gang. They deal in upper class drugs, underground fight rings, brothels, casinos, and they have their hands in the pockets of most politicians.",
        1,
    ),
    (
        "The Nobles of Naught – Led by the Crow Prince, a mysterious figure who wears a cloak of black feathers, the Nobles of Naught are everywhere. Dedicated to bringing an end to corruption and the mistreatment of the poor, the Nobles could be anyone, from the city guard, to the baker, to the small orphan on the street corner.",
        1,
    ),
    (
        "The Sirens – Led by Madame Tuvelle, an elegant older woman, the Sirens are a group of elite spies and assassins around the world disguised as escorts and whores. Their base is in a huge, gaudy establishment known as the Sanguine Songbird, which fronts as an upper class casino/bar/brothel.",
        1,
    ),
    (
        "Council of the Eight Tipped Star – An order of mages led by eight masters, each focused on one of the schools of magic.",
        1,
    ),
    (
        "The Knights of the Arsenal – An order of holy knights who value showmanship. They stage elaborate gladiatorial bouts as a way to fund expeditions to hunt and destroy evil forces throughout the world.",
        1,
    ),
    (
        "The Deep Corsairs – Vicious pirates, mutated by some elder sea god into half-humanoid, half-fish monstrosities. Usually, they don’t bother with ships of their own, simply rising out of the sea and sending their victims (and their treasure) to watery graves for later retrieval.",
        1,
    ),
    (
        "The Order of St. Davûm – A holy order, founded by a priest of the god of death, whose priests go with armies marching to war to serve as healers and medics; they perform burial rights after battles for the fallen soldiers on both sides to prevent them from being brought back as undead.",
        1,
    ),
    (
        "The Fraternal Order of the Azure Quill – An organization of sages and spies. Secretly run by an evil blue dragon, most members do not realize that they are collecting information specifically on the dragon’s rivals to help him take them down.",
        1,
    ),
    (
        "The Order of the Archive – A knightly order dedicated to preserving all knowledge, even reprehensible works by demon worshippers and necromancers, against a future dark age, and making sure it stays safely in the right hands. Knights of the Archive train rigorously in shutting down black mages, helping those who have had their minds stolen by evil magic, and protecting and copying ancient writings.",
        1,
    ),
    (
        "The Gabbo Initiative – A group of wizards that are convinced they can civilize goblins.",
        1,
    ),
    (
        "The Council of Gears – Warforged, Gnomes, and Dwarves sit on this very public group whose main purpose is to limit the proliferation of dangerous technologies. Their influence spans continents.",
        1,
    ),
    (
        "The Hollow Moon Pack – Lycanthropes, shape changers, and animagi so ancient they no longer change with the moon. They mostly keep to themselves, but when angered their savagery is legendary.",
        1,
    ),
    (
        "Crone Rock Watch – A group of paladins and clerics that hunt down hags and witches.",
        1,
    ),
    (
        "The Magistari – Five aasimar wizards sent from the east to destroy a great evil.",
        1,
    ),
    (
        "The Silver Woodsmen – Anti lycanthrope, and expert monster hunters. They have all lost family to this affliction and are not known for showing mercy.",
        1,
    ),
    (
        "The 50’s – A gang of half-breeds. Half-orcs, half-elves, half-halflings (quarterlings?). You name it. They just want to be seen as legitimate races.",
        1,
    ),
    (
        "The Order of The White Stag – a group of rangers still loyal to an elven Prince in exile.",
        1,
    ),
    (
        "The Last Arc – a group of environmentalist who believe that the end of days is coming, and have built a huge raft to ride out the apocalypse.",
        1,
    ),
    (
        "Fragmented Truth – a faction of believers who think that the written history of the land is a lie, created by the ruling kingdom to control the common people. They seek the truth about history so they can expose the kingdom for the fakes they are.",
        1,
    ),
    (
        "Angelic Fighters – a well known faction of warriors who wish to finish to take their last breath on the battlefield. The faction will fight for any side in any conflict for the right coin.",
        1,
    ),
    (
        "Glory’s Treasure – a faction of low rank adventurers, searching for the long lost treasure of the ancient kingdom.",
        1,
    ),
    ("Altered Magic – The faction of dark mages who wish to change magic forever.", 1),
    (
        "Librarians of The Kingdom – a faction that seeks the knowledge lost to time. This faction consists of several scholars ranging from Historians to Poets. This faction has one core belief that the blue dragons are the superior creatures of this world, and as such the Librarians can’t harm a blue dragon.",
        1,
    ),
    (
        "Shady Ladies – The mysterious faction of ladies who have been cast out of society for various reasons. The faction works in secret to gain enough power to over throw the current kingdom.",
        1,
    ),
    (
        "Black Bards – a famous group of bards that travel the lands searching for musical talent to join their faction.",
        1,
    ),
    (
        "Huntsmen of Grim-Lock – a group of huntsmen that protect the town of Grim-Lock from the unknown evil of the world. This faction is mysterious in nature, and the very location of Grim-Lock is unknown. Joining the faction much less finding them is a struggle of impossible feats.",
        1,
    ),
    (
        "The Gaia Chain – A massive, world-wide, ancient order comprised of druid circles, dragons, and elementals. Membership is usually passed along bloodlines. However, they have three gigantic temples that are open to the public only once a year.",
        1,
    ),
    (
        "The Razing Horde – Barbarians, Orcs, and Goblin tribes that united and utterly destroyed a city for tormenting them with necromancy and dark magiks. They diverted a river to wash away the ruins of the wizard filth.",
        1,
    ),
    (
        "The Capellbairn of Craghoof – Mostly scouting parties, traders, farmers, and warbands of centaurs & halflings. Very territorial… and very odd to see.",
        1,
    ),
    (
        "The Witchgamut – An order headed by three sphinxes, three LE hags, and three Aasimar that are dedicated to keeping wild magic in check.",
        1,
    ),
    (
        "The Praxus Inquisitors – Order dedicated to purging the world of magic and their practitioners.",
        1,
    ),
    (
        "Infiltration Unit 42 – Warforged led spy cabal that hasn’t stopped even though the Great War is long over.",
        1,
    ),
    (
        "Flumphs for a Peaceful Future – A cloister of flumphs have made a group that encourages peaceful interactions amongst the Underdark.",
        1,
    ),
    (
        "The Green Order – A group of knights that protect a forest. When knighted, as part of their oath to the [forest/diety/whatever] their hair turns a dark forest green. (Shamelessly stolen from Matt Colville’s Ratcatcher books)",
        1,
    ),
    (
        "The Unalloyed – A group of xenophobic Dwarves that want to remove all non-Dwarves from Dwarven lands.",
        1,
    ),
    (
        "Order of the Black Sun – a group of monster-hunters, made up of people who have lost family or friends to monstrosities. They are lead by a Knight in dark armor who’s face is never seen. The Order is made up of good people, who aren’t afraid to get their hands dirty.",
        1,
    ),
    (
        "Dragão azul (Order of the Blue Dragon) – A secret organization of agents that handle the less scrupulous needs of the ruling class. They have a set of coded chits they keep on their possession when communicating with each other.",
        1,
    ),
    (
        "The Glacial Stream – A mercenary group of made up of goliaths that were expelled from their tribes. They travel the world and take on dangerous tasks that either lead them to glory or an honorable death.",
        1,
    ),
    (
        "Syndicates – a group of wizards, scientists and engineers who develop technologies to dominate the world. They live and work in underground chambers, protected by runes and automatons, and often attack settlements for supplies and test subjects.",
        1,
    ),
    (
        "Owlbear Team Nine – an elite force of highly skilled combatants, who respond to immediate terrorist threats, and hunt down their headquarters in order to eliminate them.",
        1,
    ),
    (
        "The NewWorlders – magic users who believe to have discovered a way to create a new plane of existence. Their objective is to create a realm of pure good, where all races can live happily and safely forever. They attempt to achieve this by the easiest and quickest means, which often involves theft and murder.",
        1,
    ),
    (
        "The Knights of Pi – a group of paladins/druids that live in a big forest, supposedly protecting it from evildoers. They channel their magic using math, that always involves circles, and shouting the letter π.",
        1,
    ),
    (
        "The Scarlet Troupe – a company of tricksters, jugglers, acrobats and strange animals that roam the land delighting the masses with dangerous acts and daring twirls. But that’s a façade, for the Lady —head of the troupe— is a Mistress of the Assassin’s Guild, and she moves the Troupe to where she (and them) must fulfill contracts.",
        1,
    ),
    (
        "Knights of Levistus – an ancient group of devil worshippers that use only fire based magic. Their only goal for centuries has been to travel to their master in the Fifth Layer of Hell and melt the ice that imprisons him, and in turn they have been promised eternal life and power if they succeed.",
        1,
    ),
    (
        "The Sixth House – Members of a dishonoured / forgotten noble family who work in the shadows to destabilize the ruling Five Houses.",
        1,
    ),
    (
        "The Circus of Smiles – A roaming caravan of performers and clowns which is actually a dangerous cult of chaos and insanity. This roaming band leaves only destruction in their wake, as their charms lure members in with displays of debauchery and madness.",
        1,
    ),
    (
        "The Curators – An organization of wizards of several races that have banded together to create the greatest compendium of magical knowledge called Index. They are known to fanatically hunt down and catalogue magical artifacts and tomes to add to their already sizable collection. They have even been known to trade in countries’ secrets and intelligence, running a vast underground spy network.",
        1,
    ),
    (
        "The Nighthawks – A group of assassins, under the guise of servants of the local death god/goddess. They are a rogue element, and disavowed by the death temple, as they actively kill, rather than letting death come naturally. Of course, this is a front for their true identity, a cult of demon worshippers, hunting artifacts of ancient power to fuel the gate spells that they intend to cast in order to allow their demon king to cross to the material realm and claim it. The most dedicated/depraved members have been gifted/cursed with a charm of undeath, rising a short time after they are killed as near-unkillable vessels of the demon king to exert his will and rage upon the mortal world for a time.",
        1,
    ),
    (
        "The Golden Legacy – A terrorist organization composed of the descendants and worshippers of a tyrannical gold dragon. The dragon left behind its naturally good outlook on life in pursuit of greater power, starting a cult during the process. Even though it has been centuries since the dragon’s passing, members of all races can be found among the ranks of those that believe that the dragon will return one day. The organization is led by gold dragonborn who are believed to be of the dragon’s lineage, and are thereby holy in the organization’s eyes. The faction’s main focus is to seize the “holy land”, the capital of a nearby empire which had originally been the dragon’s lair. In addition, the faction is strongly predjudiced against all dragonborn that are not gold, even other metallic-descended dragonborn. They are seen as unholy, and the Legacy wages a race war on all “inferior” dragonborn in order to purge such “blasphemous creatures” from the world.",
        1,
    ),
    ("The Church of the Great Eye – A cult that worships Chezdrur, a beholder.", 1),
    (
        "The Faith of the Lazer Eye – A similar cult that worships Eloks, a rival beholder of Chezdrur.",
        1,
    ),
    (
        "Anonymouse – A group of anarchistic ratfolk. Known for their foul mouths and horrible pranks.",
        1,
    ),
    (
        "Tiamat’s Teeth – Dragonborn and human followers make up this army. Conquest for their dragon masters is the only thing they know.",
        1,
    ),
    (
        "The Oak Defenders – Mostly comprised of farmers, fighters, and freed slaves they will fight to protect their lands. They have quite the armory from all the foes they’ve defeated over generations. The local nobles are getting scared of their growing political aspirations.",
        1,
    ),
    (
        "The Stone Hewers – They built most of the walls in the kingdom. Mostly civilized giants, human engineers, dwarf masons and ogres. They have a monopoly on both building walls and destroying them.",
        1,
    ),
    (
        "The Tonabi – Hunter gatherers that live in yurts along a coastal mountain range to the north. Their territory extends to many islands and many an intruder has fallen to their arrows and harpoons. Love to trade fish, meats, pelts, and seaweed for metal.",
        1,
    ),
    (
        "The Yarn Pride – Tabaxi rouges that got tired of being treated poorly by society. They steal anything not nailed down. Scratch that…they just stole the nails. Check your pockets.",
        1,
    ),
    (
        "The Sel’drow Heretics – Former wanderers and slaves from the Underdark. These Drow have taken to farming the lands of the surface world over generations. They spread out like ants, forming colonies with underground tunnels that connect to their home caves. They have never forgotten the old ways though.",
        1,
    ),
    (
        "The Piruaga – Jungle dwellers that claim a large territory and are known for sending out emissaries to trade. Their fruits, bushmeats, nuts, medicines and other exotic goods are highly prized. Their dart poisons, however, are a well kept secret.",
        1,
    ),
    (
        "The Tokupi – Known headhunters. They are experts at water warfare. Their obsidian weapons are meant more to maim instead of kill. They are known slave traders.",
        1,
    ),
    (
        "The Red Thrush – A group of Kenku that splintered off from the local Thieves Guild. An abandoned wizard’s tower is their base of operations.",
        1,
    ),
    (
        "The Ainmhithe Triads – Three corrupted druid conclaves that are committed to destroying every city on the planet.",
        1,
    ),
    (
        "Daughters of the Nymph – All female druid-led communes that hunt and capture men once a year.",
        1,
    ),
    (
        "The Paper Court – A secret organization of scholars, wizards, and other knowledge-seekers. Most librarians and booksellers in the region are affiliated with them in some way. It is said that they have a sprawling underground library under a major city.",
        1,
    ),
    (
        "The Fold – A very selective organization of efficient mercenaries led secretly by a bronze dragon.",
        1,
    ),
    (
        "The Order of Balance – An ancient mystical organisation of wizards and sages who try to keep the equilibrium between order and chaos. Not much is known about them but they appear to have had their hands in every major political conflict in the past thousand years.",
        1,
    ),
    (
        "Multiverse Intervention Block – short MIB, A shadowy organisation that deals with beings from another realm, unknown to most people. Conspiracies have formed about the existence of this group. It consists of highly trained mages and fighters who seem to be wherever some unidentified creatures causes havoc. They always wear black and seem somewhat inhuman to the people they encounter. Unfortunately, nobody ever remembers their faces or what happened after their visit.",
        1,
    ),
    (
        "The Wee Green Men – Gnome farmers that will take over any land they feel they should own, and convert it to cabbage farming. They turn an impressive crop, but since most of it is fermented into alcohol they end up a nuisance for every nearby town a few weeks after the harvest. No town has survived more than one farming season without driving them out.",
        1,
    ),
    (
        "Madam Maga’s Travelling Brothel – A roaming caravan filled with, for lack of a better term, magic prostitutes. They use magic to charm people into entering and then change their forms to suit the needs of their , ahem, clients. It’s run by a succubus with no real interest in wars or political troubles, unless it effects her work for the worse.",
        1,
    ),
    (
        "The Rosehills – A traveling family of halfling diplomats committed to making peace between all races and factions. In fact they’re so committed to peace that they are willing to lie, steal, bribe, kill, and in extreme cases commit genocide if that’s what it takes to stop the bloodshed.",
        1,
    ),
    (
        "Cade’s Foundation – An order of wizards who seek to educate the common people about magic and make taboo magical arts, such as necromancy, more socially acceptable.",
        1,
    ),
    (
        "The Dammed – A group of druids protects a forest directly next to a massive trade city. Any time the city attempts to expand into the forest, The Dammed responds by organizing all the beavers in the forest to dam the main trade river that leads into the city.",
        1,
    ),
    (
        "The Goblin Crown – They possess one third of a magical crown that can control an ancient army of golden clock-work automatons. Known for kidnapping gnomes and dwarves in an effort to find the other pieces.",
        1,
    ),
    (
        "The Ancient Golden Dwarves – They possess one third of a magical crown that can control an ancient army of golden clock-work automatons. Known for kidnapping gnomes and goblins in an effort to find the other pieces.",
        1,
    ),
    (
        "The Clockwork Gnomes – They possess one third of a magical crown that can control an ancient army of golden clock-work automatons. Known for kidnapping goblins and dwarves in an effort to find the other pieces.",
        1,
    ),
    (
        "The Kingdom of the Blood Oak – A heavily armored and regimented army of elves. Their forest strongholds and forts are found along established trade routes. Their expansion throughout the forest resembles symbiosis more than conquest.",
        1,
    ),
    (
        "Eyes of the Serpent – Yuan-Ti Purebloods, Lizardfolk, Tortles, and Dragonborn make up the bulk of this spy network. They trade in poisons and secrets. Their negotiations start with offering you a drink, and ends when they decide to give you the antidote.",
        1,
    ),
    (
        "The Emerald Kingdom of Zô – A giant Dwarven stronghold sits on a bed of giant green crystals. These crystals are the size of mountains and run forever in rich subterranean veins. Home to dwarves, gnomes, and halflings they rarely allow the tallfolk to enter their domain. Their crystals release a gas that fuels an armada of air ships.",
        1,
    ),
    (
        "Siggi’s Marauders – Vikings, barbarians, berserkers, shield maidens… once they were roving tribes of raiding parties. That was until a legendary shield maiden gave her life to save the entire northern part of the continent. United under her banner, the peace her sacrifice wrought encouraged trade and expansion south. To kill a fellow Northerner is taboo and punishable by blood eagle.",
        1,
    ),
    (
        "The H’radrome Empire – A hobgoblin civilization based on ancient Rome. They use goblins as foot soldiers and their grand coliseum hosts daily games. The twisted columns leave much to be desired.",
        1,
    ),
    (
        "Order of the Shadow Lotus – Yuan-Ti Pureblood royal assassins and alchemists make up the upper echelons of this group. There are whispers of a lich leading them for the last 500 years.",
        1,
    ),
    (
        "The Red Kings – An alliance of monsters and villains bent on ruling the world. Currently led by Kaanchiweartoliock the red emperor, an ancient red dracolich.",
        1,
    ),
    (
        "House of Bjernson – An ancient Nordic clan. Every male is named Bjern Bjernson and seeks some unique accomplishment to use as a Suffix. Founded by Bjern Bjernson the Lightbringer, vampire-hunting paladin. Currently lead by Bjern Bjernson the Darkslayer, monster hunter who has killed over two-hundred shadows.",
        1,
    ),
    (
        "The Halls of the Dead – Reformed undead, vampires, zombies, ghouls and skeletons that just want to be left alone. They consider necromancers doctors and their territory envelopes graveyard after graveyard.",
        1,
    ),
    (
        "The Titan Provincial Government – Refusing the ordning and the inequality it promotes, these giants have established a peaceful, stable community with humans out in the wilds. It is a true democracy, but is known for utterly destroying hostile invaders…and their homes…and their cities…and their countries. One of the last places on earth known to harvest the giantsbane plant. “Humanoids are friends, not food…unless they attack first.”",
        1,
    ),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {roll(table)}\n")


if __name__ == "__main__":
    main()
