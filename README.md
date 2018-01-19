# PowerShell-ServerCommands: 
 Contains various Powershell script to perform specifc tasks using "PaperCut Server Commands". Here is the link having detail of Server Command: https://www.papercut.com/products/ng/manual/common/topics/tools-server-command.html
  
#  Python-WebXML: 
 Contains various Python scripts to perform specifc tasks using "PaperCut XML Web Services APIs". Here is the link having detail of The XML Web Services API: https://www.papercut.com/products/ng/manual/common/topics/tools-web-services.html

## ImportJobs: 
This will read the CSV and import Job logs from "Joblog_template.csv" to PaperCut Server Folder Contains readme, Joblog_template.csv and ImportJobLog.py

## adjustAccBalPerRow.py:
This will read the "aub.csv" from c:\tmp directory. Skip first row. raed the user ID and balance to balance. The abub.csv format should be like: User,amount Tom,10 john,20

## adjustBalPerFile.py: 
This script will addjust amount to users listed in specific file. create three files on 'Web-Service Client Machine': u20.txt, u15.txt and u7.txt.6. In u20.txt list down the name of all "User ID" (avoid any space ) seprated by new line who should be allocated £20. In u15.txt list down the name of all "User ID" (avoid any space ) separated by new line who should be allocated £15. In u7.txt list down the name of all "User ID" (avoid any space ) separated by new line who should be allocated £7.

## listSharedAccPin.py:
List the account name and pin numbers. OutPut the File will create a "SharedAccountPin.csv" in C:\tmp directory.

## listUserProperties.py:
List down properties of users. This wull create UserIdProperty.csv' in C:\temp folder.. UserID','account-selection.mode','account-selection.can-charge-personal','account-selection.can-charge-shared-from-list','account-selection.can-charge-shared-by-pin''auto-shared-account','default-shared-account'

## userGroupSync.py:
This script will run UseAnd Group Synch whenever it runs

## addInternalUser.py:
Created on 18 Jan. 2018 @author: nikhils
This script is to create internal users in Bulk using web-xml API..
it reads batch-internal-user-example.tsv from c:\tmp directory and set properties.Please refrence.
Pros=> Remove the dependency to access Server terminal access to run server command and put tsv file.
 	Critical steps before running the script>  
    		- Install Python3; 
    		- Enable Web-XML API on Server.
    		- Create batch-internal-user-example.tsv file. 
      		Refer => https://www.papercut.com/products/ng/manual/applicationserver/topics/user-guest-internal.html#user-guest-internal-import-file-format


#  Python: 
Contains python script to play with reports and csv file.
	
## addEmailPrintSummery.py: 
Run "user list" and "User printing - summary" Reports from "PaperCut web-admin >> Reports >> User" in CSV format to get "user_list.csv" and "print_summary_by_user.csv" . Save the both files in  "c:\tmp" location. Run this script. This script read email address of users from  and map them with user ID in the Output file is "print_summary_by_user_Email.csv" in "c:\tmp"
	
##  printPer.py:
Input file    =>  print_logs_by_printer.csv in c:\tmp\ folder 
Output file   => is target in c:\tmp\. Enter letter in 1St Arguments : a for all; h for hour;w for weekday;m for month number 
		Example: 
		"printPer.py"   i.e. without argument will list Print per hour by default
		"printPer.py a" will print all data
		"printPer.py wd" will print week and day  
		
# Go:
Conatin Scripts in Go Lang to Perform specific tasks.
	
## ImportJobLogs:
This will use PaperCut WebXML API to to connect PaperCut. Please check the IP and Token in follwing lines of script as per your PaperCut Server.
		v.Param[0].Arg1 = "token" 
		req, err := http.NewRequest("POST", "http://127.0.0.1:9191/rpc/api/xmlrpc", bytes.NewBuffer([]byte(output)))
		This will  read the CSV and import Job logs from "c:\temp\Joblog_template.csv" to PaperCut Server	
