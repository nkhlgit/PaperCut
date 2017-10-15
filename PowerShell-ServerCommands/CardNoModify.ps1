<# This is the Script to subsiture '.' with '-' for all users in PaperCut
 Author: Nikhil Singh
#>

cd 'C:\Program Files\PaperCut MF\server\bin\win\'
Foreach ($name in $(.\server-command.exe list-user-accounts))
{

$card = ''
$card = $(.\server-command.exe get-user-property $name primary-card-number) 

$card
if ( $card -ne ''){
        $card = 
        $card = $card.Substring(0,10) -replace ‘[.,-]’,'' 

    .\server-command.exe set-user-property $name primary-card-number $card
}
}
"Done"