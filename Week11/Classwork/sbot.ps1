# Send an email using Powershell


$toSend = @('dune@mymail.champlain.edu','null@champlain.edu','dunston@champlain.edu')

# Message body
$msg = "Hello"


while($true) {

    foreach ($email in $toSend) {

        # Send the email
        Write-Host "Send-MailMessage -From 'dunston@mymail.champlain.edu' -To $email -Subject 'Tisk Tisk' `
        -Body $msg -SmtpServer X.X.X.X"

        # Pause for 1 second
        #start-sleep 1

    }

}