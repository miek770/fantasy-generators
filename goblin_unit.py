from roll import roll


# Source: https://www.reddit.com/r/d100/comments/is3iy3/lets_build_d100_goblin_units_and_their_lore/
table_gobling_unit = [
    (
        """Civilians: All goblins were born to live and die for the mighty. Civilians may be insignificant but they make for a valuable meat shield.""",
        1,
    ),
    (
        """Goblin Scouts: The nimble footed goblin makes a perfect scout. Considered as common infantry, many Goblin Scouts have dreams of grandeur that are never achieved because of their short lifespan.""",
        1,
    ),
    (
        """Bugbear Soldiers: Strong and fast, the bugbear soldiers are frontline mercenaries, doing anything for a free meal.""",
        1,
    ),
    (
        """The Green Maws: An elite group of Paladins that fight for goblinkin. The Green Maws are normal soldiers at first until proven worthy to join the ranks of The Green Maws. Once a new paladin is chosen they are baptized in the holy tar pit of The Black Forest and swear an oath to protect goblinkin.""",
        1,
    ),
    (
        """Black Forest Rangers: Sneaky and cunning, Black Forest Rangers lay traps in wait for unsuspecting enemies while foraging for food that the tribe may eat. It’s a common stereotype that Black Forest Rangers love pork. They take great offense to this because it’s completely untrue... maybe it’s a little true.""",
        1,
    ),
    (
        """The Ghostbashers: Goblins make many enemies, some from beyond the grave. The Ghostbashers are monks that train in one thing and one thing alone, killing ghosts. The Ghostbashers are a highly revered organization for their expertise in destroying undead and their knowledge on exorcism rituals that they stole from a long dead wood elf city.""",
        1,
    ),
    (
        """Worg Riders: Goblins and world have been allies for generations. The worg riders travel on their hounds with pike in hand slaying all who have coin. Ambush tactics are common with these swift gremlins.""",
        1,
    ),
    (
        """Bugbearzerkers: Violence is bred deep within the bugbears. Those who have a particular list for blood and chaos are known as the bugbearzerkers. An unpredictable folk that kill anyone they please. Hobgoblins are employed to keep them in line but even then they tend to do as they please.""",
        1,
    ),
    (
        """Hobgoblin Commander: Hobgoblins being the proud creatures they are it’s common they find success in leadership roles. Commanders are almost never liked but no single goblin will stand up to a hobgoblin.""",
        1,
    ),
    (
        """The Engineers: Only the brightest goblins get the coveted title of engineer. Engineers don’t fight in combat, instead their role lies in inventions. The engineers create all of the goblin artillery, chariots, and most importantly, explosives.""",
        1,
    ),
    (
        """Bombers: A self explanatory rank in goblinoid military. Bombers carry large bombs and detonate them in enemy lines. Many have been known to survive multiple bombing runs, some say its luck, others say they are chosen by the gods. Whatever the reason is they are feared by many an empire.""",
        1,
    ),
    (
        """Shadow Walkers: An elite organization of hobgoblin shadow monks. Most don’t believe they exist. Shadow Walkers carry out assassinations, and steal technology from other kingdoms (mostly from gnomes and dwarves). Their monastery is located in the underdark and every initiate must prove themselves you killing two other initiatives in The Pit of Darkness, a gladiator arena where the only weapon permitted is ones own fists.""",
        1,
    ),
    (
        """Beast Priests: Druidic warriors that forge bonds with the animals now nature to fight in the endless green tide. A beast priest usually takes a liking to one animal over others and gets a namesake for their choice like Styx the Crow, Bear of War, Giraffe Goblin, etc but some choose any animal and fight with what they can find.""",
        1,
    ),
    (
        """Green Merchants: Not everyone needs to participate in battles to destroy the kingdoms of order. Green merchants help out their kin a different way. Green Merchants (typically with the help of underdark dwarves) set up black markets underneath cities to trade nefarious items to the citizens above. They buy the goblin made poisons, thieves tools, etc and the coin is used to fund the goblinoid kingdoms they inhabit while also aiding those who want to cause chaos on the city above. The Green merchants live by a motto “business with a smile”.""",
        1,
    ),
    (
        """Hobgoblin War Mages: The goblin race knows the value of magic, especially when it comes to war. The War Mages spend the majority of their time studying how to destroy things with magic. The War Mages were created after the battle of mount pike where the goblinkin lost a great battle because of the high elves magical prowess. The Shadow Walkers stole the high elven scrolls of magic from their ancient libraries and ever since the War Mages have been a valuable organization for the good of the goblin tribes. Hobgoblin War Mages spend much less time on theory than other wizards, they’re only concerned with results.""",
        1,
    ),
    (
        """Hill Giants: Giant kind and goblin kind were once at war until their shared disgust of the dragonborn forged a bond between the two. Hill giants are paid handsomely with food.""",
        1,
    ),
    (
        """Trolls: A long time ago the king of goblins and the king of trolls met at the edge of the Karagov Bridge. The two fought for ownership of the bridge for 10 days until the booming voice of a god demanded the two join kingdoms to defeat the round eared ones to the west. The two agreed to help each other on their war against humans and ever since the trolls have been aligned with the goblinkin.""",
        1,
    ),
    (
        """Ogres: The Ogre and goblin friendship is a more recent one. Goblins found out that ogres will do anything for gemstones and so they deploy them in their wars for the promise of emeralds and sapphires.""",
        1,
    ),
    (
        """Catapulters: Siege equipment has been with the goblins for a long time. Goblin catapults are cheap to build since they’re made out of cheap wood and even cheaper labor.""",
        1,
    ),
    (
        """Dark Scientists: Deep in the parts of the gratpix mountain underneath the earth is the dark laboratory. A horrendous place where goblins experiment on slaves and citizens. The dark laboratory cannot run without the dark scientists who are insane and immoral enough to go through with the worst of deeds.""",
        1,
    ),
    (
        """Bugbear Hybrids: a twisted race made by experimenting with biomancy from Dark Scientists. Bugbear hybrids can be any animal but are usually mixed with bugs. Lots of horrifying spider, locust, and wasp bugbears lurk in the underground.""",
        1,
    ),
    (
        """Abominations: Ten foot tall monstrosities that breath acid and corrode metals with their sweat. One abomination requires the sacrifice of 20 goblins. It’s eyes taint magic, twisting spells into something more sickening. Abominations regenerate with incredible speed and their flesh can be squishy or hard as rock depending on their mood.""",
        1,
    ),
    (
        """G0bl1n Prototype: a failed creation from The Dark Lab. The G0bl1n was meant to be a goblin made entirely out of steel with no emotion much like the warforged, unfortunately the first attempt had escaped without having proper systems to differentiate friend or foe. The Dark Scientists are hard at work to find G0bl1n before it’s too late.""",
        1,
    ),
    (
        """Psygobs: A strange organization of hobgoblins that have psychic abilities. The psygobs are all completely insane but they’re incredibly effective fighters that have honed the ability to attack the mind. Many fear psygobs because they hear stories of those who met one and left their presence missing a brain. Thankfully these are probably just rumors, probably.""",
        1,
    ),
    (
        """Vermin Swarm Initiates: The Vermin Swarmers, also known as plaguebringers, are an organization of goblins that specialize in training rats. There are many ranks in the Vermin Swarmers with the lowest being initiates. Initiates must prove themselves worthy of rising in rank through great deeds. Initiates are not allowed to have over ten rats, if they exceed that number they must eat their rats until they have only ten. The Vermin Swarmers live in a place called The Plague Pit where they stay to avoid poisoning all of their race with diseases they’ve made.""",
        1,
    ),
    (
        """Vermin Swarm Lords: The Vermin Swarm Lords are the highest rank in The Vermin Swarmers taking orders only from the Rat King himself. Vermin Swarm Lords can have anywhere from 50-500 rats and ride on giant rats which are fed the corpses of their enemies and unloyal initiates. Vermin Swarm Lords spend their time caring for their swarm, fighting battles, and creating new diseases. The average Swarm Lord has over 15 diseases in their bloodstream and uses this to their advantage by feeding their rats some of their blood and sending them to towns and cities so they can infect their enemies. Most don’t believe The Vermin Swarmers even exist. They are very wrong.""",
        1,
    ),
    (
        """Conquerors: These murderous bugbears are trained from a young age for warfare. They take an oath in the sacred halls of destroyed temples to continue to destroy and siege. The conquerors were at first not an ally of the goblins but after King Meatsak had heard of their accomplishments he recruited them with the promise that they could wage wars all across the land. To seal their agreement he let them siege and kill everyone in the vine avenue, a city Meatsak owned.""",
        1,
    ),
    (
        """Warhorners: The Warhorners are troops that go out in battle with their trusty war horns and sound out to attack. Warhorners cast spells to assist allies and disrupt enemy forces. Warhorners are known for being talented and very attractive, for goblins. Warhorners are also required to know how to play bagpipes in case they need to lure out dwarves. The most common spell warhorners have are stinking cloud. Warhorners being the mischievous little cretins they are don’t always use stinking cloud on enemies.""",
        1,
    ),
    (
        """Gooblins: An ooze that swallowed several goblins and their weapons within a goblin lair was sealed up and used as a guard for the tribe. This gave the Dark Scientists an idea. With some gene splicing here and some acid there they created the first ooze goblin hybrid. These green dripping creatures always seem like they’re in pain.""",
        1,
    ),
    (
        """Ear Takers: One of the greatest enemies of goblin kind are the elves. With their grace and affinity for magic they have proved to be a thorn in the side of goblinkin everywhere. Ear Takers especially hate the knife ears. The Ear Takers are hobgoblin warriors that specialize in killing elves. They learn elven anatomy, elven war strategy, even their culture so they have the best chance in defeating their foe. Ear Takers unsurprisingly get their namesake from killing elves and taking their ears. While Ear Takers prefer elven prey they are accomplished mage slayers and are the perfect unit for killing wizards, sorcerers, druids, etc. The Ear Takers don’t like going on missions that don’t involve elf killing but they know when a mage is giving the goblins trouble they’re the best force to deal with it.""",
        1,
    ),
    (
        """Diplomat: not every goblin is a twisted killing machine. Some are twisted sweet-talkers. These goblins convince non-goblinoid towns and cities to let down their arms so their fellows can “liberate” them (in reality, most towns are slaughtered), or, to create new allies among the more monstrous races. Diplomats have friends everywhere, and are instrumental in keeping up good relations with the peoples of the underdark so the goblin empire can keep their most top secret facilities down there.""",
        1,
    ),
    (
        """Shattered Souls: A rank of holy warriors. The Shattered Souls are completely devoted to the word of The Great Green Lord. Shattered Souls wear only rags, eat only cheap foods, and have basic clubs as weapons. The Shattered Souls believe they must fight to keep goblinkin alive and that death is their greatest honor. Shattered Souls wear cloth blindfolds while fighting so they don’t see their foe and cower in fear. Shattered Souls come in droves and some are impeccable fighters who use hearing alone to win battle after battle.""",
        1,
    ),
    (
        """The Fizzies: When goblin science goes wrong, the test subjects are weaponized into the fizzies. Bottles and bottles of potions, poisons, acids, and explosives clink together dangerously as the fizzies charge into battle, unhinged and unafraid. The Fizzies and bombers despise each other with Fizzies saying bombers are archaic and bombers thinking Fizzies are too proud of themselves.""",
        1,
    ),
    (
        """Acid Throwers: Thanks to the genius of The Engineers they have made a secret weapon that the enemy won’t except. An acid thrower is a hose attached to a tank filled with acid that is sprayed at a trigger hold. Acid Throwers are usually bugbears but there is an occasional goblin that gets the honor of joining their ranks. Acid Throwers wear black masks with large glass eye holes that hide their face along with a black uniform. Acid Throwers take good care of their weapons and uniform or they are killed by sergeants. Acid Throwers are used to spray down walls and gates to make an entry for the rest of the army. Acid throwers have also been known to kill monsters like manticores and wyverns. You can tell if an Acid Thrower has been in an area of the stench of vinegar and decay full the air and if bones picked clean of flesh are scattered everywhere.""",
        1,
    ),
    (
        """Firebugs: In any other society arson is frowned upon, however, goblinkin with their superior ingenuity see arsonists as a useful ally. Any citizen that wishes to light things on fire must tell their tribes hobgoblin leader and they will get a tinderbox, some alcohol, and a map showing who they should burn. The Firebugs are an absolute menace to the feywild and druids alike.""",
        1,
    ),
    (
        """⁠The Pikes of The Waxing Moon: What appears to be a ramshackle mob of green kin garbed in garish gambesons proves to be the downfall of an unwary general. In a moments notice the goblins are able to assume a variety of formations that make full use of the reach of the pikes, creating a death trap for most cavalry and infantry. Their surprising discipline on and off the battlefield coupled with their vastly more organized culture to other goblins has lead to rumors that they descend from the former vassals to a feudal lord turned tyrant.""",
        1,
    ),
    (
        """The Chuckwagons: Logistics is a nightmare for any army even in the best of times, and marching on an empty stomach is well known to the green kin. Still there are a few who defy the haphazard nature of goblin warfare while combining it's strengths, as was the case with the unknown inventor of the chuckwagon. Not only operating as a supply train and mobile food preperation, the ability to quickly circle the wagons creates formidable fortress that can change the course of battle even mid-melee. However, the truly critical question of food quality depends on who prepares it. Many a halfling captive has been found in the comparatively less uncomfortable position of indentured cook; a gifted chef can even gain the awe of the rank and file with their culinary skill.""",
        1,
    ),
    (
        """The Sandmen: Many think of The Sandmen as a myth, hobgoblins that kidnap soldiers in the middle of the night to enslave? Absurd! Our garrisons are impenetrable. These are the words of the blissfully ignorant. The Sandmen wander into towns and cast sleep on people they deem fit for service. Once sleep is casted they are given sleeping poisons and put in a large sack made of skin. The kidnapped wake up to psychological torture until they break and are used for slave labor. Truly a horrific fate. The Sandmen are immortal, corrupt, vile, and very good at their job.""",
        1,
    ),
    (
        """Snake-Charmers: Goblin science gives access to many powers others might think to be... unnatural. The snake-charmers are just one example of these unnatural units. Wielding crossbows armed with snake-arrows, and hauling around massive basilisk-cannons, the snake-charmers are truly a terrifying and venomous force. The Snake-Charmers have learned their tactics from ancient yuan-ti texts stolen by Shadow Walkers.""",
        1,
    ),
    (
        """Bobgoblins: Aquatic Strikers, capable of swimming with specialized floating equipment, diving, and boarding enemy ships. These green terrors of the sea fight with small, nasty implements easily carried on their harnesses as well as grenades and tools of sabotage.""",
        1,
    ),
    (
        """Goblin Pirate Powder Monkeys: when Goblinkind discovered how easy it is to steal on the high seas the goblin golden age began. Powder monkeys are simple pirates. They board the ship, man the cannons, and clean. Many sea shanties are sung in the wide blue ocean from these brave souls.""",
        1,
    ),
    (
        """Bugbear Pirate Boaders: The towering brute force of a bugbear can be very effective in fighting. These pirates are tasked with boarding ships and shooting bows at the enemy. The Bugbear Pirate Boarders are known to many sailors.""",
        1,
    ),
    (
        """Hobgoblin Pirate Captains: Proud and demanding, Hobgoblin Pirate Captains run each ship, making sure their crew knows their place. Hobgoblin Pirate Captains are always accompanied by at least two bugbear guards and most have magic. Hobgoblin Pirate Captains have been known to destroy their ships when a mutiny starts, rather dying than lose their honor. Hobgoblin Pirate Captains are usually underwhelming but the rare few that rise above are feared across the sea like Captain Styx, Captain Gougefell, and Captain Jeniffer Holmes who got her name simply because she liked it after hearing a human say it and kills the crewmates that don’t call her by her full name.""",
        1,
    ),
    (
        """Wulf Killers: Deep in The Dark Laboratory the scientists stew and plan. Mixing genetics for the ultimate warriors. Wulf Killers are Goblin that undergo experimentation to become a blood hunter. Wulf Killers get their name because they were originally made as a way to track down a werewolf terrorizing the goblin tribes of the north but now they are used for hunting down any monsters that need a sword through their heart.""",
        1,
    ),
    (
        """Druk’s Army of The Dead: Long ago Druk was a powerful wizard known to many a goblin. He was a controversial figure, publicly showing sustain for hobgoblins. On the grand feast of autumn killed fifty hobgoblins and began to wage a civil war against hobgoblin tyranny. One day Druk vanished. The civil war was over and most assumed he was simply assassinated until he came back to the tribe with a black hood and a zombie army. He explained he no longer wishes to kill the hobgoblins as he was too powerful to waste his time in them being the important lich he is. Druk occasionally comes down from his Fortress of Necromancy in the Jagged Peaks to help his old goblin nation when they ask. Many times has Druk refused to help, he usually sends messages refusing aid by giving the messenger back in pieces with a well written note giving his humble regards.""",
        1,
    ),
    (
        """Shroomers: A unique type of goblin that lives in the underdark. Shroomers spend their days taking psychedelic after psychedelic. Shroomers worship a finger with black and red spots and a purple stalk known as the doom shroom. When called into battle is the only time Shroomers eat the doom shroom. Once eaten, the user feels no pain and gain incredible strength, speed, and heightened senses making for an ultimate fighter. One fatal problem with the doom shroom is despite its wonderful benefits. After an hour the user has a 10% chance of having a heart attack and dying.""",
        1,
    ),
    (
        """Shroomer Druids: Shroomer Druids are the holy leaders of the shroomers. They wear large mushroom cap hats and have mushroom stalk staffs. The Shroomer Druids are the ones who grow the doom shrooms and have a strange aura around them. People within ten feet of a Shroomer Druid must make a constitution saving throw or have their mind affected by hallucinogenic mushrooms""",
        1,
    ),
    (
        """Shroom Globbers: While not apart of The Shroomers, The Shroomer Globbers are still respected by them and will sometimes partake in their rituals. Shroomer Globbers are a simple unit. They take poisonous and psychedelic mushrooms from the underdark, put them in glass balls, heat them up to make gasses, and hurl their ball of drug infused chaos at the enemy. To fight in a battle where the enemy can’t even trust their own senses is a useful position to be in.""",
        1,
    ),
    (
        """The Cave Zealots: A clan of goblins and bugbears that worship a dead god. They live in cave systems and attack people who wander in their territory. Many have died but for unexplained reasons when one dies they just come back later with a scar and some stitches where the fatal wound was. Those who ask what happened and how they’re still alive are brutally killed.""",
        1,
    ),
    (
        """Lorekeepers: Lorekeepers are Hobgoblin librarians that guard the library of the cracked plains for fear of any other race gaining their knowledge. Lorekeepers don’t usually fight but when they have to they cast very high level spells in an attempt to resolve problems as fast as possible though they prefer using enchantment spells to subdue foes first.""",
        1,
    ),
    (
        """Order of The Winter King: The goblin race isn’t just satisfied with conquering the material plane. There’s an entire world of areas they can steal their claim to. The Order is The Winter King are goblins who made a deal with The Winter King, an evil fey, for powers so they can take over the feywild. The Order of The Winter King has been stopped time and time again but they are nothing if not persistent. They’ll try again each and every time until they take over the feywild.""",
        1,
    ),
    (
        """Battle Forges: A machine with four wheel and thick copper plating. The Battle Forge is a machine powered by coal and billows black smoke from two pipes on top of the machine and one pipe behind it. Each Battle Forge has a cannon that shoots molten hot cannonballs into the walls of cities or into the faces of humans. The Battle Forge has a fully functional Forge on its inside with a goblin blacksmith working tirelessly to make weaponry and pilot The Battle Forge. While traveling troops can get weapons and armor through the forge and the armor plating offers a strong frontline force to push back armies.""",
        1,
    ),
    (
        """Dinner Archers: Practiced at picking targets out of the sky to cook for supper, these bow-wielding goblins adorn themselves with the feathers of their prey (mostly pigeons). Dinner Archers often get into competitions with Black Forest Rangers and always lose.""",
        1,
    ),
    (
        """Skull Priests: Goblins worshipers of Myrkul the Lord of Bones. They aren't exactly necromancers, but they do carry some magic and have been known to use human femurs as maces. They are seen with skull masks and bone coats.""",
        1,
    ),
    (
        """Globins: Globins (globe-ins) are hunch-backed goblins who have armadillo-like shells on their backs. They are able to roll up into a ball, and propel themselves at great speeds.""",
        1,
    ),
    (
        """Scrap Goblins: Scrap goblins like to tear apart metal items they find and rearrange them to create new objects, including weapons and armour. While this gives them the appearance of trash-clad hooligans, they are actually quite sophisticated, with a society built around artistic talent and expression... though, they're also no less violent than their other kin, and can be surprisingly skilled with their odd-looking weapons. Known to collect near cities where people tend to generate metalic garbage.""",
        1,
    ),
    (
        """Brainpicker Goblins: if you ever encounter a goblin with a jar of pinkish-grey goo, know you're facing a brainpicker. They open the skulls of their enemies and take turns removing small chunks of brain that they collect in jars. Brainpicker goblins seem to be able to actually collect small pieces of knowledge from this practice, and as such their cultures and fighting styles incorporate elements of nearby species', up to and including magic.""",
        1,
    ),
    (
        """Skittles: Skittles, or rainbow goblins, are a strange group of technicolour goblins who seem to have different elemental affinities. A red Skittle may breathe fire and resist heat damage, a blue one may freeze you with its touch, a yellow one might shock you, and so on. Oddly, Skittle colour does not seem to be hereditary at all, and researchers have found no pattern of which Skittles will sire which colour.""",
        1,
    ),
    (
        """Lamp Goblins: Lamp goblins exhibit a form of bio-luminescence, glowing from every part of their body at will. When doing so, they are hot to the touch, and have been known to fight by grappling enemies and overheating them. Though their skins are tough, when eventually pierced, they bleed out their black blood with shocking speed. Lamp goblin blood is sticky and heavy, impeding the progress of anyone who becomes covered in it, and it is also highly flammable. Though both of these features make them dangerous, their blood makes excellent fuel, and they are prized by experienced hunters good at killing from afar.""",
        1,
    ),
    (
        """Goblin Archers: Goblins aren’t known for being the best marksmen but these ones are passable. Their bows are mostly stolen and their arrows are often drenched in poison.""",
        1,
    ),
    (
        """Bugbear Horrors: The bugbears huge size is what gives them an edge in fighting. The Dark Scientists thought of a brilliant way to push this advantage. bugbear Horrors are put in a thick green sludge when born called a growth vat. Once they have spent five years in the ooze they come out as fully grown terrors. Weighing 500-700 pounds and reaching 10-15 feet tall while hunched over the Bugbear Horrors are not to be trifled with. The Bugbear Horrors have a 5 in intelligence and only want to kill. Their massive stature and large goat horns are used to fire poor individuals near it. Bugbear Horrors have awful spines and are always hunched over with two fists in the ground to help them walk.""",
        1,
    ),
    (
        """Claw Masters: A group of goblinoid monks that practice an art known as the way of the beast. While the occasional hobgoblin and bugbear are apart of the monastery it’s mostly goblins. These monks will use their claws, teeth, and speed to wreak havoc on their foes. Some tape knives to their hands so their clawing is even more effective. One Claw Master Grandleader is capable of incapacitating 10 guards at once with their bare hands.""",
        1,
    ),
    (
        """Hunters of Men: This elite rank of goblinkin are Archers that have proved themselves worthy of the title Hunter of Men. Hunters of Men have a special poison only they know to make called hunters specialty. On Hunter of Men can shoot a squirrel from 300 feet away.""",
        1,
    ),
    (
        """Rot Grub Slingadiers: The Roy grubs are a parasite known for eating their victims alive and chewing their heart to ribbons. Rot Grub Slingadiers are a group of goblins that take these pests, put them in vials and potion bottles, and uses a sling to launch them into enemies. Rot Grub Slingadiers life is short. They typically live a year at most while handling these bugs.""",
        1,
    ),
    (
        """Insane Hoppers: The dark lab made a group of goblins that can jump up to 10-25 ft they are used to jump and invade walls and open doors for others the strong goblins can jump up to 40ft. The Insane Hoppers project is now discontinued since the Insane Hoppers have an unfortunate side effect of having their knees explode randomly.""",
        1,
    ),
    (
        """Armored Guard: The Armored Guard are artificers that specialize in armors and shields. The Armored Guards wear large suits making them 8 feet tall with fists the size of a dwarves head. Their helmet resembles a jester mask and they emit the sound of cranking gears everywhere they walk. Armored Guards are slow but their fists are capable of crushing skulls and the sound their armor makes is deafening.""",
        1,
    ),
    (
        """Armored Infiltrators: The armored infiltrators work with the Armored Guard as artificers except the Infiltrators concern is with disruption. Armored Infiltrators have a suit with two long and fast legs connected to their metal arms. Armored infiltrators also have a Tesla cool on their back which they call the lightning bolter. Lightning bolters shoot green lightning which is poisonous, how they manage to make lightning poisonous is a secret they will never tell. Infiltrators lie in wait for an army to ambush. Their speed and weaponry makes it so nobody escapes to tell tales of them.""",
        1,
    ),
    (
        """Fiendborn: Few can match the cunning and ferocity of The Fiendborn. Hobgoblins believed to have the blood of the hells themselves, The Fiendborn conjure demons and devils from thin air and cast spells of firey doom. Fiendborn are merciless just like the creatures they summon for their bidding.""",
        1,
    ),
    (
        """Children of Druk: goblins are naturally bred to seek power. Even in the face of danger power is a great motivator for goblinkin. Some goblins make the treacherous journey to The Jagged Peaks in order to meet Druk the lich for the opportunity to serve hm. Most are killed by Druk and turned into undead but some are welcomed to drink wine in his study. After an interview Druk will decide if you’re worthy of a fraction of his gifts. If he is generous a pact will be sighted in blood for their soul when killed. Those who sign get powerful spells and a choice between a magical weapon or an ancient tome as a gift for their service. Children of Druk are feared even by hobgoblins for nobody crosses an angry warlock of the dead.""",
        1,
    ),
    (
        """War Chariots: Poorly made and efficient to use, The War Chariots are made of cheap wood and glue. Pushed by worgs and operated by Worg Riders, War Chariots are designed to trample enemies with their spiked wheels and defend the driver with wooden walls.""",
        1,
    ),
    (
        """Goblinoid Pirate Salty Souls: The Salty Souls are sorcerers born to sail the seas. Salty Souls are uncommon but are seen as a blessing from the gods. Salty Souls tend to start spellcasting at six and have a pull towards the sea. Goblins see The Salty Souls as valuable soldiers who can fight for superiority of the oceans.""",
        1,
    ),
    (
        """The Red Hosts: This ancient sect of goblins go through a magical ritual upon entering adulthood that implants a sentient and parasitic mote of blood magic in their brain. When under the blood parasite's control, these goblins are a fearless and vicious fighting force that will even turn upon their own if they run out of enemy blood to spill.""",
        1,
    ),
    (
        """Corpse Wagons: Goblins Bree’s like rats, what’s a few casualties when they can be replenished in a day? Goblinoid culture has little value for life and The Corpse Wagons show this. When a fight is won goblins pick up the dead that the necromancers and Vermin Swarmers don’t want and put them in The Corpse Wagon, a coal powered wagon that can carry hundreds of bodies. These bodies can be used for a number of purposes including: more bodies for necromancers, burning them to leave a smell that hangs over the air to disgust enemies, use them as catapult ammunition, burn them to escape in black smoke, attract more rats for The Vermin Swarmers, etc.""",
        1,
    ),
    (
        """Farmers Bane: Goblins need food like every other creature, unfortunately goblin farmers are near nonexistent. The Farmers Bane play an important part of goblin society. Farmers Bane goblins steal food from other nations and give to the goblinoids. Farmers may try to defend their land but for every Farmers Bane goblin there’s 20 more.""",
        1,
    ),
    (
        """The Many Armed Ones: The Many Armed Ones are self explanatory. They are goblins with at least 4-5 arms. The Dark Scientists thought it would be a good idea to graft more arms on a goblin. Many Armed Ones use four shortswords most of the time but they’ll pick up anything usable. They don’t have the best control over each arm.""",
        1,
    ),
    (
        """Brain Shields: While hearing word of a mind flayer cult nearby The Dark Scientists got to work on a super goblin that was immune to psychic attacks, they technically succeeded. Brain Shields have a 0 in intelligence and wisdom along with being immune to psychic damage. Even while in a vegetative state Brain Shields have a strange trait making them very valuable. All psychic attacks and attempts to read minds are drawn to Brain Shields like a magnet. Goblin soldiers will be seen with a few Brain Shields making any goblin in a 10 foot radius next to a Brain Shield immune to psychic damage as it is all transferred into the Brain Shields empty mind.""",
        1,
    ),
    (
        """Mutators: A small sect of hobgoblins that live and die by polymorph. Mutators will find large monsters and generals to turn into worms for their own enjoyment. mutators often help The Engineers and Dark Scientists by capturing large beasts and containing them in a jar as a bug for an hour.""",
        1,
    ),
    (
        """Swamp Lurkers: The Swamp Lurkers are a disease ridden folk that live in the Blight Swamps. A sick and twisted people that hide in the water and fog to ambush tortles and other creatures to cook and eat. The Swamp smells like sulfur and barbecue.""",
        1,
    ),
    (
        """Beastbears: These bugbears have minotaur DNA. Dark Scientists had trouble getting a minotaur but once they got it they used it to the fullest. Beastbears are recognizable by their large bull horns and their short temper.""",
        1,
    ),
    (
        """Night Flyers: These goblins have found the secrets of the night and can sprout wings when the moon is out. Night Flyers are a druidic organization that creates spikes on the ground and drop explosives from above to kill ground dwellers. The few that use crossbows are excellent marksmen. Night Flyers are very tight-lipped and wear skull masks painted black to hide their faces. A Night Flyer would rather die than share their ancient knowledge. Nobody knows where they go to preform rituals but anyone who is seen prying in their business is made a sacrifice to the moon gods. Are they vampires, ghosts, demons? The question remains unanswered.""",
        1,
    ),
    (
        """Wasp Nests: The Engineers did a fine job with this piece of artillery. The Wasp Nest is a large wooden cube on wheels with a door to open it when ready to fire. the Wasp Nests ammunition is a hundred arrows with rockets attached to them. The Wasp Nests occasionally kill goblin soldiers but that’s a small price for an armies forces being crippled by hundreds of rocket powered arrows.""",
        1,
    ),
    (
        """Shriekers: A very rare form of artillery that was inspired by a design the goblins found in the nine hells. A shrieked is made by having a dead body, some steel, and a hint of necromancy. Shriekers have a crank that when spun causes the machine to yell a horrifying sound that does both eardrum and psychological scarring. Operators of Shriekers can swear they hear it speak to them. It wants something. A dark deed but what the deed is can’t be deciphered.""",
        1,
    ),
    (
        """Frost Goblins: These Ice blue goblins have been in the cold regions up north for generations. Magic and evolution has given them the ability to survive I cold climates with their bugbear allies.""",
        1,
    ),
    (
        """Goblin War Shamans: War Shamans share different view, values, and beliefs but the one thing that they all agree on is that Wars should be fought and that healing the weak is necessary. Goblin War Shamans are considered heroes in many tribes for what they do.""",
        1,
    ),
    (
        """Witches: Goblins have only recently found witchcraft and love the idea of making things ugly. Lots of hags see a piece of themselves in goblins and offer their help in the new aspiring witches.""",
        1,
    ),
    (
        """Vulture Rangers: A rank of bugbear hunters that specialize in tracking down fleeing enemies and killing them. Vulture Rangers wear bird skull necklaces and have longbows made of bones. It is said a Vulture Ranger can smell their prey from five miles away. Those who escape from The Vulture Rangers are rare but mistakes can be made. This doesn’t stop The Vulture Rangers from tracking down prey for their entire lives.""",
        1,
    ),
    (
        """The Spiderbacks: While most goblin cavalry rides worgs there are rare few who ride a more exotic creature. The Spiderbacks are underdark dwellers who ride giant spiders. The Spiderbacks learned how to ride the venomous beasts through the drow which they keep in high regard. The Spiderbacks don’t leave the underdark cave systems much. They prefer to lie in wait for an ambush on unsuspecting prey but they can also be found in forests and swamps.""",
        1,
    ),
    (
        """Spiderback Generals: Most Spiderback Generals are hobgoblins though goblins can also attain the coveted title. Spiderback Generals have special armor given to their spider to show their rank. The armor is made of red leather and Spiderback Generals only feed the finest meat to their spiders.""",
        1,
    ),
    (
        """Dark Pressure Sorcerers: Calling These hobgoblin scholars sorcerers is misleading as they have studied hard to learn the secrets of Graviturgy. Dark Pressure Sorcerers gained this knowledge through trail and error with a lot of error to the dismay of the goblinkin. Even now their magics are not perfected leading to catastrophic consequences. Dark Pressure Sorcerers are deployed when flying enemies need to be grounded or when Dark Scientists need their abilities.""",
        1,
    ),
    (
        """Dark Pressure Bugbears: These bugbears are kidnapped in the dead of night to be the latest lab rats in a new experiment. Dark Pressure Bugbears are put in chambers that have increased gravity from the magic of Dark Pressure Sorcerers. Dark Pressure Bugbears don’t see another creature outside of masked goblins until they’re sixteen. The harsh gravity and lack of love and attention leaves The Dark Pressure Bugbears into Incredibly muscular super soldiers with no compassion and a desire to kill.""",
        1,
    ),
    (
        """Krakenborn: After a hard fought battle at sea between a kraken and Captain Jennifer Holmes, the goblinoids like always, were victorious. Captain Jennifer Holmes took a few tentacles as a trophy with King Meatsak paying her handsomely for them. A true goblin never turns down a large sack of gold and thus King Meatsak was the proud owner of kraken tentacles. The moment he got them he threw them in The Dark Lab and told the scientists to figure out something with this. With some unethical experiments here and some biomancy there the krakenborn were made. Krakenborn are half goblin and half kraken, they stand, 6 feet tall with eight arms, a resilience against cold and lightning, and an unquenchable thirst to destroy. many krakenborn feel awful about their lust for destruction but their naturally drawn to it. Most are wizards and druids.""",
        1,
    ),
    (
        """Cavalkillers: The Cavalkillers specialize in killing cavalrymen. They use their strong grip or pickaxes to grasp onto horses, elks or whatever a creature may be riding and use their own weight to slow the mount down to a stop. Once the rider is killed the mount is usually eaten alive.""",
        1,
    ),
    (
        """Shielded Sworders: A very simple rank but a highly respected one. Shielded Sworders use swords and shields, the quality of each can vary. some Shielded Sworders would magical Shields with dwarf crafted flame tongue shortswords with others world a rusty longsword and a plank of wood. Shielded Sworders are front line infantry that fight with what they can muster.""",
        1,
    ),
    (
        """Sewer Nightmares: The Dark Scientists has made a scheme to create a biological weapon but the end result was a mess of goblin limbs and screaming mouths. The failed experiment was incinerated and threw into the humans sewer system and that was the end of it... or so they thought. The creature grew and adapted, feeding off of rats and alligators. Many humans have beef blinked in the sewers and sighting of a huge blob of green flesh that runs incredibly swiftly with its many legs, arms and bones devouring people with its three mouths and hacking up victims with its mandibles are becoming increasingly more common. The humans fear whatever this monstrosity is has found a way to multiply.""",
        1,
    ),
    (
        """Dark Eliminators: These bugbears work in The Dark Laboratory and wear a black suit that covers their entire body. The Dark Eliminators task is to keep experiments contained and kill ones who are needed to be eliminated. the Dark Eliminators are equipped with aces and some with spellcasting tomes to ignite experiments gone wrong. Each make an oath to do their job as dutifully as possible. Most of The Dark Eliminators are warlocks but even they don’t know what patron they serve.""",
        1,
    ),
    (
        """Wardens: Goblin society runs on two things, greed and slave labor, hobgoblin Wardens ensure the slave labor is done. Armed with whips and morningstars, Wardens oversee the slaves to keep them working hard. Wardens are brutal and cruel individuals and each slave has their own story of a Warden setting an example to the slaves. Wardens wear scalemail armor and ensure it’s always in perfect condition. Wardens are the embodiment of pride and cruelty. Dwarves see killing one as a great favor to the clan.""",
        1,
    ),
]


def main():
    print(roll(table_gobling_unit))


if __name__ == "__main__":
    main()
