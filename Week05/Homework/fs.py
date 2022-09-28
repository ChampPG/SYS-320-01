# File to traverse a given directory and it's subdirs and retrieve all the files.
import os, sys, argparse, yaml, re
from sys import platform

try:
    with open('searchTerms.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)

except EnvironmentError as e:
    print(e.strerror)

# parser
parser = argparse.ArgumentParser(

    description="Look through directory of logs using searchTerms",
    epilog="Developed by Paul Gleason, 20220921"
)

# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="False", help="Directory of logs you want to look through")
parser.add_argument("-s", "--searchTerm", required="False", help="Selected Search Term | Avaible Terms: registry, javascript, powerhsell")


# Parse the arguments
args = parser.parse_args()

# print(keywords)

rootdir = args.directory
searchTerm = keywords[args.searchTerm]
print(searchTerm)

# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print('invalid dir => {}'.format(rootdir))
    exit()

# List to save files
fList = []

# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):
    
    for f in filenames:
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

    listOfKeywords = terms.split(", ")
    # print(listOfKeywords)

    # Open a file
    with open(filename) as f:
        #'logs/'+

        # read in the file and save it to a variable
        contents = f.readlines()
        
    # List to store the results
    results = []
    # Loop through list and return each element is a line form the smallSyslog file
    for line in contents:
        
        # Loops through keywords list
        for eachKeyword in listOfKeywords:
            
            # If the 'line' contains the keywork then it will print
            #if eachKeyword in line:
            # Searches and returns results using a regular expression search
            x = re.findall(r''+eachKeyword+'', line)
        
            for found in x:
                
                # Append the returned keyworks to the results list
                results.append(found)
        
    # Sort the list    
    results = sorted(results)


    for line in results:
        print("""
            traffic: 'suspicious traffic'
            line: {}
            """.format(line))

# Main Function Call
for f in fList:
    _syslog(f, searchTerm)