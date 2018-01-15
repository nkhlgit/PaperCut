#ImportJobs
  This will  read the CSV and import Job logs from "Joblog_template.csv" to PaperCut Server
  Folder Contains readme, Joblog_template.csv and ImportJobLog.py

#adjustAccBalPerRow.py
	This will read the "aub.csv" from c:\\tmp directory. Skip first row. raed the user ID and balance to balance. The abub.csv format should be like:
	User,amount
	Tom,10
	john,20

#adjustBalPerFile.py
	This script will addjust amount to users listed in specific file.
	create three files on 'Web-Service Client Machine': u20.txt, u15.txt and u7.txt.6. 
	In u20.txt list down the name of all "User ID" (avoid any space ) seprated by new line who should be allocated £20. 
	In u15.txt list down the name of all "User ID" (avoid any space ) separated by new line who should be allocated £15. 
	In u7.txt list down the name of all "User ID" (avoid any space ) separated by new line who should be allocated £7.

#listSharedAccPin.py
	list the account name and pin numbers. OutPut the File will create a "SharedAccountPin.csv" in C:\tmp directory. 

#listUserProperties.py
	List down properties of users. This wull create UserIdProperty.csv' in C:\temp folder..
UserID','account-selection.mode','account-selection.can-charge-personal','account-selection.can-charge-shared-from-list','account-selection.can-charge-shared-by-pin''auto-shared-account','default-shared-account'


#userGroupSync.py
	This script will run UseAnd Group Synch whenever it runs