# Fantasy Generators

Random content generators for fantasy roleplay games.

>The project is being migrated to `uv` (WiP).

## Usage

Run with:

    uv run main.py

## Sources

- The names are generated using [jmathes' *names* repo](https://github.com/jmathes/names); it has only been converted to Python 3 and integrated to the current repo (there was no PyPI package).
- Other tables are inspired by or extracted from [Reddit/d100](https://www.reddit.com/r/d100/wiki/finished).

### Parsing [Reddit/d100](https://www.reddit.com/r/d100/wiki/finished) lists

In MS Excel:

    CONCAT("    ('";SUBSTITUTE(A1;LEFT(A1;FIND(". ";A1)+1);"");"', 1),")
