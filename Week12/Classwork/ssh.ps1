# Login to a remote SSH server
#New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential paul.gleason) -Port '2222'

<#
while ($True) {

    # Add a prompt to run commands
    $the_cmd = Read-Host -Prompt "Please enter a command"

    # Run command on remote SSH server
    (Invoke-SSHCommand -index 0 $the_cmd).Output

}
#>

#Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential paul.gleason) -Port '2222' `
#-Destination '/home/paul.gleason' -Path './Week12/Classwork/pid2.txt'

# Close SSH connection
Remove-SSHSession -SessionId 0

<#
Notes
Get-SSHSession - Shows you active sshd

#>