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


class TestingGui:
    def __init__(self, master):
        # hold information about the current location/character
        # set the time to wait between tests
        self.wait_time = 2

        self.focusCharacter = ""
        self.locationName = "BobsHouse"
        # to ensure two focus mode do not overlap
        self.currentFocusMode = "follow"
        self.isInputEnabled = False
        # location name of character test
        self.characterLocation = "characterFarm"
        self.isCreated = False
        self.onePersonView = False
        self.isBodyCharacter = False
        # all the characters to be used for clothing/hairstyles, last character is used for the body type
        self.characters = ["charA", "charB", "charC", "charD", "charE", "charF", "charG", "charH"]
        # item name that will be placed by the place test
        self.placeItem = "placebag"
        self.mainCharacter = "BobB"
        # # buttons/textbox for input and output for camelot
        self.myButton = Button(master, text="Run Command", command=self.get_input)
        self.clearButton = Button(master, text="Clear", command=self.clear_output)
        self.commandBox = Text(master, height=5, width=40)
        self.outputBox = Text(master, height=12, width=40)
        # reset button but scrapped due to it not working
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
        # create buttons and assign its proper function
        Button(partialTestingWindow, text="Character", command=lambda: self.createCharacterWindow(partialTestingWindow)).pack()
        Button(partialTestingWindow, text="Items", command=self.itemsTest).pack()
        Button(partialTestingWindow, text="Places", command=lambda: self.createPlacesTestingWidnow(partialTestingWindow)).pack()
        Button(partialTestingWindow, text="Visual Effects", command=self.visual_effects_test).pack()
        Button(partialTestingWindow, text="Sound Effects", command=self.play_sound).pack()
        Button(partialTestingWindow, text="Animations Single", command=self.single_actions).pack()
        Button(partialTestingWindow, text="Animations Double", command=self.test_two_CharacterActions).pack()
        Button(partialTestingWindow, text="Icons", command=self.test_icons).pack()

        partialTestingWindow.mainloop()

    # runs all tests
    def run_all_tests(self):
        self.clothingTest()
        self.hair_style_test()
        self.itemsTest()
        for i in CamelotLists.locations_list:
            self.test_Place(i)
        self.visual_effects_test()
        self.single_actions()
        self.test_two_CharacterActions()
        self.play_sound()
        self.test_icons()

    # create a places testing window that allows for a specific place to be picked
    def createPlacesTestingWidnow(self, master):
        placesWindow = Toplevel()
        placesWindow.title("Manual Places Experience Manager")
        placesWindow.geometry("400x500")

        master.withdraw()
        placesWindow.protocol("WM_DELETE_WINDOW", lambda: self.openOldWindow(master, placesWindow))

        places_frame = Frame(placesWindow)

        placesBox = Listbox(places_frame)
        scrollbar = Scrollbar(places_frame, orient=VERTICAL)
        # get all the places and put it in the listbox
        for i in CamelotLists.All_Places:
            placesBox.insert(END, i)

        placesBox.config(width = 50, yscrollcommand=scrollbar.set)
        scrollbar.config(command=placesBox.yview)
        scrollbar.pack(side =RIGHT, fill=Y)
        placesBox.pack(pady=15)
        # label to display the current test
        Label(placesWindow, text="Current Test Running")
        placesLabel = Label(placesWindow, text ="None")

        places_frame.pack()

        Button(placesWindow, text="Run Test", command=lambda:self.selectPlace(placesWindow,placesLabel,placesBox)).pack()
        Label(placesWindow, text="Current Test Running").pack()
        placesLabel.pack()

        placesWindow.mainloop()

    # helper function for place testing
    def selectPlace(self, master, newLabel, newlistbox):

        selected_place = str(newlistbox.get(newlistbox.curselection()))
        newLabel.config(text=selected_place)
        master.update()

        for i in CamelotLists.locations_list:
            if i.title == selected_place:
                selected_location = i
        self.action(self.test_Place(selected_location))


    # create a character window that allows a selection
    def createCharacterWindow(self,master):
        characterWindow = Toplevel()
        characterWindow.title("Manual Character Experience Manager")
        characterWindow.geometry('400x400')

        master.withdraw()
        characterWindow.protocol("WM_DELETE_WINDOW", lambda: self.openOldWindow(master, characterWindow))

        Button(characterWindow,text="Clothing", command=self.clothingTest).pack()
        Button(characterWindow, text= "HairStyle", command=self.hair_style_test).pack()




        characterWindow.mainloop()

    # helper function to window
    def properWindow(self,height, width):
        ws = root.winfo_screenwidth()
        hs = root.wininfoscreenwidth()

        x = (ws/2)-(width/2)
        y = (hs/2) - (height/2)

        return width, height, x, y

 #   def run_full_test(self):

    def visual_effects_test(self):
        visual_character = self.focusCharacter
        # custom time to see the full effect
        custom_time = "5"
        self.action(self.create_command(['SetPosition', visual_character, "BobsHouse"]))
        self.action(self.create_command(['SetCameraFocus', visual_character]))
        self.action('SetCameraMode(follow)')
        for i in CamelotLists.Visual_Effects:
            command_list = ['CreateEffect', visual_character, i]
            self.action(self.create_command(command_list))
            self.action("Wait(%s)"% custom_time)
            command_list = ['DisableEffect', visual_character]
            self.action(self.create_command(command_list))

    # testing icons, has a manual component due to camelot limit
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
        # make a sublist of all the items that will fit in the icon window
        for i in range(0, len(CamelotLists.Icons), 10):
            sublist.append(CamelotLists.Icons[i:i + 10])
        for lists in sublist:
            for icons in lists:
                # make a merchant that you walk up to and right click
                command_list = ['EnableIcon', str(icons), icons, 'Merchant']
                self.action(self.create_command(command_list))
                if lists.index(icons) == len(lists) - 1:
                    self.action('Wait(2)')
                    for deleteIcons in lists:
                        command_list = ['DisableIcon', str(deleteIcons), 'Merchant']
                        self.action(self.create_command(command_list))

    # helper function to ensure two windows stay open
    def openOldWindow(self, master, current):
        master.deiconify()
        current.destroy()
        current.update()

    # hair style testing
    def hair_style_test(self):

        old_character = ""
        self.action(self.create_command(['SetCameraMode', 'focus']))
        # if the character has not already been created
        if not self.isBodyCharacter:
            for i in self.characters:
                command_list = ['CreateCharacter', i, i[-1]]
                self.action(self.create_command(command_list))
            self.isBodyCharacter = True
        for i in self.characters:
            # set the character to a custom location
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


    # runs items test on the current focus character
    def itemsTest(self):
        item_character = self.mainCharacter
        self.action(self.create_command(['SetPosition', item_character, "BobsHouse"]))
        self.action(self.create_command(['SetCameraFocus', item_character]))
        self.action('SetCameraMode(follow)')
        for i in CamelotLists.Items:
            # makes the item
            # puts the item in the item_character's hand
            # makes it pocket it
            # draw it out
            # sheathe it
            # repeat
            command_list = ['CreateItem', i, i]
            self.action(self.create_command(command_list))
            command_list = ['SetPosition', i, item_character]
            self.action(self.create_command(command_list))
            if i == CamelotLists.Items[0]:
                self.action(self.create_command(["SetCameraFocus", i]))
            self.action("Wait(%s)"% self.wait_time)
            command_list = ['Pocket', item_character, i]
            self.action(self.create_command(command_list))
            self.action("Wait(%s)"% self.wait_time)
            command_list = ['Draw', item_character, i]
            self.action(self.create_command(command_list))
            self.action("Wait(%s)"% self.wait_time)
            command_list = ['Sheathe', item_character, i]
            self.action(self.create_command(command_list))
            self.action("Wait(%s)"% self.wait_time)

        self.action(self.create_command(["SetCameraFocus", self.focusCharacter]))

    def clothingTest(self):
        # don't want to create new characters every time
        if not self.isCreated:
            # create custom characters
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
            # set up location for the four character that the camera will revolve around
            self.action('WalkToSpot(charA, 300, 0, 10)')
            if not self.onePersonView:
                self.action('WalkToSpot(A, 300, 0, 12)')
            self.action('WalkToSpot(C, 300, 0, 8)')
            self.action('WalkToSpot(D, 302, 0, 10)')
            self.action('WalkToSpot(B, 298, 0, 10)')
            # make all the character's face a default character
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
            # female clothing
            if i[-1] in ['B', 'D', 'F', 'H']:
                for m in CamelotLists.Outfits_BDFH:
                    command_list = ['SetClothing', i, m]
                    self.action(self.create_command(command_list))
                    self.spinCamera()
            # make the character go away
            command_list = ['SetPosition', i]
            self.action(self.create_command(command_list))
            self.action(self.create_command(['SetClothing', i]))

    # helper function for character to spin the camera around
    def spinCamera(self):
        self.action('SetCameraFocus(A)')
        self.action('SetCameraFocus(B)')
        self.action('SetCameraFocus(C)')
        self.action('SetCameraFocus(D)')

    def action(self, command):
        print('start ' + command)
        # set the currentFocusMode to the current focus.
        # Camelot crashes if its set to the same once
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
        # function to stop a crash with setting the camera focus to the same character
        if command.startswith("SetCameraFocus"):
            chosenCharacter = command[command.find('(')+1:command.find(')')]
            if chosenCharacter == self.focusCharacter:
                return True
            else:
                self.focusCharacter = chosenCharacter

        while True:
            i = input()
            # ignore wait to avoid clutter; Can be removed
            if not i.startswith('succeeded Wait'):
                # if fail or error print out that error, if success print it to output box
                if i.startswith('succeeded'):
                    self.outputBox.insert(INSERT, i + '\n')
                    return True
                elif i.startswith('fail'):
                    ctypes.windll.user32.MessageBoxW(0, i , "Fail Detected", 1)
                    self.outputBox.insert(INSERT, i + '\n')
                    return False
                elif i.startswith('error'):
                    self.outputBox.insert(INSERT, i + '\n')
                    ctypes.windll.user32.MessageBoxW(0, i , "Error Detected", 1)
                    return False
            else:
                return True

    # runs places test on the passed location, goes through all camera angles and places and picks up items in all surfaces
    def test_Place(self, place: Location):
        self.focusCharacter = self.mainCharacter
        # make the place
        self.action(self.create_command(["CreatePlace", place.title, place.title]))
        # for every camera angle
        for i in ("track", "follow", "focus"):
            # make the character move around to the various locations
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
                            # if it matches the attributes perform that action
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
    # helper function for input
    def get_input(self):
        input = self.commandBox.get("1.0", 'end-1c')
        self.action(input)
        self.commandBox.delete('1.0', END)
    # play all the sounds and wait for the duration of the sounds
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

    # use all single actions animations
    # kneel causes a crash
    def single_actions(self):
        commandList = ['SetCameraFocus', self.focusCharacter]
        self.action(self.create_command(commandList))
        self.action('SetCameraMode(follow)')
        self.action('SetCameraMode(focus)')
        for i in CamelotLists.Actions_Single:
            commandList = [i, self.focusCharacter]
            self.action(self.create_command(commandList))


    # test two character animations, repeat from both character's focus
    def test_two_CharacterActions(self):
        self.action("CreatePlace(CharacterInteraction, Farm")
        self.action("CreateCharacter(TestDummy, A)")
        second_character = "BobB"
        self.action("CreateItem(DummyPotion, BluePotion)")
        self.action("CreateItem(DummySword, Sword)")
        # for both character's perspective
        for char in ("TestDummy", "BobB"):
            command_list = ['SetCameraFocus', char]
            self.action(self.create_command(command_list))
            self.action("SetCameraMode(Follow)")
            command_list = ['SetPosition', second_character, "CharacterInteraction"]
            self.action(self.create_command(command_list))
            self.action("SetPosition(TestDummy, CharacterInteraction.Exit)")
            command_list = ['SetClothing', second_character, "Peasant"]
            self.action(self.create_command(command_list))
            self.action("SetClothing(TestDummy, Peasant)")

            command_list = ["Draw", second_character, "DummySword"]
            self.action(self.create_command(command_list))
            command_list = ["Attack", second_character, "TestDummy", "false"]
            self.action(self.create_command(command_list))
            command_list = ["Attack", second_character, "TestDummy", "true"]
            self.action(self.create_command(command_list))
            command_list = ["Pocket", second_character, "DummySword"]
            self.action(self.create_command(command_list))

            self.walkAway()
            command_list = ["Cast", second_character, "TestDummy"]
            self.action(self.create_command(command_list))
            command_list = ["DanceTogether", second_character, "TestDummy"]
            self.action(self.create_command(command_list))

            self.walkAway()
            command_list = ["Face", second_character, "TestDummy"]
            self.action(self.create_command(command_list))

            command_list = ["Give", second_character, "DummyPotion", "TestDummy"]
            self.action(self.create_command(command_list))
            command_list = ["LookAt", second_character, "TestDummy"]
            self.action(self.create_command(command_list))
            command_list = ["LookAt", second_character]
            self.action(self.create_command(command_list))

            self.walkAway()
            command_list = ["Put", "TestDummy", "DummyPotion", second_character]
            self.action(self.create_command(command_list))

            self.walkAway()
            command_list = ["Take", "TestDummy", "DummyPotion", second_character]
            self.action(self.create_command(command_list))

    # helper function for animation test
    def walkAway(self):
        command_list = ['MoveAway', self.focusCharacter]
        self.action(self.create_command(command_list))




newUI = TestingGui(root)
root.mainloop()

