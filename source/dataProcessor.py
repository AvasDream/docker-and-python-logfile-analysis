import sys 
import os
import requests
import json 
import time 
import codecs

def generatePayload(ips):
    try:
        payload = []
        for ip in ips:
            payload.append({"query": ip})
        return payload
    except:
        e = sys.exc_info()[1]
        print("[!] Error while creating Payload")
        print( "[!] Error: %s" % str(e) )

def batchRequest(ips):
    try:
        payload = generatePayload(ips)
        resp = requests.post('http://ip-api.com/batch', data=json.dumps(payload))
        if resp.status_code != 200:
            print("Error while getting Data")
            sys.exit(1)
        if resp.status_code == 422:
            print("Too much IPs in request")
            sys.exit(1)
        else:
            data = resp.json()
        return data
    except:
        e = sys.exc_info()[1]
        print("[!] Error while making Request to API")
        print( "[!] Error: %s" % str(e) )

class dataProcessor:
    def __init__(self):
        print("[*] Initialized dataImporter")

    def importIps(self,date):
        try:
            script_dir = os.getcwd()
            s = "input/"
            s += str(date) + "_ips.txt"
            filepath = os.path.join(script_dir, s)
            f = open(filepath,'r')
            ips = []
            for line in f:
                ips.append(line.rstrip("\n"))
            print("[*] Imported Ips from file %s" % str(filepath))
            return ips
        except:
            e = sys.exc_info()[1]
            print("[!] Error while importing Ips from file")
            print( "[!] Error: %s" % str(e) )

    def createChunks(self, ip_list):
        try:
            chunks = [ip_list[x:x+100] for x in range(0, len(ip_list), 100)]
            print("[*] Created %d chunks with 100 IPs per chunk" % len(chunks))
            return chunks
        except:
            e = sys.exc_info()[1]
            print("[!] Error while creating chunks from IP list")
            print( "[!] Error: %s" % str(e) )

    def getInformation(self,chunks):
        try:
            for c,l in enumerate(chunks):
                data = batchRequest(l)
                # More than 150 Requests per Second will get you blocked
                time.sleep( 1 )
                script_dir = os.getcwd()
                s = "data/"
                s +=  str(c)
                s += "_output.json"
                path = os.path.join(script_dir, s)
                with open(path, "wb") as outfile:
                    json.dump(data,codecs.getwriter('utf-8')(outfile), ensure_ascii=False)
                print("[*] Information for chunk %s saved to %s" % (str(c),s))
        except:
            e = sys.exc_info()[1]
            print("[!] Error while getting Data")
            print( "[!] Error: %s" % str(e) )

    def cleanup(self):
        try:
            filelist = [ f for f in os.listdir("data") if f.endswith(".json") ]
            for file in filelist:
                os.remove(os.path.join("data", file))
            print("[*] Cleaned data directory")
        except:
            e = sys.exc_info()[1]
            print("[!] Error cleaning up")
            print( "[!] Error: %s" % str(e) )