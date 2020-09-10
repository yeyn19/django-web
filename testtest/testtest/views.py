from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from django.core.paginator import Paginator
import json
from django.db import models
import os
import math
from django import forms
 
def hello(request):
    return HttpResponse("Hello world ! ")


def runoob(request):
    context          = {}
    context['hello'] = 'Hello World! mother fucker'
    return render(request, 'runoob.html', context)


#def ss(request):
#    context = {}
#    return render(request, 'ss.html', context)

class SysConfigForm(forms.Form):
    DatabaseType=forms.ChoiceField(choices=[('sqlserver','SQLServer'),('oracle','Oracle')])

class IndexForm(forms.Form):
    # 模板,用户提交的name和这里的变量名一定要是一致的.否则不能获取数据
    user = forms.CharField(label='sss',min_length=6, error_messages={'required': '用户名不能为空', 'min_length': '用户名长度不能小于6'})
    email = forms.EmailField(error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'})
    
       #单选
    favor = forms.ChoiceField(
        choices=[(1, '小虎'), (2, '小小虎'), (3, '小B虎')]
    )
    
    ''' 多选
    favor = forms.MultipleChoiceField(
        choices=[(1, '小虎'), (2, '小小虎'), (3, '小B虎')]
    )'''
    pass

def ss(request):
    obj = IndexForm()
    return render(request, 'ss.html', {"obj":obj})


def compA(a):
    return len(a['movies'])

def movieInfo(request, name):
    path = "/Users/yeyining/web/movies"
    #tempname = name.replace("_"," ")
    files = os.listdir(path)
    context = {}
    for file in files:
        if name in file:
            f = open(path+'/'+file,'r',encoding = "utf-8")
            context = json.load(f)
            break
    #context['photo'] = "/Users/yeyining/web/m"
    return render(request, 'movieInfo.html', context)

def actorInfo(request, name):
    path = "/Users/yeyining/web/actors"
    name = name.replace("_"," ")
    files = os.listdir(path)
    context = {}
    for file in files:
        if name in file:
            f = open(path+'/'+file,'r',encoding = "utf-8")
            context = json.load(f)
            break
    count = 0
    context['paint'] = []
    for movie in context['movies']:
        #count+=1
        if count % 5 == 0:
            context['paint'].append({'nn':movie,'cc':1})
        else:
            context['paint'].append({'nn':movie,'cc':0})
        count+=1
    context['temp'] = []
    for i in context['hezuo']:
        context['temp'].append({"nn":i[0],'cc':i[1]})
    #context['photo'] = "/Users/yeyining/web/m"
    return render(request, 'actorInfo.html', context)

def comp(a):
    return a['average']

def movieListsF(request):
    count = 1
    path = "/Users/yeyining/web/movies"
    files = os.listdir(path)
    context = []
    for file in files:
        f = open(path+'/'+file,'r',encoding = "utf-8")
        dicts = {}
        dicts = json.load(f)
        if 'average' in dicts and dicts['average'] != None:
            dicts['average'] = float(dicts['average'])
        else:
            dicts['average'] = 0.0
        context.append(dicts)
        f.close()
    context.sort(key=comp,reverse=True)
    mmax = int(len(context) / 20)+1
    if count <= mmax:
        context = context[(count-1)*20: count*20]
    else :
        context = context[(count-1)*20:]
    for i in range(len(context)):
        if i % 5 == 0:
            context[i]['ifHuan'] = 1
        else :
            context[i]['ifHuan'] = 0
    temp = {}
    temp['movies'] = context
    temp['now'] = int(min(count, mmax))
    temp['all'] = mmax
    temp['nowA1'] = temp['now']+1
    temp['nowA2'] = temp['now']+2
    temp['nowA3'] = temp['now']+3
    temp['nowM1'] = temp['now']-1
    temp['nowM2'] = temp['now']-2
    temp['nowM3'] = temp['now']-3
    return render(request, 'movieL.html', temp)

def movieLists(request, count):
    count = int(count)
    path = "/Users/yeyining/web/movies"
    files = os.listdir(path)
    context = []
    for file in files:
        f = open(path+'/'+file,'r',encoding = "utf-8")
        dicts = {}
        dicts = json.load(f)
        if 'average' in dicts and dicts['average'] != None:
            dicts['average'] = float(dicts['average'])
        else:
            dicts['average'] = 0.0
        context.append(dicts)
        f.close()
    context.sort(key=comp,reverse=True)
    mmax = int(len(context) / 20)+1
    if count <= mmax:
        context = context[(count-1)*20: count*20]
    else :
        context = context[(count-1)*20:]
    for i in range(len(context)):
        if i % 5 == 0:
            context[i]['ifHuan'] = 1
        else :
            context[i]['ifHuan'] = 0
    temp = {}
    temp['movies'] = context
    temp['now'] = int(min(count, mmax))
    temp['all'] = mmax
    temp['nowA1'] = temp['now']+1
    temp['nowA2'] = temp['now']+2
    temp['nowA3'] = temp['now']+3
    temp['nowM1'] = temp['now']-1
    temp['nowM2'] = temp['now']-2
    temp['nowM3'] = temp['now']-3
    return render(request, 'movieL.html', temp)


def actorLists(request, count):
    count = int(count)
    path = "/Users/yeyining/web/actors"
    files = os.listdir(path)
    context = []
    for file in files:
        f = open(path+'/'+file,'r',encoding = "utf-8")
        dicts = {}
        dicts = json.load(f)
        dicts['paint'] = len(dicts['movies'])
        context.append(dicts)
        f.close()
    context.sort(key=compA,reverse=True)
    mmax = int(len(context) / 20)+1
    count = min(mmax,count)
    if count <= mmax:
        context = context[(count-1)*20: count*20]
    else :
        context = context[(count-1)*20:]
    for i in range(len(context)):
        if i % 5 == 0:
            context[i]['ifHuan'] = 1
        else :
            context[i]['ifHuan'] = 0
    temp = {}
    temp['actors'] = context
    temp['now'] = int(min(count, mmax))
    temp['all'] = mmax
    temp['nowA1'] = temp['now']+1
    temp['nowA2'] = temp['now']+2
    temp['nowA3'] = temp['now']+3
    temp['nowM1'] = temp['now']-1
    temp['nowM2'] = temp['now']-2
    temp['nowM3'] = temp['now']-3
    return render(request, 'actorL.html', temp)
