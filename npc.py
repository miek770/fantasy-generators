from roll import expand, roll, roll_exclusive
from enum import Enum


class Alignment(Enum):
    Good = 0
    Neutral = 1
    Evil = 2


class Lawfulness(Enum):
    Lawful = 0
    Neutral = 1
    Chaotic = 2


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

# To be replaced with an open source table with more entries
table_animal = [
    ("cats", 1),
    ("dogs", 1),
    ("mouses", 1),
    ("rats", 1),
    ("birds", 1),
    ("insects", 1),
    ("spiders", 1),
    ("scorpions", 1),
    ("bats", 1),
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

table_weight = [
    (" and slim", 3),
    ("", 4),
    (" and round", 2),
    (" and fat", 1),
]

table_height = [
    ("a tiny", 1),
    ("a small", 3),
    ("a", 4),
    ("a tall", 2),
]

table_side = [
    ("left", 1),
    ("right", 1),
]

table_upper_lower = [
    ("upper", 1),
    ("lower", 1),
]

table_body_part = [
    ("head", 1),
    ("face", 1),
    ("nose", 1),
    (f"{roll(table_side)} eye", 1),
    ("mouth", 1),
    (f"{roll(table_side)} ear", 1),
    ("neck", 1),
    (f"{roll(table_side)} elbow", 1),
    (f"{roll(table_side)} arm", 1),
    (f"{roll(table_side)} hand", 1),
    (f"{roll(table_side)} foot", 1),
    (f"{roll(table_side)} leg", 1),
    (f"{roll(table_side)} knee", 1),
    (f"{roll(table_side)} shoulder", 1),
    (f"{roll(table_side)} nipple", 1),
    (f"{roll(table_upper_lower)} lip", 1),
]

table_body_piercing_location = [
    ("nostril", 1),
    ("eyebrow", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
]

table_appearance = [
    ("wears distinctive jewelry", 1),
    (f"wears piercings on the {roll(table_body_part)}", 1),
    ("wears flamboyant or outlandish clothes", 1),
    ("wears formal, clean clothes", 1),
    ("wears ragged, dirty clothes", 1),
    (f"bears a pronounced scar on the {roll(table_body_part)}", 1),
    ("has a missing teeth", 1),
    ("has missing fingers", 1),
    ("has an unusual eye color (or 2 different colors)", 1),
    (f"has visible tattoos on the {roll(table_body_part)}", 1),
    (f"has a visible birthmark on the {roll(table_body_part)}", 1),
    (f"has a bruised {roll(table_body_part)}", 1),
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

table_craft = [
    ("cook", 1),
    ("mason", 1),
    ("carpenter", 1),
    ("jeweler", 1),
    ("smith", 1),
    ("tinkerer", 1),
    ("alchemist", 1),
    ("scribe", 1),
    ("hunter", 1),
]

table_proficiency = [
    ("novice", 30),
    ("skilled", 50),
    ("talented", 20),
    ("expert", 5),
    ("master", 3),
    ("legendary", 1),
]

table_instrument = [
    ("flute", 1),
    ("luthe", 1),
    ("drum", 1),
]

table_talent = [
    (f"enjoys playing the {roll(table_instrument)}", 1),
    ("hates music of any genre", 1),
    ("speaks several languages fluently", 1),
    ("is unbelievably lucky", 1),
    ("has a perfect memory", 1),
    ("has trouble remembering names", 1),
    ("is great with animals", 1),
    ("is great with children", 1),
    ("is great at solving puzzles", 1),
    ("is great at one specific game", 1),
    ("is great at impersonations", 1),
    ("draws beautifully", 1),
    ("paints beautifully", 1),
    ("sings beautifully", 1),
    ("drinks everyone under the table", 1),
    (f"is an {roll(table_proficiency)} {roll(table_craft)}", 1),
    (f"is an {roll(table_proficiency)} dart thrower and rock skipper", 1),
    (f"is an {roll(table_proficiency)} juggler", 1),
    (f"is a {roll(table_proficiency)} actor and master of disguise", 1),
    (f"is a {roll(table_proficiency)} dancer", 1),
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
    ("likes to help others", 2, Alignment.Good),
    ("doesn't particularly tend to help others", 3, Alignment.Neutral),
    ("is rather self-centered", 1, Alignment.Evil),
]

table_lawfulness = [
    ("believes in law and order", 3, Lawfulness.Lawful),
    ("believes laws are sometimes wrong and civilization has a price", 2, Lawfulness.Neutral),
    ("believes rules are for others", 1, Lawfulness.Chaotic),
]

table_good_ideal = [
    ("beauty", 1),
    ("charity", 1),
    ("greater good", 1),
    ("life", 1),
    ("respect", 1),
    ("self-sacrifice", 1),
]

table_evil_ideal = [
    ("domination", 1),
    ("greed", 1),
    ("might", 1),
    ("pain", 1),
    ("retribution", 1),
    ("slaughter", 1),
]

table_lawful_ideal = [
    ("community", 1),
    ("fairness", 1),
    ("honor", 1),
    ("logic", 1),
    ("responsibility", 1),
    ("tradition", 1),
]

table_chaotic_ideal = [
    ("change", 1),
    ("creativity", 1),
    ("freedom", 1),
    ("independence", 1),
    ("no limits", 1),
    ("whimsy", 1),
]

table_neutral_ideal = [
    ("balance", 1),
    ("knowledge", 1),
    ("live and let live", 1),
    ("moderation", 1),
    ("neutrality", 1),
    ("people", 1),
]

table_other_ideal = [
    ("aspiration", 1),
    ("discovery", 1),
    ("glory", 1),
    ("nation", 1),
    ("redemption", 1),
    ("self-knowledge", 1),
]

table_multiple_bonds = [
    (1, 9),
    (2, 1),
]

table_bond = [
    ("dedicated to fulfilling a personal life goal", 1),
    ("protective of close family members", 1),
    ("protective of colleagues or compatriots", 1),
    ("loyal to a benefactor, patron or employer", 1),
    ("captivated by a romantic interest", 1),
    ("drawn to a special place", 1),
    ("protective of a sentimental keepsake", 1),
    ("protective of a valuable possession", 1),
    ("out for revenge", 1),
]

table_flaw = [
    ("being susceptible to romance", 1),
    ("enjoying decadent pleasures", 1),
    ("arrogance", 1),
    ("envy", 1),
    ("overpowering greed", 1),
    ("being prone to rage", 1),
    ("a foolhardy bravery", 1),
    ("glutony", 1),
    ("pride", 1),
    ("sloth", 1),
    ("jealousy", 1),
]

table_secret = [
    ("a forbidden love", 1),
    ("a powerful ennemy", 1),
    (f"a fear of {roll(table_animal)}", 1),
    ("a shameful or scandalous history", 1),
    ("a past crime or misdeed", 1),
    ("the possession of forbidden lore", 1),
]


def npc():
    description = []
    sex = roll(table_sex)
    if sex == "male":
        pronoun = "he"
        pronoun_poss = "his"
    else:
        pronoun = "she"
        pronoun_poss = "her"

    description.append(f"{pronoun} is {roll(table_height)}{roll(table_weight)} {roll(table_age_qualifier)} {sex} {roll(table_race)} {roll(table_age)}.".capitalize())
    description.append(f"{pronoun} {roll(table_appearance)}.".capitalize())

    a = roll_exclusive(table_high_ability, table_low_ability)

    description.append(f"{pronoun} {a[0]} but {a[1]}.".capitalize())
    description.append(f"{pronoun} {roll(table_talent)} and {roll(table_mannerism)}.".capitalize())
    description.append(f"{pronoun} is {roll(table_frequency)} {roll(table_interactions)}.".capitalize())

    alignment = roll(table_alignment)
    lawfulness = roll(table_lawfulness)

    description.append(f"{pronoun} {alignment[0]} and {lawfulness[0]}.".capitalize())

    ideals = []
    if alignment[1] == Alignment.Good:
        ideals.append((table_good_ideal, 10))
    else:
        ideals.append((table_good_ideal, 1))
    if alignment[1] == Alignment.Evil:
        ideals.append((table_evil_ideal, 10))
    else:
        ideals.append((table_evil_ideal, 1))
    if lawfulness[1] == Lawfulness.Lawful:
        ideals.append((table_lawful_ideal, 10))
    else:
        ideals.append((table_lawful_ideal, 1))
    if lawfulness[1] == Lawfulness.Neutral:
        ideals.append((table_neutral_ideal, 10))
    else:
        ideals.append((table_neutral_ideal, 1))
    if lawfulness[1] == Lawfulness.Chaotic:
        ideals.append((table_chaotic_ideal, 10))
    else:
        ideals.append((table_chaotic_ideal, 1))
    ideals.append((table_other_ideal, 5))
    table_ideal = roll(ideals)
    ideal1, ideal2 = roll_exclusive(table_ideal, table_ideal)

    description.append(f"{pronoun} values {ideal1} and {ideal2} above all else.".capitalize())

    n_bonds = roll(table_multiple_bonds)
    if n_bonds == 1:
        description.append(f"{pronoun} is {roll(table_bond)}.".capitalize())
    else:
        bond1, bond2 = roll_exclusive(table_bond, table_bond)
        description.append(f"{pronoun} is {bond1} and {bond2}.".capitalize())

    description.append(f"{pronoun_poss} biggest flaw is {roll(table_flaw)};".capitalize())
    description.append(f"{pronoun_poss} deepest secret is {roll(table_secret)}.")

    #description.append(f"".capitalize())

    print(" ".join(description))


if __name__ == "__main__":
    npc()