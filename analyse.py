#! python
import requests
import json
import codecs

def getInfo(ip):
    resp = requests.get('http://ip-api.com/json/' + ip)
    if resp.status_code != 200:
        data_formated = "Error while getting Data for ", ip
    else:
        data = resp.json()
        # "ctry": data["country"], "isp": data["isp"],"org": data["org"]
        data_formated = {"ip": ip, "lon": data["lon"], "lat": data["lat"], "country": data["country"], "isp": data["isp"],"org": data["org"] }
    return data_formated

def getIps():
    f = open('ips.txt','r')
    ips = []
    for line in f:
        ips.append(line.rstrip("\n"))
        #print(line.rstrip("\n"))
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
        data_formated = "Error while getting Data for ", ip
    if resp.status_code == 422:
        data_formated = "Too much IPs in request"
    else:
        data = resp.json()
    return data


def main():
    ips = getIps()
    ip_arry = []
    # Cut array in chunks because of the api limitation
    chunks = [ips[x:x+100] for x in range(0, len(ips), 100)]
    for c,l in enumerate(chunks):

        data = batchRequest(l)
        s =  str(c)
        s += "_output.json"
        with open(s, "wb") as outfile:
            json.dump(data,codecs.getwriter('utf-8')(outfile), ensure_ascii=False)
















if __name__ == "__main__":
    main()