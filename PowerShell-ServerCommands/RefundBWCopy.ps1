<# This is powerShell Script to read Schedule report and Black & white Copy job
Enviroment Variables: 
	-"$reportCsv": Please set this as per your Scheduled Resport
	-The PaperCut is instaled in C:\Program Files\PaperCut MF\
		
Tested with PaperCut 6.3 and Powershell 5 on windowws 10		

	Author: Nikhil Singh
#>


# Report Dump Location and Report File name. Please Configure scheduled Resport
$reportLoc = 'C:\Program Files\PaperCut MF\server\data\scheduled-reports'
$reportCsv = 'ScheuleGroup.csv'

# Location where server-commands.exe 
$binLoc =  'C:\Program Files\PaperCut MF\server\bin\win'

# Open directory to Report Location
Set-Location $ReportLoc

$today = (get-date).Date

# Check if File Exist & If its created today or not.
if (!(Test-Path $reportCsv)){
    "$(get-date) : Can't find the report File" | Out-File -LiteralPath ScriptError.txt -Append
    Return

} ElseIf ( (Get-ChildItem $reportCsv).CreationTime.Date -ne $today ){
    "$today : This an old report" | Out-File -LiteralPath ScriptError.txt -Append
     Return
}


# Proces Report to get csv data grouped by UserID.
$t = (Select-String  -Path "$reportCsv" -Pattern '^[^#|"#]').Line | ConvertFrom-Csv |
    Where-Object {
            ($_.Cost -as [int] -gt 0) -and
            ($_.'Total Color Pages' -as [int] -EQ 0) #-and
#           ($_.'Refunded' -EQ 'NOT_REFUNDED') # -and
#           ($_.'Use Type' -EQ 'COPY')                      
    } |
    Group-Object -Property 'Username'

# change directory to PaperCut bin location
Set-Location  $binLoc
 foreach ($i in $t){
       $amt = ($i.group | Measure-Object -Property 'Cost' -Sum).Sum 
       $userId = $i.Name 
       $userId
       .\server-command.exe adjust-user-account-balance-if-available $userId $amt bwCopy_Refund_Vis_Script
}