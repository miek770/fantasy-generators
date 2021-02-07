from roll import roll


# Source: http://dndspeak.com/2019/03/05/100-warm-up-roleplaying-questions-for-players/
table = [
    ("If your character wasn’t an adventurer, what livelihood would they lead?", 1),
    ("Who in the party would your character trust the most with their life?", 1),
    ("What are your character’s core moral beliefs?", 1),
    ("What relationship does your character have with their parents and siblings?", 1),
    ("Does your character have any biases for or against certain races?", 1),
    ("What is your character’s opinion on nobility? On authority?", 1),
    (
        "Describe your character’s current appearance: clothes, armor, scars they’ve picked up along the journey, etc.",
        1,
    ),
    (
        "What location encountered in the campaign has your character felt the most “at home” in, or just generally liked the most?",
        1,
    ),
    (
        "What deity, if any, does your character worship? What’s their opinion on other people’s worship?",
        1,
    ),
    (
        "If your character had time to pick up any artisan’s tools, game set, instrument, etc., what would it be?",
        1,
    ),
    (
        "Describe your character’s current relationship with the player character sitting to your right.",
        1,
    ),
    ("What is your character’s current goal, summed up in one sentence?", 1),
    (
        "Does your character ever want to “settle down” with a spouse, children, house, etc.?",
        1,
    ),
    ("Has your character ever been in love?", 1),
    ("What battle in the campaign has been most memorable to your character?", 1),
    (
        "If your character wasn’t whatever class they are, what would they be instead?",
        1,
    ),
    ("What is your character’s favorite season?", 1),
    (
        "What would your character’s Zodiac sign be, following stereotypical astrology?",
        1,
    ),
    ("Where in the world does your character most want to visit?", 1),
    ("What is the biggest mistake your character has ever made?", 1),
    (
        "Does your character have any noticeable scars? If so, what are their stories?",
        1,
    ),
    ("What animal best represents your character?", 1),
    (
        "If your character could go back in time and change one thing about their life, what would it be?",
        1,
    ),
    (
        "Which other player character does your character find themselves having the most in common with?",
        1,
    ),
    ("Does your character regret any particular choice the party has made?", 1),
    ("What would your character say their best trait would be?", 1),
    ("What is your character’s greatest fear? Deep, irrational?", 1),
    ("What is currently motivating your character to stay with the party?", 1),
    ("What are your character’s hobbies and interests outside of their class?", 1),
    ("What would most people think when they first see your character?", 1),
    (
        "What stereotypical group role does your character play in the party? (The Mom, the Mess, the Comic Relief, etc. Optionally: What role would your character play in the “Five Man Band” structure?)",
        1,
    ),
    ("What is your character the most insecure about?", 1),
    ("What person does your character admire most?", 1),
    (
        "What does your character admire and dislike the most about the player character sitting to your left?",
        1,
    ),
    (
        "Why is your character’s lowest stat their lowest (the in-character reason, not “because there’s no reason for a wizard to have 16 strength, duh”)?",
        1,
    ),
    (
        "What would be your character’s theme song/favorite band/favorite genre of music?",
        1,
    ),
    (
        "What stereotypical role would your character play in a high school AU/if they attended a normal high school? (Nerd, jock, bully, goth, etc.)",
        1,
    ),
    (
        "What treasure/item/artifact that your character has collected during the adventure is the most important to them?",
        1,
    ),
    (
        "Is there any particular weapon, item, etc. that your character longs to find?",
        1,
    ),
    ("Where does your character feel the most at home?", 1),
    (
        "Does your character care about how they’re perceived by others? How do they change themselves to fit in with other people?",
        1,
    ),
    ("What does your character think is the true meaning of life?", 1),
    (
        "What is your character’s scent? (Bonus points for a description that sounds like it could be from a bad [or awesome] fanfic.)",
        1,
    ),
    ("Does your character think more with their heart or their brain?", 1),
    ("What is your character’s most recent or frequent nightmare?", 1),
    (
        "What opinion does your character have on [CERTAIN ESTABLISHED GROUPS/AUTHORITIES IN THE GAME WORLD]? (Dragonmarked Houses, royal crown, etc.)",
        1,
    ),
    (
        "How did your character spend their childhood? Where did they grow up/who were their childhood friends?",
        1,
    ),
    (
        "What aspect of your character’s future are they most curious about? (If they could know one thing about the future, what would it be?)",
        1,
    ),
    ("What colors are associated with your character?", 1),
    (
        "Who in the party would your character prioritize rescuing, in dire circumstances?",
        1,
    ),
    ("Is your character the most swayed by ethos, pathos, or logos?", 1),
    (
        "If your character was granted a single use of Wish, what would they use it for?",
        1,
    ),
    (
        "What is your character’s favorite spell? If they don’t use spells: what is their favorite personal weapon/combat maneuver/skill/etc.?",
        1,
    ),
    (
        "How does your character feel about keeping secrets from the rest of the party?",
        1,
    ),
    ("What type of creature in the world is your character the most intrigued by?", 1),
    (
        "When they were a child, what did your character want to be, or think they were going to be, when they grew up?",
        1,
    ),
    (
        "The player character to your left admits that they’re passionately in love with your character. How would your character respond?",
        1,
    ),
    (
        "If somebody (an NPC, someone from their backstory, etc.) your character trusts/loves asked your character to do something against the party’s best interest, who would they side with?",
        1,
    ),
    ("Does your character value their own best interest more than the party’s?", 1),
    (
        "What decision would the party have to make in order for your character to consider splitting off from the group?",
        1,
    ),
    ("How does your character imagine the way they will die?", 1),
    ("What is your character’s greatest achievement?", 1),
    (
        "Is your character willing to risk the well-being of others in order to achieve their goal?",
        1,
    ),
    ("What is your character’s opinion on killing others?", 1),
    ("What is your character’s favorite food? Beverage?", 1),
    ("How generous is your character? Especially to those they don’t know?", 1),
    (
        "What is your character the most envious about, regarding anyone in the party?",
        1,
    ),
    (
        "The player character to your left and the player character to your right are both telling your character two different versions of the truth. Who does your character believe?",
        1,
    ),
    ("What is your character’s sexuality/relationship with sex?", 1),
    ("What is your character’s biggest pet peeve?", 1),
    (
        "Describe how your character feels about the party’s current situation/objective/etc.",
        1,
    ),
    (
        "Who in the party would your character trust the most to keep an important secret?",
        1,
    ),
    (
        "If your character knew that they were going to die in a month, how would they spend the rest of their life?",
        1,
    ),
    ("What makes your character feel safe?", 1),
    (
        "If your character had the chance to rename the party/give the party a name, no questions asked, what would it be?",
        1,
    ),
    ("What memory does your character want to forget the most?", 1),
    (
        "If your character had to multiclass into a class they currently aren’t the next time they level up, what would it be and what reason would they have for doing so?",
        1,
    ),
    (
        "What television/book/video game/etc. character would your character be best friends with? (Or: what media character is your character the most influenced by/similar to?",
        1,
    ),
    ("What unusual talents does your character possess?", 1),
    (
        "How does your character feel about receiving/giving orders? Are they more of a leader, or a follower?",
        1,
    ),
    (
        "What does your character’s name represent to them? (Or: why as a player did you choose your character’s name?)",
        1,
    ),
    ("Is your character more of an introvert, or an extrovert?", 1),
    (
        "How far is your character willing to go to pursue the “greater good”? Do they believe in a greater good at all?",
        1,
    ),
    ("What does your character want to be remembered by?", 1),
    ("What would be your character’s major in college?", 1),
    ("Does your character consider themselves a hero, villain, or something else?", 1),
    ("What major arcana tarot card best represents your character?", 1),
    ("Where does your character see themselves in 20 years?", 1),
    (
        "What is your character’s relationship with magic? Are they scared of it, wish to know more about it, indifferent to it?",
        1,
    ),
    ("Who is your character’s biggest rival?", 1),
    ("What is your character’s guiltiest pleasure?", 1),
    ("What does your character hope for the afterlife?", 1),
    ("Who in the party does your character trust the least?", 1),
    ("What is your character’s biggest flaw?", 1),
    ("How did your character learn the languages that they speak?", 1),
    ("What is your character’s favorite school of magic/type of weaponry?", 1),
    ("What is most important to your character: health, wealth, or happiness?", 1),
    ("What advice would your character give to a younger version of themselves?", 1),
    (
        "Are there any social or political issues your character feels strongly about?",
        1,
    ),
    ("What, currently, is your character the most curious about?", 1),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {roll(table)}\n")


if __name__ == "__main__":
    main()
