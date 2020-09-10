import urllib.parse
import urllib.request
import re
import requests
import json
import random
import time
import string
import os
from bs4 import BeautifulSoup
from lxml import etree
from io import BytesIO
from PIL import Image
import requests
#from bs4 import BeautifulSoup

#user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

mmin = 1
mmax = 3

class doubanMovie():
    
    def __init__(self,title):
        self.url = title
        #self.url = "hhttps://movie.douban.com/j/new_search_subjects?sort=T&range=0%2C10&tags=%E7%94%B5%E5%BD%B1%2C%E5%89%A7%E6%83%85%2C%E7%BE%8E%E5%9B%BD&start=0&genres=%E5%96%9C%E5%89%A7&countries=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86"
        self.url = urllib.request.quote(self.url, safe=string.printable)
        #self.url = "https://baidu.com"
        self.title = title
        self.reqData = urllib.parse.urlencode({'q' : 'python'})
        self.headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
        #self.data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='gbk')

    def getMovie(self, title):
        time.sleep(random.randint(mmin,mmax))
        #respon = requests.get(url = self.url, headers=self.headers)
        #doc = urllib.request.urlopen(url = self.url)
        #print(respon.content.decode())
        req = urllib.request.Request(self.url, headers=self.headers)
        response = urllib.request.urlopen(req)
        the_page = response.read().decode()
        #print(the_page)
        return the_page

    def getActor(self,lianjie):
        time.sleep(random.randint(mmin,mmax))
        req = urllib.request.Request(lianjie, headers=self.headers)
        response = urllib.request.urlopen(req)
        the_page = response.read().decode()
        #print(the_page)
        return the_page        

    def moviePic(self, title, name):
        try:
            time.sleep(random.randint(mmin,mmax))
            '''req = urllib.request.Request(self.url, headers=self.headers)
            response = urllib.request.urlopen(req)
            the_page = response.read()'''
            resp = requests.get(title, headers=self.headers)
            byte_stream = BytesIO(resp.content)
            im = Image.open(byte_stream)
            #im.show()     
            if im.mode == "RGBA":
                im.load()  # required for png.split()
                background = Image.new("RGB", im.size, (255, 255, 255))
                background.paste(im, mask=im.split()[3]) 
            im.save("./moviephotos/"+name+".jpg", 'JPEG')
        except:
            return

    def actorPic(self, title, name):
        try:
            time.sleep(random.randint(mmin,mmax))
            '''req = urllib.request.Request(self.url, headers=self.headers)
            response = urllib.request.urlopen(req)
            the_page = response.read()'''
            resp = requests.get(title, headers=self.headers)
            byte_stream = BytesIO(resp.content)
            im = Image.open(byte_stream)
            #im.show()     
            if im.mode == "RGBA":
                im.load()  # required for png.split()
                background = Image.new("RGB", im.size, (255, 255, 255))
                background.paste(im, mask=im.split()[3]) 
            im.save("./actorphotos/"+name+".jpg", 'JPEG')
        except:
            return

    def str2Json(self,data):
        print(type(data))
        print(data)
        dict_data = json.loads(data)
        print(dict_data)

    def dealActor(self,lianjie,name):
        dicts = {}
        a = self.getActor(lianjie)
        soup = BeautifulSoup(a, 'html.parser')
        temp = soup.find('div', id = "wrapper").find('div',id = "content").find('h1')
        #print(temp.string)
        dicts['name'] = temp.string
        #print(temp.string)
        if os.path.exists('./actors/'+dicts['name']+".json"):
            f = open('./actors/'+dicts['name']+".json","r",encoding = 'utf-8')
            jsonStr = json.load(f,strict=False)
            if name not in jsonStr['movies']:
                jsonStr['movies'].append(name)
            json_str = json.dumps(jsonStr, indent=4)
            with open("./actors/"+dicts['name']+".json", 'w', encoding="utf-8") as json_file:
                json_file.write(json_str)
            return 2,dicts['name']
        
        temp = soup.find('div', id = "wrapper").find('div', class_ = "grid-16-8 clearfix").find('div', class_='article').find('div', id = "headline").find('div', class_= 'pic').find('a',class_='nbg')
        self.actorPic(temp['href'],dicts['name'])     

        dicts['movies'] = [name]


        temp = soup.find('div', id = "wrapper").find('div', class_ = "grid-16-8 clearfix").find('div', class_='article').find('div', id = "headline").find('div', class_='info')
        kk = temp.get_text()
        kk = kk.replace("  ","")
        kk = kk.replace("\n\n","\n")
        #print(kk)

        searchObj = re.search( r"性别:.*\n(.*)\n\n", kk)
        if searchObj:
            dicts['male'] = searchObj.group(1)
            #print(searchObj.group(1)n
        else:
            dicts['male'] = 'not found'

        searchObj = re.search( r"星座:.*\n(.*)\n\n", kk)
        if searchObj:
            dicts['xingzuo'] = searchObj.group(1)
            #print(searchObj.group(1))
        else:
            dicts['xingzuo'] = 'not found'

            
        searchObj = re.search( r"出生日期:.*\n(.*)\n\n", kk)
        if searchObj:
            dicts['birth'] = searchObj.group(1)
            #print(searchObj.group(1))
        else:
            dicts['birth'] = 'not found'

        searchObj = re.search( r"出生地:.*\n(.*)\n\n", kk)
        if searchObj:
            dicts['area'] = searchObj.group(1)
            #print(searchObj.group(1))
        else:
            dicts['area'] = 'not found'

        searchObj = re.search( r"职业:.*\n(.*)\n", kk)
        if searchObj:
            dicts['zhiye'] = searchObj.group(1).split(' / ')
            #print(searchObj.group(1))
        else:
            dicts['zhiye'] = []

        searchObj = re.search( r"更多中文名:.*\n(.*)\n", kk)
        if searchObj:
            dicts['moreName'] = searchObj.group(1).split(' / ')
            #print(searchObj.group(1))
        else:
            dicts['moreName'] = []

        searchObj = re.search( r"家庭成员:.*\n(.*)\n", kk)
        if searchObj:
            dicts['family'] = searchObj.group(1).split(' / ')
            #print(searchObj.group(1))
        else:
            dicts['family'] = []

        temp = soup.find('div', id = "wrapper").find('div', id = "content").find('div', class_ = 'grid-16-8 clearfix').find('div', class_ = 'article').find('div', id = 'intro').find('div', class_ = 'bd')
        if temp.get_text() != "":
            dicts['intro'] = temp.get_text()
        else:
            temp = temp.find_all('span')
            dicts['intro'] = 'not found'
            for cont in temp:
                a = cont.get_text()
                print(a)
                if "展开全部" not in a:
                    dicts['intro'] = a
                    break
        

        dicts['hezuo'] = []

        json_str = json.dumps(dicts, indent=4)
        with open("./actors/"+dicts['name']+".json", 'w', encoding="utf-8") as json_file:
            json_file.write(json_str)
        return  1,dicts['name']


    def dealMovie(self):
        actors = []
        dicts = {}
        a = self.getMovie(self.title)
        soup = BeautifulSoup(a, 'html.parser')

        kk = soup.get_text()
        kk = kk.replace("  ","")
        kk = kk.replace("\n\n","")

        searchObj = re.search( r"导演: (.*)\n", kk)
        if searchObj:
            dicts['director'] = searchObj.group(1)
            #print(searchObj.group(1))
        else:
            dicts['director'] = 'not found'

        searchObj = re.search( r"编剧: (.*)\n", kk)
        if searchObj:
            dicts['bianju'] = searchObj.group(1)
            #print(searchObj.group(1))
        else:
            dicts['bianju'] = 'not found'

        searchObj = re.search( r"片长: (.*)\n", kk)
        if searchObj:
            dicts['length'] = searchObj.group(1)
            #print(searchObj.group(1))
        else:
            dicts['length'] = 'not found'

        searchObj = re.search( r"语言: (.*)\n", kk)
        if searchObj:
            dicts['lang'] = searchObj.group(1).split(' / ')
            #print(searchObj.group(1))
        else:
            dicts['lang'] = []

        searchObj = re.search(r"制片国家/地区: (.*)\n", kk)
        if searchObj:
            dicts['area'] = searchObj.group(1).split(' / ')
            #print(searchObj.group(1))
        else:
            dicts['area'] = []

        fenlei = []
        searchObj = re.search( r"类型: (.*)\n", kk)
        if searchObj:
            fenlei = searchObj.group(1).split(' / ')
            dicts['select'] = fenlei
        else:
            dicts['select'] = []

        temp = soup.find('div', id = "wrapper").find('div', id = "content").find('h1').find('span',property="v:itemreviewed")
        dicts['name'] = temp.string
        print(dicts['name']+': ',end=" ")

        temp = soup.find('div', id = "wrapper").find('div', id = "content").find('h1').find('span', class_="year")
        dicts['year'] = temp.string.lstrip('(').rstrip(')')


        temp = soup.find('div', id = "wrapper").find('div', id = "content").find('div', class_ = 'grid-16-8 clearfix').find('div', class_ = 'article').find('div', class_ = 'related-info').find('div', class_ = 'indent')
        dicts['intro'] = 'not found'
        i = temp.get_text()
        i = i.replace("  ","")
        i = i.replace("\n"," ")
        searchObj = re.search("展开全部(.*)", i)
        #print(i)
        if searchObj:
            dicts['intro'] = searchObj.group(1)
        else :
            dicts['intro'] = i

        try:
            temp = soup.find('div', id = "wrapper").find('div', id = "content").find('div', class_ = 'grid-16-8 clearfix').find('div', class_ = 'article').find('div', class_ = 'indent clearfix').find('div', class_ = 'subjectwrap clearfix').find('div', id = 'interest_sectl').find('div', class_ = 'rating_wrap clearbox').find('div', class_ = 'rating_self clearfix').find('strong',class_="ll rating_num")
            dicts['average'] = temp.string
        except:
            dicts['average'] = 0.0
        
        try:
            temp = soup.find('div', id = "wrapper").find('div', id = "content").find('div', class_ = 'grid-16-8 clearfix').find('div', class_ = 'article').find('div', class_ = 'indent clearfix').find('div', class_ = 'subjectwrap clearfix').find('div', id = 'interest_sectl').find('div', class_ = 'rating_wrap clearbox').find('div', class_ = 'rating_self clearfix')#.find('div',class_="rating_right").find('div',class_="rating_sum").find('a').find('span',property="v:votes")
            dicts['averageNum'] = temp.string
        except:
            dicts['averageNum'] = 0
            
        comms = []
        temp = soup.find('div', id = "wrapper").find('div', id = "content").find('div', class_ = 'grid-16-8 clearfix').find('div', class_ = 'article').find('div', id = 'comments-section').find('div', class_ = 'mod-bd').find('div', class_ = 'tab-bd').find("div",id="hot-comments").find_all('div', class_='comment-item')
        for item in temp:
            ttt = item.find("div", class_="comment").find('p').find_all('span')
            for cont in ttt:
                #if len(cont.string) < 1:
                #    continue
                if(cont['class'] == ['hide-item full']):
                    comms.append(cont.string)
                    break
                elif (cont['class'] == ['short']):
                    comms.append(cont.string)
        dicts['comments'] = comms

        recomm = []
        temp = soup.find('div', id = "wrapper").find('div', id = "content").find('div', class_ = 'grid-16-8 clearfix').find('div', class_ = 'article').find('div', id = 'recommendations').find('div', class_ = 'recommendations-bd').find_all('dl')
        for item in temp:
            a = item.find('dt').find('a')
            lianjie = a['href']
            recomm.append(lianjie)
        ###是否符合条件
        #if ("科幻" not in dicts['select']) and ("动作" not in dicts['select']) and ("剧情" not in dicts['select']) and ("奇幻" not in dicts['select']) and ("冒险" not in dicts['select']) and ("悬疑" not in dicts['select']):
        #    return 0,[],recomm,dicts['name']

        if os.path.exists('./movies/'+dicts['name']+".json"):
            return -1,[],recomm,dicts['name']

        if dicts['year'] >= '2020':
            return -2,[],recomm,dicts['name']
        

        temp = soup.find('div', id = "wrapper").find('div', id = "content").find('div', class_ = 'grid-16-8 clearfix').find('div', class_ = 'article').find('div', class_ = 'indent clearfix').find('div', class_ = 'subjectwrap clearfix').find('div', class_ = 'subject clearfix').find('div', id = 'mainpic').find('a', class_ = 'nbgnbg').find('img')
        #print(temp['src'])
        self.moviePic(temp['src'],dicts['name'])


        temp = soup.find('div', id='info')
        actorL = []
        count = 0
        for aa in temp.find_all(attrs = {"rel" : "v:starring"}):
            if count > 9:
                continue
            #print(aa.string, end=' ')
            tt = 'https://movie.douban.com' + aa['href']
            #print(tt)
            tai,actName = self.dealActor(tt,dicts['name'])
            print(actName,end=" ")
            actorL.append(actName)
            count+=1
            #self.getMovie(tt)
            #print('movie.douban.com' + aa['href']) 
        dicts['actors']  = actorL     

        json_str = json.dumps(dicts, indent=4)
        with open("./movies/"+dicts['name']+".json", 'w', encoding="utf-8") as json_file:
            json_file.write(json_str)
        
        return 1,actorL,recomm,dicts['name']





if __name__ == "__main__":
    dd = doubanMovie("https://movie.douban.com/subject/26394152/")
    a,b,c = dd.dealMovie()
    if(a != 1):
        print(a)
    #spider()