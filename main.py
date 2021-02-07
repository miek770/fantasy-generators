# Standard library
from gooey import Gooey, GooeyParser

# Current module: General
from npc import main as roll_npc
from goblin_unit import main as roll_goblin_unit
from magic_services import main as roll_magic_services

# Current module: Encounters
from city_street_encounter import main as roll_city_street_encounter
from scary_forest_encounter import main as roll_scary_forest_encounter
from beach_encounter import main as roll_beach_encounter
from travel_complication import main as roll_travel_complication
from road_social_encounter import main as roll_road_social_encounter
from tavern_encounter import main as roll_tavern_encounter
from forest_encounter import main as roll_forest_encounter
from sea_travel_events import main as roll_sea_travel_event
from desert_encounter import main as roll_desert_encounter
from interesting_potion import main as roll_interesting_potion
from poison import main as roll_poison
from warm_up_rp_questions import main as roll_warm_up_rp_questions
from failed_info_check import main as roll_failed_info_check
from inn_patron import main as roll_inn_patron
from faction import main as roll_faction
from secret_society import main as roll_secret_society
from god import main as roll_god
from landmark import main as roll_landmark


__title__ = "Fantasy Generators"
__description__ = "Collection of generators for DND5e or similar fantasy RPG games"
__version__ = "0.2.0"


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
        choices=sorted(
            [
                "NPC",
                "Goblin unit",
                "Magic services",
                "City street encounter",
                "Scary forest encounter",
                "Beach encounter",
                "Travel complication",
                "Road social encounter",
                "Tavern encounter",
                "Forest encounter",
                "Sea travel event",
                "Desert encounter",
                "Interesting potion",
                "Poison",
                "Warm up RP questions",
                "Failed info check",
                "Inn patron",
                "Faction",
                "Secret society",
                "God",
                "Landmark",
            ]
        ),
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

    elif args.category == "Beach encounter":
        roll_beach_encounter(args.count)

    elif args.category == "Travel complication":
        roll_travel_complication(args.count)

    elif args.category == "Road social encounter":
        roll_road_social_encounter(args.count)

    elif args.category == "Tavern encounter":
        roll_tavern_encounter(args.count)

    elif args.category == "Forest encounter":
        roll_forest_encounter(args.count)

    elif args.category == "Sea travel event":
        roll_sea_travel_event(args.count)

    elif args.category == "Desert encounter":
        roll_desert_encounter(args.count)

    elif args.category == "Interesting potion":
        roll_interesting_potion(args.count)

    elif args.category == "Poison":
        roll_poison(args.count)

    elif args.category == "Warm up RP questions":
        roll_warm_up_rp_questions(args.count)

    elif args.category == "Failed info check":
        roll_failed_info_check(args.count)

    elif args.category == "Inn patron":
        roll_inn_patron(args.count)

    elif args.category == "Faction":
        roll_faction(args.count)

    elif args.category == "Secret society":
        roll_secret_society(args.count)

    elif args.category == "God":
        roll_god(args.count)

    elif args.category == "Landmark":
        roll_landmark(args.count)


if __name__ == "__main__":
    main()
