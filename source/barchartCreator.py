import json
import itertools
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import os


class barchartCreator:
    def __init__(self):
        print("[*] Initialized barchartCreator")

    def getTop15(self,data, dataname):
        return_data = []
        for x in data:
            return_data.append(data[x][dataname])
        tmp = Counter(return_data).most_common()
        return_data = tmp[:15]
        return return_data

    def readDataFromFiles(self):
        data = {}
        for filename in os.listdir("data"):
            with open("data/"+filename,"r", encoding="utf8") as infile:
                raw = json.load(infile)
                for c,i in enumerate(raw):
                    s = str(c)
                    s += "-"
                    s += str(filename)
                    data[s] = i
        return data

    def createBarGraph(self,data,  xlabel, ylabel, title, filename):
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
        plt.savefig( "output/" + filename + ".png")
        print("[*] Plot saved to output/" + filename + ".png")
        