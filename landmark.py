from roll import roll


# Source 1: http://dndspeak.com/2018/01/23/100-natural-landmarks/
# Source 2: http://dndspeak.com/2020/02/07/100-odd-landmarks-to-spread-across-your-fantasy-world/
table = [
    (
        "A large oak tree that is swarming with beautiful blue butterflies in the morning, and blue fireflies at night.",
        1,
    ),
    (
        "A cave hidden deep in the forest, with walls and floors that seem to shine with a fortunes worth of priceless gems that sparkle without any light. These “priceless gems” immediately turn to useless stones once removed from the cave.",
        1,
    ),
    (
        "A large Cave system found in the middle of a jungle. The only known opening to the cave was found by a group of locals who were hunting in the jungle that day. The cave entrance spans an opening of roughly 100ft, and if seen from the sky looks like a large impact crater. The depth of the cave is unknown, and no one knows if it is inhabited by monsters.",
        1,
    ),
    (
        "A large tree that has a village of sprites living in it. The tree moves to one of three positions in the forest every week.",
        1,
    ),
    (
        "A tiny island in the center of a lake. There is a single bullywug sitting on the island eating fish on an improvised raft.",
        1,
    ),
    ("A magical floating bush. It hovers around in circles.", 1),
    ("A hollow tree stump with a friendly faerie dragon.", 1),
    ("Erosion has carved what appears to be a face into the side of a cliff.", 1),
    (
        "A giant skeleton sticking out of the ground. Looks like a triceratops, but larger.",
        1,
    ),
    (
        "A giant flower with lots of bees surrounding it. Thousands of flowers similar to the giant one grow around it at a wide range of heights. Different kinds of fey live around it too.",
        1,
    ),
    (
        "An overgrown, moss-covered, patinaed statue that looks just like elderly versions of the party.",
        1,
    ),
    ("A pond of sulphide water, with a geyser regularly rising at its centre.", 1),
    ("A cliff face with geometric crystal structures jutting out of the side.", 1),
    (
        "A cave entrance with several sharp rocks resembling the maw and teeth of a large beast.",
        1,
    ),
    ("A tremendous pillar of rock in the exact center of a dried lakebed.", 1),
    (
        "A small pond in the center of a clearing. The pond is faintly luminescent and flowers grow around its edge.",
        1,
    ),
    ("A large smooth stone with runes in an ancient language adorning its surface.", 1),
    (
        "A beached shipwreck that has been looted and broken on the shore. Overgrown with algae, seaweed, and barnacles.",
        1,
    ),
    ("A cliff with sharp rocks below known to locals as the maw of the sea.", 1),
    (
        "A large tree that is over 30 feet in diameter. This hulking monstrosity of nature has been cared for by locals and some revere it as a god.",
        1,
    ),
    (
        "A frozen lake with a polished ice surface. If you look closely enough, you can see dead floating beneath the surface.",
        1,
    ),
    (
        "A rock formation that looks eerily like a grinning goblin if viewed from the proper angle.",
        1,
    ),
    (
        "A mountain range that when viewed from above looks like a gigantic quadruped monster.",
        1,
    ),
    (
        "The ribcage of a giant whale that fell out of the sky a long time ago, surrounded by a field of petunias. Local legends differ in how it got there, but the most accepted answer is that it was an unexpected side effect of a wizards reckless attempt to mess with the nature of probability.",
        1,
    ),
    (
        "A rocky, windy precipice rises above the surroundings, with vultures perched on every available foothold. Locals say the place is terribly cursed, but in reality the vultures only congregate there because the wind allows them to smell corpses from a great distance.",
        1,
    ),
    (
        "Stone God’s Thumb: Large fist of a mountain with a peak resembling a thumb. A plot of onions and a natural spring are located at the top.",
        1,
    ),
    (
        "The Carved Oni Heads: Early Dwarven cultures carved these stone markers to ward off demons. They break the tree line and denote a path between two prehistoric dwarf cities each stone just within sight of the other.",
        1,
    ),
    (
        "The Firefall: A rare geological phenomenon causes a plume of fire to escape a lone lava tube and cascade down instead of up. There might be something special hidden behind it…but mostly the charred remains of people who thought there was something behind it.",
        1,
    ),
    (
        "A rotting, moss covered bookshelf in a forest clearing. Its decrepit shelves are filled with molding tomes in various states of decay. What is still legible in the books is a variety of languages and dialects, some unknown.",
        1,
    ),
    (
        "A massive mushroom with a wide, flat top. Only the top is visible, and the rest is below ground. It will slowly rise from the the ground when it thinks no one is watching. If something looks at it while it is extended, it will quickly slam back into the ground.",
        1,
    ),
    (
        "An old and gnarled tree has grown over and half-swallowed what appears to be the remains of a cart – the wood has rotted away, but the metal axel is still visible.",
        1,
    ),
    (
        "A tree has fallen over a creek, its trunk forming a narrow bridge. It would be easy for a small-sized creature to walk across, but medium-sized creatures might have difficulty.",
        1,
    ),
    (
        "A cluster of bright pink and yellow mushrooms have grown over and completely blanketed a rotted tree trunk.",
        1,
    ),
    (
        "A series of miniature arches that is nearly always in the shadow of a larger arch.",
        1,
    ),
    (
        "An extremely deep and narrow slot canyon. It’s easy to jump over, but if you fell in it would mean certain death.",
        1,
    ),
    ("An enormous boulder balanced precariously on a thin, natural pillar.", 1),
    (
        "A wide, flat field completely covered in small holes… Something is living underground here.",
        1,
    ),
    (
        "Enormous bones are scattered densely in this area. It’s a graveyard where large beasts come to die.",
        1,
    ),
    (
        "A set of standing stones with intricate carvings cut into them. When the wind blows a certain way, the stones make a low humming sound that can be heard from miles away. The sound fills anyone that can here it with dread and despair.",
        1,
    ),
    (
        "A small dark cave with with an extremely narrow crack in the floor, with steam billowing out. Due to the nature of the steam and the shape of the cave, it creates a low whistling sound at all times of the day.",
        1,
    ),
    (
        "A magical Island that is invisible to those who don’t or can’t use magic; because of this may ship captains have crushed on its beach with no survivors due to the island’s security system. From the outside the island appears to a cluster of destroyed ships that have created a ring around the island, but when most captains see this mysterious landmark they write it off as ships running aground on a reef.",
        1,
    ),
    (
        "The ruins of a Tower once connected to a series of watch stations that surround this area or did in the ancient world. There are several of these towers, each with their own secrets.",
        1,
    ),
    ("An area of land in a forest where no plants can grow.", 1),
    (
        "A Forest with many small trees with 1 very large tree in the center of the same species.",
        1,
    ),
    (
        "A pond of water that rotates one direction in the morning and the other direction in the evening.",
        1,
    ),
    ("Cliff Face that appears to have a large portion removed by a giant bite.", 1),
    (
        "A tall rock formation with two boulders at the bottom… Totally not phallic… (It is).",
        1,
    ),
    (
        "A small statue of a hooded sitting hunched figure that always points slightly northwest.",
        1,
    ),
    (
        "A large stone monolith towering upon a hillside. Along the back, a single rune written in charcoal and in the language of giants, the symbol for “help”.",
        1,
    ),
    (
        "A dried up river or stream, with the remains of a long forgotten exodus. Bones stick up through the mud at strange angles.",
        1,
    ),
    ("A small chasm cutting across an otherwise open field.", 1),
    ("Two tall pines holding up the skeletal remains of a behemoth.", 1),
    ("A massive multi-faceted field of quartz.", 1),
    (
        "The Award-Winning Fjords of Slartibartfast: They’re fjords, they’re incredibly beautiful, and they’ve won awards for being incredibly beautiful. Can be used for hidden bases, surprise attacks from the cliffs above to the passages of water below, a suddenly dangerous yet exciting end of a chase off the edge of one of the cliffs, or just a pleasant boat ride.",
        1,
    ),
    (
        "A roughly circular depression overgrown with strangely warped vegetation. The very middle is raised and bare rock looking almost like cracked dark glass.",
        1,
    ),
    (
        "Two trees, an ash and an elm which have grown up so close that they spiral around each other as they grew trunks and branches pressed together and entwined.",
        1,
    ),
    (
        "The Stone Queen’s Bed: A stone giant made the mistake of picking a fight with a pack of druids. Rooted and slammed into the earth they planted Somnus trees all around the raised crater. The constant stream of pollen keeps her in a perpetual dream state.",
        1,
    ),
    (
        "The Volcano Coral Tubes: A sulphuric smoke constantly rises from these inhospitable series of rock tubes. Large filter feeding red fronds rake the air in an effort to capture nutrients from the plumes of smoke. Glows red and attracts lightning strikes.",
        1,
    ),
    (
        "Morla’s Daughter: In the middle of a swamp is a lone mountain with a small town at the top. There is something weird about the tortle settlement that leads visitors to think they are hiding something…even the mountain is shaped like a turtle shell.",
        1,
    ),
    (
        "A sudden 12ft escarpment running roughly north-south for as far as the eye can see. Almost as if the all the land to the east as far as the sea had suddenly dropped 4 yards overnight.",
        1,
    ),
    (
        "A region of open sand dunes a half days hike across and several days hike long that has swallowed a northern rainforest. Only the tops of verdant hills peek through like tree islands in an ocean of sand.",
        1,
    ),
    (
        "A weathered treestump about the height of a man. Dozens of age-tarnished coins have been hammered into one side of the stump.",
        1,
    ),
    (
        "A large black obelisk stationed in the middle of a small island that is within what is now a lake. A river eroded the area and over the course of time the river carved out a small lake around the obelisk.",
        1,
    ),
    (
        "A small cave at the start of river or brook. Inside the cave is small oasis, a waterfall, pool of crisp clear water, and flowering vines crawling up the walls leading to a an opening that lets in sunlight.",
        1,
    ),
    ("An old tree with a fox shaped canopy when viewed from the South East.", 1),
    (
        "A small clearing between some rocks, with three sitting petrified trolls, with horrified looks in their faces.",
        1,
    ),
    (
        "Two extremely close peaks with a river flowing between them. Looks like a mountain that was cut in half by the water.",
        1,
    ),
    (
        "A big colorful crystal coming out of the ground, that separates the light that comes through it, creating miniature rainbows.",
        1,
    ),
    (
        "A tiny volcano, that spews small embers, burning the vegetation directly next to it.",
        1,
    ),
    (
        "Huge bones are in the area, sticking out from ground. An elephant could fit in the middle of them. They belonged to the abdomen of a really large creature.",
        1,
    ),
    (
        "A giant’s skeleton on the side of a cliff. A large sword still stuck through it’s chest.",
        1,
    ),
    (
        "A flooded pit quarry; standing neck-deep in the murky green water is the 75′ statue of a human king, his features fixed in a contemptuous snarl. Birds nest in his nostrils.",
        1,
    ),
    ("Tar Pits rumored to have claimed the lives of various monstrosities.", 1),
    ("A winding path of high ground through a swamp, called the Witches Walk", 1),
    (
        "A tall rock surrounded by 20 evenly spaced smaller rocks. The smaller rocks have ancient number tunes on them, this structure is clearly some ancient sundial.",
        1,
    ),
    ("A statue of a panicked witch in between a fork in the road.", 1),
    (
        "A pine tree that curves wildly. They say if you listen closely for a while you can hear the wails of the ghost trapped inside.",
        1,
    ),
    (
        "A pit that is at least 50 feet deep. The bottom is always obscured in the darkest shadow.",
        1,
    ),
    (
        "Native hobgoblin burial ground that brings pets back to life with the fiend subtype added. Anything you bury will come back and try to kill you. (A groundskeeper named Sking optional.)",
        1,
    ),
    (
        "Three treefolk have pinned down a stone golem. Roots have all but immobilized the once rampaging construct. It’s been 100 years since the battle and the treefolk are still sleepy from all the action.",
        1,
    ),
    (
        "A soda geyser field that shoots out carbonated water out of the ground. Could be very profitable with anyone thinking of selling goodberry/fruit tonics the next town over.",
        1,
    ),
    (
        "A group of islands with a mountain range in them. From the distance the peaks resemble a dragon’s claw emerging from the sea.",
        1,
    ),
    (
        "What appears to be a puddle is actually a 30 foot deep pool of water with a 10 foot radius. Upon diving under, it appears to be full of tropical ocean life, and those submerged can hear what sounds like waves crashing on the surface.",
        1,
    ),
    (
        "An invisible mountain. The only way this mountain is visible is by a seemingly floating waterfall beginning at 50 feet in the sky. (it is coming from a cave in the mountain.)",
        1,
    ),
    (
        "A twenty foot high mushroom, enclosed in a circle of smaller mushrooms of varying heights(up to 5 feet). A history check reveals this location to have been home to a giant toad who would rest on the largest mushroom. Occasionally a ghostly ribbit pierces the air.",
        1,
    ),
    (
        "A snow-covered field that looks flat, but the powdery snow covers up areas that are much deeper than expected. Heavy creatures could fall chest-deep (or worse) at any time.",
        1,
    ),
    (
        "A small tropical oasis that exists year-round in the middle of a frozen tundra.",
        1,
    ),
    ("Something about the weather of this place makes it rain perpetually.", 1),
    (
        "A volcano that is constantly spewing forth smoke. It’s never erupted, however.",
        1,
    ),
    (
        "A swamp that experiences daily earth-tremors. When these happen, the water drains briefly and then refills over the next day.",
        1,
    ),
    (
        "A clear, cold mountain spring that releases the same liquid as a healing potion. When the liquid has been out of the spring for more than an hour, it becomes normal water.",
        1,
    ),
    (
        "The Drow Stone – Jutting at an odd angle off the side of the path is a towering pillar of stone which is made of a dark glass like material. Stories abound of how it marks the entrance to the Underdark, however, it’s simply Volcanic glass from an ancient volcano.",
        1,
    ),
    (
        "The Salt Chasm – Rock shafts, split into hexagonal patterns, known as Columnar Basalt pervade this small valley. Their presence precludes the growth of any significant plant life.",
        1,
    ),
    (
        "The Cascading Quagmire – a series of shallow broad drops in a slow moving swamp river. The combination of floating peat moss and thick algal blooms makes what would be waterfalls instead a viscous slime dribble.",
        1,
    ),
    (
        "“Howlker’s Rise” A naturally formed column of earth and stone that is only around 75 feet in diameter with a roughly circular shape, but goes up almost 300 feet straight up. It is covered in moss, plants and even a few sideway-growing trees, it is said to have a lake on top and has a plunging waterfall that goes from the top all the way down to the pond at is souther footside. The climb is brutal. A Dwarven man named Howlker Dirtnose is said to have lived a top it for a time, after finding some very tricky caverns leading upwards along the inside of it, but no one ever manages to even find an entrance.",
        1,
    ),
    (
        "The Lonely Sentinel: A massive oak tree stands alone in a vast field, not far from a cliffside overlooking the sea. It bears the scars of numerous lightning strikes and more than one attempt to chop it down, but it is still healthy and strong.",
        1,
    ),
    (
        "A natural bridge of dirt that goes over a wide area of reed thicket marshes. The wind slowly sways the cat tails and tall grasses as squishing sounds and croaks can be heard from either side of the bridge.",
        1,
    ),
    (
        "A very large tree covered in clear stones. If a creature of good approaches the tree, the stones and the leaves will grow green and blue, and flowers bloom on the tree. Neutral creatures makes them turn brown and orange. An evil creature makes them turn dark purple and red. Unaligned creatures make them turn different shades of gray.",
        1,
    ),
    (
        "A bush that seems unaffected by the wind. If a lawful creature approaches the bush, the feeding of a calm wind will pass both the bush and the creature. A neutral creature will cause a moderately strong wind to affect the two. A chaotic creature causes hurricane level winds to hit both of them.",
        1,
    ),
    ("A cave full of phosphorescent mushrooms that glow at night.", 1),
    (
        "The Pillar of First Blood – A 15ft dark stone pillar that has engraved writing on each side ‘The spot where the first blood was split between a batch of common devils”.",
        1,
    ),
    (
        "The Drawing Moss – A smooth stone with a bunch of growing moss on it. Touching the stone with a bare hand results in the moss slowing moving to wherever was touched. On the stone are several handprints and doodles perfectly covered over with the moss.",
        1,
    ),
    (
        "Curci’s Crypt – A small white stone structure deep in the woods with carvings of trees on each side. Entering brings you into the hidden crypt of Curci.",
        1,
    ),
    (
        "The Crumbling Shack – Far away from any civilization lays what once was a small shack. The windows are broken, some walls have crumbled away, and parts of the roof are open and fallen in.",
        1,
    ),
    (
        "Trio of Faces – On the side of a rocky cliff are a well carved trio of protruding faces all looking the same direction",
        1,
    ),
    (
        "Cone Shaped Prison – In the middle of a grassy field stands an 8ft slim cone made of iron bars, in the middle of the structure lies a sun-bleached skeleton bound in iron shackles.",
        1,
    ),
    (
        "The Tree of Sacrifice – A abnormally large and oddly pale brown tree where the branches are twisted, and the leaves are a sickly saturated green color. At the base of the tree lies a blood stained alter that the roots of the tree have grown around it and now hold it in place. The base of the tree as well as the ground around the alter are permanently stained a deep red. If the tree is cut, a thick blood sap seeps out of wound. If a creature is sacrificed on the alter, the blood pools near where the roots touch the alter and are absorbed while what appear to be veins appear on the tree that go up into the branches.",
        1,
    ),
    (
        "The Bone Pit – In an open field there is a 10ft wide and 50ft deep pit with no life growing around it. The walls of this chasm are lined with dark cobblestone and going down there are three uneven sized holes that are covered by iron bars. At the bottom there are a large pile of bones.",
        1,
    ),
    (
        "The Odd Stone Slab – A big square stone slab rests hidden near the side of the road. Carved into the slab is a symbol and a riddle that upon answering correctly leads to a small dungeon.",
        1,
    ),
    (
        "The Copper Fox – A 4ft oxidized copper statute of a fox with a small locked box in its mouth and two ruby eyes.",
        1,
    ),
    (
        "The Pointing Eagle – On top of a large rock formation is a big iron statue of an eagle pointing its body to the east.",
        1,
    ),
    (
        "The Feasting Table – Out away from any kind of civilization sits a large gray solid stone table with ancient carvings on the sides. Upon its surface are newly lit candles and a banquet of food that seems to be warm, fresh, and untouched by its surroundings. If one where to eat or take anything from the table, the next day it would be completely restocked and replenished.",
        1,
    ),
    (
        "The Jeweled Bush – A seemingly average looking berry bush that happens to grow small jewels instead of berries. If one where to try and consume one of the jewels picked off of the bush within 24hrs, that person gains a temporary magical effect or bonus, otherwise it’s a normal jewel.",
        1,
    ),
    (
        "The Ice Blood Spot – Located on the cliff face of a large mound of ice there is one spot that is dark red instead of the pure blue that surrounds it.",
        1,
    ),
    (
        "Dragon’s Graveyard – in a valley, there are 8-10 adult dragon skeletons, half-buried.",
        1,
    ),
    (
        "Petunia, the Land Whale – A large whale skeleton surrounded by petunias. The whale is miles away from the sea and the petunias aren’t native to this location.",
        1,
    ),
    (
        "Wondrous Obelisk – an obelisk, comprised of rose quartz and decorated with sylvan runes, appears to be of fey origin. it is surrounded in a 120-foot field of wild magic.",
        1,
    ),
    (
        "The Old Folk Hero – A half erected statue of an old folk hero. Either under construction or half crumbled.",
        1,
    ),
    (
        "The Hope Tree – It’s an oak tree with the word hope carved into it in large letters. No one knows who did it or why, but it’s turned into a useful landmark for the local village.",
        1,
    ),
    (
        "The Moon’s Egg – It’s a massive dome-like stone formation that shines pearlescent in the moonlight. It lays in a bare outcropping of rock and is warm to the touch.",
        1,
    ),
    (
        "Hollering Pit – A 50ft deep sinkhole. Well-hidden at the bottom is the lair of an accomplished burglar who calls himself the Jeweler. He’s too old to do much in the way of harm, but the countless traps he installed are not.",
        1,
    ),
    (
        "The Painted Cliff Face – A cliff that has been entirely covered in paint from hundreds of people.",
        1,
    ),
    (
        "Threeshades Tower- A weathered, ivy-mantled square tower atop a small hill. Has three levels, and each is built from a different kind of stone. The longsword stuck in one of the bricks on the top level is +1 and can project the bearer’s voice up to 50’ away.",
        1,
    ),
    (
        "Pigeons’ Chest – an ornate, but empty, chest of silver and pearl sitting by the road. It will not move by any means yet discovered, material nor magical.",
        1,
    ),
    (
        "The Ol’ Inn – The ancient ruins of a strangely ‘modern-looking’ tavern located in the deepest patches of forest. No path leads to it, no other buildings or ruins are found besides it, but dozens of deformed footsteps can be found heading out of the site. At night, the faint, muffled sound of a single viol can be heard coming out of the muddy floor.",
        1,
    ),
    (
        "The Forgotten Emperor’s Statue – An incredibly detailed, broken bust of a young wood elf, bearing a red crown. Its nose and left ear are missing and where its left eye should be, the socket is destroyed, and a monstrously decomposed snake eye can be found. The base has a bronze plaque which reads (in broken Celestial): ‘The only one truly meant to rule’, followed by a name which seems scratched out.",
        1,
    ),
    (
        "The Candle Trees – deep in the woods, a small group of trees whose leaves are bright red. They contrast starkly with the normal trees around them. The Candle trees appear otherwise normal, but the dried leaves can be brewed into a tea that warms the bones even on the coldest nights.",
        1,
    ),
    (
        "Tale of a Desert’s Origin – A granite obelisk in the desert with glyphs on it. It seems to tell the tale of a very powerful magic user stealing all the life from this area, killing all the plants and turning it into a desert.",
        1,
    ),
    (
        "The Waning Waterfall – a small waterfall that appears to reverse direction on every night with a bright full moon, running up instead of down.",
        1,
    ),
    (
        "The Sandmount – There’s a strange dune of sand in the middle of this grassy field, covered in scorpions.",
        1,
    ),
    (
        "The Awoken Stones – three stone pillars at the top of a hill, each engraved with a different rune of no known language. The pillars appear to change positions, but how this is done is unknown.",
        1,
    ),
    (
        "Ghost village – There’s a half-buried village in the sand, with sandstone walls being the only remnants… except for one house, which has a simple roof and door carved into the stone.",
        1,
    ),
    (
        "Impossible Shipwreck – Dashed upon the rocks are the remains of a large merchant ship. Weathered and ancient, the skeletons of the crew still scattered around though most everything of value has long since been looted. The most peculiar thing about this is that the rocks, and ship, are in a cavern 100ft underground, miles from the nearest navigable waters.",
        1,
    ),
    (
        "Sapphire Beach – a small stretch of coastline hidden between two nigh-inaccessible cliff faces. The sand is particularly fine and a brilliant blue. Rumor has it that the sand was formed when giants destroyed the jewel horde of a local dragon. There are also rumors of a dragon being sighted in the oceans nearby. Digging deep into the sands turn up giant bones.",
        1,
    ),
    (
        "The Lovers’ Spring – a secluded hot spring, with the initials of many young lovers carved into nearby rocks. Discarded and forgotten undergarments can be found on tree branches in the area.",
        1,
    ),
    (
        "The Arms of the Last Bard – A broken but thick 15ft wide half-circle embedded to the ground made of quartz and intricately laced with gold strips. An assortment of precious gems are embedded in its surface. Any attempt to collect and/or destroy this construct will cause severe psychic damage and a loud high-pitched tone to play loudly. The half-circle aligns perfectly with sunset/sunrise and every time it does, the most beautiful flute melody plays that is sourceless.",
        1,
    ),
    (
        "The Iron Tree – A big, old tree which seems to be made of iron, but as far as anyone can tell, is alive and growing, if slowly.",
        1,
    ),
    (
        "Hades’ Hand – A 15ft tall stone hand stretches from the ground, reaching for the sky.",
        1,
    ),
    (
        "The Stone Toad – A gigantic stone carving of a toad’s head, crumbling, half-buried, and covered in moss.",
        1,
    ),
    (
        "The Wrecked Ship – The sun-bleached wreckage of a ship that ran aground long ago. Inside the hull is a massive cage with thick steel bars that appear to have been smashed outward from the inside.",
        1,
    ),
    (
        "The Three-Sided Tower – A half-collapsed stone tower with curious triangular architecture. The bones of a lonely watchman sitting in a chair lie atop it. The watchman wears a helmet shaped like a triangular pyramid. Several towers of this type can be found around the same area.",
        1,
    ),
    (
        "Giant’s Playground – this field is entirely stone, and many massive footprints can be seen stomped into it. There are boulders laying around, some cracked.",
        1,
    ),
    (
        "The Fallen Hero – The legs of a giant metal statue standing beside the top of a waterfall overlooking the valley below. At the bottom of the lake below the falls, the head and torso can be found. It appears to be the likeness of a famous ancient hero that a PC might recognize.",
        1,
    ),
    (
        "The Charity Cave – A cave with a chest that says, ‘if you take something, leave something.’ It’s unlocked and has several trinkets inside.",
        1,
    ),
    (
        "The Eye of the Moon – on top of this hill is a pool surrounded with stone. The water is always cool, and at night the full moon can always be seen in its reflection, regardless of clouds or moon cycle.",
        1,
    ),
    (
        "Bigfoot – A large tree in the forest that bends and splits in such a way that the bottom looks like a foot, with toes.",
        1,
    ),
    (
        "Goddess of Death Statue – A worn smooth but still recognizable ancient statue of a goddess of death. At her feet sets a black stone bowl filled with fresh rose petals. If you were to kneel down at the bowl and look up at her, you would see her eyes stare unwaveringly into yours.",
        1,
    ),
    (
        "The Red Altar – in the middle of a copse in a strange swamp lies a smooth altar made of red stone, with strange carvings of trees and water all around its base. Upon touching the altar, you will hear a voice in your mind ‘sacrifice”, and you will feel a strange primal urge to sacrifice a creature on top of it.",
        1,
    ),
    (
        "Timnar’s Beard – A copse of trees growing in a single spot on an otherwise barren mountain. Unbeknownst to the world, it is the burial place of a great wizard of earthen magics. It is watched over by a trio of stone golems and a handful of slumbering treants to guard the immense knowledge held within the tomb.",
        1,
    ),
    (
        "The Sundered Mount – a mountain that appears to have been cleaved in two and creating two crumbling peaks with a narrow cut of a valley between them. It does not appear naturally created.",
        1,
    ),
    (
        "The Mage Wastes – A region where fertile grassland suddenly stops and abruptly becomes a barren wasteland of decaying grass and reddish soil. It seems as if it was the sight of some magical battle. The ground is pocked with craters and scorch marks, yet it seems as if this battle was an ancient long finished, but the battlefield has remained a wasteland frozen in time.",
        1,
    ),
    (
        "The Dragons Maw – A series of jutting tooth like spires of black igneous rock which rise out from the sea. These “teeth” have proven to be an extreme hazard to sailors and shipping which pass too near to them. Tearing hulls and ripping sails.",
        1,
    ),
    (
        "The Gods Sacrament Statue -A old weathered statue of a god with beautiful gems inlaid and surrounded with wicker basket offerings of gold, flowers, food, and trinkets. Stealing from the statue result in a curse (permanent level of exhaustion) from the deity until either greater restoration is cast on the thief or they repent and make an offering of twice the amount stolen. Award inspiration for respectful offerings or prayers given to the statue.",
        1,
    ),
    (
        "The Dragonblood – A massive artwork carved into a boulder placed some ways away from the banks of a nearby river. The artwork seems to depict a struggle between giants and dragons, with the giants as the victors. The faintly red runes which line it are giantish, and anyone who can decipher them will read that it marks a momentous battle between giants and dragons, over which should decide the course of the river.",
        1,
    ),
    (
        "The Daughter of the Sun – An enormous stone of a singular soft yellow color. It is hot to the touch but by day it is warm and comfortable simply standing near it. By night however the stone begins to glow brightly, illuminating its surroundings in radiant golden light. Large chips of the same stone can be found in the foliage growing around it. With similar glowing properties.",
        1,
    ),
    (
        "Would you kindly -A sentient door in the side of a mountain that has short term memory loss. He has no idea of his name or how to open himself but enjoys talking with travelers none the less. Speaking the magic word “please” will cause the door to open revealing a shortcut through the mountain. No form of magic or otherwise can lead through or get around this door without speaking the magic word due to an ancient magical barrier.",
        1,
    ),
    (
        "The Bread Boy – a small statue in a park depicting a street urchin. In one hand he has what is left of a small loaf of bread. With the other hand he is spreading crumbs for the birds, so they do not go hungry too. A place where the street kids gather.",
        1,
    ),
    (
        "Sculpture Garden – a small clearing in a forest, near a cave mouth, contains dozens of statues of humanoid creatures, many armed & armored, all with looks of surprise & horror on their stone faces.",
        1,
    ),
    (
        "Saben’s Cauldron – a large, circular pool off of a main river which is geothermally heated.",
        1,
    ),
    (
        "The Teeth – a series of vaguely conic stone spires lined up along a gentle arc. Each is over 15ft tall and 5ft across at the base, and tapers to a narrow tip. Nobody knows the origin of this formation. Some say the teeth are all that remains from some colossal dragon skeleton, others think the stones were placed there by a dragon cult, or as a sign from Bahamut.",
        1,
    ),
    (
        "Mage-Crater – a 120ft diameter crater. Now filled with water and inhabited by pond creatures.",
        1,
    ),
    (
        "The Old Man – a natural rock formation that just happens to look like the face of an old man with a long beard. Ruins of temples from several ancient civilizations can be found in the valley below, apparently attracted there to worship the face, or perhaps just to be under his watchful gaze. Most humanoid races in the region are sure the old man looks like their race and have their own legend about him.",
        1,
    ),
    (
        "The Deino Flats -roughly 40 acres of salt flats. A long dried up saltwater marsh from ancient times.",
        1,
    ),
    (
        "Grand Defender – a large, symmetrical hill where the site of a great battle once was. Stone rubble and ruins barely peaks out from the top. Flowers are left there every so often.",
        1,
    ),
    (
        "The Adventurers Billiard Hall – A stone statue of a Local adventurer rests on a green glass dome in the center of a public lake. The dome is lit gently from beneath. Somewhere nearby lies a dilapidated entrance which runs through a small puzzle focused dungeon.",
        1,
    ),
    (
        "Turned-Inn – An inn that has been carefully constructed to appear as if it was turned upside-down.",
        1,
    ),
    (
        "The Signposts – A collection of several dozen poles each with a dozen or more signs mounted to them pointing towards various distant lands, nearby businesses, and bizarre joke locations. It started with travelers who erected a signpost pointing to their distant homelands which other travelers added to. Eventually it got out of hand.",
        1,
    ),
    (
        "Worm’s Desert – A small sandy desert only a couple hundred acres in size of so. A great desert-making worm arrived from another world and sought to covert the world into an ecosystem like its home but caught a local disease it was unresistant to and died before it made much progress. The residual poison from the worm’s body deters plants from overtaking the sand.",
        1,
    ),
    (
        "Lightning Lab – A bizarre building with a strange mushroom-shaped metal lattice on top. It was the lab of a researcher studying non-magical electricity who died from electrocution.",
        1,
    ),
    (
        "The Sandlot – A square of property with no building where children come to play. A greedy landlord raised the rent on a long-term elderly tenant when they purchased the property, driving the tenant into poverty and eventually death. The tenant cursed the land with dying breath that no-one would never profit from the property. Every future tenant was driven out by terrifying haunts, and eventually the building was burned down.",
        1,
    ),
    (
        "Dwarven Monument – An enormous high relief of six dwarven warriors cut from a cliff pointing the way along, commemorating their epic journey.",
        1,
    ),
    (
        "Atlas Boulders A series of differently sized large stone spheres far too large for a man to lift. The strongest giants would lift them to prove their strength. They sometimes move, so perhaps the giants still use them.",
        1,
    ),
    (
        "Ancient Battlefield – ramparts, high hills, and trenches filled with water that stretch for mile marking the location an ancient battlefield. It has grown over.",
        1,
    ),
    (
        "The Epicenter – A large swath of woods where all the trees in a massive circle have been bent at a 90-degree angle towards the center but continue to grow that way. There is nothing (currently) anomalous at the center, but a powerful coven of druids hold it as one of their holiest places and guards it closely.",
        1,
    ),
    (
        "Ol Demons Place – a once portal to the abyss, sealed by hero’s long ago, now just a crumbling arch with an unsettling aura.",
        1,
    ),
    (
        "The Broken Hill – a hill that you need to walk uphill to get to and walk uphill to get away from.",
        1,
    ),
    (
        "The Rooster of Mourning – An enormous statue of a rooster, made from a strange metal, finely detailed and colored. It is hollow, and when the first ray of sunrise strikes it, a great, sad-sounding crow arises from it. Legend says that it commemorates a great battle in the distant past.",
        1,
    ),
    (
        "The Angry Spot – a small stone platform on the top of a hill, standing on the platform makes a person irrationally angry. Barbarians may involuntarily rage as a result.",
        1,
    ),
    (
        "The Alter of a Thousand Arms. – At a crossroads sits an unusual statue, made of stone it stands over 10 feet tall and has arms sticking out in every direction with their palm turned upwards. In nearly every hand there is a candle, some still lit but most are fully melted. Placing a candle in one of the hands and lighting it will give the player the blessing of ‘A helping hand.’ When a player next fails a roll, they may roll an additional d6 and add it to their total.",
        1,
    ),
    (
        "The Weeping Sister – A fifteen-foot statue of a girl unmarred by time. Next to her are the shattered remains of another statue, close enough that the body may have once held her outstretched hand. The feet of this larger statue are all that remain affixed to the earth – the rest is scattered throughout the clearing. Water, clean and pure, travels down her face in steady rivulets but leaves no erosion there.",
        1,
    ),
    (
        "The Sensible Stone Head -a large stone head protruding from the surface of a glacier. It is the head of an earth elemental and if you get his attention, he is friendly. If asked what he is doing their he replies ”swimming in the river”, given he exists at a geological place the slow flow of the glacier is like a river to him.",
        1,
    ),
    (
        "Glass Tree – A fairly tall an elaborate tree made entirely out of glass raises from the earth, at its base there is a plaque written in dwarven, it’s to commemorate a dwarf leader who fell in battle.",
        1,
    ),
    (
        "The Titan’s Blade – A 50 ft rust covered sword driven into the earth. The whole area has a magical aura and no wildlife lingers within a quarter mile of the sword.",
        1,
    ),
    (
        "The Well of Good Tidings – A well by the side of the road that is a base in a local hafling tradition that if one where to lose a tooth, that it is to be tossed in the well with a tip of the hat. When doing so, good fortune is sure to come. Characters that throw in teeth later find small amounts of wet coins in various locations on their person. Characters that throw rubbish, or are otherwise disrespectful of the well, find their respective objects on their person once more soaking wet and covered in bite marks.",
        1,
    ),
    (
        "Skilltown – A small but clearly once-bustling town lays abandoned inside of a titan’s skull. The skull is half buried in the sand; its eye sockets and mouth aim up at an angle. Walking through its mouth is the only way to enter the town. The skull looks to be that of an enormous version of whatever scariest creature lives in that area. It provides ample shade during most of the day.",
        1,
    ),
    (
        "Best Rest Graveyard – A cleric once prayed over a graveyard that all within would ‘rest well.’ Now anyone who falls asleep in that graveyard has the best night of sleep they’ve ever had.",
        1,
    ),
    (
        "Bird Hill – a grassy hill of noticeable height rises from the otherwise flat plains. On the hill are several lines of cobblestone that do not grow grass and have no discernible pattern from the surface. If flying, however, you see the cobblestone lines form the shape of a bird, along with some arcane symbols. If you happen to look up during the spring or fall, you’ll see migratory birds alter their course to fly over this hill.",
        1,
    ),
    (
        "Stairway to Nowhere – All that remains of an ancient fortress, the remarkably well constructed staircase rises for 3 stories out of the ground at the end of an ancient road, and then just abruptly stops.",
        1,
    ),
    (
        "The Crossroads – This is the place where four kingdoms meet. The main road for each lead to a massive stone pillar. Many years ago, all four kingdoms were at war, and a pillar was placed there as a symbol that none from neighboring kingdoms would be allowed to cross. It is now an annual meeting place for the four to discuss their continued amnesty.",
        1,
    ),
    (
        "Cloudland Canyon – It’s a canyon nestled in a northern mountain range that’s so high even the base of the canyon is a higher elevation than most of the other mountains in this world. Wondrously magical things occur here.",
        1,
    ),
    (
        "Stone Tree Garden – It was a garden from a former ancient culture, which vanished out of unknown reasons. One of the only things found was this tree garden. Are the trees made of stone or turned to, no one knows.",
        1,
    ),
    (
        "‘The Circle’ -There once was a meteorite which crashed into the land. The first to arrive found weird writing in a (Insert required size) diameter circle. No one could read what was written. In the center of the circle, where the meteor should have been, there was nothing, not even a small crater.",
        1,
    ),
    (
        "The Well – A seemingly normal well on the top of a hill. Anything that is placed into it is immediately tossed out of it.",
        1,
    ),
    (
        "The Pariah’s Mountain -One mountain among an otherwise unimpressive range, its only defining feature is its completely upside down. The base measures about 60ft across, but the peak 3,000ft up is easily a mile across. Stairs may have been carved into the side, but the climb down to the summit (or is it up to the base? The locals aren’t quite sure) is precarious at times. The locals are also similarly vague when asked about what’s on top…",
        1,
    ),
    (
        "Worried stones – A group of 3 standing stones with anxiety. When encountered in their clearing, they will disappear once all eyes are off them. Careful inspection will reveal them to hiding nearby – peeking from behind a nearby tree, bottom of a lake, hidden by bushes, behind where the party is now looking, etc. If discovered, they disappear again if not observed. The stones are not malicious, and do not harm the party. They would just rather you all left them to it, thank you.",
        1,
    ),
    (
        "The Quiet Creek – An otherwise ordinary creek that runs through a forest. It is abnormally quiet near the stream, in such that there is almost no echo around it, and it is surprisingly hard to hear from a distance. All along its course stand small boulders, almost fully grown over with moss.",
        1,
    ),
    (
        "The Shifting Hills – A large field of hills, dotted with rocks, grasses, and flowers. Careful study has found the hills are constantly moving, as though old creatures crawl along under a carpet of earth. Magics which call upon the earth always seem to produce unexpected results when among them.",
        1,
    ),
    (
        "The Devil’s Wager – A large disc shaped stone at the base of a long dormant volcano. Visitors toss a copper at it for good luck. There are a couple hundred copper around it. It is considered extraordinarily bad luck to take the coppers.",
        1,
    ),
    (
        "The Swordleaf Trees – there is a patch of trees here with a non-stop turbulent wind rustling the leaves and branches violently. The leaves’ edges appear to be razor sharp.",
        1,
    ),
    (
        "Beacon Mountain – A mountain that, on some nights, has a bright ball of light form over it which slowly dissipates over several hours. Local religion strictly forbids climbing the mountain.",
        1,
    ),
    (
        "Mist Valley – a short pathway of stone carved into a mountain, roughly five feet wide with names of couples and graffiti on the stone walls. The pathway always has a thick fog settled over it, making it seem eerie.",
        1,
    ),
    (
        "Ancient Battleground – Deep in a forest, trees are marred with years old axe and sword marks. Hundreds of skeletons dressed in rusted armor and weapons lie in this area. Taking a trinket, or even loitering may be unwise.",
        1,
    ),
    (
        "True Clarity Bridge – A bridge between two high places that, for many people, while staring off the side, provides answers for their most troubling issue or deep question, whether they were looking for the answer or not.",
        1,
    ),
    (
        "Lover’s Glade – Two sequoia trees whose bases are over a hundred feet apart have grown together and connect about 160 to 180 feet off the ground. The branches and leaves of these giant trees create a pleasantly shaded area below which is often used by the local populace as sites of wedding ceremonies.",
        1,
    ),
    (
        "Round Rock – A mysterious perfectly round rock that stands nearly 20ft tall. It is too heavy to roll and never seems to chip. It is the center of many local legends, varying wildly on their truthfulness.",
        1,
    ),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {roll(table)}\n")


if __name__ == "__main__":
    main()
