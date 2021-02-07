from roll import roll


# Source: http://dndspeak.com/2018/03/100-social-encounters-on-the-road/
table = [
    ("A bard or minstrel, half dressed and looking over his shoulder.", 1),
    ("Farmer going to/returning from market with his meager goods.", 1),
    ("Farmer going to/returning from town with his/her sons.", 1),
    ("Farmer going to/returning from town with his/her daughters.", 1),
    ("Girl running away from home.", 1),
    ("Boy running away to the city.", 1),
    ("A lost child, in tears and holding a torn sack.", 1),
    ("A troupe of entertainers, led by an overdressed and curious Elf.", 1),
    ("Full company of mercenaries, led by a stout, dark bearded Captain.", 1),
    ("A small group of mercenaries, dishevelled and sweating.", 1),
    ("Minor noble travelling via horse, with servants.", 1),
    ("Minor noble going to/returning from hunt, with retinue.", 1),
    ("Local bailiff, sheriff or warden, with a suspicious outlook of strangers.", 1),
    ("A hunter or poacher, with a huge longbow strapped to their back.", 1),
    (
        "A pair of hunters or poachers, arguing about who is to blame for a missed shot.",
        1,
    ),
    ("Large trading caravan, with accompanying surly guards.", 1),
    ("A lone trader/merchant on foot, leading a mule carrying their wares.", 1),
    ("Lone trader/merchant riding on a horse drawn wagon.", 1),
    ("Limping bailiff and his badly beaten prisoner.", 1),
    ("Escaped prisoner, manacled and carrying a religious icon.", 1),
    ("Sheriff and his dogs, out hunting an outlaw.", 1),
    ("A boundary warden with a broken bow and empty scabbard, fuming as he walks.", 1),
    ("Lone travelling priest, carrying a lit censer with an acrid smell.", 1),
    ("Lone travelling cleric, with a faintly glowing mace.", 1),
    (
        "Charismatic priest and retinue of apostles, who are mumbling to each other and won’t make eye contact.",
        1,
    ),
    ("A cleric and a small retinue of acolytes, full of confidence.", 1),
    ("A ranger/boundary warder patrol, with a cheerful leader.", 1),
    ("A patrol from the local city or town guard, nervous about being out of town.", 1),
    ("A foot messenger, with a ducal ring on his hand.", 1),
    (
        "A horse messenger wearing a royal tabard and carrying a fine leather satchel.",
        1,
    ),
    ("A travelling historian carrying a sack of old stone statues.", 1),
    ("A starving beggar, willing to trade information for food.", 1),
    (
        "A group of refugees, telling stories of war and oppression in their homeland.",
        1,
    ),
    ("A wounded soldier, limping along on crutches.", 1),
    ("A deserting soldier carrying a memento of a fallen friend.", 1),
    ("A wandering dog, with a silver collar and name tag.", 1),
    ("A bear wearing a collar and trailing a frayed rope.", 1),
    ("A riderless horse, with bulging saddlebags.", 1),
    ("A thrown rider, trying to catch his horse.", 1),
    ("A wandering madman, ranting about an invisible creature.", 1),
    (
        "A pair of dwarven prospectors, arguing loudly about where they took a wrong turn.",
        1,
    ),
    ("Halfling cook/chef, out foraging for ingredients.", 1),
    ("Overturned wagon with injured merchant.", 1),
    ("A bored elderly gnome, with a curious mechanical toy.", 1),
    ("Fisherman by a riverside, without any fish.", 1),
    ("Druid planting rows of trees across the road.", 1),
    ("A drunk from a nearby tavern, unsteady on his feet.", 1),
    ("A partially smashed coffin, with a “corpse” inside which is slowly moving.", 1),
    ("A dealer of “used magical artefacts”.", 1),
    ("An elf picking and eating wild berries.", 1),
    ("A manic Herbalist, with green smears around his mouth.", 1),
    ("Group of robed monks, carrying a lit censer.", 1),
    ("A squire chasing his drunken master’s horse.", 1),
    ("An armoured Dragonborn sitting on a stone, sharpening a sword and sighing.", 1),
    ("Farmer with an unmoving mule, laden with fruit.", 1),
    ("Guarded and chained prisoners digging a ditch.", 1),
    ("A pair of wagon drivers preparing to race each other.", 1),
    (
        "A tiny Earth Elemental, shifting pebbles from one side of the road to the other.",
        1,
    ),
    ("A group of dancing lights, which keep just ahead of the party.", 1),
    ("A drug addict, coming down from their last score.", 1),
    ("A harmless ghost, sadly humming an old song.", 1),
    ("A gnome riding an armoured mastiff.", 1),
    ("A hawker trying to find his bird.", 1),
    ("A grave robber, with mud on his shoes and a dark, wet sack on his back.", 1),
    (
        "A friendly necromancer with several raised skeletons, who offers to share food.",
        1,
    ),
    ("A gang of youths from a nearby town.", 1),
    ("A gnomish tinker & merchant, offering magical mending.", 1),
    ("A Quickling, fleeing from the service of a warlock.", 1),
    ("A drunken Hill Giant, asleep and snoring loudly.", 1),
    ("A starving hermit, bearing a sword handle without a blade.", 1),
    ("A migrating Treant, walking down the middle of the road.", 1),
    ("A dead knight’s retinue, returning the body home.", 1),
    ("Traveling reeve or magistrate, summoned to a case.", 1),
    ("A group of pilgrims, one of which is carrying a small, heavily bound chest.", 1),
    ("A backwoods moonshiner, offering free samples of his wares.", 1),
    ("A surveyor excited about discovering a door into an artificial hillock.", 1),
    ("A dripping wet fisherman, climbing up from a riverbank with an angry look.", 1),
    ("A girl picking wildflowers, acting as a lookout for local bandits.", 1),
    ("A boy swinging a stick like a sword, with a pet dog following.", 1),
    ("Villagers cutting wood to make bows.", 1),
    (
        "A stone golem with one leg shorter than the other, never walking in a straight line.",
        1,
    ),
    ("A pixie telling rude jokes and riddles.", 1),
    (
        "Four villagers burning a pile of corpses, which are emitting a thick purple smoke.",
        1,
    ),
    ("A wagoner trying to fix his strangely burned cart.", 1),
    ("A contented Halfling, smoking an oddly scented pipe.", 1),
    ("A wild-eyed and dishevelled Alchemist, ranting about a breakthrough.", 1),
    ("An imp caught in a rabbit trap, screeching loudly.", 1),
    ("A lost wagon guard, with scratches on his face.", 1),
    ("A seller of genuine, if minor, religious relics.", 1),
    ("An old gnome in hat and tattered clothes, rapidly shuffling a deck of cards.", 1),
    ("An ebullient Orc, dressed in bright fine silks.", 1),
    ("A Green Hag, offering a reward for revenge on those who tricked her.", 1),
    ("A wine merchant, asking for directions to the nearby town festival.", 1),
    ("A fur trapper, with a live wolverine as a pet.", 1),
    ("A sour old grandmother, complaining bitterly about her eldest son.", 1),
    ("A Hobgoblin out to see the world.", 1),
    ("A young man, with a hideous mask magically stuck to his face.", 1),
    ("A band of giant hunters, paid to kill a troublesome old Hill Giant.", 1),
    ("A charcoal burner, telling stories about haunted trees.", 1),
    ("A potion merchant, with a backpack full of ‘alternative’ potions.", 1),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {roll(table)}\n")


if __name__ == "__main__":
    main()