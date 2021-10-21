import CamelotLists
from tkinter import *
from tkinter import ttk
import Location

# sets the root for the testing window
root = Tk()
root.title('Camelot Testing Environment')

cottage_locations = ["Door", "Bed", "Chair", "Table", "Shelf", "Bookshelf", "Chest"]


class TestingGui:
    def __init__(self, master):
        self.focusCharacter = "BobB"
        self.characters = ['BobA', 'BobB', 'BobC', 'BobD', 'BobE', 'BobF', 'BobG', 'BobH']
        self.locationName = "BobsHouse"
        self.characterList = list()
        self.characterList.append("BobB")
        self.trashList = list()
        self.trash = "Trashcan"
        self.currentFocusMode = ""
        self.waitTime = .5
        self.isInputEnabled = False

        self.partialTestingButton = Button(master, text="Partial Testing",
                                           command=lambda: self.createPartialTestingWindow(root))

        self.myButton = Button(master, text="Run Command", command=self.get_input)
        self.clearButton = Button(master, text="Clear", command=self.clear_output)
        self.commandBox = Text(master, height=5, width=40)
        self.outputBox = Text(master, height=12, width=40)

        # self.items_button = Button(master, text="Items", command=self.items)
        # self.visual_effects_button = Button(master, text="Visual Effects", command=self.visual_effects)
        self.run_aroundButton = Button(master, text="Run Around", command=self.test)
        # self.all_clothingButton = Button(master, text="All Clothing", command=self.all_clothing)
        #self.inputButton = Button(master, text="Allow input", command=self.inputEnable)
        # self.defaultButton = Button(master, text="Default", command=self.test)
        self.soundButton = Button(master, text="Play sound", command=self.play_sound)
        self.forest_button = Button(master, text="Forest Path Test",
                                    command=lambda: self.test_Place(CamelotLists.ForestPath))
        self.farm_button = Button(master, text="Farm Test",
                                  command=lambda: self.test_Place(CamelotLists.Farm))
        self.spooky_path_button = Button(master, text="Spooky Path Test",
                                         command=lambda: self.test_Place(CamelotLists.SpookyPath))
        self.iconsWindow = Button(master, text="Icons", command=self.test_icons)

        self.commandBox.pack()
        self.myButton.pack()
        self.outputBox.pack()
        self.clearButton.pack()
        self.run_aroundButton.pack()
        #self.inputButton.pack()
        #self.defaultButton.pack()
        #self.forest_button.pack()
        #self.forest_manual_button.pack()
        #self.partialTestingButton.pack()
        self.soundButton.pack()
        self.forest_button.pack()
        self.farm_button.pack()
        self.spooky_path_button.pack()
        self.iconsWindow.pack()


        self.initialize()

    def createManualWindow(self, master):
        manualwindow = Toplevel(master)
        manualwindow.title("Manual Experience Manager")
        manualwindow.geometry("300x300")

        manualwindow.mainloop()

    def test_Place(self, place: Location.Location):
        self.action("SetCameraMode(track)")
        self.action(self.create_command(["CreatePlace", place.title, place.title]))
        command_list = ['SetPosition', self.focusCharacter, place.title]
        self.action(self.create_command(command_list))
        command_list = ['SetClothing', self.focusCharacter, "Bandit"]
        self.action(self.create_command(command_list))
        for location in place.locs:
            print("place: " + str(place.locs[0]))
            if location[0] is not None:
                command_list = ['WalkTo', self.focusCharacter, place.title + "." + location[0]]
                self.action(self.create_command(command_list))
                self.action('Wait(2)')
            if location[1] is not None:
                for attr in location[1]:
                    if attr == "Surface":
                        command_list = ['CreateItem', CamelotLists.Items[1], CamelotLists.Items[1]]
                        self.action(self.create_command(command_list))
                        command_list = ['Put', self.focusCharacter, CamelotLists.Items[1],
                                        place.title + "." + location[0]]
                        self.action(self.create_command(command_list))
                    if attr == "Can Open and Close":
                        command_list = ['OpenFurniture', self.focusCharacter, place.title + "." + location[0]]
                        self.action(self.create_command(command_list))
                        command_list = ['CloseFurniture', self.focusCharacter, place.title + "." + location[0]]
                        self.action(self.create_command(command_list))
        for portal in place.exits:
            command_list = ['WalkTo', self.focusCharacter, place.title + "." + portal]
            self.action(self.create_command(command_list))
            self.action(self.create_command(["Exit", self.focusCharacter, place.title + "." + portal]))
            self.action(self.create_command(["Enter", self.focusCharacter, place.title + "." + portal]))

    def all_clothing(self):
        oldcharacter = self.focusCharacter
        # self.action('SetCameraMode(track)')
        for i in self.characters:
            self.characterList.append(i)
            command_list = ['CreateCharacter', i, i[-1]]
            self.action(self.create_command(command_list))
            command_list = ['SetPosition', i, self.locationName]
            self.action(self.create_command(command_list))
            command_list = ['SetCameraFocus', i]
            self.action(self.create_command(command_list))
            self.focusCharacter = i
            command_list = ['SetPosition', oldcharacter]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')
            for j in CamelotLists.Outfits_All_Body_Types:
                command_list = ['SetClothing', i, j]
                self.action(self.create_command(command_list))
                self.action('Wait(.5)')
            command_list = ['SetClothing', i]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')
            if i[-1] in ['A', 'C', 'E', 'G']:
                for k in CamelotLists.Outfits_ACEG:
                    command_list = ['SetClothing', i, k]
                    self.action(self.create_command(command_list))
                    self.action('Wait(.5)')
            if i[-1] in ['B', 'D', 'F', 'H']:
                for m in CamelotLists.Outfits_BDFH:
                    command_list = ['SetClothing', i, m]
                    self.action(self.create_command(command_list))
                    self.action('Wait(.5)')
            oldcharacter = i

    def inputEnable(self):
        if self.isInputEnabled:
            self.action('DisableInput()')
            self.isInputEnabled = False
        else:
            self.action('EnableInput()')
            self.isInputEnabled = True

    def clothing(self):
        for i in CamelotLists.Outfits_All_Body_Types:
            command_list = ['SetClothing', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.test2()

    def hair_style(self):
        for i in CamelotLists.Hairstyles_All_Body_Types:
            command_list = ['SetHairStyle', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')

    def eye_color(self):
        for i in CamelotLists.Eyecolor:
            command_list = ['SetEyeColor', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')

    def default(self):
        # command_list = ['SetCameraMode', focus]
        # self.action(self.create_command(command_list))
        command_list = ['SetPosition', self.focusCharacter, self.locationName]
        self.action(self.create_command(command_list))
        command_list = ['SetClothing', self.focusCharacter]
        self.action(self.create_command(command_list))
        command_list = ['SetHairStyle', self.focusCharacter]
        self.action(self.create_command(command_list))
        command_list = ['SetEyeColor', self.focusCharacter]
        self.action(self.create_command(command_list))
        command_list = ['SetHairColor', self.focusCharacter]
        self.action(self.create_command(command_list))
        command_list = ['SetSkinColor', self.focusCharacter, str(0)]
        self.action(self.create_command(command_list))

    def hair_color(self):
        for i in CamelotLists.Hair_Color:
            command_list = ['SetHairColor', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')

    def skin_color(self):
        for i in range(10):
            command_list = ['SetSkinColor', self.focusCharacter, str(i)]
            self.action(self.create_command(command_list))
            self.action('Wait(.5)')

    def items(self):
        for i in CamelotLists.Items:
            command_list = ['CreateItem', i, i]
            self.action(self.create_command(command_list))
            command_list = ['SetPosition', i, self.focusCharacter]
            self.action(self.create_command(command_list))
            self.action('Wait(.75)')
            command_list = ['Pocket', self.focusCharacter, i]
            self.action(self.create_command(command_list))

    def visual_effects(self):
        for i in CamelotLists.Visual_Effects:
            command_list = ['CreateEffect', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.action('Wait(1)')

    def clear_output(self):
        self.outputBox.delete('1.0', END)

    def get_input(self):
        input = self.commandBox.get("1.0", 'end-1c')
        self.action(input)
        self.commandBox.delete('1.0', END)

    def run_around(self):
        for i in cottage_locations:
            command_list = ['WalkTo', self.focusCharacter, self.locationName + "." + i]
            self.action(self.create_command(command_list))
            self.action('Wait(1)')

    def test_forestpath(self):
        self.action("SetCameraMode(track)")
        self.currentFocusMode = "track"
        self.action("CreatePlace(Forest, ForestPath)")
        command_list = ['SetPosition', self.focusCharacter, "Forest"]
        self.action(self.create_command(command_list))
        command_list = ['SetClothing', self.focusCharacter, "Bandit"]
        self.action(self.create_command(command_list))
        command_list = ['SetHairStyle', "A"]
        self.action(self.create_command(command_list))
        command_list = ['SetEyeColor', self.focusCharacter]
        self.action(self.create_command(command_list))
        command_list = ['SetHairColor', self.focusCharacter]
        self.action(self.create_command(command_list))
        command_list = ['SetSkinColor', self.focusCharacter, str(0)]
        self.action(self.create_command(command_list))
        for key in CamelotLists.ForestPath.names:
            print("place: " + str(CamelotLists.ForestPath.names[key]))
            command_list = ['WalkTo', self.focusCharacter, "Forest" + "." + CamelotLists.ForestPath.names[key]]
            self.action(self.create_command(command_list))
            self.action('Wait(2)')
        self.action(self.create_command(["Exit", self.focusCharacter, "Forest.WestEnd"]))
        self.action(self.create_command(["Enter", self.focusCharacter, "Forest.EastEnd"]))
        self.action("Wait(1)")
        self.action(self.create_command(["Exit", self.focusCharacter, "Forest.EastEnd"]))
        self.action(self.create_command(["Enter", self.focusCharacter, "Forest.WestEnd"]))

    def test_forestpath_manual(self):
        self.action("SetCameraMode(track)")
        self.currentFocusMode = "track"
        self.action("CreatePlace(Forest, ForestPath)")
        command_list = ['SetPosition', self.focusCharacter, "Forest"]
        self.action(self.create_command(command_list))
        command_list = ['SetClothing', self.focusCharacter, "Bandit"]
        self.action(self.create_command(command_list))
        command_list = ['SetHairColor', self.focusCharacter]
        self.action(self.create_command(command_list))
        self.action("EnableInput()")
    def initialize(self):
        """
        self.action('CreatePlace(BobsHouse, Farm)')
        self.action('CreateCharacter(BobB, B)')
        # self.action('CreateCharacter(A)')
        # self.action('CreateCharacter(B)')
        # self.action('CreateCharacter(C)')
        # self.action('CreateCharacter(D)')
        # self.action('SetPosition(A, BobsHouse)')
        # self.action('SetPosition(B, BobsHouse)')
        # self.action('SetPosition(C, BobsHouse)')
        # self.action('SetPosition(D, BobsHouse)')
        self.action('SetPosition(BobB, BobsHouse)')
        self.action('SetCameraFocus(BobB)')
        self.action('SetCameraMode(focus)')
        self.action('SetCameraBlend(1.25)')
        self.currentFocusMode = "focus"
        self.focusCharacter = "BobB"
        self.action('ShowMenu()')
        self.action('HideMenu()')
        """
        self.action('CreatePlace(BobsHouse, Cottage)')
        self.action('CreateCharacter(BobB, B)')
        self.action('SetPosition(BobB, BobsHouse.Door)')
        self.action('SetCameraFocus(BobB)')
        self.action('SetCameraMode(focus)')
        self.action('ShowMenu()')
        self.action('HideMenu()')


    def test_icons(self):
        self.action('CreatePlace(Courtyard, Courtyard)')
        self.action('CreateCharacter(BobC, B)')
        self.action('SetPosition(BobC, Courtyard.Fountain)')
        self.action('CreateCharacter(Merchant, G)')
        self.action('SetCameraFocus(BobC)')
        self.action('SetCameraMode(follow)')
        self.action('SetPosition(Merchant, Courtyard.Exit)')
        self.action('WalkTo(BobC, Merchant)')
        self.action('Face(BobB, Merchant)')
        self.action('EnableInput()')
        sublist = []
        for i in range(0, len(CamelotLists.Icons), 10):
            sublist.append(CamelotLists.Icons[i:i + 10])
        for lists in sublist:
            for icons in lists:
                command_list = ['EnableIcon', str(icons), icons, 'Merchant']
                self.action(self.create_command(command_list))
                if lists.index(icons) == len(lists) - 1:
                    self.action('Wait(2)')
                    for deleteIcons in lists:
                        command_list = ['DisableIcon', str(deleteIcons), 'Merchant']
                        self.action(self.create_command(command_list))

    def play_sound(self):
        for i in range(len(CamelotLists.SoundEffects_Actions[0])):
            command_list = ['PlaySound', CamelotLists.SoundEffects_Actions[0][i], self.focusCharacter]
            self.action(self.create_command(command_list))
            command_list = ['Wait', CamelotLists.SoundEffects_Actions[1][i]]
            self.action(self.create_command(command_list))
        for i in range(len(CamelotLists.SoundEffects_Ambient[0])):
            command_list = ['PlaySound', CamelotLists.SoundEffects_Ambient[0][i], self.focusCharacter]
            self.action(self.create_command(command_list))
            command_list = ['Wait', CamelotLists.SoundEffects_Ambient[1][i]]
            self.action(self.create_command(command_list))
        for i in range(len(CamelotLists.SoundEffects_Characters[0])):
            command_list = ['PlaySound', CamelotLists.SoundEffects_Characters[0][i], self.focusCharacter]
            self.action(self.create_command(command_list))
            command_list = ['Wait', CamelotLists.SoundEffects_Characters[1][i]]
            self.action(self.create_command(command_list))
        for i in range(len(CamelotLists.SoundEffects_Effects[0])):
            command_list = ['PlaySound', CamelotLists.SoundEffects_Effects[0][i], self.focusCharacter]
            self.action(self.create_command(command_list))
            command_list = ['Wait', CamelotLists.SoundEffects_Effects[1][i]]
            self.action(self.create_command(command_list))
        for i in range(len(CamelotLists.SoundEffects_Furniture[0])):
            command_list = ['PlaySound', CamelotLists.SoundEffects_Furniture[0][i], self.focusCharacter]
            self.action(self.create_command(command_list))
            command_list = ['Wait', CamelotLists.SoundEffects_Furniture[1][i]]
            self.action(self.create_command(command_list))
        for i in range(len(CamelotLists.SoundEffects_Music[0])):
            command_list = ['PlaySound', CamelotLists.SoundEffects_Music[0][i], self.focusCharacter]
            self.action(self.create_command(command_list))
            command_list = ['Wait', CamelotLists.SoundEffects_UI[1][i]]
            self.action(self.create_command(command_list))
        for i in range(len(CamelotLists.SoundEffects_Music[0])):
            command_list = ['PlaySound', CamelotLists.SoundEffects_UI[0][i], self.focusCharacter]
            self.action(self.create_command(command_list))
            command_list = ['Wait', CamelotLists.SoundEffects_UI[1][i]]
            self.action(self.create_command(command_list))

    def test(self):
        self.action('WalkToSpot(BobB, 300, 0, 10')
        self.action('WalkToSpot(A, 300, 0, 11.3')
        self.action('WalkToSpot(C, 300, 0, 8.7')
        self.action('WalkToSpot(D, 301.3, 0, 10')
        self.action('WalkToSpot(B, 298.7, 0, 10')
        self.action('Face(A, BobB)')
        self.action('Face(B, BobB)')
        self.action('Face(C, BobB)')
        self.action('Face(D, BobB)')

    def test2(self):
        self.action('SetCameraFocus(A)')
        self.action('SetCameraFocus(B)')
        self.action('SetCameraFocus(C)')
        self.action('SetCameraFocus(D)')



    def action(self, command):
        print('start ' + command)
        while True:
            i = input()
            if not i.startswith('succeeded Wait'):
                if i == 'succeeded ' + command:
                    self.outputBox.insert(INSERT, i + '\n')
                    return True
                elif i == 'failed ' + command:
                    self.outputBox.insert(INSERT, i + '\n')
                    return False
                elif i.startswith('error'):
                    self.outputBox.insert(INSERT, i + '\n')
                    return False
            else:
                return True

    @staticmethod
    def create_command(command_list):
        if len(command_list) > 1:
            new_command = command_list[0] + "("
            for i in command_list[1:]:
                new_command = new_command + i + ","
            new_command = new_command[:-1]
            new_command = new_command + ")"
        else:
            new_command = command_list[0] + "()"

        return new_command


newUI = TestingGui(root)
root.mainloop()
