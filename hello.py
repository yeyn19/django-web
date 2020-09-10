import random
import os
import json
import time
import string
from bs4 import BeautifulSoup
from lxml import etree
from io import BytesIO
from PIL import Image
import requests
import crawlStartTimely as cst
import queue


path = "/Users/yeyining/web/actors"
files = os.listdir(path)
count = 0

def comp(a):
    return a[1]

for file in files:
    if count % 100 == 0:
        print(count)
    count += 1
    f = open(path+'/'+file,'r',encoding = 'utf-8')
    dicts = json.load(f)
    lists = []
    for oth in files:
        if oth == file:
            continue
        f2 = open(path+'/'+oth,'r',encoding = 'utf-8')
        dicts2 = json.load(f2)
        cc = 0
        for movie in dicts['movies']:
            if movie in dicts2['movies']:
                cc+=1
        lists.append([dicts2['name'],cc])
        f2.close()
    lists.sort(key=comp, reverse=True)
    for i in range(10):
        dicts['hezuo'].append(lists[i])
    f.close()

    json_str = json.dumps(dicts, indent=4)
    with open("/Users/yeyining/web/actorsNew/"+dicts['name']+".json", 'w', encoding="utf-8") as json_file:
        json_file.write(json_str)
    
        