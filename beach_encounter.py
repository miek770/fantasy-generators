from roll import roll


# Source: http://dndspeak.com/2018/09/100-beach-encounters/
table = [
    (
        "A bearded and rag-draped man scrabbles in the sand. He’s looking for something he lost there. His mind, he says. It would be very bad for the world if he ever found it.",
        1,
    ),
    (
        "Some inhuman sailors and their half-living vessel, washed into this world by aberrant winds. Will barter for supplies with esoteric navigational instruments and the locations of magical anomalies they’ve found here while searching for their route home.",
        1,
    ),
    (
        "A furrow has been dragged into the sand, leading down the mouth of a cave eroded into a low cliff. The furrow’s sides are stained with blood.",
        1,
    ),
    (
        "A derelict ship picked clean by scavengers human and otherwise. Might still be good for firewood, or shelter lurking vermin.",
        1,
    ),
    (
        "Two tiny armies form ranks in the sand and march into battle: one of red crabs climbing from the sea, another of white crabs from the dunegrass up inland. Even a few crabs are no threat to a human, but enough of them might be. If you ignore them they’ll go about their violent business and eventually one side will emerge victorious. If you aid one side against the other, the victors will reward you with cached spoils. Mostly tide-washed junk, but a handful of lost treasures as well. If you attack both sides they’ll band together to fight you.",
        1,
    ),
    (
        "Mud slurries obscenely here. A water elemental and an earth elemental in a forbidden tryst. They’ll offer a modest bribe to get you to forget what you’ve seen, but plot sudden, stalking violence if you try to haggle or refuse. Don’t trust sand or saltwater after you’ve provoked them.",
        1,
    ),
    (
        "A black-clad widow kneels in the surf and weeps for the love she lost at sea. She’ll pay dearly for word that they may yet live, or a smaller but still respectable amount for gossip and alcohol.",
        1,
    ),
    (
        "A gang of urchins pick at the driftwood for anything that could be sold. They’ll work for a pittance and rob you blind in a blink if the opportunity arrives.",
        1,
    ),
    (
        "Some patches of sand here are sunken and pitted with bubbles. Giant, carnivorous clams lurk beneath these. Watch your step, or you might lose a foot to their clamping shells.",
        1,
    ),
    (
        "A whale, wide-eyed with terror, beaches itself before you. It won’t be long now til it dies. The whale’s pursuer waits in the shallows offshore, waves beating at its fins and spines. If the whale is not returned to the water, it will drag its glistening bulk ashore to retrieve it.",
        1,
    ),
    (
        "A mass of imperishable plastic waste from a gone and forgotten civilization. Maybe worth something to a collector of curiousities or an alchemist.",
        1,
    ),
    (
        "A patch of reeds. The sand around it seems recently disturbed. Underneath, a squad of blue-skinned goblins waits for a chance ambush. Their rattling breaths can be heard from the reeds just over the sound of the breeze.",
        1,
    ),
    (
        "A galley and its crew, resting ashore. They’re looking for slaves to replace the ones who died at sea. They’ll pay for prisoners, as well as tips about vulnerable populations, but may try to capture you if you give an impression of weakness. If released the slaves on the galley will split evenly between those who flee and those who try to kill the crew.",
        1,
    ),
    (
        "A marooned man with salt-cracked lips, escaped from exile on a ramshackle raft. He’s near death and deserved worse than marooning for what he did, but he also knows secrets you’ll want.",
        1,
    ),
    (
        "An explorer from a distant land. She’s curious about the region and will report anything you tell her as truth back to her emperor, and in some months time when the full expeditionary fleet arrives they’ll act off that information.",
        1,
    ),
    (
        "The severed tentacle of a sea monster, still grasping on the dying reactions of its ganglionic brain. It will flop after the closest thing generating vibrations (besides the waves), such as by stepping on the sand, and try to crush it. Hard to take on in a straight fight, easy to trick.",
        1,
    ),
    (
        "Someone’s made an elaborate mandala in the sand. If you can step within it without disturbing its lines, you’ll be blessed with peace of mind and rapid healing while they stay there. The mandala will be wiped away when the tide comes in.",
        1,
    ),
    (
        "Off in the distance you can see an approaching black cloud, a buzzing noise rising as it nears. A swarm of sandflies in ravenous frenzy. Too many to fight. Flee, find shelter, or suffer a death of a million little bites.",
        1,
    ),
    (
        "A flock of sirens competing in a singing contest. Passers-by will be pressed into judging the winner. Losers will be furious.",
        1,
    ),
    (
        "You spot something shiny ahead: the handle of a sword jutting up from the sand. There’s not much left beneath that hasn’t rusted to powder. Inscribed on the blade is part of a poem in a language only scholars still speak, florid in its dedication of the sword to a young prince by their father, the king. The sword’s enchantment is as broken as its blade. Where once its cut carried golden light that ate away at wounds, it now inflicts a contagious, blistering radiance.",
        1,
    ),
    (
        "Assorted fish, bloated with eggs, pulled onto land by the parasites which have now grown larger than the fish’s mouths which once held them. The parasites are here to nest, and will protect their broods with maternal ferocity.",
        1,
    ),
    (
        "Some grumpy merfolk lounge a ways offshore. When they spot you they’ll throw insults and rocks, but will disperse if the situation is escalated beyond that or if you can dish out a better insult than theirs’.",
        1,
    ),
    (
        "Several serrated teeth scattered near a bleached, broken jaw. If thrown on the ground these teeth will sprout into fully-grown humanoid remora warriors loyal to whoever threw the teeth. They’ll quickly suffocate on land.",
        1,
    ),
    (
        "A woman overturns rocks in a panic. In the distance angry shouts can be heard. She’s a selkie fleeing a wealthy merchant husband who forbid her from returning to the ocean, unable to find her skin. The husband has roused a mob to drag her back to their house and children. Not much time’s left before the mob arrives.",
        1,
    ),
    (
        "The sand here is a riot of many hues, stained by wild magic. Magic cast while standing on this sand works chaotically. Sleeping on it brings prophetic nightmares. Eating it is mutagenic. All of these properties are preserved even if the sand’s removed from the beach.",
        1,
    ),
    (
        "A boot sunk in to its ankle. It’s within a wide patch of hard-to-distinguish quicksand blocking the path. The boot is of high quality, but otherwise unremarkable.",
        1,
    ),
    (
        "A lighthouse, the light of which is an uncanny green. Its keeper is more than a little mad, and spends all day gathering fireflies and their grubs. At dusk the keeper places his daily catch in a fine-mesh cage at the lighthouse’s top. Each night the fireflies feed on each other, becoming larger, brighter, and crueler. This will not end happily.",
        1,
    ),
    (
        "A Mexican stand-off between three pirates, a recently-unburied chest full of booty in the middle of them.",
        1,
    ),
    (
        "A worn-away wisp of a dryad, clinging to the driftwood which was once her tree. Will try to commit suicide-by-adventurer by convincing them she’s more dangerous than she is to end her agony. If her bluff is called and she’s shuffled gently off this mortal coil, the dryad’s driftwood splits open to reveal a magic seed.",
        1,
    ),
    (
        "A smuggler in a heavy cloak and a rowboat that seems too rotten to float. Direct light will reveal the smuggler’s true, skeletal face. She discovered a treacherous route out of the underworld then decided to continue the profession she followed in life. The dead smuggler offers goods not found among the living, and attempts to rope you into her schemes.",
        1,
    ),
    (
        "The sand in this section of beach is greyish-red, iron-like, magnetically anomalous. Carrying ferrous metal through it can kick up obscuring clouds and rasping sandstorms.",
        1,
    ),
    (
        "A man in a suit of armour sitting on a stone. Not really a man at all, but a knight-crab (like a hermit crab, but bigger, more dangerous, and uses armour instead of shells to house its vulnerable parts) grown a bit too large for its current home and looking to upgrade. Will mimic human behaviour as well as a clever animal can to lure prey closer before it attacks.",
        1,
    ),
    (
        "An idol of verdigrised bronze half-buried in the sand. Time and water have worn away its features to the point that you can’t tell whether it was supposed to look angelic or demonic.",
        1,
    ),
    (
        "Goblins racing wheels and wagons down the slope of the waterline. They won’t let you pass unless you beat them at their own race. Materials for a vehicle will be provided, including: old planks, nails, an inflated pig skin, and very hard melons. Sabotage of other racers is not only allowed, it’s encouraged.",
        1,
    ),
    (
        "A sea-hag crouches in the water, combing tangles from her hair. She’s self-serving, always hungry, and morbidly humourous, but willing to barter fresh flesh and magical objects for her services and charms. The hag will die if her hair ever dries out.",
        1,
    ),
    (
        "A worn leather case containing a smeared and mildewed scroll bobs in the waves. The scroll contains a random spell, but the damage to the scroll will mess with its activation. Maybe it’ll fizzle out, or affect a different target, or even become more powerful.",
        1,
    ),
    (
        "A rusted machine. Its gears turn so slowly that the movement is nearly imperceptible, its ticking seeming perhaps to be your imagination. It will finally wind down in a matter of hours, and when it does it will explode. With tools (or fingers you don’t mind getting pinched off) the gears can be manually re- or unwound. Immersing the machine in water will delay its detonation indefinitely.",
        1,
    ),
    (
        "A shark-man brute leaps from the water, positioning itself so that dazzling, blinding light shines off the surface at its back and into your face. Tries to intimidate its way to a toll of wealth and rations, fights reluctantly.",
        1,
    ),
    (
        "An unhinged wizard rants and raves against the ocean. He seeks allies against it, and will attack anyone who seems to be in league with it (e.g. by sailing upon it, eating its fish, etc.).",
        1,
    ),
    (
        "Hungry beachworms tunnelling below, bulging the sand above their passage. They can’t dig through solid rock, but are fast enough to overtake a running person. The sand above softens any blows against them except for when they lunge or watch periscope-like for prey.",
        1,
    ),
    (
        "Galumphing kelp-freits wielding enormous shell-and-bone scissors. They work to separate the abominable in-betweens of land and sea: amphibians, sailors, seagulls, and so on, with the edge of their scissors if necessary (it’s most often necessary). The kelp-freits try to set up flanks between themselves, so they can combine their scissors to gruesome amputative effect.",
        1,
    ),
    (
        "A drunken giant building an equally giant sandcastle. It’s dangerously oblivious in its scooping and molding, and if pestered will demand you act out its imaginings of what life in a castle is like with the frightened prisoners the giant’s already captured.",
        1,
    ),
    (
        "A big, stoic sandstone face carved into the side of a hill. It will open its mouth to the treasure stashed within only for the person it was carved to resemble. The enchantment on it is rather crude, so a mask painted to look like it, its reflection in a mirror, and the like would all be sufficient to fool the face into opening. Dynamite will also open the face, but risks damaging the treasure within.",
        1,
    ),
    (
        "A discarded coffer full of cursed silver coins. If carried they’ll tarnish any other precious metals you touch, and will return to your possession the night after you spend them. They’ll appear in your mouth if you’ve got no bags or pockets for them.",
        1,
    ),
    (
        "A group of young nobles play polo as their bodyguards watch on. They’re growing bored with their game and eager for new amusements. They nobles unfamiliar with the possibility of their actions having negative consequences. Together their horses and jewelry are worth a small fortune to a discreet buyer who wouldn’t sell you out to the nobles’ parents.",
        1,
    ),
    (
        "A decrepit yacht drifting down the shore. Its undead passengers believe themselves to still be alive and at an upscale party, dancing and drinking from dusty glasses. They’ll get violent if anything disturbs this illusion, and start off assuming any unfamiliar faces are servants. Some durable valuables are still onboard.",
        1,
    ),
    (
        "A storm tears through the area, coming and going in maelstromous moments. Soon after the storm passes, a party of fairies riding albatrosses swoop down and ask which direction their quarry went. If told honestly you’ll wake up some days later with a bottle of lightning by your head. If they’re lied to you’ll find yourself caught in a deluge every time you try to sleep outside for the next month.",
        1,
    ),
    (
        "A spattering of holes and the goblins digging them. They’ve got a waterlogged treasure map, the ink too smudged to read clearly, and are digging all over the approximate area of where “X” marked the spot.",
        1,
    ),
    (
        "A collection of jars, some shattered, some whole, all caught in some muck. Within them is some goo. Drinking the goo inflicts a piscine mutation: gills, bulging eyes, legs fused into fins, skin turned to scales, and so on. Each jar’s goo inflicts a single mutation.",
        1,
    ),
    ("An estuary where crocodiles lurk.", 1),
    (
        "A basket bobbing in the sea foam. Within is a wailing baby, several items of golden jewelry, and a note. The note explains that the baby is the youngest son of a king, sent downriver to escape the murderous attention of the crown prince. It further implores its reader to raise the baby well, take the jewelry as payment (though leaving one piece as a keepsake), and some day tell them of their royal heritage and duty to overthrow their tyrannous sibling.",
        1,
    ),
    (
        "An impromptu bazaar halfway in the water. Merchants from land and sea have gathered here to trade goods only found in their respective environs.",
        1,
    ),
    (
        "A holy oil spill shimmering on top of the water. It’ll still be potent if bottled. In the center of the spill a ghoul shivers atop a raft and cries for help.",
        1,
    ),
    (
        "A crate of wax-sealed amphora full of wine that’s soured to vinegar. One of the amphora, painted with sharks instead of dolphins, is packed with cocaine or something similar.",
        1,
    ),
    (
        "The way down the beach here is craggy, with rough waters slamming rougher rocks hemming in one side and a sheer cliff the other. The crags ahead are home to giant barnacles, glued in place but able to lash out at intruders with their tremendous penises.",
        1,
    ),
    ("Some fishermen gambling around a barbecue pit.", 1),
    (
        "The sand here is full of sharp shards of rock and glass, cutting feet like caltrops if walked on. Goblins on stilts with bows and pikes are patrolling the area.",
        1,
    ),
    (
        "Coral mounds dot this place and strange fish swim through the air. This is the ghost of an ancient reef now on land by the long movement of geology, lost in the memory of life. The ghostly animals behave as they would while alive, including attacking when hungry or provoked.",
        1,
    ),
    (
        "Someone’s drowning, caught in a riptide. If rescued they’ll be grateful, but don’t have much to offer besides their service.",
        1,
    ),
    (
        "A friendly horse trots up the beach to you. It’s a kelpie in disguise. If touched you’ll stick to it and it’ll gallop into the water.",
        1,
    ),
    ("A floating dock that trails out to a prime fishing spot.", 1),
    (
        "A fresh shipwreck. There’s a three-way argument between some human scavengers, goblins, and fish-men as to how to split the spoils. They haven’t come to blows yet, but they’re close.",
        1,
    ),
    (
        "A desiccated ocean chimera (eel for a tail, heads from a turtle, a pufferfish, and a seahorse, body like all four mashed together, breathes gouts of inky venom) placed above the high tide line. Contact with water will restore it instantly to lively hostility.",
        1,
    ),
    (
        "A dire cormorant snacking on a splatter of dead fish washed ashore by a swell. Protective of its food but otherwise placid. Tameable.",
        1,
    ),
    (
        "A party of adventurers like yourself, all naked and quite deranged from sun exposure and drinking seawater. If kept calm will tell confusing fragments of how they arrived at their current state.",
        1,
    ),
    (
        "Colourful, frilly seaslug-men crowd around you and probe with soft appendages, babbling all the while. They’re tourists from the undersea realms. Curious about you, but unable to speak your language, and assume their gesticulations are more comprehensible than they are. At the first sign of violence they’ll vomit their guts out and crawl over each other to get back in the ocean.",
        1,
    ),
    (
        "A sea stack engraved with abstract images. On moonless nights a coven of witches convenes to dance atop it with an octopoid demon, the master they’re sworn to.",
        1,
    ),
    (
        "A salt evaporation pond. People from a nearby village sing work songs as they dredge the salt.",
        1,
    ),
    (
        "An abandoned, algae-encrusted net. Entangled in it is a fish-bitten revenant on a quest to avenge its own murder, stymied by the fact that its hands and tongue have been eaten off.",
        1,
    ),
    (
        "Gems ground to dust have been mixed into the sand here, glittering in ruby and sapphire hues. It’d be valuable but time consuming to sift it out here, but this risks attracting the attention of wandering monsters. The mixed sand could be packed up to be sifted elsewhere, but the ratio of sand-to-gem-dust could make it prohibitively heavy.",
        1,
    ),
    (
        "A lifelike, gently smiling statue carved from salt, up to its knees in the sand. Those within the statue’s field of view (if its eyes could see) receive a penalty to their ability to resist outside influences on their mind.",
        1,
    ),
    (
        "A fishing ogre with waves lapping at its shins. The ogre is currently distracted wrestling with a shark that’s bitten its line.",
        1,
    ),
    ("A lightly sleeping lion-naga basking on the sun-warmed sand.", 1),
    (
        "Something golden glints in shallow water. It’s treasure, being used as a lure by fish-men. They’ll attack if you blunder into their environment.",
        1,
    ),
    (
        "A lone mermaid, swimming down the beach from the opposite direction as you. Gives a wave, then goes on her way.",
        1,
    ),
    (
        "The sea foam’s piled ashore here over your head, and widely enough that you can’t easily walk around it. Easy enough to push through it, but you can’t see in it past your nose. Something’s hiding in the foam, waiting for prey to wander in.",
        1,
    ),
    (
        "A shrine to a maritime deity, shells and ribbons laid at its idol’s feet. A tired, old, snappy priestess and her bored apprentice live in a shack nearby and maintain the shrine.",
        1,
    ),
    ("Goblins training gulls to shit in peoples’ eyes.", 1),
    (
        "A red tide laps at the shore. It’s infested with vampiric, symbiotic algae. A gaggle of infested people (evident by their crimson eyes and veins) are bathing in the stuff. They try to ply you with drugs and good company to offer up some blood (any sort will do), and become increasingly agitated if you do not. Their preferred mode of attack is to spike the dose of whatever they can get you to take with a sedative and drain you while you’re passed out.",
        1,
    ),
    (
        "A sea turtle nesting site. You’ve arrived at just the right time to see the mass hatching. Predators will be gathering soon to pick off the baby turtles before they reach the water. Maybe you’ll be joining them.",
        1,
    ),
    (
        "A sudden fog rolls in. Vague lights can be seen through it. Lanterns? Will-o’-wisps? Lures? Perhaps it’s better to avoid them than investigate.",
        1,
    ),
    (
        "A burial at sea. Mourners place treasures on the boat of their chief, then set it ablaze. It’ll sink some distance out. Polite observers will be invited to join the festivities to follow.",
        1,
    ),
    (
        "An execution. The offender is being buried up to their head below the high tide line. Someone in the gathered crowd is being held back, screaming that the one being buried has been falsely charged. By law they’ve got until the tide comes in to prove it.",
        1,
    ),
    ("A retreat of mystics contemplating the mysteries of the ocean.", 1),
    (
        "The tower of a heretical astrologer attempting to capture the moon and stars in their reflection off the water.",
        1,
    ),
    (
        "A floating hull overcome with lead-grey fungus, its crew dead by a saprophytic plague they picked up on distant shores. Some immature sprouting stalks already release thin streams of spores. If not burned or otherwise disposed of the hulk might fully fruit and infest the whole region.",
        1,
    ),
    (
        "The sand here is spongy, grey, mercury-infused. The fumes rising off it can induce delusions. Some goblins who think themselves human are already here huffing the stuff.",
        1,
    ),
    (
        "A tide pool with a sheepishly dying merman stuck in it. Needs some convincing that surviving is worth the embarrassment of his situation, but will vouch for you to other his underwater allies if rescued.",
        1,
    ),
    (
        "A nuckalavee charges from the surf. A tireless pursuer, but can’t cross freshwater.",
        1,
    ),
    (
        "A resplendent coconut palm held sacred by local people. They know, but don’t speak openly of, a ritual by which you can remove an evil presence from someone’s mind (possession, madness, domination, enchantment, etc.) by trepanning them, drilling to the core of a coconut from the sacred palm, and placing the holes together to draw the evil presence from their head and into the coconut. Trees grown from coconuts used in the ritual are twisted things, bearing the mark of the evil they contained.",
        1,
    ),
    (
        "A group clad in immaculate white robes, browbeating some reluctant few members into following them willingly into the ocean. Apparently a suicide cult. Non-members are proselytized to, and asked not to interfere.",
        1,
    ),
    (
        "A dwindling iceberg-fortress run aground too far south by unfavourable currents. Its garrison of snow elves are paranoid towards outsiders but desperate for direction to a colder place. It’s a toss-up as to which sentiment will win out.",
        1,
    ),
    (
        "A self-crewed golem-ship in need of a captain. Willing to kidnap someone to serve the role.",
        1,
    ),
    (
        "The secret dockyards of a nearby nation, where they’re developing experimental ships. Its guards will be aware of your perimeter breach (though not your exact position) and on high alert.",
        1,
    ),
    (
        "A fisher-monk stands posed upon a rock in impossible stillness, wielding a barbed harpoon. He waits for the vanishingly rare rainbow-urchin to pass by, a creature with spines of light of every hue and shade. When he spots it he’ll strike with unerring precision. If interrupted before then the monk will be incomprehensibly salty.",
        1,
    ),
    (
        "Sargasso spreads before you, from the beach to the distant horizon. Everything you’ve ever lost beckons from its green tangles. This is a portal to the Sargassium, a world where all things can be found again, or where you too might be lost forever.",
        1,
    ),
    ("The water withdraws, the horizon swells. A tidal wave is coming.", 1),
    (
        "A fish-man flags you down, says they were supposed to meet with a representative from a nearby village to discuss trade agreements, tribute, and breeding rights. As that representative is late, the fish-man explains, you will have to do. Some time in to the negotiation (or fighting, or whatever else) the representative will arrive and react to you based on how you’ve argued for the village’s interests.",
        1,
    ),
    (
        "You glimpse a howling whirlpool and waltzing waterspouts a long way from the shore. The visible surface signs of the weapons of an underwater war.",
        1,
    ),
    (
        "While walking along on the sand, you suddenly look down and see a turtle crawling toward you. You reach down and flip it over onto its back. The turtle lies there, its belly baking in the hot sun, beating its flippers, trying to turn itself over, but it cannot do so without your help. You are not helping. Why?",
        1,
    ),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. {roll(table)}\n")


if __name__ == "__main__":
    main()
