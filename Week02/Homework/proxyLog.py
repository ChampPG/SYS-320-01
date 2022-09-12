import syslogCheck, re
import importlib
importlib.reload(syslogCheck)

def proxy_events(filename, service, term):
    
    # Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename, service, term)
    
    # found list
    found = []
    
    # Loop through the results
    for eachFound in is_found:
        
        #print(eachFound)
        # Split the results
        sp_results = eachFound.split(" ")
        
        # Append the split value to the found list

        # Gets rid of any domain with qq
        for item in sp_results:
            if bool(re.search(r"[qq]{2}", item)):
                sp_results.remove(item)

        #print(sp_results)

        if term == "open":
            found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[3] + " " + sp_results[4] + " " + sp_results[5])
        if term == "bytes":
            if len(sp_results) >= 7:
                sp_results.remove(sp_results[1])
            found.append(sp_results[3] + " " + sp_results[4])
    
    #print(found)
    
    hosts = set(found)

    # Print results
    for eachValue in hosts:

        print(eachValue)
    
# Open proxy sessions
def proxy_open(filename, service, term):
    
    # Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename, service, term)
    
    # found list
    found = []

    # Loop through the results
    for eachFound in is_found:
        # Filters out qq domain
        if not bool(re.search(r"qq", eachFound)):
        
            #print(eachFound)
            # Split the results
            sp_results = eachFound.split(" ")

            #print(sp_results)

            found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[3] + " " + sp_results[6])
        
        #print(found)
        
        found.sort()

        # Print results
    for eachValue in found:

        print(eachValue)
        
# Closed proxy sessions
def proxy_closed(filename, service, term):
    # Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename, service, term)
    
    # found list
    found = []
    
    is_found.sort()

    #print(is_found)

    # Loop through the results
    for eachFound in is_found:
        # Filters out qq domain and couldn't connect through proxy
        if not bool(re.search(r"qq", eachFound)) and not bool(re.search(r"Could", eachFound)):
        
            # Split the results
            sp_results = eachFound.split(" ")

            # Gets rid of any domain with qq
            # for item in sp_results:
            #     if bool(re.search(r"[qq]{2}", item)):
            #         sp_results.remove(item)
            
            #print(sp_results)

            # Standardises the output for all conidtions
            if len(sp_results) >= 7:
                if bool(re.search(r"\(", sp_results[6])):
                    sp_results.remove(sp_results[1])
                    sp_results.remove(sp_results[5])
                    sp_results.remove(sp_results[5])
                else:
                    sp_results.remove(sp_results[1])

            #print(sp_results)

            found.append(sp_results[0] + " " + sp_results[1] + " " + sp_results[3] + " " + sp_results[4]+ " " + sp_results[5]+ " " + sp_results[6]+ " " + sp_results[7]+ " " + sp_results[8])

            #=print(sp_results)

    # Remove duplicated bty using set
    # and convert the list to a dictionary
    #print(found)
    
    # Print results
    for eachValue in found:

        print(eachValue)