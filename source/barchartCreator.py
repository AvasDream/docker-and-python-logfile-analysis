import json
import itertools
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import os


class barchartCreator:
    def __init__(self):
        print("[*] Initialized barchartCreator")

    def readDataFromFiles(self):
        data = {}
        for filename in os.listdir("data"):
            print(filename)
            with open("data/"+filename,"r", encoding="utf8") as infile:
                raw = json.load(infile)
                for c,i in enumerate(raw):
                    #print(i)
                    s = str(filename)
                    s += "-"
                    s += str(c)
                    data[s] = i
        return data