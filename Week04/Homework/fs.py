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
parser.add_argument("-s", "--searchTerm", required="False", help="Selected Search Term | Avaible Terms: shell_attacks, sql_attacks, traversal_attacks, cms_attacks")
parser.add_argument("-r", "--returnAttack", required="False", help="If only suspicious traffic enter 1, only non-suspicious 2, and both 3. example: -r 1 will return all suspicious traffic")

# Parse the arguments
args = parser.parse_args()

# print(keywords)

rootdir = args.directory
searchTerm = keywords[args.searchTerm]
returnValue = args.returnAttack
# print(returnValue)

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

    suspicious = []
    nonsuspicious = []

    for line in results:
        split_line = line.split(" ")
        if int(split_line[8]) == 200 and int(split_line[9]) >= 1000:
            suspicious.append(line)
        else:
            nonsuspicious.append(line)

    if int(returnValue) == 1:
        for line in suspicious:
            print("""
            traffic: 'suspicious traffic'
            line: {}
            """.format(line))
    elif int(returnValue) == 2:
        for line in nonsuspicious:
            print("""
            traffic: 'non-suspicious traffic'
            line: {}
            """.format(line))
    elif int(returnValue) == 3:
        for line in suspicious:
            print("""
            traffic: 'suspicious traffic'
            line: {}
            """.format(line))
        for line in nonsuspicious:
            print("""
            traffic: 'non-suspicious traffic'
            line: {}
            """.format(line))

# Main Function Call
for f in fList:
    _syslog(f, searchTerm)