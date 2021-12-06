*******************************************************************************
* CAMELOT TESTING ENVIROMENT                                                 *
* Version 1.0                                                                *
*******************************************************************************
To run:
Ensure you have all the files from: https://github.com/BlinkOfAEye/CamelotTesting
Edit StartExperienceManager.bat to include python mainmanager.py
Run Camelot.exe

To use:
The user can type in any Camelot readable commands found at: http://cs.uky.edu/~sgware/projects/camelot/v1-2/actions.html,
into the inputbox
Pressing run command will send that command to Camelot and any output from Camelot is displayed in the output box, should an error happen,
the TEC will produce an error/fail box.
Selecting Full Test will run every single test in this order:
	Clothing
	Hairstyle
	Items
	All Places
	Visual Effects
	All Single Actions
	All Two Character Actions
	All Sound Effects
	All Icons
Selecting Partial Testing Window will generate another window and allow for specific assets to be tested.
The character button will create another window allowing the user to choose between clothing test and hairstyle test
The places button will create new window that will have a list of all places that can be tested, selecting one and pressing run test will run that place test.
All other assets run the asset they are assigned.
