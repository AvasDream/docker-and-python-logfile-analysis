import sys
import os
from dateutil.parser import parse
from dataProcessor import dataProcessor
from barchartCreator import barchartCreator
from pdfCreator import pdfCreator

def is_date(string, fuzzy=False):
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

def main():
    # Check if gitignore folders exist yet
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("output"):
        os.makedirs("output")
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
    dp = dataProcessor()
    ip_list = dp.importIps(date)
    chunks = dp.createChunks(ip_list)
    dp.getInformation(chunks)

    # Create BarChart
    bc = barchartCreator()
    data = bc.readDataFromFiles()
    data_type = "countryCode"
    country_data = bc.getTop15(data,data_type)
    bc.createBarGraph(country_data, \
                'Countries', \
                'IP addresses', \
                'IPs from country', \
                date + "-country")
    # Create PDF report
    pdfC = pdfCreator(date)
    pdfC.generateReport(date,data)
    # delete /data
    dp.cleanup()
if __name__ == "__main__":
    main()