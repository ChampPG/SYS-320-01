# Array of websites containing threat intell
$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

$var = Read-Host -Prompt "Please enter Windows or IPTables"

# Loop Through the URLs for the rules list
foreach ($u in $drop_urls) {

    # Extract the filename
    $temp = $u.Split("/")
    # The last element int he array plucked off is the filename
    $file_name = $temp[-1]

    if (Test-Path "./Week12/Homework/$file_name") {
        continue
    } else {
    # Download the rules list
    Invoke-WebRequest -Uri $u -OutFile "./Week12/Homework/$file_name"
    }
}

# Array containing the filename
$input_path = @("./Week12/Homework/compromised-ips.txt","./Week12/Homework/emerging-botcc.rules")

# Extract the IP addresses
# 108.190.109.107
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Append the IP addresses to the temporary IP list
Select-String -Path $input_path -Pattern $regex_drop | `
ForEach-Object { $_.Matches } | `
ForEach-Object { $_.Value } | Sort-Object | Get-Unique | `
Out-File -FilePath "./Week12/Homework/ips-bad.tmp"

# Get the IP addresses discovered, loop through and replace the beginning of th eline with the IPTables syntax
# After the IP address, add the remaining IPTables syntax and ave the results to a file.
# iptables -A INPUT -s IP -j DROP

switch ($var) {
    'Windows' {  
        (Get-Content -Path "./Week12/Homework/ips-bad.tmp") | % `
        { $_ -replace "^" , "New-NetFirewallRule -DisplayName 'Bad IP Blocker' -Direction OutBound -LocalPort Any -Protocol Any -Action Block -RemoteAddress " -replace "$" } | `
        Out-File -FilePath "./Week12/Homework/Firewall.ps1"
    }
    'IPTables' {
        (Get-Content -Path "./Week12/Homework/ips-bad.tmp") | % `
        { $_ -replace "^" , "iptables -A INPUT -s " -replace "$", " -j DROP" } | `
        Out-File -FilePath "./Week12/Homework/iptables.bash"
        Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential paul.gleason) -Port '2222' `
        -Destination '/home/paul.gleason/' -Path './Week12/Homework/iptables.bash'

        New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential paul.gleason) -Port '2222'
        (Invoke-SSHCommand -index 0 "ls -la").Output
    }
}

