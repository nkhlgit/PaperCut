<# This script is to adjust user accoutn balanace
	This is the path from wher this script will pull userID, amount and comment.
	The format should be <UserID><space><Amount><space><coment_without_any_space>
Author: Nikhil Singh
#> 


#Example: nikhil 100 AdjustBalancce 
$InputFile = "C:\tmp\UserAmountList.txt"

# Select the server command
$call = "adjust-user-account-balance"

# Read the Input file and execute each line
cd 'C:\Program Files\PaperCut MF\server\bin\win'
foreach ($line in  (Get-Content -Path $InputFile)) {
$name = $line.Split()[0]
$amount = $line.Split()[1]
$comment = $line.Split()[2]
.\server-command.exe $call $name $amount $comment
}
pause