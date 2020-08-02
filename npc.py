from random import randint

table_sex = [
    ("male", 1),
    ("female", 1),
]

table_race = [
    ("human", 1),
    ("elf", 1),
    ("half-elf", 1),
    ("dwarf", 1),
    ("half-orc", 1),
    ("thiefling", 1),
    ("dragonborn", 1),
]

table_age_qualifier = [
    ("a young", 1),
    ("a", 1),
    ("an old", 1),
]

table_age = [
    ("child", 1),
    ("teen", 1),
    ("adult", 1),
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
    ("is powerful, brawny, strong as an ox", 1),
    ("is lithe, agile, graceful", 1),
    ("is hardy, hale, healthy", 1),
    ("is studious, learned, inquisitive", 1),
    ("is perceptive, spiritual, insightful", 1),
    ("is persuasive, forceful, born leader", 1),
]

table_low_ability = [
    ("feeble, scrawny", 1),
    ("clumsy, fumbling", 1),
    ("sickly, pale", 1),
    ("dim-witted, slow", 1),
    ("oblivious, absentminded", 1),
    ("dull, boring", 1),
]

table_talent = [
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
]

table_mannerism = [
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
    ("", 1),
]


def expand(table):
    t = []
    for r in table:
        for _ in range(r[1]):
            t.append(r[0])
    return t


def roll(table):
    t = expand(table)
    return t[randint(1, len(t) - 1)]


def roll_exclusive(table1, table2):
    t1 = roll(table1)
    for index1, entry in enumerate(table1):
        if entry[0] == t1:
            break
    while(True):
        t2 = roll(table2)
        for index2, entry in enumerate(table2):
            if entry[0] == t2:
                break
        if index1 != index2:
            return (t1, t2)


def random_npc():
    description = []
    sex = roll(table_sex)
    pronoun = "he" if sex == "male" else "she"
    description.append(f"{pronoun} is {roll(table_age_qualifier)} {sex} {roll(table_race)} {roll(table_age)}.".capitalize())
    description.append(f"{pronoun} {roll(table_appearance)}.".capitalize())
    a = roll_exclusive(table_high_ability, table_low_ability)
    description.append(f"{pronoun} {a[0]} but {a[1]}.".capitalize())
    print(" ".join(description))


if __name__ == "__main__":
    random_npc()