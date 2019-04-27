#! python
import json
import itertools
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import os

def readIps():
    data = {}
    for i in range(0,47):
        s =  str(i)
        s += "_output.json"
        varForI = i
        with open(s,"r", encoding="utf8") as infile:
            raw = json.load(infile)
            for c,i in enumerate(raw):
                #print(i)
                s = str(varForI)
                s += "-"
                s += str(c)
                data[s] = i
    return data

def createBarGraph(data,  xlabel, ylabel, title):
    label = []
    no = []

    for i in data:
        label.append(i[0])
        no.append(i[1])

    index = np.arange(len(label))
    plt.bar(index, no)
    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.xticks(index, label, fontsize=8, rotation=30)
    plt.title(title)
    plt.figure(figsize=(10,6))
    """ plt.plot() """
    return plt

def getDataFromFiles():
    for filename in os.listdir("data"):
        print(filename)

def main():
    # ToDo
    # - Save to PDF
    # - Create World Map
    data = getDataFromFiles()
    """ countrys = []
    lonlat = []
    isps = []
    # Prepare Data
    for i in data:
        countrys.append(data[i]["country"])
        lonlat.append((data[i]["lon"],data[i]["lat"]))
        isps.append(data[i]["isp"])
    # Count Data
    ispsCount = Counter(isps).most_common()
    countrysCount = Counter(countrys).most_common()
    # Top Ten
    countryTop10 = countrysCount[:10]
    ispsTop10 = ispsCount[:10]
    # Create Bar Graph
    countryPlt = createBarGraph(countryTop10, 'Countrys', 'No of IPs', 'Number of IPs from country')
    ispPlt = createBarGraph(ispsTop10, 'ISP', 'No of ISP', 'ISP of IP adresses')
    

    fig = plt.figure(figsize=(20, 16))
    m = Basemap(projection='robin',lon_0=0,resolution='c')
    m.fillcontinents(color='white',lake_color='white')
    m.drawcoastlines()
    # Map (long, lat) to (x, y) for plotting
    for i in lonlat:
        x, y = m(i[0], i[1])
        plt.plot(x, y, 'ro', markersize=3)
    plt.title("Source of login attempts")
    plt.show()
    print(len(lonlat))


    
    #ispPlt.show()
    # Save to PDF """
    

if __name__ == "__main__":
    main()