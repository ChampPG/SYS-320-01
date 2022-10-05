import os, argparse, yaml, re, csv

def load_search(searchTerm):
    try:
        with open('searchTerms.yaml', 'r', errors='ignore') as yf:
            keywords = yaml.safe_load(yf)

    except EnvironmentError as e:
        print(e.strerror)

    return keywords[searchTerm]

def set_parser():
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

    return args

def load_dir(rootdir):
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
            reader = csv.DictReader(csvfile)
            for row in reader:
                csv_contents.append(row)
    
    return csv_contents


def main():
    # deploy arguements
    args = set_parser()
    # Set rootdir to directoy
    contents = load_dir(args.directory)
    
    # Set searchTerm from searchTerm input
    searchTerm = load_search(args.searchTerm)

    # split searchTerms into a list
    terms = searchTerm.split(', ')

    # loop through the content lines
    for line in contents:
        # loop through terms 
        for term in terms:
            # if term is found in the argument line return true
            if bool(re.findall(r''+term+'', line.get("arguments"))):
                print("""
                Term: {}
                Line: {} | {} | {} | {} | {}
                """.format(term,
                line["arguments"], 
                line["hostname"], 
                line["name"],
                line["path"],
                line["pid"],
                line["username"]))

if __name__ == "__main__":
    main()