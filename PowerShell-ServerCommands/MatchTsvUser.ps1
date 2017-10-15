<# This script will read the content of "C:\tmp\test1.tsv" file 
 and compare them If those IDs exist in Surver.
 If yes it will list them in C:\tmp\test2.ts
#>
cd 'C:\Program Files\PaperCut MF\server\bin\win\'
[array]$f1 = @()
[array]$f2 = @()

$f1 = (Get-Content  C:\tmp\test1.tsv).Split(",").Trim(" ")

Foreach ($name in $(.\server-command.exe list-user-accounts))
{
    if ($f1 -contains $name )
    {
         $f2 +="$name"
    }

}
Out-File -InputObject ($f2 -join ", ") -FilePath C:\tmp\test2.tsv