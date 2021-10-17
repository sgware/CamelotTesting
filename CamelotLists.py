import Location

Items = ["Apple", "Bag", "BlueBook", "BlueCloth", "BlueKey", "BluePotion", "Bottle", "Bread", "ChickenLeg",
         "Coin", "Compass", "Cup", "EvilBook", "GoldBook", "GreenBook", "GreenKey", "GreenPotion", "Hammer",
         "Helmet", "InkandQuill", "JewelKey", "LitTorch", "Lock", "MagnifyingGlass", "OpenScroll", "PurpleBook",
         "PurpleCloth", "PurpleKey", "PurplePotion", "Rags", "RedBook", "RedCloth", "RedKey", "RedPotion",
         "Scroll", "Skull", "SpellBook", "Sword", "Torch"]

Visual_Effects = ["Aura", "Blackflame", "Blood", "Brew", "Campfire", "Death", "Diamond", "Explosion",
                  "Force", "Heart", "Heartbroken", "Magic", "Poison", "Poof", "Resurrection", "Skulls",
                  "Spiralflame", "Wildfire"]

Hair_Color = ["gray", "black", "brown", "red", "blonde"]

Hairstyles_All_Body_Types = ["Long", "Spiky", "Short", "Short_Beard", "Short_Full"]

BodyTypes = ["A", "B", "C", "D", "E", "F", "G", "H"]

Expressions = ["neutral", "happy", "sad", "angry", "disgusted", "scared", "surprised", "asleep"]

Hairsyles_ACEG = ["Ponytail", "Straight"]

Hairsyles_BDFH = ["Mage", "Mage_Beard", "Mage_Full", "Musketeer", "Musketeer_Beard", "Musketeer_Full"]

Outfits_All_Body_Types = ["Bandit", "Beggar", "HeavyArmour", "LightArmour", "Merchant", "Naked",
                          "Noble", "Peasant", "Priest"]

Eyecolor = ["white", "black", "blue", "red", "brown", "green"]

Outfits_ACEG = ["Queen", "Witch"]

Outfits_BDFH = ["King", "Warlock"]

SoundEffects_Actions = [["Clap", "Draw", "Eat", "Hammer", "Lock", "Pocket", "Sheathe", "Unlock",
                        "Unpocket", "Write"], ["1", "4", "1", "4", "1", "1", "1", "1", "1","1","1"]]

SoundEffects_Ambient = [["Forest_Day", "Forest_Night", "Port", "River", "Spooky", "Town_Day", "Town_Night"], ["19", "4", "9", "16", "16", "120", "60"]]

SoundEffects_Characters = [["Attack1", "Attack2", "Cry1", "Cry2", "Death1", "Death2", "EvilLaugh1", "EvilLaugh2",
                           "Hit1", "Hit2", "Laugh1", "Laugh2", "Scream",["1", "1", "6", "3", "2", "2", "1", "2", "1", "1", "2", "3", "3"]]]

SoundEffects_Effects = [["Brew", "DarkMagic", "Fireball", "MixPotion", "Potion", "Spell", "Spell2", "Spell3", ["24", "2", "1", "3", "1", "1", "2", "1"]]]

SoundEffects_Furniture = [["Book", "CloseChest", "CloseDoor1", "CloseDoor2", "Fireplace", "Horse", "OpenChest",
                          "OpenDoor1", "OpenDoor2", "SecretDoor"], ["1", "1", "1", "1", "20", "1", "1", "1", "1", "1"]]

SoundEffects_Music = [["Danger1", "Danger2", "Danger3", "Dramatic", "Explorer", "Grief", "Kingdom", "LivelyMusic",
                      "Ominous", "Peaceful", "Serenade", "Serenity", "Tavern", ["72", "130", "81", "135", "47", "151", "97", "86", "128", "21", "92", "69", "151"]]]

SoundEffects_UI = [["Button", "Error", "Flute1", "Flute2", "Menu"],["1", "2", "2", "3", "1"]]

SoundEffects_UI = ["Button", "Error", "Flute1", "Flute2", "Menu"]

ForestPath = Location.Location({1: "EastEnd", 2: "Well", 3: "Plant", 4: "DirtPile", 6: "WestEnd"}, {}, {5: "PathBlock"})
