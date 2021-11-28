import csv
import pickle

import CamelotLists
from tkinter import *
from tkinter import ttk
import ctypes

# sets the root for the testing window

import Location
from PlaceReader import parseData

root = Tk()
root.title('Camelot Testing Environment')

# for i in CamelotLists.All_Places:
#     CamelotLists.locations_list.append(parseData("PlaceCSVs\\%s" % i, i))

class TestingGui:
    def __init__(self, master):
        # hold information about the current location/character

        self.focusCharacter = ""
        self.locationName = "BobsHouse"
        self.currentFocusMode = "follow"
        self.isInputEnabled = False
        self.characterLocation = "characterFarm"
        self.isCreated = False
        self.onePersonView = False
        self.isBodyCharacter = False
        self.characters = ["charA", "charB", "charC", "charD", "charE", "charF", "charG", "charH"]
        self.placeItem = "placebag"
        self.mainCharacter = "BobB"
        # # buttons/textbox for input and output for camelot
        self.myButton = Button(master, text="Run Command", command=self.get_input)
        self.clearButton = Button(master, text="Clear", command=self.clear_output)
        self.commandBox = Text(master, height=5, width=40)
        self.outputBox = Text(master, height=12, width=40)
        #
        # self.reset_button = Button(master, text="Test", command=self.resetCamelot)
        # self.initialize_button = Button(master, text="Initialize", command=self.initialize)
        #

        self.fullTestingButton = Button(master, text ="Full Test", command=self.run_all_tests)

        self.partialTestingButton = Button(master, text="Partial Testing",
                                           command=lambda: self.createPartialTestingWindow(root))

        # pack buttons
        self.commandBox.pack()
        self.myButton.pack()
        self.outputBox.pack()
        self.clearButton.pack()

        # self.reset_button.pack()
        # self.initialize_button.pack()
        self.fullTestingButton.pack()
        self.partialTestingButton.pack()


        # call initialize
        self.initialize()

    # reset camelot and use initialize
    def resetCamelot(self):
        self.action('Reset()')
    # partial testing window
    def createPartialTestingWindow(self, master):
        partialTestingWindow  = Toplevel(master)
        partialTestingWindow.title("Partial Testing Experience Manager")
        partialTestingWindow.geometry("400x400")
        partialTestingWindow.update()

        Button(partialTestingWindow, text="Character", command=lambda: self.createCharacterWindow(partialTestingWindow)).pack()
        Button(partialTestingWindow, text="Items", command=self.itemsTest).pack()
        Button(partialTestingWindow, text="Places", command=lambda: self.createPlacesTestingWidnow(partialTestingWindow)).pack()
        Button(partialTestingWindow, text="Visual Effects", command=self.visual_effects_test).pack()
        Button(partialTestingWindow, text="Sound Effects", command=self.play_sound).pack()
        Button(partialTestingWindow, text="Animations", command=self.single_actions).pack()
        Button(partialTestingWindow, text="Two Char Animations", command=self.test_two_CharacterActions).pack()
        Button(partialTestingWindow, text="Icons", command=self.test_icons).pack()

        partialTestingWindow.mainloop()


    def run_all_tests(self):
        self.clothingTest()
        self.hair_style_test()
        self.itemsTest()
        for i in CamelotLists.locations_list:
            self.action(self.test_Place(i))
        self.visual_effects_test()
        self.single_actions()
        self.test_two_CharacterActions()
        self.play_sound()
        self.test_icons()


    def createPlacesTestingWidnow(self, master):
        placesWindow = Toplevel()
        placesWindow.title("Manual Places Experience Manager")
        placesWindow.geometry("400x500")

        master.withdraw()
        placesWindow.protocol("WM_DELETE_WINDOW", lambda: self.openOldWindow(master, placesWindow))

        places_frame = Frame(placesWindow)

        placesBox = Listbox(places_frame)
        scrollbar = Scrollbar(places_frame, orient=VERTICAL)

        for i in CamelotLists.All_Places:
            placesBox.insert(END, i)

        placesBox.config(width = 50, yscrollcommand=scrollbar.set)
        scrollbar.config(command=placesBox.yview)
        scrollbar.pack(side =RIGHT, fill=Y)
        placesBox.pack(pady=15)

        Label(placesWindow, text="Current Test Running")
        placesLabel = Label(placesWindow, text ="None")

        places_frame.pack()

        Button(placesWindow, text="Run Test", command=lambda:self.selectPlace(placesWindow,placesLabel,placesBox)).pack()
        Label(placesWindow, text="Current Test Running").pack()
        placesLabel.pack()

        placesWindow.mainloop()


    def selectPlace(self, master, newLabel, newlistbox):

        selected_place = str(newlistbox.get(newlistbox.curselection()))
        newLabel.config(text=selected_place)
        master.update()

        for i in CamelotLists.locations_list:
            if i.title == selected_place:
                selected_location = i
        self.action(self.test_Place(selected_location))



    def createCharacterWindow(self,master):
        characterWindow = Toplevel()
        characterWindow.title("Manual Character Experience Manager")
        characterWindow.geometry('400x400')

        master.withdraw()
        characterWindow.protocol("WM_DELETE_WINDOW", lambda: self.openOldWindow(master, characterWindow))

        Button(characterWindow,text="Clothing", command=self.clothingTest).pack()
        Button(characterWindow, text= "HairStyle", command=self.hair_style_test).pack()




        characterWindow.mainloop()


    def properWindow(self,height, width):
        ws = root.winfo_screenwidth()
        hs = root.wininfoscreenwidth()

        x = (ws/2)-(width/2)
        y = (hs/2) - (height/2)

        return width, height, x, y

 #   def run_full_test(self):

    def visual_effects_test(self):
        visual_character = self.focusCharacter
        wait_time = "5"
        self.action(self.create_command(['SetPosition', visual_character, "BobsHouse"]))
        self.action(self.create_command(['SetCameraFocus', visual_character]))
        self.action('SetCameraMode(follow)')
        for i in CamelotLists.Visual_Effects:
            command_list = ['CreateEffect', visual_character, i]
            self.action(self.create_command(command_list))
            self.action("Wait(%s)"% wait_time)
            command_list = ['DisableEffect', visual_character]
            self.action(self.create_command(command_list))





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

    def openOldWindow(self, master, current):
        master.deiconify()
        current.destroy()
        current.update()

    def hair_style_test(self):

        old_character = ""
        self.action(self.create_command(['SetCameraMode', 'focus']))

        if not self.isBodyCharacter:
            for i in self.characters:
                command_list = ['CreateCharacter', i, i[-1]]
                self.action(self.create_command(command_list))
            self.isBodyCharacter = True
        for i in self.characters:
            command_list = ['SetPosition', i, self.characterLocation]
            self.action(self.create_command(command_list))
            self.action(self.create_command(['SetCameraFocus', i]))
            for j in CamelotLists.Hairstyles_All_Body_Types:
                command_list = ['SetHairStyle', i, j]
                self.action(self.create_command(command_list))
                self.action('Wait(.5)')
            if i[-1] in ['B','D''F','H']:
                for k in CamelotLists.Hairsyles_BDFH:
                    command_list = ['SetHairStyle', i, k]
                    self.action(self.create_command(command_list))
                    self.action('Wait(.5)')
            if i[-1] in ['A','C','G', 'E']:
                for n in CamelotLists.Hairsyles_ACEG:
                    command_list = ['SetHairStyle', i, n]
                    self.action(self.create_command(command_list))
                    self.action('Wait(.5)')
            self.action(self.create_command(['SetCameraFocus', self.characterLocation + ".Exit"]))
            self.action(self.create_command(['SetPosition', i]))



    def itemsTest(self):
        item_character = self.mainCharacter
        wait_time = "1.5"
        self.action(self.create_command(['SetPosition', item_character, "BobsHouse"]))
        self.action(self.create_command(['SetCameraFocus', item_character]))
        self.action('SetCameraMode(follow)')
        for i in CamelotLists.Items:
            command_list = ['CreateItem', i, i]
            self.action(self.create_command(command_list))
            command_list = ['SetPosition', i, item_character]
            self.action(self.create_command(command_list))
            if i == CamelotLists.Items[0]:
                self.action(self.create_command(["SetCameraFocus", i]))
            self.action("Wait(%s)"% wait_time)
            command_list = ['Pocket', item_character, i]
            self.action(self.create_command(command_list))
            self.action("Wait(%s)"% wait_time)
            command_list = ['Draw', item_character, i]
            self.action(self.create_command(command_list))
            self.action("Wait(%s)"% wait_time)
            command_list = ['Sheathe', item_character, i]
            self.action(self.create_command(command_list))
            self.action("Wait(%s)"% wait_time)

        self.action(self.create_command(["SetCameraFocus", self.focusCharacter]))

    def clothingTest(self):
        # don't want to create new characters every time
        if not self.isCreated:
            if not self.onePersonView:
                self.action('CreateCharacter(A, A)')
            self.action('CreateCharacter(B, B)')
            self.action('CreateCharacter(C, C)')
            self.action('CreateCharacter(D, D)')
            if not self.isBodyCharacter:
                for i in self.characters:
                    command_list = ['CreateCharacter', i, i[-1]]
                    self.action(self.create_command(command_list))
                self.isBodyCharacter = True
        # set up the clothing location
            self.action(self.create_command(['SetCameraFocus', self.characters[0]]))
            command_list = ['SetPosition', self.characters[0], self.characterLocation]
            self.action(self.create_command(command_list))
            if not self.onePersonView:
                command_list = ['SetPosition', "A", self.characterLocation]
                self.action(self.create_command(command_list))
            command_list = ['SetPosition', "B", self.characterLocation]
            self.action(self.create_command(command_list))
            command_list = ['SetPosition', "C", self.characterLocation]
            self.action(self.create_command(command_list))
            command_list = ['SetPosition', "D", self.characterLocation]
            self.action(self.create_command(command_list))
            self.action('SetCameraMode(follow)')
            self.action('WalkToSpot(charA, 300, 0, 10)')
            if not self.onePersonView:
                self.action('WalkToSpot(A, 300, 0, 12)')
            self.action('WalkToSpot(C, 300, 0, 8)')
            self.action('WalkToSpot(D, 302, 0, 10)')
            self.action('WalkToSpot(B, 298, 0, 10)')
            command_list = ["Face", "A", self.characters[0]]
            self.action(self.create_command(command_list))
            command_list = ["Face", "B", self.characters[0]]
            self.action(self.create_command(command_list))
            command_list = ["Face", "C", self.characters[0]]
            self.action(self.create_command(command_list))
            command_list = ["Face", "D", self.characters[0]]
            self.action(self.create_command(command_list))

            self.isCreated = True

        # actual loop for clothing
        for i in self.characters:
            # all clothing
            command_list = ['SetPosition', i, self.characterLocation]
            self.action(self.create_command(command_list))
            self.action(self.create_command(["WalkToSpot", i, "300", "0", "10"]))
            self.action('SetClothing(charA, Bandit)')
            for j in CamelotLists.Outfits_All_Body_Types:
                command_list = ['SetClothing', i, j]
                self.action(self.create_command(command_list))
                self.spinCamera()
            # male clothing
            if i[-1] in ['A', 'C', 'E', 'G']:
                for k in CamelotLists.Outfits_ACEG:
                    command_list = ['SetClothing', i, k]
                    self.action(self.create_command(command_list))
                    self.spinCamera()
            # male clothing
            if i[-1] in ['B', 'D', 'F', 'H']:
                for m in CamelotLists.Outfits_BDFH:
                    command_list = ['SetClothing', i, m]
                    self.action(self.create_command(command_list))
                    self.spinCamera()
            command_list = ['SetPosition', i]
            self.action(self.create_command(command_list))

    def spinCamera(self):
        self.action('SetCameraFocus(A)')
        self.action('SetCameraFocus(B)')
        self.action('SetCameraFocus(C)')
        self.action('SetCameraFocus(D)')

    def action(self, command):
        print('start ' + command)
        # set the currentFocusMode to the current focus, don't run it if its the same
        if command.startswith("SetCameraMode"):
            chosenFocus = ""
            if "focus" in command:
                chosenFocus = "focus"
            if "follow" in command:
                chosenFocus = "follow"
            if "track" in command:
                chosenFocus = "track"
            if chosenFocus == self.currentFocusMode:
                return True
            else:
                self.currentFocusMode = chosenFocus

        if command.startswith("SetCameraFocus"):
            chosenCharacter = command[command.find('(')+1:command.find(')')]
            if chosenCharacter == self.focusCharacter:
                return True
            else:
                self.focusCharacter = chosenCharacter

        while True:
            i = input()
            if not i.startswith('succeeded Wait'):
                if i.startswith('succeeded'):
                    self.outputBox.insert(INSERT, i + '\n')
                    return True
                elif i.startswith('fail'):
                    ctypes.windll.user32.MessageBoxW(0, "failed" + str(command), "Fail Detected", 1)
                    self.outputBox.insert(INSERT, i + '\n')
                    return False
                elif i.startswith('error'):
                    self.outputBox.insert(INSERT, i + '\n')
                    ctypes.windll.user32.MessageBoxW(0, "error " + str(command), "Error Detected", 1)
                    return False
            else:
                return True

    def test_Place(self, place: Location):
        self.focusCharacter = self.mainCharacter
        self.action(self.create_command(["CreatePlace", place.title, place.title]))
        for i in ("track", "follow", "focus"):
            self.action("SetCameraMode(" + i + ")")
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
                                command_list = ['Put', self.focusCharacter, self.placeItem,
                                                place.title + "." + location[0]]
                                self.action(self.create_command(command_list))
                                command_list = ['Take', self.focusCharacter, self.placeItem,
                                                place.title + "." + location[0]]
                                self.action(self.create_command(command_list))
                                if location[2] is not None:
                                    for pos in location[2]:
                                        command_list = ['Put', self.focusCharacter, self.placeItem,
                                                        place.title + "." + location[0] + "." + pos]
                                        self.action(self.create_command(command_list))
                                        command_list = ['Take', self.focusCharacter, self.placeItem,
                                                        place.title + "." + location[0] + "." + pos]
                                        self.action(self.create_command(command_list))
                            if attr == "Seat":
                                command_list = ['Sit', self.focusCharacter, place.title + "." + location[0]]
                                self.action(self.create_command(command_list))
                                self.action("Wait(1)")
                                command_list = ['WalkTo', self.focusCharacter, place.title + "." + location[0]]
                                self.action(self.create_command(command_list))
                                if location[0] == "Bed":
                                    command_list = ['Sleep', self.focusCharacter, place.title + "." + location[0]]
                                    self.action(self.create_command(command_list))
                                    self.action("Wait(1)")
                                    command_list = ['WalkTo', self.focusCharacter, place.title + "." + location[0]]
                                    self.action(self.create_command(command_list))
                                if location[2] is not None:
                                    for pos in location[2]:
                                        command_list = ['Sit', self.focusCharacter, place.title + "." + location[0]
                                                        + "." + pos]
                                        self.action(self.create_command(command_list))
                                        self.action("Wait(1)")
                                        command_list = ['WalkTo', self.focusCharacter, place.title + "." + location[0]]
                                        self.action(self.create_command(command_list))
                            if attr == "Furniture":
                                command_list = ['Bash', self.focusCharacter, place.title + "." + location[0]]
                                self.action(self.create_command(command_list))
                            if attr == "Can Open and Close":
                                command_list = ['OpenFurniture', self.focusCharacter, place.title + "." + location[0]]
                                self.action(self.create_command(command_list))
                                command_list = ['CloseFurniture', self.focusCharacter, place.title + "." + location[0]]
                                self.action(self.create_command(command_list))
                                if location[0] not in place.exits:
                                    command_list = ['OpenFurniture', self.focusCharacter,
                                                    place.title + "." + location[0]]
                                    self.action(self.create_command(command_list))

            for portal in place.exits:
                command_list = ['WalkTo', self.focusCharacter, place.title + "." + portal]
                self.action(self.create_command(command_list))
                self.action(self.create_command(["Exit", self.focusCharacter, place.title + "." + portal, "true"]))
                self.action(self.create_command(["Enter", self.focusCharacter, place.title + "." + portal, "true"]))

    # initializer function for camelot for basic spawn
    def initialize(self):
        self.action('CreatePlace(characterFarm, Farm)')
        self.action('CreatePlace(BobsHouse, Cottage)')
        self.action('CreateCharacter(BobB, B)')
        self.action('SetPosition(BobB, BobsHouse.Door)')
        self.action('SetCameraFocus(BobB)')
        self.action('SetCameraMode(focus)')
        self.action('CreateItem(placebag, Bag)')
        self.action('ShowMenu()')
        self.action('HideMenu()')
        self.focusCharacter = "BobB"
        self.currentFocusMode = "focus"
    # function that takes in a string list and turns into a proper command for camelot

    def create_command(self, command_list):
        if len(command_list) > 1:
            new_command = command_list[0] + "("
            for i in command_list[1:]:
                new_command = new_command + i + ","
            new_command = new_command[:-1]
            new_command = new_command + ")"
        else:
            new_command = command_list[0] + "()"

        return new_command

    # output box functions
    def clear_output(self):
        self.outputBox.delete('1.0', END)

    def get_input(self):
        input = self.commandBox.get("1.0", 'end-1c')
        self.action(input)
        self.commandBox.delete('1.0', END)

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

    def single_actions(self):
        commandList = ['SetCameraFocus', self.focusCharacter]
        self.action(self.create_command(commandList))
        self.action('SetCameraMode(follow)')
        self.action('SetCameraMode(focus)')
        for i in CamelotLists.Actions_Single:
            commandList = [i, self.focusCharacter]
            self.action(self.create_command(commandList))

    def test_two_CharacterActions(self):
        self.action("CreatePlace(CharacterInteraction, Farm")
        self.action("CreateCharacter(TestDummy, A)")
        for char in ("TestDummy", "BobB"):
            command_list = ['SetCameraFocus', char]
            self.action(self.create_command(command_list))
            self.action("SetCameraMode(Follow)")
            command_list = ['SetPosition', self.focusCharacter, "CharacterInteraction"]
            self.action(self.create_command(command_list))
            self.action("SetPosition(TestDummy, CharacterInteraction.Exit)")
            command_list = ['SetClothing', self.focusCharacter, "Peasant"]
            self.action(self.create_command(command_list))
            self.action("SetClothing(TestDummy, Peasant)")

            self.action("CreateItem(DummySword, Sword)")
            command_list = ["Draw", self.focusCharacter, "DummySword"]
            self.action(self.create_command(command_list))
            command_list = ["Attack", self.focusCharacter, "TestDummy", "false"]
            self.action(self.create_command(command_list))
            command_list = ["Attack", self.focusCharacter, "TestDummy", "true"]
            self.action(self.create_command(command_list))
            command_list = ["Pocket", self.focusCharacter, "DummySword"]
            self.action(self.create_command(command_list))

            self.walkAway()
            command_list = ["Cast", self.focusCharacter, "TestDummy"]
            self.action(self.create_command(command_list))
            command_list = ["DanceTogether", self.focusCharacter, "TestDummy"]
            self.action(self.create_command(command_list))

            self.walkAway()
            command_list = ["Face", self.focusCharacter, "TestDummy"]
            self.action(self.create_command(command_list))
            self.action("CreateItem(DummyPotion, BluePotion)")
            command_list = ["Give", self.focusCharacter, "DummyPotion", "TestDummy"]
            self.action(self.create_command(command_list))
            command_list = ["LookAt", self.focusCharacter, "TestDummy"]
            self.action(self.create_command(command_list))
            command_list = ["LookAt", self.focusCharacter]
            self.action(self.create_command(command_list))

            self.walkAway()
            command_list = ["Put", "TestDummy", "DummyPotion", self.focusCharacter]
            self.action(self.create_command(command_list))

            self.walkAway()
            command_list = ["Take", "TestDummy", "DummyPotion", self.focusCharacter]
            self.action(self.create_command(command_list))







newUI = TestingGui(root)
root.mainloop()

