import os, argparse, yaml, re, csv


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
f_list = []

# walks through the input directory
for root, _, filenames in os.walk(rootdir):
    for filename in filenames:
        f_list.append(root + '\\' + filename)

# csv file contents
csv_contents = []
# loop through list of files and get content
for file in f_list:
    # open csv file in read only mode with utf-8 encoding
    with open(file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(file)
        for row in reader:
            csv_contents.append(row)

for item in csv_contents:
    print(item)
