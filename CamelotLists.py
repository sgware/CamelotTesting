import Location
from PlaceReader import parseData

Items = ["Apple", "Bag", "BlueBook", "BlueCloth", "BlueKey", "BluePotion", "Bottle", "Bread", "ChickenLeg",
         "Coin", "Compass", "Cup", "EvilBook", "GoldCup", "GreenBook", "GreenKey", "GreenPotion", "Hammer",
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

Actions_Single = ["Clap", "Die", "Revive", "Drink", "Laugh", "Wave"]
Eyecolor = ["white", "black", "blue", "red", "brown", "green"]

Outfits_ACEG = ["Queen", "Witch"]

Outfits_BDFH = ["King", "Warlock"]

All_Places = ["AlchemyShop", "Blacksmith", "Bridge", "Camp", "CastleBedroom", "CastleCrossroads", "City", "Cottage",
              "Courtyard", "Dining Room", "Dungeon", "Farm", "ForestPath", "GreatHall", "Hallway", "Library", "Port",
              "Ruins", "SpookyPath", "Storage", "Tavern"]

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


locations_list = []
AlchemyShop = parseData("PlaceCSVs\\AlchemyShop.csv", "AlchemyShop")

Bridge = parseData("PlaceCSVs\\Bridge.csv", "Bridge")

Camp = parseData("PlaceCSVs\\Camp.csv", "Camp")

CastleBedroom = parseData("PlaceCSVs\\CastleBedroom.csv", "CastleBedroom")

CastleCrossroads = parseData("PlaceCSVs\\CastleCrossroads.csv", "CastleCrossroads")

City = parseData("PlaceCSVs\\City.csv", "City")

Cottage = parseData("PlaceCSVs\\Cottage.csv", "Cottage")

Courtyard = parseData("PlaceCSVs\\Courtyard.csv", "Courtyard")

DiningRoom = parseData("PlaceCSVs\\DiningRoom.csv", "DiningRoom")

Dungeon = parseData("PlaceCSVs\\Dungeon.csv", "Dungeon")

Farm = parseData("PlaceCSVs\\Farm.csv", "Farm")

ForestPath = parseData("PlaceCSVs\\ForestPath.csv", "ForestPath")

GreatHall = parseData("PlaceCSVs\\GreatHall.csv", "GreatHall")

Hallway = parseData("PlaceCSVs\\Hallway.csv", "Hallway")

Library = parseData("PlaceCSVs\\Library.csv", "Library")

Port = parseData("PlaceCSVs\\Port.csv", "Port")

Ruins = parseData("PlaceCSVs\\Ruins.csv", "Ruins")

SpookyPath = parseData("PlaceCSVs\\SpookyPath.csv", "SpookyPath")

Storage = parseData("PlaceCSVs\\Storage.csv", "Storage")

Tavern = parseData("PlaceCSVs\\Tavern.csv", "Tavern")

locations_list.append(AlchemyShop)
locations_list.append(Bridge)
locations_list.append(Camp)
locations_list.append(CastleBedroom)
locations_list.append(CastleCrossroads)
locations_list.append(City)
locations_list.append(Cottage)
locations_list.append(Courtyard)
locations_list.append(DiningRoom)
locations_list.append(Dungeon)
locations_list.append(Farm)
locations_list.append(ForestPath)
locations_list.append(GreatHall)
locations_list.append(Hallway)
locations_list.append(Library)
locations_list.append(Port)
locations_list.append(Ruins)
locations_list.append(SpookyPath)
locations_list.append(Tavern)





