import CamelotLists
from tkinter import *


# sets the root for the testing window
root = Tk()
root.title('Camelot Testing Environment')

Hair_Color = ["gray", "black", "brown", "red", "blonde"]
cottage_locations = ["Door", "Bed", "Chair", "Table", "Shelf", "Bookshelf", "Chest"]

class TestingGui:
	def __init__(self, master):
		self.characterName = "Bob"
		self.locationName = "BobsHouse"
		self.myButton = Button(master, text="Run Command", command=self.get_input)
		self.clearButton = Button(master, text="Clear", command=self.clear_output)
		self.commandBox = Text(master, height=5, width=40)
		self.outputBox = Text(master, height=12, width=40)
		self.clothingBoxButton = Button(master, text="Clothing", command=self.clothing)
		self.eyeColorButton = Button(master, text="Eye Color", command=self.eye_color)
		self.hairStylesButton = Button(master, text="Hair Styles", command=self.hair_style)
		self.defaultButton = Button(master, text="Default", command=self.default)
		self.hair_colorButton = Button(master, text="Hair Color", command=self.hair_color)
		self.skin_colorButton = Button(master, text="Skin Color", command=self.skin_color)
		self.items_button = Button(master, text = "Items", command=self.items)
		self.visual_effects_button = Button(master, text="Visual Effects", command=self.visual_effects)
		self.run_aroundButton = Button(master, text= "Run Around", command=self.run_around)

		self.commandBox.pack()
		self.myButton.pack()
		self.outputBox.pack()
		self.clearButton.pack()
		self.clothingBoxButton.pack()
		self.eyeColorButton.pack()
		self.hairStylesButton.pack()
		self.hair_colorButton.pack()
		self.skin_colorButton.pack()
		self.items_button.pack()
		self.visual_effects_button.pack()
		self.run_aroundButton.pack()
		self.defaultButton.pack()

		self.initialize()

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
		command_list = ['SetPosition', self.characterName, self.locationName]
		self.action(self.create_command(command_list))
		command_list = ['SetClothing', self.characterName]
		self.action(self.create_command(command_list))
		command_list = ['SetHairStyle', self.characterName]
		self.action(self.create_command(command_list))
		command_list = ['SetEyeColor', self.characterName]
		self.action(self.create_command(command_list))
		command_list = ['SetHairColor', self.characterName]
		self.action(self.create_command(command_list))
		command_list = ['SetSkinColor', self.characterName, str(0)]
		self.action(self.create_command(command_list))

	def hair_color(self):
		for i in Hair_Color:
			command_list = ['SetHairColor', self.characterName,i]
			self.action(self.create_command(command_list))
			self.action('Wait(.5)')

	def skin_color(self):
		for i in range(10):
			command_list = ['SetSkinColor', self.characterName, str(i)]
			self.action(self.create_command(command_list))
			self.action('Wait(.5)')

	def items(self):
		for i in CamelotLists.Items:
			command_list = ['CreateItem',i , i]
			self.action(self.create_command(command_list))
			command_list = ['SetPosition',i , self.characterName]
			self.action(self.create_command(command_list))
			self.action('Wait(.75)')
			command_list = ['Pocket', self.characterName, i]
			self.action(self.create_command(command_list))

	def visual_effects(self):
		for i in CamelotLists.Visual_Effects:
			command_list = ['CreateEffect', self.characterName, i]
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
			command_list = ['WalkTo', self.characterName, self.locationName + "." + i]
			self.action(self.create_command(command_list))
			self.action('Wait(1)')

	def initialize(self):
		self.action('CreatePlace(BobsHouse, Cottage)')
		self.action('CreateCharacter(Bob, B)')
		self.action('SetPosition(Bob, BobsHouse.Door)')
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



