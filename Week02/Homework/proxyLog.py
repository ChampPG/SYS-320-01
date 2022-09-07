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

        print(sp_results)

        if term == "open":
            found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[3] + " " + sp_results[4] + " " + sp_results[5])
        if term == "bytes":
            found.append(sp_results[4] + " " + sp_results[5])
    

    # Remove duplicated bty using set
    # and convert the list to a dictionary
    hosts = set(found)

    # Print results
    for eachValue in hosts:

        print(eachValue)