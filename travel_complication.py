from roll import roll


# Source: http://dndspeak.com/2018/05/100-travel-complications/
table = [
    (
        "While traveling on the road, you come across a massive tree that has fallen in the middle of the road. It will take 1d10 hours to clear. Unbeknownst to the party, a massive ogre is hiding in a nearby cliff waiting for an unsuspecting caravan to wander into his tree trap.",
        1,
    ),
    (
        "The main road has been washed out. Crossing the gap would be dangerous and time consuming. There is an alternate route through the woods which are known to harbour a multitude of threats, but it’s faster than dealing with the washout.",
        1,
    ),
    (
        "The party comes across a caravan in distress. Bandits have been known to set ambushes like this to catch unsuspecting travelers, but there are also rumours of a merchant caravan that’s late returning from the capitol. What do you do?",
        1,
    ),
    (
        "A lost child wanders the road, heading back the way you came. It’s too late in the day to get back to town before nightfall, and you need to be in the next city over by morning.",
        1,
    ),
    (
        "You see a dying man at the side of the road. If you stop, he tells you that [Person]’s guards attacked and robbed him. You are en route to an audience with [Person] to negotiate a lucrative commission, and as far as you know, s/he is a pillar of the community.",
        1,
    ),
    (
        "A blizzard swirls up, impairing vision and forcing players to make con saves against cold damage.",
        1,
    ),
    (
        "A white stag/any other big game animal crosses the road and bolts. Do the adventurers pass on this trophy that could be worth money for its pelt/antlers/alchemical ingredients or do they go hunting?",
        1,
    ),
    (
        "The party happen upon a hoard of coins (usually gold) in the middle of the road. It’s more than they can carry and there’s no obvious way to transport it. A group of level appropriate humanoids are circling around, intent on taking the hoard for themselves.",
        1,
    ),
    (
        "You find the last survivor of a zombie/goblin/werewolf/etc. attack. He/she asks you to bring him back to his guild, which specializes in hunting this kind of monster.",
        1,
    ),
    (
        "You come across the last survivor of a pack of peaceful werewolves who are being hunted by vicious werewolf hunters. He/she asks you to return him to the rest of the clan.",
        1,
    ),
    (
        "You stumble into the middle of a fight between bandits and evil wizards fighting over a caravan of potentially valuable supplies. Neither party has seen you yet.",
        1,
    ),
    (
        "A farmer or other commoner is transporting an offering to a fearsome enemy (giant, wizard, orc chieftain, etc.). He/she tells you that the village has managed to remain untouched by offering livestock/goods/gold in exchange for safety.",
        1,
    ),
    (
        "You are approached by a zealous group of cultists. They begin preaching to you that the world is going to about to be destroyed by the god they worship, and ask you if you’d like to join their end-of-the-world party (attending reveals that the world is not, in fact, about to end).",
        1,
    ),
    (
        "While passing through an abandoned farm, you come across a scarecrow that psychically whispers to you. It gives the party an “impossible” riddle and claims that if you cannot answer then it will not let you pass. Note: Scarecrow cannot move and players need not answer the riddle in order to simply walk past.",
        1,
    ),
    (
        "A group of goblins standing on each other’s shoulders in trenchcoats trick travelers into coming to help fix their broken down wagon, and rob them for every copper they’re worth.",
        1,
    ),
    (
        "The only way to progress is through the aftermath of a battlefield. Many of the traps put in place by mages haven’t been disabled yet, and the party must navigate safely through it.",
        1,
    ),
    (
        "There is an illusory spell over the forest that they are traveling in that causes people to think that the road is taking them in circles. People who pass the save must convince the others that they are going the right way.",
        1,
    ),
    (
        "There is a caravan of magical meat traders that are going from city to city. However, they only trade meat for meat instead of trading with gold.",
        1,
    ),
    (
        "There is a tiny earth elemental trying to learn how to juggle. If the party tries to touch it, an angry mother will come out of the woods to attack them.",
        1,
    ),
    (
        "A group of teenagers were smoking in the woods and accidentally started a forest fire. Unfortunately, the party is in that forest and needs to get out.",
        1,
    ),
    (
        "The road comes to a large river. A new, high-quality bridge has been built over the river by a goblin clan who are seeking to overcome evil natures and to make an honest living. They are charging what is, in fact, a high if still fair fee.",
        1,
    ),
    (
        "The path and map somehow did not mention a mountain that sits right in the middle of the road. The party did not notice the mountain until it was directly upon them.",
        1,
    ),
    (
        "The village that you come to has just had adventurers a lot like your party come through, and have prepared an appropriate welcome. If your party are heroes, it might be fresh-baked bread. If your party is a bunch of jerk murder-hoboes, it might be tar and feathers.",
        1,
    ),
    (
        "A large group of pigs are running every which way. A young girl in a ragged dress is trying to herd them together, sniffling slightly. If approached, she explains her father and mother are sick, but the pigs are supposed to be sold at the market, and they need the money for medicine.",
        1,
    ),
    (
        "A worried-looking half-orc desperately tries to convince your party they are going the wrong way, and that they should take a similar (if slightly longer) trail to their destination. A religion check reveals that he is a cleric of a knowledge deity. If the party ignore him, he tries to convince them for a while, then shakes his head sadly and begins trudging away.",
        1,
    ),
    (
        "A small stretch of woods are petrified in place and time, completely silent and perfectly still. Anyone touching anything but the path in the forest finds it hard as stone and completely immovable. There are birds and other animals in the forest, but they too are as still as statues.",
        1,
    ),
    (
        "A vicious squirrel begins throwing nuts and chattering at the party. It doesn’t do any real damage, but it is painful and annoying.",
        1,
    ),
    (
        "A nest of baby hydras! Kill ’em, avoid ’em, or (with a successful handle animal check) take one with you! Where’s the mother, anyway?",
        1,
    ),
    (
        "Someone has left a trail of copper pieces, leading off the road to a cave. The cave is heavily trapped and ends in an empty chest. You hear giggling when the chest opens, but no one is in sight.",
        1,
    ),
    (
        "A large group of pilgrims and flagellants are making their way slowly up the road in front of you, slowing you down. They make no attempt to give ground to you and eye you with some vague hostility.",
        1,
    ),
    (
        "A deep moat has been dug across the path in front of you. Two gnomes on the other side are looking at a map and blueprints and arguing with each other. They make no attempt to help you cross.",
        1,
    ),
    (
        "An 8-year old boy is peacefully leading a giant pit fiend/ Manticore/ Purple Worm on a chain behind him down the road. If asked about it, he laughs and says, “oh, that’s our cow. She just likes to play tricks on strangers.” He then ruffles the- whatever- and continues on his way whistling.",
        1,
    ),
    (
        "Your map failed to mention a road inn halfway to your destination. The inn is completely empty with the door torn off it’s hinges. With a local knowledge/geography check you know that this inn shouldn’t even be here, this was once the location of a grave site.",
        1,
    ),
    (
        "An armored retinue of Soldiers and Clerics bearing a King’s/Lord’s/God’s banner have set up an inspection point, requiring all passing through to declare their belongings, allegiances and purpose for passing. Zone of Truth, Detect Evil and Good, and Truesight are in use.",
        1,
    ),
    (
        "You come across 2 NPC’s arguing over which one is real, and which is a hallucination.",
        1,
    ),
    (
        "You discover a 50ft wide flowing river crossing perpendicular to your path. This same river can’t be found on any maps.",
        1,
    ),
    (
        "A great human knight has just died of a heart attack as he travelled down the road. His squire and page have pulled him to the side, and one has gone to fetch help. The knight has powerful magical armor and weaponry which would fetch a pretty penny, and there are robbers about…",
        1,
    ),
    (
        "The road is completely blocked off as if an avalanche or rock slide occurred. Problem is the area is pretty flat and you don’t understand how the rocks got here.",
        1,
    ),
    (
        "A group of animals have been killed and aligned in a strange formation with weird symbols drawn in blood. Party could find out this was used for a ritual of sorts.",
        1,
    ),
    (
        "You turn a corner and the road ahead is blocked by a pool of lava. Upon inspection, there is no heat. Futher inspection will reveal it is a illusion spell. Perhaps a silly prank by a wizard. You can walk through the lava.",
        1,
    ),
    (
        "As you make your way along the road, you come across a rotting dead animal carcass. The smell is horrid, but it is nothing out of the ordinary. As you continue, a few more animal carcasses are strewn across the road. More and more bodies begin to appear along the road the further you go. You eventually come face to face with a 20ft wall stacked full of bodies ranging from livestock, predatory animals, and even people. The wall blocks the road, and the only ways to proceed include scaling a nearby muddied-with-blood slope, backtracking to find another route, or digging through.",
        1,
    ),
    (
        "The travelers find themselves at a crossroads, then the same going forward, and again. The party is trapped in a magical loop, until they can dispel it or notice the difference in the pattern, such as flower locations or a bird’s flight path.",
        1,
    ),
    (
        "You were sold bad travelling gear at your last stop – the rations are worthless, the water tainted, the leather goods falling apart.",
        1,
    ),
    (
        "Flash Flood: A downpour upstream has triggered a flash flood over a low part of the road. Although the water is 3 feet deep, the current is so swift that it will without fail sweep away anyone trying to ford it. Individuals swept away face the risks of bludgeoning, impalement on debris, and drowning. By stepping in it at the shallower edge, it is obvious to even survival novices that it will be extremely dangerous to cross, especially towards the middle. The party can choose to wait it out if they like although it will take a long while.",
        1,
    ),
    (
        "Stampede: A large herd of bison/gnus has been spooked and is wildly stampeding down the road as it is the path of least resistance. Get out of the way or be trampled.",
        1,
    ),
    (
        "Landslide: Heavy rain and a small earthquake triggers a series of small 30-foot-wide landslides. The party needs to book it before a larger one hits.",
        1,
    ),
    (
        "Help with wheel repair: A traveling caravan of nomadic folk has a broken wagon wheel. The lady in charge is a seer and offers insight on your fortunes, but no gold, if you stop and help.",
        1,
    ),
    (
        "Bad signs: A jerk has rearranged the roadsigns at an intersection so they point to the wrong places.",
        1,
    ),
    (
        "Pulled over by the highway patrol: A peacekeeping army-guard convoy is marching through. They are corrupt and will harass and attempt to search the party and may try to take money or goods they find suspicious or the party cannot explain the providence of. They will also apprehend known criminals. The party may get most of their stuff returned by “appealing” (aka paying a bribe) to a similarly corrupt local court.",
        1,
    ),
    (
        "The Wyld Hunt – The fey are out hunting. Beware. They have already chosen a quarry, but don’t stick around, lest one of them choose you as their next.",
        1,
    ),
    (
        "After walking for a good few miles along the path down the clear road, you reach an invisible barrier. Then the illusion breaks – this Mirage Arcane made this deep cave look like a clear plains with a nice lovely stone path identical to the one you’ve been following. You are half a mile into this cave, and the fey who have lured you here do NOT want you to leave without doing something for them first.",
        1,
    ),
    (
        "Modrons: Along the path you find a group of modrons (2 monodrones and a duodrone). These modrons were not given the return order during the last modron march (due to complications from becoming attacked) and are still trying to collect data. Upon noticing the party they harass them for data, doing things like surveying them and mesuring the size of their clothes while they are walking. They continue to do this until they either lose sight of the party or are destroyed.",
        1,
    ),
    (
        "A fire can be seen just under a mile away in an obviously cultivated field, the wind now blows billows of smoke over the road the party is crossing. The field belongs to a local alchemist who has seeded it with various medicinal herbs. The smoke is highly intoxicating, impressing odd conditions and visions upon the party members.",
        1,
    ),
    (
        "Improper care – the terrain has taken an unfortunate toll on your foot ware. Your soles are falling apart, movement reduced by 33%.",
        1,
    ),
    (
        "A mounted knight in full tournament jousting gear mistakes the party for his entourage/bodyguard and insists that they escort him to his next competition.",
        1,
    ),
    (
        "The party come across a revenant who is nearing his target. The target isn’t any one in the party but the adventurers have a chance to intervene.",
        1,
    ),
    ("Someone in your party has dysentery.", 1),
    (
        "Everyone the party asked in the last town/village/waypoint has said the only safe way to get through the valley is to take the blue path, detailed and maintained by both of the communities it is flanked by. The villagers all said the upkeep was mutual, and that they were on very good terms with the other town/village/waypoint.",
        1,
    ),
    (
        "Upon getting out of the first town’s territory, they find the rest of the path barricaded and blocked, the barricade older and written in an archaic version of the prime language. The trees and animals all look like they are from a different time. There is a ‘detour’ path but it’s filled with primeval dangers.",
        1,
    ),
    (
        "While traveling the carriage you are riding on hits a rather large bump causing an already weak axel to snap rendering the carriage useless. The party must either find a way to fix the snapped wood so that they continue, or they can try and convince another traveler to help.",
        1,
    ),
    (
        "You find the rats have gotten into your rations. You’ll either need to make constitution saving throws or find new food.",
        1,
    ),
    (
        "A massive and extremely powerful dragon ambushes you somewhere along your journey through a massively dense and vast forest. It is strong enough to slaughter you all without trying, and is upset that you are not aware of it. Gonna have to talk fast to appease it. It also desires a rare food item you possess, and will allow you to pass if you offer it the food and an appeal to its vanity.",
        1,
    ),
    (
        "This actually happened to me in a campaign: An axle on the cart breaks and a druid, in an attempt to repair the cart, accidentally Druidcrafts the wooden wheel or another wooden piece of the cart into a bush.",
        1,
    ),
    (
        "There’s been an earthquake, and the pathway is blocked by something. It might be a fallen tree, a crack in the ground, or a piece of land that broke off a mountainside. Either way, it’s going to be difficult to get past it and nigh-impossible to get a cart across.",
        1,
    ),
    (
        "Jack’s Lanterns – Strange lights can be seen far away, off the path. They hover over pits and quagmire, and will trap unwary travellers.",
        1,
    ),
    (
        "Dimensional Instability – There’s been a small ripple in the planar fabric between worlds. For a few moments, another plane is open. It might be the Elemental Plane of Fire, the Feywild, the Shadowfell, the Astral Plane, or even one of the realms of the gods.",
        1,
    ),
    (
        "Mystic Orchard – A large area filled with various trees and bushes, each one covered with different fruits. Food is plentiful, but some of the assorted berries might be poisonous or have a side-effect.",
        1,
    ),
    (
        "Overgrowth – The path is overgrown with vines, grasses, and tree roots. It is difficult terrain to move past, and will take twice as long to cross.",
        1,
    ),
    (
        "Oh look, it’s a giant stag. Roll 2d4. 2-4 means the stag charges. 5-7 means it looks at your party and moves on. 8 means it bows before you, granting your party a 2-point Charisma Bonus for the next week.",
        1,
    ),
    (
        "A felled tree blocks your path, and the way around is blocked by dense overgrowth.",
        1,
    ),
    (
        "You come across a large battlefield of some previous encounter with hundreds of bodies laying strewn across the ground and piles of corpses heaped into stinking mounds, crossing around will take a full day but if they cross through they need to make a Constitution save DC 15 or become sickened with rot from fly bites carrying disease which gives the poisoned status for 24 hours.",
        1,
    ),
    (
        "The next town is roughly 50 days away around the mountain and the only other way is through a tunnel with a REALLY steep fee. (Or a SECRET TUNNEL)",
        1,
    ),
    ("A mating ball of poisonous snakes is in the way.", 1),
    (
        "A herd of wild goats appear. One takes a particular liking to any dwarves in the party.",
        1,
    ),
    (
        "The remains of a horse on the trail have attracted a bear. It’s too busy gorging to notice you.",
        1,
    ),
    ("A forest fire blocks the path after a thunderstorm.", 1),
    (
        "Snow melt have turned a small creek into a massive raging river. The only bridge is destroyed.",
        1,
    ),
    (
        "A recent landslide has resulted in several large boulders tumbling into a narrow section of the river, making it very difficult to navigate in the Dory boat the party is traveling in. The boat has an HP of 13, roll 1d4 x 4 to see if it safely makes it through, without the hull being opened up, which would cause it to sink.",
        1,
    ),
    (
        "A mess of vines blocks the party’s way. Seems like a sharp weapon will be needed.",
        1,
    ),
    (
        "Two bugbears are sleeping off their hangover in the middle of the road. You can try to sneak past, take a detour, or attack.",
        1,
    ),
    (
        "Part of the path has been washed away leaving a large, deep mud puddle that is difficult to traverse around with the wagon/cart because of the dense bush either side. If the party chooses to forge through it takes them 2d20 minutes, and they end up covered in the thick, sticky, foul smelling mud. If the party chooses to clear a path to the side it takes them 3d20 minutes.",
        1,
    ),
    (
        "You notice an abundance of sink holes in the field. Players bust be careful with their footing as well as not grouping up to close together.",
        1,
    ),
    (
        "You find two exact similar dwarfs fighting each other with crossbows and taking cover. Both say the other is a doppelgänger. None of them is, they’re just lost siblings. One is named Thruduanir and the other is just named Greg.",
        1,
    ),
    (
        "A small red skinned creature sits ontop of a rock on the side of the road. It waves to you and implies that it wants to play a game with you, to pass his test to get his higher devil horns. If not, he vanishes. Roll a d6. 1-2 the devil vanishes and leaves a small purse filled with coin, around 10gp.(the coins turn to lead in one hour) 3-4 a group of (appropriate) undead appears and will fight for their souls to be released by the devil. 5-6 a (appropriate) demonic being is brought into existence, will attack the group immediately.",
        1,
    ),
    (
        "An old sagelike man sits on the side of the road and begs the party for food, water or gold. -If given food, he disappears and gives a blessing to the goddess of wanderers, the party will not be disturbed on their next long rest. -If given water/wine/ale, the old man hands the party an everflowing mug, containing what they gave him in the first place. -If given gold, he asks the partymember what his favorite animal is and then hands over a golden egg. Soon, a familiar of choice (will grow up to one feet tall) will be born from the egg. -If given nothing, he curses you and will stripe your party of half their rations and water.",
        1,
    ),
    (
        "A hangman and magistrate with a constructed gallows are preparing to execute a man for poaching. The man sees the party and yells for help as the hangman struggles to get him in the noose.",
        1,
    ),
    (
        "A “very human” child is drawing strange runes in the dirt with a bag of blue sand.",
        1,
    ),
    (
        "A Traveling circus is coming the other way and they want to practice their act: A mind control/hypnosis performance. At some point the party realizes they have no intention of letting whoever they hypnotize leave the troupe.",
        1,
    ),
    (
        "A dozen ogres are playing hide and seek. They don’t really feel like eating you, they just want to play.",
        1,
    ),
    (
        "You find a merfolk in a barrel of water by the side of the road. You are at least a mile from the nearest water source.",
        1,
    ),
    ("Half a skeleton grabs onto the back of your horse/wagon.", 1),
    (
        "All forms of vegetation along a lengthy stretch of the road have been transformed into glass, while the top inch of the terrain has transformed into obsidian. Along the sides of the road are statues of confused, frightened animals made from random rocks and minerals. All organic life in the area slowly begins transforming into various rocks and minerals over the course of one full day, at which point the organisms are petrified. A fully transformed organism may only be cured through use of Greater Restoration or a similarly powerful magical effect. Upon leaving the stretch of the road, any partially petrified creatures have the transformation process occur in reverse at the same rate.",
        1,
    ),
    (
        "A friendly, sentient dust devil comes across the party and follows them around for 1d4 hours, behaving like an excited puppy for its duration. It communicates by swaying forward and back for affirmation, and left and right for negation.",
        1,
    ),
    (
        "A speaking animal, like a frog or a bird, is passing your way, looking for direction and a way to be polymorphed back into it’s true form.",
        1,
    ),
    (
        "A bare piece of plains, with a large stone set in the middle. The still legible inscription reminds of a great battle long ago. Ghosts are said to haunt here in the night.",
        1,
    ),
    (
        "A flat corridor between mountain passes has many windmills dotting the landscape due to the constant and unvarying wind flow. One of the windmills lies in the middle of the path ahead.",
        1,
    ),
    (
        "A large, deep depression in the ground that appears to be covered in smooth, gray-black glass. If one slips and falls in, it is very difficult to get out. At the edges, it fades into the soil, and there is grass growing in cracks in it. If broken, it is very sharp. There are several animal skeletons at the bottom.",
        1,
    ),
    ("A recent landslide has exposed a large fossil in the middle of the path.", 1),
    (
        "Two wizards are dueling on the path ahead. They continually cast Ice Wall, making it nearly impossible to pass.",
        1,
    ),
    (
        "A two-headed giant is napping on the path ahead. Do you try and fight, or sneak past him?",
        1,
    ),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {roll(table)}\n")


if __name__ == "__main__":
    main()
