# PyPI
import click

# Current module
from npc import npc as roll_npc
from goblin_unit import main as roll_goblin_unit


@click.command()
@click.option("--npc/--no-npc")
@click.option("--goblins/--no-goblins")
def main(npc, goblins):
    if npc:
        roll_npc()
    if goblins:
        roll_goblin_unit()


if __name__ == "__main__":
    main()
