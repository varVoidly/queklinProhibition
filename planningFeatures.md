# Features

* Clock in(amount of time spent working)
* Clock out(define amount of play time earned based on amount of time spent working)

  * Uses all clock in time available, does not leave any leftover.
* File defining pathways to applications that should be locked down

  * Also include the time period in which these should be locked down? Maybe
* Notification when play time is about to end (15m, 10m, 5m)

  * Psuedocode: z = x - a, x = play time available at start of playtime, a = 15, 10 and 5 for z15, z10 and z5, each z value is used as a countdown til the warning goes off
* Auto-locating of the masterFile(that holds info on play time, pathways and app names) and, if not found, auto creation of it

  * Locate the file at the start of the program. If the file is not found, set a global Boolean to false(file is not found), otherwise set it to true(file is found)

