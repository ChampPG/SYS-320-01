# List the files in a directory and
# Get-ChildItem -Recurse -Path .\Documents
# Get-ChildItem -Recurse -Include *.pdf -Path .\Documents
#                                   (*.file extension)

# List all files and print the full path
#Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt -Path .\Documents | Select FullName

Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt -Path .\Documents | Export-Csv `
-Path .\files.csv

# Import the csv file.
$fileList = Import-Csv .\files.csv -Header FullName


# Loop through the results
foreach ($f in $fileList) {

    Get-ChildItem -Path $f.FullName

}