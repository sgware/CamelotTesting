import CamelotLists
from tkinter import *
from tkinter import ttk
import ctypes
import time

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


        self.partialTestingButton = Button(master, text = "Partial Testing", command=lambda: self.createPartialTestingWindow(root))

        self.myButton = Button(master, text="Run Command", command=self.get_input)
        self.clearButton = Button(master, text="Clear", command=self.clear_output)
        self.commandBox = Text(master, height=5, width=40)
        self.outputBox = Text(master, height=12, width=40)



        self.items_button = Button(master, text="Items", command=self.items)
        self.visual_effects_button = Button(master, text="Visual Effects", command=self.visual_effects)
        self.run_aroundButton = Button(master, text="Test Camera", command=self.spinCamera)
        self.all_clothingButton = Button(master, text="All Clothing", command=self.all_clothing)
        self.inputButton = Button(master, text="Clothing Test", command=self.clothing)
        self.forest_button = Button(master, text="Forest Path Test", command=self.test_forestpath)
        self.forest_manual_button = Button(master, text="Manual Forest Path Test", command=self.test_forestpath_manual)
        self.defaultButton = Button(master, text="Move", command=self.test)
        self.soundButton = Button(master, text ="Play sound", command=self.play_sound)
        self.single_actions_button = Button(master, text = "Single Action", command = self.single_actions)

        self.commandBox.pack()
        self.myButton.pack()
        self.run_aroundButton.pack()
        self.outputBox.pack()
        self.clearButton.pack()
        self.inputButton.pack()
        self.defaultButton.pack()
        self.visual_effects_button.pack()
        self.forest_button.pack()
        self.forest_manual_button.pack()
        self.partialTestingButton.pack()
        self.soundButton.pack()
        self.run_aroundButton.pack()
        self.items_button.pack()
        self.single_actions_button.pack()
        self.initialize()



    def createManualWindow(self, master):
        manualwindow = Toplevel(master)
        manualwindow.title("Manual Experience Manager")
        manualwindow.geometry("300x300")

        clothingWindow = Button(manualwindow, text="Clothing",
                                command=lambda: self.generateClothingWindow(manualwindow))
        hairWindow = Button(manualwindow, text="HairStyle", command=lambda: self.generateHairStyleWindow(manualwindow))

        expressionWindow = Button(manualwindow, text = "Expressions", command =lambda :self.generateExpressionWindow(manualwindow))

        characterWindow = Button(manualwindow, text="Character Creator", command = lambda :self.generateCharacterWindow(manualwindow))

        clothingWindow.pack()
        hairWindow.pack()
        expressionWindow.pack()
        characterWindow.pack()

        manualwindow.mainloop()

    def createPartialTestingWindow(self, master):
        partialTestingWindow  = Toplevel(master)
        partialTestingWindow.title("Partial Testing Experience Manager")
        partialTestingWindow.geometry("400x800")

        Button(partialTestingWindow, text = "Selection Testing", command= lambda :self.createSelectingTestingWindow(partialTestingWindow)).pack()
        Button(partialTestingWindow, text="Auto Testing",
               command=lambda: self.createautoTestWindow(partialTestingWindow)).pack()


        partialTestingWindow.mainloop()

    def createautoCharacterWindow(self,master):
        autoCharacterWindow = Toplevel(master)
        autoCharacterWindow.title("Partial Testing Experience Manager")
        autoCharacterWindow.geometry("400x800")

        Button(autoCharacterWindow, text="Clothing", command=self.clothing).pack()
        Button(autoCharacterWindow, text="Eye Color", command=self.eye_color).pack()
        Button(autoCharacterWindow, text="Hair Styles", command=self.hair_style).pack()
        Button(autoCharacterWindow, text="Hair Color", command=self.hair_color).pack()
        Button(autoCharacterWindow, text="Skin Color", command=self.skin_color).pack()

        autoCharacterWindow.mainloop()
        
    def createautoTestWindow(self,master):
        autoTestWindow = Toplevel(master)
        autoTestWindow.title("Full Partial Experience Manager")
        autoTestWindow.geometry("400x800")

        Button(autoTestWindow, text = "Auto Character", command=lambda :self.createautoCharacterWindow(autoTestWindow)).pack()

        autoTestWindow.mainloop()

    def createSelectingTestingWindow(self,master):
        selectionTestingWindow = Toplevel(master)
        selectionTestingWindow.title("Full Partial Experience Manager")
        selectionTestingWindow.geometry("400x800")

        manualTestButton = Button(selectionTestingWindow, text = "Manual Test", command=lambda :self.createManualWindow(selectionTestingWindow))
        autoTestButton = Button(selectionTestingWindow, text = "Auto Test", command = lambda :self.createautoTestWindow(selectionTestingWindow))
        manualTestButton.pack()
        autoTestButton.pack()

        selectionTestingWindow.mainloop()

    def generateHairStyleWindow(self, master):
        hairStyleWindow = Toplevel(master)
        hairStyleWindow.title("Manual HairStyle Experience Manager")
        hairStyleWindow.geometry("400x800")

        Label(hairStyleWindow, text="Hair Style:").pack()
        for i in CamelotLists.Hairstyles_All_Body_Types:
            ttk.Button(hairStyleWindow, text=i, command=lambda i=i: self.manualhairstyle(i)).pack()
        if self.focusCharacter[-1] in ['A', 'C', 'E', 'G']:
            for j in CamelotLists.Hairsyles_ACEG:
                ttk.Button(hairStyleWindow, text=j, command=lambda j=j: self.manualhairstyle(j)).pack()
        if self.focusCharacter[-1] in ['B', 'D', 'F', 'H']:
            for k in CamelotLists.Hairsyles_BDFH:
                ttk.Button(hairStyleWindow, text=k, command=lambda k=k: self.manualhairstyle(k)).pack()

        Label(hairStyleWindow, text="Hair Color:").pack()
        for i in CamelotLists.Hair_Color:
            ttk.Button(hairStyleWindow, text=i, command=lambda i=i: self.manualhaircolor(i)).pack()

        hairStyleWindow.mainloop()

    def generateCharacterWindow(self,master):
        characterWindow = Toplevel(master)
        characterWindow.title("Manual Character Experience Manager")
        characterWindow.geometry("400x500")


        characterWindow.mainloop()


    def generateExpressionWindow(self,master):
        expressionWindow = Toplevel(master)
        expressionWindow.title("Manual Expression Experience Manager")
        expressionWindow.geometry("400x500")

        for i in CamelotLists.Expressions:
            ttk.Button(expressionWindow, text=i, command=lambda i=i: self.manualexpression(i)).pack()

        expressionWindow.mainloop()


    def generateClothingWindow(self, master):
        clothingWindow = Toplevel(master)
        clothingWindow.title("Manual Clothing Experience Manager")
        clothingWindow.geometry("400x400")

        for i in CamelotLists.Outfits_All_Body_Types:
            ttk.Button(clothingWindow, text=i, command=lambda i=i: self.manualclothing(i)).pack()
        if self.focusCharacter[-1] in ['A', 'C', 'E', 'G']:
            for j in CamelotLists.Outfits_ACEG:
                ttk.Button(clothingWindow, text=j, command=lambda j=j: self.manualclothing(j)).pack()
        if self.focusCharacter[-1] in ['B', 'D', 'F', 'H']:
            for k in CamelotLists.Outfits_BDFH:
                ttk.Button(clothingWindow, text=k, command=lambda k=k: self.manualclothing(k)).pack()

        clothingWindow.mainloop()


    def manualclothing(self, clothingname):
        command_list = ['SetClothing', self.focusCharacter, clothingname]
        self.action(self.create_command(command_list))

    def manualhairstyle(self, hairstylename):
        command_list = ['SetHairStyle', self.focusCharacter, hairstylename]
        self.action(self.create_command(command_list))

    def manualhaircolor(self, haircolor):
        command_list = ['SetHairColor', self.focusCharacter, haircolor]
        self.action(self.create_command(command_list))

    def manualexpression(self,expression):
        command_list = ['SetExpression', self.focusCharacter, expression]
        self.action(self.create_command(command_list))

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
            self.spinCamera()

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
        #command_list = ['SetCameraMode', focus]
        #self.action(self.create_command(command_list))
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
            self.spinCamera()
            command_list = ['Pocket', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            command_list = ['Draw', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.spinCamera()
            command_list = ['Sheathe', self.focusCharacter, i]
            self.action(self.create_command(command_list))



    def visual_effects(self):
        for i in CamelotLists.Visual_Effects:
            command_list = ['CreateEffect', self.focusCharacter, i]
            self.action(self.create_command(command_list))
            self.spinCamera()
            command_list = ['DisableEffect', self.focusCharacter]
            self.action(self.create_command(command_list))


    def clear_output(self):
        self.outputBox.delete('1.0', END)

    def get_input(self):
        input = self.commandBox.get("1.0", 'end-1c')
        self.action(input)
        self.commandBox.delete('1.0', END)


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

    def single_actions(self):
        for i in CamelotLists.Actions_Single:
            commandList = [i, self.focusCharacter]
            self.action(self.create_command(commandList))
            self.spinCamera()
            if i == "Kneel":
                self.action('WalkToSpot(BobB, 300, 0, 10')


    def initialize(self):
        self.action('CreatePlace(BobsHouse, Farm)')
        self.action('CreateCharacter(BobB, B)')
        self.action('CreateCharacter(A, A)')
        self.action('CreateCharacter(B, B)')
        self.action('CreateCharacter(C, C)')
        self.action('CreateCharacter(D, D)')
        self.action('SetPosition(A, BobsHouse)')
        self.action('SetPosition(B, BobsHouse)')
        self.action('SetPosition(C, BobsHouse)')
        self.action('SetPosition(D, BobsHouse)')
        self.action('SetPosition(BobB, BobsHouse)')
        self.action('SetCameraFocus(BobB)')
        self.action('SetCameraMode(focus)')
        self.action('SetCameraBlend(1.25)')
        self.currentFocusMode = "focus"
        self.focusCharacter = "BobB"
        self.action('ShowMenu()')
        self.action('HideMenu()')


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
        self.action('SetCameraMode(follow)')
        self.action('WalkToSpot(BobB, 300, 0, 10')
        self.action('WalkToSpot(A, 300, 0, 12')
        self.action('WalkToSpot(C, 300, 0, 8')
        self.action('WalkToSpot(D, 302, 0, 10')
        self.action('WalkToSpot(B, 298, 0, 10')
        self.action('Face(A, BobB)')
        self.action('Face(B, BobB)')
        self.action('Face(C, BobB)')
        self.action('Face(D, BobB)')

    def spinCamera(self):
        self.action('SetCameraFocus(A)')
        self.action('SetCameraFocus(B)')
        self.action('SetCameraFocus(C)')
        self.action('SetCameraFocus(D)')

    def action(self, command):
        print('start ' + command)
        totaltime = -1
        while True:
            start = time.time()
            i = input()
            if not i.startswith('succeeded Wait'):
                if i == 'succeeded ' + command:
                    self.outputBox.insert(INSERT, i + '\n')
                    return True
                elif i == 'failed ' + command:
                    ctypes.windll.user32.MessageBoxW(0, "failed" + str(command), "Fail Detected", 1)
                    self.outputBox.insert(INSERT, i + '\n')
                    return False
                elif i.startswith('error'):
                    self.outputBox.insert(INSERT, i + '\n')
                    ctypes.windll.user32.MessageBoxW(0, "error " + str(command), "Error Detected", 1)
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
