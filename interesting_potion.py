from roll import roll


# Source: http://dndspeak.com/2018/09/12/100-interesting-potion-containers/
table_container = [
    ("A sealed gourd.", 1),
    ("A drinking horn.", 1),
    ("A sealed leather pouch, like a cross between a wine skin and a caprison.", 1),
    ("A section of bamboo.", 1),
    (
        "A paralyzed living giant firefly with a bloated potion filled light-up-part that you must squeeze the potion out of.",
        1,
    ),
    ("Pint sized clay jug.", 1),
    ("A sealed stein/tankard", 1),
    ("A (literally) pint-sized portable hole", 1),
    ("A coconut sealed with a cork.", 1),
    ("A wineskin made from a cow’s udder so that four people can drink at once.", 1),
    ("A hollow sword hilt.", 1),
    (
        "A viking-style horned helmet, except both horns are hollow and you can use small bamboo straws to drink from them.",
        1,
    ),
    (
        "A realistic-looking artificial hand which is actually hollow; the thumb is the removable stopper.",
        1,
    ),
    (
        "A very large, leathery leaf, carefully wrapped and tied to preserve the thick liquid within.",
        1,
    ),
    (
        "The upper half of a skull (obviously this one can’t be sealed but could still hold liquid).",
        1,
    ),
    (
        "A long, thin leather bladder with straps specifically designed to be concealed in the sleeve of a cloak and tied to the forearm.",
        1,
    ),
    ("A syringe.", 1),
    (
        "A leather boot that looks like it could fit a human child, but upon closer inspection the boot would have been far too wide for any human foot. A large, cork stopper is where an ankle would have been.",
        1,
    ),
    ("Wine skin / water skin.", 1),
    ("Glass flask.", 1),
    ("Metal flask.", 1),
    ("Tiny metal flask built into a pendant.", 1),
    (
        "A small box enchanted to freeze anything inside it. Potions are frozen into icy popsicles.",
        1,
    ),
    (
        "Fruit that has been soaked in potion until it takes on properties of the potion. Squeeze the juice out to get the potion.",
        1,
    ),
    ("Mason jar.", 1),
    (
        "Wax tube filled with potion & then sealed with more wax, kept in a wooden box to keep them from breaking.",
        1,
    ),
    ("Honey comb filled with potion & then sealed with bee’s wax.", 1),
    ("The hilt of a magic sword.", 1),
    ("A sealed glove so five people can drink at once.", 1),
    ("A watch where the face opens up.", 1),
    ("A flask that looks like a tie.", 1),
    ("A hollowed out crystal.", 1),
    (
        "A completely invisible, nigh-unbreakable flask, stoppered with an ordinary cork. Think a floating sphere of fluid suspended from a cork.",
        1,
    ),
    (
        "The hollowed out canine tooth of a wyvern, with a cloth circle edged with bone acting as its lid.",
        1,
    ),
    (
        "A small and delicate urn made from fired clay. Beautiful artwork covers the surface, and multiple handles jut out from the sides.",
        1,
    ),
    (
        "A sealed steel canister with a button on its bottom. By twisting and pulling the button, an inactive rune of purification activates and transforms any liquids among the container’s contents into nonmagical water.",
        1,
    ),
    (
        "A Sock of Resist Moistening. Though it looks and feels like an ordinary sock, the liquid contained within doesn’t seem to soak through.",
        1,
    ),
    (
        "An elegant scroll case covered in ancient script that looks magical, but to the trained eye just describes how disappointed the creator was with how the case turned out.",
        1,
    ),
    (
        "A jar of small, colorful candies, filled with potion beneath each candy shell.",
        1,
    ),
    (
        "A carved wooden fish with its mouth gripping onto a smaller squid shaped cork.",
        1,
    ),
    ("A conch shell.", 1),
    ("The fingerbone of an ogre.", 1),
    ("An enchanted vial that follows you around.", 1),
    ("A perfume bottle/atomizer to spray the potion as a fine mist.", 1),
    (
        "A glass ball with no opening that must be shattered to release the liquid within.",
        1,
    ),
    (
        "The swollen translucent abdomen of a living wasp-like insect—can be stored with other potions of its kind in a specialized wasp nest. (okay, now I see there’s already an insect on the list.)",
        1,
    ),
    (
        "The potion is reduced to a solid and emulsified into a powdered cube. Requires the addition of water to reconstitute, or dropped into a drink, or simply swallowed.",
        1,
    ),
    (
        "A metal cylinder with indecipherable runes running along the side. It has a tab on the top to pop open and the contents are always fizzy.",
        1,
    ),
    ("A fruit juice box.", 1),
    (
        "A belt of rope holding giant screw-shape seashells stoppered with sealant to stop spillage.",
        1,
    ),
    (
        "A large tulips-like flower, its tips stitched with a fine thread, the petals surprisingly hardy.",
        1,
    ),
    (
        "A miniature cloud that can be stored in a bag or will otherwise follow its owner around.",
        1,
    ),
    (
        "Some kind of coral-like sea creature who when sung to will bloom sponges containing the potion. Can be restored with the right know-how to recreate the potion.",
        1,
    ),
    ("A sturdy pod that needs to be bit into, bitter to the taste.", 1),
    ("A teapot, short and stout. Possibly a child reciting a nursery rhyme.", 1),
    (
        "An elaborate metal samovar, designed to keep the liquid at its ideal temperature. Has a tap and key dispenser and can be hung on the back of an adventurer’s pack.",
        1,
    ),
    (
        "Someone repurposed the tip of a giant scorpion’s tail, hollowing it out and hacking off the stinger’s tip to use it as a makeshift gourd. That said, the tip could still probably be used as a type of injector if need be…",
        1,
    ),
    (
        "A hollow glass bracelet with a nozzle, easy for quick combat use, not so easy to fill, but very handy nevertheless. Need a quick heal? It’s right there on your left wrist, have a sip!",
        1,
    ),
    (
        "A bronze, presumably Dwarvish, gyroscopic bowl. It’s very strange how, with minimal magic, something could be devised that wouldn’t let its contents spill, even without a proper lid! Still, it remains easy to drink from. Simply stop the middle axle from moving and drink away… science these days, am I right?",
        1,
    ),
    (
        "An elaborate steampunk-esque gauntlet with several trigger-activated self injectors. Not too sure what they could be useful for, but perhaps someone skilled enough with mechanics could flip it to inject other things without breaking the interesting piece of work…",
        1,
    ),
    (
        "It looks like a feline skull, but it’s actually just a hollow wooden carving. It has a hole in the top for liquid consumption, and it has a lid so it can be emptied and refilled. The inside is prone to staining, but at least the outside maintains a whitish stained color.",
        1,
    ),
    (
        "There absolutely had to be some sort of druidcraft at play here. No normal bonsai tree would grow hollow, nor would it grow with a resealable top, right? It’s too convenient.",
        1,
    ),
    (
        "Meant to be quick and single-use items, these little orbs of thin glass-like material contain quick dosages, essentially shots of potions. Pop one in the mouth, bite down, spit the shell, move on.",
        1,
    ),
    (
        "These little bags are made from banana leaves stitched together with spider silk, and contain potent poultices. All you need to do is tear the bag open and apply the contents to the skin, then let them work their herbal magic~!",
        1,
    ),
    (
        "A “shake-and-go” bottle, a somewhat normal looking potion bottle with a small capsule on the inside containing other materials. When shaken, the capsule tears, allowing the inner materials to mix with the liquid inside. Perfect for inhalant mixtures, or things that just don’t quite work the same if you get them pre-made.",
        1,
    ),
    (
        "It looks like a child’s toy, a simple stuffed animal. However, the clip on the back says otherwise. Open the teddy bear up to reveal a hidden metal cylinder with holes in it. Shake the bear or move it with enough force, and whatever is inside will mix and spit gas everywhere… Sinister…",
        1,
    ),
    ("A wooden jar, with a small lid. The lid is held down with a leather strap.", 1),
    ("An ornate iron flagon, inscribed with a promise to whoever drinks from it.", 1),
    ("A hollowed out hilt for a sword, where the pommel acts as a stopper.", 1),
    ("A leather waterskin from an animal you don’t recognise.", 1),
    ("A snapped bone from a humanoid, which has been re-purposed into an odd vial.", 1),
    (
        "A palm-sized oak barrel attached to a short length of thin rope in such a way that it can be worn as a necklace.",
        1,
    ),
    (
        "A glass vial that seems to be filled by a black oily liquid, upon uncorking and looking inside the liquid appears red.",
        1,
    ),
    (
        "A beautifully carved red gem on the end of a mages stave, clearly used as a spellcasting focus. This gem is hollow glass filled with a healing potion, which must be broken to use.",
        1,
    ),
    (
        "A rodent preserved through taxidermy, its insides hollowed and cleaned with its mouth acting as the opening. all other orifices are stitched up.",
        1,
    ),
    ("A seemingly unblemished egg.", 1),
    ("A cigar with a label bearing the symbol of the god of life.", 1),
    ("An inhaler. (Similar to jet from Fallout)", 1),
    (
        "A beer bottle resealed with a cork and with rope tied around the top in order to make it easier to carry, or attach to beasts of burden",
        1,
    ),
    ("Eye drops. (Similar to bloody eye in Cowboy Bebop)", 1),
    ("Bandages with a healing salve prepared inside.", 1),
    (
        "A bundle of incense that when broken create a sweet scent that can heal wounds.",
        1,
    ),
    ("A paper tube with a fine, snortable powder inside.", 1),
    (
        "A tiny statue holding a potion bottle that when brought to your mouth pours the potion inside.",
        1,
    ),
    ("Hard candies wrapped individually like butterscotch.", 1),
    ("Soft, waxy, chewy candy that has a potion in the center similar to gushers.", 1),
    (
        "An single use iron brand (like a car cigarette lighter) that feels warm and tingly to the touch",
        1,
    ),
    ("Small pills that look to have been ground and crushed by hand.", 1),
    (
        "A seemingly simple silver hip flask. It actually functions as multiple flasks of holding, each containing a different potion, with access determined by how one opens it. Unscrew the cap to the left, one potion. Unscrew to the right, another potion. Pull straight out, a third. Etc. Unfortunately, the flask is unmarked, and resists all efforts to mark it with directions.",
        1,
    ),
    ("A tiny wooden leg for a three legged dog. The paw can be unstoppered.", 1),
    ("A club, ugly, restrained with iron bands. Has a cork in the top.", 1),
    ("A large edible gelatin ball you could bite into.", 1),
    ("A bread bowl with a cap.", 1),
    ("A large snail shell filled with liquid.", 1),
    ("A water balloon, but filled with a potion.", 1),
    ("A hollowed out piece of rock salt.", 1),
    ("A blown glass bottle that used a dragon’s fire as it’s furnace.", 1),
    ("A hollowed out wooden figure of a dwarf.", 1),
    ("A coconut, which must be smashed to get the potion out.", 1),
    (
        "A glass vial in the shape of a beholder. You drink out of one of the eye-stalks.",
        1,
    ),
]

# Source: http://dndspeak.com/2017/12/100-random-potion-effects/
table_effect = [
    ("You can speak 3 additional languages, chosen by the DM, for 1d10 days.", 1),
    ("Roll on the polymorph table.", 1),
    (
        "You can jump four times as high for 24 hours, also all fall damage you take is divided by four for the duration.",
        1,
    ),
    ("Your WIS increases by 1d4, and INT decreases by 1d4 for 2d12 hours.", 1),
    ("Grow feathers for 1d8 hours.", 1),
    ("An erection lasting more than 4 hours.", 1),
    ("Classic love Potion.", 1),
    (
        "A Potion that if poured on the ground will grow an acre of trees overnight. If drank….. Well that’s unfortunate.",
        1,
    ),
    ("Grows a hideous feature that lasts 1d8 hours (like mandibles).", 1),
    ("You grow a beautiful ginger beard down to your knees.", 1),
    ("You drool uncontrollably for 1d4 hours.", 1),
    (
        "The index finger on your dominant hand start to glow shed bright light in a 20-foot radius and dim light for an additional 20 feet for the next 1d8 hours.",
        1,
    ),
    ("You forget everything that’s happened over the last 2 days.", 1),
    (
        "Two extra arms sprout from your sides and function as normal for 10 minutes. You can use these arms to take a bonus action during combat. After 10 minutes the arms suddenly fall away, lifeless.",
        1,
    ),
    (
        "The potion is a water elemental. Drinking it tastes like the freshest water you’ve ever drank. As soon as you take part in vigorous activity you spawn a water elemental in the same square as you.",
        1,
    ),
    (
        "The potion is Coca-Cola. Describe the sugary taste and fizz, but don’t use the brand name. See if the player figures it out.",
        1,
    ),
    (
        "The potion is clear, with glitter floating in it. Drinking it gives you minty fresh breath, and you don’t need to fart or go to the toilet for 48 hours as your body becomes 100% efficient.",
        1,
    ),
    (
        "The thick yellow potion twists and moves of its own accord. The fluid inside will actively try to avoid being drunk, clinging to the inside of the bottle. It’s actually a Tiny Ochre Jelly.",
        1,
    ),
    (
        "The potion is blood-red with fleshy chunks in it, as through a brain has been put through a blender. Drinking it telegraphs the player’s mood and thoughts to all characters within 30ft for one hour, as if under the Detect Thoughts spell.",
        1,
    ),
    ("You hover 4 inches above the ground for 1d6 hours.", 1),
    ("You gain a mild fear of arrows.", 1),
    ("You grow a third eye in your forehead granting you +2 perception.", 1),
    (
        "Dark green potion : tastes cold and you transform into a lizardmen, permanantly.",
        1,
    ),
    (
        "For the next 2d6 minutes any slippery or sticky surface is treated as normal terrain for you, but any normal terrain is treated as 1d2: 1) Sticky 2) Slippery.",
        1,
    ),
    (
        "When you talk it comes out in gibberish, but to you it sounds perfectly normal.",
        1,
    ),
    (
        "You see that everyone has a slight outline around them, the color ranging from green to red, but you don’t know the meaning. It’s showing you how long since someone has taken a shit, green being recently and red being long ago.",
        1,
    ),
    ("You grow an extra toe on each foot.", 1),
    ("Your hair turns the color of the potion you drank.", 1),
    (
        "Your skin turns green. Reduce your intelligence and increase your strenght by 1d4 for 10 minutes.",
        1,
    ),
    (
        "The drinker must dance until they fall unconscious. They do not know that they must fall unconscious, and will resist all attempts to make them do so.",
        1,
    ),
    (
        "The drinker turns a deep green and can photosynthesize, but must consume dirt and/or fertilizer to do so.",
        1,
    ),
    ("The drinker’s nose is inverted, and sinks into their head.", 1),
    (
        "The drinker restores all their spell slots, but can only use them to cast one spell until the next long rest.",
        1,
    ),
    (
        "The potion contains an unknown acid that passes through flesh and organs without harming them, nor does it stop on anything other than glass. In fact, it will pass through it all except glass and bone, which it dissolves rather painfully. It’s bone hurting juice.",
        1,
    ),
    (
        "The potion restores a lost organ or body part as long as it isn’t larger than an orc’s heart. The restored body part will be partially see-through and assume a foggy white color, however, and phantom pain will still be felt where applicable.",
        1,
    ),
    (
        "The potion is highly addictive (roughly 1 in 4 experienced adventurers fall victim to it), but has no other effects. It can be identified as the Hero’s Flaw by a pharmacist, experienced merchant or local dealer.",
        1,
    ),
    (
        "The potion contains a highly flammable see-through fluid that can explode when intensely moved, dealing 1d4 damage per quarter of a litre around 2 meters (+1 every half a litre). Can be used to create fire or shrapnel based explosives.",
        1,
    ),
    (
        "The potion is empty, someone has painted over the glass with bright blue paint and promptly treated with a Major Illusion spell. Who would waste a spell on something so trivial? Who knows? Not you!",
        1,
    ),
    (
        "You can hover an inch above the ground. Base speed is now 40 feet for 1d4 hours.",
        1,
    ),
    ("You fart loudly every 1d4 minutes (as a free action).", 1),
    (
        "When you speak you hear yourself normal, but everyone else ears you like a dog trying to speak.",
        1,
    ),
    (
        "It’s so bitter that it makes you projectile vomit profusely for 1d4 hours. Disadvantage on stealth checks because of all the sound and tracking checks against you have advantage. Can be weaponized, treat as Acid Splash, 2d6 acid damage.",
        1,
    ),
    (
        "You suffer the outward effects being intoxicated, but your intelligence score is increased by 8 or up to 20 for 1d4 hours. Once the time is up, you recover from all effects and your intelligence reverts.",
        1,
    ),
    (
        "Potion of Equilibrium: For the next 1d4 hours, one random ability score is increased by 6 (no maximum), and one different random ability score is decreased by 6 (no minimum).",
        1,
    ),
    (
        "Potion of Lethargic Levitation: For the next hour, you gain a 10ft flying speed, but lose your walking speed.",
        1,
    ),
    (
        "Potion of Healing (Spoiled): Gain 2d4+4 hit points and gain a randomly chosen condition for 1d4 hours: either poisoned, blinded, or deafened.",
        1,
    ),
    ("Potion of Sentient Clothing.", 1),
    ("Get drunk for 1d6 hours.", 1),
    ("Get Truesight for 1d10 hours, and then pass out for 1d10 hours.", 1),
    ("You are set on fire.", 1),
    (
        "Your body slowly starts to become transparent, and you eventually become completely invisible. Lasts until you get hit.",
        1,
    ),
    (
        "You get flight movement equal to your walking movement, until you get 100ft high.",
        1,
    ),
    ("You get a single wish spell.", 1),
    (
        "You get a single wish spell, except what happens is the exact opposite of what you asked for.",
        1,
    ),
    (
        "Your STR is permanently increased by 1. If it’s already 20, it goes down to 19.",
        1,
    ),
    (
        "The liquid is actually blood. You make a CR 10 WIS or CHA check. On a fail, you throw up.",
        1,
    ),
    (
        "The liquid seems to be normal water. Next time you are targeted by a spell, however, it’s effect is doubled.",
        1,
    ),
    (
        "You feel your skin getting harder. You AC is increased by 3, but your movement speed is halved.",
        1,
    ),
    (
        "Next time you get hit by an undead creature or necrotic spell, you have to make a CR 18 CONS save. On a fail, your body starts to shiver, for no mere mortal can resist the evil of the thriller (You start to become a zombie. The transformation lasts 2d6 days, and can be dispelled by magic, before it’s completed).",
        1,
    ),
    (
        "Your breath is minty fresh for a half hour afterwards, but your stomach turns. You get the feeling you weren’t supposed to swallow it.",
        1,
    ),
    (
        "You immediately unleash the fire breath of a red dragon wyrmling directly in front of you.",
        1,
    ),
    (
        "Gommi Forrest Syrup: A thick, glowing, cyan potion. Tastes like blueberries and honey. Upon drinking, all bodily fluids glow a bright blue, causing them to emit a feint glow for 2d6 days. This glow becomes stronger when bleeding.",
        1,
    ),
    (
        "Catharsis Poison: A deep red, runny potion. Tastes like bad wine. Upon drinking, the drinker will sweat profusely, followed by intense vomiting, crying, urination, and diarrhea for 3d6 minutes. If the drinker survives, they lose all emotional attachment for 2d4 days.",
        1,
    ),
    (
        "Holtven Panacea: A bright gold potion with swirls of pink. Tastes like cherries and sorbet. Upon drinking, all negative conditions are removed, health is restored to full, and any injuries are instantly healed. Extremely expensive.",
        1,
    ),
    (
        "Hathopod Blood: A black potion with flecks of green. Tastes like rotting apples. Upon drinking, gain immunity to all negative effects that would be obtained by a substance entering the body for 1d4 days.",
        1,
    ),
    (
        "Basalisk Tears: A transparent potion. Tastes like saltwater. Casts “Stone to Flesh” when used on a petrified object or person. When used on normal stone, it transmutes in to a random meat.",
        1,
    ),
    (
        "Alchemist’s Cheese: a yellow-white potion so thick it must be heated to be viscous enough to flow. Tastes like normal cheese. Upon consumption, the drinker will vomit various dairy products throughout the day, including milk, cheese, ice cream, and yogurt. The product is from whatever animal was used to make the potion, and is completely edible.",
        1,
    ),
    (
        "Lotus Crystal Solution: A bubbly pink potion. Tastes like sugar and bubble gum. Upon drinking, all ability score improvements are doubled for 1d6 hours. After the 5th time drinking this kind of potion, the drinker will have all stat bonuses halved when not under the effects.",
        1,
    ),
    (
        "Character can only speak in haikus, each haiku must reference a vision of nature in some way (“the sun sets promptly, this dungeon breathes a foul stench, goblins await us”).",
        1,
    ),
    (
        "The potion resembles bubble tea containing 1d10 small tapioca balls. If you chew on the tapioca balls, they turn into little snails or frogs in your mouth",
        1,
    ),
    (
        "Whoever drinks this potion experiences a very vivid daydream from his childhood that leaves him shaken for 1d3 hours.",
        1,
    ),
    (
        "You feel an extraordinary fluency and efficacy in your words and are able express thoughts with great clarity for 1d6 hours.",
        1,
    ),
    (
        "The liquid in this flask appears pearlescent and if you look into it for long enough, you can see ghostly, familiar shapes in its reflection. You forget everything that has happened since you woke up.",
        1,
    ),
    (
        "This potion has a bubbling, bloody texture. You have the sudden urge to go the the privy. You have 10 minutes, after which time you are incapacitated for the next 24 hours, at the end of which you fall unconscious and successfully lay a fertilised egg. The egg takes 1 year to hatch as the dragon wyrmling imprints on you.",
        1,
    ),
    (
        "This potion appears as a silvery, translucent liquid that when drunk, makes your body fall limp as you become a ghostly apparition for an hour.",
        1,
    ),
    (
        "The content of the potion is in fact : a soul! If you try to drink it, you must succeed on a DC 13 charisma saving throw or your soul will be swapped for 1d10 days.",
        1,
    ),
    ("It swaps your gender.", 1),
    ("The drinker is teleported back to the location they found the potion.", 1),
    (
        "The drinker is teleported to the nearest body of fresh water, with a niggling sense they should refill the bottle with it.",
        1,
    ),
    (
        "The drinkers head becomes invisible. They become deaf dumb and mute for 1d4 minutes.",
        1,
    ),
    ("The drinker becomes extremely physically attractive for 1d4 hours.", 1),
    (
        "The drinker has a Scottish accent for 1 hour, and takes 1d4 damage every time the player says something in character without attempting that accent.",
        1,
    ),
    (
        "The potion is slightly viscous and smells of iron. Drinking it causes your entire mouth to fill with a metallic flavour, rendering you unable to smell or taste for 1d4 hours but during that duration, you are immune to ingested poisons.",
        1,
    ),
    (
        "The potions falls upward, defying gravity. Instead of having the expected effect of levitation, the potion leaves you light-headed as it seeps into your brain. -1 on perception and intelligence checks but during that duration, you feel no pain and gain +1 to endurance and strength checks.",
        1,
    ),
    (
        "The potion tastes like the best dessert you ever had, even though it smells like a wet dog. Drinking this potions grants you the benefits of a full day of rations.",
        1,
    ),
    (
        "It’s a blood thinner! For 1 day, you bleed out after getting hit. Take half of the damage done on your first hit and subtract it for all following rounds until you are healed.",
        1,
    ),
    (
        "The potion made you extremely flammable! Stay away from fire or be prepared for things to get lit!",
        1,
    ),
    (
        "It’s a Rage Potion! This potion gives you Rage just like a Barbarian. The bottle contains enough liquid for two drinks.",
        1,
    ),
    (
        "The potion is a heavy mist. On consumption, your skin turns slimy as you gain water-breathing for 1d4 minutes but lose the ability to breathe above water.",
        1,
    ),
    (
        "The bottle contains an addictive poison! When you drink it, it tastes like the worse thing you’ve ever tasted, but then you soon start wanting to take another drink. Each drink causes 1d6 damage, and there is enough on the vial for five drinks.",
        1,
    ),
    ("It was just moonshine! Disadvantage on dexterity checks.", 1),
    ("The vial contains water. Dyed water.", 1),
    (
        "The potion has floating crumbs of copper in it. Drinking it gives a boost to your immunity system, curing you of diseases.",
        1,
    ),
    (
        "The potion has a strong tangy flavour and you feel it course through your body. When it gets to your feet, your shoes/boots melt off.",
        1,
    ),
    (
        "Elixir of Mint: When drink you can exhale a frost breath in a 15 feet cone. Each creature in the area must make a DC13 Constitution save, or take 3d6 cold damage, and half on a success.",
        1,
    ),
    ("Potion of False vigor: When drank, give 2d4+4 temporary life points.", 1),
    (
        "Potion of inner fire: When drank, you feel really hot, and you feel your blood boiling. For the next 6 hour, you become resistant to fire damage, you when you are hit by an attack, every creature 5 feet around you must make a DC12 Dexterity save, or take 1d6 fire damage, and half on a sucess.",
        1,
    ),
    (
        "You begin growing hair all over your body. After 1d4 days all your hair begins to fall out unless you drink more.",
        1,
    ),
    (
        "Cabbage Potion – A potion that transforms it’s drinker in a cabbage. roll a 1d20, thats how many days the person stays a cabbage, on a 20 they become permanently a cabbage. Potion includes telepathy for the cabbage.",
        1,
    ),
    (
        "Your veins seem to rise to the top of your body briefly. They leave dark purple and blue markings across your skin which will remain as tattoos.",
        1,
    ),
]


def main(repeat=0):
    for i in range(repeat - 1):
        print(f"{i + 1}. [{roll(table_container)}] {roll(table_effect)}\n")


if __name__ == "__main__":
    main()
