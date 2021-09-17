import CamelotLists
from tkinter import *

root = Tk()
root.title('Camelot Testing Environment')

Hair_Color = ["gray", "black", "brown", "red", "blonde"]

class TestingGui:
	def __init__(self, master):
		self.characterName = "Bob"
		self.myButton = Button(master, text="Run Command", command=self.getInput)
		self.clearButton = Button(master, text="Clear", command=self.clearOutput)
		self.commandBox = Text(master, height=5, width=40)
		self.outputBox = Text(master, height=12, width=40)
		self.clothingBoxButton = Button(master, text="Clothing", command=self.clothing)
		self.eyeColorButton = Button(master, text="Eye Color", command=self.eye_color)
		self.hairStylesButton = Button(master, text="Hair Styles", command=self.hair_style)
		self.defaultButton = Button(master, text="Default", command=self.default)
		self.haircolorButton = Button(master, text="Hair Color", command=self.hair_color)
		self.increaseDifficulty = Button(master, text="Skin Color", command=self.skin_color)

		self.commandBox.pack()
		self.myButton.pack()
		self.outputBox.pack()
		self.clearButton.pack()
		self.clothingBoxButton.pack()
		self.eyeColorButton.pack()
		self.hairStylesButton.pack()
		self.haircolorButton.pack()
		self.increaseDifficulty.pack()
		self.defaultButton.pack()

		self.initialize()

	@staticmethod
	def create_command(commandList):
		if len(commandList) > 1:
			new_command = commandList[0] + "("
			for i in commandList[1:]:
				new_command = new_command + i + ","
			new_command = new_command[:-1]
			new_command = new_command + ")"
		else:
			new_command = commandList[0] + "()"

		return new_command

	def clothing(self):
		for i in CamelotLists.Outfits_All_Body_Types:
			command_list = ['SetClothing', self.characterName, i]
			self.action(self.create_command(command_list))
			self.action('Wait(.5)')

	def hair_style(self):
		for i in CamelotLists.Hairstyles_All_Body_Types:
			command_list = ['SetHairStyle', self.characterName, i]
			self.action(self.create_command(command_list))
			self.action('Wait(.5)')

	def eye_color(self):
		for i in CamelotLists.Eye_Color:
			command_list = ['SetEyeColor', self.characterName, i]
			self.action(self.create_command(command_list))
			self.action('Wait(.5)')


	def default(self):
		commandList = ['SetClothing', self.characterName]
		self.action(self.create_command(commandList))
		commandList = ['SetHairStyle', self.characterName]
		self.action(self.create_command(commandList))
		commandList = ['SetEyeColor', self.characterName]
		self.action(self.create_command(commandList))
		commandList = ['SetHairColor', self.characterName]
		self.action(self.create_command(commandList))
		commandList = ['SetSkinColor', self.characterName, str(0)]
		self.action(self.create_command(commandList))

	def hair_color(self):
		for i in Hair_Color:
			commandlist = ['SetHairColor', self.characterName,i]
			self.action(self.create_command(commandlist))
			self.action('Wait(.5)')

	def skin_color(self):
		for i in range(10):
			commandlist = ['SetSkinColor', self.characterName, str(i)]
			self.action(self.create_command(commandlist))
			self.action('Wait(.5)')

	def clearOutput(self):
		self.outputBox.delete('1.0', END)

	def getInput(self):
		input = self.commandBox.get("1.0", 'end-1c')
		self.action(input)
		self.commandBox.delete('1.0', END)


	def initialize(self):
		self.action('CreatePlace(BobsHouse, Cottage)')
		self.action('CreateCharacter(Bob, B)')
		self.action('SetClothing(Bob, Peasant)')
		self.action('SetPosition(Bob, BobsHouse.Door)')
		self.action('EnableIcon("Open_Door", Open, BobsHouse.Door, "Leave the house", true)')
		self.action('SetCameraFocus(Bob)')
		self.action('SetCameraMode(focus)')
		self.action('ShowMenu()')
		self.action('HideMenu()')

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


newUI = TestingGui(root)
root.mainloop()



