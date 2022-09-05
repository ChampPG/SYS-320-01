import syslogCheck
import importlib
importlib.reload(syslogCheck)

# SSH authentication failures
def ssh_opened(filename, searchTerms):
    
    # Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename,searchTerms)
    
    # found list
    found = []
    
    # Loop through the results
    for eachFound in is_found:
        
        #print(eachFound)
        # Split the results
        sp_results = eachFound.split(" ")
        
        # Append the split value to the found list
        found.append(sp_results[5])
    

    # Remove duplicated bty using set
    # and convert the list to a dictionary
    hosts = set(found)

    # Print results
    for eachHost in hosts:

        print(eachHost)