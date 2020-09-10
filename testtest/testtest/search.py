from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from django.core.paginator import Paginator
import json
from django.db import models
import os
import math
from . import views
import time
 
yiye = 10

'''def search_post(request):
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)'''

def comp(a):
    return float(a['average'])

def compA(a):
    return len(a['movies'])



def movieListSearch(request):
    return views.movieLists(request, request.POST['q'])
    #return HttpResponse("Hello world ! ")
def actorListSearch(request):
    return views.actorLists(request, request.POST['q'])


def searchMovieF(request):
    time_start=time.time()
    count = 1
    tt = ""
    name = request.POST['q']
    if len(name)> 20:
        name = name[:20]
    if 'SStype' in request.POST:
        tt = request.POST['SStype']
    else:
        tt = 'movie'

    if tt == 'movie':
        path = "/Users/yeyining/web/movies"
        files = os.listdir(path)
        context = []
        names = []
        temp = {}
        for file in files:
            f = open(path+'/'+file,'r',encoding = "utf-8")
            dicts = {}
            dicts = json.load(f)
            if 'average' in dicts and dicts['average'] != None:
                dicts['average'] = float(dicts['average'])
            else:
                dicts['average'] = 0.0
            dicts['paint'] = []
            pan1 = 0
            pan2 = 0
            if (name in dicts['name']):
                pan1 = 1
            for actorName in dicts['actors']:
                if name in actorName:
                    pan2 = 1
                    dicts['paint'].append(actorName)  
            if pan1 == 1:
                context.append(dicts) 
            elif pan2 == 1 :
                names.append(dicts)   
            f.close()
        context.sort(key=comp,reverse=True)   
        names.sort(key=comp,reverse=True)   
        context = context+names
        mmax = int(len(context) / yiye)+1
        temp['totalCount'] = len(context)
        if count <= mmax:
            context = context[(count-1)*yiye: count*yiye]
        else :
            context = context[(count-1)*yiye:]
        time_end=time.time()
        temp['name'] = name
        temp['cost'] = time_end - time_start
        temp['movies'] = context
        temp['now'] = int(min(count, mmax))
        temp['all'] = mmax
        temp['nowA1'] = temp['now']+1
        temp['nowA2'] = temp['now']+2
        temp['nowA3'] = temp['now']+3
        temp['nowM1'] = temp['now']-1
        temp['nowM2'] = temp['now']-2
        temp['nowM3'] = temp['now']-3
        return render(request, 'ssResult.html', temp)
    elif tt == 'actor':
        path = "/Users/yeyining/web/actors"
        files = os.listdir(path)
        context = []
        temp = {}
        for file in files:
            f = open(path+'/'+file,'r',encoding = "utf-8")
            dicts = {}
            dicts = json.load(f)
            dicts['paint'] = []
            dicts['chuyan'] = len(dicts['movies'])
            for movie in dicts['movies']:
                if name in movie:
                    dicts['paint'].append(movie)
            if (name in dicts['name'] or len(dicts['paint']) != 0):                                
                context.append(dicts) 
            f.close()

        context.sort(key=compA,reverse=True)    
        mmax = int(len(context) / yiye)+1
        temp['totalCount'] = len(context)
        if count <= mmax:
            context = context[(count-1)*yiye: count*yiye]
        else :
            context = context[(count-1)*yiye:]
        time_end=time.time()
        temp['name'] = name
        temp['cost'] = time_end - time_start
        temp['movies'] = context
        temp['now'] = int(min(count, mmax))
        temp['all'] = mmax
        temp['nowA1'] = temp['now']+1
        temp['nowA2'] = temp['now']+2
        temp['nowA3'] = temp['now']+3
        temp['nowM1'] = temp['now']-1
        temp['nowM2'] = temp['now']-2
        temp['nowM3'] = temp['now']-3
        return render(request, 'actorResult.html', temp)
    elif tt == 'comment':
        path = "/Users/yeyining/web/movies"
        files = os.listdir(path)
        context = []
        names = []
        temp = {}
        for file in files:
            f = open(path+'/'+file,'r',encoding = "utf-8")
            dicts = {}
            dicts = json.load(f)
            if 'average' in dicts and dicts['average'] != None:
                dicts['average'] = float(dicts['average'])
            else:
                dicts['average'] = 0.0
            for com in dicts['comments']:
                if name in com:
                    dicts['paint'] = com
                    context.append(dicts)
                    break
            f.close()
        context.sort(key=comp,reverse=True)    
        mmax = int(len(context) / yiye)+1
        temp['totalCount'] = len(context)
        if count <= mmax:
            context = context[(count-1)*yiye: count*yiye]
        else :
            context = context[(count-1)*yiye:]
        time_end=time.time()
        temp['name'] = name
        temp['cost'] = time_end - time_start
        temp['movies'] = context
        temp['now'] = int(min(count, mmax))
        temp['all'] = mmax
        temp['nowA1'] = temp['now']+1
        temp['nowA2'] = temp['now']+2
        temp['nowA3'] = temp['now']+3
        temp['nowM1'] = temp['now']-1
        temp['nowM2'] = temp['now']-2
        temp['nowM3'] = temp['now']-3
        return render(request, 'commentResult.html', temp)    
    else:
        return views.ss(request)


def searchComment(request, count, Sname):
    path = "/Users/yeyining/web/movies"
    files = os.listdir(path)
    context = []
    count = int(count)
    Sname = str(Sname)
    if len(Sname)> 20:
        Sname = Sname[:20]
    temp = {}
    time_start = time.time()
    for file in files:
        f = open(path+'/'+file,'r',encoding = "utf-8")
        dicts = {}
        dicts = json.load(f)
        if 'average' in dicts and dicts['average'] != None:
            dicts['average'] = float(dicts['average'])
        else:
            dicts['average'] = 0.0
        for com in dicts['comments']:
            if Sname in com:
                dicts['paint'] = com
                context.append(dicts)
                break
        f.close()
    context.sort(key=comp,reverse=True)    
    mmax = int(len(context) / yiye)+1
    temp['totalCount'] = len(context)
    if count <= mmax:
        context = context[(count-1)*yiye: count*yiye]
    else :
        context = context[(count-1)*yiye:]
    time_end=time.time()
    temp['name'] = Sname
    temp['cost'] = time_end - time_start
    temp['movies'] = context
    temp['now'] = int(min(count, mmax))
    temp['all'] = mmax
    temp['nowA1'] = temp['now']+1
    temp['nowA2'] = temp['now']+2
    temp['nowA3'] = temp['now']+3
    temp['nowM1'] = temp['now']-1
    temp['nowM2'] = temp['now']-2
    temp['nowM3'] = temp['now']-3
    return render(request, 'commentResult.html', temp)  

def searchActor(request, count, Sname):
    path = "/Users/yeyining/web/actors"
    files = os.listdir(path)
    context = []
    count = int(count)
    Sname = str(Sname)
    if len(Sname)> 20:
        Sname = Sname[:20]
    time_start=time.time()
    temp = {}
    for file in files:
        f = open(path+'/'+file,'r',encoding = "utf-8")
        dicts = {}
        dicts = json.load(f)
        dicts['paint'] = []
        dicts['chuyan'] = len(dicts['movies'])
        for movie in dicts['movies']:
            if Sname in movie:
                dicts['paint'].append(movie)
        if (Sname in dicts['name'] or len(dicts['paint']) != 0):                                
            context.append(dicts) 
        f.close()

    context.sort(key=compA,reverse=True)    
    mmax = int(len(context) / yiye)+1
    temp['totalCount'] = len(context)
    if count <= mmax:
        context = context[(count-1)*yiye: count*yiye]
    else :
        context = context[(count-1)*yiye:]
    time_end=time.time()
    temp['name'] = Sname
    temp['cost'] = time_end - time_start
    temp['movies'] = context
    temp['now'] = int(min(count, mmax))
    temp['all'] = mmax
    temp['nowA1'] = temp['now']+1
    temp['nowA2'] = temp['now']+2
    temp['nowA3'] = temp['now']+3
    temp['nowM1'] = temp['now']-1
    temp['nowM2'] = temp['now']-2
    temp['nowM3'] = temp['now']-3
    return render(request, 'ActorResult.html', temp)


def searchMovie(request, count, Sname):
    time_start=time.time()
    path = "/Users/yeyining/web/movies"
    files = os.listdir(path)
    context = []
    temp = {}
    count = int(count)
    Sname = str(Sname)
    if len(Sname)> 20:
        Sname = Sname[:20]
    names = []
    for file in files:
        f = open(path+'/'+file,'r',encoding = "utf-8")
        dicts = {}
        dicts = json.load(f)
        if 'average' in dicts and dicts['average'] != None:
            dicts['average'] = float(dicts['average'])
        else:
            dicts['average'] = 0.0
        dicts['paint'] = []
        pan1 = 0
        pan2 = 0
        if (Sname in dicts['name']):
            pan1 = 1
        for actorName in dicts['actors']:
            if Sname in actorName:
                pan2 = 1
                dicts['paint'].append(actorName)  
        if pan1 == 1:
            context.append(dicts) 
        elif pan2 == 1 :
            names.append(dicts)                   
        f.close()
    context.sort(key=comp,reverse=True)   
    names.sort(key=comp,reverse=True)   
    context = context+names
    for i in range(len(context)):
        if i % 5 == 0:
            context[i]['ifHuan'] = 1
        else :
            context[i]['ifHuan'] = 0
    mmax = int(len(context) / yiye)+1
    temp['totalCount'] = len(context)
    if count <= mmax:
        context = context[(count-1)*yiye: count*yiye]
    else :
        context = context[(count-1)*yiye:]
    time_end=time.time()
    temp['name'] = Sname
    temp['cost'] = time_end - time_start
    temp['movies'] = context
    temp['now'] = int(min(count, mmax))
    temp['all'] = mmax
    temp['nowA1'] = temp['now']+1
    temp['nowA2'] = temp['now']+2
    temp['nowA3'] = temp['now']+3
    temp['nowM1'] = temp['now']-1
    temp['nowM2'] = temp['now']-2
    temp['nowM3'] = temp['now']-3
    return render(request, 'ssResult.html', temp)