from roll import roll


# Source: http://dndspeak.com/2017/12/21/100-secret-societies/
table = [
    (
        "The Figulari, they disguise their actions in public as the Potter’s Guild. In truth they construct enchanted clay traps that capture the souls of their political opponents. Their members are referred to as “Clayed Men”.",
        1,
    ),
    (
        "Magitologists; a large well known cult in certain parts of the world. Started by psychic writer L Rob Hupyard, they are a vastly rich organization rich enough not to be hunted down by the authorites in the cities they reside in. They have many famous people among their ranks. Rumors are that they horribly torture and brainwash those who try to leave.",
        1,
    ),
    (
        "The Guild of Undertakers and Gravediggers has a secret: the town was built on the site where an evil, nameless god was slain millenia ago and anyone buried there will arise as undead in three days. They have a ritual they perform out of sight of the deceased’s loved ones that prevents this, but a necromancer has infiltrated their ranks and has figured out how to reverse it. Unless stopped, the whole area will be awash in undead.",
        1,
    ),
    (
        "Lizard people who secretly control large sections of the government. They are actually lizardfolk, with numerous members dedicated to the creation of hats of disguise to further infiltrate.",
        1,
    ),
    (
        "Magic users pretending to be an anti-magic organization for two reasons: the ability to discreetly cape and stop real anti-magic supporters, and so that they can use terrible arguments in politics to reduce resistance to magic-positive rulers and legislation.",
        1,
    ),
    (
        "A cult that worships inactive spheres, with prophecies saying that someday the spheres will activate, and Grant them limitless power (spheres are inactive Mythallar, waiting for DAM plot point)",
        1,
    ),
    (
        "Pixies intent on researching and recovering permanency spells, intent on permanently shrinking the other races to a more proper size (with a smaller subsection planning to grow, themselves, and subjugate both other pixies and newly-Tiny races)",
        1,
    ),
    (
        "Ancient cult of half-dragons, dragon born, and kobolds, worshipping an ancient, True-Polymorphed wizard, who will refuse to believe their dragon isn’t real.",
        1,
    ),
    (
        "Necromancers whose only goal is to live in peace, using undead to do manual labor and creating a hidden City where all live rich, happy lives. A necromancer controlling some farming zombies dies of old age, leaving some zombies free from control, and those zombies attack a nearby, surprised village. Adventurers are brought in, offered lots of gold to defeat “the Neverland behind all of this”.",
        1,
    ),
    (
        "A hidden underground elf City, not drow, just wood elves who would prefer to be left alone. They mostly hunt but they also sell beautiful bone and wood carvings in nearby towns. Their City was once a valley, but, using their druid and ranger members, they had trees grow over the top. Now noon is as twilight, and twilight is as night.",
        1,
    ),
    (
        "A society of gnomes dedicated to gnome rights. They believe (correctly or incorrectly) gnome rights are being trampled on and intend to right this wrong from the inside. Using trenchcoats and disguise kits, sets of three gnomes disguise themselves as humans and try to gain political power to force all businesses and public places to lower counters, tables, chairs, and shelves to a height appropriate for “all sentient and decent folk”.",
        1,
    ),
    (
        "A secret cabal of merchants that rig the price of a particular raw material in the surrounding towns. When competition arises, they have bandits attack the rival caravans while faking attacks on their own. If the PCs get too close to the truth they’ll be hired as caravan guards during their investigation, only to be attacked by bandits and all the members of the caravan during an ambush.",
        1,
    ),
    (
        "A cult of humans that believe elves are favored by the gods due to their grace and longevity. To fool the gods, their priests wear masks and gloves made from the skin of elves and pray to Elven gods for long life. They will kidnap and starve elves and half elves so their skin become looser and easier to remove after they’re killed.",
        1,
    ),
    (
        "A small cult of commoners who believe that magic isn’t real, and is a series of mechanical tricks performed by incredibly well disguised constructs.",
        1,
    ),
    (
        "A group of pale, starved elves who travel the globe kidnapping humanoids and feeding them to a dark beast, in an attempt to increase it’s power enough to level cities.",
        1,
    ),
    (
        "Every person in town talks in a whisper, because they believe they are living in the ear of their god, and they don’t wanna wake him.",
        1,
    ),
    (
        "The UnderTown, a town ruled by dwarves that connects to other towns, they can always be found beneath the city, ready to accept another dwarf into their ranks to help him/her out. Enjoys causing earthquake-like collapses of relatively important structures in small towns and has a fromidable army to destroy nations underfoot (literally under).",
        1,
    ),
    (
        "The Silver Adders – A group of rebellious teenagers from noble families that have taught themselves the art of poison and assassination. They’ve honed their skills with thrill kills of random merchants and peasants, leaving behind a silver broach as a calling card. They now seek more challenging prey, specifically adventurers like the PCs.",
        1,
    ),
    (
        "A town full of people living on the top of a cliff who throw offerings off the cliff to their god, mostly harming the people passing down under the cliff.",
        1,
    ),
    (
        "The Clean Slate – Those who study history are doomed to repeat the same mistakes and stagnate. The Clean Slate does its best to destroy the chains of precedence and history so people can try new things. The more novel ideas realized the better chance of founding a perfect society. Once that is done all other history would be useless anyway.",
        1,
    ),
    (
        "The True Royals – They have a child who is supposedly the heir to a kingdom long since destroyed. They need to find other people first willing to follow them and then willing to reform the kingdom. The problem is somebody in the past did their best to erase all mention of the kingdom so nobody remembers or cares. The True Royals sponsor missions to rediscover this ancient civilization. If it was a good or evil place remains a mystery.",
        1,
    ),
    (
        "The Needle Conglomerate – The world is flat and they know it. What they keep secret is ancient writi vs that state there is a world of riches and gems on the underside if this one. They work to dig deep at the thinnest parts of the world to get through to this land. Their luck isn’t to good cause they keep hitting ancient dungeons or lakes of fire that burst out onto the surface.",
        1,
    ),
    (
        "The Friends in the Dark: a shadowy secret network of informers and rumor-mongers whose purposes and goals are unknown, even to many members. Actually, the secret police/intelligence agency of a collapsed and forgotten kingdom that still goes through the motions even though they have nothing left to protect/answer to.",
        1,
    ),
    (
        "The Order of the Spellbreakers: An order of paladins who believe that only the gods may use magic (or grant it to their followers), and all other magic is heresy. They seek to eradicate magic from the world, starting with villainous characters such as liches and making their way toward the more innocent local enchanter or wandering Druid.",
        1,
    ),
    (
        "The Hidden Fangs – A group of vampires who disguise themselves as vampire hunters, allowing them to visit towns which have vampire problems and feast on the citizens without being detected easily.",
        1,
    ),
    (
        "The Helping Hand – this group of helpful clerics and healers secretly believe that doomsday is right around the corner and is helping it along, for their perceived prize in the afterlife",
        1,
    ),
    (
        "The Leathercrafter’s Union – to normal society a normal gathering of Latherworkers, like any other trade guild, but secretly they plan and execute attacks on smiths – particularly armorsmiths, that they feel are making them obsolete.",
        1,
    ),
    (
        "The Divine Crown – this cult believes that the mightiest kings and Lords aren’t just blessed by the gods, but instead that they are the reincarnation of the gods. How the royalty they worship reacts to worship varies among ruler to ruler, but most royalty do begin to be annoyed when the cult makes unauthorized assassinations on their enemies – which they almost always do.",
        1,
    ),
    (
        "The Undergrounders: These humans became fascinated by the dwarves and built their own small society emulating dwarven tradition’s and customs. The dwarves who meet this society can’t seem to agree whether or not this is a mockery or humans finally coming to their senses. There are similar societies fascinated by gnomes, halflings and elves, with elves being the most offended at this odd display. There also were a small society dedicated to emulating orcs, but these societies are usually killed when they meet actual orc tribes.",
        1,
    ),
    (
        "The shadows. A group headed by an unknown man that contacts mercenaries and potential members through mysterious envelopes that appear out of seemingly nowhere. They have an intricate network of common folk that allows them to stay up to date with affairs all over the city.",
        1,
    ),
    (
        "The Golden Cradle – A group of hereditary nobles that were secretly adopted into their families when their parents were unable to conceive children. They secretly fund numerous orphanages and sponsor orphans as apprentices to various guilds. Given that all their wealth and power is built upon their falsified bloodlines, though, they will stop at nothing to preserve their secrets. They may feel terrible about their actions, but they justify it as the only way to protect their good works.",
        1,
    ),
    (
        "The Risen: A group of people who have been resurrected and believe themselves to be chosen amongst the masses. They seek to further their agenda of purifying non-believers.",
        1,
    ),
    (
        "The Moundeliers:. A goup of halflings, gnome, druid and firbolg who seek to prevent the expansion of villages into the woodland area.",
        1,
    ),
    (
        "Gold Bloods:. They are a group of people who have seen the destruction of the world fortold by celestials. They believe Orcs and worshippers of grumsh are the bringers of the end time and seek to eradicate them.",
        1,
    ),
    (
        "The Grave Barons: Teifling nobles who became Teifling once partaking in a ritual for Asmodius for greater power. They have spread throughout the land slowly corrupting nobles.",
        1,
    ),
    (
        "The Umbraconti: An (figuratively and sometimes literally) underground school of wizards and artificers who research taboo magic. Their actions are normally not overtly malicious but it has been said that Umbraconti wizards have killed entire cities in pursuit of arcane knowledge.",
        1,
    ),
    (
        "The High-hats: A guild of minstrels and fools whose entire purpose is to infiltrate the celebrations and courts of royalty and, using their enchanted bardic music and foolery, influence the royals for the betterment of the guild.",
        1,
    ),
    (
        "Reachers: A society of Gnomes who worship a human con-man who claims to be a gnome that found the cure for shortness. He gives them “magic growth tonics” (water) in exchange for valuables they steal from passing travelers.",
        1,
    ),
    (
        "The Spore: A group of Druids who have found that a dangerously addictive mushroom can only be grown on the dead bodies of Firbolgs. As such, the group has taken to hunting down Firbolgs and killing them to further their addictions.",
        1,
    ),
    (
        "The Brine: A society of fisherman and dock workers who smuggle the dead from Tartarus by means of the River Styx without arousing suspicion from Kharon, the Ferryman of Hades.",
        1,
    ),
    (
        "A group of priests, nuns, monks, paladins, etc., who run a society dedicated to the welfare of orphans and foundlings. They run orphanages but specialize in placing babies and very young (preverbal) children with families who cannot conceive. They are militant in their charity, but no matter how hard the PCs look, there is absolutely nothing creepy about them. A statistically improbable number of the children gain wild magic sorcerous powers once they hit puberty, though this is kept mostly secret.",
        1,
    ),
    (
        "Loyal Order of the Water Buffalo: The Grand Exalted Imperial PooBah welcomes you to join this brotherhood focused on the manlier aspects of life: hunting, fishing, drinking, BBQs, more drinking, etc. Be recommended by a member and bring your first dues installment to your local chapter; Lodge 26.",
        1,
    ),
    (
        "The Fellowship of Whispers, a religious chapter of paladins, clerics and assassins dedicated to rooting out politicians, noblemen & all other influential members of society that have been corrupted by demonic influence. Their name comes from the quietly whispered prayer associated with their more unsavoury activities. Or perhaps from the fact that their existence is only known through whispers in dark places. Or…",
        1,
    ),
    (
        "The Bloody Brothers & The Sanguine Sisterhood, twin societies founded by two ancient vampires who tired of the hunt and instead compete to control civilisation(s)- keeping score with one another. Their leadership is split on gender lines, but thralls exists in all forms. Many wars and disasters have been caused by one trying to torpedo the other.",
        1,
    ),
    (
        "The Order of the Mask, a group of revolutionaries and enlightened thinkers who believe that a republic is the only way forward for society. They idolise a Masked Jester, whose name is lost in history, who assassinated the last of the great kings of the kingdom and caused a century of strife. The Jester would likely be bemused if he was brought back, he killed the king because it was fun.",
        1,
    ),
    (
        "The Preservers, a society that collects knowledge on all things and store it in their hidden library. Their leadership are members of a long forgotten and ill-fated civilisation, related to the Lizardfolk and Yuan-ti. Some claim the library exists on it’s own plane and is accessible only through the realm of dreams through years of training in traversing the planes or by following a guide that knows the way.",
        1,
    ),
    (
        "The Wilhallow Society for Scientific Endeavor: a group of wizards, alchemists, necromancers and scientists performing countless experiments on the unknowing denizens of the small town of Wilhallow over the course of the last 60 years. By now, the majority of Wilhallow’s residents are barely human, having been replaced bit-by-bit with zombified flesh, goblin and orc limbs, or advanced mechanical prosthetics. Fortunately, they’ve all been magically disguised to not notice this, and the fact that none of them seem to age anymore hasn’t particularly bothered the citizens of Wilhallow.",
        1,
    ),
    (
        "The Devil’s Circle: A high-stakes gambling ring overseen by a minor Baron of Hell, Zycobulz. The Circle’s patrons include kings and wizards, Fay lords and Drow matriarchs. The bets are on the outcome of wars, the survival of empires, and can take decades to play out. The rewards are souls, titles, favors and magic trinkets, and Zycobulz ensures that the house always walks away a bit richer.",
        1,
    ),
    (
        "The Redstreet Genuine Gentlemen’s Club: a dizzyingly complex and far-reaching information network set up by a long-deceased master detective, the Redstreet Club can get dirt on anyone and anything, and has years-long casefiles on interesting individuals locked away in the Club’s record books. The Club’s members are detectives, city guardsmen, street urchins and thieves, each one pulling from a pool of resources to fund their own investigations and to hand out information to interested buyers.",
        1,
    ),
    (
        "Six Sky Triad: a Thri-Kreen society hidden in a small desert town. Triad activities are mostly benign, with the Thri-Kreen secretly discussing town matters and fulfilling ancient cultural rites that have been suppressed by the local government. Every Thri-Kreen citizen of the town is either a Triad member or at least knows of it, and they keep their society hidden through telepathic communication, their nighttime meetings occurring in total silence. Occasionally the Triad will journey out into the desert for a night, singing desert songs and praising the Sand Father, but these journeys are rare, and getting rarer as time goes by.",
        1,
    ),
    (
        "The Monks of the Eclectic Feline: An order of monks who’s origin is shrouded in mystery, but who operate based on the whims and wishes of an “Immortal Tabaxi Warrior” which, if investigated, turns out to be a house-cat familiar with a catnip addiction. Where’s the house-cat’s mage?",
        1,
    ),
    (
        "The Delumminati: a group of blind Drow that believe the entire world should be cursed with the darkness they suffer themselves. They extinguish any source of light they find, kill magic users that produce light effects, and eventually hope to kill the sun.",
        1,
    ),
    (
        "Death liberators; This underground group of Necromancers work to remove the stigma of Necromancy and get it legalised.",
        1,
    ),
    (
        "The Faithless; a group that dont recognise the divinity of the gods, and seek to end organized religion. They “achieve” this by sabotaging places of worship, usually disguised to look like an attack by another religion. When confronted they will usually respond with a variation of: “If the gods are so powerful, why didn’t they prevent it?”",
        1,
    ),
    (
        "Mary Mage’s Managerie: This traveling band hides their criminal activity by also performing as a travelling circus. Unlike many other circuses Mary’s main attractions are extraordinary magic displays and training of magical animals",
        1,
    ),
    (
        "Sorcery: The Collective; this widespread hobby is particularly popular amongst young men, but they play in secret clubs due to watchdog groups that claim that the players are tempted by the infernal by participating.",
        1,
    ),
    (
        "The Vanishing Act: A network of entertainers and performers that spans the globe. The Act is centered around the “liberating” of valuable goods and information, which are then traded around the network for a price. Becoming a member is difficult due to the organization granting membership by invitation only. In addition, one who wishes to join must not only prove themselves to be uniquely talented in their chosen art, but equally skillful in the retrieval of valuable goods, in whatever forms those goods come. Members are given a subtle yet distinctive tattoo and a musical excerpt to memorize, which allows them to identify other members. “Studios” can be found in various cities (typically hidden in very expensive clubs or brothels), and many Actors find themselves frequenting such locations. Those who wish to trade their valuables can sniff out the areas and seek admittance by presenting their tattoo and music, upon which they will be free to go about their business.",
        1,
    ),
    (
        "The Gutter’s Court: Once upon a time, all the highborn lords and ladies of the land agreed that they could not be bothered dealing with all the troubles presented by the everyday peasant. To remedy this issue, they created the Gutter’s Court, a seperate, less powerful court then their own, composed of remarkable peasants that have demonstrated an above average level of loyalty to their respective feudal leader. These peasants are recruited by their feudal lords to handle menial administrative duties as well as provide an additional layer of contact between the nobility and the commoners. The Court is also a tool used for a less innocent purpose. Due to the chosen peasants being the lowborn representatives of their lords, any issues that the lords have with one another are typically resolved through violent retaliation directed towards their proxy. Chosen peasants often make their own plots to seize power in the Gutter’s Court, and exceptionally prominent ones may even be taken into their lords house.",
        1,
    ),
    (
        "The White Eldritches: Lots are born to control, few are born free. Acting in the darkness, this mind flayers are born with the gift of the free will. Able to hear the Elder brain orders, but free to choose what to do, they want Illithid people to be free from the hive brain control. Excep for their terroristic actions against the elder brain they’re quite the good guys (Chaotic Good/Neutral).",
        1,
    ),
    (
        "The Baker’s guild: a regular guild to a passerby, is in fact a mafia organisation. Money laundering, exerting social pressure by under or overdelivery, smuggling in flour, etc..",
        1,
    ),
    (
        "The Terrorizing Tinkers: A clandestine collection of Gnomes who are popularizing the use of machinery over magic to better life and solve problems through evil means.",
        1,
    ),
    (
        "The Oldguard: A band of mercenaries that the government pays to keep the peace. Secretly they work towards a revolution, trying to bring back the “old ways”.",
        1,
    ),
    (
        "The cult of the UnBroken god: A group/cult that believes if a god can be killed/maimed/broken they are not worthy of worship. Because of this belief they are trying to destroy all the gods, to find out if there are any gods left worthy of worship.",
        1,
    ),
    (
        "DAD – Dwarves Against Drinking. A secret society of dwarves who think that the drunken culture of dwarves is holding them back and once dwarfs stop drinking they will be able to rule the world.",
        1,
    ),
    (
        "A guilds of artists. They do tattoos mostly. Their secret isn’t that evil. They always offer tattoo songbirds to the hands of any travelers for free. They believe that the songbirds let the people get into heaven. And knowing no one would take the offer that way they trick people into getting them saying that the tattoos are a promotional gimmick.",
        1,
    ),
    (
        "A society of rich merchants and hired psychopaths/assassins that all have a taste for death. They lure large groups to their false town with promises such as payment for getting rid of a menace or a safe place to sleep for whatever group may pass by only to hunt them for sport the next night.",
        1,
    ),
    (
        "Mans Best Friend – On the outside, a charitable organization funded by the crown to provide service dogs for disabled citizens. In truth, the dogs are magically enchanted to serve as the eyes and ears of the government.",
        1,
    ),
    (
        "The Brawlers are a group of fighters and monks who use cestus gloves (1d8 damage) as their weapons. This group is unknown by the townsfolk and are usually in the taverns and inns. The brawlers blend in with the townsfolk and aren’t able to be noticed. They have no motives but to fight when provoked. If a fight starts in the inn between the PCs and just 1 brawler, all the Brawlers attack the instigator of the encounter.",
        1,
    ),
    (
        "Mephistopheles: This secret society of Teifling traders all use masks of disguise self to appear identical, and all operate under the name Mephistopheles. They work together to slowly begin to form a monopoly on the trade of magical items in order to drive up the prices.",
        1,
    ),
    (
        "The Srepeek Ooz: A racially diverse order that seeks to preserve all forms of life by storing small populations of all races and species inside enchanted underground zoos. Inside one of these “life vaults” you can find many strange creatures both magical and mundane, some of them exist nowhere else.",
        1,
    ),
    (
        "The Loreguards: A small but powerful group of individuals who make sure no one rediscover the how to create magic items.",
        1,
    ),
    (
        "Cult of the Creation Dragon: these members believe that the world is in fact a the first dragon curled up waiting to wake up, the cult aims to wake the dragon and re create the world as we know it.",
        1,
    ),
    (
        "The Allseeing Eye: A huge network of wizards who use the detect thoughts, sending, and message spells to obtain information and give it to people for the right price. They sometimes secretly give unknowing people information about their rivals to get them to try and fight.",
        1,
    ),
    (
        "A secret all-female cabal of makeup artists that specializes in making dead people look alive. Through their expansive network of powerful individuals they are able to ensure they find out about deaths before anyone else. They offer the most powerful a chance at reanimation if they agree to work under the cabal’ s thumb and they keep them in line by threatening to reveal their secret. Remember that famous bard that you thought had died? Or that kind mayor who you thought was buried under rubble? Turns out it was a “false alarm”.",
        1,
    ),
    (
        "Dark Arts Anonymous: A collective of wizards who peered into the dark arts and wound up changed in some way. Despite many being banned from the “good” institutions of learning, many remain there, surreptitiously researching their hobby and corrupting their souls. They meet on Wednesday nights in a secret cave in the Feywild, and try to support each other in quitting this corrupting influence. To protect they’re anonymity though, they will do anything.",
        1,
    ),
    (
        "The Farmer’s Society: A society that owns a giant farm, and control nearby cities with blackmail using food.",
        1,
    ),
    (
        "The Medusa Cult: A cult of blind cultists who worship a Medusa. They can’t see her, so they don’t get any problems when living with her.",
        1,
    ),
    (
        "You have heard much disturbing gossip about the Iron League of the Cup. Apparently the Unspoiled Presbyter of the Grail is seeking the lost “Tome of Bivariate Energies” to further the Cup’s excavation of a graven burrow past the Wandering Waters. As he gathers information on the Tome, the Presbyter is also distributing “tokens of redemption” that can only be redeemed at the excavation site.",
        1,
    ),
    (
        "The Unalloyed: An organization of Dwarves that seeks to remove all non-Dwarves from Dwarven territory and cut off all trade and travel to and from other races’ territories.",
        1,
    ),
    (
        "The Necrocrats: A cult of powerful necromancers that seek out the worlds best and strongest of rulers to grant them immortality through lichdom, all in a quest to bring law to the world.",
        1,
    ),
    (
        "Order of the Specter, a group of noble men across the kingdom who deal in dark magic to receive visions of future events that could come to pass. The Order uses this knowledge to increase there own individual power and wealth. The magic they use requires that the users sacrifice one of there living family members: Son, Daughter, Father, Mother, etc.. Within the same blood line as them, no step-family or people they have married. Depending on how closely related they are to the sacrifice determines the length of the vision, and its importance to them.",
        1,
    ),
    (
        "Sisterhood of Silence, a highly trained group of criminals that direct the kingdoms court system through secret members and rituals/curses while also helping several criminals avoid the law. This sisterhood is rumored to have several hundred members all of which are female from many different races.",
        1,
    ),
    (
        "Matriarchs of Society: Only women who have become Grandmothers are invited to join. In general they work to make sure their lines continue. Another of their tasks is to find homes for displaced children, adding this child to a Matriarch’s list of grandchildren.",
        1,
    ),
    (
        "The Leftovers club. A secret sect of necromancers gather as many dead bodies as they can, making deals with or stealing from butchers, morgues, hospitals, veterinarians, or local criminal organizations. These “leftovers” are given to two teams, who use a combination of necromatic techniques and surgery to create undead monsters. Once a month, a battle between the monsters is held, and the winning team is greatly rewarded. Once the battle is over, new teams are assigned and the cycle starts again.",
        1,
    ),
    (
        "Barbers guild: with franchises in different towns (usually a rented room in an inn), The locals see travelers go in and come out with shorter hair or clean shave. In actuality, they are a front for information brokers.",
        1,
    ),
    (
        "Thralls of the Crimson God. The Thralls believe that the only thing preventing the universe from destruction is to sate their god’s need for blood: this includes ritual cutting, self-flagellation, and piercing as part of routine practice. The cult centers on human sacrifice, where a victim is drained of all of their blood in a ceremony to appeal to the Crimson God for mercy and protection.",
        1,
    ),
    (
        "The Rosen Order: A group of powerful warriors brought together by their love of flowers. They tend to all the city’s flower gardens, keeping them in tip-top shape. The existence of the order is kept secret; its members fear their reputations as mighty heroes being ruined if they are ever found out.",
        1,
    ),
    (
        "The Fatladin: The secret group of the Paladin of Gras, God of the grease and good food, Avatar of Bacon. Gras has been forgotten, but not by these man, united in the Quest, to find the most greasy and wondrful food, to please their god.",
        1,
    ),
    (
        "The Teachers: The Teachers are a group of benevolent entities dedicated to training heroes to defend the world against evil.",
        1,
    ),
    (
        "The Shadow Empire: The Shadow Empire is a small group of demi-liches who back villains. They are patient, quiet, and totally committed to the conquest of everything.",
        1,
    ),
    (
        "The Stone Brotherhood: This is a dwarven cult dedicated to protecting dwarven craftsmen, and any other artisan they feel is unable to stand up for themselves.",
        1,
    ),
    (
        "The Libra Facta: One of the oldest known cults, Libra Facta has its origins shrouded in the ancient history of the druids. From time immemorial, the druids and their neutral followers have been working quietly to neutralize and balance the powerful forces for law and chaos, good and evil. In Libra Facta, this task took a peculiar but effective form.",
        1,
    ),
    (
        "The Mithril Chain was an order of knights, including cavaliers and fighters of all types. Very little is known of this organization, which boasted only a handful of members worldwide. Members of the Mithril Chain, known as “Links”, often fought better than would be expected based on their known experience and abilities. In addition, some have been reported to display unusual powers, such as flying, creating fire, water, lightning, or light, passing through walls, or being unaffected by weapon attacks. Each wore a highly ornate steel chain around his neck; rarely were they seen together.",
        1,
    ),
    (
        "The Ring of Blood was a band of chaotic assassins pledged to promote terror. Each member assassin performed at least one assassination per week, with at least one each month being notorious (usually a well-known individual or an especially gory slaying).",
        1,
    ),
    (
        "The Brotherhood of Death was a chaotic evil order dedicated to the worship and service of Orcus through the promotion of chaos especially in sadistic orgies and human, demihuman, or humanoid sacrifices. Although open to evil chaotics of any race or class, the inner circle was made up of outstanding adventurer types, and the hierarchy headed by human clerics and demons. Peasants and idle nobles could only be initiates; initiates were not generally aware of the secrets of the society.",
        1,
    ),
    (
        "The Unending Alliance of the Beast: A quasi-Druidic cult that seeks out positions of power over animals; zoos, circuses, vet hospitals, all are used to train and foster a legion of animal servants who will eventually fight for their masters’ glory. When and where that fight will happen, only the Alliance knows.",
        1,
    ),
    (
        "Cult of the Eternal Flame: The followers of the Eternal Flame cult were fascinated by the destructive power of fire in all its manifestations. They aspired to use the power of fire to eradicate the “corruption” of both civilization and nature using volcanic eruptions, forest fires, heat waves, and droughts, in order to herald a new world of ash and cinders ruled by fire alone. In the fire cultists’ doctrine, the world and all its peoples were wicked and malformed, and the only hope was to purify everything, reducing all to smoking cinders.",
        1,
    ),
    (
        "The Choir: Members of the Choir had the ability to influence others through their strange songs.",
        1,
    ),
    (
        "The Silver Hand: A group of Paladins who are devoted to stopping evil, if it should ever appear. The members like to keep their identity secret so no harm comes to their families.",
        1,
    ),
    (
        "Grumlik’s “Secret” Order of Gnome Mischief: A ‘secret’ order of Gnomes who go around and cause mild mischief, such as placing a dead fish in the pillowcase of a noble lord. What is their reasoning? There isn’t one, they are just mean.",
        1,
    ),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {roll(table)}\n")


if __name__ == "__main__":
    main()
