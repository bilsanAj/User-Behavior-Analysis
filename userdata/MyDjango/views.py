from django.shortcuts import render
import requests
import json
import pandas as pd
import numpy as np
from bson import ObjectId
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.http import HttpResponse  ,JsonResponse 
from plotly.offline import plot
from plotly.graph_objs import Scatter ,Bar
from scipy import stats





def getMinMax(request):
    # df = data_analytics()
    
    df = pd.read_csv('userData.csv')
    min_ind =df['area'].value_counts().min()
    max_ind = df['area'].value_counts().max()
    dic = df.groupby('area').count().to_dict(orient='dict')
    dic = dic['__v']
    min_area=[]
    max_area=[]
    all_counts=[]
    for key in dic.keys():
        if dic[key]==min_ind:
            min_area.append({'count':dic[key] ,'area':key} )
        if dic[key]==max_ind:
            max_area.append({'count':dic[key] ,'area':key})
        all_counts.append(dic[key])
    all_counts = np.array(all_counts)
    mean = np.mean(all_counts)
    median=np.median(all_counts)
    mode = stats.mode(all_counts)
    mode = mode.mode
    mode =str(mode[0])
    data = {'max' :max_area,'min':min_area , 'mean' :mean,'median':median,'mode':mode}
    data = {'data' :data}
    return JsonResponse(data)



def getLastMonth(request):
    df = pd.read_csv('userData.csv')
    date = df['_id'].apply(lambda x : ObjectId(x).generation_time)
    df['date'] = date
    now = datetime.now()
    byMonth = format (now - relativedelta(months=1))
    last_month = df[df['date']>(byMonth)]
    dic = last_month.groupby('area').count().to_dict(orient='dict')
    dic = dic['__v']
    last_month_list = []
    for key in dic.keys():  
        last_month_list.append({'count':dic[key] ,'area':key} )
    h = dic
    data = {'data' :last_month_list }
    return JsonResponse(data)



def getLast2Weeks(request):
    df = pd.read_csv('userData.csv')
    date = df['_id'].apply(lambda x : ObjectId(x).generation_time)
    df['date'] = date
    now = datetime.now()
    byWeeks = format(now - relativedelta(weeks=2))
    last_2weeks = df[df['date']>(byWeeks)]
    dic = last_2weeks.groupby('area').count().to_dict(orient='dict')
    dic = dic['__v']
    last_month_list = []
    for key in dic.keys():  
        last_month_list.append({'count':dic[key] ,'area':key} )
   
    data = {'data' :last_month_list}
    return JsonResponse(data)





def getLastWeek(request):
    df = pd.read_csv('userData.csv')
    date = df['_id'].apply(lambda x : ObjectId(x).generation_time)
    df['date'] = date
    now = datetime.now()
    byWeek = format (now - relativedelta(weeks=1))
    last_week = df[df['date']>(byWeek)]
    dic = last_week.groupby('area').count().to_dict(orient='dict')
    dic = dic['__v']
    last_week_list = []
    for key in dic.keys():  
        last_week_list.append({'count':dic[key] ,'area':key} )
    data = {'data' :last_week_list}
    return JsonResponse(data)




def getToday(request):
    df = pd.read_csv('userData.csv')
    date = df['_id'].apply(lambda x : ObjectId(x).generation_time)
    df['date'] = date
    now = datetime.now()
    byDay = format(now.date() ) 
    today= df[df['date']>(byDay)]
    dic = today.groupby('area').count().to_dict(orient='dict')
    dic = dic['__v']
    today_list = []
    for key in dic.keys():  
        today_list.append({'count':dic[key] ,'area':key} )
   
    data = {'data' :today_list}
    return JsonResponse(data)



def MinMax(request):
    df = pd.read_csv('userData.csv')
    dic = df.groupby('area').count().to_dict(orient='dict')
    dic = dic['__v']
    area=[]
    all_counts=[]
    for key in dic.keys():
        area.append(key )
        all_counts.append(dic[key])
    all_counts = np.array(all_counts)
    plot_div = plot([Bar(x=area, y=all_counts,
                        name='test',
                        opacity=0.8, marker_color='blue')],
               output_type='div')
    return render(request, "MinMax.html", context={'plot_div': plot_div})






def lastMonth(request):
    df = pd.read_csv('userData.csv')
    date = df['_id'].apply(lambda x : ObjectId(x).generation_time)
    df['date'] = date
    now = datetime.now()
    byMonth = format (now - relativedelta(months=1))
    last_month = df[df['date']>(byMonth)]
    dic = last_month.groupby('area').count().to_dict(orient='dict')
    dic = dic['__v']
    all_counts = []
    area =[]
    for key in dic.keys():
        all_counts.append(dic[key]) 
        area.append(key) 
    plot_div = plot([Bar(x=area, y=all_counts,
                         name='test',
                        opacity=0.8, marker_color='blue')],
               output_type='div')
    return render(request, "lastMonth.html", context={'plot_div': plot_div})




def last2Weeks(request):
    df = pd.read_csv('userData.csv')
    date = df['_id'].apply(lambda x : ObjectId(x).generation_time)
    df['date'] = date
    now = datetime.now()
    by2Weeks = format (now - relativedelta(weeks=2))
    last_2weeks = df[df['date']>(by2Weeks)]
    dic = last_2weeks.groupby('area').count().to_dict(orient='dict')
    dic = dic['__v']
    all_counts = []
    area =[]
    for key in dic.keys():
        all_counts.append(dic[key]) 
        area.append(key) 
    plot_div = plot([Bar(x=area, y=all_counts,
                         name='test',
                        opacity=0.8, marker_color='blue')],
               output_type='div')
    return render(request, "last2Weeks.html", context={'plot_div': plot_div})
  

def lastWeek(request):
    df = pd.read_csv('userData.csv')
    date = df['_id'].apply(lambda x : ObjectId(x).generation_time)
    df['date'] = date
    now = datetime.now()
    byWeek = format (now - relativedelta(weeks=1))
    last_week = df[df['date']>(byWeek)]
    dic = last_week.groupby('area').count().to_dict(orient='dict')
    dic = dic['__v']
    all_counts = []
    area =[]
    for key in dic.keys():
        all_counts.append(dic[key]) 
        area.append(key) 
    plot_div = plot([Bar(x=area, y=all_counts,
                        name='test',
                        opacity=0.8, marker_color='blue')],
               output_type='div')
    return render(request, "lastWeek.html", context={'plot_div': plot_div})
  

def Today(request):
    df = pd.read_csv('userData.csv')
    date = df['_id'].apply(lambda x : ObjectId(x).generation_time)
    df['date'] = date
    now = datetime.now()
    byDay = format(now.date() ) 
    today = df[df['date']>(byDay)]
    dic = today.groupby('area').count().to_dict(orient='dict')
    dic = dic['__v']
    all_counts = []
    area =[]
    for key in dic.keys():
        all_counts.append(dic[key]) 
        area.append(key) 
    plot_div = plot([Bar(x=area, y=all_counts,
                        name='test',
                        opacity=0.8, marker_color='blue')],
               output_type='div')
    return render(request, "today.html", context={'plot_div': plot_div})




def LastMonthHours(request):
    df = pd.read_csv('userData.csv')
    date = df['_id'].apply(lambda x : ObjectId(x).generation_time)
    df['date'] = date
    now = datetime.now()
    byMonth = format (now - relativedelta(months=1))
    last_month = df[df['date']>(byMonth)]
    month_hour=[]
    xx = np.arange(0,24)
    for i in range(24):
        month_hour.append(last_month.loc[last_month.date.dt.hour==i].shape[0])
    plot_div = plot([Bar(x=xx, y=month_hour,
                        name='test',
                        opacity=0.8, marker_color='blue')],
               output_type='div')
    return render(request, "LastMonthHours.html", context={'plot_div': plot_div})











def Last2WeeksHours(request):
    df = pd.read_csv('userData.csv')
    date = df['_id'].apply(lambda x : ObjectId(x).generation_time)
    df['date'] = date
    now = datetime.now()
    by2Weeks = format (now - relativedelta(weeks=2))
    last_2weeks = df[df['date']>(by2Weeks)]
    month_hour=[]
    xx = np.arange(0,24)
    for i in range(24):
        month_hour.append(last_2weeks.loc[last_2weeks.date.dt.hour==i].shape[0])
    plot_div = plot([Bar(x=xx, y=month_hour,
                        name='test',
                        opacity=0.8, marker_color='blue')],
               output_type='div')
    return render(request, "Last2WeeksHours.html", context={'plot_div': plot_div})





def LastWeekHours(request):
    df = pd.read_csv('userData.csv')
    date = df['_id'].apply(lambda x : ObjectId(x).generation_time)
    df['date'] = date
    now = datetime.now()
    byWeek = format (now - relativedelta(weeks=1))
    last_week = df[df['date']>(byWeek)]
    month_hour=[]
    xx = np.arange(0,24)
    for i in range(24):
        month_hour.append(last_week.loc[last_week.date.dt.hour==i].shape[0])
    plot_div = plot([Bar(x=xx, y=month_hour,
                        name='test',
                        opacity=0.8, marker_color='blue')],
               output_type='div')
    return render(request, "LastWeekHours.html", context={'plot_div': plot_div})








def TodayHours(request):
    df = pd.read_csv('userData.csv')
    date = df['_id'].apply(lambda x : ObjectId(x).generation_time)
    df['date'] = date
    now = datetime.now()
    byDay = format(now.date() ) 
    today= df[df['date']>(byDay)]
    month_hour=[]
    xx = np.arange(0,24)
    for i in range(24):
        month_hour.append(today.loc[today.date.dt.hour==i].shape[0])
    plot_div = plot([Bar(x=xx, y=month_hour,
                        name='test',
                        opacity=0.8, marker_color='blue')],
               output_type='div')
    return render(request, "TodayHours.html", context={'plot_div': plot_div})