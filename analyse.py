#! python
import requests
import json
import codecs
import os
import time
import sys
def getInfo(ip):
    resp = requests.get('http://ip-api.com/json/' + ip)
    if resp.status_code != 200:
        data_formated = "Error while getting Data for ", ip
    else:
        data = resp.json()
        # "ctry": data["country"], "isp": data["isp"],"org": data["org"]
        data_formated = {"ip": ip, "lon": data["lon"], "lat": data["lat"], "country": data["country"], "isp": data["isp"],"org": data["org"] }
    return data_formated

def readIpFile(filename):
    script_dir = os.getcwd()
    s = "input/"
    s += filename
    filepath = os.path.join(script_dir, s)
    f = open(filepath,'r')
    ips = []
    for line in f:
        ips.append(line.rstrip("\n"))
    return ips

def generatePayload(ips):
    payload = []
    for ip in ips:
        payload.append({"query": ip})
    return payload

def batchRequest(ips):
    payload = generatePayload(ips)
    resp = requests.post('http://ip-api.com/batch', data=json.dumps(payload))
    if resp.status_code != 200:
        data_formated = "Error while getting Data"
    if resp.status_code == 422:
        data_formated = "Too much IPs in request"
    else:
        data = resp.json()
    return data


def main():
    if len(sys.argv) < 2:
        print("Usage: analyse.py <Filename in /input>")
        sys.exit()
    else:
        ips = readIpFile(sys.argv[1])
        # Cut array in chunks because of the api limitation
        chunks = [ips[x:x+100] for x in range(0, len(ips), 100)]
        for c,l in enumerate(chunks):
            data = batchRequest(l)
            # More than 150 Requests per Second will get you blocked
            time.sleep( 1 )
            script_dir = os.getcwd()
            s = "data/"
            s +=  str(c)
            s += "_output.json"
            absPath = os.path.join(script_dir, s)
            print("Chunk Number ", str(c) + " Path: " + str(absPath) )
            with open(absPath, "wb") as outfile:
                json.dump(data,codecs.getwriter('utf-8')(outfile), ensure_ascii=False)













if __name__ == "__main__":
    main()