# Fantasy Generators

Random content generators for fantasy roleplay games.

# Content

- [Fantasy Generators](#fantasy-generators)
- [Content](#content)
- [NPC](#npc)
- [Sources](#sources)
  - [Parsing those lists](#parsing-those-lists)

# NPC

To generate an NPC, simply run:

    python npc.py

The output should look like this:

> Kevennevol Goor is a small and thin a young male human teen. He has braided beard or hair and his eyes are a deep grey. He is insightful but feeble. He enjoys playing the flute and bites fingernails. He is always irritable. He doesn't particularly tend to help others and believes rules are for others. He values discovery and aspiration above all else. He is dedicated to fulfilling a personal life goal. His biggest flaw is being prone to rage; his deepest secret is a shameful or scandalous history.

The names are generated using [jmathes' *names* repo](https://github.com/jmathes/names); it has only been converted to Python 3 and integrated to the current repo (there was no PyPI package).

# Sources

- [Reddit/d100](https://www.reddit.com/r/d100/wiki/finished)

## Parsing those lists

In MS Excel:

    CONCAT("    ('";SUBSTITUTE(B1;LEFT(B1;FIND(". ";B1)+1);"");"', 1),")
