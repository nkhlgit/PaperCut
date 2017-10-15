.\server-command.exe set-user-property aaronp primary-card-number 12,345,155-1
.\server-command.exe set-user-property abigailn primary-card-number 11,222,345-K
.\server-command.exe set-user-property adama primary-card-number 33.444.333-K
.\server-command.exe set-user-property adamb primary-card-number 44.666.111-5

.\server-command.exe set-user-property nikhils primary-card-number 
$card = $(.\server-command.exe get-user-property nikhils primary-card-number) 
$card
if ( $card -ne ''){$card}