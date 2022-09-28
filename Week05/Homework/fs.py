# File to traverse a given directory and it's subdirs and retrieve all the files.
from importlib.resources import contents
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

# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="False", help="Directory of logs you want to look through")
parser.add_argument("-s", "--searchTerm", required="False", help="Selected Search Term | Avaible Terms: registry, javascript, powerhsell")


# Parse the arguments
args = parser.parse_args()

# print(args.searchTerm)

rootdir = args.directory
searchTerm = keywords[args.searchTerm]
# print(searchTerm)

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

    results = []
    with open(filename, encoding='utf-8') as csvfile:
        contents = csv.reader(csvfile)
        for _ in range(1):
            next(contents)
        for line in contents:
            # print(' '.join(line))
            # Loops through keywords list
            for eachKeyword in listOfKeywords:
                # print(eachKeyword)
                # If the 'line' contains the keywork then it will print
                #if eachKeyword in line:
                # Searches and returns results using a regular expression search
                x = re.findall(r''+eachKeyword+'', ' '.join(line))
                for found in x:
                    results.append(found)
                    # if len(results) > 0:
                    #     for item in results:
                    #         if not item[0] == found[0]:
                    #             results.append(found)
                    # else:
                    #     results.append(found)

    results.sort()

    for line in results:
        print("""
            file: {}
            line: {}
            """.format(filename, line))

# Main Function Call
for f in fList:
    _syslog(f, searchTerm)