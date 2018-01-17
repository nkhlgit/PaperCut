# PowerShell-ServerCommands: 
 Contains various Powershell script to perform specifc tasks using "PaperCut Server Commands". Here is the link having detail of Server Command: https://www.papercut.com/products/ng/manual/common/topics/tools-server-command.html
  
#  Python-WebXML: 
 Contains various Python scripts to perform specifc tasks using "PaperCut XML Web Services APIs". Here is the link having detail of The XML Web Services API: https://www.papercut.com/products/ng/manual/common/topics/tools-web-services.html

#  Python: 
Contains python script to play with reports and csv file.
	
	##	addEmailPrintSummery.py: 
		Run "user list" and "User printing - summary" Reports from "PaperCut web-admin >> Reports >> User" in CSV format to get "user_list.csv" and "print_summary_by_user.csv" . Save the both files in  "c:\tmp" location. Run this script. This script read email address of users from  and map them with user ID in the Output file is "print_summary_by_user_Email.csv" in "c:\tmp"
	
	##	printPer.py:
		Input file    =>  print_logs_by_printer.csv in c:\tmp\ folder 
		Output file   => is target in c:\tmp\. Enter letter in 1St Arguments : a for all; h for hour;w for weekday;m for month number 
		Example: 
		"printPer.py"   i.e. without argument will list Print per hour by default
		"printPer.py a" will print all data
		"printPer.py wd" will print week and day  
		
# Go:
Conatin Scripts in Go Lang to Perform specific tasks.
	
	##	ImportJobLogs:
		This will use PaperCut WebXML API to to connect PaperCut. Please check the IP and Token in follwing lines of script as per your PaperCut Server.
		v.Param[0].Arg1 = "token" 
		req, err := http.NewRequest("POST", "http://127.0.0.1:9191/rpc/api/xmlrpc", bytes.NewBuffer([]byte(output)))
		This will  read the CSV and import Job logs from "c:\temp\Joblog_template.csv" to PaperCut Server	
