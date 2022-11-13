# Task 1
Copy-Item "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -Destination "C:\Users\paul.gleason"

$random = Get-Random -Minimum 1000 -Maximum 9876

$NewName = "EnNoB-$random.exe"

Rename-Item -Path "C:\Users\paul.gleason\powershell.exe" -NewName $NewName

if ( Test-Path "C:\Users\paul.gleason\$NewName") {
    Write-Host "File is Found!"
} else {
    Write-Host "error"
}


# Task 2
$message = "If you want your files restored, please contact me at dunston@champlain.edu. I look forward to doing business with you." 
$message | Out-File -FilePath "C:\Users\paul.gleason\Desktop\Readme.READ"

if ( Test-Path "C:\Users\paul.gleason\Desktop\Readme.READ" ){
    Write-Host "File is Found!"
} else {
    Write-Host "Error ReadMe.READ not found"
}

<#
Reflection

What did you like the most and least about the assignment?
I enjoyed flow of this assignment from the last few.

What additional questions do you have?
 N/A

#>