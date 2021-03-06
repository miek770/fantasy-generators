from roll import roll


# Source: http://dndspeak.com/2018/08/09/100-useless-people-you-find-on-a-failed-gather-information-check/
table = [
    (
        "A teenaged ne’er-do-well tried to sell you a narcotic herb. It turned out to be oregano. There’s no law against selling oregano.",
        1,
    ),
    ("You met a very friendly puppy. The owner let you pet it.", 1),
    (
        "Two old women insisted that whatever you’re asking about, that’s what’s wrong with kids these days, asking questions like that.",
        1,
    ),
    (
        "A little boy said he was lost. His mother was literally right across the street. She apologizes to you for the trouble he’s caused.",
        1,
    ),
    (
        "You saw someone with a really cool-looking jacket. Nothing matching the description of anyone you’re looking for, you just thought it looked really nice.",
        1,
    ),
    (
        "A street artist was drawing and selling caricatures of people, but when you described what you were looking for, she said she hadn’t seen anything like that.",
        1,
    ),
    (
        "A man selling sausages in buns said he hadn’t seen anything and grumbled ‘Idle questions don’t pay the bills– sausages do’.",
        1,
    ),
    (
        "An old man recognized you as a fellow adventurer. He told you his life story and promised he’ll get to the good part soon. He never got to the good part. It was barely even a story, just a list of things he killed and treasure he found. You learned nothing from it.",
        1,
    ),
    (
        "An old woman was having a serious discussion with a dog. It was strange, but it didn’t help your investigation.",
        1,
    ),
    (
        "An old man claimed to have seen what/who you’re looking for. You followed him for nearly an hour. When you finally asked him how long to get to the thing. He couldn’t remember what you were looking for or where you were going.",
        1,
    ),
    (
        "A small child asked you why you were ‘dressed funny’. Then she asked you ‘Why?’. And then asked you ‘Why?’. This continued until her mother dragged her away.",
        1,
    ),
    (
        "You are pretty sure you saw a middle-aged lady squat and relieve herself in an alleyway.",
        1,
    ),
    (
        "You didn’t find anyone with information, but you did spot a newspaper headline where the word ‘nebulousness’ spelled incorrectly.",
        1,
    ),
    (
        "You found someone with a hooded cloak drawn down over their face, writing on a wall. They ran off before you could ask them any questions. They left behind a drawing that is … inappropriate.",
        1,
    ),
    (
        "A woman was handing out samples of a new cultivar of apple. It’s not great. It’s not terrible. Sweet but a little mealy.",
        1,
    ),
    (
        "You found a group of guards on smoke break. They didn’t see whatever it was you were looking for and they suggest you move along quickly.",
        1,
    ),
    (
        "You saw a little old lady playing chess with her great-granddaughter, though she was blind and she had the girl move her pieces for her. This was heartwarming, but it didn’t solve your current problem.",
        1,
    ),
    ("You saw a cat playing with a dead mouse- it ran away before you got close.", 1),
    (
        "You saw a cat playing with a live bird– the cat paused to look at you and the bird flew away. The cat glared at you angrily.",
        1,
    ),
    (
        "You met a merchant from a foreign land selling exotic spices. He didn’t seem to have heard of anything– he barely knows the language, and constantly turned the conversation back to what spices you’ll buy. You think.",
        1,
    ),
    (
        "A woman selling ointments and perfumes from a cart blocked your path and badgered you to buy something. She spritzed you with a free sample and you now smell like lavender.",
        1,
    ),
    (
        "A street cleaner offered to let you search the contents of his bin for anything useful. After an hour, you found nothing and now you smell like rotten fruit.",
        1,
    ),
    (
        "You asked a bartender for information. He said they do trivia on Tuesdays, live music on Fridays and ale is half-priced on Mondays. And that’s pretty much it.",
        1,
    ),
    (
        "A group of drunk old men waved you over to their table at the local pub, claiming they had information. Each of them gave contradicting stories. As you walked away, they argued over who hoodwinked you the most.",
        1,
    ),
    (
        "A well-dressed woman says that she had the object of your search in her shop right now. Once you get in, she began a presentation about how her patented liniment of castor oil, camphor, and 7 secret herbs and resins will cure all your ailments and change your life.",
        1,
    ),
    (
        "You asked a monk if he’s seen what you’re looking for. He hasn’t, and you interrupted his prayers.",
        1,
    ),
    (
        "Three old women were discussing possibilities of marriage for their grandchildren. They went quiet and glared at you when you walked past; when they thought you were out of earshot, agreed amongst themselves that you were an example of the type of suitor they hoped to avoid.",
        1,
    ),
    (
        "A group of children were roughhousing, pretending to be adventurers. They stared open-mouthed as you approached them, as if seeing a celebrity, but acted shy when you came too close.",
        1,
    ),
    (
        "You heard a group of girls discussing peoples’ outfits as they observed passers-by. They agreed amongst themselves that they don’t completely hate your outfit. Your mood is significantly brightened, but you didn’t collect any useful information.",
        1,
    ),
    (
        "An old woman said she’s sure her nephew knows, but you had to remind her several times why you approached her in the first place. When you arrived at her nephew’s home, he thanked you for bringing the old lady back but didn’t know anything that could help you solve your problem.",
        1,
    ),
    (
        "You passed a bard with limp black hair and thick eyeliner. His voice was barely audible above his sad guitar. When you asked him if he’s seen anything he told you that no one sees anything, we are all puppets with our strings cut, washing downstream, waiting to drown.",
        1,
    ),
    (
        "An excitable elderly man gave you specific and detailed instructions to a building. They sell jars of maraschino cherries, and they didn’t have any information.",
        1,
    ),
    (
        "You saw an old man yelling at a cloud. There are just some regular clouds floating by. He wore an onion tied to his belt and yelled at you for looking at him funny.",
        1,
    ),
    (
        "A man claimed to have been be abducted by fairies, but the more he revealed the more it’s clear he was just blackout drunk and spent the night in jail.",
        1,
    ),
    (
        "A toddler insisted on telling you about the snail he found today. Unfortunately, you could only understand about one word in five, and everything you said or did seemed to encourage him.",
        1,
    ),
    (
        "You saw an elven woman was yelling at a food kart. She wanted her money back because her meat kebab contained meat. Eventually the town guard had to be called in to settle the dispute.",
        1,
    ),
    (
        "A handsome young man waved to you. When you waved back and approached him, he seemed confused. He was waving at his friend, who was standing several feet behind you.",
        1,
    ),
    (
        "Someone pointed out a flyer for a laundry service with a clever pun name. When you try telling your companions about it, you can’t remember the name. You feel foolish.",
        1,
    ),
    (
        "A man was trying to sell eyeglasses on a street corner and he insisted that you needed a pair. You did not need a pair, especially not ones with a great big scratch on the left lens.",
        1,
    ),
    (
        "You saw someone with the worst haircut you’ve ever encountered. You briefly forgot what you were looking for as you marveled at just how bad this haircut was. You couldn’t even put into words just how unflattering it was and you become exasperated trying to explain to the rest of the party how deeply disturbed you are that someone left the house looking like that.",
        1,
    ),
    (
        "You met another party of adventurers. They asked you about answers to their own quest first, and then you asked them about your own. You couldn’t help each other, so they wished you luck on your quest and bid you a sincere goodbye.",
        1,
    ),
    (
        "You spotted a group of youths who tried to look as innocent as possible as you walked past. You’re not even sure what they were guilty of, they just looked like trouble-makers, but definitely not worth the hassle.",
        1,
    ),
    (
        "A gnome in the tavern swore he knew all about what you’re looking for but can’t remember anything of use for less than 3 top-shelf drinks. He talked about many things before he fell asleep, none of them pertaining to your questions.",
        1,
    ),
    (
        "You asked a normal-looking gentleman if he knew anything, he looked at you wide-eyed, and gasped. ‘You can see me? You can really see me?!’ Before you can answer he’d run away, lost in the crowd. That was the last time you saw him.",
        1,
    ),
    (
        "A man with a sock puppet introduces it as his wife and talks through her in a falsetto ‘female’ voice. Neither the sock or the man had information relevant to your situation.",
        1,
    ),
    (
        "A dwarf was picking lice out of his beard and eating them. He noticed you noticing him and pretended he was just scratching his chin instead.",
        1,
    ),
    (
        "You saw two sweet-looking old people holding hands. It almost made you believe in true love again. Almost.",
        1,
    ),
    (
        "A citizen claimed to have the all of the answers and went on to explain a conspiracy theory that the government is suppressing the ‘truth’ that the world is cube-shaped for reasons that remain unclear. You left before he could finish.",
        1,
    ),
    (
        "As you posed questions to a local merchant, you notice a woman, her hood pulled up against the sun, staring at you unblinkingly. On confronting this suspicious behavior, it is revealed that she was simply staring into space, contemplating dinner.",
        1,
    ),
    (
        "A child said he knows a very bad secret, but none of the grownups would listen to him. He showed you his father’s cache of wood relief carvings, each crudely carved with images of improbably-proportioned women performing lewd acts. This was a waste of time, they weren’t even carved very well.",
        1,
    ),
    (
        "A six-year-old girl told you she knows something very important, then sagely informs you on the anatomical differences between boys and girls. She wandered off before you could react.",
        1,
    ),
    (
        "A street urchin said he had some inside information, but he couldn’t remember properly until you gave him a few coins. He said loudly that you’re a creep for trying to pay him off, and smugly walked away as people stopped what they were doing to stare. When they went back to what they were doing without questioning you, you suspected that you weren’t the first one to fall for this trick. The boy was long gone by then.",
        1,
    ),
    (
        "You felt like the locals were viewing you strangely. Like they knew something you didn’t. When you finally cornered one into an admission, they informed you that your waterskin had been leaking, making it look like you wet your trousers.",
        1,
    ),
    (
        "A man smiled at you knowingly but refused to answer any of your questions. A helpful passerby told you that this man is the village idiot, and that he always smiles like that.",
        1,
    ),
    (
        "An enterprising street entertainer had no information to share, but for a silver piece he will do a whistle, a tumble, and a fart — all at the same time.",
        1,
    ),
    (
        "A heavyset woman boldly stated that she doesn’t know and doesn’t care, but if you’d like to earn a copper piece she has four large pots that need to be scraped clean.",
        1,
    ),
    (
        "A foreigner didn’t know anything but dammit, they wanted to be helpful. So they just filled in their gaps of knowledge with anything they could think up.",
        1,
    ),
    (
        "A woman was walking strangely, changing her course for no apparent reason. She didn’t appear to be drunk. Turns out she compulsively avoids cracks in the pavement and didn’t have any information for you.",
        1,
    ),
    (
        "One of the commoners had a really nice butt. Really nice. What were you looking for again?",
        1,
    ),
    (
        "Vincent Tallman, three gnomes wearing a large overcoat, were trying to pass as a human. It doesn’t seem very convincing but no else seemed to notice. You’re not even sure why they were doing it but they never broke character, insisting that they were, in fact, a perfectly normal human adult. Even when one of the gnomes sneezed and the whole lot of them nearly toppled over.",
        1,
    ),
    (
        "A shadowy figure lurking in the darkest corner of the shadiest pub in town turned out to be a hat and coat hung up on a rack. That was the closest you got to any useful information.",
        1,
    ),
    (
        "A young man was sitting in a pillory, a broken lute at his feet. ‘Tasteless Scatological Jokester’ was written on a sign next to him. He did not look repentant. Perhaps even a little proud of himself. He did not know anything.",
        1,
    ),
    (
        "You find a dead body. You must stay as a witness for the local law enforcement, for 2 d6 X 10 min. Relatives eventually show up. The person died of perfectly ordinary natural causes related to a pre-existing medical condition.",
        1,
    ),
    (
        "A watchman follows you around acting like he thinks you’re a criminal, and frightening off your contacts. When you confront him, he says he’s bored and you looked suspicious, and then wanders off.",
        1,
    ),
    (
        "An old man in a tavern who declares that he will lead you to the local tavern with the best gossip so you can ask around there. He takes you out back, walks around to the front, and reenters through the main door. He got a laugh from the regulars.",
        1,
    ),
    (
        "“Marv the Magnificent”, a street performer who very loudly and extravagantly boasts to be the most mind-bogglingly talented juggler in all the land. You put off your investigation to watch for a few minutes. He’s ok.",
        1,
    ),
    (
        "A young girl is throwing pebbles at you. She will follow you for a good ways and will continue to pick up pebbles. The adults who recognize her tell you that you look like the neighbor she doesn’t like. The neighbor happens to be totally ordinary but does look a bit like you.",
        1,
    ),
    (
        "Three kenkus are following each other and mimicking each other with different accents and personalities. They are now mimicking you because you tried to ask them some questions.",
        1,
    ),
    (
        "Two people leafing through a manuscript in complex code with elaborate artwork of maps, exotic places, and mysterious artifacts. Each page has a different font, layout, and art style. After eavesdropping, you discover they are a scribe and author picking out a format and font. The manuscript is the scribe’s stylebook filled with nonsense.",
        1,
    ),
    (
        "There is a pair of little girls ahead of you selling flowers for a copper each. They’re just local wildflowers but they’re pretty and they smell nice.",
        1,
    ),
    (
        "You discover the barkeep at one of the taverns cheats their patrons by pouring them cheaper wine and beer after they have already had a few. You advise your party not to stay at that tavern.",
        1,
    ),
    (
        "An elderly woman who said a relevant keyword to her younger friend. You tried to talk with her, but only got more and more confused as the lady rambled incoherently. Her caretaker explains the lady is a stroke survivor with mild aphasia and uses the wrong words without realizing it.",
        1,
    ),
    (
        "A gaggle of homemakers gossiping about property laws, taxes, and which of their acquaintances they suspect of having extramarital affairs while doing laundry.",
        1,
    ),
    (
        "You find a child playing hide and seek. They roped you into the game, so you had to find all of the rest.",
        1,
    ),
    (
        "You follow a sparse trail of blood and gore to an abandoned shed. The butcher had given their favorite stray dog some offal, and the dog carried it here to eat.",
        1,
    ),
    (
        "A group of three philosophers sitting on a street corner debating an obscure moral quandary with great energy and enthusiasm. None of them seem to notice that they all actually agree with each other.",
        1,
    ),
    (
        "What looks like some rags tossed into a corner of an alleyway is in fact a poorly dressed beggar sleeping. He’s upset you woke him up.",
        1,
    ),
    (
        "A man standing outside a building, staring up at the window as a woman throws clothes and other personal items down at him with great vigor. He shouts up at her, demanding that she give him another chance.",
        1,
    ),
    (
        "A morose man hiding his drinking habits from his wife. None of his problems are helpful to your quest.",
        1,
    ),
    (
        "A tall elf walks through the street, accompanied by two half-elf bodyguards. He refuses to speak in Common, and even if addressed in Elvish, wants nothing to do with you. The elf happens to be both dreadfully boring and standoffish.",
        1,
    ),
    (
        "A cart with boxes marked with warnings to stay away in several languages. When approached, a halfling woman in a bee keeper’s outfit appears. She’s very annoyed you are disturbing her hives and tells you to buzz off.",
        1,
    ),
    (
        "Two crossdressers wanted you to judge whose outfit is better. You found a way to say nice things about both their choices and slipped off when they got distracted.",
        1,
    ),
    (
        "You see an amorphous cloud of dark smoke coming out of a fireplace. In the smoke you find a dirty chimney sweep, not understanding what is going on.",
        1,
    ),
    (
        "You meet a blind gnome who gives you incredibly specific and confident directions. He is lying, but you don’t notice. When you go to the wrong place, someone helpfully informs you that the gnome is a pathological liar.",
        1,
    ),
    (
        "A wizard appears in a puff of smoke, he approaches you and starts to speak, then looks around confused. He looks back at you, mumbles an apology about being in the wrong place, and disappears.",
        1,
    ),
    ("A mediocre busker.", 1),
    (
        "An old woman who makes a horrible grimace at you, but then scuttles away unexpectedly. She thought you were her child and was about to chew you out for your clothes and skipping work, but realized you were someone else when she got a closer look.",
        1,
    ),
    (
        "A pigeon with unusual coloring. You kept trying to get closer to see better, but the flock kept flying away. Eventually the flock mingled with another and you noticed several similarly unusual birds. It must be a common local mutation.",
        1,
    ),
    (
        "A pair of children who accidentally threw a small toy in your direction, which lands at your feet. One runs up to you and snatches it back, calling you a singsong name. His friend, standing behind him, mouths a silent apology to you.",
        1,
    ),
    (
        "Upon investigation, a citizen claims to have the information you’re looking for, though they can’t go into detail in public. They try to take you to their ‘hideout’ but you decide to give him/her the slip. The person turns out to be an innocent weirdo whose only goal is to convince you of a hairbrained conspiracy that is provably untrue.",
        1,
    ),
    ("A halfling who does nothing but brag about his hat.", 1),
    (
        "A young man crying by the side of the road. They are crying because they accidentally got sand in their eyes a few hours ago and it still hurts.",
        1,
    ),
    (
        "A young gnome that keeps making egg-cellent egg jokes. I’m not egg-saggerating, he knows and egg-cessive amount of yolks.",
        1,
    ),
    (
        "A person walked by you who smelled incredibly odd. The NPC denies s/he smells at all and tries to leave quickly. You pressed the NPC and discovered that he/she knocked over a bottle of perfume and that s/he has no sense of smell.",
        1,
    ),
    (
        "While conversing with a far-traveled merchant of antiquities, you notice some guards watching you intently, their eyes narrowed, money changing hands. You conclude your business with the merchant and challenge the guards. It is revealed they were betting on whether you’d waste money on the merchant’s junk.",
        1,
    ),
    (
        "A loud preacher in the nearby town courtyard who was denouncing what he believes to be evils in society for everyone to hear. There was a small crowd listening, some of whom were hecklers. You didn’t learn anything.",
        1,
    ),
    ("Three young women gossiping and fawning over a handsome local.", 1),
    ("A young woman ignores your questions as she is too interested in her book.", 1),
    (
        "A man who only likes to talk about his hobbies and shrugs off your attempts to leave the conversation.",
        1,
    ),
    (
        "A farmer observing a hole in his fence where an amorous bull broke through. The bull introduced himself to the cows.",
        1,
    ),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {roll(table)}\n")


if __name__ == "__main__":
    main()
