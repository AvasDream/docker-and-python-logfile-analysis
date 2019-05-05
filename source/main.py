import sys
from dateutil.parser import parse
from dataProcessor import dataProcessor
from barchartCreator import barchartCreator
def is_date(string, fuzzy=False):
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage python main.py <DATE>")
        print("Date has to be in this format:")
        print("DD-MM-YY")
        sys.exit(1)
    if not is_date(sys.argv[1]):
        print("Incorrected Date Format")
    else:
        date = sys.argv[1]
    # Get Information and save to json files
    """ dp = dataProcessor()
    ip_list = dp.importIps(date)
    chunks = dp.createChunks(ip_list)
    dp.getInformation(chunks) """

    # Create BarCharts
    bc = barchartCreator()



if __name__ == "__main__":
    main()