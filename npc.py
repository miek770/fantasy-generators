from roll import expand, roll, roll_exclusive

table_sex = [
    ("male", 1),
    ("female", 1),
]

table_race = [
    ("human", 50),
    ("elf", 5),
    ("half-elf", 10),
    ("dwarf", 10),
    ("halfling", 10),
    ("half-orc", 5),
    ("thiefling", 5),
    ("dragonborn", 5),
]

table_age_qualifier = [
    ("a young", 1),
    ("a", 2),
    ("an old", 1),
]

table_age = [
    ("child", 1),
    ("teen", 2),
    ("adult", 7),
]

table_appearance = [
    ("wears distinctive jewelry", 1),
    ("wears piercings", 1),
    ("wears flamboyant or outlandish clothes", 1),
    ("wears formal, clean clothes", 1),
    ("wears ragged, dirty clothes", 1),
    ("bears a pronounced scar", 1),
    ("has a missing teeth", 1),
    ("has missing fingers", 1),
    ("has an unusual eye color (or 2 different colors)", 1),
    ("has visible tattoos", 1),
    ("has a visible birthmark", 1),
    ("has an unusual skin color", 1),
    ("is bald", 1),
    ("has braided beard or hair", 1),
    ("has an unusual hair color", 1),
    ("has a nervous eye twitch", 1),
    ("has a distinctive nose", 1),
    ("has a distinctive posture (crooked or rigid)", 1),
    ("is exceptionally beautiful", 1),
    ("is exceptionally ugly", 1),
]

table_high_ability = [
    ("is powerful, brawny and strong as an ox", 1),
    ("is lithe, agile and graceful", 1),
    ("is hardy, hale and healthy", 1),
    ("is studious, learned and inquisitive", 1),
    ("is perceptive, spiritual and insightful", 1),
    ("is persuasive, forceful and a born leader", 1),
]

table_low_ability = [
    ("feeble and scrawny", 1),
    ("clumsy and fumbling", 1),
    ("sickly and pale", 1),
    ("dim-witted and slow", 1),
    ("oblivious and absentminded", 1),
    ("dull and boring", 1),
]

table_talent = [
    ("enjoys playing a musical instrument", 1),
    ("hates music of any genre", 1),
    ("speaks several languages fluently", 1),
    ("is unbelievably lucky", 1),
    ("is reputably unlucky", 1),
    ("has a perfect memory", 1),
    ("has trouble remembering names", 1),
    ("is great with animals", 1),
    ("is afraid of dogs", 1),
    ("is great with children", 1),
    ("hates children", 1),
    ("is great at solving puzzles", 1),
    ("doesn't enjoy games", 1),
    ("is great at one specific game", 1),
    ("is great at impersonations", 1),
    ("draws beautifully", 1),
    ("paints beautifully", 1),
    ("sings beautifully", 1),
    ("sings like a dying rooster", 1),
    ("drinks everyone under the table", 1),
    ("is awkward when drunk", 1),
    ("is an expert carpenter", 1),
    ("is an expert cook", 1),
    ("is an expert dart thrower and rock skipper", 1),
    ("is an expert juggler", 1),
    ("is a skilled actor and master of disguise", 1),
    ("is a skilled dancer", 1),
    ("knows thieves' cant", 1),
]

table_mannerism = [
    ("is prone to singing, whistling, or humming quietly", 1),
    ("speaks in rhymes or some other peculiar way", 1),
    ("has a particularly high voice", 1),
    ("has a particularly low voice", 1),
    ("slurs words", 1),
    ("lisps", 1),
    ("stutters", 1),
    ("enunciates overly clearly", 1),
    ("speaks loudly", 1),
    ("whispers", 1),
    ("uses flowery speech and long words", 1),
    ("frequently uses the wrong word", 1),
    ("uses colorful oaths and exclamations", 1),
    ("makes constant jokes or puns", 1),
    ("is prone to predictions of doom", 1),
    ("constantly fidgets", 1),
    ("often squints", 1),
    ("sometimes stare into the distance", 1),
    ("is always chewing on something", 1),
    ("paces when inactive", 1),
    ("taps fingers", 1),
    ("bites fingernails", 1),
    ("twirls hair or tugs beard", 1),
]

table_frequency = [
    ("always", 1),
    ("often", 1),
    ("sometimes", 1),
    ("scarcely", 1),
    ("rarely", 1),
]

table_interactions = [
    ("argumentative", 1),
    ("arrogant", 1),
    ("blustering", 1),
    ("rude", 1),
    ("curious", 1),
    ("friendly", 1),
    ("honest", 1),
    ("hot tempered", 1),
    ("irritable", 1),
    ("ponderous", 1),
    ("quiet", 1),
    ("suspicious", 1),
]

table_alignment = [
    # Good
    ("likes to help others", 2),

    # Neutral
    ("doesn't particularly tend to help others", 3),

    # Evil
    ("is rather self-centered", 1),
]

table_lawfulness = [
    # Lawful
    ("believes in law and order", 3),

    # Neutral
    ("believes laws are sometimes wrong and civilization has a price", 2),

    # Chaotic
    ("believes rules are for others", 1),
]


def npc():
    description = []
    sex = roll(table_sex)
    if sex == "male":
        pronoun = "he"
    else:
        pronoun = "she"

    description.append(f"{pronoun} is {roll(table_age_qualifier)} {sex} {roll(table_race)} {roll(table_age)}.".capitalize())
    description.append(f"{pronoun} {roll(table_appearance)}.".capitalize())

    a = roll_exclusive(table_high_ability, table_low_ability)

    description.append(f"{pronoun} {a[0]} but {a[1]}.".capitalize())
    description.append(f"{pronoun} {roll(table_talent)} and {roll(table_mannerism)}.".capitalize())
    description.append(f"{pronoun} is {roll(table_frequency)} {roll(table_interactions)}.".capitalize())
    description.append(f"{pronoun} {roll(table_alignment)} and {roll(table_lawfulness)}.".capitalize())

    print(" ".join(description))


if __name__ == "__main__":
    npc()