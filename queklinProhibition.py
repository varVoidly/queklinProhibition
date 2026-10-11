# --------------------- LEFT OFF AT: Line 170 ---------------------
# This program has Todos scattered around that can be tracked by using ctrl+f and searching for "Todo:" without the quotations

# --------------------- Notes ---------------------
# Note 00: Note 0's are used for general notes that are not referenced anywhere in the code.

# Note 01: Yes, i am fully aware(at the time of writing this, v0.1.0) that the current version can only handle a single file/profile. That may or may not change down the line when I finish the program and think "hmmmm, having a profiles system sure would be nice".
 

# Note 1: Note how we use two back slashes in the split and addition operator string. One slash is used as a string/escape operator and has an effect on the string its within dependant on the character that follows the slash. By adding two backslashes, the first backslash "escapes" the second backslash, allowing it to exist without being interpreted as an effector that does not have a defined purpose(due to the lack of a character following it)

# Note 2: Some functions are not created to reduce repetition, but rather to organize the script itself. functionFileLocator, for example, is only called at the start of the file however this line of the script is in between welcoming the user and presenting them the action menu, while the process of the function itself presents no user interaction. Thus, to make it look nicer, the process is defined as a function and instead called at the appropriate line instead of clogging up the segment.


# Note 3: open("filepath", "x") errors throw the subclass error "FileNotFoundError" AND the class error "IOError". Use "except (FileNotFoundError, IOError):" to catch whichever appears, or catch both, im not fully sure. Note that within the try portion, any error will instantly end the execution of the try portion and begin the execution of the except portion, preventing the execution of any lines following the line raising an error in the try portion

# --------------------- Ideas ---------------------
# Theoretical 1: Instead of finding processes, instead ask for the directory of the prohibited application, then kill processes that start from that directory
# Practical 1.1: How will we know when a process starts from that directory? 
# --------------------- Imports ---------------------
from pathlib import Path
import os
import time

# os.system('pip install wmi')
# Source - https://stackoverflow.com/a/50255019
# Posted by Aaron de Windt, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-18, License - CC BY-SA 4.0

import subprocess
import sys
    
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("wmi")
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
	masterList = file.read().splitlines() # Establishes the master list as a list with each element being each line

masterTime = map(int, masterList[0].split("#")) # Establishes the masterTime list by splitting the first line into elements deliminated by the hastag symbol and then turns each string element into an integer
masterProcess = masterList[1].split("#") # Establishes the masterProcess list by splitting the second line into elements deliminated by the hastag symbol
masterNickname = masterList[2].split("#") # Establishes the masterNickname list by splitting the third line into elements deliminated by the hastag symbol
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

def functionUpdateMasterFile():
	updateMasterTime = "#".join(map(str, masterTime)) # Converts the integers of the masterTime list to strings and then joins that list into one single string with each element separated by hashtags
	updateMasterProcess = "#".join(masterProcess) # Joins each element of masterProcess into a string with each element separated by hashtags
	updateMasterNickname = "#".join(masterNickname) # Joins each element of masterNickname into a string with each element separated by hashtags

	
	updateMasterFile = updateMasterTime + "\n" + updateMasterProcess + "\n" + updateMasterNickname
	with open(pathMasterFile, "w") as file:
		file.write(updateMasterFile)




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
		print("1. Add New Process To Monitoring List") # This section is completed, but not tested, as of 0.1.7.
		print("2. Remove Processes From Monitoring List")
		print("3. Display Monitoring List")

		inputProhibitionMenu = input("INPUT: Enter Desired Options Number: ")
		listProcessChamber = [] # Prepares the process chamber list for use throughout the function
		listNicknameChamber = [] # Prepares the nickname chamber list for use throughout the function

		match inputProhibitionMenu:
			case "1":
				inputProcessName = input("INPUT: What Is The Name Of The Application You Would Like To Add?: ") #  Asks for and stores the name of processes to search for, doesnt actually do anything with them yet 
				print("INFORM: If Multiple Processes Are Found Containing '%s', Do Not Worry. You Will Be Able To Dcide Which You Would Like To Add To The Prohibition List After They Are Found.\n ---")
				input("INPUT: Please Open %s And Press Enter Once It Has Fully Booted Up: " % inputProcessName) # Asks to boot up the desired programs so they can be found
				for process in wmi.Win32_Process(): # Iterates through each processes in the Win32_Process list
					if process.name in inputProcessName: # If the current process matches the input:
						print("SUCCESS: %s Was Found. Adding To Chamber List. \n ---" % process.name) 
						listProcessChamber.append(process.name) # Adds the process name to the list, but not a nickname(multiple processes can be found with the same input)
				if(len(listProcessChamber) == 0): # If no proceses are found
					print("ERROR: No Process Found With %s In It's Name." % inputProcessName)
					inputManualProcessName = input("INPUT: Would You Like To Manually Enter The Name Of The Desired Process? Y/N: ")
					if(inputManualProcessName.upper == "Y"):
						print("INFORM: To Find The Name Of Your Process, Press The Windows Button, Type 'Powershell' And Press Enter, Then Type 'ps' Into The Console And Search For The Name Of Your Process.")
						statusManualInput = True
						while(statusManualInput):
							print("Type '=' To Finish Inputting.")
							inputManualInput = input("INFORM: ONLY DO THIS IF YOU ARE CONFIDENT IT IS THE PROCESS ASSOCIATED WITH YOUR DESIRED APPLICATION. \n INPUT: Enter The Name Of The Process To Directly Add It To The Prohibition List: ") # Adds the manual entry to a seperate, manual input variable
							if(inputManualInput == "="): 
								statusManualInput = False
							else:
								print("SUCCESS: %s Added To Chamber List." % inputManualInput)
								listProcessChamber.append(inputManualInput) # Adds the manual input variable to the process chamber.
				functionClearTerminal() # Clears the terminal after processes have been found/entered
				print("INFORM: Processes Found Are As Follows. Please Enter A Nickname For Each Process As They appear. Type 'Remove This Process' If You Want To Specifically Remove The Current Process.")
				for process in listProcessChamber: # Iterates through current processes in the chamber
					inputProcessNickname = input("Nickname for '%s': " % process) # Gets a nickname
					if(inputProcessNickname.lower == "Remove This Process"):
						print("SUCCESS: Removing %s From The Process List." % process)
						listProcessChamber.remove(process)
					else:
						listNicknameChamber.append(inputProcessNickname) 
				statusAddingChambers = True
				while(statusAddingChambers):
					inputChamberListAdd = input("INPUT: Would You Like To Add These Processes To The Prohibition List? Y/N: ") # Final confirmation
					if(inputChamberListAdd.upper == "Y"):
						print("SUCCESS: Adding To List And Returning To Prohibition Menu.")
						masterProcess.extend(listProcessChamber) # Adds each element of the process chamber to the masterProcess, does NOT add listProcessChamber as a list though (which is what would happen if we used .append)
						masterNickname.extend(listNicknameChamber) # Adds each element of the nickname chamber to the masterNickname, does NOT add listNicknameChamber as a list though (which is what would happen if we used .append)

						listProcessChamber.clear() # Clears the chambers for the next use.
						listNicknameChamber.clear()

						statusAddingChambers = False
					elif(inputChamberListAdd.upper == "N"):
						print("SUCCESS: Discarding Chambers And Returning To Prohibition Menu.")
						listProcessChamber.clear()
						listNicknameChamber.clear()

						statusAddingChambers = False
					else:
						print("ERROR: Unknown Input Detected. Please Try Again.")
				







							
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

	inputMainMenu = input("INFORM/INPUT: Enter Desired Options Number: ")
	match inputMainMenu:
		case "0":
			functionClearTerminal()
			if(statusClockedIn == True):
				statusLocal = True
				while(statusLocal):
					inputExitProgramClockedIn = ("INPUT: You Are Currently Clocked In, Are You Sure You Would Like To Clock Out? Y/N: ")
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
			inputToDoOrProhibition = input("INPUT: Enter Desired Options Number: ")
			match inputToDoOrProhibition:
				case "1":
					print("xxx")
# To-Do Menu Implementation To Be Done, for now this print function serves to prevent errors
				case "2":
					functionClearTerminal()
					print("SUCCESS: Entering Prohibition Menu Now.")
			





