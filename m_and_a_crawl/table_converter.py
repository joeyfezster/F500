import argparse

from m_and_a_crawl.html_table import Wikipedia_table

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="<Required> .html file containing html table to parse", required=True)
parser.add_argument("-k", "--ticker", help="<Required> stock ticker for the respective company", required=True)
parser.add_argument("-t", "--titles", nargs="*", help='<Required> list of titles/table headers in the order you\'d '
                                                      'like', required=True)
parser.add_argument("-o", "--outfile", help="<Required> output filename", required=True)
args = parser.parse_args()

# read html table into soup
with open(args.file) as html_table:
    table = Wikipedia_table(html_table)

table.write_to_file(args.outfile, args.titles, args.ticker)
print("Done")