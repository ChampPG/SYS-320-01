# Create and interface to search through syslog files
import re, sys

def _syslog(filename, listOfKeywords):
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
                
                
    # Check to see if there are results
    if len(results) == 0:
        print("No Results")
        sys.exit(1)
        
    # Sort the list    
    results = sorted(results)
    
    return results
            # print(x)
