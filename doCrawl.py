import urllib.parse
import urllib.request
import re
import requests
import json
import time
import string
import os
from bs4 import BeautifulSoup
from lxml import etree
from io import BytesIO
from PIL import Image
import requests
import crawlStartTimely as cst
import queue


cnt = 850
a = queue.Queue()
'''for i in [1,2,3,4,5]:
    a.put(i)

for i in range(5):
    b = a.get()
    print(b)'''

source = cst.doubanMovie("https://movie.douban.com/subject/30209818/?tag=%E6%82%AC%E7%96%91&from=gaia")
tai,actorL,recomm,name = source.dealMovie()
for cont in recomm:
    a.put(cont)


lists = []

while(a.empty() != True):
    if (cnt > 1000):
        break
    print("\n**********************"+str(cnt)+"********************")
    b = a.get()
    try:
        if b in lists:
            print(b+": satisfied")
            continue
        else :
            lists.append(b)
        temp = cst.doubanMovie(b)
        tai,actorL,recomm,name = temp.dealMovie()
        if tai == 1:
            cnt += 1
            for cont in recomm:
                a.put(cont)
        elif tai == 0:
            print(' not scientic')
        elif tai == -1:
            print(' already satisfied')
        elif tai == -2:
            print(' have not been published')
    except:
        print("Error")

print("the end, cnt = "+str(cnt))


