import Location

Items = ["Apple", "Bag", "BlueBook", "BlueCloth", "BlueKey", "BluePotion", "Bottle", "Bread", "ChickenLeg",
         "Coin", "Compass", "Cup", "EvilBook", "GoldBook", "GreenBook", "GreenKey", "GreenPotion", "Hammer",
         "Helmet", "InkandQuill", "JewelKey", "LitTorch", "Lock", "MagnifyingGlass", "OpenScroll", "PurpleBook",
         "PurpleCloth", "PurpleKey", "PurplePotion", "Rags", "RedBook", "RedCloth", "RedKey", "RedPotion",
         "Scroll", "Skull", "SpellBook", "Sword", "Torch"]

Visual_Effects = ["Aura", "Blackflame", "Blood", "Brew", "Campfire", "Death", "Diamond", "Explosion",
                  "Force", "Heart", "Heartbroken", "Magic", "Poison", "Poof", "Resurrection", "Skulls",
                  "Spiralflame", "Wildfire"]

Icons = ["arrest", "draw", "drink", "exit", "forge", "kneel", "listen", "lockpick", "research", "swords", "talk",
         "unlock", "usekey", "armour", "beard", "boot", "crown", "dress", "gloves", "helm", "paintbrush", "palette",
         "sewing", "brokenheart", "charm", "firespell", "hurt", "skull", "snowflake", "star", "bed", "cauldron", "chair",
         "chest", "door", "fireplace", "lockedchest", "lockeddoor", "plant", "target", "throne", "well", "woodendoor",
         "apple", "book", "bookshelf", "bread", "chickenleg", "coins", "darkmagic", "evilbook", "flask", "flower",
         "healingpotion", "ink", "key", "lovepotion", "magnifyingglass", "openscroll", "padlock", "poison", "potion",
         "present", "ring", "scroll", "sword", "torch", "woodpile", "cancel", "checkmark", "dice_five", "dice_four",
         "dice_one", "dice_six", "dice_three", "dice_two", "fist", "hand", "hourglass", "meal", "music", "return",
         "sleep", "snake", "sunrise", "time", "tree", "anvil", "bridge", "campfire", "castle", "city", "cottage",
         "dungeon", "forest", "mug", "ship", "shopsign", "stonepath"]


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

ForestPath = Location.Location("ForestPath", ["EastEnd", "Well", "Plant", "DirtPile", "PathBlock", "WestEnd"],
                               [None, None, None, None, None, None],
                               [None, None, None, None, "PathBlock", None],
                               ["EastEnd", "WestEnd"])

Farm = Location.Location("Farm", ["Exit", "Haypiles", None, "Anvil", "Door", "Well"],
                         [None, None, None, ["Surface"], ["Can Open and Close"], None],
                         [None, "Haypiles", None, None, None, None],
                         ["Exit", "Door"])

SpookyPath = Location.Location("SpookyPath", ["WestEnd", "DirtPile", "Plant", "Well", "PathBlock", "EastEnd"],
                               [None, None, None, None, None, None],
                               [None, None, None, None, "PathBlock", None],
                               ["WestEnd", "EastEnd"])


