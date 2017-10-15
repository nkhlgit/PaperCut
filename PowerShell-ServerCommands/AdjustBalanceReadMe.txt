PowerShell script "AdjustBalance.ps1" is to updated User Balance users.

1. Create Input test file: Please create a file and put in username in following format:  <UserID><SPACE> <amount><SPACE> <comment>
 Likewise, I have created list of three users to adjust balance of  +10$ to "nikhil"; +20$ to "mel"; and +30$ to shane :

nikhil 10 DailyAdjust
mel 20 DailyAdjust
shane 50 DailyAdjust

I saved the file as "C:\tmp\UserAmountList.txt"

2. I updated the varialble "$InputFile" of the script as  "C:\tmp\UserAmountList.txt". Likewise, at line-7 of the script after  "$InputFile =" string please append filename with absolute path of the file one you have created as per steps 1 above.

4. Please take the database backup in case you run the script for the first time so that you can revert the changes in case something goes wrong. Here is the step to take database backup: https://www.papercut.com/products/ng/manual/common/topics/sys-backups.html
