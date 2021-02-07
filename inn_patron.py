from roll import roll


# Source: http://dndspeak.com/2018/04/16/100-inn-patrons/
table = [
    (
        "A mysterious man sits in the corner of the bar wearing temple robes. He looks worried. If asked why, he will tell you that he saw an omen this morning that signifies the end of the world.",
        1,
    ),
    (
        "A popular local bard just got done playing on the stage. He is surrounded by beautiful women and is having the time of his life.",
        1,
    ),
    (
        "A figure sitting in a more shadowy part of the bar. When the players ask about them, they’re given a different name from every person they ask.",
        1,
    ),
    (
        "Contrary Charlie – a patron who, whenever the players state anything, will either instantly take the opposing view to them, deny what’s being said, or claim that the players are misinformed.",
        1,
    ),
    (
        "Hesjing, a kobold bard with a strange-looking lute way too big for him, humming a familiar song while tuning it.",
        1,
    ),
    (
        "Mmmjimmy : a long bearded redneck wizard sitting in the corner and chuckling to himself.",
        1,
    ),
    (
        "Otto the Miserable- a very dour-looking gnome with a sign next to him reading “make me laugh for 10 gp”. He is immune to Tasha’s hideous laughter.",
        1,
    ),
    (
        "A heavily veiled woman in a very low-cut and tight dress makes eyes at men as they walk by; she is in reality the wife of a local noble looking to catch her philandering husband, who unbeknownst to her is involved in something far different than simple adultery…",
        1,
    ),
    (
        "Hoid. A half elf bard who uses a magical flute to animate the smoke from the fireplace to make visuals for his stories. He tells only children stories, fairy tale style that all end in moral lessons (similar to how real life fairy tales do).",
        1,
    ),
    ("Durog: the Half-Orc bard. His singing is notoriously bad.", 1),
    ("Felsa: A female Tabaxi Ice Wizard that serves as a fence for stolen goods.", 1),
    ("Htrog: A Firbolg warrior for hire. Loves mead. He is the last of his clan.", 1),
    (
        "A beastmaster who keeps his pet owlbear with him at all times. Will feed it whatever food he gets from the inn.",
        1,
    ),
    ("A common speaking mimic that wishes to live in human society.", 1),
    (
        "An unknown humanoid who snores extremely loudly at certain times in the night. His door is always locked and has “DO NOT DISTURB” painted on it in black letters.",
        1,
    ),
    (
        "A giant rat that speaks common as well as elven. Will buy pieces of cheese from the party for 2-3 gp per piece.",
        1,
    ),
    (
        "A kenku that offers tips for successful adventures for the price of a small amount of food from the party.",
        1,
    ),
    ("Johnny, the local drunk. Of course he’s here again, and drunk.", 1),
    (
        "A half orc sitting alone at the bar, drinking from his own large personalised tankard, which reads Ughurv.",
        1,
    ),
    (
        "Three Dragonborn haggling with a human male who is trying to persuade them to buy several gold chains at a table in the corner.",
        1,
    ),
    (
        "A halfling bard, standing on the end of the bar, singing an operatic aria that has several of the patrons fighting back tears.",
        1,
    ),
    (
        "An elderly Tabaxi, seated on a threadbare armchair before the fireplace, seemingly lost in a personal reverie.",
        1,
    ),
    (
        "Two young giggling high elf women sipping red wine, seated at a table, guarded by three bored looking local Lords guardsmen.",
        1,
    ),
    (
        "A member of the town council sits at the bar. Other patrons keep trying to bring up council business, but the councilman just wants to have some food and a drink in peace.",
        1,
    ),
    (
        "A limping old woman with a cane, called “Grandma Maggie” by everyone. Nobody knows whose grandmother she actually is, they’ve always called her that. She doesn’t hesitate to give out spankings for bad behavior, but she has to brace herself since she’s not as stable as she used to be.",
        1,
    ),
    (
        "A constantly-drunk young man with a fancy sword, who was supposed to be a particular “Hero of Prophecy”, except that someone else took care of that problem first.",
        1,
    ),
    (
        "A woman in leather armor with a scar across her face. She quietly drinks from a flagon of ale on the far end of the bar. An especially large sword rests on the floor next to her travel sack.",
        1,
    ),
    (
        "A duck sits at the bar with a flagon of ale and a bowl of stale bread crumbs in front of it. When the inn keep notices you looking quizzically at the duck he says “that’s philbert, Inn security, so watch your P’s and Q’s or he’ll be given ya what’s for!” Philbert looks at you dead in the eyes and lets out a mighty quack with a +10 to intimidate.",
        1,
    ),
    (
        "A tall, portly man who smells strongly of garlic sits to one side of the bar; he is very interested in any conversations about undead. If engaged in conversation, he introduces himself as Marit Clovenhill, a garlic merchant and part-time vampire hunter.",
        1,
    ),
    (
        "A large fat woman sits on a specially made wooden chair by the fire pit. She is covered head to toe in tattoos.",
        1,
    ),
    (
        "A dwarf fighter (e.g. Orik). He is best friend with the human barkeeper (e.g. Castor). They chat very loud. Whenever they start a sentence they say the name of the person they talk to first (or end the sentence with it). When they don’t know the name they use stranger or friend. Apparently the dwarf never gets drunk.",
        1,
    ),
    (
        "A cursed witch. She was transformed into a cat. Still able to talk and to use magic. Comes by everyday for her milk served in a golden bowl with her name on it.",
        1,
    ),
    (
        "A wiry, elderly man sits at the bar talking to the barkeep. He’s asking what needs cleaned or doing as he is taking the next shift soon.",
        1,
    ),
    (
        "A young, attractive couple who are looking for a 3rd person to take up to their room to have some bedroom fun.",
        1,
    ),
    (
        "A man who drank far too much and vomited all over himself. The barkeep is trying to get him to leave but he has passed out.",
        1,
    ),
    (
        "A cigar smoking old woman who asks for her food extra cooked. She refuses any meal that isn’t blackened and burnt completely.",
        1,
    ),
    ("A doll maker who is always tinkering with his creepy dolls.", 1),
    (
        "Two old married men, trying to get away from their nagging wives by coming to the inn and playing checkers.",
        1,
    ),
    (
        "A beautiful young woman in a slightly worn-out green dress. She is not interested in any of the men who have approached her, but she seems to have been watching the inn waitress with a coy smile.",
        1,
    ),
    (
        "A fat noble lady who complains loudly but drinks heavily and soon is undressing herself while singing.",
        1,
    ),
    (
        "A pair of twin halflings stand on a bench playing the piano in the corner together.",
        1,
    ),
    (
        "A medium height figure stumbles into the pub while wearing a long green cloak. It’s actually two halflings one on the others shoulders.",
        1,
    ),
    (
        "A large silent figure walking into the inn. On her back is a wicker basket filled with rusted weapons that give off a strong magical aura.",
        1,
    ),
    ("Two dwarves arguing over who has the more luscious beard.", 1),
    ("A traveling perfume salesman.", 1),
    (
        "Fat John. Sits in the same corner at the same table. Has been there for years. Never seems to not be there. But somehow he knows everybody and everything going on in town. Secretly he’s a divination sorcerer with subtle spells that allow him to scry on anyone within a few mile radius.",
        1,
    ),
    (
        "An elderly paladin is deep in thought in the back of the tavern. If asked, he feels he is too old to stop a Lich that he has been chasing for years.",
        1,
    ),
    (
        "5 whatever race or sex you walk into the bar. They are bedecked in flashy garb (that doesn’t quite fit right, armor and gear. One of them is boasting about there great deeds. It starts to sound more and more outlandish if someone actually decides to listen. In reality they are highway bandit’s that just ambushed and looted actual adventurers. They can find the bodies about 4 miles along the road out of the town, buried in very shallow graves.",
        1,
    ),
    (
        "A young man in the clothing of a lesser noble, quite visibly drunk, is being dragged out of the inn by a woman in similar garb, presumably his wife.",
        1,
    ),
    (
        "A halfling dances on a table, slips and falls under it. Some patrons who had been observing the performance gasp when the little man is not under the table, but his sudden and triumphant ‘Ta-Dah’ from the other side of the room merits some applause.",
        1,
    ),
    (
        "Two burly looking men, their uniforms identifying them as local guardsmen, chug from large tankards of the local brew. The winner falls over backwards off his stool, prompting raucous laughter from those around him.",
        1,
    ),
    (
        "An elvish woman in clothes much too exquisite for an establishment of this sort sits alone at her table, sipping from a glass of wine with haughty countenance and incessantly playing with a pendant hanging from her neck.",
        1,
    ),
    (
        "An aged priest with a week’s beard and patched robes staring mournfully at a glass of water.",
        1,
    ),
    (
        "A gnome and a Goliath are arm wrestling. The gnome beats the Goliath so the Goliath takes out a mechanical contraption that freezes the gnome.",
        1,
    ),
    (
        "A man in bright clothing stands in the corner. He’s laughing and talking to seemingly no one. When approached he stops talking and just stared intently, waiting for something.",
        1,
    ),
    ("Harth Stonebrew – An ent as “houseplant”/bard.", 1),
    (
        "A red dragonborn sits at the bar in fine clothing and is ordering strange drinks. If talked to enough (and if he’s drunk a bit too much) he’ll tell you he’s on a quest to prove himself to the clan.",
        1,
    ),
    (
        "A group of Kobolds carry around a dwarf dressed like a dragon. They adore him and answer to his every command. He lies to the 3 Kobolds and will pay them in scraps. If people talk to him and try to help the kobolds, the dwarf will pay you off to shut up and let it happen",
        1,
    ),
    (
        "A group of rowdy dwarves… they are obsessively talking about the local sports team (Go Sports!)",
        1,
    ),
    (
        "A scarecrow dressed like a ranger in all black in the darkest corner of the inn. The barkeep keeps a tally of how many people try to talk to him to get a quest or attack it when it doesn’t respond.",
        1,
    ),
    (
        "A young-looking elf woman, who looks almost like a drow, but not quite. She is dark-haired, and has black eyes. When she moves, her cloak shifts aside to reveal that her arm ends just above the elbow. She seems to prefer the shadows, and drinks a dark ale most consider too bitter for their tongues. The innkeeper recommends that, should you approach her, you should definitely not call her a drow.",
        1,
    ),
    (
        "A slime. A humanoid slime. Looks vaguely female. Is trying very hard to get drunk, but its body processes alcohol too fast to get more than buzzed. Has a lot of gold that it is siting on. The bar tender is starting to get a bit desperate to find a brew that with actually inebriate the slime, even for a moment. It has threatened to buy the whole stock of alcohol and try to down it all at once by flooding the basement and jumping in.",
        1,
    ),
    (
        "A goblin stripper named Grelka. Grelka tries to steal bedrolls from people she dances for because the definition of “take them to bed” got muddled up with “take their bed”.",
        1,
    ),
    (
        "A cheesemaker, trying to make a business deal with the owner of the bar. He offers a free sample and if the player tries it, DC 15 Constitution check to see if the player gets food poisoning",
        1,
    ),
    (
        "A shady man who comes in, orders 20 bottles of hard liquor, then pours them all into an Erlenmeyer flask and lights a fire under it. He proceeds to fill five of the bottles with the substance, stuffs napkins in them, and walks out.",
        1,
    ),
    (
        "You see a party of visually shaken dwarfs silently drowning their sorrow in a corner of the pub. Chatting with them reveals that they were part of a trade caravan visiting an obscure dwarven outpost, only to discover nothing but a deserted fortress of horribly mutilated corpses.",
        1,
    ),
    ("Three gnomes in a trench coat.", 1),
    (
        "A frantic looking young wizard pours over countless tomes and scrolls. She seems to be searching for a particular spell and when questioned she only mentions that her mentor is going to kill her if she can’t locate which plane that town went soon.",
        1,
    ),
    (
        "A patriot veteran of a previous war in the land. Having lost his leg in the war, he now spends most his time at the bar telling war stories, or drunkenly singing the national anthem or some obscure war ballad. Just don’t bring up any battles the nation lost though…",
        1,
    ),
    (
        "A jolly half elf named Craig who looks a lot like Patton Oswald. Craig has a list of jobs, personal ads, missed connections etc. Whenever you ask about work in the Inn, they suggest you check out The list that Craig has made.",
        1,
    ),
    (
        "A mother and father, and their three kids. Their house burned down in a mysterious fire and they are sheltering at the inn until they can find somewhere else to stay.",
        1,
    ),
    (
        "A spellcaster who lost their apprenticeship. The spellcaster was a reliable student but was the victim of a covetous rival who sabotaged their work and spread rumors. The spellcaster doesn’t have the motivation to fight back since the rival was better liked and no one wanted to hear the other side of the story.",
        1,
    ),
    (
        "A local merchant who scored a big foreign contract. S/he and team are excited about hiring more workers and boosting the local economy and the town/city’s reputation.",
        1,
    ),
    (
        "An inquisitor tracking a heinous criminal. The trail has gone cold and the inquisitor is looking for rumors or sightings.",
        1,
    ),
    (
        "A horse racing team bringing horses to a grand prix in a city nearby. The coach and an experienced racer are encouraging a nervous first-timer who is already getting prerace jitters.",
        1,
    ),
    (
        "Gundrick Aleseeker, a brewer of great renown on a test to try ever beer produced in the land. He sits at a side table with a set of the smallest glasses the inn have, studiously sniffing and tasty one then writing notes for five minutes. Once he has tried each if their are no more inns in town he will order his favourite and sip it contently. Any who approach him before this will be bluntly asked to leave but after finished tasting he is an avid conversationalist.",
        1,
    ),
    (
        "Blart is a bugbear who comes from a far away tribe, that collapsed do to lack of food. Despite the deaths of his people, Blart is a barbarian of the ancestral guardian path, and the deaths of his people empower him. He speaks in a loud squeaky voice, and has strange habit of drinking black tar.",
        1,
    ),
    (
        "Wendel Waterweary is a normal human merchant. She is in charge of the towns trade with other towns, and frequently leads the trade mission. When not on the job, she can be found in the Inn hosting games where players use strange polyhedral dice and their imaginations to simulate great adventures.",
        1,
    ),
    (
        "Kaza Arbiter, also known by his alias “Luke Warm” is a human artificer and criminal. Using transmutation magic, he disguises himself and his inventions (albeit mostly stolen) to become mundane items when not in use. An astute person might be able to recognize Kaza by his short stature, young appearance, and abnormal love of tea. When not on heists, he disguises himself as “Luke Warm”, an everyday scholar studying chemistry.",
        1,
    ),
    (
        "A dwarf, and and elf all enter together, order a drink at the bar and go upstairs. When they come down shortly after, and it seems as though they have exchanged clothes.",
        1,
    ),
    (
        "Three old geezers sat around a table for four. They won’t let anyone take the empty forth stool. The barkeep steps in if anyone objects. They have a tab even if such a facility isn’t available to all. They never seem to order but the drinks arrive at a steady rate. Always 4. One each and one in front of the empty stool. When they finish, the spare is tipped into a nearby plant, out of the window or otherwise disposed of. Except the last of the evening when one of the old men will sometimes pass it to a young’un sat nearby as they all get up to leave.",
        1,
    ),
    (
        "A middle aged man and his wife. Will hustle her out of the bar at the first sign of trouble, impropriety or bad language muttering grossly. She seems supremely unconcerned (or even interested in anything salacious!).",
        1,
    ),
    (
        "An unkempt elven apprentice mage who will enthusiastically discuss magic theory and categorisation of cantrips with (Or more accurately at) anyone not fast or savvy enough to get away. Not particularly interested in whether you have magical knowledge and even gets disturbed if you disagree or try to change topic.",
        1,
    ),
    (
        "A Goliath in a dark cloak desperately trying to hide how tall he is by slouching as much as he can.",
        1,
    ),
    (
        "A human male with an eyepatch and one arm who rents the largest room in the inn and leaves.",
        1,
    ),
    ("An elderly man covered in old tribal tattoos chatting with three young men.", 1),
    (
        "Ambros, a grey bearded dwarf with nasty scars over his face, hes known for his knowledge of beer, mead and ale.",
        1,
    ),
    (
        "A trickster mage named Elondur, always surprises his fellow guests with sleight of hand tricks. Nobody knows if theres actual magic involved.",
        1,
    ),
    (
        "Welka – An extremely beautiful woman, standing a full 6’6″, with guinea-gold locks and an ice-blue greataxe. She seems to be waiting for someone, and looks up whenever a man walks in the room.",
        1,
    ),
    (
        "Gustav Ironboots- A grizzled Dwarf guard captain, with a kindly eye and a friendly word from half of the patrons. Gustav has been a guardsman in the area for nearly 150 years, and most people know him well. Has a relaxed but careful attitude.",
        1,
    ),
    (
        "Gladiolas Doombaker- A high elf with odd magical facial brands and the look of an archmage offers succulent pastries to the party. A former Archvillain, Gladiolas was defeated by a party who used powerful divine magic to switch his focus from the arcane to the oven. He now prepares incredibly delicious breads, muffins, and other doughy goodies.",
        1,
    ),
    (
        "Darlan the Human – a swarthy, golden-eyed man with dark hair drinks alone at the bar. With very little provocation, he will inform you he isn’t a Tiefling, and that he was just born looking a little different. His grandfather was a priest of the sun god. There is no demonic line in his family, thank you very much.",
        1,
    ),
    (
        "Curtis and Lissandra- a younger-middle aged couple are holding hands at one of the tables. He is a wizard, and she is a paladin. They have left their children with the neighbor’s daughter and are having a quiet dinner together.",
        1,
    ),
    (
        "Two rather drunk clerics are performing a raucous and somewhat raunchy augury, asking about people in the room to shouts of laughter from onlookers.",
        1,
    ),
    (
        "Palwise the Invisible Hand – A halfling sits on a stool, enjoying what looks like lemonade. His arms and hands are completely and permanently invisible, the result of a misspoken wish. He sometimes wears long sleeves and gloves, but not today.",
        1,
    ),
    (
        "A group of sopping wet adventurers come slouching in the tavern, leaving muddy footprints. It is a clear day outside. If asked, the fighter smacks the wizard upside the head and mutters about a cooling spell gone wrong.",
        1,
    ),
    (
        "A man (clearly royalty or nobility in disguise) is chatting amiably with those around him, while his guard, also in disguise and looking long-suffering, sits close by. The locals can tell, but are taking it in good grace.",
        1,
    ),
    (
        "Nepason Burke – An Eldritch knight and half of Burke and Habbes, a famous adventuring duo from twenty years ago. Eprim Habbes is now a Lord and a General. Burke has chosen the quiet life, and seems content with his choice.",
        1,
    ),
    ("A very drunk doppelganger. His disguise is slipping as he drinks.", 1),
    (
        "Garick Jenerick – An odd old man who approaches different parties and implores their aid. Very wealthy and rather senile, he has a gruesome ‘hobby’ collecting body parts from various monsters- goblin ears, rat tails, wolf pelts, etc. What he does with them no one knows.",
        1,
    ),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {roll(table)}\n")


if __name__ == "__main__":
    main()
