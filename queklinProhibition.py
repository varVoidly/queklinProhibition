# --------------------- LEFT OFF AT: Line 157 ---------------------


# --------------------- Notes ---------------------
# Note 00: Note 0's are used for general notes that are not referenced anywhere in the code.

# Note 01: Yes, i am fully aware(at the time of writing this, v0.1.0) that the current version can only handle a single file/profile. That may or may not change down the line when I finish the program and think "hmmmm, having a profiles system sure would be nice".



# Note 1: Note how we use two back slashes in the split and addition operator string. One slash is used as a string/escape operator and has an effect on the string its within dependant on the character that follows the slash. By adding two backslashes, the first backslash "escapes" the second backslash, allowing it to exist without being interpreted as an effector that does not have a defined purpose(due to the lack of a character following it)

# Note 2: Some functions are not created to reduce repetition, but rather to organize the script itself. functionFileLocator, for example, is only called at the start of the file however this line of the script is in between welcoming the user and presenting them the action menu, while the process of the function itself presents no user interaction. Thus, to make it look nicer, the process is defined as a function and instead called at the appropriate line instead of clogging up the segment.


# Note 3: open("filepath", "x") errors throw the subclass error "FileNotFoundError" AND the class error "IOError". Use "except (FileNotFoundError, IOError):" to catch whichever appears, or catch both, im not fully sure. Note that within the try portion, any error will instantly end the execution of the try portion and begin the execution of the except portion, preventing the execution of any lines following the line raising an error in the try portion


# --------------------- Imports ---------------------
from pathlib import Path
import os
import sys
import time

os.system('pip install wmi')
import wmi
wmi= wmi.WMI() # Gives us a class nickname to call when executing related functions like x.Win32_Processes(), for example, where x = wmi 

# --------------------- Global Variables ---------------------

pathLocalDirectory = os.path.dirname(os.path.realpath(__file__))
# Stores the directory of this file - Used to determine the directory to be searched for the master file
# Should be "X:\Code\Python\queklinProhibition", with X being the drive letter 

pathDriveDirectory = ((pathLocalDirectory).split("\\"))[0] + "\\"
# Stores the directory of the drive this file is in - May or may not have a use, TBD
# Should be "X:\" with X being the drive letter

# Note 1 - Double backslashes

pathMasterFile = pathLocalDirectory + "\\pythonQueklinMasterFile.txt"
# Stores the pathway of the master file - Used to quickly reference the Master file without having to repeatedly locate it using functionFileLocator.
# Note 1 - Double backslashes

statusClockedIn = False

timeStart = None
timeEnd = None

masterList = []
with open(pathMasterFile) as file:
	fileOriginal = file.read().splitlines()

masterTime = masterList[0]
masterProcess = masterList[1]
# --------------------- General Function Defining ---------------------
# Note 2 - Function purposes clarification

# Ensure the master exists, and creates it if not.
def functionFileLocator():
	try:
		print("DEBUG/INFORM: Determining Master File Presence.")
		open(pathMasterFile, "x").close() # .close() automatically closes it, preventing resource leaks and avoiding using a with statement
		print("DEBUG: File Not Found, Writing.")
		with open(pathMasterFile, "w") as file:
			file.write("000 \n prohibitedAppPathwayList#\n prohibitedAppNameList#") # Play time in seconds
		print("DEBUG/SUCCESS: pythonQueklinMasterFile.txt Created.")
		# with open(
		
			
		# Note 3
	except (FileNotFoundError, IOError):
		print("DEBUG/SUCCESS: File Found. Continuing.")


def functionClearTerminal():
	os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal




# --------------------- Main Menu Function Defining ---------------------


# ==== Function: Clock In ====

def functionFormatTime(sec):
  mins = sec // 60 # Minutes
  sec = sec % 60 # Seconds leftover after converting to minutes
  hours = mins // 60 # Hours
  mins = mins % 60 # Minutes leftover after converting to hours
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

# Example code stolen from a website:
	# input("Press Enter to start")
	# start_time = time.time()
	# input("Press Enter to stop")
	# end_time = time.time()
	# time_lapsed = end_time - start_time
	# time_convert(time_lapsed)


def functionClockIn():
	# Begins clocked-in stopwatch
	statusClockedIn == True
	timeStart = time.time()

	# Begins watchers to ensure queklin is prohibited





# ==== Function: Prohibition Lists ====
# Remember that prohibited app process names are stored on line 2, and prohibited app names stored on line 3 of the master file
def functionProhibitionMenu():
	statusProhibitionMenu = True
	while(statusProhibitionMenu):
		print("Prohibition Menu")
		print("1. Add New Process To Monitoring List")
		print("2. Remove Processes From Monitoring List")
		print("3. Display Monitoring List")
		inputProhibitionMenu = input("INPUT: Enter Desired Options Number.")
		listProcessChamber = []
		match inputProhibitionMenu:
			case "1":
				inputProcessName = input("INPUT: What Is The Name Of The Application You Would Like To Add?")
				print("INFORM: If Multiple Processes Are Found Containing '%s', Do Not Worry. You Will Be Able To Decide Which You Would Like To Add To The Prohibition List After They Are Found.\n ---")
				input("INPUT: Please Open %s And Press Enter Once It Has Fully Booted Up." % inputProcessName)
				for process in wmi.Win32_Process():
					ticker = 0
					if process.name in inputProcessName:
						print("SUCCESS: %s Was Found. Adding To Chamber List." % process.name)
						listProcessChamber.append(process.name)
				if(len(listProcessChamber) == 0):
					print("ERROR: No Process Found With %s In It's Name.")
					inputManualProcessName = input("INPUT: Would You Like To Manually Enter The Name Of The Desired Process? Y/N")
					if(inputManualProcessName.upper == "Y"):
						print("INFORM: To Find The Name Of Your Process, Press The Windows Button, Type 'Powershell' And Press Enter, Then Type 'ps' Into The Console And Search For The Name Of Your Process.")
						statusManualInput = True
						while(statusManualInput):
							print("Type '=' To Finish Inputting.")
							inputManualInput = input("INPUT/INFORM: Enter The Name Of The Process. ONLY DO THIS IF YOU ARE CONFIDENT IT IS THE PROCESS ASSOCIATED WITH YOUR DESIRED APPLICATION.")
							if(inputManualInput == "="):
								statusManualInput = False
							else:
								print("SUCCESS: %s Added To Chamber List." % inputManualInput)
								listProcessChamber.append(inputManualInput)
				else:
					functionClearTerminal()
					print("INFORM: Processes Found Are As Follows.")
					for process in listProcessChamber:
						print(process)
					inputChamberListAdd = input("INPUT: Would You Like To Add These Processes To The Prohibition List? Y/N")
					if(inputChamberListAdd.upper == "Y"):
						print("SUCCESS: Adding To List")




							
# print("SUCCESS: Process %s Found, Adding To Chamber List." % process.name)








# --------------------- Actual program ---------------------





print("INFORM: Good Morning, User.")
varName = input("QUERY: Who Are We Today?: ")

print("SUCCESS: Confirmed, Let Us Begin %s" % varName)
print("---")

functionFileLocator()
functionClearTerminal()

statusMainMenu = True
while(statusMainMenu):
	print("Main Menu.")
	print("0. End program.")
	print("1. Clock In")
	print("2. Clock Out")
	print("3. Display Current Clock In Information")
	print("4. Display Clockout Information")
	print("5. To-Do And Prohibition Lists")

	inputMainMenu = input("INFORM/INPUT: Enter Desired Options Number")
	match inputMainMenu:
		case "0":
			functionClearTerminal()
			if(statusClockedIn == True):
				statusLocal = True
				while(statusLocal):
					inputExitProgramClockedIn = ("INPUT: You Are Currently Clocked In, Are You Sure You Would Like To Clock Out? Y/N")
					if(inputExitProgramClockedIn.upper() == "Y"):
						print("SUCCESS: Exiting Program")
# CLOCK OUT NEEDS TO BE PUT HERE WHEN THE CLOCKOUT FUNCTION IS MADE!!!!!
						sys.exit # Exits the program
			else:
				print("SUCCESS: Exiting Program. ")
				sys.exit

		case "1":
			print("SUCCESS: Clocking In.")
			print("INFORM: This Program Will Run In The Background And Can be Interacted With While Clocked In, However It Must Remain Open.")
			input("INFORM: Press Enter To Continue")
			functionClockIn()

		case "2":
			print("xxx")
# Clock Out implementation to be done later, for now this print function serves to prevent errors
		case "5":
			print("QUERY: Where Would You Like To Go?")
			print("1. To Do lists")
			print("2. Prohibition Lists")
			inputToDoOrProhibition = input("INPUT: Enter Desired Options Number")
			match inputToDoOrProhibition:
				case "1":
					print("xxx")
# To-Do Menu Implementation To Be Done, for now this print function serves to prevent errors
				case "2":
					functionClearTerminal()
					print("SUCCESS: Entering Prohibition Menu Now.")
			





