# Features

* Clock in(amount of time spent working)



* Clock out(define amount of play time earned based on amount of time spent working)

  * Uses all clock in time available, does not leave any leftover.



* File defining names of processes that should be locked down

  * Also include the time period in which these should be locked down? Maybe
  * Psuedo code: Ask the user for the name of the application that should be locked down, ask them to open the application and press enter when it is fully running, then search processes for a process with that name. If found, add it to the prohibition list. If not found, advise the user on how to find the process and how to input the process name(or even ID) that will then be added to the prohibition list.



* Notification when play time is about to end (15m, 10m, 5m)

  * Psuedocode: z = x - a, x = play time available at start of playtime, a = 15, 10 and 5 for z15, z10 and z5, each z value is used as a countdown til the warning goes off



* \[DONE] Auto-locating of the masterFile(that holds info on play time, pathways and app names) and, if not found, auto creation of it

  * Locate the file at the start of the program. If the file is not found, set a global Boolean to false(file is not found), otherwise set it to true(file is found)



* To-Do List for that day

  * Maybe even a to-do list of past days that were not completed







\----- To-Do After 1.0 Release -----

* Shove main functions into another file that is referenced when needed to clean up the code a bit
* Add or allow manual assigning of names to processes in the master file(thats what line 3 is for, but its currently not used \[v0.1.4])

