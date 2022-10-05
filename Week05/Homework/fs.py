# File to traverse a given directory and it's subdirs and retrieve all the files.
import os, sys, argparse, yaml, re, csv
from sys import platform

try:
    with open('searchTerms.yaml', 'r', errors='ignore') as yf:
        keywords = yaml.safe_load(yf)

except EnvironmentError as e:
    print(e.strerror)

# parser
parser = argparse.ArgumentParser(
    description="Look through directory of logs using searchTerms",
    epilog="Developed by Paul Gleason, 20220921"
    )

# Add argument for directory
parser.add_argument(
    "-d", 
    "--directory", 
    required="False", 
    help="Directory of logs you want to look through"
    )

# Add arguement for search term
parser.add_argument(
    "-s", 
    "--searchTerm", 
    required="False", 
    help="Selected Search Term | Avaible Terms: registry, javascript, powerhsell"
    )


# Parse the arguments
args = parser.parse_args()

# print(args.searchTerm)

# Set rootdir to directoy
rootdir = args.directory
# Set searchTerm from searchTerm input
searchTerm = keywords[args.searchTerm]

# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print('invalid dir => {}'.format(rootdir))
    exit()

# List to save files
fList = []

# Crawl through the provided directory
for root, subfolders, filename in os.walk(rootdir):
    
    for f in filename:
        # print(root + '\\' + f)

        # If linux system
        if platform == 'linux' or platform == 'linux2':
            fileList = root + '/' + f

        # If OS X System
        # elif platform == 'darwin':

        # If windows system
        elif platform == 'win32':   
            fileList = root + '\\' + f

        #print(fileList)
        fList.append(fileList)

# Create an interface to search through each log file
def _syslog(filename, service):

    # Query the yaml file for the 'term' or direction and
    # retrieve the strings to search on.
    terms = service

    # Split terms to make listOfKeywords
    listOfKeywords = terms.split(", ")

    # Create list for results
    results = []
    with open(filename, encoding='utf-8') as csvfile:
        contents = csv.reader(csvfile)

        # Skip first row
        for _ in range(1):
            next(contents)
        for line in contents:
            # Loops through keywords list
            for eachKeyword in listOfKeywords:
                # print(eachKeyword)
                # If the 'line' contains the keywork then it will print
                #if eachKeyword in line:
                # Searches and returns results using a regular expression search
                x = re.findall(r''+eachKeyword+'', ' '.join(line))
                for found in x:
                    results.append(found)
    
    # Sort results for neater list
    results.sort()

    # This will loop through the results list and remove some of the duplicates to make output smaller
    for item in range(len(results)-1):
        if results[item][0] == results[item+1][0] and len(results[item]) < len(results[item+1]):
            results.pop(item)

    # Output the filename and the line. I know you didn't want the line number but I feel it should be included because this can indicate to other threats in that csv
    for line in results:
        print("""
            file: {}
            line: {}
            """.format(filename, line))

# Main Function Call
for f in fList:
    _syslog(f, searchTerm)