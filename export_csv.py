import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random
import urllib2
import json
import codecs
import csv
#import timing
##class for data_generation






def obj_parse(item):
    position = item["pointId"].split('_')
    floor = int(position[1][2])
    zone = int(position[2])
    period = item["timestamp"].split('+')
#    item["floorzone"]=floor*100+zone
    return {"floor":floor, "zone":zone,"time":period[0], "type":item["type"], "value":item["value"]}
    
    
if __name__ == '__main__':
#if __name__ == '__main__':

#    REST_API_URL = 'https://api.powerbi.com/beta/f251f123-c9ce-448e-9277-34bb285911d9/datasets/9695916c-7bfd-4330-89dd-719084f31e6c/rows?key=vwUYe4csr%2BoLaO2og4AruRWYFx1Hga064j0Xw644oxJUmbrCrZbsbskd5A7s%2FsthebK9%2FuOXoqdJKqKBiwUSLw%3D%3D'

    while True:
        data_raw = []
        compare = {}
                
        #        for i in range(1):
        #           row = data_generation()
        response = urllib2.urlopen("https://scadadataapi.azurewebsites.net/api/values")
        html = response.read()# Fetch the given string from the URL
        obj =json.loads(html)
        for item in obj:
            row = obj_parse(item)
        
            data_raw.append(row)
            
        with open("D://02830//faysoserious.github.io//data.csv", 'w') as outcsv:   
            #configure writer to write standard csv file
            writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(['floor', 'zone', 'time', 'type', 'value'])
            for dic in data_raw:
                #Write item to outcsv
                writer.writerow([dic["floor"],dic["zone"], dic["time"], dic["type"], dic["value"]])    
#    data_json = json.dumps(data_raw)
#with open('data.txt', 'wb') as f:
#    json.dump(data_json, codecs.getwriter('utf-8')(f), ensure_ascii=False)
#        print("Data posted in Power BI API")
#The number of seconds the Python program should pause execution. 
#This argument should be either an int or a float.
        print("csv file updated")
        time.sleep(2)
        

