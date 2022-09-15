#FIX: import re
import csv, re

#FIX: ur1HausOpen changed to urlHausOpen
#FIX: searchTerm to searchTerms
def urlHausOpen(filename,searchTerms):

    # FIX: while open changed to with open
    # FIX: 'filename' changed to filename
    # FIX: as f changed to as csv_file
    with open(filename) as csv_file:
        # FIX: == to =
        # FIX: csv.review(filename) to csv.reader(csvfile)
        contents = csv.reader(csv_file)
        # FIX: indentation
        for _ in range(9):
            # FIX: indentation
            next(contents)
        # FIX: indentation
        # FIX: indentation
        for eachLine in contents:
            # FIX: indentation
            # FIX: added "" to correct locations
            # FIX: moded keywords in searchTerms look inside eachLine
            for keywords in searchTerms:
                x = re.findall(r''+keywords+'',eachLine[2])

# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.
                # FIX: indentation
                for _ in x:
                    the_url = eachLine[2].replace("http","hxxp")
                    the_src = eachLine[4]
                    print("""
                    URL: {}
                    Info: {}
                    {}""".format(the_url, the_src,"*"*60))
                    # FIX: repalced +60 with *60
                    # FIX: ,format to .format