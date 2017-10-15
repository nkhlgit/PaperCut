<# This script is to Delete users who had ZERO Print job
Author: Nikhil Singh
#>

cd 'C:\Program Files\PaperCut MF\server\bin\win\'
​​
Foreach ($name in $(.\server-command.exe list-user-accounts)){if ($(.\server-command.exe get-user-property $name print-stats.job-count) -eq 0){.\server-command.exe delete-existing-user $name}}
