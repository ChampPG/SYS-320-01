# Array of websites containing threat intell
$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

# Loop Through the URLs for the rules list
foreach ($u in $drop_urls) {

    # Extract the filename
    $temp = $u.Split("/")
    # The last element int he array plucked off is the filename
    $file_name = $temp[-1]

    if (Test-Path "./Week12/Classwork/$file_name") {
        continue
    } else {
    # Download the rules list
    Invoke-WebRequest -Uri $u -OutFile "./Week12/Classwork/$file_name"
    }
}

# Array containing the filename
$input_path = @("./Week12/Classwork/compromised-ips.txt","./Week12/Classwork/emerging-botcc.rules")

# Extract the IP addresses
# 108.190.109.107
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Append the IP addresses to the temporary IP list
Select-String -Path $input_path -Pattern $regex_drop | `
ForEach-Object { $_.Matches } | `
ForEach-Object { $_.Value } | Sort-Object | Get-Unique | `
Out-File -FilePath "./Week12/Classwork/ips-bad.tmp"

# Get the IP addresses discovered, loop through and replace the beginning of th eline with the IPTables syntax
# After the IP address, add the remaining IPTables syntax and ave the results to a file.
# iptables -A INPUT -s IP -j DROP
(Get-Content -Path "./Week12/Classwork/ips-bad.tmp") | % `
{ $_ -replace "^" , "iptables -A INPUT -s " -replace "$", " -j DROP" } | `
Out-File -FilePath "./Week12/Classwork/iptables.bash"