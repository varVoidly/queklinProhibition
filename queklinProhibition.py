# --------------------- Notes ---------------------
# Note 1: Note how we use two back slashes in the split and addition operator string. One slash is used as a string/escape operator and has an effect on the string its within dependant on the character that follows the slash. By adding two backslashes, the first backslash "escapes" the second backslash, allowing it to exist without being interpreted as an effector that does not have a defined purpose(due to the lack of a character following it)

# Note 2: Some functions are not created to reduce repetition, but rather to organize the script itself. functionFileLocator, for example, is only called at the start of the file however this line of the script is in between welcoming the user and presenting them the action menu, while the process of the function itself presents no user interaction. Thus, to make it look nicer, the process is defined as a function and instead called at the appropriate line instead of clogging up the segment.



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

def functionFileLocator():
	for entry in Path(pathLocalDirectory).iterdir():
		if entry.is_file() and entry.name == "pythonQueklinMasterFile.txt"








# --------------------- Actual program ---------------------





print("Good Morning, User.")
varName = input("Who Are We Today?")

print("Confirmed, Let Us Begin %s" % varName)
print("---")


