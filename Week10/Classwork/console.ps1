# Get a list of running processes
#Get-process

# Get list of members | Get-Member shows all available properites for cmdlt
#Get-process | Get-Member


# Get a list of processes: name, id, path
#Get-Process | Select ProcessName, Id, Path


# Save the Output to a CSV file
#Get-Process | Select ProcessName, Id, Path | Export-Csv -Path "get-process.csv"

$OutputName = "services.csv"
# System Services and properties
#Get-Service | Get-Member
Get-Service | Select-Object Status, Name, DisplayName, BinaryPathName  | Export-Csv -Path $OutputName


# Get a list of running services
#Get-Service | Where-Object { $_.Status -eq "Running" } | Export-Csv -Path $OutputName

# Check to see if the file exists
if ( Test-Path $OutputName) {
    Write-Host -BackgroundColor "Green" -ForegroundColor "White" "File was created!"
} else {
    Write-Host -BackgroundColor "Red" -ForegroundColor "White" "File was not created!"
}


