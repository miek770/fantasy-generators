# Standard library
from gooey import Gooey, GooeyParser

# Current module: General
from npc import main as roll_npc
from goblin_unit import main as roll_goblin_unit
from magic_services import main as roll_magic_services

# Current module: Encounters
from city_street_encounter import main as roll_city_street_encounter
from scary_forest_encounter import main as roll_scary_forest_encounter


__title__ = "Fantasy Generators"
__description__ = "Collection of generators for DND5e or similar fantasy RPG games"
__version__ = "0.1.0-WiP"


@Gooey(
    program_name=__title__,
    show_success_modal=False,
    menu=[
        {
            "name": "Help",
            "items": [
                {
                    "type": "AboutDialog",
                    "menuTitle": "About",
                    "name": __title__,
                    "description": __description__,
                    "version": __version__,
                    "copyright": "2020",
                    "website": "https://github.com/miek770/fantasy-generators",
                    "developer": "Michel Lavoie",
                    "license": "MIT",
                },
            ],
        },
    ],
)
def main():
    parser = GooeyParser()
    parser.add_argument(
        "-c",
        "--count",
        help="Repeat (if > 1)?",
        action="count",
        default=1,
    )
    parser.add_argument(
        "category",
        default="NPC",
        choices=[
            "NPC",
            "Goblin unit",
            "Magic services",
            "City street encounter",
            "Scary forest encounter",
        ],
    )
    args = parser.parse_args()

    if args.category == "NPC":
        roll_npc(args.count)

    elif args.category == "Goblin unit":
        roll_goblin_unit(args.count)

    elif args.category == "Magic services":
        roll_magic_services(args.count)

    elif args.category == "City street encounter":
        roll_city_street_encounter(args.count)

    elif args.category == "Scary forest encounter":
        roll_scary_forest_encounter(args.count)


if __name__ == "__main__":
    main()
