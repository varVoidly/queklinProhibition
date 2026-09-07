# --------------------- Notes ---------------------
# Note 00: Note 0's are used for general notes that are not referenced anywhere in the code.

# Note 01: Yes, i am fully aware(at the time of writing this, v0.1.0) that the current version can only handle a single file/profile. That may or may not change down the line when I finish the program and think "hmmmm, having a profiles system sure would be nice".



# Note 1: Note how we use two back slashes in the split and addition operator string. One slash is used as a string/escape operator and has an effect on the string its within dependant on the character that follows the slash. By adding two backslashes, the first backslash "escapes" the second backslash, allowing it to exist without being interpreted as an effector that does not have a defined purpose(due to the lack of a character following it)

# Note 2: Some functions are not created to reduce repetition, but rather to organize the script itself. functionFileLocator, for example, is only called at the start of the file however this line of the script is in between welcoming the user and presenting them the action menu, while the process of the function itself presents no user interaction. Thus, to make it look nicer, the process is defined as a function and instead called at the appropriate line instead of clogging up the segment.


# Note 3: open("filepath", "x") errors throw the subclass error "FileNotFoundError" AND the class error "IOError". Use "except (FileNotFoundError, IOError):" to catch whichever appears, or catch both, im not fully sure. Note that within the try portion, any error will instantly end the execution of the try portion and begin the execution of the except portion, preventing the execution of any lines following the line raising an error in the try portion


# --------------------- Imports ---------------------
import os
from pathlib import Path

# --------------------- Global Variables ---------------------

pathLocalDirectory = os.path.dirname(os.path.realpath(__file__))
# Stores the directory of this file - Used to determine the directory to be searched for the master file
# Should be "X:\Code\Python\queklinProhibition", with X being the drive letter 

pathDriveDirectory = ((pathLocalDirectory).split("\\"))[0] + "\\"
# Stores the directory of the drive this file is in - May or may not have a use, TBD
# Should be "X:\" with X being the drive letter

# Note 1 - Double backslashes

pathMasterFile = "D:\Code\Python\queklinProhibition\pythonQueklinMasterFile.txt"
# Stores the pathway of the master file - Used to quickly reference the Master file without having to repeatedly locate it using functionFileLocator.

# --------------------- Function Defining ---------------------
# Note 2 - Function purposes clarification

# Ensure the master exists, and creates it if not.
def functionFileLocator():
	try:
		open("pythonQueklinMasterFile.txt", "x").close() # .close() automatically closes it, preventing resource leaks and avoiding using a with statement
		with open("pythonQueklinMasterFile.txt", "w") as file:
			file.write("00#00#00") # Play time in order of hours, minutes and seconds
			file.write("prohibitedAppPathwayList#")
			file.write("prohibitedAppNameList#")
			
		# Note 3
	except (FileNotFoundError, IOError):
		pass # Pass does nothing, effectively nullifying the error as the exception is parsed.








# --------------------- Actual program ---------------------





print("Good Morning, User.")
varName = input("Who Are We Today?")

print("Confirmed, Let Us Begin %s" % varName)
print("---")

functionFileLocator()

