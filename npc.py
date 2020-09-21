# Standard library
from enum import Enum
from random import randint

# Current module
from roll import roll, roll_exclusive
from names.names import get as get_name


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
    ("horses", 1),
    ("llamas", 1),
    ("badgers", 1),
    ("dinosaurs", 1),
    ("wolves", 1),
]

table_age_qualifier = [
    ("young ", 1),
    ("", 2),
    ("old ", 1),
]

table_age = [
    ("child", 1),
    ("teen", 2),
    ("adult", 7),
]

table_weight = [
    ("slim", 3),
    ("thin", 3),
    ("lean", 4),
    ("round", 2),
    ("fat", 1),
    ("overweight", 2),
    ("obese", 1),
]

table_height = [
    ("tiny", 1),
    ("small", 3),
    ("typical", 10),
    ("tall", 3),
    ("huge", 2),
    ("gigantic", 1),
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
    (f"{roll(table_side)} nostril", 1),
    ("nostrils", 1),
    (f"{roll(table_side)} eyebrow", 1),
    ("eyebrows", 1),
    (f"{roll(table_upper_lower)} lip", 1),
    ("lips", 1),
    ("tongue", 1),
    (f"{roll(table_side)} ear", 1),
    ("ears", 1),
    (f"{roll(table_side)} nipple", 1),
    ("nipples", 1),
    ("belly button", 1),
    ("private parts", 1),
]

table_body_appendage = [
    (f"1 finger on the {roll(table_side)} hand", 1),
    (f"{randint(2, 5)} fingers on the {roll(table_side)} hand", 1),
    (f"1 toe on the {roll(table_side)} foot", 1),
    (f"{randint(2, 5)} toes on the {roll(table_side)} foot", 1),
    (f"the {roll(table_side)} ear", 1),
    (f"a tooth", 1),
    (f"the tip of the nose", 1),
]

table_eye_color = [
    ("brown", 1),
    ("grey", 1),
    ("blue", 1),
    ("green", 1),
    ("amber", 1),
    ("nut", 1),
    ("red", 1),
    ("yellow", 1),
    ("turquoise", 1),
    ("jade", 1),
]

table_multiple_eye_colors = [
    (1, 9),
    (2, 1),
]

table_eye_color_qualifier = [
    ("deep", 1),
    ("soft", 1),
    ("vivid", 1),
    ("diffuse", 1),
]

table_appearance = [
    ("wears distinctive jewelry", 1),
    (f"wears piercings on the {roll(table_body_piercing_location)}", 1),
    ("wears flamboyant or outlandish clothes", 1),
    ("wears formal, clean clothes", 1),
    ("wears ragged, dirty clothes", 1),
    (f"bears a pronounced scar on the {roll(table_body_part)}", 1),
    (f"is missing {roll(table_body_appendage)}", 1),
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
    (roll(["is powerful", "is brawny", "is strong as an ox"]), 1),
    (roll(["is lithe", "is agile", "is graceful"]), 1),
    (roll(["is hardy", "is hale" "is healthy"]), 1),
    (roll(["is studious", "is learned", "is inquisitive"]), 1),
    (roll(["is perceptive", "is spiritual", "is insightful"]), 1),
    (roll(["is persuasive", "is forceful", "is a born leader"]), 1),
]

table_low_ability = [
    (roll(["feeble", "scrawny"]), 1),
    (roll(["clumsy", "fumbling"]), 1),
    (roll(["sickly", "pale"]), 1),
    (roll(["dim-witted", "slow"]), 1),
    (roll(["oblivious", "absentminded"]), 1),
    (roll(["dull", "boring"]), 1),
]

# Source: http://dndspeak.com/2019/01/100-npc-jobs/
table_job = [
    ("Tinkerer", 1),
    ("Owlbear Breeder", 1),
    ("Shaman", 1),
    ("Bottle Maker", 1),
    ("Stable hand", 1),
    ("Innkeeper", 1),
    ("Blacksmith", 1),
    ("Washerwoman", 1),
    ("Town cryer", 1),
    ("Tailor", 1),
    ("Portrait painter", 1),
    ("Cobbler", 1),
    ("Lamplighter", 1),
    ("Trapper", 1),
    ("Fletcher", 1),
    ("Tanner", 1),
    ("Herbalist", 1),
    ("Farmer", 1),
    ("Carpenter", 1),
    ("Stonemason", 1),
    ("Miner", 1),
    ("Fortune teller", 1),
    ("Baker", 1),
    ("Town guard", 1),
    ("Rat catcher", 1),
    ("Doctor", 1),
    ("Messenger", 1),
    ("Lawyer", 1),
    ("Banker", 1),
    ("Animal tamer", 1),
    ("Guide", 1),
    ("Cartographer", 1),
    ("Sheriff", 1),
    ("Dairy maid", 1),
    ("Bookkeeper", 1),
    ("Academic", 1),
    ("Accountant", 1),
    ("Actor", 1),
    ("Apprentice", 1),
    ("Artisan", 1),
    ("Assassin", 1),
    ("Bandit", 1),
    ("Barde", 1),
    ("Beggar", 1),
    ("Bounty hunter", 1),
    ("Brewer", 1),
    ("Con artist", 1),
    ("Cook", 1),
    ("Druid", 1),
    ("Fisher", 1),
    ("Gambler", 1),
    ("Gravedigger", 1),
    ("Hunter", 1),
    ("Jester", 1),
    ("Knight", 1),
    ("Laborer", 1),
    ("Lawman", 1),
    ("Lumberjack", 1),
    ("Mercenary", 1),
    ("Noble", 1),
    ("Priest", 1),
    ("Ranger", 1),
    ("Sailor", 1),
    ("Scribe", 1),
    ("Servant", 1),
    ("Shepperd", 1),
    ("Slave", 1),
    ("Soldier", 1),
    ("Thief", 1),
    ("Thug", 1),
    ("Trader", 1),
    ("Treasure Hunter", 1),
    ("Wanderer", 1),
    ("Wizard", 1),
    ("Wrestler", 1),
    ("Lighthouse Keeper", 1),
    ("Landlord", 1),
    ("Author", 1),
    ("Lookout", 1),
    ("Clocksmith", 1),
    ("Exorcist", 1),
    ("Soapmaker", 1),
    ("Beekeeper", 1),
    ("Botanist", 1),
    ("Alchemist", 1),
    ("Potioneer", 1),
    ("Librarian", 1),
    ("Bartender", 1),
    ("Toymaker", 1),
    ("Woodcarver", 1),
    ("Squire", 1),
    ("Roofer", 1),
    ("Sculptor", 1),
    ("Scholar", 1),
    ("Nurse", 1),
    ("Nun", 1),
    ("Mortician", 1),
    ("Historian", 1),
    ("Gladiator", 1),
    ("Barber", 1),
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
    (f"is an {roll(table_proficiency)} {roll(table_job)}", 1),
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
    (
        "believes laws are sometimes wrong and civilization has a price",
        2,
        Lawfulness.Neutral,
    ),
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
        firstname = get_name("male").capitalize()
    else:
        pronoun = "she"
        pronoun_poss = "her"
        firstname = get_name("female").capitalize()

    lastname = get_name("surname").capitalize()

    description.append(
        f"{firstname} {lastname} is a {roll(table_height)} and {roll(table_weight)} {roll(table_age_qualifier)}{sex} {roll(table_race)} {roll(table_age)}."
    )
    description.append(f"{pronoun} {roll(table_appearance)}".capitalize())

    n_eye_colors = roll(table_multiple_eye_colors)
    if n_eye_colors == 1:
        description.append(
            f"and {pronoun_poss} eyes are a {roll(table_eye_color_qualifier)} {roll(table_eye_color)}."
        )
    else:
        eye_left, eye_right = roll_exclusive(table_eye_color, table_eye_color)
        description.append(
            f"and {pronoun_poss} left eye is a {roll(table_eye_color_qualifier)} {eye_left} and {pronoun_poss} rigth eye a {roll(table_eye_color_qualifier)} {eye_right}."
        )

    a = roll_exclusive(table_high_ability, table_low_ability)

    description.append(f"{pronoun} {a[0]} but {a[1]}.".capitalize())
    description.append(
        f"{pronoun} {roll(table_talent)} and {roll(table_mannerism)}.".capitalize()
    )
    description.append(
        f"{pronoun} is {roll(table_frequency)} {roll(table_interactions)}.".capitalize()
    )

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

    description.append(
        f"{pronoun} values {ideal1} and {ideal2} above all else.".capitalize()
    )

    n_bonds = roll(table_multiple_bonds)
    if n_bonds == 1:
        description.append(f"{pronoun} is {roll(table_bond)}.".capitalize())
    else:
        bond1, bond2 = roll_exclusive(table_bond, table_bond)
        description.append(f"{pronoun} is {bond1} and {bond2}.".capitalize())

    description.append(
        f"{pronoun_poss} biggest flaw is {roll(table_flaw)};".capitalize()
    )
    description.append(f"{pronoun_poss} deepest secret is {roll(table_secret)}.")

    # description.append(f"".capitalize())

    return " ".join(description)


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {npc()}\n")
